import type {
  Assistance,
  LearningMode,
  StoryCase,
  StoryEnding,
  StoryVariant,
} from './content-types';

export interface LearningEvent {
  knowledgeId: string;
  mode: LearningMode;
  result: number;
  assistance: Assistance;
  context: string;
  caseId: string;
  variantId: string;
  timestamp: string;
}

export interface StorySession {
  caseId: string;
  variantId: string;
  sceneId: string;
  dimensions: Record<string, number>;
  choiceHistory: { sceneId: string; choiceId: string; timestamp: string }[];
  assistanceByKnowledge: Record<string, Assistance>;
  startedAt: string;
  updatedAt: string;
  endingId: string | null;
}

const comparisons = {
  gte: (actual: number, expected: number) => actual >= expected,
  lte: (actual: number, expected: number) => actual <= expected,
  eq: (actual: number, expected: number) => actual === expected,
};

function variantFor(story: StoryCase, variantId: string): StoryVariant {
  const variant = story.variants.find((item) => item.id === variantId);
  if (!variant) throw new Error(`Unknown variant ${variantId} for case ${story.id}`);
  return variant;
}

function resolveIfNeeded(story: StoryCase, session: StorySession): StorySession {
  const variant = variantFor(story, session.variantId);
  const scene = variant.scenes[session.sceneId];
  if (!scene) throw new Error(`Unknown scene ${session.sceneId}`);
  if (scene.kind !== 'resolution') return session;
  const ending = resolveEnding(story, session);
  return { ...session, endingId: ending.id };
}

export function startStorySession(story: StoryCase, variantId: string, now: Date): StorySession {
  const variant = variantFor(story, variantId);
  const timestamp = now.toISOString();
  const session: StorySession = {
    caseId: story.id,
    variantId,
    sceneId: variant.startScene,
    dimensions: Object.fromEntries(story.dimensions.map((dimension) => [dimension, 0])),
    choiceHistory: [],
    assistanceByKnowledge: {},
    startedAt: timestamp,
    updatedAt: timestamp,
    endingId: null,
  };
  return resolveIfNeeded(story, session);
}

export function advanceNarrative(story: StoryCase, session: StorySession, now: Date): StorySession {
  const variant = variantFor(story, session.variantId);
  const scene = variant.scenes[session.sceneId];
  if (!scene) throw new Error(`Unknown scene ${session.sceneId}`);
  if (scene.kind !== 'narrative') throw new Error(`Scene ${session.sceneId} is not narrative`);
  const next = { ...session, sceneId: scene.next, updatedAt: now.toISOString() };
  return resolveIfNeeded(story, next);
}

export function markAssistance(
  session: StorySession,
  knowledgeIds: string[],
  assistance: Assistance,
  now: Date,
): StorySession {
  const assistanceByKnowledge = { ...session.assistanceByKnowledge };
  for (const id of knowledgeIds) assistanceByKnowledge[id] = assistance;
  return { ...session, assistanceByKnowledge, updatedAt: now.toISOString() };
}

export function choose(
  story: StoryCase,
  session: StorySession,
  choiceId: string,
  now: Date,
): { session: StorySession; learningEvents: LearningEvent[] } {
  if (session.endingId) throw new Error('Cannot choose after case ending');
  const variant = variantFor(story, session.variantId);
  const scene = variant.scenes[session.sceneId];
  if (!scene) throw new Error(`Unknown scene ${session.sceneId}`);
  if (scene.kind !== 'decision') throw new Error(`Scene ${session.sceneId} is not a decision`);
  const choice = scene.choices.find((item) => item.id === choiceId);
  if (!choice) throw new Error(`Unknown choice ${choiceId} at scene ${session.sceneId}`);

  const timestamp = now.toISOString();
  const dimensions = { ...session.dimensions };
  for (const [dimension, delta] of Object.entries(choice.effects)) {
    dimensions[dimension] = (dimensions[dimension] ?? 0) + delta;
  }

  const learningEvents: LearningEvent[] = choice.learning.map((signal) => ({
    knowledgeId: signal.knowledgeId,
    mode: signal.mode,
    result: signal.result,
    assistance: session.assistanceByKnowledge[signal.knowledgeId] ?? 'none',
    context: `${story.id}:${session.sceneId}:${choice.id}`,
    caseId: story.id,
    variantId: variant.id,
    timestamp,
  }));

  const next: StorySession = {
    ...session,
    sceneId: choice.next,
    dimensions,
    choiceHistory: [...session.choiceHistory, { sceneId: session.sceneId, choiceId, timestamp }],
    updatedAt: timestamp,
  };

  return { session: resolveIfNeeded(story, next), learningEvents };
}

export function resolveEnding(story: StoryCase, session: StorySession): StoryEnding {
  const variant = variantFor(story, session.variantId);
  const matched = variant.endings.find((ending) => !ending.default && ending.when.every((condition) => {
    const actual = session.dimensions[condition.dimension] ?? 0;
    return comparisons[condition.operator](actual, condition.value);
  }));
  if (matched) return matched;
  const fallback = variant.endings.find((ending) => ending.default);
  if (!fallback) throw new Error(`Variant ${variant.id} has no default ending`);
  return fallback;
}

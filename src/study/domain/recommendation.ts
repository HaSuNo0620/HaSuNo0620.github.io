import type { QualificationPack } from './content-types';
import type { LearningEvent } from './story-engine';
import { deriveKnowledgeState } from './learning-engine';

export interface VariantVisit {
  caseId: string;
  variantId: string;
  completedAt: string;
}

export interface RankedVariant {
  caseId: string;
  variantId: string;
  score: number;
}

const clamp01 = (value: number) => Math.max(0, Math.min(1, value));
const daysSince = (timestamp: string, now: Date) => Math.max(0, (now.getTime() - Date.parse(timestamp)) / 86_400_000);

export function rankVariants(
  pack: QualificationPack,
  events: LearningEvent[],
  visits: VariantVisit[],
  now: Date,
): RankedVariant[] {
  const eventsByKnowledge = new Map<string, LearningEvent[]>();
  for (const event of events) {
    const bucket = eventsByKnowledge.get(event.knowledgeId) ?? [];
    bucket.push(event);
    eventsByKnowledge.set(event.knowledgeId, bucket);
  }

  const priorityByKnowledge = new Map<string, number>();
  for (const node of pack.knowledge) {
    const state = deriveKnowledgeState(eventsByKnowledge.get(node.id) ?? [], now);
    const recencyGap = state.lastSeenAt ? clamp01(daysSince(state.lastSeenAt, now) / 30) : 1;
    const priority = 0.35 * (1 - state.apply)
      + 0.25 * (1 - state.discriminate)
      + 0.25 * (1 - state.recall)
      + 0.15 * recencyGap;
    priorityByKnowledge.set(node.id, priority);
  }

  const mostRecent = [...visits].sort((a, b) => Date.parse(b.completedAt) - Date.parse(a.completedAt))[0] ?? null;
  const ranked: RankedVariant[] = [];
  for (const story of pack.stories) {
    for (const variant of story.variants) {
      const scores = variant.targetKnowledge.map((id) => priorityByKnowledge.get(id) ?? 1);
      let score = scores.length === 0 ? 0 : scores.reduce((sum, value) => sum + value, 0) / scores.length;
      if (mostRecent?.caseId === story.id && mostRecent.variantId === variant.id) score -= 0.05;
      ranked.push({ caseId: story.id, variantId: variant.id, score });
    }
  }

  return ranked.sort((a, b) => b.score - a.score || a.caseId.localeCompare(b.caseId) || a.variantId.localeCompare(b.variantId));
}

import YAML from 'yaml';
import { z } from 'zod';
import type {
  HandbookEntry,
  KnowledgeNode,
  QualificationManifest,
  StoryCase,
} from './content-types';

const sourceRefSchema = z.object({
  id: z.string().min(1),
  label: z.string().min(1),
  url: z.string().url(),
  checkedAt: z.string().regex(/^\d{4}-\d{2}-\d{2}$/),
});

const manifestSchema = z.object({
  id: z.string().min(1),
  title: z.string().min(1),
  sections: z.array(z.object({ id: z.string().min(1), title: z.string().min(1) })).default([]),
  sources: z.array(sourceRefSchema).default([]),
});

const relationSchema = z.object({
  type: z.enum(['prerequisite', 'contrasts_with', 'example_of', 'derived_from', 'used_with']),
  target: z.string().min(1),
});

const knowledgeNodeSchema = z.object({
  id: z.string().min(1),
  title: z.string().min(1),
  statement: z.string().min(1),
  examConnection: z.string().nullable().default(null),
  section: z.string().min(1),
  tags: z.array(z.string()).default([]),
  relations: z.array(relationSchema).default([]),
  sources: z.array(z.string().min(1)).min(1),
});

const handbookEntrySchema = z.object({
  id: z.string().min(1),
  title: z.string().min(1),
  body: z.string().min(1),
  knowledgeIds: z.array(z.string().min(1)).default([]),
  sources: z.array(z.string().min(1)).min(1),
});

const learningSignalSchema = z.object({
  knowledgeId: z.string().min(1),
  mode: z.enum(['encounter', 'apply', 'discriminate', 'recall']),
  result: z.number().min(0).max(1),
});

const choiceSchema = z.object({
  id: z.string().min(1),
  text: z.string().min(1),
  next: z.string().min(1),
  effects: z.record(z.string(), z.number()).default({}),
  learning: z.array(learningSignalSchema).default([]),
});

const narrativeSceneSchema = z.object({
  kind: z.literal('narrative'),
  text: z.string().min(1),
  next: z.string().min(1),
});

const decisionSceneSchema = z.object({
  kind: z.literal('decision'),
  text: z.string().min(1),
  choices: z.array(choiceSchema).min(1),
});

const resolutionSceneSchema = z.object({
  kind: z.literal('resolution'),
  text: z.string().min(1),
});

const storySceneSchema = z.discriminatedUnion('kind', [
  narrativeSceneSchema,
  decisionSceneSchema,
  resolutionSceneSchema,
]);

const endingConditionSchema = z.object({
  dimension: z.string().min(1),
  operator: z.enum(['gte', 'lte', 'eq']),
  value: z.number(),
});

const endingSchema = z.object({
  id: z.string().min(1),
  text: z.string().min(1),
  when: z.array(endingConditionSchema).default([]),
  default: z.boolean().default(false),
});

const variantSchema = z.object({
  id: z.string().min(1),
  startScene: z.string().min(1),
  targetKnowledge: z.array(z.string().min(1)).default([]),
  scenes: z.record(z.string(), storySceneSchema),
  endings: z.array(endingSchema).min(1),
});

const storyCaseSchema = z.object({
  id: z.string().min(1),
  qualificationId: z.string().min(1),
  section: z.string().min(1),
  title: z.string().min(1),
  summary: z.string().min(1),
  durationMinutes: z.number().int().positive(),
  dimensions: z.array(z.string().min(1)).default([]),
  recommendedFirst: z.boolean().default(false),
  variants: z.array(variantSchema).min(1),
});

function parseYaml(raw: string): unknown {
  return YAML.parse(raw);
}

export function parseManifest(raw: string): QualificationManifest {
  return manifestSchema.parse(parseYaml(raw));
}

export function parseKnowledgeFile(raw: string): KnowledgeNode[] {
  const data = parseYaml(raw);
  const list = Array.isArray(data) ? data : (data as { knowledge?: unknown })?.knowledge;
  return z.array(knowledgeNodeSchema).parse(list);
}

export function parseHandbookFile(raw: string): HandbookEntry[] {
  const data = parseYaml(raw);
  const list = Array.isArray(data) ? data : (data as { entries?: unknown })?.entries;
  return z.array(handbookEntrySchema).parse(list);
}

export function parseStoryFile(raw: string): StoryCase {
  return storyCaseSchema.parse(parseYaml(raw));
}

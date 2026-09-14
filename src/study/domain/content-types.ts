export type LearningMode = 'encounter' | 'apply' | 'discriminate' | 'recall';
export type Assistance = 'none' | 'handbook' | 'hint' | 'other';
export type ComparisonOperator = 'gte' | 'lte' | 'eq';

export interface SourceRef {
  id: string;
  label: string;
  url: string;
  checkedAt: string;
}

export interface QualificationManifest {
  id: string;
  title: string;
  sections: { id: string; title: string }[];
  sources: SourceRef[];
}

export interface KnowledgeNode {
  id: string;
  title: string;
  statement: string;
  examConnection: string | null;
  section: string;
  tags: string[];
  relations: {
    type: 'prerequisite' | 'contrasts_with' | 'example_of' | 'derived_from' | 'used_with';
    target: string;
  }[];
  sources: string[];
}

export interface HandbookEntry {
  id: string;
  title: string;
  body: string;
  knowledgeIds: string[];
  sources: string[];
}

export interface LearningSignalDefinition {
  knowledgeId: string;
  mode: LearningMode;
  result: number;
}

export interface StoryChoice {
  id: string;
  text: string;
  next: string;
  effects: Record<string, number>;
  learning: LearningSignalDefinition[];
}

export type StoryScene =
  | { kind: 'narrative'; text: string; next: string }
  | { kind: 'decision'; text: string; choices: StoryChoice[] }
  | { kind: 'resolution'; text: string };

export interface EndingCondition {
  dimension: string;
  operator: ComparisonOperator;
  value: number;
}

export interface StoryEnding {
  id: string;
  text: string;
  when: EndingCondition[];
  default: boolean;
}

export interface StoryVariant {
  id: string;
  startScene: string;
  targetKnowledge: string[];
  scenes: Record<string, StoryScene>;
  endings: StoryEnding[];
}

export interface StoryCase {
  id: string;
  qualificationId: string;
  section: string;
  title: string;
  summary: string;
  durationMinutes: number;
  dimensions: string[];
  recommendedFirst: boolean;
  variants: StoryVariant[];
}

export interface QualificationPack {
  manifest: QualificationManifest;
  knowledge: KnowledgeNode[];
  handbook: HandbookEntry[];
  stories: StoryCase[];
}

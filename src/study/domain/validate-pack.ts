import type { LearningMode, QualificationPack, StoryScene } from './content-types';

export interface ValidationMessage {
  level: 'error' | 'warning';
  code: string;
  message: string;
  path?: string;
}

export interface CoverageEntry {
  knowledgeId: string;
  modes: LearningMode[];
  cases: string[];
}

export interface ValidationReport {
  errors: ValidationMessage[];
  warnings: ValidationMessage[];
  coverage: CoverageEntry[];
}

function targets(scene: StoryScene): string[] {
  if (scene.kind === 'narrative') return [scene.next];
  if (scene.kind === 'decision') return scene.choices.map((choice) => choice.next);
  return [];
}

function detectCycle(start: string, scenes: Record<string, StoryScene>): boolean {
  const visiting = new Set<string>();
  const visited = new Set<string>();

  const visit = (id: string): boolean => {
    if (visiting.has(id)) return true;
    if (visited.has(id) || !scenes[id]) return false;
    visiting.add(id);
    for (const next of targets(scenes[id])) {
      if (visit(next)) return true;
    }
    visiting.delete(id);
    visited.add(id);
    return false;
  };

  return visit(start);
}

export function validatePack(pack: QualificationPack): ValidationReport {
  const errors: ValidationMessage[] = [];
  const warnings: ValidationMessage[] = [];
  const knowledgeIds = new Set<string>();
  const sourceIds = new Set(pack.manifest.sources.map((source) => source.id));
  const coverageMap = new Map<string, { modes: Set<LearningMode>; cases: Set<string> }>();

  for (const node of pack.knowledge) {
    if (knowledgeIds.has(node.id)) {
      errors.push({ level: 'error', code: 'DUPLICATE_KNOWLEDGE_ID', message: `Duplicate knowledge id: ${node.id}` });
    }
    knowledgeIds.add(node.id);
    coverageMap.set(node.id, { modes: new Set(), cases: new Set() });
  }

  for (const node of pack.knowledge) {
    for (const source of node.sources) {
      if (!sourceIds.has(source)) {
        errors.push({ level: 'error', code: 'UNKNOWN_SOURCE_ID', message: `${node.id} references unknown source ${source}` });
      }
    }
    for (const relation of node.relations) {
      if (!knowledgeIds.has(relation.target)) {
        errors.push({ level: 'error', code: 'UNKNOWN_RELATION_TARGET', message: `${node.id} references unknown relation target ${relation.target}` });
      }
    }
  }

  for (const entry of pack.handbook) {
    for (const source of entry.sources) {
      if (!sourceIds.has(source)) {
        errors.push({ level: 'error', code: 'UNKNOWN_SOURCE_ID', message: `Handbook ${entry.id} references unknown source ${source}` });
      }
    }
    for (const id of entry.knowledgeIds) {
      if (!knowledgeIds.has(id)) {
        errors.push({ level: 'error', code: 'UNKNOWN_HANDBOOK_KNOWLEDGE_ID', message: `Handbook ${entry.id} references unknown knowledge ${id}` });
      }
    }
  }

  for (const story of pack.stories) {
    if (story.qualificationId !== pack.manifest.id) {
      errors.push({ level: 'error', code: 'QUALIFICATION_ID_MISMATCH', message: `${story.id} belongs to ${story.qualificationId}, expected ${pack.manifest.id}` });
    }
    if (story.variants.length < 2) {
      errors.push({ level: 'error', code: 'TOO_FEW_VARIANTS', message: `${story.id} must have at least two authored variants` });
    }

    for (const variant of story.variants) {
      const prefix = `${story.id}/${variant.id}`;
      const sceneIds = new Set(Object.keys(variant.scenes));
      if (!sceneIds.has(variant.startScene)) {
        errors.push({ level: 'error', code: 'INVALID_START_SCENE', message: `${prefix} start scene ${variant.startScene} does not exist` });
        continue;
      }

      for (const id of variant.targetKnowledge) {
        if (!knowledgeIds.has(id)) {
          errors.push({ level: 'error', code: 'UNKNOWN_KNOWLEDGE_ID', message: `${prefix} targets unknown knowledge ${id}` });
        }
      }

      const reachable = new Set<string>();
      const stack = [variant.startScene];
      while (stack.length) {
        const id = stack.pop()!;
        if (reachable.has(id) || !variant.scenes[id]) continue;
        reachable.add(id);
        for (const next of targets(variant.scenes[id])) stack.push(next);
      }

      for (const [sceneId, scene] of Object.entries(variant.scenes)) {
        for (const next of targets(scene)) {
          if (!sceneIds.has(next)) {
            errors.push({ level: 'error', code: 'UNKNOWN_SCENE_TARGET', message: `${prefix}/${sceneId} points to missing scene ${next}` });
          }
        }
        if (!reachable.has(sceneId)) {
          errors.push({ level: 'error', code: 'UNREACHABLE_SCENE', message: `${prefix}/${sceneId} is unreachable` });
        }
        if (scene.kind === 'decision') {
          for (const choice of scene.choices) {
            for (const signal of choice.learning) {
              if (!knowledgeIds.has(signal.knowledgeId)) {
                errors.push({ level: 'error', code: 'UNKNOWN_KNOWLEDGE_ID', message: `${prefix}/${sceneId}/${choice.id} references unknown knowledge ${signal.knowledgeId}` });
                continue;
              }
              const item = coverageMap.get(signal.knowledgeId)!;
              item.modes.add(signal.mode);
              item.cases.add(story.id);
            }
            for (const dimension of Object.keys(choice.effects)) {
              if (!story.dimensions.includes(dimension)) {
                errors.push({ level: 'error', code: 'UNKNOWN_DIMENSION', message: `${prefix}/${sceneId}/${choice.id} changes undeclared dimension ${dimension}` });
              }
            }
          }
        }
      }

      if (detectCycle(variant.startScene, variant.scenes)) {
        errors.push({ level: 'error', code: 'NON_TERMINATING_CYCLE', message: `${prefix} contains a reachable story cycle` });
      }

      const defaultCount = variant.endings.filter((ending) => ending.default).length;
      if (defaultCount !== 1) {
        errors.push({ level: 'error', code: 'INVALID_DEFAULT_ENDING_COUNT', message: `${prefix} must have exactly one default ending` });
      }
      for (const ending of variant.endings) {
        for (const condition of ending.when) {
          if (!story.dimensions.includes(condition.dimension)) {
            errors.push({ level: 'error', code: 'UNKNOWN_DIMENSION', message: `${prefix}/${ending.id} checks undeclared dimension ${condition.dimension}` });
          }
        }
      }
    }
  }

  const coverage: CoverageEntry[] = [...coverageMap.entries()].map(([knowledgeId, value]) => ({
    knowledgeId,
    modes: [...value.modes].sort(),
    cases: [...value.cases].sort(),
  }));

  for (const entry of coverage) {
    if (entry.modes.length === 0) {
      warnings.push({ level: 'warning', code: 'NO_STORY_COVERAGE', message: `${entry.knowledgeId} has no story coverage` });
    } else if (!entry.modes.some((mode) => mode === 'apply' || mode === 'discriminate')) {
      warnings.push({ level: 'warning', code: 'ENCOUNTER_ONLY_COVERAGE', message: `${entry.knowledgeId} is never applied or discriminated` });
    }
  }

  return { errors, warnings, coverage };
}

import type { QualificationPack, StoryScene } from './content-types';

export interface ValidationMessage {
  level: 'error' | 'warning'; code: string; message: string; path: string;
}
export interface CoverageRow { knowledgeId: string; encounter: number; apply: number; discriminate: number; recall: number }
export interface ValidationReport { errors: ValidationMessage[]; warnings: ValidationMessage[]; coverage: CoverageRow[] }

function targets(scene: StoryScene): string[] {
  if (scene.kind === 'narrative') return [scene.next];
  if (scene.kind === 'decision') return scene.choices.map((choice) => choice.next);
  return [];
}
function detectCycle(start: string, scenes: Record<string, StoryScene>): boolean {
  const visiting = new Set<string>(); const visited = new Set<string>();
  const visit = (id: string): boolean => {
    if (visiting.has(id)) return true;
    if (visited.has(id) || !scenes[id]) return false;
    visiting.add(id); for (const next of targets(scenes[id])) if (visit(next)) return true;
    visiting.delete(id); visited.add(id); return false;
  };
  return visit(start);
}
const validDate = (value: string) => /^\d{4}-\d{2}-\d{2}$/.test(value) && !Number.isNaN(Date.parse(`${value}T00:00:00Z`));

export function validatePack(pack: QualificationPack): ValidationReport {
  const errors: ValidationMessage[] = []; const warnings: ValidationMessage[] = [];
  const error = (code: string, message: string, path: string) => errors.push({ level: 'error', code, message, path });
  const warning = (code: string, message: string, path: string) => warnings.push({ level: 'warning', code, message, path });
  const sectionIds = new Set<string>();
  for (const section of pack.manifest.sections) { if (sectionIds.has(section.id)) error('DUPLICATE_SECTION_ID', `Duplicate section id: ${section.id}`, 'manifest.sections'); sectionIds.add(section.id); }
  const sourceIds = new Set<string>();
  for (const source of pack.manifest.sources) {
    if (sourceIds.has(source.id)) error('DUPLICATE_SOURCE_ID', `Duplicate source id: ${source.id}`, 'manifest.sources');
    sourceIds.add(source.id);
    if (!source.url.startsWith('https://')) error('INVALID_SOURCE_URL', `${source.id} must use HTTPS`, `manifest.sources.${source.id}.url`);
    if (!validDate(source.checkedAt)) error('INVALID_SOURCE_DATE', `${source.id} has invalid checkedAt`, `manifest.sources.${source.id}.checkedAt`);
  }
  const knowledgeIds = new Set<string>(); const coverage = new Map<string, CoverageRow>();
  for (const node of pack.knowledge) { if (knowledgeIds.has(node.id)) error('DUPLICATE_KNOWLEDGE_ID', `Duplicate knowledge id: ${node.id}`, `knowledge.${node.id}`); knowledgeIds.add(node.id); coverage.set(node.id, { knowledgeId: node.id, encounter: 0, apply: 0, discriminate: 0, recall: 0 }); }
  for (const node of pack.knowledge) {
    if (!sectionIds.has(node.section)) error('UNKNOWN_SECTION_ID', `${node.id} uses unknown section ${node.section}`, `knowledge.${node.id}.section`);
    if (node.sources.length === 0) error('MISSING_PROVENANCE', `${node.id} has no sources`, `knowledge.${node.id}.sources`);
    for (const source of node.sources) if (!sourceIds.has(source)) error('UNKNOWN_SOURCE_ID', `${node.id} references unknown source ${source}`, `knowledge.${node.id}.sources`);
    for (const relation of node.relations) if (!knowledgeIds.has(relation.target)) error('UNKNOWN_RELATION_TARGET', `${node.id} references unknown relation target ${relation.target}`, `knowledge.${node.id}.relations`);
  }
  for (const entry of pack.handbook) {
    if (entry.sources.length === 0) error('MISSING_PROVENANCE', `Handbook ${entry.id} has no sources`, `handbook.${entry.id}.sources`);
    for (const source of entry.sources) if (!sourceIds.has(source)) error('UNKNOWN_SOURCE_ID', `Handbook ${entry.id} references unknown source ${source}`, `handbook.${entry.id}.sources`);
    for (const id of entry.knowledgeIds) if (!knowledgeIds.has(id)) error('UNKNOWN_HANDBOOK_KNOWLEDGE_ID', `Handbook ${entry.id} references unknown knowledge ${id}`, `handbook.${entry.id}.knowledgeIds`);
  }
  for (const story of pack.stories) {
    if (story.qualificationId !== pack.manifest.id) error('QUALIFICATION_ID_MISMATCH', `${story.id} belongs to ${story.qualificationId}, expected ${pack.manifest.id}`, `stories.${story.id}.qualificationId`);
    if (!sectionIds.has(story.section)) error('UNKNOWN_SECTION_ID', `${story.id} uses unknown section ${story.section}`, `stories.${story.id}.section`);
    if (story.variants.length < 2) error('TOO_FEW_VARIANTS', `${story.id} must have at least two authored variants`, `stories.${story.id}.variants`);
    for (const variant of story.variants) {
      const prefix = `stories.${story.id}.${variant.id}`; const sceneIds = new Set(Object.keys(variant.scenes));
      if (!sceneIds.has(variant.startScene)) { error('INVALID_START_SCENE', `${story.id}/${variant.id} start scene ${variant.startScene} does not exist`, `${prefix}.startScene`); continue; }
      for (const id of variant.targetKnowledge) if (!knowledgeIds.has(id)) error('UNKNOWN_KNOWLEDGE_ID', `${story.id}/${variant.id} targets unknown knowledge ${id}`, `${prefix}.targetKnowledge`);
      const reachable = new Set<string>(); const stack = [variant.startScene];
      while (stack.length) { const id = stack.pop()!; if (reachable.has(id) || !variant.scenes[id]) continue; reachable.add(id); for (const next of targets(variant.scenes[id])) stack.push(next); }
      for (const [sceneId, scene] of Object.entries(variant.scenes)) {
        for (const next of targets(scene)) if (!sceneIds.has(next)) error('UNKNOWN_SCENE_TARGET', `${story.id}/${variant.id}/${sceneId} points to missing scene ${next}`, `${prefix}.scenes.${sceneId}`);
        if (!reachable.has(sceneId)) error('UNREACHABLE_SCENE', `${story.id}/${variant.id}/${sceneId} is unreachable`, `${prefix}.scenes.${sceneId}`);
        if (scene.kind === 'decision') for (const choice of scene.choices) {
          for (const signal of choice.learning) {
            if (!knowledgeIds.has(signal.knowledgeId)) error('UNKNOWN_KNOWLEDGE_ID', `${story.id}/${variant.id}/${sceneId}/${choice.id} references unknown knowledge ${signal.knowledgeId}`, `${prefix}.scenes.${sceneId}.${choice.id}.learning`);
            else coverage.get(signal.knowledgeId)![signal.mode] += 1;
          }
          for (const dimension of Object.keys(choice.effects)) if (!story.dimensions.includes(dimension)) error('UNKNOWN_DIMENSION', `${story.id}/${variant.id}/${sceneId}/${choice.id} changes undeclared dimension ${dimension}`, `${prefix}.scenes.${sceneId}.${choice.id}.effects`);
        }
      }
      if (detectCycle(variant.startScene, variant.scenes)) error('NON_TERMINATING_CYCLE', `${story.id}/${variant.id} contains a reachable story cycle`, prefix);
      if (variant.endings.filter((ending) => ending.default).length !== 1) error('INVALID_DEFAULT_ENDING_COUNT', `${story.id}/${variant.id} must have exactly one default ending`, `${prefix}.endings`);
      for (const ending of variant.endings) for (const condition of ending.when) if (!story.dimensions.includes(condition.dimension)) error('UNKNOWN_DIMENSION', `${story.id}/${variant.id}/${ending.id} checks undeclared dimension ${condition.dimension}`, `${prefix}.endings.${ending.id}`);
    }
  }
  const coverageRows = [...coverage.values()].sort((a, b) => a.knowledgeId.localeCompare(b.knowledgeId));
  for (const row of coverageRows) { const total = row.encounter + row.apply + row.discriminate + row.recall; if (total === 0) warning('NO_STORY_COVERAGE', `${row.knowledgeId} has no story coverage`, `knowledge.${row.knowledgeId}`); else if (row.apply === 0 && row.discriminate === 0) warning('ENCOUNTER_ONLY_COVERAGE', `${row.knowledgeId} is never applied or discriminated`, `knowledge.${row.knowledgeId}`); }
  return { errors, warnings, coverage: coverageRows };
}

import { describe, expect, it } from 'vitest';
import type { QualificationPack } from './content-types';
import { validatePack } from './validate-pack';

function basePack(): QualificationPack {
  return {
    manifest: {
      id: 'hazardous-materials',
      title: '危険物取扱者',
      sections: [{ id: 'otsu4-seisho', title: '性質・火災予防・消火' }],
      sources: [{ id: 'official', label: 'Official', url: 'https://example.com', checkedAt: '2026-09-14' }],
    },
    knowledge: [{
      id: 'k1', title: 'K1', statement: 'fact', examConnection: null, section: 'otsu4-seisho', tags: [], relations: [], sources: ['official'],
    }],
    handbook: [],
    stories: [{
      id: 'case', qualificationId: 'hazardous-materials', section: 'otsu4-seisho', title: 'Case', summary: 'summary', durationMinutes: 10,
      dimensions: ['safe'], recommendedFirst: true,
      variants: ['v1', 'v2'].map((id) => ({
        id, startScene: 'start', targetKnowledge: ['k1'],
        scenes: {
          start: { kind: 'decision' as const, text: 'choose', choices: [{ id: 'c', text: 'go', next: 'end', effects: { safe: 1 }, learning: [{ knowledgeId: 'k1', mode: 'apply' as const, result: 1 }] }] },
          end: { kind: 'resolution' as const, text: 'done' },
        },
        endings: [{ id: 'ok', text: 'ok', when: [], default: true }],
      })),
    }],
  };
}

describe('validatePack', () => {
  it('accepts a structurally valid pack', () => {
    const report = validatePack(basePack());
    expect(report.errors).toEqual([]);
    expect(report.coverage[0].modes).toContain('apply');
  });

  it('reports unknown knowledge and scene targets', () => {
    const pack = basePack();
    pack.stories[0].variants[0].scenes.start = {
      kind: 'decision', text: 'broken', choices: [{ id: 'c', text: 'go', next: 'missing', effects: {}, learning: [{ knowledgeId: 'missing', mode: 'apply', result: 1 }] }],
    };
    const report = validatePack(pack);
    expect(report.errors).toContainEqual(expect.objectContaining({ code: 'UNKNOWN_KNOWLEDGE_ID' }));
    expect(report.errors).toContainEqual(expect.objectContaining({ code: 'UNKNOWN_SCENE_TARGET' }));
  });

  it('reports unreachable scenes and invalid default endings', () => {
    const pack = basePack();
    pack.stories[0].variants[0].scenes.orphan = { kind: 'resolution', text: 'orphan' };
    pack.stories[0].variants[0].endings[0].default = false;
    const report = validatePack(pack);
    expect(report.errors).toContainEqual(expect.objectContaining({ code: 'UNREACHABLE_SCENE' }));
    expect(report.errors).toContainEqual(expect.objectContaining({ code: 'INVALID_DEFAULT_ENDING_COUNT' }));
  });

  it('warns when a knowledge node has no story coverage', () => {
    const pack = basePack();
    pack.knowledge.push({ id: 'k2', title: 'K2', statement: 'fact', examConnection: null, section: 'otsu4-seisho', tags: [], relations: [], sources: ['official'] });
    const report = validatePack(pack);
    expect(report.warnings).toContainEqual(expect.objectContaining({ code: 'NO_STORY_COVERAGE' }));
  });
});

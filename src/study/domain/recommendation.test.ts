import { describe, expect, it } from 'vitest';
import type { QualificationPack } from './content-types';
import type { LearningEvent } from './story-engine';
import { rankVariants } from './recommendation';

const pack: QualificationPack = {
  manifest: { id: 'q', title: 'Q', sections: [{ id: 's', title: 'S' }], sources: [] },
  knowledge: [
    { id: 'weak', title: 'weak', statement: 'weak', examConnection: null, section: 's', tags: [], relations: [], sources: [] },
    { id: 'strong', title: 'strong', statement: 'strong', examConnection: null, section: 's', tags: [], relations: [], sources: [] },
  ],
  handbook: [],
  stories: [
    { id: 'a', qualificationId: 'q', section: 's', title: 'A', summary: 'A', durationMinutes: 10, dimensions: [], recommendedFirst: false, variants: [{ id: 'weak-v', startScene: 'r', targetKnowledge: ['weak'], scenes: { r: { kind: 'resolution', text: 'end' } }, endings: [{ id: 'e', text: 'end', when: [], default: true }] }] },
    { id: 'b', qualificationId: 'q', section: 's', title: 'B', summary: 'B', durationMinutes: 10, dimensions: [], recommendedFirst: false, variants: [{ id: 'strong-v', startScene: 'r', targetKnowledge: ['strong'], scenes: { r: { kind: 'resolution', text: 'end' } }, endings: [{ id: 'e', text: 'end', when: [], default: true }] }] },
  ],
};

const strongEvents: LearningEvent[] = ['apply', 'discriminate', 'recall'].map((mode) => ({
  knowledgeId: 'strong', mode: mode as 'apply' | 'discriminate' | 'recall', result: 1, assistance: 'none', context: 'test', caseId: 'b', variantId: 'strong-v', timestamp: '2026-09-14T00:00:00Z',
}));

describe('rankVariants', () => {
  it('ranks a weak target above a strong target', () => {
    const result = rankVariants(pack, strongEvents, [], new Date('2026-09-14T00:00:00Z'));
    expect(result[0]).toMatchObject({ caseId: 'a', variantId: 'weak-v' });
  });

  it('breaks equal scores deterministically by case then variant', () => {
    const result = rankVariants(pack, [], [], new Date('2026-09-14T00:00:00Z'));
    expect(result.map((item) => item.caseId)).toEqual(['a', 'b']);
  });
});

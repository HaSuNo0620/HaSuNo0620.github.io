import { describe, expect, it } from 'vitest';
import type { Assistance, LearningMode } from './content-types';
import type { LearningEvent } from './story-engine';
import { deriveKnowledgeState } from './learning-engine';

const event = (mode: LearningMode, result: number, assistance: Assistance, timestamp: string): LearningEvent => ({
  knowledgeId: 'k1', mode, result, assistance, timestamp, context: 'test', caseId: 'case', variantId: 'v1',
});

describe('deriveKnowledgeState', () => {
  const now = new Date('2026-09-14T00:00:00Z');

  it('weights unaided success above handbook-assisted success', () => {
    const state = deriveKnowledgeState([
      event('apply', 1, 'handbook', '2026-09-13T00:00:00Z'),
      event('apply', 1, 'none', '2026-09-14T00:00:00Z'),
    ], now);
    expect(state.apply).toBeGreaterThan(0.75);
    expect(state.helpDependence).toBe(0.5);
  });

  it('returns finite zeros for empty history', () => {
    const state = deriveKnowledgeState([], now);
    expect(state).toMatchObject({ encounter: 0, apply: 0, discriminate: 0, recall: 0, helpDependence: 0, eventCount: 0, lastSeenAt: null });
    expect(Object.values(state).filter((value) => typeof value === 'number').every(Number.isFinite)).toBe(true);
  });

  it('decays fallback recall with elapsed time', () => {
    const fresh = deriveKnowledgeState([event('apply', 1, 'none', '2026-09-14T00:00:00Z')], now);
    const old = deriveKnowledgeState([event('apply', 1, 'none', '2026-06-14T00:00:00Z')], now);
    expect(fresh.recall).toBeGreaterThan(old.recall);
  });
});

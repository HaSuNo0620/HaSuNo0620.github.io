import { deleteDB, openDB } from 'idb';
import { afterEach, describe, expect, it } from 'vitest';
import type { LearningEvent, StorySession } from '../domain/story-engine';
import { createStudyRepository } from './repository';

const learningEvent: LearningEvent = {
  knowledgeId: 'k1', mode: 'apply', result: 1, assistance: 'none', context: 'test', caseId: 'case', variantId: 'v1', timestamp: '2026-09-14T00:00:00.000Z',
};
const session: StorySession = {
  caseId: 'case', variantId: 'v1', sceneId: 'scene', dimensions: {}, choiceHistory: [], assistanceByKnowledge: {}, startedAt: '2026-09-14T00:00:00.000Z', updatedAt: '2026-09-14T00:00:00.000Z', endingId: null,
};

afterEach(async () => {
  await deleteDB('qualification-study');
});

describe('study repository', () => {
  it('persists events, active sessions, and atomic completion', async () => {
    const bootstrap = await createStudyRepository();
    expect(bootstrap.persistent).toBe(true);
    const repo = bootstrap.repository;
    await repo.appendLearningEvents([learningEvent]);
    expect(await repo.listLearningEvents()).toHaveLength(1);
    await repo.saveActiveSession(session);
    expect(await repo.loadActiveSession(session.caseId)).toMatchObject({ variantId: 'v1' });
    await repo.completeSession(session, 'controlled', new Date('2026-09-14T00:10:00Z'));
    expect(await repo.loadActiveSession(session.caseId)).toBeNull();
    expect(await repo.listCaseHistory()).toHaveLength(1);
  });

  it('preserves data from a future schema as a recovery snapshot', async () => {
    const future = await openDB('qualification-study', 2, {
      upgrade(db) {
        db.createObjectStore('learning-events', { keyPath: 'id', autoIncrement: true });
        db.createObjectStore('case-history', { keyPath: 'id' });
        db.createObjectStore('active-sessions', { keyPath: 'caseId' });
      },
    });
    await future.add('learning-events', { ...learningEvent });
    future.close();

    const bootstrap = await createStudyRepository();
    expect(bootstrap.warning).toBe('incompatible-schema');
    expect(bootstrap.recoverySnapshot?.learningEvents).toHaveLength(1);

    const reopened = await openDB('qualification-study');
    expect(reopened.version).toBe(2);
    reopened.close();
  });
});

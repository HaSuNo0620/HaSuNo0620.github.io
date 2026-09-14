import { openDB, type DBSchema, type IDBPDatabase } from 'idb';
import type { LearningEvent, StorySession } from '../domain/story-engine';
import { MemoryStudyRepository } from './memory-repository';

const DB_NAME = 'qualification-study';
const DB_VERSION = 1;

export interface CaseHistoryEntry {
  id: string;
  caseId: string;
  variantId: string;
  endingId: string;
  startedAt: string;
  completedAt: string;
  choiceHistory: StorySession['choiceHistory'];
}

export interface StudySnapshot {
  schemaVersion: number;
  learningEvents: LearningEvent[];
  caseHistory: CaseHistoryEntry[];
  activeSessions: StorySession[];
}

export interface StudyRepository {
  appendLearningEvents(events: LearningEvent[]): Promise<void>;
  listLearningEvents(): Promise<LearningEvent[]>;
  saveActiveSession(session: StorySession): Promise<void>;
  loadActiveSession(caseId: string): Promise<StorySession | null>;
  listActiveSessions(): Promise<StorySession[]>;
  completeSession(session: StorySession, endingId: string, completedAt: Date): Promise<void>;
  listCaseHistory(): Promise<CaseHistoryEntry[]>;
  exportSnapshot(): Promise<StudySnapshot>;
}

export interface RepositoryBootstrap {
  repository: StudyRepository;
  persistent: boolean;
  warning: 'none' | 'unavailable' | 'incompatible-schema';
  recoverySnapshot: StudySnapshot | null;
}

interface StudyDb extends DBSchema {
  'learning-events': { key: number; value: LearningEvent & { id?: number }; autoIncrement: true };
  'case-history': { key: string; value: CaseHistoryEntry };
  'active-sessions': { key: string; value: StorySession };
  settings: { key: string; value: { key: string; value: unknown } };
}

class IndexedDbStudyRepository implements StudyRepository {
  constructor(private readonly db: IDBPDatabase<StudyDb>) {}

  async appendLearningEvents(events: LearningEvent[]): Promise<void> {
    const tx = this.db.transaction('learning-events', 'readwrite');
    for (const event of events) await tx.store.add({ ...event });
    await tx.done;
  }

  async listLearningEvents(): Promise<LearningEvent[]> {
    const values = await this.db.getAll('learning-events');
    return values.map(({ id: _id, ...event }) => event);
  }

  async saveActiveSession(session: StorySession): Promise<void> {
    await this.db.put('active-sessions', structuredClone(session));
  }

  async loadActiveSession(caseId: string): Promise<StorySession | null> {
    return (await this.db.get('active-sessions', caseId)) ?? null;
  }

  async listActiveSessions(): Promise<StorySession[]> {
    return this.db.getAll('active-sessions');
  }

  async completeSession(session: StorySession, endingId: string, completedAt: Date): Promise<void> {
    const completedAtIso = completedAt.toISOString();
    const entry: CaseHistoryEntry = {
      id: `${session.caseId}:${session.variantId}:${completedAtIso}`,
      caseId: session.caseId,
      variantId: session.variantId,
      endingId,
      startedAt: session.startedAt,
      completedAt: completedAtIso,
      choiceHistory: structuredClone(session.choiceHistory),
    };
    const tx = this.db.transaction(['case-history', 'active-sessions'], 'readwrite');
    await tx.objectStore('case-history').put(entry);
    await tx.objectStore('active-sessions').delete(session.caseId);
    await tx.done;
  }

  async listCaseHistory(): Promise<CaseHistoryEntry[]> {
    return this.db.getAll('case-history');
  }

  async exportSnapshot(): Promise<StudySnapshot> {
    return {
      schemaVersion: DB_VERSION,
      learningEvents: await this.listLearningEvents(),
      caseHistory: await this.listCaseHistory(),
      activeSessions: await this.listActiveSessions(),
    };
  }
}

async function openVersion1(): Promise<IDBPDatabase<StudyDb>> {
  return openDB<StudyDb>(DB_NAME, DB_VERSION, {
    upgrade(db) {
      if (!db.objectStoreNames.contains('learning-events')) db.createObjectStore('learning-events', { keyPath: 'id', autoIncrement: true });
      if (!db.objectStoreNames.contains('case-history')) db.createObjectStore('case-history', { keyPath: 'id' });
      if (!db.objectStoreNames.contains('active-sessions')) db.createObjectStore('active-sessions', { keyPath: 'caseId' });
      if (!db.objectStoreNames.contains('settings')) db.createObjectStore('settings', { keyPath: 'key' });
    },
  }).then(async (db) => {
    await db.put('settings', { key: 'schema-version', value: DB_VERSION });
    return db;
  });
}

async function recoverFutureDatabase(): Promise<StudySnapshot> {
  const db = await openDB(DB_NAME);
  try {
    const learningEvents = db.objectStoreNames.contains('learning-events')
      ? (await db.getAll('learning-events')).map((value: LearningEvent & { id?: number }) => {
        const { id: _id, ...event } = value;
        return event;
      })
      : [];
    const caseHistory = db.objectStoreNames.contains('case-history') ? await db.getAll('case-history') as CaseHistoryEntry[] : [];
    const activeSessions = db.objectStoreNames.contains('active-sessions') ? await db.getAll('active-sessions') as StorySession[] : [];
    return { schemaVersion: db.version, learningEvents, caseHistory, activeSessions };
  } finally {
    db.close();
  }
}

export async function createStudyRepository(): Promise<RepositoryBootstrap> {
  try {
    const db = await openVersion1();
    return { repository: new IndexedDbStudyRepository(db), persistent: true, warning: 'none', recoverySnapshot: null };
  } catch (error) {
    if (error instanceof DOMException && error.name === 'VersionError') {
      try {
        const recoverySnapshot = await recoverFutureDatabase();
        return { repository: new MemoryStudyRepository(), persistent: false, warning: 'incompatible-schema', recoverySnapshot };
      } catch {
        return { repository: new MemoryStudyRepository(), persistent: false, warning: 'incompatible-schema', recoverySnapshot: null };
      }
    }
    return { repository: new MemoryStudyRepository(), persistent: false, warning: 'unavailable', recoverySnapshot: null };
  }
}

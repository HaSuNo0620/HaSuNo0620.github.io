import type { LearningEvent, StorySession } from '../domain/story-engine';
import type { CaseHistoryEntry, StudyRepository, StudySnapshot } from './repository';

export class MemoryStudyRepository implements StudyRepository {
  private learningEvents: LearningEvent[] = [];
  private caseHistory: CaseHistoryEntry[] = [];
  private activeSessions = new Map<string, StorySession>();

  async appendLearningEvents(events: LearningEvent[]): Promise<void> {
    this.learningEvents.push(...events.map((event) => ({ ...event })));
  }

  async listLearningEvents(): Promise<LearningEvent[]> {
    return this.learningEvents.map((event) => ({ ...event }));
  }

  async saveActiveSession(session: StorySession): Promise<void> {
    this.activeSessions.set(session.caseId, structuredClone(session));
  }

  async loadActiveSession(caseId: string): Promise<StorySession | null> {
    const session = this.activeSessions.get(caseId);
    return session ? structuredClone(session) : null;
  }

  async listActiveSessions(): Promise<StorySession[]> {
    return [...this.activeSessions.values()].map((session) => structuredClone(session));
  }

  async completeSession(session: StorySession, endingId: string, completedAt: Date): Promise<void> {
    const completedAtIso = completedAt.toISOString();
    this.caseHistory.push({
      id: `${session.caseId}:${session.variantId}:${completedAtIso}`,
      caseId: session.caseId,
      variantId: session.variantId,
      endingId,
      startedAt: session.startedAt,
      completedAt: completedAtIso,
      choiceHistory: structuredClone(session.choiceHistory),
    });
    this.activeSessions.delete(session.caseId);
  }

  async listCaseHistory(): Promise<CaseHistoryEntry[]> {
    return this.caseHistory.map((entry) => structuredClone(entry));
  }

  async exportSnapshot(): Promise<StudySnapshot> {
    return {
      schemaVersion: 1,
      learningEvents: await this.listLearningEvents(),
      caseHistory: await this.listCaseHistory(),
      activeSessions: await this.listActiveSessions(),
    };
  }
}

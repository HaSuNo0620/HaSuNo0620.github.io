import { useEffect, useMemo, useState } from 'react';
import { loadContentPacks } from '../content/load-content';
import type { QualificationPack, StoryCase } from '../domain/content-types';
import { startStorySession, type LearningEvent, type StorySession } from '../domain/story-engine';
import { createStudyRepository, type CaseHistoryEntry, type RepositoryBootstrap, type StudyRepository } from '../storage/repository';
import CaseLibrary from './CaseLibrary';
import Debrief from './Debrief';
import KnowledgeView from './KnowledgeView';
import QualificationPicker from './QualificationPicker';
import StorageWarning from './StorageWarning';
import StoryPlayer from './StoryPlayer';

const packs = loadContentPacks();

type ScreenState =
  | { screen: 'qualifications' }
  | { screen: 'library'; qualificationId: string }
  | { screen: 'story'; qualificationId: string; caseId: string; session: StorySession }
  | { screen: 'debrief'; qualificationId: string; caseId: string; session: StorySession }
  | { screen: 'knowledge'; qualificationId: string };

export default function StudyApp() {
  const [screen, setScreen] = useState<ScreenState>({ screen: 'qualifications' });
  const [bootstrap, setBootstrap] = useState<RepositoryBootstrap | null>(null);
  const [repository, setRepository] = useState<StudyRepository | null>(null);
  const [events, setEvents] = useState<LearningEvent[]>([]);
  const [history, setHistory] = useState<CaseHistoryEntry[]>([]);
  const [activeSessions, setActiveSessions] = useState<StorySession[]>([]);

  useEffect(() => {
    let cancelled = false;
    void createStudyRepository().then(async (result) => {
      const [loadedEvents, loadedHistory, loadedSessions] = await Promise.all([result.repository.listLearningEvents(), result.repository.listCaseHistory(), result.repository.listActiveSessions()]);
      if (cancelled) return;
      setBootstrap(result); setRepository(result.repository); setEvents(loadedEvents); setHistory(loadedHistory); setActiveSessions(loadedSessions);
    });
    return () => { cancelled = true; };
  }, []);

  const currentPack = useMemo<QualificationPack | null>(() => screen.screen === 'qualifications' ? null : packs.find((pack) => pack.manifest.id === screen.qualificationId) ?? null, [screen]);
  const replaceActiveSession = (session: StorySession) => setActiveSessions((current) => [...current.filter((item) => item.caseId !== session.caseId), session]);

  const startCase = async (story: StoryCase, variantId: string) => {
    if (!currentPack || !repository || !variantId) return;
    const session = startStorySession(story, variantId, new Date());
    await repository.saveActiveSession(session); replaceActiveSession(session);
    setScreen({ screen: 'story', qualificationId: currentPack.manifest.id, caseId: story.id, session });
  };
  const resumeCase = (story: StoryCase, session: StorySession) => { if (currentPack) setScreen({ screen: 'story', qualificationId: currentPack.manifest.id, caseId: story.id, session }); };
  const storyForScreen = screen.screen === 'story' || screen.screen === 'debrief' ? currentPack?.stories.find((story) => story.id === screen.caseId) ?? null : null;

  const finishCase = async (session: StorySession, story: StoryCase) => {
    if (!repository || !currentPack || !session.endingId) return;
    await repository.completeSession(session, session.endingId, new Date());
    const [nextEvents, nextHistory, nextActive] = await Promise.all([repository.listLearningEvents(), repository.listCaseHistory(), repository.listActiveSessions()]);
    setEvents(nextEvents); setHistory(nextHistory); setActiveSessions(nextActive);
    setScreen({ screen: 'debrief', qualificationId: currentPack.manifest.id, caseId: story.id, session });
  };

  return (
    <div className="study-shell">
      <header className="study-hero"><p className="study-eyebrow">study / cases</p><h1>資格学習</h1><p>問題を一つずつ消費する代わりに、状況を読み、判断し、その結果から概念をつなぐ。</p></header>
      {bootstrap && <StorageWarning bootstrap={bootstrap} />}{!bootstrap && <p className="study-muted" role="status">学習履歴を読み込んでいます…</p>}
      {bootstrap && screen.screen === 'qualifications' && <QualificationPicker packs={packs} onSelect={(qualificationId) => setScreen({ screen: 'library', qualificationId })} />}
      {bootstrap && screen.screen === 'library' && currentPack && <CaseLibrary pack={currentPack} events={events} history={history} activeSessions={activeSessions} onStart={(story, variantId) => { void startCase(story, variantId); }} onResume={resumeCase} onKnowledge={() => setScreen({ screen: 'knowledge', qualificationId: currentPack.manifest.id })} onBack={() => setScreen({ screen: 'qualifications' })} />}
      {bootstrap && screen.screen === 'story' && currentPack && storyForScreen && repository && <StoryPlayer story={storyForScreen} session={screen.session} handbook={currentPack.handbook} repository={repository} onSessionChange={(session) => { replaceActiveSession(session); setScreen({ screen: 'story', qualificationId: currentPack.manifest.id, caseId: storyForScreen.id, session }); }} onLearningEvents={(newEvents) => { if (newEvents.length > 0) setEvents((current) => [...current, ...newEvents]); }} onReview={(session) => { void finishCase(session, storyForScreen); }} onBack={() => setScreen({ screen: 'library', qualificationId: currentPack.manifest.id })} />}
      {bootstrap && screen.screen === 'debrief' && currentPack && storyForScreen && <Debrief pack={currentPack} story={storyForScreen} session={screen.session} onDone={() => setScreen({ screen: 'library', qualificationId: currentPack.manifest.id })} />}
      {bootstrap && screen.screen === 'knowledge' && currentPack && <KnowledgeView pack={currentPack} events={events} onBack={() => setScreen({ screen: 'library', qualificationId: currentPack.manifest.id })} />}
    </div>
  );
}

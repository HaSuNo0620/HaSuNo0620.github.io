import { useEffect, useMemo, useState } from 'react';
import { loadContentPacks } from '../content/load-content';
import type { QualificationPack, StoryCase } from '../domain/content-types';
import { startStorySession, type LearningEvent, type StorySession } from '../domain/story-engine';
import { createStudyRepository, type CaseHistoryEntry, type RepositoryBootstrap, type StudyRepository } from '../storage/repository';
import CaseLibrary from './CaseLibrary';
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
      const [loadedEvents, loadedHistory, loadedSessions] = await Promise.all([
        result.repository.listLearningEvents(), result.repository.listCaseHistory(), result.repository.listActiveSessions(),
      ]);
      if (cancelled) return;
      setBootstrap(result); setRepository(result.repository); setEvents(loadedEvents); setHistory(loadedHistory); setActiveSessions(loadedSessions);
    });
    return () => { cancelled = true; };
  }, []);

  const currentPack = useMemo<QualificationPack | null>(() => {
    if (screen.screen === 'qualifications') return null;
    return packs.find((pack) => pack.manifest.id === screen.qualificationId) ?? null;
  }, [screen]);

  const replaceActiveSession = (session: StorySession) => {
    setActiveSessions((current) => [...current.filter((item) => item.caseId !== session.caseId), session]);
  };

  const startCase = async (story: StoryCase, variantId: string) => {
    if (!currentPack || !repository || !variantId) return;
    const session = startStorySession(story, variantId, new Date());
    await repository.saveActiveSession(session);
    replaceActiveSession(session);
    setScreen({ screen: 'story', qualificationId: currentPack.manifest.id, caseId: story.id, session });
  };

  const resumeCase = (story: StoryCase, session: StorySession) => {
    if (!currentPack) return;
    setScreen({ screen: 'story', qualificationId: currentPack.manifest.id, caseId: story.id, session });
  };

  const storyForScreen = screen.screen === 'story' || screen.screen === 'debrief'
    ? currentPack?.stories.find((story) => story.id === screen.caseId) ?? null
    : null;

  return (
    <div className="study-shell">
      <header className="study-hero">
        <p className="study-eyebrow">study / cases</p>
        <h1>資格学習</h1>
        <p>問題を一つずつ消費する代わりに、状況を読み、判断し、その結果から概念をつなぐ。</p>
      </header>
      {bootstrap && <StorageWarning bootstrap={bootstrap} />}
      {!bootstrap && <p className="study-muted" role="status">学習履歴を読み込んでいます…</p>}

      {screen.screen === 'qualifications' && <QualificationPicker packs={packs} onSelect={(qualificationId) => setScreen({ screen: 'library', qualificationId })} />}

      {screen.screen === 'library' && currentPack && (
        <CaseLibrary
          pack={currentPack} events={events} history={history} activeSessions={activeSessions}
          onStart={(story, variantId) => { void startCase(story, variantId); }} onResume={resumeCase}
          onKnowledge={() => setScreen({ screen: 'knowledge', qualificationId: currentPack.manifest.id })}
          onBack={() => setScreen({ screen: 'qualifications' })}
        />
      )}

      {screen.screen === 'story' && currentPack && storyForScreen && repository && (
        <StoryPlayer
          story={storyForScreen}
          session={screen.session}
          handbook={currentPack.handbook}
          repository={repository}
          onSessionChange={(session) => {
            replaceActiveSession(session);
            setScreen({ screen: 'story', qualificationId: currentPack.manifest.id, caseId: storyForScreen.id, session });
          }}
          onLearningEvents={(newEvents) => { if (newEvents.length > 0) setEvents((current) => [...current, ...newEvents]); }}
          onReview={(session) => setScreen({ screen: 'debrief', qualificationId: currentPack.manifest.id, caseId: storyForScreen.id, session })}
          onBack={() => setScreen({ screen: 'library', qualificationId: currentPack.manifest.id })}
        />
      )}

      {screen.screen === 'debrief' && currentPack && storyForScreen && (
        <section className="study-panel">
          <p className="study-eyebrow">debrief</p>
          <h2>{storyForScreen.title}</h2>
          <p className="study-muted">判断の振り返りを準備しています。</p>
          <button className="study-button-secondary" type="button" onClick={() => setScreen({ screen: 'library', qualificationId: currentPack.manifest.id })}>ケース一覧へ</button>
        </section>
      )}

      {screen.screen === 'knowledge' && currentPack && (
        <section className="study-panel">
          <p className="study-eyebrow">knowledge</p><h2>理解の状態</h2>
          <p className="study-muted">詳細ビューを準備しています。</p>
          <button className="study-button-secondary" type="button" onClick={() => setScreen({ screen: 'library', qualificationId: currentPack.manifest.id })}>ケース一覧へ</button>
        </section>
      )}
    </div>
  );
}

import { useMemo, useState } from 'react';
import type { HandbookEntry, StoryCase } from '../domain/content-types';
import {
  advanceNarrative,
  choose,
  markAssistance,
  type LearningEvent,
  type StorySession,
} from '../domain/story-engine';
import type { StudyRepository } from '../storage/repository';
import HandbookDrawer from './HandbookDrawer';

interface Props {
  story: StoryCase;
  session: StorySession;
  handbook: HandbookEntry[];
  repository: StudyRepository;
  onSessionChange: (session: StorySession) => void;
  onLearningEvents: (events: LearningEvent[]) => void;
  onReview: (session: StorySession) => void;
  onBack: () => void;
}

export default function StoryPlayer({ story, session, handbook, repository, onSessionChange, onLearningEvents, onReview, onBack }: Props) {
  const [handbookOpen, setHandbookOpen] = useState(false);
  const [busy, setBusy] = useState(false);
  const variant = useMemo(() => story.variants.find((item) => item.id === session.variantId), [story, session.variantId]);
  if (!variant) return <p role="alert">このケースのバリアントを読み込めません。</p>;
  const scene = variant.scenes[session.sceneId];
  if (!scene) return <p role="alert">現在の場面を読み込めません。</p>;

  const persist = async (next: StorySession, emitted: LearningEvent[] = []) => {
    setBusy(true);
    try {
      if (emitted.length > 0) await repository.appendLearningEvents(emitted);
      await repository.saveActiveSession(next);
      onLearningEvents(emitted);
      onSessionChange(next);
    } finally {
      setBusy(false);
    }
  };

  const continueNarrative = () => {
    const next = advanceNarrative(story, session, new Date());
    void persist(next);
  };

  const selectChoice = (choiceId: string) => {
    const outcome = choose(story, session, choiceId, new Date());
    void persist(outcome.session, outcome.learningEvents);
  };

  const reference = async (entry: HandbookEntry) => {
    const next = markAssistance(session, entry.knowledgeIds, 'handbook', new Date());
    await persist(next);
  };

  const ending = session.endingId ? variant.endings.find((item) => item.id === session.endingId) ?? null : null;

  return (
    <section className="study-story" aria-labelledby="story-title">
      <div className="study-story-topbar">
        <button className="study-button-secondary" type="button" onClick={onBack}>ケース一覧</button>
        <button className="study-button-secondary" type="button" onClick={() => setHandbookOpen(true)}>危険物手帳</button>
      </div>
      <p className="study-eyebrow">case / {session.variantId}</p>
      <h2 id="story-title">{story.title}</h2>
      <div className={`study-scene study-scene-${scene.kind}`}>
        {scene.kind === 'resolution' && <p className="study-scene-label">結末</p>}
        <p className="study-scene-text">{scene.kind === 'resolution' && ending ? ending.text : scene.text}</p>
        {scene.kind === 'narrative' && (
          <button type="button" disabled={busy} onClick={continueNarrative}>続ける</button>
        )}
        {scene.kind === 'decision' && (
          <div className="study-choices">
            {scene.choices.map((choice) => (
              <button type="button" disabled={busy} key={choice.id} onClick={() => selectChoice(choice.id)}>{choice.text}</button>
            ))}
          </div>
        )}
        {scene.kind === 'resolution' && (
          <button type="button" disabled={busy} onClick={() => onReview(session)}>ケースを振り返る</button>
        )}
      </div>
      {handbookOpen && <HandbookDrawer entries={handbook} onReference={reference} onClose={() => setHandbookOpen(false)} />}
    </section>
  );
}

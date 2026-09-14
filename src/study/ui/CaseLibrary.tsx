import type { QualificationPack, StoryCase } from '../domain/content-types';
import type { LearningEvent, StorySession } from '../domain/story-engine';
import { rankVariants } from '../domain/recommendation';
import type { CaseHistoryEntry } from '../storage/repository';

interface Props {
  pack: QualificationPack;
  events: LearningEvent[];
  history: CaseHistoryEntry[];
  activeSessions: StorySession[];
  onStart: (story: StoryCase, variantId: string) => void;
  onResume: (story: StoryCase, session: StorySession) => void;
  onKnowledge: () => void;
  onBack: () => void;
}

export default function CaseLibrary({ pack, events, history, activeSessions, onStart, onResume, onKnowledge, onBack }: Props) {
  const visits = history.map(({ caseId, variantId, completedAt }) => ({ caseId, variantId, completedAt }));
  const ranked = rankVariants(pack, events, visits, new Date());
  const recommended = ranked[0] ?? null;
  const activeByCase = new Map(activeSessions.map((session) => [session.caseId, session]));

  const suggestedVariant = (caseId: string) => ranked.find((item) => item.caseId === caseId)?.variantId
    ?? pack.stories.find((story) => story.id === caseId)?.variants[0]?.id
    ?? '';

  return (
    <section className="study-panel" aria-labelledby="case-library-heading">
      <div className="study-section-header">
        <div>
          <p className="study-eyebrow">{pack.manifest.title}</p>
          <h2 id="case-library-heading">ケースから入る</h2>
          <p className="study-muted">順番は自由。おすすめは現在の学習履歴から変わります。</p>
        </div>
        <div className="study-header-actions">
          <button className="study-button-secondary" type="button" onClick={onKnowledge}>理解の状態</button>
          <button className="study-button-secondary" type="button" onClick={onBack}>資格一覧</button>
        </div>
      </div>
      <div className="study-card-grid study-case-grid">
        {pack.stories.map((story) => {
          const active = activeByCase.get(story.id);
          const completions = history.filter((entry) => entry.caseId === story.id).length;
          const variantId = suggestedVariant(story.id);
          const isRecommended = recommended?.caseId === story.id;
          return (
            <article className="study-card study-case-card" key={story.id}>
              <div className="study-card-meta">
                <span>{story.durationMinutes} min</span>
                <span>{completions > 0 ? `${completions}回完了` : '未完了'}</span>
              </div>
              {isRecommended && <span className="study-recommendation">今やるならこれ</span>}
              <h3>{story.title}</h3>
              <p>{story.summary}</p>
              {active ? (
                <button type="button" onClick={() => onResume(story, active)}>続きから</button>
              ) : (
                <button type="button" onClick={() => onStart(story, variantId)}>このケースを始める</button>
              )}
            </article>
          );
        })}
      </div>
    </section>
  );
}

import { useMemo, useState } from 'react';
import type { QualificationPack } from '../domain/content-types';
import { deriveKnowledgeState, type KnowledgeState } from '../domain/learning-engine';
import type { LearningEvent } from '../domain/story-engine';

interface Props {
  pack: QualificationPack;
  events: LearningEvent[];
  onBack: () => void;
}

function description(state: KnowledgeState): string {
  let text: string;
  if (state.apply >= 0.8 && state.recall >= 0.7) text = '安定して使えている';
  else if (state.apply >= 0.55) text = '使える場面が増えている';
  else if (state.encounter > 0) text = 'もう一度別の状況で使いたい';
  else text = 'まだケースで扱っていない';
  if (state.helpDependence >= 0.5) text += '。資料を参照しながら使った経験が多い。';
  return text;
}

const percent = (value: number) => `${Math.round(value * 100)}%`;

export default function KnowledgeView({ pack, events, onBack }: Props) {
  const [detailed, setDetailed] = useState(false);
  const rows = useMemo(() => pack.knowledge.map((node) => ({
    node,
    state: deriveKnowledgeState(events.filter((event) => event.knowledgeId === node.id), new Date()),
  })), [pack, events]);

  return (
    <section className="study-panel" aria-labelledby="knowledge-title">
      <div className="study-section-header">
        <div>
          <p className="study-eyebrow">knowledge</p>
          <h2 id="knowledge-title">理解の状態</h2>
          <p className="study-muted">点数ではなく、ケースの中で概念をどう使えたかを見る。</p>
        </div>
        <div className="study-header-actions">
          <button className="study-button-secondary" type="button" onClick={() => setDetailed((value) => !value)}>{detailed ? '簡易表示に戻す' : '詳細を見る'}</button>
          <button className="study-button-secondary" type="button" onClick={onBack}>ケース一覧</button>
        </div>
      </div>

      {!detailed ? (
        <div className="study-knowledge-list">
          {rows.map(({ node, state }) => (
            <article key={node.id}>
              <strong>{node.title}</strong>
              <p>{description(state)}</p>
            </article>
          ))}
        </div>
      ) : (
        <div className="study-table-wrap">
          <table className="study-knowledge-table">
            <thead><tr><th>知識</th><th>遭遇</th><th>適用</th><th>識別</th><th>再利用</th><th>資料依存</th><th>記録数</th><th>最終</th></tr></thead>
            <tbody>
              {rows.map(({ node, state }) => (
                <tr key={node.id}>
                  <th scope="row">{node.title}</th>
                  {(['encounter', 'apply', 'discriminate', 'recall', 'helpDependence'] as const).map((key) => (
                    <td key={key}><progress max={1} value={state[key]} aria-label={`${node.title} ${key}`} /> <span>{percent(state[key])}</span></td>
                  ))}
                  <td>{state.eventCount}</td>
                  <td>{state.lastSeenAt ? new Date(state.lastSeenAt).toLocaleDateString('ja-JP') : '—'}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </section>
  );
}

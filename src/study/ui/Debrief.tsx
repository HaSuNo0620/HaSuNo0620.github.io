import type { QualificationPack, StoryCase } from '../domain/content-types';
import type { StorySession } from '../domain/story-engine';

interface Props {
  pack: QualificationPack;
  story: StoryCase;
  session: StorySession;
  onDone: () => void;
}

export default function Debrief({ pack, story, session, onDone }: Props) {
  const variant = story.variants.find((item) => item.id === session.variantId);
  if (!variant) return <p role="alert">振り返りデータを読み込めません。</p>;
  const ending = variant.endings.find((item) => item.id === session.endingId) ?? null;

  const decisions = session.choiceHistory.map((record, index) => {
    const scene = variant.scenes[record.sceneId];
    if (!scene || scene.kind !== 'decision') return null;
    const choice = scene.choices.find((item) => item.id === record.choiceId);
    if (!choice) return null;
    const next = variant.scenes[choice.next];
    const consequence = next?.kind === 'narrative' ? next.text : next?.kind === 'resolution' ? ending?.text ?? next.text : '';
    const knowledge = choice.learning
      .map((signal) => pack.knowledge.find((node) => node.id === signal.knowledgeId))
      .filter((node): node is NonNullable<typeof node> => Boolean(node));
    const knowledgeIds = new Set(knowledge.map((node) => node.id));
    const handbook = pack.handbook.filter((entry) => entry.knowledgeIds.some((id) => knowledgeIds.has(id)));
    return { index: index + 1, choice, consequence, knowledge, handbook };
  }).filter((item): item is NonNullable<typeof item> => Boolean(item));

  return (
    <section className="study-panel study-debrief" aria-labelledby="debrief-title">
      <p className="study-eyebrow">debrief / {session.variantId}</p>
      <h2 id="debrief-title">{story.title} — 振り返り</h2>
      {ending && <p className="study-ending-summary">{ending.text}</p>}

      <h3>あなたの判断</h3>
      <ol className="study-debrief-list">
        {decisions.map((item) => <li key={item.index}>{item.choice.text}</li>)}
      </ol>

      <h3>起きたこと</h3>
      <div className="study-debrief-cards">
        {decisions.map((item) => (
          <article key={item.index}>
            <span>判断 {item.index}</span>
            <p>{item.consequence || 'この判断は次の状況へ直接つながった。'}</p>
          </article>
        ))}
      </div>

      <h3>関係する知識</h3>
      <div className="study-knowledge-notes">
        {decisions.flatMap((item) => item.knowledge).filter((node, index, array) => array.findIndex((other) => other.id === node.id) === index).map((node) => (
          <article key={node.id}>
            <strong>{node.title}</strong>
            <p>{node.statement}</p>
            {pack.handbook.filter((entry) => entry.knowledgeIds.includes(node.id)).map((entry) => <small key={entry.id}>手帳: {entry.title}</small>)}
          </article>
        ))}
      </div>

      <h3>試験ではどう問われるか</h3>
      <ul className="study-exam-links">
        {decisions.flatMap((item) => item.knowledge).filter((node, index, array) => node.examConnection && array.findIndex((other) => other.id === node.id) === index).map((node) => (
          <li key={node.id}><strong>{node.title}</strong> — {node.examConnection}</li>
        ))}
      </ul>
      <button className="study-button-secondary" type="button" onClick={onDone}>ケース一覧へ戻る</button>
    </section>
  );
}

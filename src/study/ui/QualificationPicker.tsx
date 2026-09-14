import type { QualificationPack } from '../domain/content-types';

interface Props {
  packs: QualificationPack[];
  onSelect: (qualificationId: string) => void;
}

export default function QualificationPicker({ packs, onSelect }: Props) {
  return (
    <section className="study-panel" aria-labelledby="qualification-heading">
      <p className="study-eyebrow">qualification</p>
      <h2 id="qualification-heading">学ぶ資格を選ぶ</h2>
      <div className="study-card-grid">
        {packs.map((pack) => (
          <article className="study-card" key={pack.manifest.id}>
            <p className="study-card-kicker">content pack</p>
            <h3>{pack.manifest.title}</h3>
            <p>{pack.manifest.sections.map((section) => section.title).join(' / ')}</p>
            <button type="button" onClick={() => onSelect(pack.manifest.id)}>ケースを見る</button>
          </article>
        ))}
      </div>
    </section>
  );
}

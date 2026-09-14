import { useState } from 'react';
import type { HandbookEntry } from '../domain/content-types';

interface Props {
  entries: HandbookEntry[];
  onReference: (entry: HandbookEntry) => Promise<void>;
  onClose: () => void;
}

export default function HandbookDrawer({ entries, onReference, onClose }: Props) {
  const [selectedId, setSelectedId] = useState<string | null>(null);

  const select = async (entry: HandbookEntry) => {
    setSelectedId(entry.id);
    await onReference(entry);
  };

  return (
    <aside className="study-handbook" aria-label="危険物手帳">
      <div className="study-handbook-header">
        <div>
          <p className="study-eyebrow">handbook</p>
          <h3>危険物手帳</h3>
        </div>
        <button className="study-button-secondary" type="button" onClick={onClose}>閉じる</button>
      </div>
      <p className="study-muted">資料を開いて考えてもかまいません。参照したことは学習履歴に残りますが、減点にはなりません。</p>
      <div className="study-handbook-list">
        {entries.map((entry) => (
          <section className="study-handbook-entry" key={entry.id}>
            <button
              type="button"
              className="study-handbook-title"
              aria-expanded={selectedId === entry.id}
              onClick={() => { void select(entry); }}
            >
              {entry.title}
            </button>
            {selectedId === entry.id && <p>{entry.body}</p>}
          </section>
        ))}
      </div>
    </aside>
  );
}

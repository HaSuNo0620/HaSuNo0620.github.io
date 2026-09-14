import type { RepositoryBootstrap, StudySnapshot } from '../storage/repository';

function downloadSnapshot(snapshot: StudySnapshot) {
  const blob = new Blob([JSON.stringify(snapshot, null, 2)], { type: 'application/json' });
  const url = URL.createObjectURL(blob);
  const anchor = document.createElement('a');
  anchor.href = url;
  anchor.download = `qualification-study-recovery-${new Date().toISOString().slice(0, 10)}.json`;
  anchor.click();
  URL.revokeObjectURL(url);
}

interface Props {
  bootstrap: RepositoryBootstrap;
}

export default function StorageWarning({ bootstrap }: Props) {
  if (bootstrap.warning === 'none') return null;
  if (bootstrap.warning === 'unavailable') {
    return (
      <aside className="study-warning" role="status">
        このブラウザでは学習履歴を保存できません。現在のセッションはページを閉じると失われます。
      </aside>
    );
  }
  return (
    <aside className="study-warning" role="status">
      <p>保存データの形式がこの版より新しいため、既存データには変更を加えず、一時モードで開いています。</p>
      {bootstrap.recoverySnapshot && (
        <button className="study-button-secondary" type="button" onClick={() => downloadSnapshot(bootstrap.recoverySnapshot!)}>
          既存データを書き出す
        </button>
      )}
    </aside>
  );
}

# HaSuNo Garden 再構築仕様

2026-11-28。対象は全32記事。監査記録は editorial-audit/ を参照。本仕様は改稿・実装の基準であり、公開済みの変更を意味しない。

## 情報設計

- トップ / は分野への入口を主とし、最近の更新を併記する。既存の色・書体・数式・図版のデザイン基盤を維持する。
- /fields/ と /fields/{field}/ を新設。分野IDは interfaces, statistical-physics, quasicrystals, mathematics, economics, culture。
- /notes/ は全記事の検索、分野・状態による絞り込み、更新順・公開順。スピン専用フィルターを分野ページへ移す。
- /topics/ と /topics/{topic}/ は概念索引として維持。既存の分野アンカーも保持する。
- /updates/ は公開日と実際の改訂日を区別した履歴。移行だけで全記事の改訂日を変えない。
- /about/ はサイトの目的と現在の関心。/now/ は既存リンクのため保持し、主要ナビゲーションからは外す。
- 資格学習は公開しない。Git履歴で復元可能にし、学習専用コード・教材・検証・CI設定・依存関係を参照調査後に整理する。
- 日本語を主としたナビゲーション。固有の専門用語は必要な英語を残す。

## 記事の移行台帳

旧ID | 移行先（notes/ 以下、fields/ は絶対パス） | 扱い
--- | --- | ---
interface-thinking-map | /fields/interfaces/ | 案内へ
young-laplace-coarse-graining | 同ID | 維持
gibbs-to-tolman-gauge-curvature | 同ID | 維持
van-der-waals-diffuse-interface | 同ID | 維持
kirkwood-buff-stress-anisotropy | 同ID | 維持
新設 | curvature-dependent-surface-tension | 曲率・代表面・応力モーメントを集約
spin-model-thinking-map | /fields/statistical-physics/ | 案内へ
finite-range-symmetry-comparison | 同ID | 共通理論に改題・拡充
ising-rn-transfer-matrix | finite-range-symmetry-comparison | 統合
clock-chain-finite-range | finite-range-symmetry-comparison | 統合
xy-chain-finite-range | finite-range-symmetry-comparison | 統合
ising-range-comparison | finite-range-symmetry-comparison | 統合（一部R2へ）
ising-xy-nearest-neighbor-comparison | clock-chain-nearest-neighbor | 統合
ising-transfer-matrix | 同ID | 維持
ising-r2-transfer-matrix | 同ID | 維持
clock-chain-nearest-neighbor | 同ID | 維持
clock-chain-second-neighbor | 同ID | 維持
xy-chain-nearest-neighbor | 同ID | 維持
xy-chain-second-neighbor | 同ID | 維持
ising-xy-second-neighbor-comparison | 同ID | 比較固有の内容に限定
ising-r1-periodic | 同ID | 維持
xxz-chain-quantum | 同ID | 維持
quasicrystal-order-without-periodicity | /fields/quasicrystals/ | 案内へ
quasiperiodic-functions-torus | 同ID | 維持
fibonacci-cut-and-project | 同ID | 維持
quasicrystal-diffraction-fourier-module | 同ID | 維持
asymptotic-analysis-map | 同ID | 維持
elliptic-functions-map | 同ID | 維持
consumer-choice-and-price-formation | 同ID | 維持
nash-bertrand-price-competition | 同ID | 維持
price-quality-joint-choice | 同ID | 維持
multiproduct-competitor-repositioning | 同ID | 維持
anime-vector-analysis | 同ID | 構想として維持

合計25本文（既存24＋新設1）、案内6。旧Ising専用ページ /notes/ising/ は統計物理の模型表へ誘導。統合前に移管する固有内容・図・出典を照合し、移行先完成までは元記事を非公開化しない。

## メタデータ

既存 area は学問分類として保持し、field を主閲覧分類として追加する。準結晶に属する数学記事も field=quasicrystals とする。topics は横断概念、system はスピン模型の属性。kind は theory/model/comparison/essay/proposal を区別。prerequisites と related は記事ID配列。旧IDとの対応は単一の移行台帳（TypeScript）で管理する。順序・グループは分野定義で管理し、同じ記事を複数箇所に複製しない。移行中は optional な項目と既存IDの明示的な分類表を用い、完了後に必須化する。依存は循環させない。関連リンクは循環可。

## 分野内の読み順

- 界面：Young–Laplace → Gibbs → 曲率（Gibbsを前提）、平方勾配とKirkwood–Buffは独立経路。曲率と局所応力の関係は条件を限定。
- 統計物理：有限範囲の一般理論を基礎とし、最近接/第二近接×Ising/Clock/XYの表、比較、周期系、量子系を配置。XXZは古典転送作用素を前提にしない。
- 準結晶：準周期関数 → Fibonacci射影 → 回折。導入で非周期秩序の意味を説明。
- 数学：漸近解析と楕円関数は独立。
- 経済：消費者選択 → 価格競争 → 品質選択 → 複数商品。価格競争は複数商品にも直接必要。
- 文化：構想を結果と区別。

## 静的サイト移行

GitHub Pagesの静的配信なのでサーバー側301を前提にしない。旧URLに静的な移転案内HTML（canonical、移転先への通常リンク、必要ならmeta refresh）を生成する。旧記事と同じルートに二重生成しない。統合記事の節リンクは検証した見出しIDに対応できる場合のみ付与。旧タグは索引または移転案内を保持。内部リンクは正規URLへ更新する。旧URL・新URLを全件検査。

## 実装順序・受け入れ条件

1. 分野台帳、スキーマの後方互換拡張、移行台帳の検証。
2. 分野一覧と詳細、トップ、記事一覧、個別記事のパンくず・前提・関連リンク、更新履歴。既存のCSS基盤を使用。
3. 分野ごとの本文改稿（共通理論を先に）。数式と書誌の検証、再現計算、図版の移管。
4. 統合先が完成した時点で旧記事の静的移転ページを有効化。
5. 学習専用の依存関係とCIを整理。package-lockとの整合を維持。
6. クリーン環境でnpm ci、型検査、テスト、ビルド。全内部リンク、画像、旧URL、依存関係、MathJax、モバイル表示、検索、キーボード操作を確認。
7. mainへの統合は検証結果をレビューした後。

既存の prebuild は validate:study を実行し、React統合等も残る。削除は利用状況確認後に行う。複数商品記事に欠損図があるため、生成コードと参照を別途点検する。

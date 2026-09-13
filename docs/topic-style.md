# Topic Style v1.0

`topics` は本文中のキーワード一覧ではなく、Notes を横断して辿るための分類タグとして使う。

## 基本原則

- 1 Note あたり原則 2–4 topics。最大 4。
- `area` がすでに表している大分類を topics で繰り返さない。
- その語をクリックしたとき、同じ専門テーマの複数 Note が意味のあるまとまりになるものを優先する。
- 本文に登場するだけの一般語、観測量、操作、説明用語は原則 topic にしない。
- 1 Note にしか現れず、今後も独立した系列を作らない細かすぎる語は避ける。

## 残しやすいもの

- 対象・模型: `Ising model`, `XY model`, `XXZ model`, `quasicrystals`, `elliptic functions`
- 系列を分ける構造: `frustration`, `periodic modulation`, `chirality`, `aperiodic order`
- 複数 Note を実際につなぐ専門手法: `transfer matrix`, `cut and project`, `Kirkwood-Buff`

## 原則として表に出さないもの

`statistical mechanics`, `correlation`, `memory`, `wave number`, `linear response`, `external field`, `data analysis`, `pricing` など、広すぎる分野語・一般概念・本文上の操作語。

サイトでは `curateTopics()` が既存 front matter にもこの方針を適用し、重複除去・低情報量 topic の除外・最大 4 件への制限を行う。

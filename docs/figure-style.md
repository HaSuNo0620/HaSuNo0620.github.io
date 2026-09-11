# Figure Style v1.4

HaSuNo0620.github.io で用いる図の共通書式。図は独立した白い論文図ではなく、**ページの紙面の一部**として扱う。v1.4 では v1.3 の大きな文字・太い線・数式 typography を維持しつつ、**凡例・直接ラベルの可読性と light / dark 両テーマでのコントラスト**を明文化する。

## 1. 基本原則

1. 図を作る前に「この図を見た人に何を発見してほしいか」を一文で決める。
2. 図内タイトルは原則置かない。節見出しとキャプションに説明を任せる。
3. Figure canvas 自体は透明とする。ただし **legend / direct label の可読性を確保する局所的な paper 背景は使用する**。
4. 色だけで系列を区別しない。線種・marker・太さを併用する。
5. 本文の数式と図の表記を一致させる。
6. SVG を標準形式とし、図は再生成可能なスクリプトから作る。
7. 細く繊細な論文図より、Web ページ上で一目で読める強さを優先する。
8. 情報量が増えたら文字や線を細くせず、図を分ける。
9. **文字色に固定 black / white を使わず、theme-aware ink を使う。**

## 2. Canvas

標準サイズは 760 × 440 px 相当（Matplotlib では 7.6 × 4.4 inch）。

- standard plot: 760 × 440
- wide comparison: 760 × 360
- tall schematic: 760 × 520 まで
- multi-panel: 全体幅 760 を基準にする

余白は詰めすぎず、軸ラベル・凡例・データの間に十分な呼吸を残す。

## 3. Site palette

| semantic role | light | dark |
| --- | --- | --- |
| paper | `#f3efe6` | `#1c1c19` |
| paper-2 | `#ebe5d9` | `#272720` |
| ink / axis | `#171714` | `#f0eadf` |
| muted | `#716d64` | `#a8a196` |
| grid / border | `#cbc3b5` | `#4a4740` |
| primary / accent | `#5866e9` | `#99a2ff` |
| secondary / comparison | `#39705a` | `#8bc4a9` |

意味を固定する。

- **accent blue**: 主対象、厳密解、現在注目している量
- **green**: 比較、近似、参照理論
- **ink**: データ点、基準線、構造そのもの、通常文字
- **muted**: 補助系列、二次的情報
- **paper / paper-2**: 局所的な legend / annotation の下地

3系列以上では無制限に色を増やさず、線種・marker・濃淡を使う。虹色 palette は使わない。

## 4. Line semantics

| content | representation |
| --- | --- |
| exact / primary theory | accent blue, solid, **4.5 px** |
| approximation / asymptote / fit | green, dashed, **3.6 px** |
| secondary series | **3.6 px** 前後、dash pattern で区別 |
| simulation / measured data | marker, ink or accent, **8–9 px** |
| guide / reference / zero line | muted, dotted, **2.0 px** |
| error bar | **1.8 px**, marker より弱く |
| uncertainty band | same semantic color, alpha ≈ 0.15 |

「data = marker, theory = line」を基本とする。主線は本文幅に縮小された状態でも一目で追える太さを優先する。

## 5. Axes and grid

- 上・右 spine は表示しない。
- 左・下 spine は **1.8 px**。
- major grid のみを標準とし、**1.1 px**、低コントラスト。
- minor grid は必要な場合のみ。
- zero line や臨界点など、物理的意味を持つ基準線だけを追加する。
- tick を過密にしない。

## 6. Typography

標準値：

- axis label: **19–20 px / pt 相当**
- tick label: **16 px / pt 相当**
- legend: **18 px / pt 相当**
- annotation: **17 px / pt 相当**
- panel label `(a)`: **18 px / pt 相当**, semibold

凡例は「補助情報だから小さくする」のではなく、系列を読むための主要情報として tick より大きくする。

通常文字、凡例、注釈、直接ラベルは theme-aware `ink` を使う。固定 `black` は light mode では使えても dark mode で背景へ同化するため禁止する。

## 7. Mathematical labels

### 7.1 すべてを italic にしない

図中で数式らしい字体を使う場合も、数式全体へ一括して `font-style: italic` を掛けない。

**italic にするもの**：

- 変数・物理量・可変パラメータ：$h$, $J$, $T$, $q$, $r$, $m$, $\beta$, $\chi$, $\xi$
- 添字が変数なら、その添字も variable として扱う

**upright にするもの**：

- 数字：`0`, `1.2`, `10`
- 演算子・関係記号：`=`, `+`, `−`, `/`
- 括弧・角括弧・カンマなどの区切り記号
- 説明語：`exact`, `response`, `field`, `low-T asymptote`
- 規格化に使う固定定数など、その文脈で変数ではない記号（例：$q/\pi$ の $\pi$）
- 単位・説明的な添字

したがって `βJ = 1.2` なら `β` と `J` だけが italic で、`= 1.2` は upright にする。`χ(q) / χ(0)` では `χ` と `q` は italic、括弧・slash・`0` は upright とする。

### 7.2 Matplotlib

Matplotlib では mathtext を使い、通常の TeX 数式規則に任せる。説明語は math mode に入れない。upright にしたい単位・語・定数は `\mathrm{}` 等を使う。

例：

```python
ax.set_xlabel(r"$q / \mathrm{\pi}$")
ax.set_ylabel(r"$\chi(q) / \chi(0)$")
```

### 7.3 SVG を直接生成する場合

SVG を `<img>` として読み込む場合、MathJax は SVG 内部を再組版しない。そのため `STIX Two Math`, `Cambria Math`, `Times New Roman` などを fallback にしつつ、`<tspan>` 単位で役割を分ける。

```svg
<text class="mathlabel">
  <tspan class="mi">β</tspan><tspan class="mi">J</tspan>
  <tspan class="mo"> = </tspan><tspan class="mn">1.2</tspan>
</text>
```

ここで `mi` は variable identifier、`mo` は operator / punctuation、`mn` は numeral として扱う。数式フォントを使うことと、全体を italic にすることは別である。

本文の数式表記ルールは [`docs/math-style.md`](math-style.md) に従う。

## 8. Legend and direct labels

凡例は完全透明を標準にしない。データ曲線と重なったとき、凡例文字と sample line の両方が読みにくくなるためである。

優先順位：

1. **少数系列なら direct label を優先**する。
2. 図内凡例が必要なら、**半透明 paper box** を使う。
3. 曲線が密なら **outside legend** を使う。

### 8.1 In-plot legend

light mode:

- face: paper `#f3efe6`, alpha ≈ **0.90**
- edge: ink, alpha ≈ **0.14**
- text: ink `#171714`

 dark mode:

- face: dark paper `#1c1c19` または paper-2 `#272720`, alpha ≈ **0.84–0.90**
- edge: light ink, alpha ≈ **0.14**
- text: ink `#f0eadf`

枠線は細く、shadow は原則使わない。legend sample は実線より細くせず、必要なら **5 px 相当**まで太くする。

### 8.2 Direct label

curve 上または curve の近傍へ置く。線との重なりで読みにくい場合は、paper 色の小さな下地を alpha **0.80–0.90** 程度で置く。文字は theme-aware ink とする。

## 9. Captions

説明は図内タイトルではなく本文側の caption に置く。caption は「何を描いたか」だけでなく「何を読むべきか」まで一文で書く。物理量は [`Math Style`](math-style.md) に従って inline math にする。

## 10. Multiple panels

関連する量を同時に読む必要があるときだけ multi-panel を使う。特に

- real space ↔ reciprocal space
- data ↔ model residual
- microscopic ↔ coarse-grained
- exact ↔ asymptotic

の対を積極的に可視化する。panel label は大きめに置き、数式部分と説明部分の typography を分ける。

## 11. Heatmaps and field plots

連続スカラー場では知覚的に単調な colormap を使う。

- nonnegative / sequential scalar: `cividis` を第一候補
- signed quantity with meaningful zero: zero-centered diverging map
- categorical map: 少数カテゴリのみ、境界や label を併用

colorbar の文字サイズも通常の tick より小さくしない。虹色 `jet` は使わない。

## 12. Schematics

模式図はグラフと同じ palette を使う。詳細な模式図の幾何学・言語・配置ルールは [`docs/diagram-style.md`](diagram-style.md) に従う。

- system / geometry: ink
- focus / selected object: accent blue
- interaction / response / comparison: green
- construction line / auxiliary geometry: muted

線は細くしすぎず、矢印・境界・ラベルが本文縮小後も明瞭に残る太さを選ぶ。

## 13. File formats and naming

- plot / diagram / schematic: SVG
- simulation snapshot / raster field: PNG or WebP
- photo: WebP
- animation: WebM; GIF は必要時のみ

Figure canvas は transparent background とする。ファイル名は内容を説明する kebab-case とする。

## 14. Reproducibility

図は可能な限り生成スクリプトを残す。Matplotlib では `scripts/figure_style.py` を import し、色・線幅・文字・軸・保存規則を共有する。Ising $R=1$ の図は development / production build 前に `scripts/ising_r1_figures.py` で再生成される。

## 15. Pre-publish checklist

- [ ] 図から読み取らせたい主張が一つに絞られている
- [ ] Figure canvas は transparent background
- [ ] 図内タイトルなし
- [ ] 軸ラベルと本文の記号が一致
- [ ] **変数だけが italic で、数字・演算子・括弧・説明語まで italic になっていない**
- [ ] **凡例・直接ラベルの文字が背景や曲線に埋もれていない**
- [ ] **凡例が必要な場合、半透明 paper box または図外配置になっている**
- [ ] **文字色に固定 black / white を使っていない**
- [ ] **主線が一目で追える太さになっている**
- [ ] 色だけで情報を符号化していない
- [ ] grid が data より目立たない
- [ ] exact / data / fit の線種規則が守られている
- [ ] caption が図の意味まで説明している
- [ ] SVG または適切な raster format
- [ ] 再生成スクリプトが残っている

この文書を **HaSuNo0620.github.io Figure Style v1.4** の基準とする。

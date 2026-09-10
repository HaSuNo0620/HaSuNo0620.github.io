# Figure Style v1.1

HaSuNo0620.github.io で用いる図の共通書式。図は独立した白い論文図ではなく、**ページの紙面の一部**として扱う。v1.1 では実際のブラウザ表示を基準に、文字と線を一段大きく・太くし、縮小表示でも読みやすいことを優先する。

## 1. 基本原則

1. 図を作る前に「この図を見た人に何を発見してほしいか」を一文で決める。
2. 図内タイトルは原則置かない。節見出しとキャプションに説明を任せる。
3. 背景は透明。白背景の `<rect>` や白い legend box は置かない。
4. 色だけで系列を区別しない。線種・marker・太さを併用する。
5. 本文の数式と図の表記を一致させる。軸名は文章より `symbol / normalization` を優先する。
6. SVG を標準形式とし、図は再生成可能なスクリプトから作る。
7. 細く繊細な論文図より、Web ページ上で一目で読める強さを優先する。

## 2. Canvas

標準サイズは 760 × 440 px 相当（Matplotlib では 7.6 × 4.4 inch）。

- standard plot: 760 × 440
- wide comparison: 760 × 360
- tall schematic: 760 × 520 まで
- multi-panel: 全体幅 760 を基準にする

余白は詰めすぎず、軸ラベルとデータの間に十分な呼吸を残す。

## 3. Site palette

サイト本体の CSS と意味を合わせる。

| semantic role | light | dark |
| --- | --- | --- |
| ink / axis | `#171714` | `#f0eadf` |
| muted | `#716d64` | `#a8a196` |
| grid / border | `#cbc3b5` | `#4a4740` |
| primary / accent | `#5866e9` | `#99a2ff` |
| secondary / comparison | `#39705a` | `#8bc4a9` |

意味を固定する。

- **accent blue**: 主対象、厳密解、現在注目している量
- **green**: 比較、近似、参照理論
- **ink**: データ点、基準線、構造そのもの
- **muted**: 補助系列、注釈、二次的情報

3系列以上では無制限に色を増やさず、線種・marker・濃淡を使う。虹色 palette は使わない。

## 4. Line semantics

| content | representation |
| --- | --- |
| exact / primary theory | accent blue, solid, **3.2 px** |
| approximation / asymptote / fit | green, dashed, **2.6 px** |
| secondary series | **2.6 px** 前後、dash pattern で区別 |
| simulation / measured data | marker, ink or accent, **7 px** 前後 |
| guide / reference / zero line | muted, dotted, **1.5 px** |
| error bar | **1.5 px**, marker より弱く |
| uncertainty band | same semantic color, alpha ≈ 0.15 |

「data = marker, theory = line」を基本とする。fit と theory を同じ実線で表さない。

## 5. Axes and grid

- 上・右 spine は表示しない。
- 左・下 spine は **1.4 px**。
- major grid のみを標準とし、**0.9 px**、低コントラスト。
- minor grid は必要な場合のみ。
- zero line や臨界点など、物理的意味を持つ基準線だけを追加する。
- tick を過密にしない。

軸ラベルは短くする：`h / J`, `q / π`, `z / σ`, `χ(q) / χ(0)`, `T*` など。

## 6. Typography

図内の標準値を次に固定する。

- axis label: **17 px / pt 相当**
- tick label: **14 px / pt 相当**
- legend / direct label: **14 px / pt 相当**
- annotation: **15 px / pt 相当**
- panel label `(a)`: **16 px / pt 相当**, semibold

図が本文幅に縮小されても読めることを基準にする。小さな文字で情報量を詰め込まず、必要なら図を分ける。

font family は `Noto Sans JP`, `system-ui`, sans-serif 相当。数学記号は可能なら Unicode (`β`, `χ`, `ξ`, `Δ`, `π`) を使う。

## 7. Legend

- 枠なし、背景なし。
- データを覆わない位置に置く。
- 系列数が少なければ curve への直接ラベルを優先する。
- 凡例の文字も tick と同程度以上にする。

## 8. Captions

説明は図内タイトルではなく本文側の caption に置く。caption は「何を描いたか」だけでなく「何を読むべきか」まで一文で書く。

> **Fig. 4 —** 最近接 Ising 鎖の波数依存感受率。低温になるほど応答は `q=0` 周辺へ集中する。

Markdown では当面、画像直後の斜体段落を caption とする。

## 9. Multiple panels

関連する量を同時に読む必要があるときだけ multi-panel を使う。特に

- real space ↔ reciprocal space
- data ↔ model residual
- microscopic ↔ coarse-grained
- exact ↔ asymptotic

の対を積極的に可視化する。panel label は `(a)`, `(b)` を大きめに置き、長い panel title は避ける。

## 10. Heatmaps and field plots

連続スカラー場では知覚的に単調な colormap を使う。

- nonnegative / sequential scalar: `cividis` を第一候補
- signed quantity with meaningful zero: zero-centered diverging map
- categorical map: 少数カテゴリのみ、境界や label を併用

colorbar の文字サイズも通常の tick より小さくしない。虹色 `jet` は使わない。

## 11. Schematics

模式図はグラフと同じ palette を使う。

- system / geometry: ink
- focus / selected object: accent blue
- interaction / response / comparison: green
- construction line / auxiliary geometry: muted

線は細くしすぎず、矢印・境界・ラベルが本文縮小後も明瞭に残る太さを選ぶ。

## 12. File formats and naming

- plot / diagram / schematic: SVG
- simulation snapshot / raster field: PNG or WebP
- photo: WebP
- animation: WebM; GIF は必要時のみ

SVG は transparent background とする。ファイル名は内容を説明する kebab-case とする。

## 13. Reproducibility

図は可能な限り生成スクリプトを残す。Matplotlib では `scripts/figure_style.py` を import し、色・線幅・文字・軸・保存規則を共有する。Ising R=1 の図は production build 前に `scripts/ising_r1_figures.py` で再生成される。

```python
from figure_style import new_figure, style_axes, plot_exact, plot_approx, save_figure

fig, ax = new_figure()
plot_exact(ax, x, y_exact)
plot_approx(ax, x, y_asymptotic)
style_axes(ax, xlabel="q / π", ylabel="χ(q) / χ(0)")
save_figure(fig, "public/figures/example.svg")
```

## 14. Pre-publish checklist

- [ ] 図から読み取らせたい主張が一つに絞られている
- [ ] transparent background
- [ ] 図内タイトルなし
- [ ] 軸ラベルと本文の記号が一致
- [ ] **文字が本文埋め込み時にも十分大きい**
- [ ] **主線が一目で追える太さになっている**
- [ ] 色だけで情報を符号化していない
- [ ] legend は frameless
- [ ] grid が data より目立たない
- [ ] exact / data / fit の線種規則が守られている
- [ ] caption が図の意味まで説明している
- [ ] SVG または適切な raster format
- [ ] 再生成スクリプトが残っている

この文書を **HaSuNo0620.github.io Figure Style v1.1** の基準とする。

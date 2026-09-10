# Figure Style v1

HaSuNo0620.github.io で用いる図の共通書式。図は独立した白い論文図ではなく、**ページの紙面の一部**として扱う。目的は、研究ノート全体で意味・視線誘導・再現性を揃えることにある。

## 1. 基本原則

1. 図を作る前に「この図を見た人に何を発見してほしいか」を一文で決める。
2. 図内タイトルは原則置かない。節見出しとキャプションに説明を任せる。
3. 背景は透明。白背景の `<rect>` や白い legend box は置かない。
4. 色だけで系列を区別しない。線種・marker・太さを必ず併用する。
5. 本文の数式と図の表記を一致させる。軸名は文章より `symbol / normalization` を優先する。
6. SVG を標準形式とし、図は再生成可能なスクリプトから作る。

## 2. Canvas

標準サイズは 760 × 440 px 相当（Matplotlib では 7.6 × 4.4 inch）。

- standard plot: 760 × 440
- wide comparison: 760 × 360
- tall schematic: 760 × 520 まで
- multi-panel: 全体幅 760 を基準にする

余白は `tight_layout` / `constrained_layout` で詰めすぎず、軸ラベルとキャプションの間に呼吸を残す。

## 3. Site palette

サイト本体の CSS と意味を合わせる。

| semantic role | light | dark site token |
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
| exact / primary theory | accent blue, solid, 2.4 px |
| approximation / asymptote / fit | green, dashed, 1.8 px |
| simulation / measured data | marker, ink or accent, 5–6 px |
| guide / reference / zero line | muted, dotted, 1.0 px |
| secondary series | 1.6–1.8 px, distinguish by dash pattern |
| error bar | 1.0 px, visually weaker than marker |
| uncertainty band | same semantic color, alpha ≈ 0.15 |

「data = marker, theory = line」を基本とする。fit と theory を同じ実線で表さない。

## 5. Axes and grid

- 上・右 spine は表示しない。
- 左・下 spine は 1.0 px。
- major grid のみ。0.7 px 程度、低コントラスト。
- minor grid は必要な場合のみ。
- zero line や臨界点など、物理的意味を持つ基準線だけを追加する。
- tick を過密にしない。

軸ラベルは短くする。

- `h / J`
- `q / π`
- `z / σ`
- `χ(q) / χ(0)`
- `γ / (ε σ⁻²)`
- `T*`

図内で説明文を軸ラベル代わりにしない。

## 6. Typography

図内の既定値：

- axis label: 14 pt
- tick label: 12 pt
- legend / direct label: 12 pt
- annotation: 12–13 pt
- panel label `(a)`: 13 pt, semibold

font family は `Noto Sans JP`, `system-ui`, sans-serif 相当。数学記号は可能なら Unicode (`β`, `χ`, `ξ`, `Δ`, `π`) を使い、図内で別の TeX レンダラに依存しすぎない。

## 7. Legend

- 枠なし、背景なし。
- データを覆わない位置に置く。
- 系列数が少なければ、凡例より curve への直接ラベルを優先する。
- 凡例の順序は物理的な比較順にする（温度昇順、距離昇順など）。

## 8. Captions

説明は図内タイトルではなく本文側の caption に置く。caption は「何を描いたか」だけでなく「何を読むべきか」まで一文で書く。

例：

> **Fig. 4 —** 最近接 Ising 鎖の波数依存感受率。低温になるほど応答は `q=0` 周辺へ集中する。

Markdown では当面、画像直後の斜体段落を caption とする。

## 9. Multiple panels

関連する量を同時に読む必要があるときだけ multi-panel を使う。

特にこのサイトでは

- real space ↔ reciprocal space
- data ↔ model residual
- microscopic ↔ coarse-grained
- exact ↔ asymptotic

の対を積極的に可視化する。

panel label は左上に `(a)`, `(b)` と置く。各 panel に長いタイトルは付けない。

## 10. Heatmaps and field plots

曲線図の2色規則を無理にヒートマップへ適用しない。連続スカラー場では知覚的に単調な colormap を使う。

- nonnegative / sequential scalar: `cividis` を第一候補
- signed quantity with meaningful zero: zero-centered diverging map
- categorical map: 少数カテゴリのみ、色だけでなく境界や label を併用

colorbar には量と規格化を明記する。虹色 `jet` は使用しない。

vector field は矢印を ink / muted に抑え、背景スカラー場より視覚的に強くしすぎない。

## 11. Schematics

模式図はグラフと同じ palette を使うが、PowerPoint 的な色付き箱を多用しない。

- system / geometry: ink
- focus / selected object: accent blue
- interaction / response / comparison: green
- construction line / auxiliary geometry: muted
- arrow: thin, minimal

「教科書の余白に描いた図を整えた」程度の密度を目標にする。

## 12. File formats and naming

- plot / diagram / schematic: SVG
- simulation snapshot / raster field: PNG or WebP
- photo: WebP
- animation: WebM; GIF は必要時のみ

ファイル名は内容を説明する kebab-case とする。

```text
public/figures/<note-slug>/correlation-distance.svg
public/figures/<note-slug>/susceptibility-q.svg
public/figures/<note-slug>/density-map.png
```

SVG は必ず transparent background で保存する。

## 13. Reproducibility

図は可能な限り生成スクリプトを残す。Matplotlib では `scripts/figure_style.py` を import し、色・線幅・軸・保存規則を共有する。

```python
from figure_style import new_figure, style_axes, save_figure, COLORS

fig, ax = new_figure()
ax.plot(x, y_exact, color=COLORS["accent"], lw=2.4)
ax.plot(x, y_asymptotic, color=COLORS["green"], lw=1.8, ls="--")
style_axes(ax, xlabel="q / π", ylabel="χ(q) / χ(0)")
save_figure(fig, "public/figures/example.svg")
```

## 14. Pre-publish checklist

- [ ] 図から読み取らせたい主張が一つに絞られている
- [ ] transparent background
- [ ] 図内タイトルなし
- [ ] 軸ラベルと本文の記号が一致
- [ ] 色だけで情報を符号化していない
- [ ] legend は frameless
- [ ] grid が data より目立たない
- [ ] exact / data / fit の線種規則が守られている
- [ ] caption が図の意味まで説明している
- [ ] SVG または適切な raster format
- [ ] 再生成スクリプトが残っている

この文書を **HaSuNo0620.github.io Figure Style v1** の基準とし、例外を使う場合は「その図で物理的意味をより正確に伝えるため」という理由を優先する。
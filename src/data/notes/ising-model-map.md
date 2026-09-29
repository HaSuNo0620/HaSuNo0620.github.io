---
title: "1次元 Ising 系の地図 — 相互作用範囲と空間構造"
summary: "1次元 classical cosine-Z2 系の既存ノートを、相互作用範囲 R と空間構造の二方向から案内する Ising 専用 hub。個別模型、R 比較、対称性比較の役割を分け、次にどの座標を動かすかを見える形にする。"
publishedAt: 2026-09-29T17:06:00+09:00
updatedAt: 2026-09-29
area: "Physics"
topics: ["statistical mechanics", "Ising model", "transfer matrix", "domain wall"]
status: growing
system:
  dimension: 1
  spatial: [uniform, periodic]
  range: [R1, R2, Rn]
  interaction: cosine
  symmetry: [Z2]
  mechanics: classical
  role: hub
---

Ising 系のノートが増えると、最近接、第二近接、有限範囲、周期結合が別々の模型に見えやすい。実際には、現在の系列では

$$
oxed{
d=1,qquad
	ext{classical},qquad
	ext{cosine},qquad
Z_2
}
$$

を固定し、

$$
oxed{
R
quad	ext{と}quad
	ext{spatial organization}
}
$$

を主に動かしている。

より上位の整理は [スピン系をどう読むか](/notes/spin-model-thinking-map) に置き、このページでは **Ising 系の現在地だけ**を取り出す。

---

## Ising では何を記憶しているか

局所変数を

$$
	au_i=s_i s_{i+1}=pm1
$$

とおくと、$	au_i=-1$ は domain wall / spin flip に対応する。

したがって Ising 系で固定されている memory variable は

$$
oxed{
	ext{二値の反転情報 } 	au_i
}
$$

である。

この局所変数を変えずに、

- 相互作用が何個の $	au$ を同時に読むか
- その読み方が空間のどこで変わるか

を動かしている。

---

## 相互作用範囲 (R) を動かす

一様系では

$$
oxed{
R=1
longrightarrow
R=2
longrightarrow
R=n
}
$$

が一つの系列になる。

| (R) | wall 表示 | 物理的な違い | 個別ノート |
| --- | --- | --- | --- |
| (1) | 単独の (	au_i) | wall が独立 | [最近接 Ising](/notes/ising-transfer-matrix) |
| (2) | (	au_i	au_{i+1}) が入る | wall 配置が相関 | [第二近接 Ising](/notes/ising-r2-transfer-matrix) |
| (n) | 最大 (n) 個の連続積 | より長い wall pattern を読む | [有限範囲 Ising](/notes/ising-rn-transfer-matrix) |

この軸だけを横断して比較する内容は [相互作用範囲の比較](/notes/ising-range-comparison) にまとめている。

したがって、

$$
oxed{
R=	ext{局所 Boltzmann 重みが読む空間履歴の深さ}
}
$$

という見方が Ising 系では使いやすい。

---

## 空間構造を動かす

(R=1) を固定したまま結合を

$$
J_i=J
$$

から

$$
J_{i+p}=J_i
$$

へ変えると、wall 同士を相互作用させずに、wall の生成コストだけを場所ごとに変えられる。

$$
oxed{
	ext{uniform}
longrightarrow
	ext{periodic}
}
$$

に対応する個別ノートは [周期的最近接 Ising](/notes/ising-r1-periodic) である。

一様最近接では **independent identical walls**、周期最近接では **independent nonidentical walls** になる。

ここでは (R) は変わっていない。変わったのは

$$
oxed{
	ext{memory rule の spatial organization}
}
$$

である。

周期外場による応答も同じ模型座標の観測として、この個別ノート内に置いている。

---

## 現在埋まっている Ising 座標

現在の個別模型を (R) と空間構造で並べると、

| 空間構造 | (R=1) | (R=2) | (R=n) |
| --- | --- | --- | --- |
| uniform | [最近接](/notes/ising-transfer-matrix) | [第二近接](/notes/ising-r2-transfer-matrix) | [有限範囲](/notes/ising-rn-transfer-matrix) |
| periodic | [周期最近接](/notes/ising-r1-periodic) | — | — |
| quasiperiodic | — | — | — |
| random | — | — | — |

となる。

この表の空欄は、そのまま「新しいノートを埋めるべき場所」という意味ではない。新しい座標へ進む前に、

$$
oxed{
	ext{その座標を動かすことで、
既存の模型では見えなかった何が分離できるか}
}
$$

を先に問う。

---

## 対称性を変える比較は Ising の外へ出る

Ising 内で (R) や空間構造を動かすのとは別に、

$$
Z_2
longrightarrow
Z_q
longrightarrow
U(1)
$$

と状態空間を変える比較がある。

最近接では [Ising–XY 最近接比較](/notes/ising-xy-nearest-neighbor-comparison)、第二近接では [Ising–XY 第二近接比較](/notes/ising-xy-second-neighbor-comparison) がその橋になる。

有限範囲まで含めた対称性横断は [有限範囲スピン系の比較](/notes/finite-range-symmetry-comparison) に置く。

ここで動かしているのは (R) ではなく、

$$
oxed{
	ext{何を memory variable として区別するか}
}
$$

である。

---

## 近似・表現は座標ではなく information filter

同じ Ising 模型でも、何を残す表現を選ぶかで見える物理は変わる。

domain-wall 表示では

$$
oxed{
	ext{flip の配置とその相関}
}
$$

が直接見える。

transfer matrix では

$$
oxed{
	ext{有限履歴と長距離 spectrum}
}
$$

が見える。

粗視化場や saddle-point 表現を使う場合には、欠陥や texture の形が前面に出る。

したがって近似・表現は、

$$
oxed{
	ext{模型座標}
}
$$

に追加する第4座標ではなく、

$$
oxed{
	ext{どの情報を残して模型を見るか}
}
$$

を決める filter として扱う。

---

## この hub から見る次の方向

現在の Ising 系で基準となる一様 (R) 系列はすでに

$$
R=1	o2	o n
$$

までつながっている。

そのため、次の拡張で候補になるのは (R) をさらに細かく増やすことより、空間構造の側を

$$
oxed{
	ext{uniform}
	o
	ext{periodic}
	o
	ext{quasiperiodic}
	o
	ext{random}
}
$$

と動かす方向である。

ただし新規ノートは空欄を埋めるためには作らない。

たとえば quasiperiodic bond を考えるなら、

$$
C_i(r)
=
prod_{m=0}^{r-1}
	anh(eta J_{i+m})
$$

に、周期でもランダムでもない結合列の秩序がどう残るか、という独立した問いが立ったときに進む。

Ising 系では今後も、

$$
oxed{
	ext{何を固定し、
どの座標だけを動かしたか}
}
$$

を先に決めてから個別模型を見る。

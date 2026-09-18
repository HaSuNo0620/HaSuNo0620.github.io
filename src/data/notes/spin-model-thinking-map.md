---
title: "スピン系をどう読むか — 状態空間・相互作用範囲・空間構造"
summary: "1次元 classical cosine スピン系を、状態空間 / 対称性、相互作用範囲 R、空間構造という模型座標で整理する。各模型座標には個別ノートを1本だけ置き、比較ノートは一つの軸だけを動かす橋として扱う。現在は一様系の R×対称性平面が閉じている。"
publishedAt: 2026-09-16T03:45:00+09:00
updatedAt: 2026-09-19
area: "Physics"
topics: ["statistical mechanics", "spin models", "transfer matrix", "memory", "linear response"]
status: growing
---

Ising、clock、XY を別々の模型名として並べるだけでは、何を変えたことで物理が変わったのかが見えにくい。

現在のノート群では、1次元 classical cosine 系を

$$
\boxed{
H
=
-\sum_i\sum_{r=1}^{R}
J_{i,r}
\cos(\theta_{i+r}-\theta_i)
}
$$

という共通形に置き、

$$
\boxed{
\text{模型座標}
=
(\text{状態空間 / 対称性},\ R,\ \text{空間構造})
}
$$

で整理する。

相互作用族は当面 cosine に固定する。

$$
\boxed{
V(\Delta\theta)=-J\cos\Delta\theta
}
$$

したがって、今見ている違いは「別の相互作用関数」ではなく、同じ相互作用族の中で

- 局所状態が何を取りうるか
- どこまで離れた自由度を結ぶか
- 結合が空間のどこでどう変化するか

を分けて動かしたものである。

---

## 1. 状態空間 / 対称性 — 何を記憶できるか

局所状態空間は

$$
\boxed{
Z_2
\longrightarrow
Z_q
\longrightarrow
U(1)
}
$$

と並べる。

具体的には

$$
\theta_i\in
\begin{cases}
\{0,\pi\}, & Z_2,\\[4pt]
\left\{\dfrac{2\pi n}{q}\right\}, & Z_q,\\[8pt]
S^1, & U(1).
\end{cases}
$$

$Z_2$ では

$$
\cos(\theta_i-\theta_j)=s_is_j,
\qquad
s_i=\pm1,
$$

なので標準 Ising 相互作用を cosine-$Z_2$ として厳密に含められる。

局所増分で見ると、

$$
Z_2:\quad
\tau_i=s_is_{i+1}=\pm1,
$$

$$
Z_q,\ U(1):\quad
\phi_i=\theta_{i+1}-\theta_i.
$$

したがって状態空間軸は、

$$
\boxed{
\text{二値の反転記憶}
\to
\text{有限角度の増分記憶}
\to
\text{連続位相増分の記憶}
}
$$

という変化として読める。

最近接では特に、

$$
\{0,\pi\}
\to
\left\{\frac{2\pi a}{q}\right\}
\to
S^1
$$

という**記憶アルファベットの細分化**がそのまま転送スペクトルの細分化につながる。

有限 $q$ と $U(1)$ の差は、単に状態数の大小ではない。角度刻み

$$
\Delta\phi=\frac{2\pi}{q}
$$

と熱揺らぎ幅

$$
\sigma_T\sim K^{-1/2},
\qquad
K=\beta J
$$

の比

$$
\boxed{
\eta
\sim
\frac{2\pi\sqrt K}{q}
}
$$

によって、離散ジャンプとして見えるか、連続的な位相拡散として見えるかが変わる。

---

## 2. 相互作用範囲 \(R\) — どこまで履歴を読むか

相互作用範囲を変えても、局所状態空間そのものは変わらない。

$Z_2$ では

$$
s_i s_{i+r}
=
\prod_{m=0}^{r-1}\tau_{i+m},
$$

なので

$$
\boxed{
H
=
-\sum_i\sum_{r=1}^{R}
J_r
\prod_{m=0}^{r-1}\tau_{i+m}
}
$$

となる。

したがって

$$
R=1:
\quad
\text{独立なドメイン壁},
$$

$$
R=2:
\quad
\text{相互作用するドメイン壁},
$$

$$
R=n:
\quad
\text{高次ドメイン壁相互作用}
$$

へ進む。

$Z_q$ と $U(1)$ でも

$$
\theta_{i+r}-\theta_i
=
\sum_{m=0}^{r-1}\phi_{i+m}
$$

なので、

$$
\boxed{
H
=
-\sum_i\sum_{r=1}^{R}
J_r
\cos\left(
\sum_{m=0}^{r-1}\phi_{i+m}
\right)
}
$$

となる。

ここから

$$
\boxed{
R
=
\text{局所統計を閉じるために必要な空間履歴の深さ}
}
$$

という見方が出る。

増分表示では、有限範囲 $R$ に対して直前の $R-1$ 個の増分を保持すればよい。

したがって履歴空間は

$$
\boxed{
\{0,\pi\}^{R-1}
\to
\mathbb Z_q^{\,R-1}
\to
(S^1)^{R-1}
}
$$

となる。

この形にすると、

$$
\boxed{
R
=
\text{履歴の深さ}
}
$$

と

$$
\boxed{
Z_2\to Z_q\to U(1)
=
\text{履歴1要素あたりの分解能}
}
$$

を明確に分けられる。

---

## 3. 空間構造 — 記憶則がどこで変わるか

相互作用範囲と状態空間を固定したまま、結合の位置依存性を変える方向が空間構造軸である。

最近接なら

$$
H=-\sum_iJ_i\,V(x_i,x_{i+1})
$$

として、

$$
J_i=J
$$

なら一様、

$$
J_{i+p}=J_i
$$

なら周期、

Fibonacci 列などに従えば準周期、

確率変数ならランダムとなる。

例えば最近接 $Z_2$ では

$$
H=-\sum_iJ_i\tau_i
$$

なので、周期化してもドメイン壁同士は独立なままである。

変わるのは

$$
\boxed{
\text{壁を作りやすい場所の空間規則}
}
$$

である。

零外場では

$$
\boxed{
C_i(r)
=
\prod_{n=0}^{r-1}
\tanh(\beta J_{i+n})
}
$$

なので、Hamiltonian に入れた空間列が相関の空間構造へ直接写る。

この軸では

$$
\boxed{
\text{一様}
\to
\text{周期}
\to
\text{準周期}
\to
\text{ランダム}
}
$$

を順に動かす。

---

## 4. 一つの模型座標には一つの個別ノートだけを置く

現在は

$$
\boxed{
\text{1模型座標}
=
\text{1個別ノート}
}
$$

を原則にしている。

同じ

$$
(d,\ \text{空間構造},\ R,\ \text{相互作用族},\ \text{状態空間})
$$

を持つ内容を、外場、カイラリティ、構造因子などの話題ごとに別ノートへ分けない。

それらは同じ模型の異なる観測・表現なので、**一つの個別ノート内の節としてまとめる**。

現在の個別模型は次のようになる。

| 空間構造 | $R$ | $Z_2$ | $Z_q$ | $U(1)$ |
| --- | --- | --- | --- | --- |
| 一様 | $1$ | [模型](/notes/ising-transfer-matrix) | [模型](/notes/clock-chain-nearest-neighbor) | [模型](/notes/xy-chain-nearest-neighbor) |
| 一様 | $2$ | [模型](/notes/ising-r2-transfer-matrix) | [模型](/notes/clock-chain-second-neighbor) | [模型](/notes/xy-chain-second-neighbor) |
| 一様 | $n$ | [模型](/notes/ising-rn-transfer-matrix) | [模型](/notes/clock-chain-finite-range) | [模型](/notes/xy-chain-finite-range) |
| 周期 | $1$ | [模型](/notes/ising-r1-periodic) | — | — |

このうち周期 $R=1,Z_2$ では、零外場の構造波数と周期外場応答を同じ個別ノートに統合している。

一様 $R=2,U(1)$ でも、螺旋記憶、カイラリティキンク、複数の記憶長、一様・周期・回転外場への応答を同じ個別ノートに統合している。

---

## 5. \(R\times\) 状態空間の基準平面は閉じた

一様・classical・cosine を固定した断面では、

| 相互作用範囲 | $Z_2$ | $Z_q$ | $U(1)$ | 比較 |
| --- | --- | --- | --- | --- |
| $R=1$ | [模型](/notes/ising-transfer-matrix) | [模型](/notes/clock-chain-nearest-neighbor) | [模型](/notes/xy-chain-nearest-neighbor) | [比較](/notes/ising-xy-nearest-neighbor-comparison) |
| $R=2$ | [模型](/notes/ising-r2-transfer-matrix) | [模型](/notes/clock-chain-second-neighbor) | [模型](/notes/xy-chain-second-neighbor) | [比較](/notes/ising-xy-second-neighbor-comparison) |
| $R=n$ | [模型](/notes/ising-rn-transfer-matrix) | [模型](/notes/clock-chain-finite-range) | [模型](/notes/xy-chain-finite-range) | [比較](/notes/finite-range-symmetry-comparison) |
| **\(R\) 比較** | [比較](/notes/ising-range-comparison) | — | — | — |

したがって

$$
\boxed{
(R=1,\ R=2,\ R=n)
\times
(Z_2,\ Z_q,\ U(1))
}
$$

の基準平面は埋まった。

ここで見えている共通構造は、

$$
\boxed{
\text{履歴の深さ}
\times
\text{履歴の分解能}
}
$$

である。

この平面は今後、新しい模型点を増やす場所というより、空間構造や相互作用族を動かしたときの**基準面**として使う。

---

## 6. 比較ノートは模型点を増やさず、軸を横断する

比較ノートは独立した模型ではない。

$$
\boxed{
\text{比較ノート}
=
\text{一つの模型座標だけを動かす橋}
}
$$

とする。

現在は、

- $R=1$ 固定で $Z_2\leftrightarrow Z_q\leftrightarrow U(1)$
- $R=2$ 固定で $Z_2\leftrightarrow Z_q\leftrightarrow U(1)$
- $R=n$ 固定で $Z_2\leftrightarrow Z_q\leftrightarrow U(1)$
- $Z_2$ 固定で $R=1\leftrightarrow R=2\leftrightarrow R=n$

の比較がある。

比較ノートでは個別導出を繰り返さず、

$$
\boxed{
\text{模型A}
\leftrightarrow
\text{共通量}
\leftrightarrow
\text{模型B}
}
$$

という辞書を作る。

共通して追う量は、

$$
\text{局所増分},
\qquad
\text{履歴次数},
\qquad
\text{転送対象},
\qquad
\xi,
\qquad
q_{\rm corr},
\qquad
\chi(Q)
$$

などである。

---

## 7. 各個別ノートは応答まで通す

個別ノートでは、内部構造だけで終わらず、外からどう読めるかまでつなぐ。

共通 spine は

$$
\boxed{
\text{Hamiltonian}
\to
\text{局所記憶変数}
\to
\text{転送スペクトル / 長距離記憶}
\to
\text{一様外場}
\to
\text{周期外場}
\to
\text{応答波数}
}
$$

である。

一様外場は

$$
Q=0
$$

を読む。

周期外場

$$
h_i=h_Q\cos(Qi+\varphi)
$$

は

$$
\boxed{
\delta O(Q)
=
\chi(Q)h_Q
}
$$

として波数依存応答を読む。

$U(1)$ 系ではさらに

$$
\boxed{
H_{\rm rot}
=
-h\sum_i
\cos(\theta_i-Qi-\varphi)
}
$$

という回転外場を使い、螺旋波数やカイラリティへ位相整合できる。

したがって、

$$
\boxed{
\text{内部の記憶}
\longrightarrow
\text{外場で観測される応答}
}
$$

までを一つの模型ノートの中で閉じる。

---

## 8. 実際に使っている近似・表現

模型座標とは別に、同じ模型をどう読むかという表現がある。

ただし、現在のノート群で実際に使っているものだけを区別する。

### 転送行列 / 転送作用素

これはほぼ全系列の共通言語になっている。

離散状態では

$$
T\psi_a=\lambda_a\psi_a,
$$

連続状態では

$$
\mathcal T\psi_a=\lambda_a\psi_a.
$$

固有値の絶対値から

$$
\boxed{
\xi_a^{-1}
=
-\ln\left|
\frac{\lambda_a}{\lambda_0}
\right|
}
$$

が出る。

複素位相を持つ傾斜スペクトルでは

$$
\boxed{
q_a=\arg\lambda_a
}
$$

が長距離相関の空間位相になる。

したがって転送法は、

$$
\boxed{
\text{局所統計}
\to
\text{長距離記憶}
\to
\text{応答}
}
$$

をつなぐ主たる表現である。

### 長波長展開 + 鞍点

これは現在、[一様第二近接 cosine-$U(1)$ 系](/notes/xy-chain-second-neighbor) で実際に使っている。

Lifshitz 点近傍で格子 Hamiltonian を展開し、

$$
F[\phi]
=
\int dx
\left[
\frac{B}{2}(\partial_x\phi)^2
+
V(\phi)
\right]
$$

という連続場を導く。

その極値を Euler--Lagrange 方程式で求めることで、

$$
\phi_{\rm kink}(x)
$$

や kink energy を得る。

これは独立に仮定した平均場模型ではなく、

$$
\boxed{
\text{格子模型}
\to
\text{小振幅・長波長展開}
\to
\text{鞍点}
}
$$

という近似である。

したがって「平均場」というより、**Landau--Ginzburg 型の有効場を鞍点で読む**と表現する方が正確である。

### Bethe / cavity はまだ使っていない

Bethe / cavity は局所条件付き確率を扱う自然な候補ではあるが、現在の個別ノートでは実際には導入していない。

したがって現段階の上位構造には含めない。

必要になった時点で、

$$
P(x_{i+1}\mid x_i,\ldots)
$$

を転送法とは別の近似として導入する。

---

## 9. 現在もっとも空いているのは空間構造軸

$R\times$ 状態空間の一様平面は閉じた。

一方、空間構造軸はまだ

$$
\boxed{
\text{一様}
\to
\text{周期}
}
$$

までしか進んでいない。

次に自然なのは

$$
\boxed{
\text{周期}
\to
\text{準周期}
}
$$

である。

最近接 $Z_2$ なら、

$$
C_i(r)
=
\prod_{n=0}^{r-1}
\tanh(\beta J_{i+n})
$$

という厳密な積構造を保ったまま、有限単位胞だけを失わせられる。

Fibonacci bond を使えば、

$$
\boxed{
\text{指数減衰}
\times
\text{準周期変調}
}
$$

が相関へどう現れるかを直接追える。

その次に random bond へ進めば、

$$
\boxed{
\text{一様}
\to
\text{周期}
\to
\text{準周期}
\to
\text{ランダム}
}
$$

という空間構造軸がつながる。

---

## 得られた見方

現在の基準系列は

$$
\boxed{
\text{cosine family fixed}
}
$$

のもとで、

$$
\boxed{
\text{状態空間 / 対称性}
\times
\text{相互作用範囲}
\times
\text{空間構造}
}
$$

という模型座標で整理できる。

このうち一様系の

$$
\boxed{
R\times(Z_2,Z_q,U(1))
}
$$

平面はすでに閉じた。

そこから得られた中心像は、

$$
\boxed{
R
=
\text{履歴の深さ}
}
$$

と

$$
\boxed{
Z_2\to Z_q\to U(1)
=
\text{履歴の分解能}
}
$$

である。

さらに各模型は、

$$
\boxed{
\text{内部記憶}
\to
\text{転送スペクトル}
\to
\text{一様・周期外場応答}
}
$$

まで一つの個別ノート内で閉じる。

次に動かすべき座標は空間構造であり、

$$
\boxed{
\text{periodic}
\to
\text{quasiperiodic}
}
$$

が現在もっとも自然な延長になる。

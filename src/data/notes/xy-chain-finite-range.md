---
title: "1次元一様有限範囲 cosine-U(1) スピン系 — 連続位相履歴と複数モード"
summary: "有限範囲の1次元U(1) cosineスピン鎖を、連続位相増分の有限履歴、(S1)^(R-1)上の転送作用素、複数の選好ねじれ、相関モード競合という構造で整理する。R=1の位相拡散とR=2の螺旋相関を一般の有限範囲へ拡張する。"
publishedAt: 2026-09-19T03:10:00+09:00
updatedAt: 2026-09-19
area: "Physics"
topics: ["statistical mechanics", "XY model", "finite-range interaction", "transfer operator", "finite memory", "helical order", "correlation"]
status: growing
system:
  dimension: 1
  spatial: uniform
  range: Rn
  interaction: cosine
  symmetry: [U(1)]
  mechanics: classical
  role: model
---

最近接では位相増分は独立に拡散し、第二近接では隣接する位相増分が相互作用して有限ねじれが生じた。有限範囲まで伸ばすと、局所エネルギーは有限長の**連続位相履歴**を読む。

$$
\phi_i=\theta_{i+1}-\theta_i\in S^1.
$$

Hamiltonian は

$$
\boxed{
H=
-\sum_i\sum_{r=1}^{R}
J_r\cos(\theta_{i+r}-\theta_i)
}
$$

である。

## 系の座標

$$
\boxed{
(d=1,\ \text{一様},\ R=n,\ \text{cosine},\ U(1))
}
$$

局所変数は一貫して $\phi_i$ であり、相互作用範囲だけを伸ばす。

## 1. 有限範囲は連続位相増分の有限履歴を結ぶ

角度差は

$$
\theta_{i+r}-\theta_i =
\sum_{m=0}^{r-1}\phi_{i+m}
$$

なので、

$$
\boxed{
H=
-\sum_i\sum_{r=1}^{R}
J_r
\cos\left(
\sum_{m=0}^{r-1}\phi_{i+m}
\right)
}
$$

となる。

したがって

$$
\boxed{
R=1:\ \text{独立な位相増分}
\to
R=2:\ \text{1ステップ相関}
\to
R:\ \text{最大 }R-1\text{ ステップ相関}
}
$$

である。

## 2. 転送状態は $(S^1)^{R-1}$ 上の連続履歴になる

最大距離 $R$ の局所重みを決めるには、直前の $R-1$ 個の位相増分を保持すればよい。

$$
\boxed{
\boldsymbol\phi_i =
(\phi_{i-R+2},\ldots,\phi_i)
\in
(S^1)^{R-1}
}
$$

次の増分 $\phi'$ を加えると、

$$
(\phi_1,\ldots,\phi_{R-1})
\longrightarrow
(\phi_2,\ldots,\phi_{R-1},\phi')
$$

と履歴窓が一つ進む。

したがって転送対象は、有限次元行列ではなく

$$
\boxed{
(S^1)^{R-1}
\text{ 上の積分作用素}
}
$$

になる。

$R$ は連続状態空間の次元を増やすのではなく、**同時に保持する過去の位相増分数**を増やしている。

## 3. 一様ねじれのエネルギーは有限 Fourier 多項式になる

一様ねじれ $\phi_i=q$ なら

$$
\boxed{
e_R(q) =
-\sum_{r=1}^{R}J_r\cos(rq)
}
$$

である。

$R=1$ では極小は基本的に $q=0$ または $\pi$ に限られる。

$R=2$ では競合結合によって有限 $q_\ast$ が生じうる。

一般の有限 $R$ では

$$
\boxed{
\frac{de_R}{dq} =
\sum_{r=1}^{R}
rJ_r\sin(rq) =
0
}
$$

となり、複数の非零ねじれ候補を持てる。

したがって相互作用範囲の増加は、

$$
\boxed{
\text{一つの選好波数}
\longrightarrow
\text{複数の局所選好波数候補}
}
$$

を可能にする。

## 4. カイラリティも一つの二値セクターで閉じない場合がある

相互作用が反転対称

$$
e_R(q)=e_R(-q)
$$

なら、非零極小は $\pm q_\ast$ の対で現れる。

ただし一般の有限 $R$ では

$$
\pm q_1,\qquad
\pm q_2,\qquad
\ldots
$$

という複数の局所極小が共存しうる。

その場合、低温の粗視化は単純な

$$
+q_\ast
\leftrightarrow
-q_\ast
$$

だけではなく、

$$
\boxed{
\{\pm q_1,\pm q_2,\ldots\}
}
$$

の間の遷移を持つ多セクター問題になる。

## 5. 長距離相関は複数の転送モードから作られる

転送作用素の固有値を

$$
\Lambda_a =
|\Lambda_a|e^{iq_a}
$$

とすると、

$$
\xi_a^{-1} =
-\ln\left|
\frac{\Lambda_a}{\Lambda_0}
\right|
$$

が各モードの相関長になる。

一般には

$$
\boxed{
C(r)
\sim
\sum_a
A_a
e^{-r/\xi_a}
\cos(q_a r+\varphi_a)
}
$$

である。

したがって有限範囲化によって、

$$
\boxed{
\text{単一の位相拡散}
\to
\text{螺旋的な相関}
\to
\text{複数の螺旋相関モード}
}
$$

へ進む。

## 6. 局所選好波数・相関波数・応答波数はさらに分離する

局所エネルギーが選ぶ波数を $q_\ast$、最長距離を支配する転送モードの位相を $q_{\rm corr}$、構造因子または感受率の最大位置を $Q_{\rm peak}$ とすると、

$$
\boxed{
q_\ast,\qquad
q_{\rm corr},\qquad
Q_{\rm peak}
}
$$

は一般に別の量である。

有限範囲ではさらに局所候補 $q_{\ast,a}$ や転送候補 $q_a$ が複数存在しうるので、

$$
\boxed{
\text{局所エネルギーのモード選択}
\to
\text{長距離モード選択}
\to
\text{応答ピーク}
}
$$

という三段階を分ける必要がある。

## 7. 有限 $q$ 系はこの連続履歴空間の離散化になる

$Z_q$ では

$$
\phi_i =
\frac{2\pi a_i}{q}
$$

なので、

$$
(S^1)^{R-1}
$$

は

$$
\mathbb Z_q^{\,R-1}
$$

へ離散化される。

したがって

$$
\boxed{
Z_q
\to
U(1)
}
$$

は有限範囲でも単なる一変数の連続極限ではなく、

$$
\boxed{
\mathbb Z_q^{\,R-1}
\to
(S^1)^{R-1}
}
$$

という**履歴空間全体の連続化**として読める。


## 8. 一様外場と周期外場は長距離モード選択を観測する

固定方向の外場を

$$
H_h =
-\sum_i h_i\cos\theta_i
$$

として加える。

一様外場 \(h_i=h\) は \(Q=0\) 成分を読み、

$$
m_x=\chi(0)h+O(h^3)
$$

となる。

周期外場

$$
h_i=h_Q\cos(Qi+\varphi)
$$

では

$$
\boxed{
\delta\langle\cos\theta_i\rangle =
\chi(Q)h_Q\cos(Qi+\varphi)
+O(h_Q^3)
}
$$

である。

有限範囲では複数の長距離モード \(q_a\) が競合できるため、

$$
\boxed{
Q_{\rm peak} =
\operatorname*{arg\,max}_Q\chi(Q)
}
$$

は、どのモードが外場から最も強く見えるかを表す。

さらに回転外場

$$
H_{\rm rot} =
-h\sum_i
\cos(\theta_i-Qi-\varphi)
$$

を用いれば、特定の螺旋波数 \(Q\) に直接位相整合できる。

したがって有限範囲 \(U(1)\) 系では、

$$
\boxed{
q_{\ast,a}
\quad\text{局所選好},
\qquad
q_a
\quad\text{長距離相関},
\qquad
Q_{\rm peak}
\quad\text{外場応答}
}
$$

を分離して読むことが必要になる。

## 得られた見方

有限範囲 $U(1)$ 系では

$$
\boxed{
R =
\text{連続位相履歴の深さ}
}
$$

である。

最近接で見えた位相拡散、第二近接で見えた螺旋・カイラリティは、一般の有限範囲では

$$
\boxed{
\text{有限履歴上の連続確率過程}
+
\text{複数の選好波数}
+
\text{複数の長距離モード}
}
$$

へ一般化される。

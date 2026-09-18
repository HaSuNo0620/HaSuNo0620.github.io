---
title: "1次元一様有限範囲 cosine-Zq スピン系 — 離散位相履歴と有限履歴"
summary: "有限範囲の1次元Zq cosineスピン鎖を、離散位相増分の有限履歴、q^(R-1)状態の転送過程、離散ねじれのロッキング、複数相関モードという構造で整理する。Z2の高次ドメイン壁相関とU(1)の連続位相履歴の間を埋める。"
publishedAt: 2026-09-19T03:05:00+09:00
updatedAt: 2026-09-19
area: "Physics"
topics: ["statistical mechanics", "clock model", "spin model", "finite-range interaction", "transfer matrix", "finite memory", "frustration"]
status: growing
system:
  dimension: 1
  spatial: uniform
  range: Rn
  interaction: cosine
  symmetry: [Zq]
  mechanics: classical
  role: model
---

第二近接では隣接する二つの離散位相増分が相互作用した。有限範囲まで伸ばすと、局所エネルギーは有限長の**離散位相履歴**を読む。

$$
\theta_i=\frac{2\pi n_i}{q},
\qquad
n_i\in\mathbb Z_q,
$$

$$
\phi_i=\theta_{i+1}-\theta_i
=\frac{2\pi a_i}{q},
\qquad
a_i\in\mathbb Z_q.
$$

有限範囲 Hamiltonian は

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
(d=1,\ \text{一様},\ R=n,\ \text{cosine},\ Z_q)
}
$$

$q=2$ では有限範囲 $Z_2$、$q\to\infty$ では有限範囲 $U(1)$ へつながる。

## 1. 距離 $r$ の結合は長さ $r$ の位相増分列を読む

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
R=1:\ \text{独立な離散増分}
\to
R=2:\ \text{1ステップ依存}
\to
R:\ \text{最大 }R-1\text{ ステップ依存}
}
$$

である。

相互作用範囲を伸ばしても、局所変数そのものは離散角 $\phi_i$ のままである。変わるのは、次の増分を決めるために必要な過去の増分数である。

## 2. 転送状態は離散位相履歴になる

最大距離が $R$ なら、次の増分を加えるときに必要なのは直前の $R-1$ 個の増分である。

$$
\boxed{
\boldsymbol a_i =
(a_{i-R+2},\ldots,a_i)
\in
\mathbb Z_q^{\,R-1}
}
$$

したがって増分表示での転送状態数は

$$
\boxed{
q^{R-1}
}
$$

になる。

遷移は

$$
(a_1,\ldots,a_{R-1})
\longrightarrow
(a_2,\ldots,a_{R-1},a_R)
$$

という有限長の窓の移動である。

$$
\boxed{
\text{有限相互作用範囲}
\Longleftrightarrow
\text{有限状態の高次マルコフ過程}
}
$$

と読める。

## 3. 一様ねじれは離散候補の中から選ばれる

一様ねじれ $\phi_i=\phi$ では、1サイトあたりのエネルギーは

$$
\boxed{
e_R(\phi) =
-\sum_{r=1}^{R}J_r\cos(r\phi)
}
$$

となる。

ただし $Z_q$ では

$$
\phi_a=\frac{2\pi a}{q}
$$

しか許されないため、

$$
\boxed{
a_\ast =
\operatorname*{arg\,min}_{a\in\mathbb Z_q}
\left[
-\sum_{r=1}^{R}
J_r\cos\left(\frac{2\pi r a}{q}\right)
\right]
}
$$

から

$$
q_\ast^{(q)}=\frac{2\pi a_\ast}{q}
$$

が決まる。

$R=2$ では単一のロッキング階段を見るだけだったが、一般の有限 $R$ では $e_R(\phi)$ 自体が複数の局所極小を持ちうる。

したがって有限 $q$ では

$$
\boxed{
\text{複数の連続候補}
+
\text{角度格子へのロッキング}
}
$$

が重なる。

## 4. 有限範囲では複数の相関モードが競合できる

転送行列の副次固有値を

$$
\Lambda_a =
|\Lambda_a|e^{iq_a}
$$

と書けば、それぞれが

$$
\xi_a^{-1} =
-\ln\left|
\frac{\Lambda_a}{\Lambda_0}
\right|,
\qquad
q_a=\arg\Lambda_a
$$

を持つ。

一般の有限範囲では候補モードが増えるため、

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

という複数モード構造が自然になる。

有限 $q$ では、これらのモード自身も離散角度空間の影響を受ける。

## 5. 長距離スピン相関には傾斜転送行列が必要になる

スピン相関は

$$
e^{i(\theta_r-\theta_0)} =
\prod_{j=0}^{r-1}e^{i\phi_j}
$$

を読む。

したがって平衡確率を伝える転送行列だけでなく、位相因子を組み込んだ傾斜転送行列の支配固有値が長距離相関を決める。

$$
\boxed{
|\Lambda_\ast|
\longrightarrow
\text{相関長},
\qquad
\arg\Lambda_\ast
\longrightarrow
\text{相関波数}
}
$$

という構造は $R=2$ と同じだが、有限範囲では候補となるモード数が増える。

## 6. $q=2$ では高次ドメイン壁相互作用を回収する

$q=2$ では

$$
\phi_i\in\{0,\pi\},
\qquad
\tau_i=e^{i\phi_i}=\pm1.
$$

このとき

$$
\cos\left(
\sum_{m=0}^{r-1}\phi_{i+m}
\right) =
\prod_{m=0}^{r-1}\tau_{i+m}
$$

なので、

$$
\boxed{
H =
-\sum_i\sum_{r=1}^{R}
J_r
\prod_{m=0}^{r-1}\tau_{i+m}
}
$$

となる。

これは有限範囲 $Z_2$ の高次ドメイン壁相互作用そのものである。

## 7. $q\to\infty$ では履歴空間そのものが連続化する

$q$ を増やすと

$$
\mathbb Z_q^{\,R-1}
\longrightarrow
(S^1)^{R-1}.
$$

したがって転送対象は

$$
\boxed{
q^{R-1}\text{ 状態の行列}
\longrightarrow
(S^1)^{R-1}\text{ 上の積分作用素}
}
$$

へ移る。

有限 $q$ は単なる角度刻みではなく、**有限履歴空間そのものの離散化**として位置づけられる。


## 8. 一様外場と周期外場は複数の離散相関モードを読む

固定方向の外場を

$$
H_h =
-\sum_i h_i\cos\theta_i
$$

として加える。

一様外場 \(h_i=h\) では \(Q=0\) の応答、

$$
m_x=\chi(0)h+O(h^3)
$$

を読む。

周期外場

$$
h_i=h_Q\cos(Qi+\varphi)
$$

なら

$$
\boxed{
\delta\langle\cos\theta_i\rangle =
\chi(Q)h_Q\cos(Qi+\varphi)
+O(h_Q^3)
}
$$

となる。

有限範囲では複数の転送モード

$$
\Lambda_a =
|\Lambda_a|e^{iq_a}
$$

が存在しうるため、\(\chi(Q)\) はそれらを全距離で重ねた応答になる。

したがって

$$
\boxed{
\{q_a\}
\longrightarrow
\chi(Q)
\longrightarrow
Q_{\rm peak}
}
$$

を区別する。

回転外場

$$
H_{\rm rot} =
-h\sum_i\cos(\theta_i-Qi-\varphi)
$$

を用いれば、離散ねじれ候補のどれに位相整合するかも直接調べられる。有限 \(q\) では、この応答にも角度格子へのロッキングが残る。

## 得られた見方

有限範囲 $Z_q$ 系では、

$$
\boxed{
R =
\text{離散位相履歴の深さ}
}
$$

である。

一方、

$$
\boxed{
q =
\text{各履歴要素の角度分解能}
}
$$

である。

したがって $R$ と $q$ は、

$$
\boxed{
\text{履歴の長さ}
\times
\text{履歴一要素の分解能}
}
$$

という二つの独立した方向として読める。

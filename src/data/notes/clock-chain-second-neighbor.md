---
title: "1次元一様第二近接 cosine-Zq スピン系 — 離散螺旋と角度記憶"
summary: "第二近接相互作用を持つ1次元Zq cosineスピン鎖を、離散位相増分の相互作用、選好ねじれの格子ロッキング、有限個のchirality sector、転送行列、相関波数と記憶長という構造で読む。Z2のinteracting wallとU(1)の連続らせんの間を埋める。"
publishedAt: 2026-09-19T02:10:00+09:00
updatedAt: 2026-09-19
area: "Physics"
topics: ["statistical mechanics", "clock model", "spin model", "second-neighbor interaction", "chirality", "transfer matrix", "frustration"]
status: growing
system:
  dimension: 1
  spatial: uniform
  range: R2
  interaction: cosine
  symmetry: [Zq]
  mechanics: classical
  role: model
---

最近接の $Z_q$ 鎖では局所位相増分 $\phi_i=\theta_{i+1}-\theta_i$ は独立だった。第二近接相互作用を加えると、
$$
\boxed{
H=
-J_1\sum_i\cos(\theta_{i+1}-\theta_i)
-J_2\sum_i\cos(\theta_{i+2}-\theta_i)
}
$$
となり、離散増分どうしが相互作用する。ここで $\theta_i=2\pi n_i/q$、$n_i\in\mathbb Z_q$ である。

## 系の座標

$$
\boxed{
(d=1,\ \text{uniform},\ R=2,\ \text{cosine},\ Z_q)
}
$$

$q=2$ で第二近接 $Z_2$、$q\to\infty$ で第二近接 $U(1)$ へつながる。

## 1. 第二近接相互作用は離散位相増分を相互作用させる

$\phi_i=2\pi a_i/q$ とおけば $\theta_{i+2}-\theta_i=\phi_i+\phi_{i+1}$ なので
$$
\boxed{
H=
-J_1\sum_i\cos\phi_i
-J_2\sum_i\cos(\phi_i+\phi_{i+1})
}
$$
となる。

したがって
$$
\boxed{
R=1:\ \text{独立な離散増分}
\quad\to\quad
R=2:\ \text{相関した離散増分}
}
$$
である。

## 2. 選好ねじれ は有限個の角度へロックされる

一様 ねじれ $\phi_i=\phi$ なら
$$
\boxed{
e(\phi)=-J_1\cos\phi-J_2\cos2\phi
}
$$
である。

ただし $Z_q$ では $\phi=\phi_a=2\pi a/q$ しか許されないので、
$$
\boxed{
a_\ast=
\operatorname*{arg\,min}_{a\in\mathbb Z_q}
\left[
-J_1\cos\frac{2\pi a}{q}
-J_2\cos\frac{4\pi a}{q}
\right]
}
$$
から
$$
\boxed{
q_\ast^{(q)}=\frac{2\pi a_\ast}{q}
}
$$
が決まる。

$U(1)$ では $\cos q_\ast=-J_1/(4J_2)$ と連続的に動けるが、有限 $q$ では $0\to2\pi/q\to4\pi/q\to\cdots$ と staircase 状にロックされる。

$$
\boxed{
\text{連続らせん}
\longrightarrow
\text{離散ねじれ locking}
}
$$

## 3. finite-$q$ では カイラリティ も離散化される

$e(\phi)=e(-\phi)$ なので、非零 ねじれ が選ばれると
$$
\boxed{
+q_\ast^{(q)},\qquad -q_\ast^{(q)}
}
$$
が縮退する。

局所 カイラリティ は $\kappa_i^{\rm ch}=\sin\phi_i$ で読める。

$Z_q$ では
$$
\boxed{
\text{カイラリティ反転}
+
\text{離散角ジャンプ}
}
$$
が 記憶-loss channel になる。

## 4. 転送行列 は $q\times q$ の離散角度 kernel になる

transfer state を $\phi_a=2\pi a/q$ とすると、対称分割した kernel は
$$
\boxed{
T_{ab} = \exp\left[
\frac{\beta J_1}{2}
(\cos\phi_a+\cos\phi_b)
+
\beta J_2\cos(\phi_a+\phi_b)
\right]
}
$$
である。

最近接 $Z_q$ の circulant matrix と異なり、一般には単純な離散 Fourier 対角化では閉じない。

有限状態 マルコフ連鎖 $P(a_{i+1}\mid a_i)$ が自然な局所記述になる。

## 5. $q=2$ では 相互作用するドメイン壁 を回収する

$q=2$ では $\tau_i=e^{i\phi_i}=\pm1$ で、$\cos\phi_i=\tau_i$、$\cos(\phi_i+\phi_{i+1})=\tau_i\tau_{i+1}$ である。
したがって
$$
\boxed{
H=
-J_1\sum_i\tau_i
-J_2\sum_i\tau_i\tau_{i+1}
}
$$
となる。

これは第二近接 $Z_2$ 鎖の interacting-wall 表現そのものである。

## 6. $q\to\infty$ では 連続転送作用素 へ移る

$q$ を増やすと $\Delta\phi=2\pi/q\to0$ なので、離散行列 $T_{ab}$ は
$$
\boxed{
\mathcal T(\phi,\phi') = \exp\left[
\frac{\beta J_1}{2}
(\cos\phi+\cos\phi')
+
\beta J_2\cos(\phi+\phi')
\right]
}
$$
へ近づく。

したがって
$$
\boxed{
2\times2
\to
q\times q
\to
\text{積分作用素}
}
$$
という 転送対象 の連続化が起こる。

## 7. 長距離 記憶 は 傾斜転送スペクトル で読む

$$
\left\langle e^{i(\theta_r-\theta_0)}\right\rangle = \left\langle
\prod_{j=0}^{r-1}e^{i\phi_j}
\right\rangle
$$
なので、位相因子を組み込んだ tilted 転送行列 の支配固有値
$$
\Lambda_\ast=|\Lambda_\ast|e^{iq_{\rm corr}}
$$
から
$$
\boxed{
\xi^{-1} = -\ln\left|\frac{\Lambda_\ast}{\Lambda_0}\right|,
\qquad
q_{\rm corr}=\arg\Lambda_\ast
}
$$
を得る。

## 8. 選好ねじれ・相関波数・応答 peak は別の量である

$$
\boxed{
q_\ast^{(q)},\qquad
q_{\rm corr},\qquad
Q_{\rm peak}
}
$$
はそれぞれ

- 局所的なエネルギー選好
- 長距離記憶 の位相
- 全距離相関を積分した 応答 peak

を表し、原理的に一致する必要はない。

これは $Z_2$ の $q_{\rm spec}\neq q_\chi$ と、$U(1)$ の $q_\ast\neq q_{\rm corr}\neq Q_{\rm peak}$ の中間に位置する。

## 9. finite-$q$ 固有の量は ねじれ-locking error である

連続 $U(1)$ の 選好ねじれ $q_\ast$ と比べ、
$$
\boxed{
\delta q_{\rm lock} = q_\ast^{(q)}-q_\ast
}
$$
を angular discretization による locking error とみなせる。

最近接 $R=1$ では finite $q$ 性は主に thermal 角度分解能 と spectral aliasing に現れた。

第二近接ではさらに
$$
\boxed{
\text{spectral discretization}
+
\text{energetic pitch locking}
}
$$
が現れる。

## 10. $Z_2\to Z_q\to U(1)$ で何が連続化されるか

実空間では
$$
\boxed{
\text{相互作用する壁}
\to
\text{ロックされた離散ねじれ}
\to
\text{連続的に相関したねじれ}
}
$$

局所遷移では
$$
\boxed{
P(\tau'|\tau)
\to
P(a'|a)
\to
P(\phi'|\phi)
}
$$

転送対象 では
$$
\boxed{
2\times2
\to
q\times q
\to
\text{積分作用素}
}
$$

となる。

## 得られた見方

第二近接 cosine 系では
$$
\boxed{
Z_2\to Z_q\to U(1)
}
$$
は
$$
\boxed{
\text{壁配置}
\to
\text{離散ねじれ locking}
\to
\text{連続らせん}
}
$$
という空間記憶の連続化として読める。

$R=1$ の finite-$q$ 性が 角度分解能 と スペクトルの折り畳み に現れたのに対し、$R=2$ では 選好ピッチ 自体が離散角へロックされる。有限 $q$ は単なる補間ではなく、**構造波数そのものが角度分解能によって量子化される領域**になる。

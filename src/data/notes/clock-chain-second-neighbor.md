---
title: "第二近接Clock鎖の基底状態と離散角度相関"
summary: "競合相互作用を持つClock鎖の基底状態を二つの隣接増分のエネルギーから厳密に求め、離散化と螺旋構造の関係を調べる。"
publishedAt: 2026-09-19T02:10:00+09:00
updatedAt: 2026-11-28
area: "Physics"
field: statistical-physics
kind: model
prerequisites: ["finite-range-symmetry-comparison"]
related: ["clock-chain-nearest-neighbor", "ising-r2-transfer-matrix", "xy-chain-second-neighbor"]
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

連続角度の第二近接XY鎖では、強磁性の最近接結合と反強磁性の第二近接結合が競合すると、一様な螺旋が基底状態になる。角度を有限個に制限したClock鎖では、螺旋の角度を離散化するだけで基底状態が求まるとは限らない。隣接する角度差が異なる配置も含めてエネルギーを最小化する必要がある。

## 増分表示と基底状態

状態数を $q\ge2$、角度を $\theta_i=2\pi n_i/q$ とし、$J_1>0$、$J_2=-\kappa J_1$、$\kappa\ge0$ とする。零外場のHamiltonianは

$$
H=-J_1\sum_i\cos\phi_i+\kappa J_1\sum_i\cos(\phi_i+\phi_{i+1}),
\quad \phi_i=\theta_{i+1}-\theta_i.
$$

角度差も $\phi_a=2\pi a/q$ のいずれかである。周期鎖では増分の総和が $2\pi$ の整数倍になる。

隣接増分のエネルギーを対称に分割して

$$
E_{ab}=J_1\left[-\frac{\cos\phi_a+\cos\phi_b}{2}
+\kappa\cos(\phi_a+\phi_b)\right]
$$

と定義する。すると $H=\sum_i E_{a_i a_{i+1}}$ である。任意の配置について $H/N\ge\min_{a,b}E_{ab}$ が成立する。ここで $E_{ab}=E_{ba}$ なので、最小値を与える増分対 $(a,b)$ を交互に繰り返すと全ての結合が下限を達成する。必要に応じて増分の周期を有限回繰り返せば元のスピン角度も周期的になる。

従って熱力学極限の基底エネルギーは厳密に

$$
e_0=\min_{a,b\in\mathbb Z_q} E_{ab}
$$

である。この模型では一般の有限範囲模型に必要な最小平均重み閉路探索が、対称な二体エネルギーの最小化へ簡約される。縮退点では、最小エネルギーの辺だけを連ねた他の配置も基底状態となりうる。

## 一様螺旋と交互増分

$a=b$ に限定した場合のエネルギーは

$$
e(\phi_a)=-J_1\cos\phi_a+\kappa J_1\cos2\phi_a.
$$

これを最小化する角度は一様螺旋の候補にすぎない。$a\ne b$ が全体の最小値を与える場合、角度差は交互に変化する。

例えば $q=2$ では、角度差は $0,\pi$ の二つである。候補のエネルギーは

| 増分対 | $E_{ab}/J_1$ |
| --- | ---: |
| $(0,0)$ | $-1+\kappa$ |
| $(0,\pi)$ | $-\kappa$ |
| $(\pi,\pi)$ | $1+\kappa$ |

となる。$\kappa>1/2$ では交互増分が選ばれ、元のスピン配置は $++--$ の周期4状態となる。一様螺旋だけを比較するとこの基底状態を見落とす。

有限 $q$ での基底状態境界は、各 $E_{ab}/J_1$ が $\kappa$ の一次関数であることを利用して求められる。候補の直線の下包絡を構成すれば、数値的な温度外挿を行わずに基底状態の切り替わりを決定できる。

増分対の和を $\Phi=\phi_a+\phi_b$ とすると、スピンの複素表示 $u_i=e^{i\theta_i}$ は $u_{i+2}=e^{i\Phi}u_i$ を満たす。従って交互増分状態のFourier成分は $\Phi/2$ と $\Phi/2+\pi$（波数は $2\pi$ を法とする）に現れうる。平均ねじれだけでは周期構造の全情報を表せない。

## 連続角度極限

XY鎖の一様螺旋の最適角度は

$$
\varphi_*=
\begin{cases}
0 & \kappa\le1/4,\\
\arccos(1/(4\kappa)) & \kappa>1/4.
\end{cases}
$$

有限Clock鎖はXY鎖の配置を制限した模型なので $e_0^{(q)}\ge e_0^{XY}$ である。一方、$\varphi_*$ に最も近い離散角を選んだ一様螺旋は変分上界を与える。$e'(\varphi_*)=0$ と角度刻み $2\pi/q$ を使えば、固定した有限の $\kappa$ に対し

$$
0\le e_0^{(q)}-e_0^{XY}=O(J_1q^{-2})
$$

が従う。基底エネルギーの収束は保証されるが、有限 $q$ で常に一様螺旋が選ばれることを意味しない。

一様螺旋に限定した角度のずれは離散化誤差として定義できる。しかし交互増分状態では、二つの増分と対応する周期構造を別々に記述する必要がある。

## 有限温度の転送行列

増分空間の転送行列は

$$
T_{ab}=e^{-\beta E_{ab}},\qquad \beta=(k_{\mathrm B}T)^{-1}
$$

である。実対称かつ全要素が正なので、最大固有値 $\lambda_0$ は単純であり、正の固有ベクトル $v$ を $\sum_a v_a^2=1$ と規格化できる。計数測度での自由エネルギー密度は $-\beta^{-1}\ln\lambda_0$ である。

熱力学極限の増分の定常分布と条件付き確率は

$$
P(a)=v_a^2,\qquad P(b\mid a)=\frac{T_{ab}v_b}{\lambda_0v_a}
$$

となる。$q=2$ では相互作用するドメイン壁の模型を回収する。$q\to\infty$ では $T/q$ が規格化円周測度を用いたXY鎖の積分作用素の離散近似となる。

## スピン相関とカイラリティ

対角行列 $(D_m)_{aa}=e^{im\phi_a}$ を導入する。距離 $r$ のスピン相関は

$$
C_m(r)=\frac{v^{\mathsf T}D_m(TD_m)^{r-1}v}{\lambda_0^{r-1}},
\qquad r\ge1.
$$

従って長距離相関の指数減衰と振動は、傾斜転送行列 $TD_m$ の寄与する固有値から決まる。固有値 $z$ が支配的なら $\xi^{-1}=-\ln|z/\lambda_0|$、相関波数は $\arg z$ である。縮退や振幅の消失には注意が必要である。

局所カイラリティを $\chi_a=\sin\phi_a$ と定めると、その相関は通常の転送行列 $T$ で計算できる。

$$
\langle\chi_0\chi_r\rangle
=\lambda_0^{-r}v^{\mathsf T}D_\chi T^rD_\chi v,
\qquad (D_\chi)_{aa}=\sin\phi_a.
$$

反転 $\phi\mapsto-\phi$ に対して奇の観測量なので、偶の最大固有ベクトルから奇セクターへの行列要素が相関を決める。有限温度では反転対称性が保たれ、平均カイラリティはゼロとなる。一様螺旋の正負が異なる状態になるのは $\phi\ne0,\pi$ の場合であり、交互増分ではカイラリティの局所分布や周期性も調べる必要がある。

## 外場応答

固定方向の外場 $-\sum_i h_i\cos\theta_i$ に対する線形感受率は、$q>2$ で

$$
\chi_{xx}(Q)=\frac{\beta}{2}\left[1+2\sum_{r\ge1}
\operatorname{Re}C_1(r)\cos(Qr)\right]
$$

となる。$q=2$ では前係数は $\beta$ である。奇数 $q$ では非線形磁化の二次項が一般に許される。

回転外場 $-h\sum_i\cos(\theta_i-Qi)$ は螺旋配置に位相整合できるが、最大応答波数は基底状態のねじれや相関の固有値位相だけからは決まらない。感受率は全距離の相関を含むためである。基底状態、長距離相関、応答の区別は[第二近接Ising鎖](/notes/ising-r2-transfer-matrix/)と[第二近接XY鎖](/notes/xy-chain-second-neighbor/)にも共通する。

---
title: "第二近接XY鎖の螺旋構造とカイラリティ相関"
summary: "競合相互作用による螺旋の形成、カイラリティキンク、位相拡散と転送作用素を通じて、異なる相関長と応答波数を区別する。"
publishedAt: 2026-09-13T22:40:00+09:00
updatedAt: 2026-11-28
area: "Physics"
field: statistical-physics
kind: model
prerequisites: ["finite-range-symmetry-comparison", "xy-chain-nearest-neighbor"]
related: ["ising-r2-transfer-matrix", "clock-chain-second-neighbor"]
topics: ["statistical mechanics", "XY model", "second-neighbor interaction", "frustration", "helical order", "chirality", "correlation", "transfer operator", "linear response"]
status: growing
system:
  dimension: 1
  spatial: uniform
  range: R2
  interaction: cosine
  symmetry: [U(1)]
  mechanics: classical
  role: model
---

競合する第二近接相互作用を持つXY鎖では、基底状態のスピンが螺旋を描く。有限温度では、同じ巻き方向の領域内でも位相が揺らぎ、さらに巻き方向そのものが反転する。この二つの機構が異なる相関長を生む。

## 螺旋の基底状態

角度増分 $\phi_i=\theta_{i+1}-\theta_i$ を用いると、零外場のHamiltonianは

$$
H=-J_1\sum_i\cos\phi_i-J_2\sum_i\cos(\phi_i+\phi_{i+1})
$$

となる。以下では $J_1>0$、$J_2=-\kappa J_1$、$\kappa\ge0$ とし、$K_i=\beta J_i$、$\beta=(k_{\mathrm B}T)^{-1}$、格子間隔1とする。

一様ねじれ $\phi_i=q$ のエネルギー密度は

$$
e(q)=J_1[-\cos q+\kappa\cos2q].
$$

この模型の基底エネルギーは一様ねじれの最小値に等しい。実際、複素スピン $u_i=e^{i\theta_i}$ を周期鎖でFourier変換すると、

$$
H=\sum_k e(k)|\widehat u_k|^2,\qquad
\sum_k|\widehat u_k|^2=N.
$$

従って $H/N\ge\min_k e(k)$ であり、最小化する許容波数の螺旋が下限を達成する。熱力学極限では波数を連続的に選べる。

$e'(q)=J_1\sin q(1-4\kappa\cos q)$ より、基底状態のねじれは

$$
q_*=\begin{cases}
0&\kappa\le1/4,\\
\pm\arccos(1/(4\kappa))&\kappa>1/4.
\end{cases}
$$

となる。以下、螺旋領域で $q_*$ は正の解を表す。

![選択ねじれとねじれ剛性](/figures/xy-second-neighbor/preferred-twist-stiffness.svg)

## 長波長展開とカイラリティキンク

$\kappa=1/4+\delta$、$0<\delta\ll1$ では $q_*\simeq\sqrt{8\delta}$ である。局所増分が小さく空間的にも緩やかに変化すると仮定する。

一様な部分のエネルギーは

$$
e(\phi)=\mathrm{const}+J_1\left[-2\delta\phi^2+
\left(\frac18+\frac{2\delta}{3}\right)\phi^4+O(\phi^6)\right].
$$

格子Hamiltonianの二次項をFourier変換すると、

$$
H_2=\frac12\sum_k A(k)|\phi_k|^2,\quad
A(k)=J_1[1-2\kappa-2\kappa\cos k].
$$

従って小波数の勾配項と局所ポテンシャルの主要項を合わせると、定数を除いた連続近似のエネルギーは

$$
E[\phi]=\int dx\left[
\frac{B}{2}(\partial_x\phi)^2+
\frac{J_1}{8}(\phi^2-\phi_0^2)^2
\right],
\quad B=J_1\kappa,\quad \phi_0^2=8\delta.
$$

これは格子Hamiltonianの展開であって、熱揺らぎを積分した厳密な自由エネルギーではない。以下のキンク解は、この連続エネルギーの鞍点近似である。

局所カイラリティを $\chi_i=\sin\phi_i$ とする。二つの螺旋を接続する境界条件 $\phi(\pm\infty)=\pm\phi_0$ に対し、Euler–Lagrange方程式の第一積分は

$$
\frac B2(\phi')^2=\frac{J_1}{8}(\phi^2-\phi_0^2)^2
$$

である。解は

$$
\phi(x)=\phi_0\tanh\frac{x-x_0}{\ell_{\rm k}},
\qquad \ell_{\rm k}=\sqrt{\frac{\kappa}{2\delta}}.
$$

この幅の規約で、形成エネルギーは

$$
\begin{aligned}
E_{\rm k}
&=\int_{-\phi_0}^{\phi_0}
\sqrt{2B\frac{J_1}{8}(\phi^2-\phi_0^2)^2}\,d\phi\\
&=\frac{32\sqrt2}{3}J_1\sqrt\kappa\,\delta^{3/2}.
\end{aligned}
$$

$\delta^{3/2}$ の依存性は、井戸間のエネルギー障壁が $\delta^2$、キンク幅が $\delta^{-1/2}$ に比例することに対応する。これは $\delta\ll1$ における連続近似の主要項である。有限温度で希薄キンク近似を使うにはさらに $\beta E_{\rm k}\gg1$ が必要となる。カイラリティ相関長はこの領域で活性化型に増大するが、前因子は揺らぎや格子効果に依存する。

## 一つの螺旋領域内での位相拡散

$\phi_i=q_*+\epsilon_i$ と書き、カイラリティ反転を無視して二次まで展開する。

$$
H_2=\frac12\sum_i[J_1\cos q_*\,\epsilon_i^2+
J_2\cos2q_*(\epsilon_i+\epsilon_{i+1})^2].
$$

Fourier空間での係数は

$$
A(k)=J_1\cos q_*+2J_2\cos2q_*(1+\cos k),
$$

$$
A_0=A(0)=e''(q_*)=J_1\left(4\kappa-\frac1{4\kappa}\right).
$$

調和近似の共分散の全空間和は $k_{\mathrm B}T/A_0$ である。従って十分長い区間の増分和の分散は

$$
\left\langle\left(\sum_{i=0}^{r-1}\epsilon_i\right)^2\right\rangle
\simeq r\frac{k_{\mathrm B}T}{A_0}.
$$

一つの巻き方向の領域内では位相相関は $e^{iq_*r}e^{-r/\xi_{\rm ph}}$ に近づき、

$$
\xi_{\rm ph}=2\beta A_0
$$

となる。二つの巻き方向を等確率で平均すれば余弦型の相関を得る。ただし、これはキンクを無視した調和近似であり、全平衡系の長距離相関とは異なる。$\kappa\to1/4$ では $A_0\to0$ となるため、この近似は一様に成立しない。

## 巻き方向の反転と位相拡散の有効模型

キンクが希薄な場合、粗視化した角度場を

$$
\partial_x\theta=q_*\sigma(x)+\eta(x)
$$

と表す有効模型を考える。$\sigma=\pm1$ は空間当たりの反転率 $\nu$ を持つ対称な二状態Markov過程、$\eta$ は独立な位相雑音と仮定する。実時間の反転速度ではない。

$$
\langle\sigma(0)\sigma(r)\rangle=e^{-2\nu r},
\qquad \xi_\chi=(2\nu)^{-1}.
$$

位相雑音について $\langle e^{i\int_0^r\eta(x)dx}\rangle=e^{-Dr}$、$D=\xi_{\rm ph}^{-1}$ とする。スピン相関は $C(r)=e^{-Dr}F(r)$ となり、二つの条件付き特性関数の連立方程式を足し引きすれば

$$
F''+2\nu F'+q_*^2F=0,\quad F(0)=1,\quad F'(0)=0
$$

を得る。$q_*>\nu$ では $\omega=\sqrt{q_*^2-\nu^2}$ として

$$
F(r)=e^{-\nu r}\left[\cos(\omega r)+\frac{\nu}{\omega}\sin(\omega r)\right].
$$

従って振動領域では

$$
q_{\rm corr}=\sqrt{q_*^2-\nu^2},\qquad
\xi_{\rm spin}^{-1}=D+\nu
=\xi_{\rm ph}^{-1}+\frac1{2\xi_\chi}.
$$

$q_*\le\nu$ では指数の固有値は実数となり、振動は消失する。局所的な螺旋の選好が消えたわけではない。これらは独立な反転過程と位相雑音を仮定した有効模型の結果である。

## 構造因子の最大波数

連続有効模型の構造因子 $S(Q)=2\int_0^\infty C(r)\cos(Qr)dr$ は、Laplace変換

$$
\widetilde F(s)=\frac{s+2\nu}{s^2+2\nu s+q_*^2}
$$

から $S(Q)=2\operatorname{Re}\widetilde F(D+iQ)$ となる。

特に $D=0$、$\nu>0$、$q_*>0$ なら

$$
S(Q)=\frac{4\nu q_*^2}{(q_*^2-Q^2)^2+4\nu^2Q^2},
$$

$$
Q_{\rm peak}=\begin{cases}
\sqrt{q_*^2-2\nu^2}&\nu<q_*/\sqrt2,\\
0&\nu\ge q_*/\sqrt2.
\end{cases}
$$

従って $q_*/\sqrt2<\nu<q_*$ の領域では、振動相関が残っていても構造因子は零波数で最大となる。この境界は有効模型のものであり、格子模型にそのまま適用できない。格子模型では全距離の相関から最大波数を求める必要がある。

## 転送作用素による厳密な定式化

規格化円周測度 $d\phi/(2\pi)$ を用いる。角度増分に対する転送核は

$$
\mathcal T(\phi,\phi')=\exp\left[
\frac{K_1}{2}(\cos\phi+\cos\phi')+K_2\cos(\phi+\phi')
\right].
$$

対称な正の核であり、最大固有値 $\lambda_0$ の固有関数 $v$ を正に選び、$\langle v,v\rangle=1$ とする。Fourier基底 $e^{im\phi}$ での行列要素は

$$
T_{mn}=\sum_{\ell\in\mathbb Z}
I_{m-\ell}(K_1/2)I_{n+\ell}(K_1/2)I_\ell(K_2).
$$

これは三つの指数因子をそれぞれFourier展開し、直交性を用いた結果である。

核は反転 $\phi\mapsto-\phi$ と可換である。局所カイラリティ $\sin\phi$ は奇なので、その相関は奇セクターの固有値のうち行列要素が非零のものから決まる。絶対値最大の寄与を持つ固有値を $\lambda_\chi$ とすると、

$$
\xi_\chi^{-1}=-\ln|\lambda_\chi/\lambda_0|.
$$

一方、スピン相関には位相因子を挿入する必要がある。$(M_m f)(\phi)=e^{im\phi}f(\phi)$ とすると、

$$
C_m(r)=\lambda_0^{-(r-1)}
\langle v,M_m(\mathcal T M_m)^{r-1}v\rangle,\quad r\ge1.
$$

傾斜作用素 $\mathcal T M_m$ は一般に自己共役ではない。$m=1$ の支配固有値を $z_*$ とすれば、対応する相関長と振動波数は

$$
\xi_{\rm spin}^{-1}=-\ln|z_*/\lambda_0|,
\qquad q_{\rm corr}=\arg z_*.
$$

このように二つの相関長は異なる作用素から決まる。振幅が消える固有値や縮退した場合は個別に扱う。

## 数値例

角度格子による独立再計算の結果を以下に示す。$\kappa=0.5$、基底状態のねじれは $q_*=\pi/3$ である。相関長と相関波数は128点・256点の一様角度格子で表示精度内に一致した。構造因子の最大波数は128点格子の傾斜作用素のresolventを用いて連続波数上で最大化した。

| $\beta J_1$ | $q_{\rm corr}$ | $Q_{\rm peak}$ | $\xi_\chi$ | $\xi_{\rm spin}$ |
| ---: | ---: | ---: | ---: | ---: |
| 4 | 1.0297 | 1.0070 | 2.44 | 3.42 |
| 6 | 1.0224 | 1.0154 | 5.38 | 6.08 |
| 8 | 1.0257 | 1.0238 | 12.57 | 10.72 |
| 10 | 1.0298 | 1.0292 | 30.68 | 17.47 |
| 12 | 1.0328 | 1.0327 | 76.82 | 25.45 |
| 16 | 1.0367 | 1.0367 | 502.14 | 41.01 |

この結果では低温ほどカイラリティ相関長とスピン相関長の差が大きくなる。局所的な巻き方向はスピン方向より長距離まで相関しうる。

## 外場で測る相関

固定方向の外場 $-\sum_i h_i\cos\theta_i$ に対して、零外場の回転対称性から

$$
\chi_{xx}(Q)=\frac{\beta}{2}\sum_{r\in\mathbb Z} C_1(r)e^{-iQr}
$$

となる。ここでは反転対称性により $C_1$ は実数である。最大応答波数は $Q_{\rm peak}$ であり、$q_{\rm corr}$ と一致する保証はない。回転外場 $-h\sum_i\cos(\theta_i-Qi)$ は特定の巻き方向の螺旋に位相整合するが、零外場の対称な平衡状態では正負の回転波数に対する線形応答は等しい。

カイラリティ相関を直接測るには $-\sum_i g_i\sin\phi_i$ のように局所カイラリティと共役な外場を導入する。通常のスピン外場への応答だけでは、二つの相関長を独立に決められるとは限らない。

[第二近接Ising鎖](/notes/ising-r2-transfer-matrix/)にも振動相関と応答ピークの分離が存在するが、XY鎖では連続位相揺らぎとカイラリティ反転を区別できる点が異なる。

---
title: "一次元最近接XY鎖の位相拡散と高調波相関"
summary: "円周上の転送作用素をFourier展開し、厳密相関、低温の位相拡散、外場応答と周期境界の巻き数制約を導く。"
publishedAt: 2026-09-12T03:10:00+09:00
updatedAt: 2026-11-28
area: "Physics"
field: statistical-physics
kind: model
prerequisites: ["finite-range-symmetry-comparison"]
related: ["clock-chain-nearest-neighbor", "xy-chain-second-neighbor", "ising-transfer-matrix"]
topics: ["statistical mechanics", "XY model", "phase diffusion", "transfer operator", "correlation", "Bessel function", "compact field"]
status: growing
system:
  dimension: 1
  spatial: uniform
  range: R1
  interaction: cosine
  symmetry: [U(1)]
  mechanics: classical
  role: model
---

一次元XY鎖では、隣接スピンの角度差が小さくても、その差が空間方向に累積するため、有限温度で遠距離のスピン相関が失われる。最近接・零外場の場合、この減衰は独立な角度増分の分布から厳密に求められる。

## 円周上の転送作用素

単位スピン $\boldsymbol S_i=(\cos\theta_i,\sin\theta_i)$ に対して

$$
H=-J\sum_i\cos(\theta_{i+1}-\theta_i),
\qquad K=\beta J,\quad \beta=(k_{\mathrm B}T)^{-1}
$$

とする。以下では $J>0$、格子間隔1とし、角度の積分測度は $d\theta/(2\pi)$ に規格化する。

開鎖では $\phi_i=\theta_{i+1}-\theta_i\pmod{2\pi}$ が独立であり、その確率密度は通常のLebesgue測度に関して

$$
p(\phi)=\frac{e^{K\cos\phi}}{2\pi I_0(K)},\qquad -\pi<\phi\le\pi
$$

となる。ここで

$$
I_m(K)=\frac{1}{2\pi}\int_{-\pi}^{\pi}e^{K\cos\phi}e^{-im\phi}\,d\phi
$$

は整数次の修正Bessel関数である。

同じ結果は転送作用素

$$
(Tf)(\theta)=\int_{-\pi}^{\pi}e^{K\cos(\theta'-\theta)}
f(\theta')\frac{d\theta'}{2\pi}
$$

からも導ける。核は角度差だけに依存するので、固有関数は $e^{im\theta}$、固有値は $I_m(K)$ である。従って熱力学極限の自由エネルギー密度は $f=-\beta^{-1}\ln I_0(K)$ となる。規格化しない角度測度を用いる場合は自由エネルギーに $-\beta^{-1}\ln(2\pi)$ が加わるが、固有値比や相関は変わらない。

## 高調波ごとの厳密相関

開鎖または熱力学極限では、距離 $r$ の角度差は独立な増分の和である。その整数次Fourier成分は

$$
\begin{aligned}
C_m(r)&=\left\langle e^{im(\theta_r-\theta_0)}\right\rangle\\
&=\prod_{j=0}^{r-1}\langle e^{im\phi_j}\rangle
=\left[\frac{I_m(K)}{I_0(K)}\right]^r.
\end{aligned}
$$

通常のスピン相関は $C_1(r)=\langle\boldsymbol S_0\cdot\boldsymbol S_r\rangle$ である。$m\ne0$ の相関長は

$$
\xi_m^{-1}=-\ln\frac{I_m(K)}{I_0(K)}.
$$

有限温度かつ有限の $K>0$ では固有値比は1未満であり、全ての非自明な高調波相関が遠距離で消失する。有限の角度集合を持つClock鎖では高調波指標が状態数を法として同一視されるが、XY鎖では整数 $m$ にわたる無限の相関階層が存在する。この離散化の影響は[最近接Clock鎖](/notes/clock-chain-nearest-neighbor/)で扱う。

## 低温での位相拡散

$K\gg1$ では角度差の主値は原点近傍に集中する。$\cos\phi\simeq1-\phi^2/2$ より、局所分布は分散 $1/K$ のGaussian分布で近似できる。

円周上の角度差そのものではなく、各主値増分を実数として累積した角度 $\widetilde\theta_r-\widetilde\theta_0=\sum_{j=0}^{r-1}\phi_j$ を考えると、

$$
\left\langle(\widetilde\theta_r-\widetilde\theta_0)^2\right\rangle
\simeq\frac{r}{K}
$$

となる。この分散は円周上の角度の分散とは異なり、距離に比例して増大できる。

Gaussian近似で整数次の特性関数を取ると

$$
C_m(r)\simeq\exp\left(-\frac{m^2r}{2K}\right),
\qquad
\xi_m\simeq\frac{2K}{m^2}.
$$

同じ漸近形は、固定した $m$ に対する修正Bessel関数の大引数展開から得られる。したがって位相拡散は低温における厳密転送スペクトルの近似でもある。相関長の増大はIsing鎖の活性化型 $e^{2K}/2$ とは異なり、温度の逆数に比例する。これは、XY鎖には非零の最小角度刻みがなく、任意に小さいエネルギーの角度変化が許されるためである。

## 外場とFourierモード

$x$ 方向の一様外場 $h$ を加えると転送核は

$$
T_h(\theta,\theta')=
\exp\left[K\cos(\theta'-\theta)
+\frac{\beta h}{2}(\cos\theta+\cos\theta')\right]
$$

となる。外場は絶対角度に依存するので、角度差のみでHamiltonianを閉じることはできない。一次の摂動では $\cos\theta=(e^{i\theta}+e^{-i\theta})/2$ により、Fourier指標 $m$ と $m\pm1$ が結合する。

零外場での回転対称性から

$$
\langle\cos\theta_i\cos\theta_j\rangle
=\frac12 C_1(|i-j|).
$$

従って $t=I_1(K)/I_0(K)$ とすれば、位置依存外場への線形感受率は

$$
\chi_{xx}(Q)=\frac{\beta}{2}\frac{1-t^2}{1-2t\cos Q+t^2}.
$$

外場 $h_i=h_Q\cos(Qi+\varphi)$ に対する磁化は、反転対称性を用いて

$$
\langle\cos\theta_i\rangle=
\chi_{xx}(Q)h_Q\cos(Qi+\varphi)+O(h_Q^3)
$$

と書ける。低温・長波長では $\chi_{xx}(Q)\simeq\beta\xi_1/[1+(Q\xi_1)^2]$ となる。Ising鎖と比較したとき、感受率の前係数が半分になるのは、零外場の一成分の分散が $1/2$ であるためである。

## 周期境界と巻き数

有限の周期鎖では、全増分の和が $2\pi$ の整数倍でなければならない。主値の角度増分を採用すれば

$$
\sum_{i=0}^{N-1}\phi_i=2\pi w,\qquad w\in\mathbb Z
$$

となる。ここで $w$ は隣接角度を主値の経路で結んだときの巻き数である。格子模型では角度差が主値の分岐点を通過すれば巻き数は変化できるため、厳密に保存される量ではない。

周期境界の分配関数は

$$
Z_N=\operatorname{Tr}T^N=\sum_{m\in\mathbb Z} I_m(K)^N
$$

となる。スピン相関も転送作用素のトレースから

$$
C_m(r)=\frac{\sum_{n\in\mathbb Z}I_n(K)^{N-r}I_{n+m}(K)^r}
{\sum_{n\in\mathbb Z}I_n(K)^N},
\qquad 0\le r\le N
$$

と求められる。固定した $r$ で $N\to\infty$ とすれば、最大固有値 $I_0(K)$ の寄与が支配し、独立増分の相関式に戻る。有限環における角度差の閉路制約は、この有限サイズのスペクトル和に含まれている。

第二近接相互作用を導入すると、隣接する角度増分が相互作用する。[第二近接XY鎖](/notes/xy-chain-second-neighbor/)では、この独立増分近似が失われるとともに、競合する相互作用によって螺旋構造とカイラリティが生じる条件を調べる。

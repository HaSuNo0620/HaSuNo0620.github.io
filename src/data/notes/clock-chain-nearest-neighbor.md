---
title: "最近接Clock鎖の離散スペクトルとXY極限"
summary: "角度の離散化が相関スペクトルを折り畳む仕組みと、有限状態の活性化型相関から連続角度の位相拡散への移行を導く。"
publishedAt: 2026-09-17T10:20:00+09:00
updatedAt: 2026-11-28
area: "Physics"
field: statistical-physics
kind: model
prerequisites: ["finite-range-symmetry-comparison"]
related: ["ising-transfer-matrix", "xy-chain-nearest-neighbor", "clock-chain-second-neighbor"]
topics: ["statistical mechanics", "clock 模型", "spin model", "transfer matrix", "phase diffusion", "correlation", "Fourier spectrum"]
status: growing
system:
  dimension: 1
  spatial: uniform
  range: R1
  interaction: cosine
  symmetry: [Zq]
  mechanics: classical
  role: model
---

最近接Clock鎖では、相互作用を変えずにスピンの取りうる角度の数を増やすことで、Ising鎖からXY鎖への移行を調べられる。ただし、角度の数が多ければ常にXY鎖に近いとは限らない。低温では有限の角度刻みが励起エネルギーを決めるためである。

## 離散角度と転送スペクトル

強磁性結合 $J>0$ を持つ零外場の鎖を考える。

$$
H=-J\sum_i\cos(\theta_{i+1}-\theta_i),\qquad
\theta_i=\frac{2\pi a_i}{q},\quad a_i\in\mathbb Z_q,
$$

ここで整数 $q\ge2$ は状態数、$K=\beta J$、$\beta=(k_{\mathrm B}T)^{-1}$ とする。格子間隔は1である。開鎖または熱力学極限では隣接角度差 $\phi_i$ は独立で、

$$
P(\phi=2\pi a/q)=\frac{e^{K\cos(2\pi a/q)}}{\Lambda_0^{(q)}}.
$$

転送行列 $T_{ab}=e^{K\cos[2\pi(b-a)/q]}$ は巡回行列である。離散Fourier基底で対角化すると

$$
\Lambda_m^{(q)}
=\sum_{a=0}^{q-1}e^{K\cos(2\pi a/q)}e^{-2\pi ima/q}.
$$

計数測度を使っているので自由エネルギー密度は $-\beta^{-1}\ln\Lambda_0^{(q)}$ である。角度相関は

$$
C_m(r)=\langle e^{im(\theta_r-\theta_0)}\rangle
=\left(\frac{\Lambda_m^{(q)}}{\Lambda_0^{(q)}}\right)^r.
$$

非自明な相関の減衰長を $\xi_m^{-1}=-\ln|\Lambda_m^{(q)}/\Lambda_0^{(q)}|$ とする。有限の周期鎖では角度差の総和に閉路制約があるため、独立増分による式はそのまま適用できない。

## Ising鎖とXY鎖

$q=2$ では許される角度は $0,\pi$ の二つであり、$\Lambda_1/\Lambda_0=\tanh K$ となる。これが[最近接Ising鎖](/notes/ising-transfer-matrix/)の相関である。

一方、固定した $K,m$ に対して $q\to\infty$ とすると、規格化した離散和は積分に収束する。

$$
\frac{\Lambda_m^{(q)}}{q}\longrightarrow I_m(K)
=\frac{1}{2\pi}\int_{-\pi}^{\pi}e^{K\cos\phi}e^{-im\phi}d\phi.
$$

従って相関の固有値比は $I_m(K)/I_0(K)$ に収束する。これは[最近接XY鎖](/notes/xy-chain-nearest-neighbor/)の厳密相関である。自由エネルギーを比較する際は、有限群でも測度を $1/q$ で規格化しておく必要がある。

## 角度離散化によるスペクトルの折り畳み

円周上のBoltzmann重みをFourier展開すると

$$
e^{K\cos\phi}=\sum_{n\in\mathbb Z}I_n(K)e^{in\phi}.
$$

離散角 $\phi=2\pi a/q$ 上では、$n$ と $n+q$ のFourier成分を区別できない。離散Fourier和の直交性から

$$
\Lambda_m^{(q)}=q\sum_{\ell\in\mathbb Z}I_{m+\ell q}(K),
$$

$$
\frac{\Lambda_m^{(q)}}{\Lambda_0^{(q)}}
=\frac{\sum_\ell I_{m+\ell q}(K)}{\sum_\ell I_{\ell q}(K)}
$$

を得る。有限角度のスペクトルは、連続角度のスペクトルを整数 $q$ ごとに折り畳んだものになっている。独立な指標は $m\bmod q$ であり、実対称な相関では $m$ と $-m$ が同じ値を持つ。

![有限$q$の相関スペクトルとXY極限](/figures/clock-r1/memory-spectrum-folding.svg)

*$K=20$ における離散スペクトルと連続極限の比較。*

## 低温での励起と相関長

有限 $q$ の最小非零角度差を $\Delta=2\pi/q$ とすると、励起エネルギーは $E_q=J(1-\cos\Delta)$ である。$q\ge3$ を固定し、$K(1-\cos\Delta)\gg1$ とすれば、最小励起は正負の二つの角度差からなる。

$$
1-\frac{\Lambda_1^{(q)}}{\Lambda_0^{(q)}}
\simeq2(1-\cos\Delta)e^{-K(1-\cos\Delta)},
$$

$$
\xi_1\simeq\frac{e^{K(1-\cos\Delta)}}{2(1-\cos\Delta)}.
$$

$q=2$ では正負の励起が同じ状態なので係数が異なり、$\xi_1\simeq e^{2K}/2$ となる。有限状態数での相関長は活性化型に増大する。

XY鎖では小角度揺らぎの分散が $K^{-1}$ であり、$\xi_1\simeq2K$ となる。角度刻みと熱揺らぎ幅の比

$$
\eta=\frac{2\pi\sqrt K}{q}
$$

が離散性の尺度である。$\eta\gg1$ なら角度変化は稀な離散励起によって生じ、$\eta\ll1$ なら熱揺らぎ幅に多数の角度状態が含まれる。

### 二重スケーリング極限

$K,q\to\infty$ で $\eta$ を有限に固定する。整数 $a$ を原点近傍の角度差の指標とすると、局所分布は

$$
P(a)\longrightarrow
\frac{e^{-\eta^2a^2/2}}{\sum_{b\in\mathbb Z}e^{-\eta^2b^2/2}}
$$

となる。$\Delta=\eta/\sqrt K$ を使って余弦を展開すれば

$$
\xi_1^{-1}\sim\frac{\eta^2}{2K}
\frac{\sum_a a^2e^{-\eta^2a^2/2}}{\sum_a e^{-\eta^2a^2/2}}.
$$

従って $\xi_1/(2K)$ はこの極限で $\eta$ だけの関数となる。$\eta\to0$ では離散和をGaussian積分に置き換えることができ、その比は1に近づく。

![相関長のClockからXYへの移行](/figures/clock-r1/correlation-length-crossover.svg)

*角度の状態数と熱揺らぎ幅の比による相関長の整理。*

固定温度では $q\to\infty$ によりXY鎖を回収するが、固定した有限 $q$ では低温にすると活性化型の漸近形が支配する。非可換性は相関長の比によって明示できる。

$$
\lim_{K\to\infty}\lim_{q\to\infty}\frac{\xi_1^{(q)}}{\xi_1^{XY}}=1,
\qquad
\lim_{q\to\infty}\lim_{K\to\infty}\frac{\xi_1^{(q)}}{\xi_1^{XY}}=\infty.
$$

## 高調波相関

連続角度では固定した整数 $m$ に対し低温で $I_m(K)/I_0(K)\simeq e^{-m^2/(2K)}$ となり、$\xi_m\simeq2K/m^2$ を得る。離散角度では折り畳みによりこの階層が変わる。Gaussian近似が妥当な波数範囲では

$$
\frac{\Lambda_m^{(q)}}{\Lambda_0^{(q)}}\simeq
\frac{\sum_\ell e^{-(m+\ell q)^2/(2K)}}{\sum_\ell e^{-(\ell q)^2/(2K)}}.
$$

これは特に前節の二重スケーリング極限に適した近似であり、任意の大きな $m,q$ に一様に成立するわけではない。$0<m\le q/2$ では最近接の折り畳み成分と元の成分の比はおよそ $e^{-q(q-2m)/(2K)}$ である。従って高調波ほど離散化の影響が残りやすい。

![高調波ごとの相関長](/figures/clock-r1/harmonic-memory-hierarchy.svg)

*有限状態数での高調波相関長とXY鎖の低温漸近則。*

## 外場応答

観測量を $\cos\theta_i$ とすると、$q>2$ の零外場では回転対称性から $\langle\cos\theta_i\cos\theta_j\rangle=C_1(|i-j|)/2$ である。$t=\Lambda_1/\Lambda_0$ と置けば、波数 $Q$ の感受率は

$$
\chi_{xx}(Q)=\frac{\beta}{2}
\frac{1-t^2}{1-2t\cos Q+t^2}.
$$

$q=2$ ではスピンの分散が1であるため係数 $\beta/2$ は $\beta$ になる。XY鎖も $q>2$ と同じ規格化である。強磁性の長相関長極限ではピーク幅が $\xi_1^{-1}$ に比例する。

奇数 $q$ では角度集合が $\pi$ 回転に対して不変ではないため、磁化の二次応答は一般には消えない。例えば $q=3$ の独立スピンでは、$x=\beta h$ とすると

$$
m(h)=\frac{e^x-e^{-x/2}}{e^x+2e^{-x/2}}
=\frac{x}{2}+\frac{x^2}{8}+O(x^3).
$$

線形感受率の形が共通していても、非線形応答は対称性の違いを反映する。

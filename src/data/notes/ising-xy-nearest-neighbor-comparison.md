---
title: "1次元一様最近接スピン系 — Z2・U(1)の空間記憶"
summary: "1次元最近接Ising鎖とXY鎖を、空間記憶の失われ方・transfer spectrum・空間変調外場への応答という共通軸で比較する。domain wallとphase diffusionの違いが、相関長とqξフィルタの温度発達の違いへどうつながるかを整理する。"
publishedAt: 2026-09-13T01:50:00+09:00
updatedAt: 2026-09-19
area: "Physics"
topics: ["statistical mechanics", "Ising model", "XY model", "correlation", "transfer matrix", "memory", "nearest-neighbor", "linear response"]
status: growing
---

1次元最近接Ising鎖とXY鎖は、どちらも有限温度では長距離秩序を持たない。ただし「向きを忘れる方法」はかなり違う。

$$
\beta\equiv\frac{1}{k_{\mathrm B}T},
\qquad
K\equiv\beta J=\frac{J}{k_{\mathrm B}T}
$$

とする。

比較の軸は、長距離秩序の有無ではなく

$$
\boxed{
\text{local memory-loss mechanism}
\longrightarrow
\xi(T)
\longrightarrow
\chi(q)}
$$

である。

## 1. Ising は稀なwall、XYは小回転の累積で向きを失う

Isingでは

$$
H_{\mathrm I}=-J\sum_i s_i s_{i+1},
\qquad s_i=\pm1
$$

に対して

$$
\tau_i=s_is_{i+1}
$$

を使うと、$\tau_i=-1$ がdomain wallになる。wall生成コストは $2J$ なので

$$
p_{\mathrm{dw}}\sim e^{-2K}.
$$

低温では記憶を反転させる欠陥が稀になる。

XYでは

$$
H_{\mathrm{XY}}
=-J\sum_i\cos(\theta_{i+1}-\theta_i)
$$

で、角度差

$$
\phi_i=\theta_{i+1}-\theta_i
$$

は連続変数である。低温でも

$$
\langle\phi_i^2\rangle
\simeq\frac1K
=\frac{k_{\mathrm B}T}{J}
$$

という小回転が至る所に残る。

$$
\theta_r-\theta_0
=\sum_{i=0}^{r-1}\phi_i
$$

なので、それらが空間方向へ累積する。

$$
\boxed{\text{Ising}:\ \text{rare localized walls}}
$$

$$
\boxed{\text{XY}:\ \text{distributed small rotations}}
$$

という対比になる。

## 2. multiplicative sign と additive phase は同じ1-step memoryへ還元される

Isingでは

$$
s_0s_r=\prod_{i=0}^{r-1}\tau_i
$$

なので、遠距離の符号はwall数の偶奇で決まる。これは multiplicative sign process である。

XYでは

$$
\theta_r-\theta_0
=\sum_{i=0}^{r-1}\phi_i
$$

なので、遠距離角度は局所増分の和でできる。こちらは additive phase process である。

零外場の開鎖では両者とも局所相対変数が独立なので

$$
\boxed{
C_{\mathrm I}(r)=[\tanh K]^r}
$$

$$
\boxed{
C_{\mathrm{XY}}(r)
=\left[\frac{I_1(K)}{I_0(K)}\right]^r}
$$

となる。

つまりどちらも

$$
\boxed{C(r)=\lambda^r}
$$

という1-step memoryの積に落ちる。

## 3. 同じ指数相関でも $\xi(T)$ の成長則は違う

$$
C(r)=e^{-r/\xi}
$$

なら

$$
\xi^{-1}=-\ln|\lambda|.
$$

Isingでは

$$
\xi_{\mathrm I}^{-1}
=-\ln(\tanh K)
$$

なので低温で

$$
\boxed{
\xi_{\mathrm I}
\simeq\frac12e^{2K}
=\frac12\exp\left(\frac{2J}{k_{\mathrm B}T}\right)}
$$

となる。

XYでは

$$
\xi_{\mathrm{XY}}^{-1}
=-\ln\left[\frac{I_1(K)}{I_0(K)}\right]
$$

かつ

$$
\frac{I_1(K)}{I_0(K)}
\simeq1-\frac{1}{2K}
$$

なので

$$
\boxed{
\xi_{\mathrm{XY}}
\simeq2K
=\frac{2J}{k_{\mathrm B}T}}
$$

となる。

$$
\boxed{
\text{Ising}:\ \text{activated growth}
\qquad
\text{XY}:\ \text{algebraic growth}}
$$

という差は、rare wall と phase diffusion の違いをそのまま反映している。

## 4. transfer spectrum は両模型の共通骨格になる

Isingでは $2\times2$ transfer matrix、XYでは積分作用素を使うが、長距離相関は同じ形で読める。

$$
\boxed{
C_a(r)
\sim\left(\frac{\lambda_a}{\lambda_0}\right)^r,
\qquad
\xi_a^{-1}
=-\ln\left|\frac{\lambda_a}{\lambda_0}\right|}
$$

である。

$$
\boxed{
\text{local transfer rule}
\longrightarrow
\text{spectral decay}
\longrightarrow
\text{spatial memory length}}
$$

という構造は共通している。

XYではさらに

$$
\lambda_m=2\pi I_m(K)
$$

という無限個のangular sectorがあり

$$
\xi_m\simeq\frac{2K}{m^2}
$$

となる。連続角度を持つXYでは、記憶長そのものにも角度分解能の階層がある。

## 5. 外場は相対方向だけで閉じる零外場の単純さを壊す

相互作用が見るのは相対方向、外場が見るのは絶対方向である。

$$
\boxed{
\text{interaction probes relative orientation}
\qquad
\text{field probes absolute orientation}}
$$

Isingでは

$$
s_i=s_0\prod_{j=0}^{i-1}\tau_j
$$

なので

$$
-\sum_i h_i s_i
=-s_0\sum_i h_i\prod_{j=0}^{i-1}\tau_j
$$

となり、wall表示が非局所化する。

XYでも

$$
\theta_i=\theta_0+\sum_{j=0}^{i-1}\phi_j
$$

なので

$$
-\sum_i h_i\cos\theta_i
=-\sum_i h_i
\cos\left(\theta_0+\sum_{j=0}^{i-1}\phi_j\right)
$$

となる。

さらにXYの零外場kernelでは独立だった $e^{im\theta}$ sectorが

$$
\cos\theta=\frac12(e^{i\theta}+e^{-i\theta})
$$

によって

$$
\boxed{m\leftrightarrow m\pm1}
$$

と混ざる。

## 6. 空間変調外場は零外場の記憶を Fourier 空間で読み出す

Isingでは

$$
\chi_{\mathrm I}(r)
=\beta[\tanh K]^{|r|}
$$

なので

$$
\boxed{
\chi_{\mathrm I}(q)
=\beta
\frac{1-\rho_{\mathrm I}^2}
{1-2\rho_{\mathrm I}\cos q+\rho_{\mathrm I}^2},
\qquad
\rho_{\mathrm I}=\tanh K}
$$

となる。

XYでは回転対称性から

$$
\chi_{\mathrm{XY}}^{xx}(r)
=\frac\beta2
\left[\frac{I_1(K)}{I_0(K)}\right]^{|r|}
$$

で

$$
\boxed{
\chi_{\mathrm{XY}}^{xx}(q)
=\frac\beta2
\frac{1-\rho_{\mathrm{XY}}^2}
{1-2\rho_{\mathrm{XY}}\cos q+\rho_{\mathrm{XY}}^2},
\qquad
\rho_{\mathrm{XY}}=\frac{I_1(K)}{I_0(K)}}
$$

となる。

長波長・長相関長極限では両方とも

$$
\chi(q)
\propto
\frac{\xi}{1+(q\xi)^2}.
$$

自然な変数は

$$
\boxed{q\xi}
$$

である。

$q\xi\ll1$ では相関領域内で外場はほぼ一様、$q\xi\gg1$ では同じ相関領域内で外場が何度も向きを変え、応答が相殺される。

この意味で

$$
\boxed{
\xi=\text{系が協調して追従できる空間スケール}}
$$

と読める。

## 7. 共通の $q\xi$ 則でも spatial filter の温度発達は違う

クロスオーバー波数を

$$
\boxed{q_\times(K)=\xi^{-1}(K)}
$$

とする。

Isingでは

$$
\boxed{
q_\times^{\mathrm I}(K)
=-\ln(\tanh K)
\simeq2e^{-2K}}
$$

である。

XYでは

$$
\boxed{
q_\times^{\mathrm{XY}}(K)
=-\ln\left[\frac{I_1(K)}{I_0(K)}\right]
\simeq\frac{1}{2K}}
$$

となる。

したがって低温化 $K\to\infty$ に対して

$$
\boxed{
\text{Ising}:\ q_\times\text{ は指数的に縮む}}
$$

のに対し

$$
\boxed{
\text{XY}:\ q_\times\text{ は代数的に縮む}}
$$

という違いが出る。

![IsingとXYの空間フィルタ幅](/figures/ising-xy-comparison/qxi-temperature-filter.svg)

*横軸は $K=\beta J$。Isingの空間フィルタは低温で指数的に狭まり、XYは $K^{-1}$ で緩やかに狭まる。*

固定波数 $q$ に対して $q\xi(K_\times)\sim1$ とすれば

$$
\boxed{
K_\times^{\mathrm I}
\sim\frac12\ln\left(\frac{2}{q}\right)}
$$

に対して

$$
\boxed{
K_\times^{\mathrm{XY}}
\sim\frac{1}{2q}}
$$

となる。

同じ外場波数でも、温度を下げたときに空間フィルタの外側へ押し出される仕方は両模型で異なる。

## 8. 共通性は「秩序しない」ではなく transfer → memory → response にある

Isingでは

$$
\text{rare walls}
\longrightarrow
\text{activated memory loss}
\longrightarrow
\xi\sim e^{2K}
$$

XYでは

$$
\text{phase diffusion}
\longrightarrow
\text{diffusive memory loss}
\longrightarrow
\xi\sim K
$$

である。

局所機構は異なるが

$$
\boxed{
\text{local transfer rule}
\longrightarrow
\text{spectral memory}
\longrightarrow
\xi
\longrightarrow
\chi(q)}
$$

という骨格は共通する。

この比較で見えるのは、「どちらも1次元だから秩序しない」という一文より、**記憶を失う局所機構の違いが $\xi(T)$ を通して空間応答の温度発達へまで伝わる**という構造である。

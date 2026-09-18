---
title: "1次元一様最近接 U(1) スピン系 — 位相拡散と角度記憶"
summary: "最近接古典XY鎖を、局所的には整列しているのに遠距離では向きを失う系として読む。独立な角度差、空間方向の位相拡散、修正Bessel関数が現れる理由、harmonicごとの記憶長、compactnessとwindingを通して、連続対称性を持つ1次元系の相関喪失機構を整理する。"
publishedAt: 2026-09-12T03:10:00+09:00
updatedAt: 2026-09-19
area: "Physics"
topics: ["statistical mechanics", "XY model", "phase diffusion", "transfer operator", "correlation", "Bessel function", "compact field"]
status: growing
---

隣り合うスピンがほとんど同じ向きなら、遠くまでその向きを覚えていそうに見える。1次元最近接XY鎖では、この直感が有限温度で外れる。

各サイトに

$$
\mathbf S_i=(\cos\theta_i,\sin\theta_i)
$$

を置き

$$
H=-J\sum_i\cos(\theta_{i+1}-\theta_i)
$$

とする。以下では

$$
\boxed{
\beta\equiv\frac{1}{k_{\mathrm B}T},
\qquad
K\equiv\beta J=\frac{J}{k_{\mathrm B}T}}
$$

と書く。

$J>0$ は隣接角度差を小さくするが、XYでは各bondが**少しずつ**ずれることを許す。この小さな誤差の累積が、局所整列と長距離秩序を分ける。

## 1. 自然な局所変数は角度差である

開鎖で

$$
\phi_i\equiv\theta_{i+1}-\theta_i
$$

と置けば

$$
H=-J\sum_i\cos\phi_i,
\qquad
\theta_n=\theta_1+\sum_{j=1}^{n-1}\phi_j.
$$

外場ゼロでは各 $\phi_i$ は独立で、1 bond の重みは

$$
e^{K\cos\phi}.
$$

規格化すると

$$
Z_1=\int_0^{2\pi}e^{K\cos\phi}\,d\phi,
\qquad
p(\phi)=\frac{e^{K\cos\phi}}{Z_1}.
$$

最近接XYの単純さは、スピン角では相互作用系に見えるものが、角度差では独立増分へ変わることにある。

## 2. 修正Bessel関数は円周上のBoltzmann重みの Fourier 係数である

$\phi$ は円周上の角度なので

$$
e^{K\cos\phi}
=\sum_{m=-\infty}^{\infty}a_m e^{im\phi}
$$

と展開するのが自然である。

係数は

$$
a_m
=\frac{1}{2\pi}
\int_0^{2\pi}
e^{K\cos\phi}e^{-im\phi}\,d\phi
$$

で、これは修正Bessel関数

$$
\boxed{
I_m(K)
=\frac{1}{2\pi}
\int_0^{2\pi}
e^{K\cos\phi}e^{-im\phi}\,d\phi}
$$

そのものである。

したがって

$$
\boxed{
e^{K\cos\phi}
=\sum_{m=-\infty}^{\infty}I_m(K)e^{im\phi}}
$$

かつ

$$
\boxed{
p(\phi)=\frac{e^{K\cos\phi}}{2\pi I_0(K)}}.
$$

修正Bessel関数は解法上の特殊関数というより、**円周上のBoltzmann重みを角度harmonicへ分解した係数**として現れている。

## 3. 低温では角度が空間方向にrandom walkする

$K\gg1$ では

$$
1-\cos\phi\simeq\frac{\phi^2}{2}
$$

なので

$$
e^{K\cos\phi}
\simeq e^K\exp\left(-\frac{K\phi^2}{2}\right).
$$

1 bond の揺らぎは

$$
\boxed{
\langle\phi^2\rangle
\simeq\frac1K
=\frac{k_{\mathrm B}T}{J}}
$$

である。

距離 $r$ では

$$
\theta_r-\theta_0
=\sum_{j=0}^{r-1}\phi_j
$$

なので

$$
\boxed{
\langle(\theta_r-\theta_0)^2\rangle
\simeq r\frac{k_{\mathrm B}T}{J}}
$$

と分散が距離に比例する。

各bondはよく整列しているのに、角度誤差は空間方向へ蓄積する。長距離物理は **phase diffusion in space** として読める。

## 4. 位相拡散は指数相関を作る

$$
C(r)
=\langle\mathbf S_0\cdot\mathbf S_r\rangle
=\langle\cos(\theta_r-\theta_0)\rangle
$$

とする。

低温Gaussian近似では

$$
\left\langle e^{i(\theta_r-\theta_0)}\right\rangle
=\exp\left[-\frac12
\langle(\theta_r-\theta_0)^2\rangle\right]
$$

なので

$$
C(r)
\simeq
\exp\left(-\frac{r k_{\mathrm B}T}{2J}\right).
$$

したがって

$$
\boxed{
\xi\simeq\frac{2J}{k_{\mathrm B}T}=2K}
$$

となる。

相関を壊すのは局所化した大欠陥ではなく、至る所にある小さな回転の累積である。

## 5. 厳密相関は角度増分の characteristic function になる

1 bond について

$$
\left\langle e^{im\phi}\right\rangle
=\frac{I_m(K)}{I_0(K)}.
$$

距離 $r$ の角度差は独立増分の和なので

$$
\boxed{
C_m(r)
\equiv
\left\langle e^{im(\theta_r-\theta_0)}\right\rangle
=\left[\frac{I_m(K)}{I_0(K)}\right]^r}
$$

となる。

通常のスピン相関は $m=1$ で

$$
\boxed{
C(r)=\left[\frac{I_1(K)}{I_0(K)}\right]^r,
\qquad
\xi_1^{-1}
=-\ln\left[\frac{I_1(K)}{I_0(K)}\right]}
$$

である。

$I_m/I_0$ は、1 bond進んだときに $m$ 次の角度情報がどれだけ残るかを表している。

## 6. 角度情報には harmonic ごとの記憶長がある

$$
\xi_m^{-1}
=-\ln\left|\frac{I_m(K)}{I_0(K)}\right|
$$

と定義できる。

低温では

$$
\frac{I_m(K)}{I_0(K)}
\simeq
\exp\left(-\frac{m^2}{2K}\right)
$$

なので

$$
\boxed{
\xi_m
\simeq\frac{2K}{m^2}
=\frac{2J}{m^2k_{\mathrm B}T}}
$$

となる。

$$
\boxed{\xi_m\propto m^{-2}}
$$

は、phase diffusionが細かい角度情報ほど早く消すことを表している。

## 7. transfer spectrum はこの記憶階層そのものである

transfer kernel

$$
T(\theta,\theta')
=e^{K\cos(\theta'-\theta)}
$$

は角度差だけに依存するので、Fourier mode

$$
\psi_m(\theta)=e^{im\theta}
$$

が固有関数になる。

$$
(T\psi_m)(\theta)
=2\pi I_m(K)\psi_m(\theta)
$$

より

$$
\boxed{\lambda_m=2\pi I_m(K)}.
$$

自由エネルギーは最大固有値

$$
\lambda_0=2\pi I_0(K)
$$

から

$$
f=-k_{\mathrm B}T\ln[2\pi I_0(K)]
$$

で決まり、一方 $m$ 次の空間記憶は

$$
C_m(r)=\left(\frac{\lambda_m}{\lambda_0}\right)^r
$$

で伝わる。

無限個の Fourier sector は、抽象的な固有mode列ではなく、**角度分解能ごとの記憶距離**として読める。

## 8. 外場は相対角だけで閉じる構造を壊す

$x$ 方向の外場を入れると

$$
H
=-J\sum_i\cos(\theta_{i+1}-\theta_i)
-\sum_i h_i\cos\theta_i.
$$

相互作用は相対角を、外場は絶対角を見る。

一様外場のkernelは

$$
T_h(\theta,\theta')
=\exp\left[
K\cos(\theta'-\theta)
+\frac{\beta h}{2}(\cos\theta+\cos\theta')
\right].
$$

$$
\cos\theta=\frac12(e^{i\theta}+e^{-i\theta})
$$

なので Fourier 空間では

$$
\boxed{m\leftrightarrow m\pm1}
$$

が結合する。零外場で独立だった harmonic sector を外場が混ぜる。

線形応答では

$$
\chi_x(r)
=\frac\beta2
\left[\frac{I_1(K)}{I_0(K)}\right]^{|r|}
$$

したがって

$$
\boxed{
\chi_x(q)
=\frac\beta2
\frac{1-\rho^2}{1-2\rho\cos q+\rho^2},
\qquad
\rho=\frac{I_1(K)}{I_0(K)}}
$$

となる。

外場は、phase diffusionによって作られた空間記憶を波数ごとにprobeしている。

## 9. compactness は局所拡散の上に winding sector を重ねる

Gaussian近似だけを見ると $\theta$ は実数場のように見えるが、XY角度は

$$
\boxed{\theta\equiv\theta+2\pi}
$$

である。

環では

$$
\theta_N=\theta_0+2\pi w,
\qquad
w\in\mathbb Z
$$

なので

$$
\boxed{
\sum_{i=0}^{N-1}\phi_i=2\pi w}
$$

というglobal constraintが入る。

開鎖で見えた局所phase diffusionに、周期境界ではwinding sectorが重なる。

## 10. この模型で残る像

最近接XY鎖では

$$
\boxed{
\text{independent phase increments}
\longrightarrow
\text{phase diffusion}
\longrightarrow
\text{harmonic-dependent memory lengths}}
$$

という一本の構造がある。

修正Bessel関数、transfer spectrum、指数相関は別々の話ではなく

$$
\boxed{
\text{phase diffusion}
\longleftrightarrow
\text{Fourier harmonic}
\longleftrightarrow
I_m(K)/I_0(K)
\longleftrightarrow
\xi_m}
$$

として同じ角度記憶の問題を異なる表現で見ている。

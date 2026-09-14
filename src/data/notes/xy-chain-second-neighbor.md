---
title: "1次元XY模型 — 第二近接相互作用と螺旋的な空間記憶"
summary: "最近接XY鎖に第二近接相互作用を加えると、独立だった角度差が相互作用し、競合相互作用から有限twist、chirality、有限波数応答が生まれる。基底状態、低温揺らぎ、transfer operator、空間変調外場への応答を通して、phase diffusionがcorrelated driftへ変わる過程を整理する。"
publishedAt: 2026-09-13T22:40:00+09:00
updatedAt: 2026-09-14
area: "Physics"
topics: ["statistical mechanics", "XY model", "second-neighbor interaction", "frustration", "helical order", "chirality", "correlation", "transfer operator", "linear response"]
status: growing
---

最近接XY鎖では

$$
\phi_i=\theta_{i+1}-\theta_i
$$

が独立で、遠距離の角度は独立な小回転の和としてphase diffusionした。

第二近接を加えると

$$
\boxed{
\text{independent phase increments}
\longrightarrow
\text{interacting phase increments}}
$$

となる。

変わるのは相関長だけではない。相互作用自身が有限の回転率を選び、相関と外場応答の中心波数を $q=0$ からfinite-$q$へ移す。

以下では

$$
\beta\equiv\frac{1}{k_{\mathrm B}T},
\qquad
K_1=\beta J_1,
\qquad
K_2=\beta J_2
$$

とする。

## 1. 第二近接は隣接する角度増分を直接結ぶ

$$
H
=-J_1\sum_i\cos(\theta_{i+1}-\theta_i)
-J_2\sum_i\cos(\theta_{i+2}-\theta_i)
$$

に対して

$$
\theta_{i+2}-\theta_i
=\phi_i+\phi_{i+1}
$$

なので

$$
\boxed{
H
=-J_1\sum_i\cos\phi_i
-J_2\sum_i\cos(\phi_i+\phi_{i+1})}
$$

となる。

最近接で独立だったphase incrementは、一段の空間記憶を持つ相関増分へ変わる。

## 2. 競合は有限twistを選ぶ

一様twist $\phi_i=q$ なら

$$
e(q)=-J_1\cos q-J_2\cos2q.
$$

極値条件は

$$
\sin q(J_1+4J_2\cos q)=0.
$$

したがって

$$
\boxed{
\cos q_\ast=-\frac{J_1}{4J_2}}
$$

というfinite-twist解が現れる。

$J_1>0$、$J_2<0$ として

$$
\kappa\equiv\frac{|J_2|}{J_1}
$$

とおけば、$\kappa>1/4$ で

$$
\boxed{
q_\ast=\arccos\left(\frac{1}{4\kappa}\right)}
$$

が選ばれる。

![第二近接XY鎖の選択twistと低温stiffness](/figures/xy-second-neighbor/preferred-twist-stiffness.svg)

*有限twistの立ち上がりと、同じ点でsoftになる一様twist stiffness。*

最近接XYの $q_\ast=0$ に対して、第二近接では相互作用自身が構造波数を選んでいる。

## 3. phase diffusion は drift + correlated diffusion へ変わる

一つのchirality sectorで

$$
\phi_i=q_\ast+\delta_i
$$

と書けば

$$
\theta_r-\theta_0
=q_\ast r+
\sum_{i=0}^{r-1}\delta_i.
$$

したがって

$$
\boxed{
\text{phase diffusion}
\longrightarrow
\text{drift}+\text{correlated diffusion}}
$$

となる。

平均角度は一定速度 $q_\ast$ で回転し、その上に相関した熱揺らぎが重なる。

## 4. 低温位相記憶は twist stiffness で決まる

$\phi_i=q_\ast+\delta_i$ として二次まで展開すると

$$
H_2
=\frac12\sum_i
\left[
J_1\cos q_\ast\,\delta_i^2
+J_2\cos2q_\ast(\delta_i+\delta_{i+1})^2
\right].
$$

Fourier空間では

$$
H_2=\frac12\sum_kA(k)|\delta_k|^2
$$

で

$$
\boxed{
A(k)=J_1\cos q_\ast
+2J_2\cos2q_\ast(1+\cos k)}
$$

となる。

長距離を支配する $k\to0$ stiffness は

$$
\boxed{
A_0
=J_1\cos q_\ast+4J_2\cos2q_\ast
=e''(q_\ast)}
$$

である。

単一chirality sectorでは

$$
\left\langle
(\theta_r-\theta_0-q_\ast r)^2
\right\rangle
\simeq r\frac{k_{\mathrm B}T}{A_0}
$$

より

$$
\boxed{
C(r)
\sim
\cos(q_\ast r)e^{-r/\xi_{\rm ph}},
\qquad
\xi_{\rm ph}\simeq\frac{2A_0}{k_{\mathrm B}T}=2\beta A_0}
$$

となる。

$\kappa=1/4$ では $A_0\to0$ なので、このGaussian近似自体がsoftになる。境界近傍では高次項が必要になる。

## 5. finite twist は離散chiralityを同時に生む

$e(q)=e(-q)$ なので

$$
\boxed{+q_\ast\quad\text{と}\quad-q_\ast}
$$

が縮退する。

局所chiralityは

$$
\kappa_i^{\rm ch}
\sim\sin(\theta_{i+1}-\theta_i)
=\sin\phi_i
$$

で見られる。

有限温度では $+q_\ast$ と $-q_\ast$ の領域の間にchirality wallが入りうるため、記憶喪失には

$$
\boxed{
\text{continuous phase fluctuation}
+\text{discrete chirality switching}}
$$

という二層がある。

## 6. $q_{\rm corr}$ と $\xi$ は別の記憶情報である

長距離相関を

$$
C(r)
\sim e^{-r/\xi}\cos(q_{\rm corr}r+\delta)
$$

と書けば

$$
\boxed{q_{\rm corr}:\ \text{どの回転率を覚えているか}}
$$

$$
\boxed{\xi:\ \text{その回転情報をどこまで覚えているか}}
$$

となる。

低温でchiralityが十分長く保たれるなら $q_{\rm corr}\simeq q_\ast$ である。ただし全系ではchirality correlation lengthも別に存在しうるため、単一の $\xi$ で全距離を閉じるとは限らない。

## 7. transfer operator は角度増分の Markov kernel になる

角度差表示では

$$
\boxed{
\mathcal T(\phi,\phi')
=\exp\left[
\frac{\beta J_1}{2}(\cos\phi+\cos\phi')
+\beta J_2\cos(\phi+\phi')
\right]}
$$

と取れる。

最近接では独立だった $\phi_i$ が、第二近接では

$$
P(\phi_{i+1}|\phi_i)
$$

というMarkov過程になる。

最近接での

$$
I_m(K_1)/I_0(K_1)
$$

という単純な1-step memoryは、一般のtransfer-operator spectrumへ置き換わる。

## 8. スピン相関は tilted spectrum の位相と絶対値を読む

$$
\left\langle e^{i(\theta_r-\theta_0)}\right\rangle
=
\left\langle\prod_{j=0}^{r-1}e^{i\phi_j}\right\rangle
$$

なので、平衡kernelだけでなく位相因子を組み込んだ tilted transfer operator が自然になる。

支配固有値を

$$
\Lambda_\ast=|\Lambda_\ast|e^{iq_{\rm corr}}
$$

と書けば

$$
C(r)
\sim
\left|\frac{\Lambda_\ast}{\Lambda_0}\right|^r
\cos(q_{\rm corr}r+\delta)
$$

であり

$$
\boxed{
\xi^{-1}
=-\ln\left|\frac{\Lambda_\ast}{\Lambda_0}\right|,
\qquad
q_{\rm corr}=\arg\Lambda_\ast}
$$

となる。

第二近接XYでは、長距離記憶が spectrum の**大きさと位相**の二つへ分かれている。

## 9. 外場応答の中心は $Q=0$ から $Q=\pm q_{\rm corr}$ へ移る

固定方向の空間変調外場

$$
H_h=-\sum_i h_i\cos\theta_i,
\qquad
h_i=h_Q\cos(Qi)
$$

に対して

$$
\delta m_x(Q)=\chi_{xx}(Q)h_Q.
$$

零外場では

$$
\chi_{xx}(r)
=\frac{\beta}{2}C(r).
$$

したがって

$$
C(r)\sim e^{-|r|/\xi}\cos(q_{\rm corr}r)
$$

なら概念的に

$$
\boxed{
\chi_{xx}(Q)
\propto
\frac{\xi}{1+\xi^2(Q-q_{\rm corr})^2}
+
\frac{\xi}{1+\xi^2(Q+q_{\rm corr})^2}}
$$

となる。

最近接強磁性XYでは $q_{\rm corr}=0$ だったが、螺旋領域では

$$
\boxed{Q\simeq\pm q_{\rm corr}}
$$

がresponse peakになる。

$$
\boxed{
\text{filter centered at }Q=0
\longrightarrow
\text{filter centered at }Q=\pm q_{\rm corr}}
$$

という質的変化である。

peak position は $q_{\rm corr}$、peak width はおおよそ $\xi^{-1}$ を測る。

## 10. rotating field は pitch と chirality の両方に phase-match する

XYでは外場自身を回転させ

$$
\mathbf h_i=h(\cos Qi,\sin Qi)
$$

とできる。

外場項は

$$
\boxed{
H_h^{\rm rot}
=-h\sum_i\cos(\theta_i-Qi)}
$$

となる。

スピンが

$$
\theta_i\simeq q_\ast i+\theta_0
$$

なら、$Q=q_\ast$ で外場とスピンの位相差は空間的にほぼ一定になる。

$$
\boxed{Q=q_\ast}
$$

は空間的なphase-matching条件である。

さらに $Q=+q_\ast$ と $Q=-q_\ast$ は回転方向が逆なので、rotating field は二つのchiralityを区別できる。

固定方向のcosine外場がpitchをprobeするのに対し、rotating fieldは**pitchとchiralityを同時にprobeできる**。

## 11. 第二近接XYで外場から読める三つの量

応答で分けて読みたいのは

$$
\boxed{q_{\rm corr},\qquad\xi,\qquad\text{chirality}}
$$

である。

- response peak position → 構造波数 $q_{\rm corr}$
- peak width → 記憶長 $\xi$
- rotating field の符号 → chirality

第二近接XYでは外場は絶対方向を揃えるだけでなく、**内部構造波数へ照準を合わせるprobe**になる。

## 12. 最近接から第二近接への変化

最近接では

$$
\boxed{
\text{independent increments}
\to
\text{phase diffusion}
\to
\chi(Q)\text{ centered at }0}
$$

だった。

第二近接では

$$
\boxed{
\text{interacting increments}
\to
\text{preferred twist}
+\text{correlated diffusion}
+\text{chirality}}
$$

となり

$$
\boxed{
\chi(Q)\text{ centered near }\pm q_{\rm corr}}
$$

へ変わる。

この模型で残る中心像は、**どの回転率を選ぶか、その回転情報をどこまで保つか、どの外場波数に最も応答するか**が同じtransfer spectrumからつながることである。

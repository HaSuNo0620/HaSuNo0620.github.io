---
title: "1次元XY模型 — 第二近接相互作用と螺旋的な空間記憶"
summary: "最近接XY鎖に第二近接相互作用を加えると、独立だった角度差が相互作用し、競合相互作用から有限twist、chirality、有限波数応答が生まれる。基底状態、低温揺らぎ、transfer operator、空間変調外場への応答を通して、phase diffusionがcorrelated driftへ変わる過程を整理する。"
publishedAt: 2026-09-13T22:40:00+09:00
updatedAt: 2026-09-13
area: "Physics"
topics: ["statistical mechanics", "XY model", "second-neighbor interaction", "frustration", "helical order", "chirality", "correlation", "transfer operator", "linear response"]
status: growing
---

最近接XY鎖では、角度差

$$
\phi_i=\theta_{i+1}-\theta_i
$$

が独立だった。そのため遠距離の角度は、独立な小さな回転を足し合わせる **phase diffusion** として理解できた。

第二近接相互作用を加えると、この単純さがちょうど壊れる。

$$
\boxed{
\text{independent phase increments}
\longrightarrow
\text{interacting phase increments}
}
$$

しかも変わるのは相関長だけではない。競合相互作用は有限の回転率を選び、相関関数のピークを $q=0$ から有限波数へ移し、外場に対する最も強い応答も有限波数へ移す。

以下では

$$
\beta\equiv\frac{1}{k_{\mathrm B}T},
\qquad
K_1\equiv\beta J_1,
\qquad
K_2\equiv\beta J_2
$$

とする。

## 1. 第二近接相互作用は隣り合う角度差どうしを結びつける

最近接と第二近接を持つ古典XY鎖を

$$
H
=-J_1\sum_i\cos(\theta_{i+1}-\theta_i)
-J_2\sum_i\cos(\theta_{i+2}-\theta_i)
$$

とする。

角度差 $\phi_i=\theta_{i+1}-\theta_i$ を使えば

$$
\theta_{i+2}-\theta_i
=\phi_i+\phi_{i+1}
$$

だから

$$
\boxed{
H
=-J_1\sum_i\cos\phi_i
-J_2\sum_i\cos(\phi_i+\phi_{i+1})
}
$$

となる。

最近接だけなら各 $\phi_i$ は独立だったが、第二近接項は $\phi_i$ と $\phi_{i+1}$ を直接結びつける。したがって空間方向のphase diffusionは、独立増分のrandom walkではなく、相関した増分を持つ過程になる。

## 2. 競合相互作用は有限のtwistを選ぶ

一様twist $\phi_i=q$ を仮定すると、1サイトあたりのエネルギーは

$$
e(q)=-J_1\cos q-J_2\cos2q.
$$

極値条件は

$$
\frac{de}{dq}
=\sin q\left(J_1+4J_2\cos q\right)=0.
$$

したがって $q=0,\pi$ のほかに

$$
\boxed{
\cos q_\ast=-\frac{J_1}{4J_2}
}
$$

という有限twist解が現れる。

特に $J_1>0$、$J_2<0$ として

$$
\kappa\equiv\frac{|J_2|}{J_1}
$$

とおくと、$\kappa>1/4$ で

$$
\boxed{
q_\ast
=\arccos\left(\frac{1}{4\kappa}\right)
}
$$

が選ばれる。

最近接XYでは自然な構造波数は $q_\ast=0$ だった。第二近接の競合は、相互作用自身によって有限の構造波数を選ぶ。

![第二近接XY鎖の選択twistと低温stiffness](/figures/xy-second-neighbor/preferred-twist-stiffness.svg)

*競合比 $\kappa=|J_2|/J_1$ に対する基底状態twist $q_\ast$ と、一様twistまわりの曲率 $A_0=e''(q_\ast)$。$\kappa=1/4$ で有限twistが立ち上がると同時に単純な調和stiffnessが消えるため、この近傍ではGaussian近似に注意が必要になる。*

## 3. 螺旋状態ではphase diffusionにdriftが加わる

一つのchiralityを選び

$$
\phi_i=q_\ast+\delta_i
$$

と書けば

$$
\theta_r-\theta_0
=q_\ast r+
\sum_{i=0}^{r-1}\delta_i.
$$

したがって最近接XYの

$$
\text{phase diffusion}
$$

は第二近接の螺旋領域で

$$
\boxed{
\text{drift}+\text{correlated diffusion}
}
$$

へ変わる。

平均的には一定速度 $q_\ast$ で角度が回転し、その上に熱揺らぎが重なる。

## 4. 低温調和近似ではtwist stiffnessが位相記憶を決める

$\phi_i=q_\ast+\delta_i$ として二次まで展開すると

$$
H_2
=\frac12\sum_i
\left[
J_1\cos q_\ast\,\delta_i^2
+J_2\cos2q_\ast\,(\delta_i+\delta_{i+1})^2
\right].
$$

Fourier空間では

$$
H_2=\frac12\sum_kA(k)|\delta_k|^2,
$$

$$
\boxed{
A(k)
=J_1\cos q_\ast
+2J_2\cos2q_\ast(1+\cos k)
}
$$

となる。

長距離の位相揺らぎを支配するのは

$$
\boxed{
A_0=A(0)
=J_1\cos q_\ast+4J_2\cos2q_\ast
=e''(q_\ast)
}
$$

である。

単一chirality sectorでの低温調和近似では

$$
\left\langle
(\theta_r-\theta_0-q_\ast r)^2
\right\rangle
\simeq
r\frac{k_{\mathrm B}T}{A_0},
$$

したがって

$$
\boxed{
C(r)
\sim
\cos(q_\ast r)
\exp\left(-\frac{r}{\xi_{\rm ph}}\right),
\qquad
\xi_{\rm ph}\simeq\frac{2A_0}{k_{\mathrm B}T}=2\beta A_0
}
$$

となる。

ただし $\kappa=1/4$ では $A_0\to0$ なので、このGaussian近似は使えない。ここでは高次勾配・非調和項を含めたsoft-mode問題になる。

## 5. 有限twistには左右二つのchiralityがある

$e(q)=e(-q)$ なので、螺旋領域では

$$
\boxed{+q_\ast\quad\text{と}\quad-q_\ast}
$$

が縮退する。

局所chiralityは例えば

$$
\kappa_i^{\rm ch}
\sim\sin(\theta_{i+1}-\theta_i)
=\sin\phi_i
$$

で測れる。低温では $\kappa_i^{\rm ch}\simeq\pm\sin q_\ast$ である。

有限温度の1次元系では、局所的に $+q_\ast$ を選んだ領域と $-q_\ast$ を選んだ領域の間にchirality wallが入りうる。したがって完全な記憶喪失には

$$
\boxed{
\text{continuous phase fluctuation}
+\text{discrete chirality switching}
}
$$

という二つの機構がある。

## 6. 相関関数では減衰長と構造波数を分けて読む

単一chirality sectorでは

$$
C(r)
\sim e^{-r/\xi}\cos(q_{\rm corr}r+\delta)
$$

という振動減衰相関が自然に現れる。低温でchiralityが長く保たれるなら $q_{\rm corr}\simeq q_\ast$ である。

ここで

$$
\boxed{q_{\rm corr}:\ \text{どの回転率を覚えているか}}
$$

と

$$
\boxed{\xi:\ \text{その回転情報をどこまで覚えているか}}
$$

は異なる情報である。

さらに全系ではchirality correlation lengthが別に現れる可能性があり、単一の $\xi$ だけで全距離を表せるとは限らない。

## 7. transfer operatorは角度差のMarkov過程になる

角度差表示ではHamiltonianが $\phi_i,\phi_{i+1}$ の最近接相互作用になるため、transfer kernelを

$$
\boxed{
\mathcal T(\phi,\phi')
=
\exp\left[
\frac{\beta J_1}{2}(\cos\phi+\cos\phi')
+\beta J_2\cos(\phi+\phi')
\right]
}
$$

と取れる。

最近接XYでは各 $\phi_i$ が独立だったのに対し、第二近接では

$$
P(\phi_{i+1}|\phi_i)
$$

という一段のMarkov過程として角度増分が伝わる。

したがって最近接での単純な

$$
I_m(K_1)/I_0(K_1)
$$

という1-step memoryは、一般のtransfer-operator固有値問題へ置き換わる。

## 8. スピン相関にはtilted transfer operatorが必要になる

元のスピン相関は

$$
\left\langle e^{i(\theta_r-\theta_0)}\right\rangle
=
\left\langle
\prod_{j=0}^{r-1}e^{i\phi_j}
\right\rangle.
$$

したがって平衡分布を作る $\mathcal T$ だけでなく、位相因子 $e^{i\phi}$ を組み込んだtilted transfer operatorを見る必要がある。

その支配固有値を

$$
\Lambda_\ast
=|\Lambda_\ast|e^{iq_{\rm corr}}
$$

と書けば、概念的には

$$
C(r)
\sim
\left|\frac{\Lambda_\ast}{\Lambda_0}\right|^r
\cos(q_{\rm corr}r+\delta).
$$

したがって

$$
\boxed{
\xi^{-1}
=-\ln\left|\frac{\Lambda_\ast}{\Lambda_0}\right|
}
$$

と

$$
\boxed{
q_{\rm corr}=\arg\Lambda_\ast
}
$$

という二つの量がスペクトルから読める。

## 9. 空間変調外場では応答ピークが有限波数へ移る

ここまでの相関構造は、微小外場への線形応答にそのまま現れる。

$x$方向の空間変調外場

$$
H_h=-\sum_i h_i\cos\theta_i,
\qquad
h_i=h_Q\cos(Qi)
$$

を考えると

$$
\delta m_x(Q)=\chi_{xx}(Q)h_Q.
$$

零外場では回転対称性から

$$
\chi_{xx}(r)
=\beta\langle\cos\theta_0\cos\theta_r\rangle
=\frac{\beta}{2}C(r).
$$

したがって

$$
C(r)\sim e^{-|r|/\xi}\cos(q_{\rm corr}r)
$$

なら、$\chi_{xx}(Q)$ は概念的に

$$
\boxed{
\chi_{xx}(Q)
\propto
\frac{\xi}{1+\xi^2(Q-q_{\rm corr})^2}
+
\frac{\xi}{1+\xi^2(Q+q_{\rm corr})^2}
}
$$

という二つのピークを持つ。

最近接強磁性XYでは $q_{\rm corr}=0$ なので応答最大は $Q=0$ だった。第二近接の螺旋領域では

$$
\boxed{
Q\simeq\pm q_{\rm corr}
}
$$

が最も強く応答する波数になる。

つまり第二近接は単に「短波長応答を弱める」のではない。

$$
\boxed{
\text{response filter centered at }Q=0
\longrightarrow
\text{response filter centered at }Q=\pm q_{\rm corr}
}
$$

という質的変化を起こす。

ピーク幅はおおよそ $\xi^{-1}$ なので、応答から

$$
\boxed{
\text{peak position}\to q_{\rm corr},
\qquad
\text{peak width}\to\xi^{-1}
}
$$

を同時に読み出せる。

## 10. XYでは回転外場が螺旋構造に直接phase-matchする

XYにはさらに自然なprobeがある。外場そのものを空間的に回転させ、

$$
\mathbf h_i
=h(\cos Qi,\sin Qi)
$$

とする。このとき外場項は

$$
\boxed{
H_h^{\rm rot}
=-h\sum_i\cos(\theta_i-Qi)
}
$$

となる。

もしスピンが

$$
\theta_i\simeq q_\ast i+\theta_0
$$

と回転しているなら、$Q=q_\ast$ の外場は各サイトでほぼ同じ位相差を保つ。逆に $Q$ が $q_\ast$ から外れると、スピンと外場の位相差が距離とともにずれていく。

したがって

$$
\boxed{
Q=q_\ast
}
$$

は空間的なresonance条件として読める。

さらに

$$
Q=+q_\ast
\quad\text{と}\quad
Q=-q_\ast
$$

は回転方向が逆なので、回転外場は二つのchiralityを区別できる。

$$
\boxed{
\text{rotating field probes not only pitch but also chirality}
}
$$

これは振幅だけを $\cos Qi$ で変調する固定方向外場にはない、XY特有の情報である。

## 11. 第二近接XYの外場応答で見るべき三つの量

第二近接XYでは、外場応答を単一の一様感受率だけで表すのは不十分になる。

見るべきなのは

$$
\boxed{
q_{\rm corr},\qquad \xi,\qquad \text{chirality}
}
$$

である。

- $\chi(Q)$ のピーク位置は、系が好む空間回転率 $q_{\rm corr}$ を測る。
- ピーク幅は、その回転情報が保たれる距離 $\xi$ を測る。
- $Q$ の符号を持つ回転外場は、$\pm q_\ast$ のchiralityを選別する。

したがって第二近接XYにおいて外場は

$$
\boxed{
\text{absolute directionを指定するだけでなく、
系の内部構造波数に照準を合わせるprobe}
}
$$

になる。

## 12. 最近接から第二近接へ何が変わったか

最近接XYでは

$$
\boxed{
\text{independent increments}
\longrightarrow
\text{phase diffusion}
\longrightarrow
\chi(Q)\text{ peaked at }Q=0
}
$$

だった。

第二近接では

$$
\boxed{
\text{interacting increments}
\longrightarrow
\text{preferred twist}+\text{correlated diffusion}+\text{chirality}
}
$$

となり、応答も

$$
\boxed{
\chi(Q)\text{ peaked near }Q=\pm q_{\rm corr}
}
$$

へ変わる。

最近接XYが「向きがどう拡散して忘れられるか」を見る模型なら、第二近接XYは

$$
\boxed{
\text{系がどの回転率を選び、その回転情報をどこまで保持し、どの外場波数に応答するか}
}
$$

を見る模型である。
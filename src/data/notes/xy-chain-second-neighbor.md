---
title: "1次元XY模型 — 第二近接相互作用と螺旋的な空間記憶"
summary: "最近接XY鎖に第二近接相互作用を加えると、独立だった角度差が相互作用し、競合相互作用から有限のtwist波数とchiralityが生まれる。基底状態、低温揺らぎ、振動相関、transfer operatorの変化を通して、phase diffusionがcorrelated driftへ変わる過程を整理する。"
publishedAt: 2026-09-13T22:40:00+09:00
updatedAt: 2026-09-13
area: "Physics"
topics: ["statistical mechanics", "XY model", "second-neighbor interaction", "frustration", "helical order", "chirality", "correlation", "transfer operator"]
status: growing
---

最近接XY鎖では、角度差

$$
\phi_i=\theta_{i+1}-\theta_i
$$

が独立だった。そのため遠距離の角度は、独立な小さな回転を足し合わせる **phase diffusion** として理解できた。

では第二近接相互作用を加えると何が変わるのか。

ここで見たいのは、単にHamiltonianの項が一つ増えることではない。

$$
\boxed{
\text{independent phase increments}
\longrightarrow
\text{interacting phase increments}
}
$$

という構造変化である。

以下では

$$
\beta\equiv\frac{1}{k_{\mathrm B}T}
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

角度差

$$
\phi_i=\theta_{i+1}-\theta_i
$$

を使えば

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

最近接だけなら各 $\phi_i$ は独立だったが、第二近接項は $\phi_i$ と $\phi_{i+1}$ を直接結びつける。

したがって第二近接XY鎖では

$$
\boxed{
\text{phase diffusion}
\text{ の増分そのものが相関する}
}
$$

ことになる。

## 2. 競合相互作用は有限のtwistを選ぶ

一様なtwist

$$
\phi_i=q
$$

を仮定すると、1サイトあたりのエネルギーは

$$
e(q)
=-J_1\cos q-J_2\cos2q
$$

である。

極値条件は

$$
\frac{de}{dq}
=J_1\sin q+2J_2\sin2q
$$

だから

$$
\boxed{
\sin q\left(J_1+4J_2\cos q\right)=0
}
$$

となる。

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

とおくと、

$$
\boxed{
\kappa>\frac14
}
$$

で

$$
\boxed{
q_\ast
=\arccos\left(\frac{1}{4\kappa}\right)
}
$$

が選ばれる。

つまり最近接XYでは $q_\ast=0$ だったのに対し、競合する第二近接相互作用を入れると、**相互作用自身が有限の構造波数を選ぶ**。

![第二近接XY鎖の選択twistと低温stiffness](/figures/xy-second-neighbor/preferred-twist-stiffness.svg)

*競合比 $\kappa=|J_2|/J_1$ に対する基底状態twist $q_\ast$ と、一様twistまわりの曲率 $A_0=e''(q_\ast)$。$\kappa=1/4$ で $q_\ast=0$ の状態から有限twistへ移り、同時に単純な調和stiffnessが消えるため、この近傍ではGaussian近似そのものに注意が必要になる。*

## 3. 螺旋状態ではphase diffusionにdriftが加わる

最近接XYでは低温で

$$
\langle\phi_i\rangle=0
$$

であり、

$$
\theta_r-\theta_0
=\sum_i\phi_i
$$

は平均driftを持たないrandom walkだった。

一方、有限twist状態では一つのchiralityを選べば

$$
\phi_i=q_\ast+\delta_i
$$

と書ける。したがって

$$
\theta_r-\theta_0
=q_\ast r+
\sum_{i=0}^{r-1}\delta_i.
$$

つまり

$$
\boxed{
\text{phase diffusion}
\longrightarrow
\text{drift + correlated diffusion}
}
$$

である。

平均的には一定の速度 $q_\ast$ で角度が回転し、その上に熱揺らぎが重なる。

## 4. 低温調和近似ではtwist stiffnessが相関長を決める

一つのchirality sectorの中で

$$
\phi_i=q_\ast+\delta_i
$$

とし、$\delta_i$ を小さいとして展開する。

二次まで残すと

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
H_2
=\frac12\sum_k A(k)|\delta_k|^2
$$

で

$$
\boxed{
A(k)
=J_1\cos q_\ast
+2J_2\cos2q_\ast(1+\cos k)
}
$$

となる。

長距離の位相拡散を支配するのは $k\to0$ のstiffness

$$
\boxed{
A_0
\equiv A(0)
=J_1\cos q_\ast+4J_2\cos2q_\ast
=e''(q_\ast)
}
$$

である。

この調和近似の範囲では

$$
\left\langle
(\theta_r-\theta_0-q_\ast r)^2
\right\rangle
\simeq
r\frac{k_{\mathrm B}T}{A_0}
$$

だから、単一chirality sector内では

$$
\boxed{
C(r)
\sim
\cos(q_\ast r)
\exp\left(-\frac{r k_{\mathrm B}T}{2A_0}\right)
}
$$

となり、

$$
\boxed{
\xi_{\rm harm}
\simeq
\frac{2A_0}{k_{\mathrm B}T}
=2\beta A_0
}
$$

を得る。

最近接XYの $A_0=J_1$ に対して、第二近接系では相互作用競合によって実効stiffnessそのものが変わる。

ただし $A_0\to0$ となる $\kappa=1/4$ 近傍では、このGaussian近似は成立しない。ここでは高次勾配や非調和項が重要になる。

## 5. 有限twistには左右二つのchiralityがある

エネルギー $e(q)$ は $q\to-q$ に対して不変なので、螺旋領域では

$$
\boxed{q_\ast\quad\text{と}\quad -q_\ast}
$$

が縮退する。

したがって局所chiralityを

$$
\kappa_i^{\rm ch}
\sim\sin(\theta_{i+1}-\theta_i)
=\sin\phi_i
$$

で見れば、低温では

$$
\kappa_i^{\rm ch}\simeq\pm\sin q_\ast
$$

という二つの向きが現れる。

ここで重要なのは、有限温度の1次元系では一つのchiralityが無限距離まで固定されるとは限らないことである。局所的には $+q_\ast$ で回転していても、途中で $-q_\ast$ の領域へ切り替わるchirality wallが入りうる。

したがって完全な有限温度相関には少なくとも

$$
\boxed{
\text{continuous phase fluctuation}
\quad+\quad
\text{discrete chirality switching}
}
$$

の二つの記憶喪失機構がある。

これは最近接XYにはなかった新しい階層である。

## 6. 振動相関には二つの意味を区別する必要がある

一つのchirality sectorだけを見れば

$$
C(r)
\sim
e^{-r/\xi}\cos(q_\ast r+\delta)
$$

という振動減衰相関が自然に現れる。

しかし全系では $\pm q_\ast$ のchirality switchingも起こるので、単一の $q_\ast$ と一つの $\xi$ だけで全距離を記述できるとは限らない。

したがって第二近接XYでは

$$
\boxed{
q_\ast:
\text{局所的に好まれる回転率}
}
$$

と

$$
\boxed{
\xi:\text{その回転情報が保たれる距離}
}
$$

を分けて考える必要がある。

さらにchirality correlation lengthが別に現れる可能性もある。

## 7. transfer operatorは角度差のMarkov過程になる

角度差表示ではHamiltonianが $\phi_i,\phi_{i+1}$ の最近接相互作用になったので、transfer kernelを

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

最近接XYでは各 $\phi_i$ が独立だったが、第二近接では

$$
\boxed{
P(\phi_{i+1}|\phi_i)
}
$$

という一段のMarkov過程として角度増分が伝わる。

したがって空間記憶は、単一bondのcharacteristic functionではなく、このtransfer operatorのスペクトルによって決まる。

最近接XYで成立した

$$
\frac{I_m(K)}{I_0(K)}
$$

という単純な1-step memoryは、第二近接では一般に行列・作用素の固有値問題へ置き換わる。

## 8. スピン相関には位相因子を組み込んだtransferが必要になる

元のスピン相関は

$$
\left\langle e^{i(\theta_r-\theta_0)}\right\rangle
=
\left\langle
\prod_{j=0}^{r-1}e^{i\phi_j}
\right\rangle
$$

である。

したがって角度差の平衡分布を与える $\mathcal T$ だけでなく、$e^{i\phi}$ を挿入したtilted transfer operatorを考えるのが自然である。

その支配固有値を

$$
\Lambda_\ast
=|\Lambda_\ast|e^{iq_{\rm corr}}
$$

と書けるなら、長距離相関は概念的に

$$
C(r)
\sim
\left|\frac{\Lambda_\ast}{\Lambda_0}\right|^r
\cos(q_{\rm corr}r+\delta)
$$

となる。

したがって

$$
\boxed{
-\ln\left|\frac{\Lambda_\ast}{\Lambda_0}\right|
\longrightarrow \xi^{-1}
}
$$

と

$$
\boxed{
\arg\Lambda_\ast
\longrightarrow q_{\rm corr}
}
$$

という、減衰長と振動波数の二つの情報がスペクトルから得られる。

## 9. 最近接から第二近接へ何が変わったか

最近接XYでは

$$
\boxed{
\text{independent increments}
\longrightarrow
\text{phase diffusion}
}
$$

だった。

第二近接では

$$
\boxed{
\text{interacting increments}
\longrightarrow
\text{preferred twist}
+\text{correlated diffusion}
+\text{chirality}
}
$$

となる。

つまり第二近接相互作用が生み出す本質は、単なる相関長の修正ではない。

- 角度増分が独立でなくなる。
- 相互作用が有限の構造波数 $q_\ast$ を選ぶ。
- 位相拡散にdriftが加わる。
- $\pm q_\ast$ のchirality自由度が生まれる。
- 減衰長と振動波数をtransfer spectrumから別々に読む必要が生じる。

最近接XYが「向きがどう拡散して忘れられるか」を見る模型なら、第二近接XYは

$$
\boxed{
\text{系がどの回転率を選び、その回転情報をどこまで保持するか}
}
$$

を見る模型である。

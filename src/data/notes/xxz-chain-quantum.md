---
title: "1次元XXZ模型 — 異方的交換相互作用と量子相関"
summary: "量子S=1/2 XXZ鎖を、Ising・XY・Heisenbergをつなぐ最近接量子スピン模型として整理する。Jordan–Wigner変換、自由フェルミオン極限、Bethe ansatz、Luttinger liquid、相関関数、磁場応答、ゼロ温度相図を通して異方性Δが何を変えるかを見る。"
publishedAt: 2026-09-12T03:15:00+09:00
updatedAt: 2026-09-14
area: "Physics"
topics: ["quantum magnetism", "XXZ model", "spin chain", "Jordan-Wigner", "Bethe ansatz", "Luttinger liquid"]
status: growing
---

古典 Ising・XY 鎖では、局所スピンそのものは古典変数だった。XXZ 鎖では各サイトに量子スピン $S=1/2$ を置き、

$$
\boxed{
H
=J\sum_i
\left(
S_i^xS_{i+1}^x
+S_i^yS_{i+1}^y
+\Delta S_i^zS_{i+1}^z
\right)
-h\sum_iS_i^z
}
$$

とする。以下では主に反強磁性的 $J>0$ を考える。

同じ最近接 Hamiltonian の中で

$$
\Delta=0:\ \text{XX},
\qquad
\Delta=1:\ \text{Heisenberg}
$$

がつながり、$|\Delta|\gg1$ では Ising-like になる。

XXZ は「相互作用距離を変えず、量子揺らぎと異方性だけを動かす」と何が変わるかを見る基準模型として使いやすい。

## 1. 非可換交換項が古典 Ising との境界を作る

$z$ 成分だけなら

$$
J\Delta\sum_iS_i^zS_{i+1}^z
$$

は対角的で、量子 Ising 的に見える。

しかし

$$
S_i^xS_{i+1}^x+S_i^yS_{i+1}^y
=\frac12
\left(
S_i^+S_{i+1}^-+S_i^-S_{i+1}^+
\right)
$$

は

$$
|\uparrow\downarrow\rangle
\leftrightarrow
|\downarrow\uparrow\rangle
$$

を量子的に混ぜる。

局所 $S_i^z$ 配置は保存されず、古典 Ising のように bond ごとの重みだけでは閉じない。一方で

$$
\boxed{S^z_{\rm tot}=\sum_iS_i^z}
$$

は保存され、$U(1)$ 回転対称性が残る。

## 2. Jordan–Wignerでは異方性がフェルミオン相互作用になる

1次元では

$$
S_i^z=n_i-\frac12,
$$

$$
S_i^+
=c_i^\dagger
\exp\left(i\pi\sum_{j<i}n_j\right)
$$

という Jordan–Wigner 変換を使える。

境界項を除けば

$$
\boxed{
H
=\frac{J}{2}\sum_i
\left(c_i^\dagger c_{i+1}+c_{i+1}^\dagger c_i\right)
+J\Delta\sum_i
\left(n_i-\frac12\right)
\left(n_{i+1}-\frac12\right)
-h\sum_i\left(n_i-\frac12\right)
}
$$

となる。

スピン言語では交換異方性だった $\Delta$ が、フェルミオン言語では**最近接密度相互作用**になる。

$$
\boxed{\Delta=0}
$$

では相互作用項が消え、XX 鎖は free spinless fermion になる。

## 3. XX 点は free-fermion 基準点になる

$\Delta=0$ で Fourier 変換

$$
c_j=\frac1{\sqrt N}\sum_ke^{ikj}c_k
$$

を行うと

$$
\boxed{
H=\sum_k(J\cos k-h)c_k^\dagger c_k+\text{const.}}
$$

となる。

1粒子分散は

$$
\boxed{\varepsilon(k)=J\cos k-h}
$$

で、$h=0$ では半充填、Fermi 点は

$$
k_F=\pm\frac\pi2
$$

にある。

低エネルギーで分散を線形化すると速度は

$$
\boxed{v=J}
$$

となる。

古典 Ising/XY の有限温度では有限相関長が中心だったが、零温度の XX 鎖では Fermi 点近傍の gapless 励起が残り、長距離相関は指数ではなくべきになる。

## 4. gapless 領域は Luttinger parameter で連続的につながる

XXZ 鎖は Bethe ansatz で可積分であり、

$$
-1<\Delta\le1
$$

では

$$
\Delta=\cos\gamma,
\qquad
0\le\gamma<\pi
$$

と置ける。

低エネルギーは Luttinger liquid で、

$$
\boxed{
K_L=\frac{\pi}{2(\pi-\gamma)}}
$$

$$
\boxed{
v=\frac{J\pi\sin\gamma}{2\gamma}}
$$

となる。

代表点は

$$
\Delta=0:\quad K_L=1,
$$

$$
\Delta=1:\quad K_L=\frac12.
$$

$\Delta$ は gapless 相の中で量子相関の指数を連続的に変えるパラメータとして働く。

## 5. 相関長の代わりに臨界指数が残る

零磁場・零温度の gapless 領域では

$$
\boxed{
\langle S_0^zS_r^z\rangle
\sim
-\frac{K_L}{2\pi^2r^2}
+A_z(-1)^rr^{-2K_L}}
$$

で、横相関は

$$
\boxed{
\langle S_0^+S_r^-\rangle
\sim
A_x(-1)^rr^{-1/(2K_L)}+\cdots}
$$

となる。

古典1次元 Ising/XY の有限温度相関

$$
C(r)\sim e^{-r/\xi}
$$

に対して、XXZ の gapless ground state では

$$
\boxed{C(r)\sim r^{-\eta}}
$$

となる。

相関長は無限大で、代わりに $K_L$ を通じた臨界指数が長距離物理を特徴づける。

## 6. $\Delta$ は gapped / gapless の零温度相図を横切る

反強磁性的 $J>0$、零磁場では

$$
\boxed{
\Delta<-1:\ \text{ferromagnetic gapped}}
$$

$$
\boxed{
-1<\Delta\le1:\ \text{gapless Luttinger liquid}}
$$

$$
\boxed{
\Delta>1:\ \text{antiferromagnetic gapped}}
$$

となる。

$\Delta<-1$ では easy-axis ferromagnet、$\Delta>1$ では Néel order が現れる。

$\Delta=1$ は gapless 相から Néel 相への BKT 型量子相転移点であり、厳密な相関には marginal logarithmic correction も重なる。ここでは主なべき指数だけを残している。

## 7. 磁場は fermion density と Fermi point を動かす

磁場項

$$
-h\sum_iS_i^z
$$

は Jordan–Wigner 表示では chemical potential になる。

磁化

$$
m=\langle S_i^z\rangle
$$

を変えることは fermion density を変えることに対応する。

Luttinger liquid では零温度一様感受率は

$$
\boxed{
\chi=\frac{K_L}{\pi v}}
$$

である。

XX 点では $K_L=1$、$v=J$ なので

$$
\boxed{\chi_{XX}=\frac{1}{\pi J}}
$$

となる。

十分強い磁場では完全偏極し、この規約では飽和磁場は

$$
\boxed{h_s=J(1+\Delta)}
$$

である。

磁場は gapless sea の充填率を連続的に動かし、そのまま空間構造波数も動かす。

## 8. 構造波数は filling と結びつく

Jordan–Wigner fermion の密度は

$$
n=m+\frac12
$$

なので

$$
k_F=\pi n
$$

である。

零磁化では $2k_F=\pi$ となり、staggered correlation に $(-1)^r$ が現れる。

磁化を変えると $k_F$ も動き、incommensurate wave number も連続的に変わる。

$$
\boxed{
\text{quantum filling}
\longleftrightarrow
k_F
\longleftrightarrow
\text{correlation wave number}}
$$

という対応になる。

周期的不均一 Ising のように外部単位胞が波数を imposed する場合とも、古典一様 Ising の $q=0,\pi$ だけの場合とも違う。

## 9. 古典 XY と量子 XXZ は自由度の作り方が違う

XXZ は $\Delta$ によって XX、Heisenberg、Ising-like 極限を一つの Hamiltonian でつなぐ。

| $\Delta$ | 物理的性質 | 低エネルギー像 |
| ---: | --- | --- |
| $0$ | XX / easy-plane | free fermion |
| $0<\Delta<1$ | easy-plane XXZ | interacting Luttinger liquid |
| $1$ | isotropic Heisenberg AF | SU(2) symmetric critical point |
| $>1$ | easy-axis AF | gapped Néel |
| $\ll-1$ | easy-axis ferro | gapped ferromagnet |

古典 XY では局所変数そのものが連続角度だった。

$$
\boxed{
\text{classical XY}:\ \text{continuous local variable}}
$$

それに対して XXZ は

$$
\boxed{
\text{quantum XXZ}:\ \text{two-state local Hilbert space + noncommuting exchange}}
$$

である。

見かけ上は「XY成分」を持っていても、連続古典角度と量子 $S=1/2$ は同じ自由度ではない。

## 10. 実在系では anisotropic chain の基準模型になる

準1次元磁性体では

$$
J_\perp(S_i^xS_{i+1}^x+S_i^yS_{i+1}^y)
+J_zS_i^zS_{i+1}^z
$$

という交換異方性が自然に現れ、

$$
\Delta=\frac{J_z}{J_\perp}
$$

で整理できる。

実在系では弱い鎖間結合、Dzyaloshinskii–Moriya相互作用、$g$ tensor異方性などが追加されうるが、XXZ鎖はそれらを載せる基準骨格として使われる。

## 11. 1次元でも quantum critical phase は有限幅に存在する

古典最近接 Ising/XY 鎖では、任意の有限温度で相関長は有限だった。

量子 XXZ では零温度という軸があり

$$
-1<\Delta\le1
$$

という有限幅の領域全体で

$$
\xi=\infty
$$

の量子臨界相が存在する。

$$
\boxed{
\text{thermal fluctuations in classical 1D}
\neq
\text{quantum fluctuations at }T=0}
$$

を分けないと、「1次元では長距離に何も残らない」という理解になってしまう。

## 12. この模型で残る像

XXZ の流れは

$$
\boxed{
\text{spin chain}
\xrightarrow{\rm Jordan\text{-}Wigner}
\text{interacting fermions}
\xrightarrow{\rm low\ energy}
\text{Luttinger liquid}}
$$

としてまとまる。

古典最近接鎖では一つの相関長が中心だったのに対し、gapless XXZ では $K_L$ と $v$ が長距離物理を支配する。

同じ「1次元最近接スピン模型」でも、量子化すると記憶の記述は有限相関長から臨界指数・Fermi wave number・collective modeへ置き換わる。

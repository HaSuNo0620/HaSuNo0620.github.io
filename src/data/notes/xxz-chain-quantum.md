---
title: "1次元XXZ模型 — 異方的交換相互作用と量子相関"
summary: "量子S=1/2 XXZ鎖を、Ising・XY・Heisenbergをつなぐ最近接量子スピン模型として整理する。Jordan–Wigner変換、自由フェルミオン極限、Bethe ansatz、Luttinger liquid、相関関数、磁場応答、ゼロ温度相図を通して異方性Δが何を変えるかを見る。"
publishedAt: 2026-09-12T03:15:00+09:00
updatedAt: 2026-09-12
area: "Physics"
topics: ["quantum magnetism", "XXZ model", "spin chain", "Jordan-Wigner", "Bethe ansatz", "Luttinger liquid"]
status: growing
---

古典 Ising・XY 模型では、サイトごとのスピン自由度を古典変数として扱った。XXZ 鎖では各サイトに量子スピン $S=1/2$ を置き、最近接交換相互作用を

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

$\Delta$ は交換異方性であり、同じ一つの模型の中に

$$
\Delta=0:\ \text{XX},
\qquad
\Delta=1:\ \text{Heisenberg},
$$

そして $|\Delta|\gg1$ の Ising-like 極限が含まれる。

したがって XXZ 模型は、「最近接相互作用」という空間構造を保ったまま、量子揺らぎと異方性を連続的に変える基準模型として読める。

## 1. Ising との違いは非可換な交換項にある

$z$ 成分だけなら

$$
J\Delta\sum_iS_i^zS_{i+1}^z
$$

は量子 Ising 的な対角相互作用である。しかし XXZ には

$$
S_i^xS_{i+1}^x+S_i^yS_{i+1}^y
=\frac12
\left(
S_i^+S_{i+1}^-+S_i^-S_{i+1}^+
\right)
$$

がある。

この項は隣接する

$$
|\uparrow\downarrow\rangle
\leftrightarrow
|\downarrow\uparrow\rangle
$$

を量子的に混ぜる。したがって局所 $S_i^z$ 配置は保存されず、古典 Ising のように bond ごとの Boltzmann 重みだけで問題を分離できない。

一方で全磁化

$$
\boxed{
S^z_{\rm tot}=\sum_iS_i^z
}
$$

は保存され、Hamiltonian は $U(1)$ 回転対称性を持つ。

## 2. Jordan–Wigner変換で1次元量子スピンをフェルミオンへ写せる

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

これにより XXZ 鎖は、境界項を除けば

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

へ写る。

したがって

$$
\boxed{
\Delta=0
}
$$

では相互作用項が消え、XX 鎖は自由 spinless fermion になる。

これは XXZ を理解するうえで重要な基準点である。$\Delta$ はスピン言語では交換異方性だが、Jordan–Wigner 後には **フェルミオン間最近接相互作用**として現れる。

## 3. XX点では完全に自由粒子として解ける

$\Delta=0$、周期境界の熱力学極限を考える。Fourier 変換

$$
c_j=\frac1{\sqrt N}\sum_k e^{ikj}c_k
$$

を行うと

$$
\boxed{
H
=\sum_k
\left(J\cos k-h\right)c_k^\dagger c_k
+\text{const.}
}
$$

となる。

したがって1粒子分散は

$$
\boxed{
\varepsilon(k)=J\cos k-h
}
$$

である。

$h=0$ では半充填となり、Fermi 点は $k_F=\pm\pi/2$ にある。低エネルギーでは Fermi 点近傍の分散が線形化され、速度は

$$
\boxed{
v=J
}
$$

となる。

古典 Ising/XY では熱揺らぎによる有限相関長を見ていたが、量子 XX 鎖のゼロ温度では Fermi 面に対応する gapless 励起が存在し、相関は指数ではなくべきで減衰する。

## 4. 一般の $\Delta$ でも Bethe ansatz で厳密可積分である

XXZ 鎖は最近接量子スピン模型でありながら Bethe ansatz で厳密可積分である。

特に

$$
-1<\Delta\le1
$$

では

$$
\Delta=\cos\gamma,
\qquad 0\le\gamma<\pi
$$

と置くと、低エネルギーは Luttinger liquid で記述できる。

Luttinger parameter は

$$
\boxed{
K_L
=\frac{\pi}{2(\pi-\gamma)}
}
$$

であり、励起速度は

$$
\boxed{
v
=\frac{J\pi\sin\gamma}{2\gamma}
}
$$

である。

代表点では

$$
\Delta=0:\quad K_L=1,
$$

$$
\Delta=1:\quad K_L=\frac12.
$$

したがって $\Delta$ を変えることは、gapless 相の中でも量子相関の指数を連続的に変えることに対応する。

## 5. gapless領域では相関は一つの相関長では記述できない

$-1<\Delta\le1$ の零磁場・零温度では、長距離相関は Luttinger liquid の形を取る。

縦相関は概略

$$
\boxed{
\langle S_0^zS_r^z\rangle
\sim
-\frac{K_L}{2\pi^2r^2}
+A_z(-1)^r r^{-2K_L}
}
$$

であり、横相関は

$$
\boxed{
\langle S_0^+S_r^-\rangle
\sim
A_x(-1)^r r^{-1/(2K_L)}
+\cdots
}
$$

となる。$A_x,A_z$ は非普遍的振幅である。

古典1次元 Ising/XY 鎖では有限温度相関が

$$
C(r)\sim e^{-r/\xi}
$$

という単一指数で整理できた。それに対して XXZ の gapless ground state では

$$
\boxed{
C(r)\sim r^{-\eta}
}
$$

となり、相関長は無限大で、代わりに **臨界指数**が物理を特徴づける。

## 6. 異方性 $\Delta$ がゼロ温度相図を作る

零磁場、反強磁性的 $J>0$ の XXZ 鎖では、$\Delta$ によって基底状態の性質が変わる。

### $\Delta<-1$：強磁性相

$z$ 方向に強い easy-axis ferromagnetic anisotropy が支配し、全スピンが同方向を向く強磁性基底状態を持つ。励起は gapped である。

### $-1<\Delta\le1$：gapless Luttinger liquid

この領域では長距離秩序はないが、べき相関が存在する。$\Delta=0$ は自由フェルミオン点、$\Delta=1$ は等方 Heisenberg 反強磁性点である。

### $\Delta>1$：反強磁性 Néel 相

$z$ 方向 easy-axis anisotropy が強くなり、基底状態は Néel 的となる。励起には gap が開き、長距離では staggered $S^z$ 秩序が現れる。

したがって

$$
\boxed{
\Delta<-1:
\text{ferromagnetic gapped}
}
$$

$$
\boxed{
-1<\Delta\le1:
\text{gapless Luttinger liquid}
}
$$

$$
\boxed{
\Delta>1:
\text{antiferromagnetic gapped}
}
$$

と整理できる。

$\Delta=-1$ では強磁性相との境界、$\Delta=1$ では gapless 相から Néel 相への BKT 型量子相転移が起こる。

## 7. 磁場は粒子密度、すなわちFermi点を動かす

磁場項

$$
-h\sum_iS_i^z
$$

は Jordan–Wigner 表示では chemical potential に対応する。

したがって磁化

$$
m=\langle S_i^z\rangle
$$

を変えることは、フェルミオン密度を変えることに等しい。

Luttinger liquid 領域では小さな磁場に対する零温度一様感受率は

$$
\boxed{
\chi
=\frac{K_L}{\pi v}
}
$$

となる。

たとえば XX 点 $\Delta=0$ では $K_L=1$、$v=J$ なので

$$
\boxed{
\chi_{XX}=\frac{1}{\pi J}
}
$$

を得る。

磁場を十分強くすると全スピンが偏極し、反強磁性的 $J>0$ では飽和磁場は

$$
\boxed{
h_s=J(1+\Delta)
}
$$

となる。したがって磁場は、gapless sea の充填率を連続的に変え、最後には完全偏極相へ到達させる。

## 8. XXZでは「波数」がFermi運動量と結びつく

零磁化では $2k_F=\pi$ なので staggered 相関は $(-1)^r$ を持つ。

磁場で磁化 $m$ を変えると Fermi 運動量も変化し、Jordan–Wigner fermion の密度

$$
n=m+\frac12
$$

に応じて

$$
k_F=\pi n
$$

となる。したがって相関中の incommensurate wave number も磁化とともに移動する。

これは周期的不均一 Ising 鎖のように外部単位胞が波数を imposed する場合とも、古典一様 Ising のように $q=0,\pi$ だけが自然に現れる場合とも違う。

XXZ では

$$
\boxed{
\text{quantum filling}
\longleftrightarrow
k_F
\longleftrightarrow
\text{correlation wave number}
}
$$

という関係が現れる。

## 9. Ising・XY・Heisenbergを一つの異方性軸で見る

XXZ の利点は、いくつかの代表模型を一つの Hamiltonian でつなげられることにある。

| $\Delta$ | 物理的性質 | 低エネルギー像 |
| ---: | --- | --- |
| $0$ | XX / easy-plane | free fermion |
| $0<\Delta<1$ | easy-plane XXZ | interacting Luttinger liquid |
| $1$ | isotropic Heisenberg AF | SU(2) symmetric critical point |
| $>1$ | easy-axis AF | gapped Néel |
| $\ll-1$ | easy-axis ferro | gapped ferromagnet |

古典 XY ノートでは $U(1)$ の連続角度自由度そのものを扱った。量子 XXZ では局所 Hilbert 空間は二次元のままだが、非可換交換相互作用によって量子揺らぎが生じる。

したがって

$$
\boxed{
\text{classical XY}:
\text{continuous local variable}
}
$$

に対し

$$
\boxed{
\text{quantum XXZ}:
\text{two-state local Hilbert space + noncommuting dynamics}
}
$$

という違いがある。

## 10. 実在系では準1次元量子磁性体の標準模型になる

XXZ 鎖は単なるトイモデルではなく、鎖方向の交換相互作用が支配的な準1次元磁性体の低エネルギー模型として広く現れる。

結晶場や spin–orbit coupling により交換相互作用が異方的になると、等方 Heisenberg ではなく XXZ 型の

$$
J_\perp(S_i^xS_{i+1}^x+S_i^yS_{i+1}^y)
+J_zS_i^zS_{i+1}^z
$$

が自然に生じ、

$$
\Delta=\frac{J_z}{J_\perp}
$$

として記述できる。

実在系では弱い鎖間結合、Dzyaloshinskii–Moriya 相互作用、g tensor 異方性などが追加されうるが、まず XXZ 鎖を基準模型にして、その上に小さな補正を加えるのが自然である。

## 11. 古典1次元模型との最も大きな違い

古典最近接 Ising/XY 鎖では、有限温度で相関長は有限であり、長距離相関は指数減衰した。

量子 XXZ 鎖では零温度という追加の軸があり、$-1<\Delta\le1$ で

$$
\xi=\infty
$$

の量子臨界相そのものが有限幅のパラメータ領域として存在する。

したがって「1次元だから長距離に何も残らない」という理解では不十分であり、

$$
\boxed{
\text{thermal fluctuations in classical 1D}
\neq
\text{quantum fluctuations at }T=0
}
$$

を区別する必要がある。

## まとめ

量子 $S=1/2$ XXZ 鎖は

$$
H
=J\sum_i
\left(
S_i^xS_{i+1}^x
+S_i^yS_{i+1}^y
+\Delta S_i^zS_{i+1}^z
\right)
-h\sum_iS_i^z
$$

という最近接模型でありながら、$\Delta$ 一つで free fermion、Luttinger liquid、Heisenberg criticality、Néel gap、ferromagnetic gap をつなぐ。

中心となる見方は

$$
\boxed{
\text{spin chain}
\xrightarrow{\rm Jordan\text{-}Wigner}
\text{interacting fermions}
\xrightarrow{\rm low\ energy}
\text{Luttinger liquid}
}
$$

である。

古典 Ising/XY の最近接鎖では「一つの相関長」が中心だったのに対し、XXZ の gapless 領域では相関長の代わりに $K_L$ と $v$ が長距離物理を支配する。

この意味で XXZ は、1次元スピン模型を **古典統計力学から量子多体系へ拡張する最も自然な次の基準点**である。
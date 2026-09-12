---
title: "準結晶の回折と Fourier module — 実空間は非周期なのに、なぜ Bragg peak は鋭いのか"
summary: "周期格子と準結晶の回折を比較し、鋭いBragg peakが周期性そのものではなく長距離の位相コヒーレンスを表すことを確認する。reciprocal latticeから高rank Fourier moduleへの拡張を理解する。"
publishedAt: 2026-09-12T02:48:00+09:00
updatedAt: 2026-09-13
area: "Physics"
topics: ["quasicrystals", "diffraction", "Fourier module", "reciprocal space", "cut and project"]
status: growing
---

[前のノート](/notes/fibonacci-cut-and-project/)では、高次元の周期格子から1次元の非周期点列を作った。

すると次の疑問が出る。

**実空間に周期格子がないのに、なぜ準結晶は鋭い Bragg peak を持てるのか。**

周期結晶では Bragg peak と reciprocal lattice がほとんど同じ話に見えるので、ここが準結晶を理解するときの大きな引っかかりになる。

まず周期結晶と準周期構造の Fourier peak を並べて見る。

![周期格子と高rank Fourier moduleのBragg peak](/figures/quasicrystals/diffraction-fourier-module.svg)

*周期格子では1個の基本波数から等間隔の peak が生成される。準周期構造では複数の独立基本波数から peak が生成されるため位置集合は複雑になるが、各 peak 自体は鋭い。弱い peak まで含めると位置集合は高密度になりうる。*

## 1. Bragg peak は何を意味しているのか

原子位置を $x_j$ とし、密度を

$$
\rho(x)=\sum_j\delta(x-x_j)
$$

と書く。

Fourier 振幅は

$$
\widetilde\rho(k)=\sum_j e^{-ikx_j}
$$

である。

ここでは各原子からの寄与が位相 $kx_j$ を持って足し合わされる。

もしある $k$ で遠く離れた原子からの位相まで整合すれば、和は打ち消し合わず大きくなる。理想的な無限系では、それが鋭い Bragg peak になる。

したがって Bragg peak が示しているのは

$$
\boxed{
\text{long-range phase coherence}
}
$$

であって、「有限単位胞があること」そのものではない。

ここが最初の答えである。

## 2. 周期結晶では位相整合が1個の基本波数で表せる

周期 $a$ の1次元格子なら

$$
x_j=ja
$$

なので

$$
\widetilde\rho(k)=\sum_j e^{-ikja}
$$

となる。

全ての項が同位相になる条件は

$$
ka=2\pi m,
\qquad m\in\mathbb Z
$$

であり、

$$
k_m=m\frac{2\pi}{a}
$$

に peak が並ぶ。

1個の基本波数

$$
k_0=\frac{2\pi}{a}
$$

の整数倍だけで全ての peak を index できる。

$d$ 次元周期結晶なら

$$
\mathbf G=\sum_{i=1}^{d}m_i\mathbf b_i
$$

となり、$d$ 個の reciprocal basis vector があれば十分である。

## 3. 準周期構造では基本波数が空間次元より多い

[準周期関数のノート](/notes/quasiperiodic-functions-torus/)で見たように、1次元でも独立な周波数を二つ持てる。

例えば

$$
k_{mn}=mb_1+nb_2,
\qquad m,n\in\mathbb Z
$$

で $b_1/b_2$ が無理数なら、1個の基本波数の整数倍には還元できない。

それでも各 peak の位置は任意ではない。二つの整数 $(m,n)$ で完全に index されている。

一般に $d$ 次元の準結晶では

$$
\boxed{
\mathbf k=\sum_{j=1}^{D}n_j\mathbf b_j,
\qquad
n_j\in\mathbb Z,
\qquad
D>d
}
$$

のような整数線形結合が現れる。

この集合が Fourier module である。

周期結晶との違いは「逆空間に規則がない」ことではない。むしろ逆で、**規則はあるが、その rank が物理空間の次元より高い**。

## 4. なぜ高次元格子から Fourier module が出るのか

cut-and-project では、$D$ 次元の整数格子から $d$ 次元の physical space へ点を射影した。

reciprocal space でも同じことをする。

高次元 reciprocal lattice のベクトルを $\mathbf K$ とし、physical space 成分と internal space 成分へ

$$
K_{\parallel}=P_{\parallel}\mathbf K,
\qquad
K_{\perp}=P_{\perp}\mathbf K
$$

と分解する。

すると Bragg peak の位置は physical-space projection

$$
\boxed{k=K_{\parallel}}
$$

として現れる。

つまり Fourier module は、低次元で突然生えた奇妙な規則ではない。

**高次元では普通の reciprocal lattice だったものを、低次元へ射影した結果**である。

ここで、実空間の cut-and-project と逆空間の Fourier module が一つにつながる。

## 5. peak の位置が稠密でも、なぜ回折像はぐちゃぐちゃにならないのか

1次元で $b_1/b_2$ が無理数なら

$$
\{mb_1+nb_2\mid m,n\in\mathbb Z\}
$$

は実軸上で稠密になりうる。

すると「鋭く分離した Bragg peak」という像と矛盾するように見える。

しかし、**位置が存在することと、強度が大きいことは別である。**

cut-and-project では、実空間で使った acceptance window $W$ の Fourier 変換が peak 強度へ入る。概念的には

$$
A(\mathbf K)\propto \widehat{1_W}(K_{\perp})
$$

となる。

したがって高次元 reciprocal lattice 点の多くは、physical space へ peak の位置を与えても非常に弱い。

$$
\boxed{
\text{dense allowed positions}
\neq
\text{uniformly strong scattering}
}
$$

である。

実験では強い peak が目立つため、「鋭い spots が並ぶ」回折像として見える。

## 6. ここまでで何が分かったか

最初の疑問は

> 周期格子がないのに、なぜ Bragg peak があるのか

だった。

答えは、Bragg peak の条件を周期性と同一視していたところにある。

周期結晶では

$$
\text{periodic lattice}
\Rightarrow
\text{phase coherence}
\Rightarrow
\text{Bragg peaks}
$$

なので区別する必要がない。

準結晶では

$$
\text{no periodic lattice}
\quad\text{but}\quad
\text{phase coherence}
\Rightarrow
\text{Bragg peaks}
$$

が起こる。

そしてその秩序は、通常の reciprocal lattice の代わりに

$$
\boxed{
\text{finite-rank Fourier module with }D>d
}
$$

として表現される。

4本を通して見ると、準結晶の見方は次の一本にまとまる。

$$
\boxed{
\text{非周期秩序}
\longrightarrow
\text{準周期関数}
\longrightarrow
\text{高次元格子からの射影}
\longrightarrow
\text{高rank Fourier module}
}
$$

実空間では周期を失っているが、構造を生成する整数的な秩序そのものが失われたわけではない。

ここから先は「準結晶とは何か」という構造論から、**準周期秩序の上に相互作用を載せたら物理がどう変わるか**へ進める。Fibonacci Ising model や quasiperiodic coupling はその自然な次の問題になる。

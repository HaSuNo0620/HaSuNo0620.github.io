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

ここではまず、周期結晶の回折で何が起きているかを確認する。そのあとで、準結晶では何を一般化すればよいのかを見る。

![周期格子と準周期構造のBragg peak](/figures/quasicrystals/diffraction-fourier-module.svg)

*左では一つの基本間隔を持つ周期格子から、等間隔の Bragg peak が生じる。右では複数の独立な波数から peak が生成されるため、位置の並び方は複雑になる。それでも各 peak 自体は鋭い。*

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

各原子からの寄与は位相 $kx_j$ を持つ。

もしある $k$ で遠く離れた原子からの寄与まで同位相で足し合わされれば、打ち消し合わず大きな強度になる。理想的な無限系では、それが鋭い Bragg peak になる。

したがって Bragg peak が示しているのは

$$
\boxed{
\text{long-range phase coherence}
}
$$

であって、「有限単位胞があること」そのものではない。

これが、準結晶でも Bragg peak が存在できる理由の出発点である。

## 2. 周期結晶では peak の位置が等間隔に並ぶ

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

つまり実空間の周期 $a$ に対して、波数空間には基本間隔 $2\pi/a$ の格子ができる。

この**波数空間側の周期格子**を reciprocal lattice、逆格子と呼ぶ。

1次元なら

$$
k_m=mk_0,
\qquad
k_0=\frac{2\pi}{a}
$$

で十分である。

$d$ 次元周期結晶では

$$
\mathbf G=\sum_{i=1}^{d}m_i\mathbf b_i,
\qquad m_i\in\mathbb Z
$$

と書ける。$\mathbf b_i$ は reciprocal lattice を作る基底ベクトルである。

ここで必要な独立基底の個数は空間次元 $d$ と同じである。

## 3. 準周期構造では一つの基本波数では足りない

[準周期関数のノート](/notes/quasiperiodic-functions-torus/)では、1次元でも二つの独立な基本周波数を持てることを見た。

例えば

$$
k_{mn}=mb_1+nb_2,
\qquad m,n\in\mathbb Z
$$

で $b_1/b_2$ が無理数なら、全ての peak を一つの基本波数の整数倍へまとめることはできない。

それでも peak の位置は任意ではない。二つの整数 $(m,n)$ で全て index できる。

ここで、「この peak 集合を生成するために、独立な基本波数が何個必要か」を **rank** と呼ぶ。

1次元周期格子なら rank は1である。一方、1次元 Fibonacci 型の準周期構造では rank 2 の波数集合が現れる。

このように、有限個の基本波数を整数係数で組み合わせて得られる集合を **Fourier module** と呼ぶ。

一般には

$$
\boxed{
\mathbf k=\sum_{j=1}^{D}n_j\mathbf b_j,
\qquad
n_j\in\mathbb Z
}
$$

で表され、$D$ がその rank である。

周期結晶なら通常 $D=d$ だが、準結晶では

$$
D>d
$$

となりうる。

つまり準結晶は「逆空間に規則がない」のではない。**規則はあるが、その整数構造が物理空間の次元より高い**。

## 4. なぜ高次元格子から Fourier module が出るのか

前の cut-and-project では、高次元格子点を physical space と internal space の二方向へ分解した。

波数空間でも同じ発想を使える。

高次元側の reciprocal lattice にある一つの波数ベクトルを $\mathbf K$ とする。それを physical space 方向と internal space 方向へ

$$
K_{\parallel}=P_{\parallel}\mathbf K,
\qquad
K_{\perp}=P_{\perp}\mathbf K
$$

と分解する。

すると低次元で観測される Bragg peak の位置は、physical-space 成分

$$
\boxed{k=K_{\parallel}}
$$

として現れる。

高次元では普通の reciprocal lattice だったものが、低次元へ射影されると rank の高い Fourier module になる。

ここで、実空間の cut-and-project と逆空間の Fourier module が一つにつながる。

## 5. peak の位置が密でも、回折像はなぜ連続にならないのか

1次元で $b_1/b_2$ が無理数なら

$$
\{mb_1+nb_2\mid m,n\in\mathbb Z\}
$$

という peak 候補の位置は実軸上で稠密になりうる。つまり、どんな小さな波数区間にも候補位置が存在しうる。

すると「鋭く分離した Bragg peak」という像と矛盾するように見える。

しかし、**peak の位置が許されることと、その peak が強いことは別である。**

cut-and-project では、どの格子点を採用するかを acceptance window $W$ で決めた。波数空間では、その window の Fourier 変換が各 peak の振幅を重み付けする。

概念的には

$$
A(\mathbf K)\propto \widehat{1_W}(K_{\perp})
$$

となる。

そのため、候補位置が多数あっても、その多くは非常に弱い。

$$
\boxed{
\text{dense allowed positions}
\neq
\text{uniformly strong scattering}
}
$$

である。

だから理想準結晶の回折は、連続的な背景に溶けるのではなく、鋭い peak の集合として現れる。

## 6. 最初の疑問へ戻る

最初の疑問は

> 周期格子がないのに、なぜ Bragg peak があるのか

だった。

周期結晶では

$$
\text{periodic lattice}
\Rightarrow
\text{phase coherence}
\Rightarrow
\text{Bragg peaks}
$$

なので、「Bragg peak があるなら周期格子がある」と思いやすい。

準結晶では

$$
\text{no periodic lattice}
\quad\text{but}\quad
\text{phase coherence}
\Rightarrow
\text{Bragg peaks}
$$

が起こる。

そして peak の位置は、普通の reciprocal lattice ではなく

$$
\boxed{
\text{finite-rank Fourier module with }D>d
}
$$

として整理される。

4本を通して見ると、準結晶の見方は

$$
\boxed{
\text{非周期秩序}
\longrightarrow
\text{準周期関数}
\longrightarrow
\text{高次元格子からの射影}
\longrightarrow
\text{Fourier module}
}
$$

という流れにまとまる。

実空間では周期を失っている。しかし、構造を生成する整数的な秩序そのものが失われたわけではない。

ここから先は「準結晶とは何か」という構造論から、**準周期秩序の上に相互作用を載せたら物理がどう変わるか**へ進める。Fibonacci Ising model や quasiperiodic coupling はその自然な次の問題になる。

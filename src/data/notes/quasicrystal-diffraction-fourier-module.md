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

ここまで来ると、最初から気になっていた疑問に戻れる。

**実空間に周期格子がないのに、なぜ準結晶は鋭い Bragg peak を持てるのか。**

周期結晶では Bragg peak と reciprocal lattice がほとんどセットで出てくるので、つい「Bragg peak があるなら周期格子もある」と思ってしまう。

まず周期結晶側で何が起きているかを整理してから、準結晶で何が変わるかを見る。

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

各原子からの寄与は位相 $kx_j$ を持つ。ある $k$ で遠く離れた原子からの寄与まで同位相で足し合わされれば、打ち消し合わず大きな強度になる。理想的な無限系では、それが鋭い Bragg peak になる。

つまり Bragg peak が直接見ているのは

$$
\boxed{
\text{long-range phase coherence}
}
$$

であって、「有限単位胞があること」そのものではない。

この区別が、準結晶でも Bragg peak が存在できる理由の出発点になる。

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

だから

$$
k_m=m\frac{2\pi}{a}
$$

に peak が並ぶ。

実空間の周期 $a$ に対して、波数空間には基本間隔 $2\pi/a$ の格子ができる。この波数空間側の周期格子が reciprocal lattice、逆格子である。

1次元なら

$$
k_m=mk_0,
\qquad
k_0=\frac{2\pi}{a}
$$

で全てを表せる。

$d$ 次元周期結晶では

$$
\mathbf G=\sum_{i=1}^{d}m_i\mathbf b_i,
\qquad m_i\in\mathbb Z
$$

となり、必要な独立基底の個数は空間次元 $d$ と同じになる。

## 3. 準周期構造では一つの基本波数では足りない

[準周期関数のノート](/notes/quasiperiodic-functions-torus/)では、1次元でも複数の独立な基本周波数を持てることを見た。

例えば

$$
k_{mn}=mb_1+nb_2,
\qquad m,n\in\mathbb Z
$$

で $b_1/b_2$ が無理数なら、全ての peak を一つの基本波数の整数倍へまとめることはできない。

ただし、peak の位置がバラバラというわけでもない。二つの整数 $(m,n)$ で全て index できる。

このとき、「peak 集合を生成するために独立な基本波数が何個必要か」を rank と呼ぶ。

1次元周期格子なら rank 1。1次元 Fibonacci 型の準周期構造では rank 2 になる。

有限個の基本波数を整数係数で組み合わせて得られる集合が **Fourier module** で、一般には

$$
\boxed{
\mathbf k=\sum_{j=1}^{D}n_j\mathbf b_j,
\qquad
n_j\in\mathbb Z
}
$$

と書ける。$D$ がその rank である。

周期結晶では通常 $D=d$ だが、準結晶では

$$
D>d
$$

となりうる。

なので準結晶は「逆空間に規則がない」のではなく、**逆空間の整数構造が物理空間の次元より高い**と見る方が自然になる。

## 4. なぜ高次元格子から Fourier module が出るのか

前の cut-and-project では、高次元格子点を physical space と internal space の二方向へ分解した。

波数空間でも同じことができる。

高次元側の reciprocal lattice にある一つの波数ベクトルを $\mathbf K$ とし、それを

$$
K_{\parallel}=P_{\parallel}\mathbf K,
\qquad
K_{\perp}=P_{\perp}\mathbf K
$$

と分ける。

低次元で観測される Bragg peak の位置は、その physical-space 成分

$$
\boxed{k=K_{\parallel}}
$$

として現れる。

高次元では普通の reciprocal lattice だったものが、低次元へ射影されると rank の高い Fourier module になる。

ここで、実空間の cut-and-project と逆空間の Fourier module が同じ高次元幾何学の表裏としてつながる。

## 5. peak の位置が密でも、回折像はなぜ連続にならないのか

1次元で $b_1/b_2$ が無理数なら

$$
\{mb_1+nb_2\mid m,n\in\mathbb Z\}
$$

という peak 候補の位置は実軸上で稠密になりうる。

ここは少し引っかかる。候補位置がどこにでもあるなら、回折像は鋭い peak ではなく連続的に埋まってしまいそうに見える。

ただ、**peak の位置が許されることと、その peak が強いことは別**である。

cut-and-project では、どの格子点を採用するかを acceptance window $W$ で決めた。波数空間では、その window の Fourier 変換が各 peak の振幅を重み付けする。

概念的には

$$
A(\mathbf K)\propto \widehat{1_W}(K_{\perp})
$$

となる。

例えば internal space で window が幅 $w$ の区間なら、

$$
\widehat{1_W}(K_{\perp})
\propto
\frac{\sin(K_{\perp}w/2)}{K_{\perp}/2}
$$

のような sinc 型の包絡が現れる。

そのため、候補位置が多数あっても、その多くは非常に弱い。

$$
\boxed{
\text{dense allowed positions}
\neq
\text{uniformly strong scattering}
}
$$

となる。

さらに、位置集合が密であることと、連続スペクトルであることも別である。理想的な Fibonacci chain では、回折は個々の鋭い Bragg peak からなる pure-point 型だが、その peak の位置集合自体は稠密になりうる。

$$
\boxed{
\text{dense pure-point support}
\neq
\text{diffuse continuum}
}
$$

「位置は高密度でも、強度は強く階層化され、各成分自体は鋭い」という像が近い。

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

この見方だと、準結晶の秩序は「実空間の単位胞」に保存されているのではなく、**有限 rank の波数構造と、それを生む高次元幾何学**に保存されている、と言えそうだ。

4本を通して並べると、

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

という流れで見えている。

実空間では周期を失っているが、構造を生成する整数的な秩序まで失われているわけではない。

ここから先は、inflation、periodic approximant、phason、Penrose tiling のような「準結晶特有の構造」を個別に掘る段階へ進めそうだ。

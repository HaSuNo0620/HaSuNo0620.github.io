---
title: "準結晶の回折をどう理解するか — 実空間は非周期、逆空間は離散的に秩序する"
summary: "周期格子を持たない準結晶がなぜ鋭いBragg peakを示すのかを、密度のFourier変換、Fourier module、高次元reciprocal lattice、windowの構造因子から整理する。"
publishedAt: 2026-09-12T02:48:00+09:00
area: "Physics"
topics: ["quasicrystals", "diffraction", "Fourier module", "reciprocal space", "cut and project"]
status: growing
---

[前のノート](/notes/fibonacci-cut-and-project/)では、Fibonacci chain を2次元格子からの cut-and-project として構成した。ここまで来ると、準結晶について最も重要な疑問に答えられる。

**実空間に並進周期がないのに、なぜ逆空間では鋭い Bragg peak が現れるのか。**

周期結晶では Bragg peak は reciprocal lattice の存在とほぼ同義なので、準結晶でも「隠れた周期格子」があるように見える。しかし物理空間そのものに通常の reciprocal lattice があるわけではない。

代わりに現れるのが Fourier module であり、その最も自然な起源が higher-dimensional reciprocal lattice である。

## 1. 回折は原子位置の位相和を見る

1次元の点集合 $\{x_j\}$ を最も単純に

$$
\rho(x)=\sum_j\delta(x-x_j)
$$

と表す。

Fourier 変換は

$$
\widetilde\rho(k)
=\sum_j e^{-ikx_j}
$$

であり、散乱強度は概念的には

$$
I(k)\propto |\widetilde\rho(k)|^2
$$

で与えられる。

ここで重要なのは、各原子が同じ振幅で足されるだけではなく、$e^{-ikx_j}$ という位相を持って加算されることである。

ある $k$ で遠く離れた原子からの寄与まで位相が揃えば、和は系サイズとともに coherent に増大し、鋭い Bragg peak が生じる。

したがって Bragg peak は、単なる局所秩序ではなく長距離にわたる位相コヒーレンスを見ている。

## 2. 周期結晶では位相整合条件が reciprocal lattice になる

周期 $a$ の1次元格子

$$
x_n=na,
\qquad n\in\mathbb Z
$$

を考える。

Fourier 振幅は

$$
\widetilde\rho(k)
=\sum_n e^{-ikna}
$$

である。

隣り合う格子点の位相差が $2\pi$ の整数倍、すなわち

$$
ka=2\pi m
$$

なら全項が同位相になり、

$$
k=G_m=\frac{2\pi m}{a}
$$

に Bragg peak が現れる。

$d$ 次元では

$$
\mathbf G
=\sum_{i=1}^{d}m_i\mathbf b_i,
\qquad
m_i\in\mathbb Z
$$

という reciprocal lattice になる。

周期結晶では real-space lattice の rank と reciprocal lattice の rank はどちらも空間次元 $d$ に等しい。

## 3. 準結晶では reciprocal lattice の代わりに Fourier module が現れる

準結晶の Bragg peak の位置を $\mathbf k$ とする。これらが $D$ 個の基底ベクトル $\mathbf b_1,\ldots,\mathbf b_D$ を使って

$$
\boxed{
\mathbf k
=\sum_{j=1}^{D}n_j\mathbf b_j,
\qquad
n_j\in\mathbb Z
}
$$

と表されるとする。

ここで重要なのは

$$
D>d
$$

となりうることである。

この整数線形結合の集合を Fourier module と呼ぶ。

周期結晶では $D=d$ なので通常の reciprocal lattice になる。準結晶では物理空間が $d$ 次元でも、それより多くの整数 index が必要になる。

したがって準結晶の逆空間構造は

$$
\boxed{
\text{no }d\text{-dimensional reciprocal lattice}
\quad\text{but}\quad
\text{a higher-rank Fourier module}
}
$$

と捉えるのがよい。

## 4. 1次元 Fibonacci chain でも rank は2になる

1次元周期格子なら Bragg peak は一つの基本波数 $k_0$ から

$$
k_n=nk_0
$$

と生成できる。

Fibonacci chain では、二つの rationally independent な基本波数 $b_1,b_2$ を使って

$$
\boxed{
k_{mn}=mb_1+nb_2,
\qquad m,n\in\mathbb Z
}
$$

と表す必要がある。

物理空間は1次元だが rank は $D=2$ である。

これは[準周期関数のノート](/notes/quasiperiodic-functions-torus/)で見た

$$
k_{\mathbf n}=\mathbf n\cdot\boldsymbol\omega
$$

と同じ構造である。

準周期関数と準結晶回折が同じ higher-rank Fourier geometry を共有していることが分かる。

## 5. cut-and-project すると peak の位置が自然に出る

2次元 direct lattice $\mathcal L\subset\mathbb R^2$ から1次元 Fibonacci chain を作ったとする。

2次元格子には通常の reciprocal lattice $\mathcal L^*$ があり、その reciprocal vector を $\mathbf K$ とする。

これを physical space と internal space に分解して

$$
K_{\parallel}=P_{\parallel}\mathbf K,
\qquad
K_{\perp}=P_{\perp}\mathbf K
$$

とする。

すると準結晶側の Bragg peak の位置は基本的に

$$
\boxed{
k=K_{\parallel}}
$$

として得られる。

つまり real space の点列と同じように、reciprocal space でも higher-dimensional lattice を physical space へ射影している。

ここで higher-dimensional description が単なる作図上の便法ではなくなる。原子配列だけでなく、回折 peak の index まで同じ $\mathbb Z^D$ 構造で整理できるからである。

## 6. window は peak の「位置」ではなく主に「強度」を決める

cut-and-project では internal space に acceptance window $W$ を置いた。

reciprocal space では、この window の Fourier 変換が Bragg peak の振幅へ現れる。

単純化して書けば、higher-dimensional reciprocal vector $\mathbf K$ に対する振幅は

$$
A(\mathbf K)
\propto
\widehat{1_W}(K_{\perp})
$$

となる。

ここで $1_W$ は window の indicator function である。

例えば1次元 internal space で幅 $w$ の区間 window を使えば

$$
\widehat{1_W}(K_{\perp})
\propto
\frac{\sin(K_{\perp}w/2)}{K_{\perp}/2}
$$

という sinc 型の包絡が現れる。

したがって

- $K_{\parallel}$ が Bragg peak の位置、
- $K_{\perp}$ と window がその強度、

を主に決める。

この対応は非常に重要である。physical space だけを見れば複雑な peak 強度列に見えるものが、高次元では「reciprocal lattice 点を window form factor で重み付けしたもの」になる。

## 7. 「Bragg peak は離散的」と「Fourier module は稠密」は矛盾しないのか

ここは準結晶回折で特に混乱しやすい。

1次元で $b_1/b_2$ が無理数なら

$$
\{mb_1+nb_2\mid m,n\in\mathbb Z\}
$$

は実軸上で稠密になる。

すると「Bragg peak が離散的」という説明と矛盾するように見える。

数学的には、理想 Fibonacci chain の pure-point diffraction の support は実際に稠密になりうる。つまり任意の波数区間に Bragg peak の位置が存在する。

しかし全ての peak が同じ強度を持つわけではない。$|K_{\perp}|$ が大きい peak は window form factor によって急速に弱くなる。

そのため、任意の有限強度 threshold を設定すると、観測される強い peak は疎になり、実験では鋭く分離した Bragg spots として見える。

したがって区別すべきなのは

$$
\boxed{
\text{dense set of allowed Bragg positions}
\neq
\text{uniformly strong dense scattering}
}
$$

である。

「準結晶の回折は離散的」という言い方は、diffuse continuum ではなく pure-point 的な鋭い peak からなる、という意味で理解する方が正確である。

## 8. では周期結晶との本質的な違いは何か

周期結晶でも準結晶でも鋭い Bragg peak がある。違いは peak の鋭さではなく、その index 構造にある。

周期結晶では

$$
\mathbf G
=\sum_{i=1}^{d}m_i\mathbf b_i
$$

と $d$ 個の基底で足りる。

準結晶では

$$
\mathbf k
=\sum_{j=1}^{D}n_j\mathbf b_j,
\qquad D>d
$$

となる。

つまり diffraction pattern は、physical space の次元より高い整数格子の影を持っている。

この意味で準結晶の回折は、実空間の非周期性とは反対に「高次元では周期的」であることを最も直接的に示す。

## 9. 回転対称性は Fourier module の幾何学として現れる

5回・10回・icosahedral などの対称性も、単に individual peak がその角度に並ぶというだけではない。

Fourier module 全体がその point-group symmetry の作用で閉じている必要がある。

周期格子なら crystallographic restriction によって許される回転は制限されるが、$D>d$ の module では物理空間に投影された基底がより多く取れるため、5回対称性などを持つ reciprocal pattern を構成できる。

つまり「禁制対称性」と「高rank Fourier module」は別々の特徴ではなく、同じ高次元構造の二つの表れである。

## 10. phonon と phason は Fourier 位相からも見える

準周期密度を

$$
\rho(\mathbf r)
=\sum_{\mathbf n}
\rho_{\mathbf n}
\exp\left[i\mathbf k_{\mathbf n}\cdot\mathbf r+i\phi_{\mathbf n}\right]
$$

とする。

周期結晶では長波長変位 $\mathbf u(\mathbf r)$ によって位相が

$$
\phi_{\mathbf n}\to
\phi_{\mathbf n}-\mathbf k_{\mathbf n}\cdot\mathbf u
$$

と変化する。これが phonon に対応する。

準結晶では $D>d$ なので、Fourier phase の独立自由度にも physical translation だけでは尽くせない成分が残る。それを higher-dimensional space で見ると perpendicular-space displacement となり、phason field に対応する。

したがって phason は real-space tiling の局所再配列としてだけでなく、**Fourier phase space の余分な連続自由度**としても理解できる。

## 11. 準結晶の「秩序」はどこに保存されているのか

ここまでを見ると、最初の疑問へかなり具体的に答えられる。

準結晶では実空間の並進周期性はない。しかし Fourier peak の位置は任意ではなく、有限個の基底から整数係数で生成される。

つまり秩序は

$$
\text{real-space unit cell}
$$

ではなく

$$
\boxed{
\text{finite-rank Fourier module}
}
$$

として保存されている。

この見方は、準結晶を「周期結晶から少し乱れたもの」と見るのとは全く違う。実空間の単位胞という秩序の表現を捨て、その代わりに Fourier phase と higher-dimensional integer structure が秩序を担っている。

## 12. 自分のための見取り図

4本のノートを通して、準結晶について今のところ中心に置くべき関係は

$$
\boxed{
\begin{aligned}
\text{aperiodic real-space order}
&\longleftrightarrow
\text{quasiperiodic Fourier expansion},\\
\text{cut-and-project set}
&\longleftrightarrow
\text{projected reciprocal lattice},\\
\text{acceptance window}
&\longleftrightarrow
\text{Bragg-intensity envelope},\\
D>d
&\longleftrightarrow
\text{extra phason degrees of freedom}.
\end{aligned}
}
$$

となる。

準結晶を「周期がない不思議な結晶」と覚えるより、

$$
\boxed{
\text{低次元では非周期}
\quad\Longleftrightarrow\quad
\text{高次元では整数格子で整理される}
}
$$

という二重の見方を持つ方が本質に近い。

この段階まで来ると、次に自然なのは構造の説明そのものではなく、**この準周期秩序の上に相互作用・統計力学を載せたとき何が変わるか**という問題である。Fibonacci Ising model や quasiperiodic coupling は、その接続点になる。

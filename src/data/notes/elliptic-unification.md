---
title: "楕円関数の統一 — 積分・周期格子・代数曲線"
summary: "GaussとJacobiの四次微分方程式をWeierstrassの三次方程式へ接続し、複素周期と代数曲線上の積分の関係を明らかにする。"
publishedAt: 2026-11-28T16:00:00+09:00
updatedAt: 2026-11-28
area: "Mathematics"
field: mathematics
kind: theory
topics: ["elliptic functions", "elliptic curves", "complex analysis"]
status: growing
---

楕円の幾何学から構成したJacobi関数と、零点の周期格子から構成したWeierstrass関数は、出発点も定義も異なる。両者が同じ理論に属するのはなぜか。本稿では微分方程式の変数変換を出発点として、積分・周期格子・代数曲線の関係を調べる。

前提となる構成は [円から楕円関数へ](./elliptic-functions-map) と [因数分解から楕円関数へ](./elliptic-factorization) に譲る。

## 1. 二つの微分方程式

Jacobiの正弦 $s=\operatorname{sn}(u,k)$ とWeierstrass関数 $x=\wp(z)$ は、それぞれ

$$
(s')^2=(1-s^2)(1-k^2s^2),\qquad
(x')^2=4x^3-g_2x-g_3
$$

を満たす。前者は四次式、後者は三次式である。双方とも変数分離すれば平方根を含む積分になるが、次数の違いはどのように解消されるのか。

## 2. GaussとJacobi

$k=1/\sqrt2$ のJacobi関数を用いて

$$
r(u)=\frac{1}{\sqrt2}
\frac{\operatorname{sn}(\sqrt2 u,k)}{\operatorname{dn}(\sqrt2 u,k)}
$$

と置く。Jacobiの微分系と代数関係を使うと $(r')^2=1-r^4$、$r(0)=0$、$r'(0)=1$ が得られる。したがって

$$
\operatorname{sl}(u)=\frac{\operatorname{sn}(\sqrt2 u,1/\sqrt2)}
{\sqrt2\,\operatorname{dn}(\sqrt2 u,1/\sqrt2)}.
$$

同じ微分方程式と初期条件を満たすという事実が、二つの構成を結びつける。特に $\ell=K(1/\sqrt2)/\sqrt2$ である。

## 3. JacobiとWeierstrass

三次式が実根 $e_1>e_2>e_3$ を持つ場合を考える。$A=e_1-e_3$、$k^2=(e_2-e_3)/A$ と置く。

$$
x=e_3+\frac{A}{s^2}
$$

を $(dx/dz)^2=4(x-e_1)(x-e_2)(x-e_3)$ に代入すれば、

$$
\left(\frac{ds}{dz}\right)^2=A(1-s^2)(1-k^2s^2).
$$

原点で $s\sim\sqrt A z$ となる枝を取ると、

$$
\wp(z)=e_3+
\frac{A}{\operatorname{sn}^2(\sqrt A z,k)}.
$$

四次式と三次式は別々の問題ではなく、変数変換によって結びつく。一般の複素根の場合は根の選択と平方根の枝を指定する必要がある。

Gaussの四次式についても $x=1/\operatorname{sl}^2u$ と置けば

$$
(x')^2=4x^3-4x,
$$

したがって $x=\wp(u;4,0)$ となる。これは正方形型の周期格子に対応する。


この変換は $s$ の符号を識別しない。四次曲線から三次曲線への写像をそのまま一対一の座標変換と呼ぶことはできない。実際、$\operatorname{sn}^2$ は $\operatorname{sn}$ より短い実周期を持つ。この違いが周期格子にも現れる。

## 4. 複素周期と楕円積分

$0<k<1$、$k'=\sqrt{1-k^2}$、$K'=K(k')$ とする。Jacobi関数の複素周期は、実軸上の周期に加えて虚軸方向にも現れる。虚引数変換

$$
\operatorname{sn}(iv,k)=i\frac{\operatorname{sn}(v,k')}{\operatorname{cn}(v,k')}
$$

は両辺が同じ微分方程式と原点での初期条件を満たすことから得られる。虚軸上で $v=K'$ に極が現れ、加法定理と解析接続から $\operatorname{sn}$ の基本周期は $4K,2iK'$ となる（虚引数変換と加法定理の詳細は参考文献を参照）。

従って $\operatorname{sn}^2$ の周期格子は $2K,2iK'$ で生成される。前節の変換で $A=e_1-e_3>0$ とした場合、Weierstrass関数の基本周期は

$$
\omega_1=\frac{2K}{\sqrt A},\qquad
\omega_2=\frac{2iK'}{\sqrt A}.
$$

完全楕円積分が周期格子の辺の長さを決めている。

## 5. 代数曲線と複素トーラス

因数分解から得たWeierstrass関数は

$$
(\wp')^2=4\wp^3-g_2\wp-g_3
$$

を満たす。写像 $z\mapsto(\wp(z),\wp'(z))$ は周期格子 $\Lambda$ に関する同値類だけに依存する。格子点では $\wp\sim z^{-2},\wp'\sim-2z^{-3}$ なので、射影曲線

$$
Y^2Z=4X^3-g_2XZ^2-g_3Z^3
$$

の無限遠点 $[0:1:0]$ に対応する。

この写像が一対一である理由は、$\wp(z)=x$ の解が重複度込みで二つあり、一般には $z,-z$ の組になることにある。$\wp'$ は奇関数なので二点を区別する。$\wp'=0$ の場合には半周期で二点が一致する。非零の三つの半周期はそれぞれ $\wp'$ の零点であり、$\wp'$ は三位の極を一つ持つので、これらの零点は単純である。対応する三つの $\wp$ の値も異なる。従って三次式は重根を持たず、

$$
\Delta=g_2^3-27g_3^2\ne0.
$$

任意の有限な曲線上の点 $(x,y)$ について $\wp(z)=x$ を解けば、微分方程式により $\wp'(z)=\pm y$ となる。必要に応じて $z$ の符号を変えれば指定した点を得る。無限遠点も含めて写像は全単射であり、コンパクトRiemann面間の正則な全単射なので双正則である。

逆方向では曲線上の微分 $dx/y$ を積分する。分岐点でも局所座標を使えば正則であり、無限遠点でも正則である。閉路に沿う積分の値が周期になる。曲線の種数が1であることから独立な二つの閉路を選ぶことができ、Abel積分による一様化定理では、その周期が張る格子による複素トーラスが得られる。本稿では任意の非特異三次曲線に対する逆方向の一様化定理の完全な証明までは扱わない。

原点近傍では、無限遠で平方根が $2t^{3/2}$ となる枝を選ぶと

$$
z=\int_{\wp(z)}^\infty\frac{dt}{\sqrt{4t^3-g_2t-g_3}}.
$$

楕円積分は曲線上の点からトーラスの座標を求め、楕円関数は逆にその座標から曲線上の点を復元する。

![三つの楕円関数の構成と代数曲線の関係](/figures/mathematics/elliptic-unification.svg)

*異なる出発点から得られた関数を、微分方程式と変数変換を通じて接続する概念図。*

## 6. 退化極限

$k\to0$ では $K\to\pi/2$、$K'\to\infty$ となり、Jacobi関数は三角関数へ退化する。$k\to1$ では $K\to\infty$ となり、固定した実引数で

$$
\operatorname{sn}u\to\tanh u,\qquad
\operatorname{cn}u,\operatorname{dn}u\to\operatorname{sech}u.
$$

この極限は周期格子の一方向が無限に伸びることに対応する。


代数曲線の側でも対応する根が合流する。例えば $e_2\to e_3$ では $k\to0$ となり、$e_1\to e_2$ では $k\to1$ となる（$A$ を有限の正値に保つ）。いずれも判別式がゼロに近づき、二重周期の関数は一重周期の三角関数または双曲線関数に退化する。

このように、楕円積分の極限、周期格子の一方向の発散、代数曲線の根の合流は同じ退化を異なる側面から記述している。

## 参考文献

- [NIST DLMF, Chapter 22: Jacobian Elliptic Functions](https://dlmf.nist.gov/22)
- [NIST DLMF, Chapter 23: Weierstrass Elliptic and Modular Functions](https://dlmf.nist.gov/23)
- E. T. Whittaker and G. N. Watson, *A Course of Modern Analysis*.

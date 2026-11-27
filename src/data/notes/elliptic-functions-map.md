---
title: "楕円積分の逆関数と複素トーラス"
summary: "振り子の運動からJacobi楕円関数を導き、Weierstrass関数、周期格子、非特異な三次曲線との対応を具体化する。"
publishedAt: 2026-09-09T18:30:00+09:00
updatedAt: 2026-11-28
area: "Mathematics"
field: mathematics
kind: theory
topics: ["elliptic functions", "special functions", "complex analysis"]
status: growing
---

楕円関数は、四次または三次多項式の平方根を含む積分を逆にすることで現れる。実変数では非線形振動の解を与えるが、複素変数に拡張すると二つの独立な周期を持つ有理型関数となる。

![振り子の運動から楕円積分の逆関数が現れ、複素解析接続と変数変換を通じて周期格子や楕円曲線へつながる](/figures/mathematics/elliptic-connections.svg)

*振り子の運動から楕円積分の逆関数が現れ、複素解析接続と変数変換を通じて周期格子や楕円曲線へつながる。格子と三次曲線は構造を示す模式図で、特定の同一母数に対する図ではない。*

## 振り子の運動と第一種楕円積分

単振り子の方程式を $\ddot\theta+\omega_0^2\sin\theta=0$ とする。振幅 $\theta_{\max}\in(0,\pi)$ の振動についてエネルギー保存則は

$$
\dot\theta^2=4\omega_0^2[k^2-\sin^2(\theta/2)],
\qquad k=\sin(\theta_{\max}/2).
$$

$\sin(\theta/2)=kx$ と変数変換し、$\theta=0$ を正の速度で通過する時刻を原点に選ぶと、

$$
\omega_0t=\int_0^x\frac{ds}{\sqrt{(1-s^2)(1-k^2s^2)}}.
$$

これは第一種楕円積分である。なお、楕円の弧長に現れる典型的な積分は第二種楕円積分であり、両者は異なる。楕円積分を逆にすることで得られる関数をJacobi楕円関数と呼ぶ。

## Jacobi楕円関数

第一種楕円積分の逆関数を $x=\operatorname{sn}(u,k)$ と定義すれば、逆関数の微分から

$$
(\operatorname{sn}'u)^2=(1-\operatorname{sn}^2u)
(1-k^2\operatorname{sn}^2u).
$$

原点近傍で $\operatorname{cn}u=\sqrt{1-\operatorname{sn}^2u}$、$\operatorname{dn}u=\sqrt{1-k^2\operatorname{sn}^2u}$ と定め、解析接続する。微分方程式は

$$
\operatorname{sn}'=\operatorname{cn}\operatorname{dn},\quad
\operatorname{cn}'=-\operatorname{sn}\operatorname{dn},\quad
\operatorname{dn}'=-k^2\operatorname{sn}\operatorname{cn}
$$

となる。ここでは引数の母数 $k$ を省略した。振り子の解は $\theta(t)=2\arcsin[k\operatorname{sn}(\omega_0t,k)]$ と書ける。

完全第一種楕円積分を

$$
K(k)=\int_0^1\frac{ds}{\sqrt{(1-s^2)(1-k^2s^2)}}
$$

とすると、振り子の周期は $4K(k)/\omega_0$ である。小振幅極限 $k\to0$ では $K\to\pi/2$ となり、周期は $2\pi/\omega_0$ に戻る。分離軌道に近づく $k\to1$ では $K$ は発散する。

同じ極限でJacobi関数は

$$
\begin{array}{c|ccc}
 &\operatorname{sn}(u,k)&\operatorname{cn}(u,k)&\operatorname{dn}(u,k)\\ \hline
k\to0&\sin u&\cos u&1\\
k\to1&\tanh u&\operatorname{sech}u&\operatorname{sech}u
\end{array}
$$

となる。これは固定した実引数での極限である。

![振り子の最大振幅と周期](/figures/mathematics/pendulum-period.svg)

*完全第一種楕円積分から計算した周期と小振幅近似の比較。最大振幅が180度に近づくと周期が発散する。*

## 複素周期格子

$0<k<1$ で補母数を $k'=\sqrt{1-k^2}$、$K'=K(k')$ とすると、$\operatorname{sn}(u,k)$ の基本周期は $4K$ と $2iK'$ である。これは実方向と虚方向に独立な二重周期性である。$\operatorname{cn},\operatorname{dn}$ の周期格子は同一とは限らない。

一般に実線形独立な複素数 $\omega_1,\omega_2$ によって

$$
\Lambda=\mathbb Z\omega_1+\mathbb Z\omega_2
$$

を定める。両周期について不変な有理型関数は複素トーラス $\mathbb C/\Lambda$ 上の有理型関数と同一視できる。非定数の二重周期関数が極を必要とするのは、極がなければコンパクトな基本領域上で有界となり、Liouvilleの定理によって定数になってしまうためである。

$k\to0$ では $K'\to\infty$、$k\to1$ では $K\to\infty$ となる。周期格子の一方向が退化することが、三角関数や双曲線関数への極限に対応する。

## Weierstrass関数と三次曲線

周期格子に対して

$$
\wp(z)=\frac1{z^2}+
\sum_{\omega\in\Lambda\setminus\{0\}}
\left[\frac1{(z-\omega)^2}-\frac1{\omega^2}\right]
$$

を定義する。格子点を除けば級数は局所一様に収束する。$\wp$ は偶関数であり、格子周期を持つ。原点のLaurent展開は

$$
\wp(z)=z^{-2}+\frac{g_2}{20}z^2+\frac{g_3}{28}z^4+O(z^6),
$$

$$
g_2=60\sum_{\omega\ne0}\omega^{-4},\qquad
g_3=140\sum_{\omega\ne0}\omega^{-6}
$$

となる。

この展開を用いると $(\wp')^2-4\wp^3+g_2\wp+g_3$ の極と定数項が消える。二重周期で正則な関数は定数なので、

$$
(\wp')^2=4\wp^3-g_2\wp-g_3
$$

を得る。したがって $x=\wp(z),y=\wp'(z)$ は曲線

$$
y^2=4x^3-g_2x-g_3
$$

上にある。判別式 $g_2^3-27g_3^2\ne0$ のとき曲線は非特異である。無限遠点を加えたこの曲線と複素トーラスとの対応は、複素楕円曲線の一様化定理によって厳密に与えられる。格子点は無限遠点に対応する。

## Jacobi形式からWeierstrass形式へ

三次式を $4(x-e_1)(x-e_2)(x-e_3)$ と因数分解する。実根が $e_1>e_2>e_3$ と並ぶ場合を考え、

$$
A=e_1-e_3,\qquad k^2=\frac{e_2-e_3}{A}
$$

とおく。$x=e_3+A/s^2$ を微分方程式に代入すると、

$$
\left(\frac{ds}{dz}\right)^2
=A(1-s^2)(1-k^2s^2)
$$

となる。原点近傍で $s\sim\sqrt A z$ となる枝を選ぶと、

$$
\wp(z)=e_3+
\frac{e_1-e_3}{\operatorname{sn}^2(\sqrt{e_1-e_3}\,z,k)}
$$

を得る。ここでは $e_1+e_2+e_3=0$ であり、原点でのLaurent展開の定数項も消える。

この変換は、二つの楕円関数の形式が同じ種類の代数曲線を異なる座標で記述することを具体的に示している。一般の複素格子では根の順序と平方根の枝を別途指定する必要がある。

## 参考文献

- NIST Digital Library of Mathematical Functions, Chapters 19, 22, 23.
- E. T. Whittaker and G. N. Watson, *A Course of Modern Analysis*.

文献の該当節との照合と周期規約の独立検算は公開前に行う。

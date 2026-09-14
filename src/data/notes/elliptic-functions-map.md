---
title: "楕円関数をどう見渡すか — 積分の逆関数から複素トーラスまで"
summary: "楕円積分の逆関数としてのJacobi楕円関数と、二重周期関数としてのWeierstrass楕円関数をひとつの地図に置く。"
publishedAt: 2026-09-09T18:30:00+09:00
updatedAt: 2026-09-14
area: "Mathematics"
topics: ["elliptic functions", "special functions", "complex analysis"]
status: growing
---

楕円関数は、三角関数の単なる一般化というより、**積分を逆にすることと複素平面上の周期性が出会う場所**として見るとつながりがよい。

## 楕円積分から逆関数へ

円の弧長や振り子の運動などでは

$$
u=\int_0^x \frac{dt}{\sqrt{(1-t^2)(1-k^2t^2)}}
$$

のような積分が自然に現れる。

三角関数の場合

$$
u=\int_0^x \frac{dt}{\sqrt{1-t^2}}=\arcsin x
$$

を逆にすると $x=\sin u$ になる。

同じ操作で楕円積分を逆にしたものが Jacobi の楕円関数

$$
x=\operatorname{sn}(u,k)
$$

である。

さらに

$$
\operatorname{cn}^2u+\operatorname{sn}^2u=1,
$$

$$
\operatorname{dn}^2u+k^2\operatorname{sn}^2u=1
$$

という関係から $\operatorname{cn}$ と $\operatorname{dn}$ も現れる。

## 三角関数との連続性

$k\to0$ では

$$
\operatorname{sn}(u,k)\to\sin u,\qquad
\operatorname{cn}(u,k)\to\cos u,\qquad
\operatorname{dn}(u,k)\to1.
$$

一方 $k\to1$ では双曲線関数に近づく。

Jacobi 楕円関数は三角関数と双曲線関数の間を連続的につなぐ族でもあるが、複素変数へ拡張したときにはさらに**2つの独立な周期**が現れる。

## 二重周期性は複素トーラスの幾何になる

三角関数の周期は1方向だけである。たとえば

$$
\sin(z+2\pi)=\sin z.
$$

楕円関数では2つの複素数 $\omega_1,\omega_2$ に対して

$$
f(z+\omega_1)=f(z),\qquad
f(z+\omega_2)=f(z)
$$

となる。

複素平面を格子

$$
\Lambda=\{m\omega_1+n\omega_2\mid m,n\in\mathbb Z\}
$$

で割った

$$
\mathbb C/\Lambda
$$

が自然な舞台になり、位相的にはトーラスになる。

楕円関数を「複素トーラス上の有理型関数」と見ると、二重周期性は公式ではなく幾何として読める。

## Weierstrass の $\wp$ 関数

Weierstrass の楕円関数は

$$
\wp(z)=\frac{1}{z^2}
+\sum_{\omega\in\Lambda\setminus\{0\}}
\left[
\frac{1}{(z-\omega)^2}-\frac{1}{\omega^2}
\right]
$$

で定義される。

この関数は

$$
(\wp')^2=4\wp^3-g_2\wp-g_3
$$

を満たす。

ここで代数曲線

$$
y^2=4x^3-g_2x-g_3
$$

が現れる。

つまり

- 楕円積分
- 二重周期関数
- 複素トーラス
- 三次曲線

が同じ対象の別の顔になっている。

## Jacobi と Weierstrass は座標の違いに近い

Jacobi形式は物理的な境界条件や実変数の運動を扱うときに便利である。$\operatorname{sn},\operatorname{cn},\operatorname{dn}$ が三角関数に似ているため、振動問題との対応も見やすい。

Weierstrass形式は複素解析・代数幾何とのつながりが見やすい。ひとつの $\wp$ 関数とその微分に構造が集約される。

どちらかが本質というより、**同じ楕円曲線的構造を異なる座標で見ている**と考える方が自然に見える。

## 自分のための見取り図

今のところ中心に置いているのは

$$
\text{elliptic integral}
\longrightarrow
\text{inverse function}
\longrightarrow
\text{doubly periodic function}
\longrightarrow
\text{complex torus}
\longleftrightarrow
\text{elliptic curve}
$$

という連鎖である。

特殊関数として公式を覚えるより、この変換関係を押さえた方が、その先の theta 関数やモジュラー形式にもつながりやすい。

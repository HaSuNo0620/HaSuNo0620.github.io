---
title: "楕円関数をどう見渡すか — 積分の逆関数から複素トーラスまで"
summary: "楕円積分の逆関数としてのJacobi楕円関数と、二重周期関数としてのWeierstrass楕円関数をひとつの地図に置く。"
publishedAt: 2026-09-09T18:30:00+09:00
topics: ["elliptic functions", "special functions", "complex analysis"]
status: growing
---

楕円関数は、三角関数の単なる一般化として見るより、**積分を逆にすることと複素平面上の周期性が出会う場所**として見ると理解しやすい。

## 出発点は楕円積分

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

同じ発想で楕円積分を逆にしたものが Jacobi の楕円関数

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

## 三角関数との対応

$k\to0$ では

$$
\operatorname{sn}(u,k)\to\sin u,\qquad
\operatorname{cn}(u,k)\to\cos u,\qquad
\operatorname{dn}(u,k)\to1.
$$

一方 $k\to1$ では双曲線関数に近づく。

つまり Jacobi 楕円関数は、三角関数と双曲線関数の間を連続的につなぐような族でもある。

ただし本質はそこだけではない。複素変数へ拡張すると、楕円関数は**2つの独立な周期**を持つ。

## なぜ二重周期なのか

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

したがって複素平面を格子

$$
\Lambda=\{m\omega_1+n\omega_2\mid m,n\in\mathbb Z\}
$$

で割った

$$
\mathbb C/\Lambda
$$

という空間が自然に現れる。これは位相的にはトーラスである。

楕円関数を「複素トーラス上の有理型関数」と見ると、二重周期性は偶然ではなく幾何学になる。

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

ここで急に代数曲線

$$
y^2=4x^3-g_2x-g_3
$$

が現れる。

つまり

- 楕円積分、
- 二重周期関数、
- 複素トーラス、
- 三次曲線

が同じ対象の別の顔になっている。

## Jacobi と Weierstrass はどう違うか

Jacobi形式は物理的な境界条件や実変数の運動を扱うときに便利である。$\operatorname{sn},\operatorname{cn},\operatorname{dn}$ が三角関数に似ているため、振動問題との対応も見やすい。

Weierstrass形式は複素解析・代数幾何とのつながりが見やすい。ひとつの $\wp$ 関数とその微分に構造が集約される。

どちらかが本質というより、**同じ楕円曲線的構造を異なる座標で見ている**と考える方が自然だと思う。

## 自分のための見取り図

今のところは

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

という流れを中心に置いている。

特殊関数として公式を覚えるより、この変換の連鎖を理解した方が、その先の theta 関数やモジュラー形式へ進むときにも迷いにくい。

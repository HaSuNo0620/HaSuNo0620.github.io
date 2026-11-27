---
title: "準周期関数とトーラス上の直線軌道"
summary: "周波数加群、トーラス軌道の稠密性、一様近似周期を区別し、準周期性を数学的に定式化する。"
publishedAt: 2026-09-12T02:46:00+09:00
updatedAt: 2026-11-28
area: "Mathematics"
field: quasicrystals
kind: theory
topics: ["quasiperiodicity", "Fourier analysis", "torus", "dynamical systems", "quasicrystals"]
status: growing
---

$f(x)=\cos x+\cos(\sqrt2 x)$ は二つの周期関数の和だが、全体としては周期を持たない。その非周期性は、二つの位相を独立な座標とすることで、トーラス上の直線運動として記述できる。

![周期関数と準周期関数の位相軌道](/figures/quasicrystals/quasiperiodic-signal-phase.svg)

## 周期が存在する条件

異なる実周波数の有限和

$$
f(x)=\sum_{j=1}^{M}c_j e^{ik_jx},\qquad c_j\ne0
$$

を考える。$T$ が周期なら

$$
\sum_j c_j(e^{ik_jT}-1)e^{ik_jx}=0
$$

が全ての $x$ で成立する。異なる指数関数の線形独立性から $k_jT\in2\pi\mathbb Z$ が全成分について必要であり、逆にこの条件は十分である。

従って非零周波数が一つの基本周波数の整数倍に収まる場合に限り、非定数の有限和は周期を持つ。冒頭の例では $T=2\pi m$、$\sqrt2 T=2\pi n$ を同時に満たす非零の $T$ は存在しない。

周波数が有理独立であることは、二つ以上の周波数を持つ有限和が非周期的であるための十分条件だが、必要条件ではない。例えば $\{1,\sqrt2,1+\sqrt2\}$ には整数関係があるものの、対応する三成分の和には周期がない。

## トーラスによる表示

$\mathbb T^D=\mathbb R^D/(2\pi\mathbb Z)^D$ 上の連続関数 $F$ に対して

$$
f(x)=F(\boldsymbol\theta_0+x\boldsymbol\omega)
$$

と定義する。以下ではこのような有限次元トーラス表示を持つ関数を準周期関数と呼ぶ。周期関数も特殊例として含める。

軌道の閉包は、整数関係 $\mathbf n\cdot\boldsymbol\omega=0$ によって定まる部分トーラスの平行移動である。Kroneckerの定理によれば、連続時間の軌道がトーラス全体で稠密になるための必要十分条件は

$$
\mathbf n\cdot\boldsymbol\omega\ne0
\quad(\mathbf n\in\mathbb Z^D\setminus\{0\})
$$

である。離散時間の写像では条件が異なり、位相の進みが $2\pi$ の整数倍になる場合も除く必要がある。

軌道が稠密でも、観測関数 $F$ が一部の座標だけに依存すれば $f$ は周期的になりうる。軌道の性質と観測関数の周期性を区別する必要がある。

## 一様な近似周期

冒頭の例で整数 $m,n$ を選び $T=2\pi m$ とすると、

$$
\sup_x|f(x+T)-f(x)|
\le 2\pi|m\sqrt2-n|.
$$

有理近似により右辺を任意に小さくできる。これは特定の位置で波形が偶然一致することとは異なる。

一般に連続な $F$ はコンパクトなトーラス上で一様連続である。従って位相移動 $T\boldsymbol\omega$ が原点に十分近ければ、全ての $x$ について $|f(x+T)-f(x)|$ が小さくなる。さらに軌道閉包のコンパクト性から、任意の精度の再帰時刻は相対稠密である。実際、原点近傍の軌道による平行移動で閉包を覆い、有限部分被覆を選ぶと、任意の長い時刻に対して有界な補正で再帰できる。

この性質はBohr概周期性の定義を満たす。有限次元トーラス表示を持たない概周期関数もあるため、概周期性はより広い概念である。

## 周波数加群

トーラス上のFourier係数を $F_{\mathbf n}$ とする。絶対収束する場合は

$$
f(x)=\sum_{\mathbf n\in\mathbb Z^D}
F_{\mathbf n}e^{i\mathbf n\cdot\boldsymbol\theta_0}
e^{i(\mathbf n\cdot\boldsymbol\omega)x}
$$

と書ける。連続性だけでは通常のFourier級数の点ごとの収束を保証しないが、多次元Fejér和による一様近似は可能である。

許容周波数は整数加群

$$
\mathcal M=\{\mathbf n\cdot\boldsymbol\omega:
\mathbf n\in\mathbb Z^D\}
$$

に属する。有理独立な基底ならその階数は $D$ である。ただし実際の非零Fourier成分が生成する部分加群は、許容加群より小さくなりうる。

例えば $\cos x+\cos(\sqrt2 x)+\cos[(1+\sqrt2)x]$ の周波数加群の階数は3ではなく2である。周波数の個数と独立な整数基底の個数は異なる。

この整数構造は、離散点集合の回折にも現れる。ただし点集合は連続なトーラス関数そのものではないため、次の[Fibonacci点列](/notes/fibonacci-cut-and-project/)では選択窓を用いて格子点を採用する別の構成を導入する。

## 参考文献

- H. Bohr, *Almost Periodic Functions*.
- M. Baake and U. Grimm, *Aperiodic Order, Vol. 1: A Mathematical Invitation*, Cambridge University Press (2013).

書誌と定理の原典照合は公開前に行う。

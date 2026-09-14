---
title: "準周期関数 — 複数周期の重ね合わせから高次元トーラスへ"
summary: "具体例 f(x)=cos x+cos(sqrt(2)x) を出発点に、周期が存在しない理由と、それでも規則性が失われない理由を考える。準周期性を高次元トーラス上の直線運動として理解する。"
publishedAt: 2026-09-12T02:46:00+09:00
updatedAt: 2026-09-14
area: "Mathematics"
topics: ["quasiperiodicity", "Fourier analysis", "torus", "dynamical systems", "quasicrystals"]
status: growing
---

[前のノート](/notes/quasicrystal-order-without-periodicity/)では、周期性を失っても秩序は残りうると整理した。

「**非周期なのに規則的**」という状態を最小の式にすると、

$$
\boxed{
f(x)=\cos x+\cos(\sqrt2\,x)
}
$$

くらいまで単純化できる。乱数も欠陥もない。それでも周期関数ではない。

![周期関数と準周期関数、対応する位相軌道](/figures/quasicrystals/quasiperiodic-signal-phase.svg)

*上段では有理数比 $1:2$ の重ね合わせは繰り返すが、無理数比 $1:\sqrt2$ は同じ形へ厳密には戻らない。下段では、その違いを二つの位相を座標にした空間で見ている。*

## 1. 周期条件は二つの位相の同時帰還になる

$f(x)$ に周期 $T$ があるなら

$$
f(x+T)=f(x)
$$

が全ての $x$ で成り立つ必要がある。

二つの cosine が同時に元の位相へ戻るには

$$
T=2\pi m,
\qquad
\sqrt2\,T=2\pi n,
\qquad
m,n\in\mathbb Z
$$

でなければならない。

両式を割ると

$$
\sqrt2=\frac nm
$$

となるが、$\sqrt2$ は無理数なので不可能である。

有限な周期 $T$ は存在しない。非周期性は複雑な式から出ているのではなく、**二つの単純な周期運動が互いに整合しない**ことから生じている。

## 2. 有理数比なら軌道は閉じる

比較として

$$
g(x)=\cos x+\cos(2x)
$$

を考える。

こちらでは第1成分が1周する間に第2成分は2周するので、$T=2\pi$ で両方が同時に元へ戻る。

一般に

$$
f(x)=\sum_{j=1}^{D}A_j\cos(\omega_jx+\phi_j)
$$

で、全ての周波数が一つの共通周期に整合するなら周期関数になる。

逆に、周波数の間に

$$
\sum_{j=1}^{D}n_j\omega_j=0,
\qquad n_j\in\mathbb Z
$$

という非自明な整数関係がないとき、共通周期は作れない。この性質を rationally independent と呼ぶ。

用語より、**どの有限距離だけ進んでも、全ての位相を同時に元へ戻せない**という意味の方が重要である。

## 3. 二つの位相はトーラス上の座標になる

$\cos x+\cos(\sqrt2 x)$ に対して

$$
\theta_1=x,
\qquad
\theta_2=\sqrt2\,x
$$

と置く。

すると

$$
f(x)=F(\theta_1,\theta_2),
\qquad
F(\theta_1,\theta_2)=\cos\theta_1+\cos\theta_2
$$

である。

$\theta_1$ も $\theta_2$ も角度なので、$2\pi$ 進めば同じ状態へ戻る。各座標を円として閉じると、二つの円を独立に持つ **2次元トーラス** が現れる。

$$
\mathbb T^2
=\mathbb R^2/(2\pi\mathbb Z)^2
$$

$x$ を増やすことは、この空間で

$$
(\theta_1,\theta_2)
=(x,\sqrt2\,x)
$$

と進むことに対応する。

比が $1:2$ なら軌道は有限距離で閉じる。比が $1:\sqrt2$ なら閉じず、長く進むとトーラス上のどの場所にもいくらでも近づく。この性質を軌道が稠密であるという。

1次元で見えていた「戻ってこない波形」は、高次元では単純な直線運動になる。

$$
\boxed{
\text{1D quasiperiodicity}
=\text{periodic geometry in higher dimension}
+\text{irrational direction}
}
$$

## 4. 再帰は厳密反復ではなく再接近になる

厳密な周期はないが、波形を見ると似た形は何度も現れる。

無理数は有理数でいくらでもよく近似できる。例えば

$$
\sqrt2\simeq\frac{99}{70}
$$

なら、ある長い距離を進んだとき二つの位相は同時にほぼ整数周だけ進む。

そのため

$$
f(x+T)\simeq f(x)
$$

となる大きな $T$ は何度も現れる。しかし等号にはならない。

周期関数では同じ構造が厳密に反復する。準周期関数では、**同じ状態へ厳密には戻らないが、任意に近く再接近する**。

この意味では、準周期性は「周期が壊れた状態」というより、**複数の周期的自由度が高次元ではそのまま残っている状態**と見た方が自然である。

## 5. Fourier 空間では有限 rank の波数集合になる

トーラス上の $F(\boldsymbol\theta)$ は各角度方向に周期的なので、通常の Fourier 級数で展開できる。

$$
F(\boldsymbol\theta)
=\sum_{\mathbf n\in\mathbb Z^D}
F_{\mathbf n}e^{i\mathbf n\cdot\boldsymbol\theta}
$$

ここで $\boldsymbol\theta=x\boldsymbol\omega$ を代入すると

$$
f(x)
=\sum_{\mathbf n\in\mathbb Z^D}
F_{\mathbf n}e^{i(\mathbf n\cdot\boldsymbol\omega)x}
$$

となる。

1次元で現れる波数は

$$
\boxed{
k_{\mathbf n}=\sum_{j=1}^{D}n_j\omega_j}
$$

である。

周期関数なら独立な基本波数は1個で、全ての peak はその整数倍に並ぶ。準周期関数では1次元でも複数の独立な基本波数が必要になる。

この「1次元なのに複数の整数 index が必要」という構造が、準結晶の Fourier module へつながる。

## 6. 準周期は一般の非周期よりかなり狭い

周期を持たない関数が全て準周期というわけではない。

準周期関数には、有限個の独立な基本周波数

$$
\omega_1,\ldots,\omega_D
$$

があり、高次元トーラス上の周期関数として表せる、という強い構造がある。

概念的には

$$
\text{periodic}
\subset
\text{quasiperiodic}
\subset
\text{almost periodic}
$$

という位置づけになる。

almost periodic はさらに広く、有限個の基本周波数だけには限られない。ランダム関数や一般の非周期関数が自動的にここへ入るわけでもない。

準結晶で欲しいのは単なる非周期性ではなく、**有限 rank の周波数構造を持つ非周期秩序**である。

## 7. いま置いている像

$$
\boxed{
\text{準周期性}
=\text{高次元では周期的}
+\text{低次元からは無理数方向に見ている}
}
$$

という像が今のところ一番使いやすい。

1次元では「いつ同じ形へ戻るか」という不整合に見えていたものが、2次元では**軌道の傾きが周期格子と整合しない**という幾何学に置き換わる。

この考え方を離散点集合へ移すと、cut-and-project 法と Fibonacci chain が現れる。

---
title: "準周期関数 — 複数周期の重ね合わせから高次元トーラスへ"
summary: "具体例 f(x)=cos x+cos(sqrt(2)x) を出発点に、周期が存在しない理由と、それでも規則性が失われない理由を考える。準周期性を高次元トーラス上の直線運動として理解する。"
publishedAt: 2026-09-12T02:46:00+09:00
updatedAt: 2026-09-13
area: "Mathematics"
topics: ["quasiperiodicity", "Fourier analysis", "torus", "dynamical systems", "quasicrystals"]
status: growing
---

[前のノート](/notes/quasicrystal-order-without-periodicity/)では、周期性を失っても秩序は残りうると整理した。

ただ、「**非周期なのに規則的**」という状態は、言葉だけだとまだ少し掴みにくい。そこで一つの関数だけを見る。

$$
\boxed{
f(x)=\cos x+\cos(\sqrt2\,x)
}
$$

乱数も欠陥も入っていない。それでも周期関数ではない。

![周期関数と準周期関数、対応する位相軌道](/figures/quasicrystals/quasiperiodic-signal-phase.svg)

*上段では有理数比 $1:2$ の重ね合わせは繰り返すが、無理数比 $1:\sqrt2$ は同じ形へ厳密には戻らない。下段では、その違いを二つの位相を座標にした空間で見ている。*

## 1. まず周期を探してみる

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

したがって有限な周期 $T$ は存在しない。

非周期性が複雑な式から出ているわけではなく、**二つの単純な周期運動が互いに整合しない**だけで生じているのが面白い。

## 2. 周波数比が有理数なら何が違うか

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

用語より、**どの有限距離だけ進んでも、全ての位相を同時に元へ戻せない**という意味の方を覚えておきたい。

## 3. 二つの位相を別々の座標にすると何が見えるか

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

$\theta_1$ も $\theta_2$ も角度なので、$2\pi$ 進めば同じ状態へ戻る。各座標を「端と端をつないだ円」として考えると、二つの円を独立に持つ空間になる。

これが **2次元トーラス** で、記号では

$$
\mathbb T^2
=\mathbb R^2/(2\pi\mathbb Z)^2
$$

と書く。要するに、$\theta_1$ と $\theta_2$ の両方向で $2\pi$ 離れた点を同じ点とみなしている。

$x$ を増やすことは、この空間で

$$
(\theta_1,\theta_2)
=(x,\sqrt2\,x)
$$

と進むことに対応する。

比が $1:2$ なら、ある有限距離で二つの位相が同時に元へ戻るので軌道は閉じる。

一方、比が $1:\sqrt2$ なら閉じない。長く進むと、トーラス上のどの場所にもいくらでも近づいていく。この性質を「軌道が稠密である」という。

1次元で見えていた「戻ってこない波形」が、高次元では単純な直線運動になる。

$$
\boxed{
\text{1D quasiperiodicity}
=\text{periodic geometry in higher dimension}
+\text{irrational direction}
}
$$

この見方は、後の cut-and-project とかなりよく似ている。

## 4. なぜ「ほぼ同じ形」は何度も現れるのか

厳密な周期はないが、波形を見ると似た形は何度も現れる。

無理数も有理数でいくらでもよく近似できる。例えば

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

この違いはかなり本質的に見える。

ここで「準周期」は、単に周期が壊れた状態ではなく、**複数の周期的自由度が高次元ではそのまま残っている状態**として見えてくる。

## 5. Fourier 空間では何が変わるか

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

したがって1次元で現れる波数は

$$
\boxed{
k_{\mathbf n}=\sum_{j=1}^{D}n_j\omega_j}
$$

である。

周期関数なら独立な基本波数は1個で、全ての peak はその整数倍に並ぶ。準周期関数では1次元でも複数の独立な基本波数が必要になる。

この「1次元なのに複数の整数 index が必要」という構造が、後で準結晶の回折を整理する Fourier module につながる。

## 6. 準周期関数は「非周期関数全部」ではない

ここまでの話だけだと、「周期でなければ準周期なのか」と見えやすいが、そうではない。

準周期関数には、有限個の独立な基本周波数

$$
\omega_1,\ldots,\omega_D
$$

があり、それらから高次元トーラス上の周期関数として表せる、というかなり強い構造がある。

概念的には

$$
\text{periodic}
\subset
\text{quasiperiodic}
\subset
\text{almost periodic}
$$

という包含関係がある。

almost periodic はさらに広い概念で、有限個の基本周波数に限らない。一方、ランダム関数や一般の非周期関数が自動的にこの中へ入るわけではない。

この区別は、準結晶を「非周期なら何でもよい」と誤解しないために役に立つ。

準結晶で欲しいのは、単なる非周期性ではなく、**有限 rank の周波数構造を持つ非周期秩序**である。

## 7. 高次元へ行く意味

高次元表示は、非周期性を消しているわけではない。

1次元では「いつ同じ形へ戻るか」という不整合として見えていたものを、2次元では**軌道の傾きが周期格子と整合しない**という幾何学へ置き換えている。

$$
\text{nonperiodic repetition problem}
\quad\longrightarrow\quad
\text{irrational geometry problem}
$$

という変換だと思えばよい。

今のところは、

$$
\boxed{
\text{準周期性}
=\text{高次元では周期的}
+\text{低次元からは無理数方向に見ている}
}
$$

という像で十分そうだ。

[次の Cut-and-project 法のノート](/notes/fibonacci-cut-and-project/)では、この考え方を連続関数ではなく点集合へ移す。高次元の周期格子から1次元の Fibonacci chain がどう現れるかを見る。

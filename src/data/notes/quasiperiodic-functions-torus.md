---
title: "準周期関数 — 複数周期の重ね合わせから高次元トーラスへ"
summary: "具体例 f(x)=cos x+cos(sqrt(2)x) を出発点に、周期が存在しない理由と、それでも規則性が失われない理由を考える。準周期性を高次元トーラス上の直線運動として理解する。"
publishedAt: 2026-09-12T02:46:00+09:00
updatedAt: 2026-09-13
area: "Mathematics"
topics: ["quasiperiodicity", "Fourier analysis", "torus", "dynamical systems", "quasicrystals"]
status: growing
---

[前のノート](/notes/quasicrystal-order-without-periodicity/)では、周期性を失っても秩序は残りうると考えた。

ただ、それだけではまだ「**非周期なのに規則的とは、実際にはどんな状態なのか**」が掴みにくい。

そこで一つの関数だけを考える。

$$
\boxed{
f(x)=\cos x+\cos(\sqrt2\,x)
}
$$

この関数には乱数も欠陥も入っていない。それでも周期関数ではない。

![周期関数と準周期関数、対応する位相軌道](/figures/quasicrystals/quasiperiodic-signal-phase.svg)

*上段では有理数比 $1:2$ の重ね合わせは繰り返すが、無理数比 $1:\sqrt2$ は同じ形へ厳密には戻らない。下段ではその違いが、2つの位相を座標にした空間で「閉じる軌道」と「閉じない軌道」として見える。*

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

ここで大事なのは、非周期性が「複雑さ」から生じたのではなく、**二つの完全に単純な周期運動が互いに整合しないこと**から生じた点である。

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

で、全ての周波数比が有理数で結びついていれば共通周期を作れる。

一方、$\omega_1,\ldots,\omega_D$ の間に

$$
\sum_{j=1}^{D}n_j\omega_j=0,
\qquad n_j\in\mathbb Z
$$

という非自明な整数関係がなければ、共通周期は作れない。このとき基本周波数は rationally independent であるという。

準周期性の出発点は、この**複数の独立周波数**である。

## 3. 1次元で複雑に見えるものを2次元で見る

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

$F$ はそれぞれの角度について $2\pi$ 周期なので、自然な空間は

$$
\mathbb T^2
=\mathbb R^2/(2\pi\mathbb Z)^2
$$

という2次元トーラスになる。

$x$ を増やすことは、このトーラス上で

$$
(\theta_1,\theta_2)
=(x,\sqrt2\,x)
$$

と進むことに対応する。

もし比が $1:2$ なら軌道は閉じる。ところが $1:\sqrt2$ では閉じない。何周しても完全には同じ位相対へ戻らず、長く進めるとトーラス全体を稠密に訪れる。

つまり、1次元で見えていた「戻ってこない複雑な波形」は、高次元では単純な直線運動である。

$$
\boxed{
\text{1D quasiperiodicity}
=\text{periodic geometry in higher dimension}
+\text{irrational direction}
}
$$

この見方が準結晶の高次元表示へ直接つながる。

## 4. なぜ「ほぼ同じ形」は何度も現れるのか

厳密な周期はないが、図を見ると似た形は繰り返し現れる。

これは $\sqrt2$ が有理数でよく近似できるからである。例えば

$$
\sqrt2\simeq\frac{99}{70}
$$

なら、ある長い距離を進んだとき二つの位相は同時にほぼ整数周だけ進む。

そのため

$$
f(x+T)\simeq f(x)
$$

となる大きな $T$ は何度も存在する。しかし等号にはならない。

ここが周期関数との決定的な違いである。

**同じ構造が厳密に反復するのではなく、任意の精度で再接近する。**

## 5. Fourier 空間では何が変わるか

高次元トーラス上の周期関数は通常の Fourier 級数を持つ。

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

周期関数なら独立な基本波数は1個で、全ての peak はその整数倍に並ぶ。準周期関数では1次元であっても、複数の独立な基本波数を必要とする。

この「空間次元より多い整数 index が必要」という構造が、後で準結晶の Fourier module として現れる。

## 6. 高次元へ行く意味

高次元表示は、非周期性を魔法のように消しているわけではない。

1次元では「いつ同じ形へ戻るか」という時間的・空間的な不整合として見えていたものを、2次元では**軌道の傾きが格子と整合しない**という幾何学へ置き換えている。

この変換が重要である。

$$
\text{nonperiodic repetition problem}
\quad\longrightarrow\quad
\text{irrational geometry problem}
$$

となるからである。

次の[Cut-and-project 法のノート](/notes/fibonacci-cut-and-project/)では、この考え方を連続関数ではなく点集合へ移す。そこで初めて、高次元の周期格子から1次元の Fibonacci chain がどう現れるかを見る。

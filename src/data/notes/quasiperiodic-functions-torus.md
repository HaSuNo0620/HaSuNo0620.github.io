---
title: "準周期関数とは何なのか — 複数周期の重ね合わせから高次元トーラスへ"
summary: "準周期性を『周期が複数ある関数』としてではなく、高次元トーラス上の周期構造を無理数方向に切ったものとして理解する。Fourier表示、可換でない周期、irrational flow、almost periodicityとの違いを整理する。"
publishedAt: 2026-09-12T02:46:00+09:00
area: "Mathematics"
topics: ["quasiperiodicity", "Fourier analysis", "torus", "dynamical systems", "quasicrystals"]
status: growing
---

[前のノート](/notes/quasicrystal-order-without-periodicity/)では、準結晶が捨てるのは秩序ではなく並進周期性だと整理した。次に疑問になるのは、**周期的ではないのに、どうやって無限遠まで規則性を保てるのか**という点である。

その最小の数学模型が準周期関数である。

準周期関数はしばしば「互いに無理数比の周期をもつ振動の重ね合わせ」と説明される。それ自体は正しいが、その説明だけではなぜ高次元空間が自然に現れるのかが見えにくい。

ここでは、準周期関数を**高次元トーラス上の周期関数を、無理数方向の直線に沿って観測したもの**として見る。

## 1. 二つの振動を足しただけで周期性は消える

まず

$$
f(x)=A_1\cos(k_1x+\phi_1)+A_2\cos(k_2x+\phi_2)
$$

を考える。

$f(x)$ が周期 $T>0$ を持つには、両方の位相が整数周だけ進めばよいので

$$
k_1T=2\pi m_1,
\qquad
k_2T=2\pi m_2,
\qquad
m_1,m_2\in\mathbb Z
$$

を同時に満たす必要がある。

したがって

$$
\frac{k_1}{k_2}=\frac{m_1}{m_2}\in\mathbb Q
$$

でなければならない。

逆に $k_1/k_2\notin\mathbb Q$ なら有限の $T$ は存在しない。つまり

$$
\boxed{
\frac{k_1}{k_2}\notin\mathbb Q
\quad\Longrightarrow\quad
f(x)\text{ は非周期}
}
$$

である。

しかし $f(x)$ はランダムではない。$A_i,k_i,\phi_i$ が決まれば全ての $x$ で値が決まる。ここに「非周期だが秩序だった」構造の最も簡単な例がある。

## 2. 「二つの周期を持つ」という言い方には注意がいる

$\cos k_1x$ の周期を $T_1=2\pi/k_1$、$\cos k_2x$ の周期を $T_2=2\pi/k_2$ と書ける。しかし $T_1/T_2$ が無理数なら、和 $f(x)$ 自体には周期がない。

したがって準周期関数を「複数の周期を持つ関数」と言うと少し危険である。より正確には、**複数の独立な基本周波数を持つが、それらに共通周期がない関数**と考える方がよい。

一般に

$$
f(x)=F(\omega_1x,\ldots,\omega_Dx)
$$

と書き、$F$ が各引数について $2\pi$ 周期だとする。

$\boldsymbol\omega=(\omega_1,\ldots,\omega_D)$ の成分間に非自明な整数関係

$$
\sum_{j=1}^{D}n_j\omega_j=0,
\qquad
n_j\in\mathbb Z
$$

が存在しないとき、これらを rationally independent と呼ぶ。このとき1変数関数 $f(x)$ は一般に周期を持たない。

## 3. 本当の周期性は高次元に残っている

$D=2$ の場合を考える。角変数

$$
\theta_1=k_1x+\phi_1,
\qquad
\theta_2=k_2x+\phi_2
$$

を導入すると、

$$
f(x)=F(\theta_1,\theta_2)
$$

であり、$F$ は

$$
F(\theta_1+2\pi,\theta_2)=F(\theta_1,\theta_2),
$$

$$
F(\theta_1,\theta_2+2\pi)=F(\theta_1,\theta_2)
$$

を満たす。

したがって $F$ の自然な定義域は

$$
\mathbb T^2
=\mathbb R^2/(2\pi\mathbb Z)^2
$$

という2次元トーラスである。

$x$ を増やすことは、トーラス上で

$$
\boldsymbol\theta(x)
=\boldsymbol\theta_0+x\mathbf k,
\qquad
\mathbf k=(k_1,k_2)
$$

という直線運動をすることに対応する。

ここで $k_1/k_2\in\mathbb Q$ なら軌道は閉じ、有限距離の後に元へ戻る。一方 $k_1/k_2\notin\mathbb Q$ なら軌道は閉じず、トーラス上を稠密に巡る。

つまり1次元で見えていた非周期性は、高次元では

$$
\boxed{
\text{periodic function on }\mathbb T^D
+\text{ irrational trajectory}
}
$$

へ分解できる。

これは準結晶の higher-dimensional description とほぼ同じ思想である。

## 4. Fourier 展開すると高rank構造が見える

$F$ はトーラス上の周期関数なので、通常の Fourier 級数を持つ。

$$
F(\boldsymbol\theta)
=\sum_{\mathbf n\in\mathbb Z^D}
F_{\mathbf n}e^{i\mathbf n\cdot\boldsymbol\theta}.
$$

$\boldsymbol\theta=\boldsymbol\theta_0+x\boldsymbol\omega$ を代入すると

$$
f(x)
=\sum_{\mathbf n\in\mathbb Z^D}
F_{\mathbf n}e^{i\mathbf n\cdot\boldsymbol\theta_0}
e^{i(\mathbf n\cdot\boldsymbol\omega)x}.
$$

したがって1次元で観測される波数は

$$
\boxed{
k_{\mathbf n}=\mathbf n\cdot\boldsymbol\omega
=\sum_{j=1}^{D}n_j\omega_j
}
$$

である。

周期関数なら独立な基本波数は1個で、$k_n=nk_0$ となる。準周期関数では独立な基本波数が $D>1$ 個あり、1次元空間に対して Fourier module の rank が高くなる。

この「物理空間の次元より Fourier 基底の rank が大きい」という構造は、準結晶回折でもそのまま現れる。

## 5. なぜ同じ模様が「ほぼ」戻ってくるのか

無理数比を持つ準周期関数には厳密な周期 $T$ はない。しかし、任意の精度で元の位相に近づく距離は存在する。

例えば $k_1/k_2=\alpha$ が無理数でも、有理数 $p/q$ によって

$$
\alpha\simeq\frac pq
$$

と近似できる。

すると $x$ を適切な大きさだけ進めたとき、二つの位相は同時にほぼ整数周進み、

$$
f(x+T)\simeq f(x)
$$

となる。

この「厳密な繰り返しはないが、任意の精度で近い繰り返しが現れる」という性質が、準周期構造の recurrent な見え方を作る。

黄金比

$$
\tau=\frac{1+\sqrt5}{2}
$$

の場合には Fibonacci 数 $F_n$ を使った近似

$$
\frac{F_{n+1}}{F_n}\to\tau
$$

が特に自然に現れる。これが Fibonacci chain と準周期性が結びつく理由の一つである。

## 6. 準周期性と almost periodicity は同じではない

準周期関数は almost periodic function の重要な部分集合である。

有限個の独立周波数だけで

$$
f(x)=F(\omega_1x,\ldots,\omega_Dx)
$$

と表せるものを通常 quasiperiodic と呼ぶ。一方、Bohr almost periodic function では Fourier 周波数の集合が有限rankである必要はない。

したがって包含関係としては概念的に

$$
\boxed{
\text{periodic}
\subset
\text{quasiperiodic}
\subset
\text{almost periodic}
}
$$

と見ることができる。

準結晶を学ぶときには「非周期なら全部準周期」という理解を避ける必要がある。ランダム配列も、一般的なaperiodic sequenceも非周期だが、必ずしも有限rankの高次元トーラス表示を持たない。

## 7. 準周期関数と準結晶は同じものではない

ここにも一段区別が必要である。

準周期関数は連続関数として

$$
f:\mathbb R^d\to\mathbb R
$$

を考える数学的概念である。一方、準結晶は原子位置の離散集合や密度場として記述される。

ただし両者には共通の構造がある。$d$ 次元の物理空間に対し、$D>d$ 個の独立波数を持つなら、密度を

$$
\rho(\mathbf r)
=\sum_{\mathbf n\in\mathbb Z^D}
\rho_{\mathbf n}
\exp\left[i\left(\sum_{j=1}^{D}n_j\mathbf b_j\right)\cdot\mathbf r\right]
$$

と書ける。

ここで $\mathbf b_j$ は $d$ 次元ベクトルだが、整数係数で生成するために $D$ 個必要である。

この higher-rank Fourier structure が、準周期関数から準結晶への橋になる。

## 8. 高次元表示は「数学的なごまかし」ではない

1次元の非周期関数をわざわざ2次元へ持ち上げると、問題を複雑にしただけに見えるかもしれない。しかし高次元表示には明確な利点がある。

1次元では「なぜこの波数が並ぶのか」を個別に追う必要がある。高次元では、それらは単に $\mathbb Z^D$ の整数格子点である。

つまり

$$
\text{complicated aperiodicity in }d\text{ dimensions}
$$

を

$$
\text{simple periodicity in }D>d\text{ dimensions}
$$

として組み替えている。

複雑さを消しているわけではなく、**非周期性を幾何学へ移している**。

この考え方を点集合へ適用したものが cut-and-project である。

## 9. 自分のための見取り図

準周期性については、次の対応を中心に置くと理解しやすい。

$$
\boxed{
\begin{aligned}
\text{1D quasiperiodic signal}
&\longleftrightarrow
\text{irrational orbit on }\mathbb T^D,\\
\text{independent frequencies}
&\longleftrightarrow
\text{axes of the higher-dimensional torus},\\
\text{Fourier module}
&\longleftrightarrow
\mathbb Z^D\text{ labels}.
\end{aligned}
}
$$

したがって準周期性の本質は、単に「違う周期を足した」ことではない。

**高次元では周期的に整理できる構造を、低次元の無理数方向から見ている**ことにある。

次の[cut-and-project のノート](/notes/fibonacci-cut-and-project/)では、この考え方を連続関数ではなく離散的な点集合へ移し、なぜ単純な高次元格子から Fibonacci chain のような非周期配列が生まれるのかを見る。

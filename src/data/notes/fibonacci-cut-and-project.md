---
title: "Cut-and-project 法 — Fibonacci列はなぜ高次元格子から生まれるのか"
summary: "2次元整数格子を無理数方向へ射影する発想から、Fibonacci chainを構成する。単なる射影では点が稠密になる理由と、acceptance windowが離散準周期構造を作る役割を図で理解する。"
publishedAt: 2026-09-12T02:47:00+09:00
updatedAt: 2026-09-13
area: "Mathematics"
topics: ["Fibonacci chain", "cut and project", "quasicrystals", "aperiodic order", "golden ratio"]
status: growing
---

[前のノート](/notes/quasiperiodic-functions-torus/)では、1次元の準周期関数を、2つの位相を持つ高次元の周期構造として見直した。

次に気になるのは、原子位置のような**離散的な点列**でも同じ見方が使えるのか、ということだ。

そこで出てくるのが cut-and-project 法である。

名前の通り、高次元の格子から一部の点を選び、それを低次元へ射影する。ただ、全部の格子点をそのまま射影すると上手くいかない。

![2次元格子からの cut-and-project](/figures/quasicrystals/cut-and-project.svg)

*2次元格子の中に斜めの帯を置き、その帯に入った格子点だけを選ぶ。選ばれた点を帯に平行な直線へ落とすと、離散的な非周期点列が得られる。*

## 1. まず作りたい Fibonacci chain を確認する

Fibonacci chain は、長い間隔 $L$ と短い間隔 $S$ に対して

$$
L\mapsto LS,
\qquad
S\mapsto L
$$

という置換を繰り返して作れる。

$$
L
\to LS
\to LSL
\to LSLLS
\to LSLLSLSL
\to\cdots
$$

有限周期はないが、$L$ と $S$ の個数比は黄金比

$$
\tau=\frac{1+\sqrt5}{2}
$$

へ近づく。

ここで黄金比が急に出てくるのは少し不思議なので、置換則そのものから確認しておく。

1回の置換で、$L$ は $LS$ を生み、$S$ は $L$ を生む。したがって $L,S$ の個数ベクトルは

$$
\begin{pmatrix}
N_L'\\
N_S'
\end{pmatrix}
=
\begin{pmatrix}
1&1\\
1&0
\end{pmatrix}
\begin{pmatrix}
N_L\\
N_S
\end{pmatrix}
$$

と更新される。

この行列

$$
M=
\begin{pmatrix}
1&1\\
1&0
\end{pmatrix}
$$

の固有値は

$$
\lambda_{\pm}
=\frac{1\pm\sqrt5}{2}
=\tau,\ -\frac1\tau
$$

である。

置換を何度も繰り返すと、絶対値の大きい固有値 $\tau$ の方向が支配的になる。対応する固有ベクトルから

$$
\frac{N_L}{N_S}\to\tau
$$

が出る。

つまり黄金比は、Fibonacci 列に後から付け足した数字ではなく、**置換規則の成長率そのもの**である。

規格化すると長い間隔と短い間隔の頻度は

$$
f_L=\frac1\tau,
\qquad
f_S=\frac1{\tau^2}
$$

となる。

この時点で、Fibonacci chain の内部にはすでに黄金比が組み込まれている。

置換則だけでも列は作れる。ただ、なぜこの列が高次元格子や回折とつながるのかはまだ見えにくい。

そこで同じ列を幾何学として作り直す。

## 2. 2次元格子に「見たい方向」を一本決める

2次元整数格子

$$
\mathbf n=(n_1,n_2)\in\mathbb Z^2
$$

を考える。

この平面内に、格子軸とは整合しない斜め方向を一本取る。最終的な1次元点列はこの方向に置く。

この方向を $E_{\parallel}$ と書く。Fibonacci chain では黄金比を使って、例えば

$$
\mathbf e_{\parallel}
=\frac{(1,\tau)}{\sqrt{1+\tau^2}}
$$

と選べる。

これに直交する方向を $E_{\perp}$ として

$$
\mathbf e_{\perp}
=\frac{(-\tau,1)}{\sqrt{1+\tau^2}}
$$

とする。

各格子点は、$E_{\parallel}$ に沿ってどこにいるかと、そこから垂直にどれだけ外れているかで表せる。

$$
x_{\parallel}=\mathbf n\cdot\mathbf e_{\parallel},
\qquad
x_{\perp}=\mathbf n\cdot\mathbf e_{\perp}
$$

最終的に原子位置として使うのは $x_{\parallel}$ の方なので、$E_{\parallel}$ を **physical space** と呼ぶ。

一方、$x_{\perp}$ は「その格子点を採用するかどうか」を判断するために使う。こちらが **internal space** である。

internal space は追加の物理空間というより、まずは「点を選別するための補助方向」と見ておけばよい。

## 3. 全部を射影すると失敗する

全ての整数格子点をそのまま $E_{\parallel}$ へ落とすと

$$
x_{\parallel}
=\frac{n_1+\tau n_2}{\sqrt{1+\tau^2}}
$$

となる。

$1$ と $\tau$ は有理数の比では結びつかない。そのため整数 $n_1,n_2$ を変えると、射影点はいくらでも近接できる。

数学的には射影点の集合が実軸上で **稠密** になる。どんなに小さな区間にも射影点が入ってしまう、という意味である。

これは欲しかった1次元原子列とは違う。

$$
\boxed{
\text{cut-and-project}\neq\text{project all lattice points}
}
$$

という点が、この方法の最初の肝になる。

## 4. window は「採用する点」を決める

そこで internal space 側で、採用してよい範囲を有限区間に制限する。この区間を **acceptance window**、単に window と呼ぶ。

条件は

$$
x_{\perp}\in W
$$

である。

つまり、2次元格子点のうち $E_{\parallel}$ に十分近いものだけを選び、その点だけを $E_{\parallel}$ へ射影する。

式でまとめると

$$
\boxed{
\Lambda=
\left\{
P_{\parallel}\mathbf n
\mid
\mathbf n\in\mathbb Z^2,
\ P_{\perp}\mathbf n\in W
\right\}
}
$$

となる。

この式だけ見ると少し硬いが、図では単に「斜めの帯に入った格子点だけ拾う」と読める。

window は補正項ではなく、**高次元格子のどの点を低次元へ残すかを決める規則そのもの**である。

## 5. なぜ長短二種類の間隔が出るのか

window に入った格子点を $E_{\parallel}$ に沿って順番に追う。

隣の採用点へ移るとき、2次元格子上では異なる基本ステップが現れる。それぞれを $E_{\parallel}$ へ射影した長さが、1次元側の長い間隔 $L$ と短い間隔 $S$ になる。

Fibonacci 構成に対応する方向と規格化を選ぶと

$$
\frac{L}{S}=\tau
$$

となる。

ここで $L,S$ の意味がかなり具体的になる。置換則の記号だったものが、**2次元格子の基本ステップを1次元へ射影した長さ**として見える。

しかも置換側でも、$L$ と $S$ の個数比に同じ $\tau$ が出ていた。

つまり黄金比は、

- 置換の成長率、
- $L,S$ の出現頻度、
- 射影方向の無理数傾き、
- 長短間隔の比、

を同時に結びつけている。

Fibonacci chain が単なる記号列ではなく、代数と幾何の両方で同じ数 $\tau$ に支配されていることが見えてくる。

## 6. 置換則と cut-and-project は同じ構造の別表現

置換則

$$
L\mapsto LS,
\qquad
S\mapsto L
$$

は、列をどう生成するかを見るのに向いている。

cut-and-project は、同じ列を高次元格子との関係として見るのに向いている。

$$
\boxed{
\begin{aligned}
\text{substitution}&:\ \text{列を作る規則},\\
\text{cut-and-project}&:\ \text{その規則の高次元幾何学}.
\end{aligned}
}
$$

どちらか一方が正しいというより、同じ Fibonacci 秩序を別の言葉で見ている。

置換則では自己相似性が見えやすく、cut-and-project では回折や高次元格子との関係が見えやすい。後で inflation や phason を考えるときにも、この二つの見方が行き来できると便利そうだ。

## 7. 高次元空間は本当に存在するのか

ここで少し引っかかるのが、$E_{\perp}$ を本当に物理的な追加空間として考えるのか、という点である。

この構成では、通常そう解釈する必要はない。$E_{\perp}$ は、低次元で非周期に見える配置を高次元の周期格子として整理するための補助座標である。

ただし、単なる記号遊びでもない。同じ高次元格子は、波数側の構造まで整理してくれる。

今のところは、

$$
\boxed{
\text{Fibonacci chain}
=\text{2D periodic lattice}
+\text{irrational orientation}
+\text{finite window}
}
$$

という像で捉えておけばよさそうだ。

[次のノート](/notes/quasicrystal-diffraction-fourier-module/)では、高次元側の reciprocal lattice を射影すると、準結晶の Bragg peak がどう整理されるかを見る。

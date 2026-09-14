---
title: "Cut-and-project 法 — Fibonacci列はなぜ高次元格子から生まれるのか"
summary: "2次元整数格子を無理数方向へ射影する発想から、Fibonacci chainを構成する。単なる射影では点が稠密になる理由と、acceptance windowが離散準周期構造を作る役割を図で理解する。"
publishedAt: 2026-09-12T02:47:00+09:00
updatedAt: 2026-09-14
area: "Mathematics"
topics: ["Fibonacci chain", "cut and project", "quasicrystals", "aperiodic order", "golden ratio"]
status: growing
---

[前のノート](/notes/quasiperiodic-functions-torus/)では、1次元の準周期関数を、複数の位相を持つ高次元の周期構造として見直した。

原子位置のような**離散点列**でも同じ見方ができるのか。Fibonacci chain は、その問いに対する最小の例になっている。

cut-and-project 法では、高次元格子から一部の点だけを選び、それを低次元へ射影する。全部の格子点を射影するだけでは点列にならない。この「選別」が本体である。

![2次元格子からの cut-and-project](/figures/quasicrystals/cut-and-project.svg)

*2次元格子の中に斜めの帯を置き、その帯に入った格子点だけを選ぶ。選ばれた点を帯に平行な直線へ落とすと、離散的な非周期点列が得られる。*

## 1. Fibonacci chain の代数的な基準形

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

黄金比は置換則そのものから出る。1回の置換で $L$ は $LS$ を生み、$S$ は $L$ を生むので、個数ベクトルは

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

置換行列

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

置換を繰り返すと、絶対値の大きい固有値 $\tau$ に対応する方向が支配的になり、

$$
\frac{N_L}{N_S}\to\tau
$$

が出る。

規格化すれば出現頻度は

$$
f_L=\frac1\tau,
\qquad
f_S=\frac1{\tau^2}
$$

となる。

黄金比は後から付けた数字ではなく、**置換規則の成長率そのもの**として入っている。ただ、置換則だけでは高次元格子との接続は見えにくい。

## 2. 2次元格子に physical space を埋め込む

2次元整数格子

$$
\mathbf n=(n_1,n_2)\in\mathbb Z^2
$$

を考える。

この平面内に、格子軸とは整合しない斜め方向を一本取り、最終的な1次元点列をこの方向に置く。この方向を $E_{\parallel}$ と書く。

Fibonacci chain では黄金比を使って、例えば

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

各格子点は

$$
x_{\parallel}=\mathbf n\cdot\mathbf e_{\parallel},
\qquad
x_{\perp}=\mathbf n\cdot\mathbf e_{\perp}
$$

で表せる。

最終的な点位置として使う $x_{\parallel}$ 側が **physical space**、点を採用するかどうかの判定に使う $x_{\perp}$ 側が **internal space** である。

internal space は追加の物理空間というより、点を選別するための補助方向と見るのが近い。

## 3. 全射影が稠密集合を作ってしまう

全ての整数格子点をそのまま $E_{\parallel}$ へ落とすと

$$
x_{\parallel}
=\frac{n_1+\tau n_2}{\sqrt{1+\tau^2}}
$$

となる。

$1$ と $\tau$ は有理数の比では結びつかない。そのため整数 $n_1,n_2$ を変えると、射影点はいくらでも近接できる。

数学的には射影点の集合が実軸上で **稠密** になる。どんなに小さな区間にも射影点が入ってしまい、欲しかった離散原子列にはならない。

$$
\boxed{
\text{cut-and-project}\neq\text{project all lattice points}
}
$$

という区別がここで効いてくる。

## 4. acceptance window が点列を離散化する

internal space 側で、採用してよい範囲を有限区間に制限する。この区間が **acceptance window** である。

条件は

$$
x_{\perp}\in W
$$

となる。

2次元格子点のうち $E_{\parallel}$ に十分近いものだけを選び、その点だけを射影する。式では

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

図では「斜めの帯に入った格子点だけ拾う」に相当する。window は補正項ではなく、**高次元格子のどの点を低次元へ残すかを決める規則そのもの**である。

## 5. 長短二種類の間隔は射影された格子ステップである

window に入った格子点を $E_{\parallel}$ に沿って順番に追う。

隣の採用点へ移るとき、2次元格子上では異なる基本ステップが現れる。それぞれを $E_{\parallel}$ へ射影した長さが、1次元側の長い間隔 $L$ と短い間隔 $S$ になる。

Fibonacci 構成に対応する方向と規格化を選ぶと

$$
\frac{L}{S}=\tau
$$

となる。

置換則の記号だった $L,S$ が、**2次元格子の基本ステップを1次元へ射影した長さ**として読める。

置換側では $L,S$ の個数比に、射影側では長さの比と無理数傾きに、同じ $\tau$ が現れる。代数と幾何が同じ黄金比で結ばれている。

## 6. substitution と cut-and-project は生成則と幾何の対応になる

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

どちらか一方が本質というより、同じ Fibonacci 秩序の別表現になっている。

## 7. いま置いている像

$E_{\perp}$ を実在する追加空間として考える必要はない。低次元で非周期に見える配置を、高次元の周期格子として整理するための補助座標である。

ただし単なる記号遊びでもなく、同じ高次元格子は波数側の構造まで整理してくれる。

今のところは

$$
\boxed{
\text{Fibonacci chain}
=\text{2D periodic lattice}
+\text{irrational orientation}
+\text{finite window}
}
$$

という像で捉えている。

この高次元格子を reciprocal space 側へ移すと、準結晶の Bragg peak と Fourier module へつながる。

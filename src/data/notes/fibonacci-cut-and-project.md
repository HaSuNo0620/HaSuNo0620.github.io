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

では、原子位置のような**離散的な点列**でも同じことができるのだろうか。

ここで出てくるのが cut-and-project 法である。

名前の通り、高次元の格子から一部の点を選び、それを低次元へ射影する。ただし重要なのは、**全部の格子点を射影してはいけない**ことである。

![2次元格子からの cut-and-project](/figures/quasicrystals/cut-and-project.svg)

*2次元格子の中に斜めの帯を置き、その帯に入った格子点だけを選ぶ。選ばれた点を帯に平行な直線へ落とすと、離散的な非周期点列が得られる。*

## 1. まず、作りたい Fibonacci chain を確認する

前のノートまでにも出てきた Fibonacci chain は、長い間隔 $L$ と短い間隔 $S$ に対して

$$
L\mapsto LS,
\qquad
S\mapsto L
$$

という置換を繰り返して作れる。

すると

$$
L
\to LS
\to LSL
\to LSLLS
\to LSLLSLSL
\to\cdots
$$

という列が得られる。

この列には有限周期がない。一方、$L$ と $S$ の個数比は黄金比

$$
\tau=\frac{1+\sqrt5}{2}
$$

へ近づく。

置換則で「どう生成するか」は分かる。しかし、なぜこの列が高次元格子や回折とつながるのかはまだ見えない。

そこで同じ列を幾何学的に作り直す。

## 2. 2次元格子に「見たい方向」を一本決める

2次元整数格子

$$
\mathbf n=(n_1,n_2)\in\mathbb Z^2
$$

を考える。

この平面内に、格子軸とは整合しない斜め方向を一本取る。これを、最終的に1次元の点列を置く方向として使う。

この方向を $E_{\parallel}$ と書く。Fibonacci chain では黄金比を使って、例えば

$$
\mathbf e_{\parallel}
=\frac{(1,\tau)}{\sqrt{1+\tau^2}}
$$

と選べる。

$E_{\parallel}$ に直交する方向も同時に用意し、これを $E_{\perp}$ と書く。

$$
\mathbf e_{\perp}
=\frac{(-\tau,1)}{\sqrt{1+\tau^2}}
$$

各格子点は、「$E_{\parallel}$ に沿ってどこにいるか」と「そこから垂直方向へどれだけ外れているか」の二つで表せる。

$$
x_{\parallel}=\mathbf n\cdot\mathbf e_{\parallel},
\qquad
x_{\perp}=\mathbf n\cdot\mathbf e_{\perp}
$$

最終的に原子位置として使うのは $x_{\parallel}$ の方である。そのため $E_{\parallel}$ を **physical space** と呼ぶ。

一方、$x_{\perp}$ は「どの格子点を採用するか」を判定するために使う補助座標である。この補助方向を **internal space** と呼ぶ。

ここで internal space は追加の物理空間ではない。まずは「点を選別するための横方向」と理解すればよい。

## 3. 全部を射影すると失敗する

全ての整数格子点をそのまま $E_{\parallel}$ へ落とすと

$$
x_{\parallel}
=\frac{n_1+\tau n_2}{\sqrt{1+\tau^2}}
$$

となる。

$1$ と $\tau$ は有理数の比では結びつかない。そのため整数 $n_1,n_2$ を変えると、射影点はいくらでも近接できる。

数学的には、射影点の集合が実軸上で **稠密** になるという。これは、どんな小さな区間を取っても射影点が入る、という意味である。

つまり全部を射影すると、原子が離散的に並ぶ1次元構造にはならない。

$$
\boxed{
\text{cut-and-project}\neq\text{project all lattice points}
}
$$

である。

## 4. window は「採用する点」を決める

そこで internal space 側で、採用してよい範囲を有限区間に制限する。この有限区間を **acceptance window**、単に window と呼ぶ。

条件は

$$
x_{\perp}\in W
$$

である。

つまり、2次元格子点のうち $E_{\parallel}$ に十分近いものだけを選び、その選ばれた点だけを $E_{\parallel}$ へ射影する。

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

図では window は、$E_{\parallel}$ に平行な有限幅の帯として見える。

window は細かな補正ではない。**高次元格子のどの点を物理空間へ採用するかを決める規則そのもの**である。

## 5. なぜ長短二種類の間隔が出るのか

window に入った格子点を $E_{\parallel}$ に沿って順番に追う。

隣の採用点へ移るとき、2次元格子上では異なる基本ステップが現れる。それぞれを $E_{\parallel}$ へ射影した長さが、1次元側の長い間隔 $L$ と短い間隔 $S$ になる。

Fibonacci 構成に対応する方向と規格化を選ぶと、その比は

$$
\frac{L}{S}=\tau
$$

となる。

ここで $L,S$ は、置換則のために便宜的に付けた二文字ではなくなる。

**2次元格子の基本ステップが、1次元へ射影された長さ**として現れている。

## 6. 置換則と cut-and-project は同じ構造の別表現

置換則

$$
L\mapsto LS,
\qquad
S\mapsto L
$$

は、列をどう生成するかを見るのに強い。

cut-and-project は、同じ列を高次元格子との関係として見るのに強い。

$$
\boxed{
\begin{aligned}
\text{substitution}&:\ \text{列を作る規則},\\
\text{cut-and-project}&:\ \text{その規則の高次元幾何学}.
\end{aligned}
}
$$

同じ Fibonacci 秩序を別の言葉で見ている。

## 7. 高次元空間は本当に存在するのか

ここで「原子が本当に $E_{\perp}$ の方向にも動いているのか」という疑問が出る。

この構成での $E_{\perp}$ は、通常は実在する追加の空間として解釈する必要はない。低次元で非周期に見える配置を、周期的な整数格子として整理するための補助座標である。

ただし単なる記号遊びでもない。

同じ高次元格子には、波数側にも普通の周期格子がある。次のノートでは、その波数側の格子を同じように射影すると、準結晶の Bragg peak の位置が整理できることを見る。

[次のノート](/notes/quasicrystal-diffraction-fourier-module/)では、そこで初めて reciprocal lattice と Fourier module を導入する。

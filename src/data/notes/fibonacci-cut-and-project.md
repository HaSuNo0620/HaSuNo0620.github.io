---
title: "Cut-and-project 法 — Fibonacci列はなぜ高次元格子から生まれるのか"
summary: "2次元整数格子を無理数方向へ射影する発想から、Fibonacci chainを構成する。単なる射影では点が稠密になる理由と、acceptance windowが離散準周期構造を作る役割を図で理解する。"
publishedAt: 2026-09-12T02:47:00+09:00
updatedAt: 2026-09-13
area: "Mathematics"
topics: ["Fibonacci chain", "cut and project", "quasicrystals", "aperiodic order", "golden ratio"]
status: growing
---

[前のノート](/notes/quasiperiodic-functions-torus/)では、1次元の準周期関数が高次元では単純な周期構造として見えることを確認した。

では、原子位置のような**離散的な点列**でも同じことができるのだろうか。

ここで出てくるのが cut-and-project 法である。

名前だけを見ると「高次元格子を斜めに射影すればよい」ように思える。しかし、実はそれでは失敗する。**全格子点を射影すると点が稠密になってしまう**からである。

この失敗をどう直すかが、cut-and-project の中身そのものである。

![2次元格子からの cut-and-project](/figures/quasicrystals/cut-and-project.svg)

*無理数方向 $E_{\parallel}$ に平行な有限幅の strip を置き、その中に入った格子点だけを選ぶ。選ばれた点を $E_{\parallel}$ へ落とすと、離散的な準周期点列が得られる。*

## 1. まず Fibonacci chain を知っている形で書く

長い間隔 $L$ と短い間隔 $S$ に対して

$$
L\mapsto LS,
\qquad
S\mapsto L
$$

という置換を繰り返す。

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

この列には有限周期がない。一方、$L$ と $S$ の個数比は

$$
\frac{N_L}{N_S}\to\tau,
\qquad
\tau=\frac{1+\sqrt5}{2}
$$

へ近づく。

置換則で作ると「なぜこの列になるか」は分かるが、なぜ高次元格子や回折とつながるのかは見えにくい。

そこで同じ列を幾何学的に作り直す。

## 2. 2次元整数格子を斜めから見る

2次元整数格子

$$
\mathbf n=(n_1,n_2)\in\mathbb Z^2
$$

を考える。

この平面内に、格子軸とは無理数の傾きを持つ1次元方向 $E_{\parallel}$ を取る。Fibonacci chain では黄金比 $\tau$ を使って、例えば

$$
\mathbf e_{\parallel}
=\frac{(1,\tau)}{\sqrt{1+\tau^2}}
$$

と選べる。

これに直交する方向を $E_{\perp}$ とし、

$$
\mathbf e_{\perp}
=\frac{(-\tau,1)}{\sqrt{1+\tau^2}}
$$

とする。

格子点 $\mathbf n$ は

$$
x_{\parallel}=\mathbf n\cdot\mathbf e_{\parallel},
\qquad
x_{\perp}=\mathbf n\cdot\mathbf e_{\perp}
$$

という二つの座標で見られる。

ここで $E_{\parallel}$ が物理空間、$E_{\perp}$ が internal space である。

## 3. 全部を射影すると失敗する

全ての整数格子点をそのまま $E_{\parallel}$ へ落とすと

$$
x_{\parallel}
=\frac{n_1+\tau n_2}{\sqrt{1+\tau^2}}
$$

となる。

$1$ と $\tau$ は有理数上で独立なので、

$$
\{n_1+\tau n_2\mid n_1,n_2\in\mathbb Z\}
$$

は実軸上で稠密になる。

つまり、いくらでも近い二点を作れてしまう。

これは「非周期な結晶」を作ったのではなく、1次元直線をほとんど埋め尽くす射影集合を作っただけである。

したがって重要なのは

$$
\boxed{
\text{cut-and-project}\neq\text{project all points}
}
$$

である。

## 4. window が必要になる

そこで internal space 側に有限区間 $W$ を置く。

そして

$$
x_{\perp}\in W
$$

を満たす格子点だけを採用する。

最後に、その採用点だけを $E_{\parallel}$ へ射影する。

これを式でまとめると

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

図では $W$ は $E_{\parallel}$ に平行な strip の幅として見える。

ここで初めて、射影後の点列は離散的になる。

window は細かな補正ではない。**高次元格子から、どの点を物理空間へ採用するかを決める本体**である。

## 5. なぜ長短二種類の間隔が出るのか

strip 内の格子点を $E_{\parallel}$ に沿って順番に追う。

隣の採用点へ移るとき、高次元格子では基本的に異なる格子ステップが使われる。それぞれを $E_{\parallel}$ へ射影した長さが、1次元側の長い間隔 $L$ と短い間隔 $S$ になる。

適切な規格化をすると

$$
\frac{L}{S}=\tau
$$

となる。

ここで Fibonacci chain の $L,S$ は、置換則のために人工的に導入した二文字ではなくなる。

**高次元格子の異なる基本ステップが、低次元へ射影された長さ**として現れている。

これが cut-and-project の一番腑に落ちるところだと思う。

## 6. 置換則と射影法は何が違うのか

置換則

$$
L\mapsto LS,
\qquad
S\mapsto L
$$

は、列をどう生成するかを見るのに強い。

cut-and-project は、同じ秩序を高次元格子との関係として見るのに強い。

したがって両者は競合する説明ではない。

$$
\boxed{
\begin{aligned}
\text{substitution}&:\ \text{symbolic generation},\\
\text{cut-and-project}&:\ \text{geometric organization}.
\end{aligned}
}
$$

同じ Fibonacci 秩序を別の座標系で見ている。

## 7. 高次元空間は本当に存在するのか

この段階で「原子が本当に2次元目へ動いているのか」という疑問が出る。

ここでの $E_{\perp}$ は、通常は物理的な追加空間として解釈する必要はない。低次元で非周期に見える配置を、周期的な整数格子として整理するための embedding space である。

ただし単なる記号上の遊びでもない。

同じ高次元格子から、次は reciprocal lattice を射影できる。すると準結晶の Bragg peak の位置まで同じ整数 index で整理できる。

つまり cut-and-project の価値は、Fibonacci列を一度作れることではなく、**実空間と逆空間を同じ高次元幾何学で結べること**にある。

それを[次のノート](/notes/quasicrystal-diffraction-fourier-module/)で見る。

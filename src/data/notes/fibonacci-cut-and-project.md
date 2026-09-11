---
title: "Fibonacci列から cut-and-project へ — なぜ高次元格子から準周期構造が生まれるのか"
summary: "Fibonacci chainを置換則と高次元射影の両方から見る。全格子点を射影すると密になる理由、acceptance windowが必要な理由、黄金比とphasonの幾何学的意味を整理する。"
publishedAt: 2026-09-12T02:47:00+09:00
area: "Mathematics"
topics: ["Fibonacci chain", "cut and project", "quasicrystals", "aperiodic order", "golden ratio"]
status: growing
---

[前のノート](/notes/quasiperiodic-functions-torus/)では、準周期関数を高次元トーラス上の周期関数の無理数方向の観測として見た。連続関数ではこの見方が自然だったが、準結晶では原子位置のような**離散的な点集合**を作らなければならない。

そこで現れるのが cut-and-project である。

この構成を初めて見ると、「高次元格子を斜めに射影するだけなら点が密になってしまうのではないか」「なぜ window が必要なのか」という疑問が生じる。この二つを区別すると、cut-and-project の仕組みがかなり明瞭になる。

## 1. Fibonacci chainをまず置換則として作る

二種類の間隔 $L$ と $S$ を考え、置換則

$$
L\mapsto LS,
\qquad
S\mapsto L
$$

を繰り返す。

$L$ から始めると

$$
L
\to LS
\to LSL
\to LSLLS
\to LSLLSLSL
\to\cdots
$$

となる。

各段階で $L$ と $S$ の個数は Fibonacci 数で増え、その比は

$$
\frac{N_L}{N_S}\to\tau,
\qquad
\tau=\frac{1+\sqrt5}{2}
$$

へ近づく。

この列には有限周期がない。しかし局所配列は任意ではなく、置換則が全体を拘束している。

ここではすでに「非周期だが秩序だった」構造ができている。cut-and-project は、この同じ構造を**高次元格子の幾何学として再表現する**。

## 2. 2次元格子を二つの方向へ分解する

整数格子

$$
\mathbf n=(n_1,n_2)\in\mathbb Z^2
$$

を考える。

2次元空間を、1次元の physical space $E_{\parallel}$ と、それに直交する internal space $E_{\perp}$ に分ける。

Fibonacci chain では黄金比を含む方向を選ぶと都合がよい。例えば単位ベクトルを

$$
\mathbf e_{\parallel}
=\frac{(1,\tau)}{\sqrt{1+\tau^2}},
\qquad
\mathbf e_{\perp}
=\frac{(-\tau,1)}{\sqrt{1+\tau^2}}
$$

と取る。

格子点 $\mathbf n$ の平行成分と垂直成分は

$$
x_{\parallel}=\mathbf n\cdot\mathbf e_{\parallel},
\qquad
x_{\perp}=\mathbf n\cdot\mathbf e_{\perp}
$$

である。

ここで $E_{\parallel}$ の傾きは格子軸に対して無理数なので、格子の周期方向と整合しない。

## 3. 全格子点を射影してはいけない

最初に思いつくのは、全ての $\mathbf n\in\mathbb Z^2$ を $E_{\parallel}$ へ射影することである。

すると

$$
x_{\parallel}
=\frac{n_1+\tau n_2}{\sqrt{1+\tau^2}}
$$

となる。

$1$ と $\tau$ は有理数上で独立なので、集合

$$
\{n_1+\tau n_2\mid n_1,n_2\in\mathbb Z\}
$$

は実軸上で稠密になる。つまり、任意に近い二点を持つことができる。

これは原子位置としては使えない。準結晶は非周期であっても、原子間距離が任意に小さくなるわけではないからである。

したがって cut-and-project は単なる projection ではない。

## 4. acceptance window が離散性を回復する

そこで internal space 側に有限区間 $W$ を用意し、

$$
x_{\perp}\in W
$$

を満たす格子点だけを採用する。

得られる点集合は

$$
\boxed{
\Lambda
=
\left\{
P_{\parallel}\mathbf n
\mid
\mathbf n\in\mathbb Z^2,
\quad
P_{\perp}\mathbf n\in W
\right\}
}
$$

である。

幾何学的には、$E_{\parallel}$ に平行な有限幅の帯を2次元格子へ重ね、その帯の内部に入った格子点だけを $E_{\parallel}$ へ落としている。

これが cut-and-project の本体である。

window $W$ は余計な技術ではなく、

$$
\boxed{
\text{higher-dimensional lattice}
+\text{ irrational orientation}
+\text{ finite window}
}
$$

の三つを揃えて、初めて低次元の離散準周期集合を作る。

## 5. なぜ二種類の間隔だけが現れるのか

帯の中に入った格子点を $E_{\parallel}$ に沿って順番にたどると、次の採用格子点へ移る方法は主に二種類になる。

2次元格子上では、例えば

$$
(n_1,n_2)\to(n_1+1,n_2)
$$

または

$$
(n_1,n_2)\to(n_1,n_2+1)
$$

というステップが対応し、それぞれの $E_{\parallel}$ への射影長が二種類の bond length になる。

その長さを $S$ と $L$ と書けば、比は規格化の取り方を除いて黄金比

$$
\frac{L}{S}=\tau
$$

になるように取れる。

つまり Fibonacci chain の長短二種類の間隔は、置換則から突然導入された記号ではない。2次元格子の基本ステップを無理数方向へ射影した長さとして理解できる。

## 6. 置換則と射影構成は同じ秩序を別の言葉で見ている

置換則では

$$
L\mapsto LS,
\qquad
S\mapsto L
$$

という combinatorial rule を使った。

cut-and-project では同じ配列が格子点と window の幾何学から現れる。

前者は「列をどう生成するか」をよく見せ、後者は「なぜ Fourier 構造が高次元格子と結びつくか」をよく見せる。

これは二つの独立な模型というより、同じ準周期秩序の

- symbolic description、
- geometric description、

である。

## 7. 黄金比は装飾ではなく irrational orientation を固定する

Fibonacci chain で黄金比が何度も出てくるのは偶然ではない。

$\tau$ は

$$
\tau^2=\tau+1
$$

を満たし、連分数展開が

$$
\tau=[1;1,1,1,\ldots]
$$

となる。

その最良有理近似は Fibonacci 数の比

$$
\frac{F_{n+1}}{F_n}
$$

で与えられる。

したがって、

- substitution の成長率、
- 長短タイルの個数比、
- irrational slope の有理近似、
- periodic approximant の周期、

が同じ Fibonacci 構造へ集約される。

黄金比は単に「5回対称性だから現れる数字」ではなく、**準周期方向を最も基本的な二次無理数で固定した結果**として現れる。

## 8. periodic approximant は何をしているのか

無理数 $\tau$ を有理数

$$
\tau\simeq\frac{F_{n+1}}{F_n}
$$

で置き換えると、physical space の傾きが格子に対して rational になる。

すると射影方向は高次元格子と有限距離で整合し、低次元構造にも大きな単位胞が現れる。

これが periodic approximant である。

したがって approximant は準結晶を「雑に周期化したもの」ではなく、irrational slope を rational slope へ近似した構造と理解できる。近似次数を上げると単位胞は大きくなり、局所構造は準結晶へ近づく。

## 9. window を動かすと何が変わるのか

physical space の向きを固定したまま window $W$ を internal space 内で少し平行移動することを考える。

多くの格子点では採用・不採用は変わらない。しかし window の境界を横切る格子点では、低次元側の点の選択が切り替わる。

この変化は通常の一様並進とは異なる。physical space に直交する internal degree of freedom に沿った変位だからである。

準結晶ではこの自由度が phason と結びつく。

通常の phonon が physical-space displacement に対応するのに対し、phason は higher-dimensional description では perpendicular-space displacement として自然に現れる。

この見方をすると phason は「準結晶特有の謎の欠陥」ではなく、$D>d$ の記述を持つことから生じる追加自由度として理解できる。

## 10. 高次元格子は実在する空間なのか

cut-and-project を学ぶと、高次元空間を物理的に実在する追加次元として受け取ってよいのかが気になる。

通常、そのように解釈する必要はない。

高次元格子は、低次元で複雑に見える準周期構造を周期構造として整理するための embedding space である。physical space の原子が実際に perpendicular direction へ移動しているという意味ではない。

ただし単なる記号操作でもない。回折 peak の index、phason 自由度、window による振幅選択などがこの幾何学で統一されるため、非常に強い構造的意味を持つ。

## 11. 自分のための見取り図

Fibonacci chain を理解するときには、次の三つを分けておくと混乱しにくい。

$$
\boxed{
\begin{aligned}
\text{substitution}
&:\ \text{配列を生成する規則},\\
\text{cut-and-project}
&:\ \text{同じ配列の高次元幾何学},\\
\text{window}
&:\ \text{射影集合を離散化する選択規則}.
\end{aligned}
}
$$

特に重要なのは、**projection だけでは準結晶にならない**ことである。全格子点の射影は稠密になり、有限 window による選別があって初めて Delone-like な離散点集合が得られる。

そしてこの構成の最も強いところは、実空間構造だけで終わらないことにある。高次元格子の reciprocal lattice を同じように射影すると、準結晶の Bragg peak の位置が自然に生成される。

それを[次の回折のノート](/notes/quasicrystal-diffraction-fourier-module/)で見る。

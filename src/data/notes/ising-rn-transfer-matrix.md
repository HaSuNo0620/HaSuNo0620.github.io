---
title: "1次元イジング模型 R=N — 相互作用範囲・高次壁相互作用・有限記憶"
summary: "有限範囲 R=N の1次元Ising鎖を一般化し、ドメイン壁表示では N 体までの局所相互作用、壁列では N-1 ステップの有限記憶が現れることを整理する。R=3 を最初の具体例として読む。"
publishedAt: 2026-09-11T19:30:00+09:00
updatedAt: 2026-09-11T19:45:00+09:00
area: "Physics"
topics: ["statistical mechanics", "Ising model", "transfer matrix", "domain wall", "finite memory", "correlation"]
status: growing
---

R=1 ではドメイン壁は独立、R=2 では壁同士が相互作用し、相関を担う転送固有値が複素化できるところまで見た。次に問うべきなのは、相互作用範囲をさらに伸ばしたとき何が一般に起こるかである。

有限範囲 $R=N$ の1次元 Ising 鎖を

$$
\boxed{
H=-\sum_{n=1}^{N}J_n\sum_i s_i s_{i+n},
\qquad s_i=\pm1
}
$$

とする。このノートの中心は、単に transfer matrix が大きくなることではない。相互作用範囲 $N$ は、ドメイン壁表示では**高次の局所相互作用**へ、壁列の条件付き統計では**有限長の記憶**へ変換される。

![相互作用範囲と壁相互作用・記憶長の対応](/figures/ising-rn/range-memory-map.svg)

*スピン相互作用の到達距離を1格子ずつ伸ばすたびに、壁表示では1段高い多体項が現れ、次の壁の局所確率を決めるために必要な履歴も1ステップずつ伸びる。*

## 1. 一般の $R=N$ を壁変数で書く

いつものように

$$
\tau_i\equiv s_i s_{i+1}
$$

を導入する。すると距離 $n$ のスピン積は望遠鏡積になり、

$$
\boxed{
s_i s_{i+n}
=\prod_{m=0}^{n-1}\tau_{i+m}
}
$$

である。したがって Hamiltonian は

$$
\boxed{
H
=-\sum_{n=1}^{N}J_n
\sum_i
\prod_{m=0}^{n-1}\tau_{i+m}
}
$$

と書ける。

この式が一般化の核心である。$n$ 次近接のスピン相互作用は、壁変数では連続する $n$ 個の $\tau$ の積になる。すなわち

$$
\boxed{
\text{spin interaction range }N
\Longleftrightarrow
\text{wall variables の最大 }N\text{体相互作用}
}
$$

である。

最初の3段階を書くと

$$
R=1:\quad
H=-J_1\sum_i\tau_i,
$$

$$
R=2:\quad
H=-J_1\sum_i\tau_i
-J_2\sum_i\tau_i\tau_{i+1},
$$

$$
R=3:\quad
H=-J_1\sum_i\tau_i
-J_2\sum_i\tau_i\tau_{i+1}
-J_3\sum_i\tau_i\tau_{i+1}\tau_{i+2}.
$$

R=3 で初めて、壁2個の関係だけでは表せない3体項が現れる。

## 2. transfer state と壁列の記憶は別の数え方をする

新しいスピン $c=s_{i+1}$ を付け加えるとき、距離 $N$ の結合 $s_{i-N+1}c$ まで局所 Boltzmann 重みを決めるには、**直前の $N$ 個のスピン**を覚えておく必要がある。したがって transfer state は

$$
\sigma_i=(s_{i-N+1},\ldots,s_i)
$$

という長さ $N$ のビット列として取れる。

状態数は

$$
\boxed{2^N}
$$

である。実際、$R=1$ なら2状態、$R=2$ なら4状態、$R=3$ なら8状態になる。遷移は窓を1サイトずらす

$$
(a_1,a_2,\ldots,a_N)
\longrightarrow
(a_2,\ldots,a_N,c)
$$

という de Bruijn 型の局所遷移である。

一方、壁変数では Hamiltonian が最大 $N$ 個連続した $\tau$ の積まで含むので、次の壁の条件付き確率には最大で直前 $N-1$ 個の壁が必要になる。この意味で

$$
R=1:\ 0\text{ step memory},
\qquad
R=2:\ 1\text{ step memory},
\qquad
R=3:\ 2\text{ step memory},
$$

そして一般に

$$
\boxed{R=N\ \Rightarrow\ \text{壁列は最大 }(N-1)\text{ step memory}}
$$

と読める。

したがって

$$
\boxed{
\text{spin transfer state}:2^N\text{ 状態}
\qquad\text{と}\qquad
\text{wall process}:N-1\text{ step memory}
}
$$

は同じ有限範囲相互作用を別の変数で表したものであり、数え方を混同しないことが重要である。

ここでいう「記憶」は、時間発展の非平衡 memory ではなく、鎖に沿って次の局所確率を決めるために必要な条件付き履歴である。

## 3. $R=3$：最初の具体例

R=3 では

$$
H=-J_1\sum_i s_is_{i+1}
-J_2\sum_i s_is_{i+2}
-J_3\sum_i s_is_{i+3}
$$

であり、

$$
s_i s_{i+3}
=\tau_i\tau_{i+1}\tau_{i+2}
$$

だから

$$
\boxed{
H=-J_1\sum_i\tau_i
-J_2\sum_i\tau_i\tau_{i+1}
-J_3\sum_i\tau_i\tau_{i+1}\tau_{i+2}
}
$$

となる。

![R=3 で初めて現れる3体壁相互作用](/figures/ising-rn/r3-wall-interaction.svg)

*$J_3$ は単独の壁や隣接壁ペアではなく、3つ並んだ壁変数の符号パターンに直接エネルギーを与える。*

確率過程として見れば、一般には

$$
P(\tau_{i+2}\mid\tau_{i+1},\tau_i)
\neq
P(\tau_{i+2}\mid\tau_{i+1})
$$

となる。R=2 の1ステップ記憶から、R=3 では2ステップ記憶へ進む。

## 4. 相関スペクトルでは何が増えるか

R=2 では、スピン相関を担う odd sector は実質 $2\times2$ であり、支配モードは2本の実固有値か1組の複素共役対だった。そのため漸近相関の本質的な振動波数は1つである。

R=3 では transfer matrix は $8\times8$ となり、スピン反転対称性を使っても各 sector はより大きい。したがって odd sector に複数の subleading mode が存在でき、長距離相関は一般に

$$
C(r)
\sim
\sum_a A_a\rho_a^r\cos(q_a r+\phi_a)
$$

の形を取りうる。

ここで重要なのは、有限距離で項が複数見えること自体ではなく、**どの固有モードが最大絶対値を持つかがパラメータとともに切り替わりうる**ことである。たとえば

$$
|\lambda_a|=|\lambda_b|
$$

を跨いで

$$
q_a\longrightarrow q_b
$$

と支配波数が変われば、これは R=2 の「実モード $\to$ 複素モード」とは別種の spectral crossover になる。

ただし、この現象が任意の $J_1,J_2,J_3$ で必ず現れるわけではない。R=3 が初めて**複数の候補モードを持てる最小の系**である、というのが正確な言い方である。

## 5. R=2 から R=N へ何が一般化されるか

R=2 で見た

$$
q_{\rm spec}
\neq
q_\chi
$$

という「最長距離モード」と「全距離を足し上げた最大応答」の分離は、R=N でもそのまま残る。むしろ $N$ が増えると、$q_{\rm spec}$ の候補自身が複数になりうるので、階層は

$$
\boxed{
\text{microscopic couplings}
\to
\text{wall-pattern weights}
\to
\text{transfer spectrum}
\to
q_{\rm spec}
\to
\chi(q)
}
$$

と見るのがよい。

R=2 では transfer spectrum の複素化が最初の新現象だった。R=N ではさらに、複数の subleading mode の競合・交差・複素化を同じ枠組みで扱える。

## 6. 次に調べるべき量

この一般化を実際の計算へ落とすときは、まず R=3 を数値対角化するのが自然である。$J_1$ を基準にして $(J_2/J_1,J_3/J_1,T/J_1)$ を走査し、各点で

$$
\lambda_0,
\qquad
\lambda_a/\lambda_0,
\qquad
q_a=\arg\lambda_a,
\qquad
\xi_a^{-1}=-\ln|\lambda_a/\lambda_0|
$$

を追う。

特に見たいのは、

1. 実固有値から複素共役対へ移る境界、
2. 異なる subleading mode の絶対値が交差する境界、
3. 支配波数 $q_{\rm spec}$ の連続変化と不連続な切り替え、
4. $q_{\rm spec}$ と $q_\chi$ のずれ、
5. 有限距離相関で複数モードの干渉が見える領域、

である。

## 7. まとめ

有限範囲1次元 Ising 鎖は、相互作用距離を増やすほど単に transfer matrix が大きくなる模型ではない。

$$
\boxed{
R=N
\quad\Longrightarrow\quad
\begin{cases}
\text{wall picture: 最大 }N\text{体相互作用}\\
\text{spin transfer picture: }2^N\text{ 状態}\\
\text{wall information picture: 最大 }N-1\text{ step memory}\\
\text{correlation picture: 複数 subleading mode の競合が可能}
\end{cases}
}
$$

R=3 はその一般則を初めて具体的に見せる最小例である。3体壁相互作用と2ステップ記憶が現れ、相関スペクトルも R=2 より多くの候補モードを持てる。

したがって次の段階では、R=3 を個別模型として閉じるのではなく、**R=N の一般構造を検証する最初の実験台として使う**のがよい。
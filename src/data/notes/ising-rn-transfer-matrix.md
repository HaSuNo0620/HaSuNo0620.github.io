---
title: "1次元イジング模型 — 有限範囲相互作用と高次壁相互作用・有限記憶"
summary: "有限範囲の1次元Ising鎖を一般化し、ドメイン壁表示では高次の局所相互作用、壁列では有限ステップの記憶が現れることを整理する。第三近接までを最初の具体例として読む。"
publishedAt: 2026-09-11T19:30:00+09:00
updatedAt: 2026-09-14
area: "Physics"
topics: ["statistical mechanics", "Ising model", "transfer matrix", "domain wall", "finite memory", "correlation"]
status: growing
---

最近接ではdomain wallは独立、第二近接ではwall同士が相互作用した。相互作用範囲をさらに伸ばすと、この対応はそのまま高次化する。

有限範囲 $N$ の Ising 鎖を

$$
\boxed{
H=-\sum_{n=1}^{N}J_n\sum_i s_i s_{i+n},
\qquad s_i=\pm1}
$$

とする。

この一般化で増えるのは transfer matrix のサイズだけではない。相互作用範囲 $N$ は、wall表示では**最大 $N$ 体の局所相互作用**へ、条件付き統計では**最大 $N-1$ step の空間記憶**へ写る。

![相互作用範囲と壁相互作用・記憶長の対応](/figures/ising-rn/range-memory-map.svg)

## 1. 距離 $n$ のスピン結合は連続する $n$ 個の wall の積になる

$$
\tau_i\equiv s_i s_{i+1}
$$

とすると

$$
\boxed{
s_i s_{i+n}
=\prod_{m=0}^{n-1}\tau_{i+m}}
$$

である。

したがって

$$
\boxed{
H
=-\sum_{n=1}^{N}J_n
\sum_i
\prod_{m=0}^{n-1}\tau_{i+m}}
$$

となる。

$$
\boxed{
\text{spin interaction range }N
\Longleftrightarrow
\text{wall variables の最大 }N\text{体相互作用}}
$$

という対応が直接見える。

最初の三段階は

$$
N=1:\quad H=-J_1\sum_i\tau_i,
$$

$$
N=2:\quad
H=-J_1\sum_i\tau_i
-J_2\sum_i\tau_i\tau_{i+1},
$$

$$
N=3:\quad
H=-J_1\sum_i\tau_i
-J_2\sum_i\tau_i\tau_{i+1}
-J_3\sum_i\tau_i\tau_{i+1}\tau_{i+2}.
$$

第三近接で初めて、壁ペアだけでは表せない3体項が現れる。

## 2. スピン表示の state size と wall 列の memory length は別の数え方になる

新しいスピンを加えるとき、距離 $N$ までの局所 Boltzmann 重みを決めるには直前の $N$ 個のスピンが必要になる。

$$
\sigma_i=(s_{i-N+1},\ldots,s_i)
$$

と取れば transfer state 数は

$$
\boxed{2^N}
$$

である。

遷移は

$$
(a_1,a_2,\ldots,a_N)
\longrightarrow
(a_2,\ldots,a_N,c)
$$

という sliding window になる。

一方、wall Hamiltonian は最大 $N$ 個連続した $\tau$ を含むので、次のwallの条件付き確率には最大で直前 $N-1$ 個のwallが必要になる。

$$
N=1:\ 0\text{ step memory},
\qquad
N=2:\ 1\text{ step memory},
\qquad
N=3:\ 2\text{ step memory}.
$$

一般には

$$
\boxed{
N\text{ range}
\Longrightarrow
(N-1)\text{ step wall memory}}
$$

となる。

ここでいうmemoryは時間発展の非平衡記憶ではなく、**鎖に沿って次の局所確率を決めるために必要な履歴**である。

## 3. 第三近接では3体wall相互作用と2-step memoryが同時に現れる

$$
H=-J_1\sum_i s_is_{i+1}
-J_2\sum_i s_is_{i+2}
-J_3\sum_i s_is_{i+3}
$$

は

$$
\boxed{
H=-J_1\sum_i\tau_i
-J_2\sum_i\tau_i\tau_{i+1}
-J_3\sum_i\tau_i\tau_{i+1}\tau_{i+2}}
$$

となる。

![R=3 で初めて現れる3体壁相互作用](/figures/ising-rn/r3-wall-interaction.svg)

$J_3$ は単独のwallや隣接wall pairではなく、3つ並んだwall patternそのものへエネルギーを与える。

確率過程としても一般には

$$
P(\tau_{i+2}\mid\tau_{i+1},\tau_i)
\neq
P(\tau_{i+2}\mid\tau_{i+1})
$$

となる。

## 4. 相関 spectrum には複数の候補 mode が入れるようになる

第二近接では、相関を担うodd sectorは実質2×2であり、長距離を支配する構造は二つの実固有値か一組の複素共役対だった。

第三近接では transfer matrix は8×8となり、対称性でsector分解しても subleading mode の候補が増える。

したがって一般には

$$
C(r)
\sim
\sum_a A_a\rho_a^r\cos(q_a r+\phi_a)
$$

と書ける。

重要なのは項数そのものではなく、パラメータ変化によって

$$
|\lambda_a|=|\lambda_b|
$$

を跨ぎ、長距離を支配するmodeが切り替わりうることである。

$$
q_a\longrightarrow q_b
$$

という spectral crossover は、第二近接での「実固有値→複素対」とは別の機構になる。

第三近接は、**複数の長距離候補modeを持てる最小の有限範囲鎖**として位置づけられる。

## 5. 相互作用範囲を伸ばしても $q_{\rm spec}$ と $q_\chi$ の区別は残る

第二近接で現れた

$$
q_{\rm spec}\neq q_\chi
$$

という区別は一般の有限範囲でも残る。

むしろmode候補が増えるため

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
\chi(q)}
$$

という階層がより重要になる。

$q_{\rm spec}$ は最も遅く減衰するmodeの位相であり、$q_\chi$ は全距離相関を足し上げたresponseの最大位置である。前者の候補が複数になっても、後者と自動的に一致するわけではない。

## 6. 第三近接で見るべき spectrum の変化

第三近接を具体的に調べるなら

$$
\lambda_0,
\qquad
\frac{\lambda_a}{\lambda_0},
\qquad
q_a=\arg\lambda_a,
\qquad
\xi_a^{-1}=-\ln\left|\frac{\lambda_a}{\lambda_0}\right|
$$

を追えばよい。

特に区別したいのは

- 実固有値が複素共役対へ移る境界
- 異なるsubleading modeの絶対値が交差する境界
- $q_{\rm spec}$ の連続的変化とmode switchingによる不連続変化
- $q_{\rm spec}$ と $q_\chi$ のずれ
- 有限距離で複数modeが干渉する領域

である。

これは「次に解く課題」というより、有限範囲化によって spectrum に許される新しい構造の一覧になっている。

## 7. 有限範囲は局所相互作用と有限記憶の二つの言葉で同じものを表す

まとめると

$$
\boxed{
N\text{ range}
\Longrightarrow
\begin{cases}
\text{wall picture: 最大 }N\text{体局所相互作用}\\
\text{spin transfer picture: }2^N\text{ states}\\
\text{wall process: 最大 }N-1\text{ step memory}\\
\text{correlation spectrum: 複数 subleading mode の競合が可能}
\end{cases}}
$$

となる。

相互作用範囲を伸ばすことは、単に結合項を増やす操作ではない。**どこまで過去を保持しなければ局所統計が閉じないか**を増やす操作としても読める。

第三近接は、その一般構造が高次wall相互作用とmode competitionとして初めて明示的に現れる基準例になっている。

---
title: "1次元一様有限範囲 cosine-Z2 スピン系 — 高次壁相互作用と有限記憶"
summary: "有限範囲の1次元Ising鎖を一般化し、ドメイン壁表示では高次の局所相互作用、壁列では有限ステップの記憶が現れることを整理する。第三近接までを最初の具体例として読む。"
publishedAt: 2026-09-11T19:30:00+09:00
updatedAt: 2026-09-19
area: "Physics"
topics: ["statistical mechanics", "Ising model", "transfer matrix", "domain wall", "finite memory", "correlation"]
status: growing
system:
  dimension: 1
  spatial: uniform
  range: Rn
  interaction: cosine
  symmetry: [Z2]
  mechanics: classical
  role: model
---

最近接ではドメイン壁は独立、第二近接ではドメイン壁同士が相互作用した。相互作用範囲をさらに伸ばすと、この対応はそのまま高次化する。

有限範囲 $N$ の Ising 鎖を

$$
\boxed{
H=-\sum_{n=1}^{N}J_n\sum_i s_i s_{i+n},
\qquad s_i=\pm1}
$$

とする。

この一般化で増えるのは 転送行列 のサイズだけではない。相互作用範囲 $N$ は、ドメイン壁表示では**最大 $N$ 体の局所相互作用**へ、条件付き統計では**最大 $N-1$ step の空間記憶**へ写る。

![相互作用範囲と壁相互作用・記憶長の対応](/figures/ising-rn/range-memory-map.svg)

## 系の座標

$$
\boxed{
(d=1,\ \text{uniform},\ R=n,\ \text{cosine},\ Z_2)
}
$$

有限範囲 Hamiltonian

$$
H = -\sum_i\sum_{r=1}^{R}
J_r s_i s_{i+r}
$$

を、局所 wall 変数

$$
\tau_i=s_i s_{i+1}
$$

で読む。$R$ を伸ばすことは、局所エネルギーが読む 壁配置 の長さを伸ばすことに対応する。

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
\text{spin 相互作用範囲 }N
\Longleftrightarrow
\text{ドメイン壁変数 の最大 }N\text{体相互作用}}
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

## 2. スピン表示の state size と ドメイン壁列の 記憶長 は別の数え方になる

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

一方、wall Hamiltonian は最大 $N$ 個連続した $\tau$ を含むので、次のドメイン壁の条件付き確率には最大で直前 $N-1$ 個のドメイン壁が必要になる。

$$
N=1:\ 0\text{ step 記憶},
\qquad
N=2:\ 1\text{ step 記憶},
\qquad
N=3:\ 2\text{ step 記憶}.
$$

一般には

$$
\boxed{
N\text{ range}
\Longrightarrow
(N-1)\text{ ステップのドメイン壁記憶}}
$$

となる。

ここでいう記憶は時間発展の非平衡記憶ではなく、**鎖に沿って次の局所確率を決めるために必要な履歴**である。

## 3. 第三近接では3体ドメイン壁相互作用と2-step 記憶が同時に現れる

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

$J_3$ は単独のドメイン壁や隣接ドメイン壁対ではなく、3つ並んだ壁配置そのものへエネルギーを与える。

確率過程としても一般には

$$
P(\tau_{i+2}\mid\tau_{i+1},\tau_i)
\neq
P(\tau_{i+2}\mid\tau_{i+1})
$$

となる。

## 4. 相関スペクトル には複数の候補 mode が入れるようになる

第二近接では、相関を担う奇セクターは実質2×2であり、長距離を支配する構造は二つの実固有値か一組の複素共役対だった。

第三近接では 転送行列 は8×8となり、対称性でsector分解しても 副次モード の候補が増える。

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
\text{ドメイン壁配置の重み}
\to
\text{転送スペクトル}
\to
q_{\rm spec}
\to
\chi(q)}
$$

という階層がより重要になる。

$q_{\rm spec}$ は最も遅く減衰するmodeの位相であり、$q_\chi$ は全距離相関を足し上げた応答の最大位置である。前者の候補が複数になっても、後者と自動的に一致するわけではない。

## 6. 第三近接で見るべき スペクトルの変化

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
- 異なる副次モードの絶対値が交差する境界
- $q_{\rm spec}$ の連続的変化とmode switchingによる不連続変化
- $q_{\rm spec}$ と $q_\chi$ のずれ
- 有限距離で複数modeが干渉する領域

である。

これは「次に解く課題」というより、有限範囲化によって スペクトルに許される新しい構造の一覧になっている。

## 7. 有限範囲は局所相互作用と有限記憶の二つの言葉で同じものを表す

まとめると

$$
\boxed{
N\text{ range}
\Longrightarrow
\begin{cases}
\text{ドメイン壁描像: 最大 }N\text{体局所相互作用}\\
\text{spin transfer picture: }2^N\text{ states}\\
\text{ドメイン壁過程: 最大 }N-1\text{ step 記憶}\\
\text{相関スペクトル: 複数 副次モード の競合が可能}
\end{cases}}
$$

となる。

相互作用範囲を伸ばすことは、単に結合項を増やす操作ではない。**どこまで過去を保持しなければ局所統計が閉じないか**を増やす操作としても読める。

第三近接は、その一般構造が高次wall相互作用とモード競合として初めて明示的に現れる基準例になっている。


## 8. 一様外場と周期外場は複数モードの重なりを読む

外場を

$$
H_h=-\sum_i h_i s_i
$$

として加える。零外場まわりでは

$$
\delta\langle s_i\rangle =
\sum_j\chi_{ij}h_j,
\qquad
\chi_{ij} =
\beta\langle s_i s_j\rangle.
$$

一様外場 \(h_i=h\) は

$$
\boxed{
m=\chi(0)h+O(h^3)
}
$$

として \(q=0\) 成分を読む。

周期外場

$$
h_i=h_q\cos(qi+\varphi)
$$

に対しては

$$
\boxed{
\delta\langle s_i\rangle =
\chi(q)h_q\cos(qi+\varphi)
+O(h_q^3)
}
$$

となる。

有限範囲では

$$
C(r)
\sim
\sum_a A_a\rho_a^r\cos(q_a r+\phi_a)
$$

なので、\(\chi(q)\) は単一モードではなく複数の転送モードを全距離で重ねた量になる。

したがって

$$
\boxed{
\text{転送スペクトルの候補 }q_a
\longrightarrow
\chi(q)
\longrightarrow
q_\chi
}
$$

という順に、内部モードと外場応答を区別して読む必要がある。

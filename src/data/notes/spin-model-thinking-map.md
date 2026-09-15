---
title: "スピン系をどう読むか — 記憶変数・相互作用範囲・空間構造・近似"
summary: "Ising・clock・XYなどのスピン模型を、何を記憶するか、どこまで記憶するか、記憶則が空間のどこで変わるか、そして近似がどの情報を残すか、という共通軸で整理する。既存ノートの上位地図として、次に何を変えると何が新しく見えるかを示す。"
publishedAt: 2026-09-16T03:45:00+09:00
updatedAt: 2026-09-16
area: "Physics"
topics: ["statistical mechanics", "spin models", "transfer matrix", "coarse graining"]
status: growing
---

Ising、clock、XYを模型名ごとに並べるだけでは、どこが同じでどこが違うのかが見えにくい。相互作用範囲を伸ばしたり、結合を周期化したり、近似法を変えたりすると、なおさら個別の話に見えてしまう。

今のところ、スピン系を読む軸は次の二層に分けるのが一番使いやすい。

$$
\boxed{
\text{模型の構造}
=
(\text{何を記憶するか},\ \text{どこまで記憶するか},\ \text{記憶則の空間構造})
}
$$

と

$$
\boxed{
\text{近似・表現}
=
\text{何を粗視化し、何を情報として残すか}
}
$$

である。

このノートは個々の模型を解くためのものではない。既存のスピン系ノートを同じ座標へ置き、**次に一つの軸だけを変えたとき何が新しく生まれるか**を見るための上位地図である。

## 1. 第一軸：何を記憶するか

最近接 Ising では

$$
\tau_i=s_i s_{i+1}=\pm1
$$

と置くと、$\tau_i=-1$ はスピンの反転、すなわち domain wall を表す。

元のスピン相関は

$$
s_0s_r=\prod_{j=0}^{r-1}\tau_j
$$

なので、遠距離のスピン記憶は局所的な符号反転の列から作られる。

一方 XY では

$$
\phi_i=\theta_{i+1}-\theta_i
$$

が局所変数であり、

$$
e^{i(\theta_r-\theta_0)}
=\prod_{j=0}^{r-1}e^{i\phi_j}
$$

となる。

両者の違いは、遠距離相関の作り方そのものより、局所増分が

$$
\tau_i\in\{+1,-1\}
$$

という離散反転なのか、

$$
\phi_i\in S^1
$$

という連続回転なのかにある。

したがって第一軸は

$$
\boxed{
\text{spin symmetry}
\longleftrightarrow
\text{何を記憶するか}
}
$$

と読める。

Ising と XY の間には $q$-state clock model が入る。角度を

$$
\theta_i=\frac{2\pi n_i}{q},
\qquad n_i=0,\ldots,q-1
$$

と制限すれば、局所増分は有限個の回転になる。

$$
\boxed{
Z_2\ \text{Ising}
\longrightarrow
Z_q\ \text{clock}
\longrightarrow
U(1)\ \text{XY}
}
$$

は、符号反転の記憶から連続位相増分の記憶へ移る軸として読める。

## 2. 第二軸：どこまで記憶するか

相互作用範囲 $R$ は、局所エネルギーがどれだけ長い増分列を見るかを決める。

Ising では

$$
s_i s_{i+r}
=\prod_{m=0}^{r-1}\tau_{i+m}
$$

なので、一般の有限範囲模型

$$
H=-\sum_i\sum_{r=1}^{R}J_r s_i s_{i+r}
$$

は bond 変数で

$$
H
=-\sum_i\sum_{r=1}^{R}
J_r\prod_{m=0}^{r-1}\tau_{i+m}
$$

となる。

$R=1$ では各 $\tau_i$ は独立だが、$R=2$ では

$$
-J_2\tau_i\tau_{i+1}
$$

が現れ、隣接する wall 変数が相関する。さらに $R=3$ では三つの wall pattern を局所エネルギーが同時に読む。

XY でも

$$
\theta_{i+r}-\theta_i
=\sum_{m=0}^{r-1}\phi_{i+m}
$$

なので、距離 $r$ の結合は

$$
-J_r\cos\left(\sum_{m=0}^{r-1}\phi_{i+m}\right)
$$

となる。

したがって

$$
\boxed{
R
\longleftrightarrow
\text{局所エネルギーが保持する memory depth}
}
$$

と見られる。

ここで重要なのは、第一軸と第二軸を分けることである。

$$
\boxed{
\text{Ising / XY の違い}
=\text{何を記憶するか}
}
$$

$$
\boxed{
R\text{ の違い}
=\text{どこまで記憶するか}
}
$$

この分離によって、例えば $R=2$ を固定して Ising と XY を比べることと、Ising を固定して $R=1\to2$ を比べることが別の問いになる。

## 3. 第三軸：記憶則は空間のどこで変わるか

相互作用変数が同じでも、結合 $J_i$ の空間構造を変えると、同じ局所記憶則が場所ごとに異なる重みを持つ。

$$
\boxed{
J_i=J
}
$$

なら一様、

$$
\boxed{
J_{i+p}=J_i
}
$$

なら周期的である。

最近接 Ising の零外場では

$$
H=-\sum_iJ_i\tau_i
$$

なので、周期 bond を入れても wall 同士は独立なままである。ただし wall を置くコストが位置依存になる。

この軸は

$$
\boxed{
\text{uniform}
\to
\text{periodic}
\to
\text{quasiperiodic}
\to
\text{random}
}
$$

と伸ばせる。

したがって第三軸は

$$
\boxed{
\text{spatial organization}
=\text{memory rule が空間のどこでどう変わるか}
}
$$

である。

周期 bond Ising はこの軸だけを変えた例であり、第二近接 Ising は第二軸だけを変えた例になる。この違いを混ぜないことが重要である。

## 4. 模型の座標を固定すると比較の意味が明確になる

既存ノートは次のように置ける。

| 模型 | 何を記憶するか | memory depth | spatial organization |
| --- | --- | --- | --- |
| [最近接 Ising](/notes/ising-transfer-matrix) | flip / wall | $R=1$ | uniform |
| [周期 bond Ising](/notes/ising-r1-periodic) | flip / wall | $R=1$ | periodic |
| [周期 bond + field Ising](/notes/ising-r1-periodic-field) | flip + absolute-spin response | $R=1$ | periodic + field |
| [第二近接 Ising](/notes/ising-r2-transfer-matrix) | wall pattern | $R=2$ | uniform |
| [有限範囲 Ising](/notes/ising-rn-transfer-matrix) | longer wall pattern | $R=n$ | uniform |
| [最近接 XY](/notes/xy-chain-nearest-neighbor) | phase increment | $R=1$ | uniform |
| [第二近接 XY](/notes/xy-chain-second-neighbor) | correlated phase increment / chirality | $R=2$ | uniform |

この表から、比較は一つの座標だけを動かして行うのがよい。

$$
\text{Ising }R=1
\longrightarrow
\text{Ising }R=2
$$

では memory variable を固定して depth の効果を見る。

$$
\text{Ising }R=2
\longleftrightarrow
\text{XY }R=2
$$

では depth を固定して memory variable の違いを見る。

$$
\text{uniform Ising }R=1
\longrightarrow
\text{periodic Ising }R=1
$$

では variable と depth を固定し、spatial organization だけを変える。

[第二近接 Ising–XY 比較](/notes/ising-xy-second-neighbor-comparison) は、このうち「同じ $R=2$ で何を記憶するかを変える」比較に対応する。

## 5. 近似は第四の模型軸ではない

mean field、Bethe/cavity、transfer matrix/operatorを、模型側の三軸と同列に置くと少し分かりにくい。

近似・表現は模型を変えるのではなく、**その模型からどの情報を残して読むか**を決める。

$$
\boxed{
\text{approximation / representation}
=\text{information filter}
}
$$

と見る方が近い。

### mean field / saddle point

揺らぎを抑えて代表的な場配置を残すため、自然に見えるのは

$$
\boxed{
\text{秩序・欠陥・texture・barrier}
}
$$

である。

第二近接 XY なら、二つの chirality sector と、それらをつなぐ kink profile、kink energy が見えやすい。

### Bethe / cavity

局所条件付き確率を残すので、中心量は

$$
P(x_{i+1}|x_i)
$$

になる。

したがって自然に見えるのは

$$
\boxed{
\text{局所遷移・switching probability・局所統計}
}
$$

である。

### transfer matrix / operator

局所情報を spectrum へ集約するので、長距離で残る mode が直接見える。

$$
\boxed{
\xi^{-1}
=-\ln\left|\frac{\lambda_1}{\lambda_0}\right|
}
$$

複素固有値なら、その位相から相関波数も得られる。

したがって自然に見えるのは

$$
\boxed{
\text{長距離memory・相関長・構造波数}
}
$$

である。

近似法の関係は

$$
\text{mean field}<\text{Bethe}<\text{exact}
$$

という精度の階段だけではない。

$$
\boxed{
\text{どの自由度を残すか}
\longrightarrow
\text{何を本質として見られるか}
}
$$

という違いである。

## 6. 模型と近似を掛け合わせる

スピン系を考えるときは、まず模型の座標

$$
\boxed{
(\text{memory variable},\ R,\ \text{spatial organization})
}
$$

を決め、そのあと

$$
\boxed{
\text{何を知りたいか}
\longrightarrow
\text{どの近似・表現を使うか}
}
$$

を決める。

例えば第二近接 XY は

$$
(\phi_i,\ R=2,\ \text{uniform})
$$

という一つの模型である。

これを saddle point で見れば chirality kink、Bethe/cavity で見れば $P(\phi'|\phi)$ と switching、transfer operator で見れば $\lambda_\chi$、$\xi_\chi$、spin correlation の tilted spectrum が中心になる。

同じ模型でも、理論が残す情報が違えば、見えてくる「本質」も違う。

## 7. 次に何を変えるべきか

この地図では、新しい模型を追加すること自体が目的ではない。**一つの軸だけを動かし、何が新しく生まれたかを調べる**ことが中心になる。

現在まだ薄い方向は次の通りである。

第一軸では、Ising と XY の間に clock model がある。

$$
Z_2
\to
Z_q
\to
U(1)
$$

と変えたとき、離散的な flip memory がどのように連続的な phase diffusion へ移るかを見ることができる。

第三軸では、周期 bond の先に quasiperiodic / random bond がある。

$$
\text{periodic}
\to
\text{quasiperiodic}
\to
\text{random}
$$

と変えたとき、Hamiltonian の空間秩序が相関関数の空間秩序へどう移るかが問いになる。

さらに現在のノート群はほぼ静的な空間記憶

$$
C(r)
$$

を扱っている。将来的には

$$
C(r,t)
$$

へ進めば、transfer spectrum が記述する spatial memory と、Markov generator が記述する temporal memory を比較できる。

次元を上げる方向もある。1次元では point defect だった domain wall が2次元では line defect になり、energy と entropy の競争が有限温度相転移を可能にする。

ただしこれらは別々の新テーマではない。すべて

$$
\boxed{
\text{どの記憶変数が、どこまで、どんな空間規則で結合し、
どの情報フィルターでそれを見るか}
}
$$

という同じ問いの変形である。

## 現在の見取り図

スピン系を模型名の一覧として見るより、今は次の形が使いやすい。

$$
\boxed{
\begin{array}{c}
\text{model coordinates}\\[1mm]
(\text{memory variable},\ R,\ \text{spatial organization})
\end{array}
}
\quad\times\quad
\boxed{
\begin{array}{c}
\text{information filter}\\[1mm]
\text{mean field / Bethe / transfer / \cdots}
\end{array}
}
$$

この二層を分けると、「新しい模型を解いた」のではなく、**どの構造を変えたことで、どの種類の記憶が新しく現れたのか**を追えるようになる。

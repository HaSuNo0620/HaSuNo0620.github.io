---
title: "スピン系をどう読むか — 記憶変数・相互作用範囲・空間構造・情報フィルター"
summary: "Ising・clock・XYなどの1次元スピン模型を、memory variable、interaction range、spatial organizationという三つの模型座標と、近似・表現が何を残すかというinformation filterに分けて整理する。既存ノート群の位置づけと、次に一軸だけ動かしたとき何が新しく現れるかを見通すための上位地図。"
publishedAt: 2026-09-16T03:45:00+09:00
updatedAt: 2026-09-19
area: "Physics"
topics: ["statistical mechanics", "spin models", "transfer matrix", "coarse graining", "memory"]
status: growing
---

Ising、clock、XYを模型名ごとに並べるだけでは、何が本質的に違うのかが見えにくい。相互作用範囲を伸ばす、結合を周期化する、近似法を変える、といった操作まで加わると、異なる種類の変更が同じ「別模型」として並んでしまう。

今のスピン系ノート群では、模型そのものを

$$
\boxed{
\text{model coordinates}
=
(\text{memory variable},\ R,\ \text{spatial organization})
}
$$

で置き、その模型をどう読むかを

$$
\boxed{
\text{approximation / representation}
=
\text{information filter}
}
$$

として分ける。

前者は「どんな系か」、後者は「その系から何を残して見るか」に対応する。

---

## 1. memory variable — 何を記憶するか

最近接 Ising では

$$
\tau_i=s_i s_{i+1}=\pm1
$$

を局所変数に取れる。$\tau_i=-1$ は domain wall / spin flip であり、

$$
s_0s_r
=
\prod_{j=0}^{r-1}\tau_j
$$

だから、遠距離のスピン記憶は局所的な符号反転列の積として作られる。

$$
\boxed{
\text{Ising}
=
\text{離散的な flip / wall 配置を記憶する系}
}
$$

XY では

$$
\phi_i=\theta_{i+1}-\theta_i
$$

が対応する局所増分で、

$$
e^{i(\theta_r-\theta_0)}
=
\prod_{j=0}^{r-1}e^{i\phi_j}.
$$

したがって

$$
\boxed{
\text{XY}
=
\text{連続的な phase increment を記憶する系}
}
$$

となる。

両者に共通するのは

$$
\boxed{
\text{局所増分の列}
\longrightarrow
\text{その累積・積が遠距離 memory を決める}
}
$$

という構造である。

### 離散二値と連続位相の間

$q$-state clock model では

$$
\theta_i=\frac{2\pi n_i}{q},
\qquad
n_i\in\mathbb Z_q,
$$

局所増分は

$$
\phi_i
=
\frac{2\pi a_i}{q},
\qquad
a_i\in\mathbb Z_q.
$$

よって

$$
\boxed{
Z_2\ \text{Ising}
\longrightarrow
Z_q\ \text{clock}
\longrightarrow
U(1)\ \text{XY}
}
$$

は

$$
\boxed{
\{0,\pi\}
\longrightarrow
\left\{\frac{2\pi a}{q}\right\}
\longrightarrow
S^1
}
$$

という **memory alphabet の細分化** として読める。

ただし、有限 $q$ が XY にどれだけ近いかは $q$ だけでは決まらない。低温での thermal angular width は

$$
\sigma_T\sim K^{-1/2},
\qquad K=\beta J,
$$

clock の角度刻みは

$$
\Delta\phi=\frac{2\pi}{q}
$$

なので、

$$
\boxed{
\eta
=
\frac{\Delta\phi}{\sigma_T}
\sim
\frac{2\pi\sqrt K}{q}
}
$$

が離散性を実際に解像できるかを決める。

$$
\eta\gg1
\quad\Rightarrow\quad
\text{rare discrete jump},
$$

$$
\eta\ll1
\quad\Rightarrow\quad
\text{dense small-step phase diffusion}.
$$

したがって symmetry 軸は単なる状態数の増加ではなく、

$$
\boxed{
\text{memory alphabet}
\times
\text{thermal resolution}
}
$$

として読む方が物理が見えやすい。

さらに Fourier 側では finite $q$ により

$$
m\sim m+q
$$

という harmonic folding が起こり、

$$
\boxed{
\text{angular discretization}
\longleftrightarrow
\text{spectral aliasing}
}
$$

が同じ有限-$q$性の二つの表現になる。

[1次元クロック模型 — 離散位相増分と角度記憶](/notes/clock-chain-nearest-neighbor) は、この $Z_2\to Z_q\to U(1)$ 軸を実際に埋める位置にある。

---

## 2. interaction range (R) — どこまで記憶するか

memory variable を固定して相互作用範囲だけを伸ばすと、局所エネルギーが読む増分列の長さが変わる。

Ising では

$$
s_i s_{i+r}
=
\prod_{m=0}^{r-1}\tau_{i+m}
$$

なので、

$$
H
=
-\sum_i\sum_{r=1}^{R}
J_r s_i s_{i+r}
$$

は

$$
\boxed{
H
=
-\sum_i\sum_{r=1}^{R}
J_r
\prod_{m=0}^{r-1}\tau_{i+m}
}
$$

となる。

$R=1$ では

$$
H=-J_1\sum_i\tau_i
$$

で wall 変数は独立。

$R=2$ では

$$
H
=
-J_1\sum_i\tau_i
-J_2\sum_i\tau_i\tau_{i+1},
$$

隣接する wall / flip 配置が相関する。

$R=3$ では

$$
s_i s_{i+3}
=
\tau_i\tau_{i+1}\tau_{i+2}
$$

が入り、より長い wall pattern を局所エネルギーが区別する。

XY でも

$$
\theta_{i+r}-\theta_i
=
\sum_{m=0}^{r-1}\phi_{i+m}
$$

なので、

$$
-J_r
\cos\left(
\sum_{m=0}^{r-1}\phi_{i+m}
\right)
$$

が長さ $r$ の phase-increment pattern を読む。

したがって

$$
\boxed{
R
=
\text{memory depth}
}
$$

とみなせる。

この分離によって

$$
\boxed{
\text{Ising / clock / XY の違い}
=
\text{何を記憶するか}
}
$$

と

$$
\boxed{
R\text{ の違い}
=
\text{どこまで記憶するか}
}
$$

を混ぜずに扱える。

---

## 3. spatial organization — 記憶則が空間のどこで変わるか

memory variable と $R$ を固定したまま、結合の配置だけを変える方向がある。

$$
J_i=J
$$

なら uniform、

$$
J_{i+p}=J_i
$$

なら periodic、

Fibonacci word に従えば quasiperiodic、

確率的に選べば random bond になる。

最近接 Ising の零外場なら

$$
H=-\sum_iJ_i\tau_i
$$

なので、$J_i$ を変えても wall 同士は独立なままである。変わるのは「どの位置で wall を作りやすいか」という空間規則である。

$$
\boxed{
\text{spatial organization}
=
\text{memory rule が空間のどこでどう変わるか}
}
$$

周期 bond Ising は

$$
\text{uniform}
\longrightarrow
\text{periodic}
$$

だけを動かした模型として読める。

次の自然な延長は

$$
\boxed{
\text{periodic}
\longrightarrow
\text{quasiperiodic}
\longrightarrow
\text{random}
}
$$

である。

最近接零外場なら

$$
C_i(r)
=
\prod_{n=0}^{r-1}
\tanh(\beta J_{i+n})
$$

だから、

$$
\ln C_i(r)
=
\sum_{n=0}^{r-1}
\ln\tanh(\beta J_{i+n})
$$

となり、Hamiltonian に入れた空間列が correlation の空間構造へ直接移る。

この軸では

$$
\boxed{
\text{Hamiltonian の spatial order}
\longrightarrow
\text{correlation の spatial order}
}
$$

が中心問題になる。

---

## 4. 既存ノートを model coordinates に置く

個別模型ノートは次の座標に置ける。

| ノート | memory variable | $R$ | spatial organization |
| --- | --- | --- | --- |
| [1次元イジング模型 — 最近接相互作用と空間応答](/notes/ising-transfer-matrix) | flip / wall | $1$ | uniform |
| [1次元イジング模型 — 周期的最近接結合と構造波数](/notes/ising-r1-periodic) | flip / wall | $1$ | periodic |
| [1次元イジング模型 — 周期外場と応答モード](/notes/ising-r1-periodic-field) | flip + absolute-spin response | $1$ | periodic + field |
| [1次元イジング模型 — 第二近接相互作用と振動相関・有限波数応答](/notes/ising-r2-transfer-matrix) | interacting wall pattern | $2$ | uniform |
| [1次元イジング模型 — 有限範囲相互作用と高次壁相互作用・有限記憶](/notes/ising-rn-transfer-matrix) | longer wall pattern | $n$ | uniform |
| [1次元クロック模型 — 離散位相増分と角度記憶](/notes/clock-chain-nearest-neighbor) | discrete phase increment | $1$ | uniform |
| [1次元XY模型 — 位相拡散と角度記憶](/notes/xy-chain-nearest-neighbor) | continuous phase increment | $1$ | uniform |
| [1次元XY模型 — 第二近接相互作用と螺旋的な空間記憶](/notes/xy-chain-second-neighbor) | correlated phase increment / chirality | $2$ | uniform |
| [1次元XY模型 — 第二近接系のchirality kinkと複数の空間記憶](/notes/xy-chain-chirality-memory) | chirality sector + phase | $2$ | uniform |

この表で重要なのは、模型数そのものではなく「どの座標を動かしたノートなのか」が見えることである。

例えば

$$
\text{Ising }R=1
\longrightarrow
\text{Ising }R=2
$$

は interaction range の変形、

$$
\text{Ising }R=1
\longrightarrow
\text{clock }R=1
\longrightarrow
\text{XY }R=1
$$

は memory variable / symmetry の変形、

$$
\text{uniform Ising }R=1
\longrightarrow
\text{periodic Ising }R=1
$$

は spatial organization の変形である。

---

## 5. 比較ノートは座標間の辞書として置く

比較ノートは独立模型ではなく、二つ以上の座標点を同じ物理量で読むための辞書に限定する。

[1次元スピン模型 — 最近接Ising・XYの空間記憶](/notes/ising-xy-nearest-neighbor-comparison) は、

$$
R=1,
\qquad
\text{uniform}
$$

を固定して、memory variable の違いが相関喪失へどう現れるかを見る。

[1次元スピン模型 — 第二近接Ising・XYを三つの解像度で見る](/notes/ising-xy-second-neighbor-comparison) は、

$$
R=2,
\qquad
\text{uniform}
$$

を固定し、

$$
\boxed{
\text{defect / texture}
\longleftrightarrow
\text{local transition probability}
\longleftrightarrow
\text{transfer spectral gap}
}
$$

という比較辞書を作る。

詳細導出は個別模型ノートへ置き、比較ノート側では同じ物理を異なる模型でどう読むかだけを残す。

---

## 6. approximation / representation は information filter

mean field、Bethe/cavity、transfer matrix/operator は model coordinates の第四軸ではない。

同じ模型に対して、どの自由度を残して見るかが異なる。

$$
\boxed{
\text{approximation / representation}
=
\text{information filter}
}
$$

とみなす。

### mean field / saddle point

揺らぎを抑えて代表的な配置を残すため、

$$
\boxed{
\text{秩序・texture・欠陥の形・barrier}
}
$$

が見えやすい。

第二近接 XY なら

$$
\phi\simeq\pm q_*
$$

という chirality sector、

$$
\phi_{\rm kink}(x)
$$

という kink profile、

$$
E_k
$$

という kink energy が自然に現れる。

### Bethe / cavity

局所条件付き確率を残すため、

$$
P(x_{i+1}|x_i)
$$

が中心量になる。

Ising なら

$$
P(\tau_{i+1}|\tau_i),
$$

XY なら

$$
P(\phi_{i+1}|\phi_i)
$$

を読む。

$$
\boxed{
\text{どの局所状態の次に何が来やすいか}
}
$$

を見る表現である。

### transfer matrix / transfer operator

局所情報を spectrum へ集約し、長距離で残る mode を直接読む。

$$
T\psi_n=\lambda_n\psi_n,
$$

$$
\boxed{
\xi^{-1}
=
-\ln\left|
\frac{\lambda_1}{\lambda_0}
\right|
}
$$

で相関長が出る。

subleading eigenvalue が複素なら

$$
q_{\rm spec}=\arg\lambda_1
$$

から構造波数も得られる。

したがって自然に見えるのは

$$
\boxed{
\text{長距離 memory・相関長・構造波数}
}
$$

である。

三つの関係は

$$
\text{mean field}
<
\text{Bethe}
<
\text{exact}
$$

という単純な精度序列ではない。

$$
\boxed{
\text{欠陥の形}
\leftrightarrow
\text{局所遷移頻度}
\leftrightarrow
\text{長距離 spectrum}
}
$$

という異なる情報の切り出し方である。

---

## 7. 今どの軸まで埋まっているか

memory-variable 軸は

$$
\boxed{
Z_2
\to
Z_q
\to
U(1)
}
$$

まで一度つながった。

ここから得られたのは、Ising と XY の差を「離散か連続か」と言うだけでは足りず、

$$
\boxed{
\text{memory alphabet}
+
\text{thermal resolution}
+
\text{harmonic resolution}
}
$$

として読む必要がある、という見方である。

interaction-range 軸も

$$
R=1
\to
R=2
\to
R=n
$$

まで Ising 側で進み、XY 側では $R=2$ まで接続している。

現在もっとも薄いのは spatial organization 軸である。

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

のうち、periodic までは既存ノートがあるが、quasiperiodic / random はまだ空いている。

そのため次の一手としては、memory variable と $R$ を固定したまま

$$
\boxed{
\text{periodic}
\to
\text{quasiperiodic}
}
$$

だけを動かすのが自然になる。

Fibonacci bond Ising は、その最小例として

$$
\boxed{
\text{指数減衰}
\times
\text{準周期 modulation}
}
$$

がどのように相関へ現れるかを直接読める。

---

## 8. その先に残る二つの方向

spatial organization の次には、模型座標そのものとは別に二つの拡張が残る。

### spatial memory から temporal memory へ

現在の中心量は

$$
C(r)
$$

だが、Glauber dynamics などを入れれば

$$
C(r,t)
$$

へ進める。

そのとき

$$
\boxed{
\text{transfer spectrum}
\longleftrightarrow
\text{dynamical generator spectrum}
}
$$

として空間記憶と時間記憶を同じ spectral viewpoint で比較できる。

### 1D の point defect から 2D の line defect へ

1D Ising の domain wall は点だが、2D では線になる。

$$
E_{\rm wall}\sim\sigma\ell,
$$

$$
S_{\rm wall}\sim s\ell
$$

なら

$$
F_{\rm wall}
\sim
(\sigma-Ts)\ell.
$$

1D で使ってきた

$$
E_{\rm defect}
\longrightarrow
\Delta F_{\rm defect}
\longrightarrow
p_{\rm defect}
$$

という考え方が、2D では defect entropy と競合して有限温度相転移へつながる。

---

## 得られた見方

スピン系を個別模型の一覧として増やすより、

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

と置く方が、何を変えたことで新しい物理が現れたのかを追いやすい。

新しい模型を追加するときの問いも

$$
\boxed{
\text{どの軸を一つ動かしたのか}
}
$$

に戻せる。

現在は symmetry / memory-variable 軸が clock を介して一度閉じ、interaction-range 軸もかなり埋まった。次に最も情報量が大きい空白は spatial organization であり、

$$
\boxed{
\text{periodic}
\to
\text{quasiperiodic}
}
$$

が次の自然な変形になる。

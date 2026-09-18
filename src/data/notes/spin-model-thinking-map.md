---
title: "スピン系をどう読むか — 記憶変数・相互作用範囲・空間構造・情報フィルター"
summary: "cosine interaction family に属する1次元スピン系を、state space / symmetry、interaction range、spatial organizationという三つの座標で整理する。Z2・Zq・U(1)を同一Hamiltonian族として比較し、近似・表現はinformation filterとして分離する。"
publishedAt: 2026-09-16T03:45:00+09:00
updatedAt: 2026-09-19
area: "Physics"
topics: ["statistical mechanics", "spin models", "transfer matrix", "coarse graining", "memory"]
status: growing
---

Ising、clock、XYは別々の模型名として学ぶことが多い。しかし最近接相互作用を角度差で書けば、三者は同じ cosine interaction family に置ける。

$$
\boxed{
H = -\sum_i\sum_{r=1}^{R}
J_{i,r}\cos(\theta_{i+r}-\theta_i)
}
$$

違うのは、まず局所状態空間である。

$$
\boxed{
\theta_i\in
Z_2,\qquad
Z_q,\qquad
U(1)
}
$$

$Z_2$ では $\theta_i\in\{0,\pi\}$ と取れば

$$
\cos(\theta_i-\theta_j)=s_i s_j
$$

なので、標準 bilinear Ising 相互作用は cosine-$Z_2$ の特殊例として厳密に含まれる。

今のスピン系ノート群では、模型そのものを

$$
\boxed{
\text{model coordinates} = (\text{state space / symmetry},\ R,\ \text{spatial organization})
\qquad
[\text{cosine family fixed}]
}
$$

で置き、その模型をどう読むかを

$$
\boxed{
\text{approximation / representation} = \text{information filter}
}
$$

として分ける。

前者は「どんな系か」、後者は「その系から何を残して見るか」に対応する。

個別ノートでは interaction family をタイトルにも明示する。現在の基準系列はすべて

$$
\boxed{
V(\Delta\theta)=-J\cos\Delta\theta
}
$$

を基本とする cosine family なので、タイトルは

$$
\boxed{
\text{1次元}
+
\text{spatial organization}
+
\text{interaction range}
+
\text{cosine-symmetry}
+
\text{スピン系}
-
\text{固有の物理}
}
$$

とする。

したがって

$$
\boxed{
\text{cosine-}Z_2
\longrightarrow
\text{cosine-}Z_q
\longrightarrow
\text{cosine-}U(1)
}
$$

が同一 interaction family 内の symmetry / state-space 軸になる。

Ising、clock、XYという名前は本文中で既存文献との対応を示す呼称として残す。別の interaction form、例えば $\cos2\phi$ や多体項を加えた場合は、symmetry が同じでもこの cosine 基準系列とは別の interaction family として扱う。

---

## 1. memory variable — 何を記憶するか

最近接 Ising では

$$
\tau_i=s_i s_{i+1}=\pm1
$$

を局所変数に取れる。$\tau_i=-1$ は domain wall / spin flip であり、

$$
s_0s_r = \prod_{j=0}^{r-1}\tau_j
$$

だから、遠距離のスピン記憶は局所的な符号反転列の積として作られる。

$$
\boxed{
\text{Ising} = \text{離散的な flip / wall 配置を記憶する系}
}
$$

XY では

$$
\phi_i=\theta_{i+1}-\theta_i
$$

が対応する局所増分で、

$$
e^{i(\theta_r-\theta_0)} = \prod_{j=0}^{r-1}e^{i\phi_j}.
$$

したがって

$$
\boxed{
\text{XY} = \text{連続的な phase increment を記憶する系}
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
\phi_i = \frac{2\pi a_i}{q},
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
\eta = \frac{\Delta\phi}{\sigma_T}
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

[1次元一様最近接 cosine-Zq スピン系 — 離散位相増分と角度記憶](/notes/clock-chain-nearest-neighbor) は、この $Z_2\to Z_q\to U(1)$ 軸を実際に埋める位置にある。

---

## 2. interaction range (R) — どこまで記憶するか

memory variable を固定して相互作用範囲だけを伸ばすと、局所エネルギーが読む増分列の長さが変わる。

Ising では

$$
s_i s_{i+r} = \prod_{m=0}^{r-1}\tau_{i+m}
$$

なので、

$$
H = -\sum_i\sum_{r=1}^{R}
J_r s_i s_{i+r}
$$

は

$$
\boxed{
H = -\sum_i\sum_{r=1}^{R}
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
H = -J_1\sum_i\tau_i
-J_2\sum_i\tau_i\tau_{i+1},
$$

隣接する wall / flip 配置が相関する。

$R=3$ では

$$
s_i s_{i+3} = \tau_i\tau_{i+1}\tau_{i+2}
$$

が入り、より長い wall pattern を局所エネルギーが区別する。

XY でも

$$
\theta_{i+r}-\theta_i = \sum_{m=0}^{r-1}\phi_{i+m}
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
R = \text{memory depth}
}
$$

とみなせる。

この分離によって

$$
\boxed{
\text{Ising / clock / XY の違い} = \text{何を記憶するか}
}
$$

と

$$
\boxed{
R\text{ の違い} = \text{どこまで記憶するか}
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
\text{spatial organization} = \text{memory rule が空間のどこでどう変わるか}
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
C_i(r) = \prod_{n=0}^{r-1}
\tanh(\beta J_{i+n})
$$

だから、

$$
\ln C_i(r) = \sum_{n=0}^{r-1}
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

## 4. 既存ノートを座標点と座標間の橋として置く

現在のノート群は、個別模型ノートを **model point**、比較ノートを **coordinate bridge** として分けると構造が見えやすい。

### 4.1 model point — 各ノートがどの座標にいるか

| role | ノート | $d$ | spatial | $R$ | interaction | symmetry / state space | local memory |
| --- | --- | ---: | --- | --- | --- | --- | --- |
| model | [1次元一様最近接 cosine-$Z_2$ スピン系 — 空間記憶と応答](/notes/ising-transfer-matrix) | 1 | uniform | $R=1$ | cosine | $Z_2$ | flip / wall |
| model | [1次元周期最近接 cosine-$Z_2$ スピン系 — 構造波数](/notes/ising-r1-periodic) | 1 | periodic | $R=1$ | cosine | $Z_2$ | position-dependent wall weight |
| model | [1次元周期最近接 cosine-$Z_2$ スピン系 — 周期外場と応答モード](/notes/ising-r1-periodic-field) | 1 | periodic + field | $R=1$ | cosine | $Z_2$ | wall + absolute-spin response |
| model | [1次元一様第二近接 cosine-$Z_2$ スピン系 — 振動相関と有限波数応答](/notes/ising-r2-transfer-matrix) | 1 | uniform | $R=2$ | cosine | $Z_2$ | interacting wall pattern |
| model | [1次元一様有限範囲 cosine-$Z_2$ スピン系 — 高次壁相互作用と有限記憶](/notes/ising-rn-transfer-matrix) | 1 | uniform | $R=n$ | cosine | $Z_2$ | longer wall pattern |
| model | [1次元一様最近接 cosine-$Z_q$ スピン系 — 離散位相増分と角度記憶](/notes/clock-chain-nearest-neighbor) | 1 | uniform | $R=1$ | cosine | $Z_q$ | discrete phase increment |
| model | [1次元一様第二近接 cosine-$Z_q$ スピン系 — 離散螺旋と角度記憶](/notes/clock-chain-second-neighbor) | 1 | uniform | $R=2$ | cosine | $Z_q$ | locked discrete twist / chirality |
| model | [1次元一様最近接 cosine-$U(1)$ スピン系 — 位相拡散と角度記憶](/notes/xy-chain-nearest-neighbor) | 1 | uniform | $R=1$ | cosine | $U(1)$ | continuous phase increment |
| model | [1次元一様第二近接 cosine-$U(1)$ スピン系 — 螺旋的空間記憶](/notes/xy-chain-second-neighbor) | 1 | uniform | $R=2$ | cosine | $U(1)$ | correlated phase increment |
| model | [1次元一様第二近接 cosine-$U(1)$ スピン系 — chirality kinkと複数の空間記憶](/notes/xy-chain-chirality-memory) | 1 | uniform | $R=2$ | cosine | $U(1)$ | phase + chirality sector |

同じ行方向で symmetry を動かし、同じ列方向で $R$ や spatial organization を動かす、と読む。

### 4.2 coordinate bridge — 比較ノートはどの軸を横断するか

| role | 比較ノート | 固定する座標 | 動かす座標 | 接続する model point | 比較する量 |
| --- | --- | --- | --- | --- | --- |
| comparison | [1次元一様最近接 cosine スピン系 — $Z_2$・$Z_q$・$U(1)$ の空間記憶](/notes/ising-xy-nearest-neighbor-comparison) | $d=1$, uniform, $R=1$, cosine, classical | symmetry / state space | $Z_2 \leftrightarrow Z_q \leftrightarrow U(1)$ | local increment, $\rho_m$, transfer spectrum, $\xi$, $\chi(k)$ |
| comparison | [1次元一様第二近接 cosine スピン系 — $Z_2$・$Z_q$・$U(1)$ を三つの解像度で見る](/notes/ising-xy-second-neighbor-comparison) | $d=1$, uniform, $R=2$, cosine, classical | symmetry / state space | $Z_2 \leftrightarrow Z_q \leftrightarrow U(1)$ | defect / texture, local transition, transfer spectrum, pitch locking |

比較ノートは新しい model point ではなく、

$$
\boxed{
\text{coordinate bridge} = \text{一つの軸だけを動かして複数の model point を読むノート}
}
$$

とみなす。

### 4.3 現在埋まっている座標面

現在もっとも密に埋まっているのは

$$
\boxed{
d=1,\qquad
\text{uniform},\qquad
\text{cosine},\qquad
\text{classical}
}
$$

という断面である。

この断面を $R$ と symmetry で並べると、

| interaction range | $Z_2$ | $Z_q$ | $U(1)$ | 横方向の比較 |
| --- | --- | --- | --- | --- |
| $R=1$ | [model](/notes/ising-transfer-matrix) | [model](/notes/clock-chain-nearest-neighbor) | [model](/notes/xy-chain-nearest-neighbor) | [$Z_2\leftrightarrow Z_q\leftrightarrow U(1)$](/notes/ising-xy-nearest-neighbor-comparison) |
| $R=2$ | [model](/notes/ising-r2-transfer-matrix) | [model](/notes/clock-chain-second-neighbor) | [model](/notes/xy-chain-second-neighbor) / [chirality](/notes/xy-chain-chirality-memory) | [$Z_2\leftrightarrow Z_q\leftrightarrow U(1)$](/notes/ising-xy-second-neighbor-comparison) |
| $R=n$ | [model](/notes/ising-rn-transfer-matrix) | — | — | — |

この表では空欄そのものが次の学習候補になる。今回 $R=2$ の $Z_q$ が埋まったことで、

$$
\boxed{
R=1, R=2
\quad\text{では}quad
Z_2\leftrightarrow Z_q\leftrightarrow U(1)
}
$$

という symmetry 軸が二段とも閉じた。次に残る明確な空白は $R=n$ 側の $Z_q/U(1)$、または spatial organization 側の quasiperiodic / random である。

一方 spatial organization 軸は $Z_2$, $R=1$ で

| spatial organization | model |
| --- | --- |
| uniform | [1次元一様最近接 cosine-$Z_2$](/notes/ising-transfer-matrix) |
| periodic | [1次元周期最近接 cosine-$Z_2$](/notes/ising-r1-periodic) |
| quasiperiodic | — |
| random | — |

となっている。

したがって現在のノート群は、

$$
\boxed{
\text{model point}
+
\text{coordinate bridge}
+
\text{empty coordinate}
}
$$

の三種類で読むことができる。

空いている座標を見れば「次にどの軸を一つ動かすか」が決まり、comparison がある場所では「その変形によって何が変わったか」を同じ物理量で追える。

---

## 5. 比較ノートは座標間の辞書として使う

比較ノートでは詳細導出を繰り返さず、個別模型ノートですでに得た量を共通座標へ写す。

最近接 comparison なら、

$$
\boxed{
Z_2
\to
Z_q
\to
U(1)
}
$$

に対して

$$
\boxed{
\phi_i
\to
\rho_m
\to
\lambda_m/\lambda_0
\to
\xi_m
\to
\chi(k)
}
$$

という共通辞書を使う。

第二近接 comparison でも、

$$
\boxed{
Z_2
\to
Z_q
\to
U(1)
}
$$

を横断しながら、

$$
\boxed{
\text{interacting wall / locked twist / helix}
\longleftrightarrow
\text{local transition probability}
\longleftrightarrow
\text{transfer spectrum}
}
$$

という三つの information filter を対応させる。ここでは finite-$q$ 固有の pitch locking が、離散 defect と continuous texture の間を埋める。

したがって比較ノートの役割は

$$
\boxed{
\text{model A の式}
\leftrightarrow
\text{共通物理量}
\leftrightarrow
\text{model B の式}
}
$$

を作ることであり、独立した模型を一つ増やすことではない。

---

## 6. approximation / representation は information filter

mean field、Bethe/cavity、transfer matrix/operator は model coordinates の第四軸ではない。

同じ模型に対して、どの自由度を残して見るかが異なる。

$$
\boxed{
\text{approximation / representation} = \text{information filter}
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
\xi^{-1} = -\ln\left|
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

## 7. 各ノートは同じ読み順を通る

タイトルだけで座標を揃えても、ノートごとに議論の入口と出口が違うと比較しにくい。節数や固有の話題は揃えず、すべての個別模型ノートが次の spine を通るようにする。

$$
\boxed{
\text{具体的な違和感・問い}
\to
\text{系の座標と Hamiltonian}
\to
\text{局所 memory variable}
\to
\text{長距離 memory / transfer spectrum}
\to
\text{観測量・response}
\to
\text{隣接する座標との比較}
\to
\text{得られた見方}
}
$$

### 座標と Hamiltonian

導入の直後に

$$
(d,\ \text{spatial organization},\ R,\ \text{interaction family},\ \text{state space / symmetry})
$$

を明示し、その座標だけでは決まらない具体的 Hamiltonian も置く。

現在の基準系列なら

$$
H=-J\sum_i\cos(\theta_{i+1}-\theta_i)
$$

まで書き、さらに $\theta_i$ の取りうる集合を $Z_2$、$Z_q$、$U(1)$ のどれかとして明示する。これで symmetry だけでは一意でない Hamiltonian の曖昧さを消す。

### 局所 memory variable

元の spin 変数をそのまま追うのではなく、その座標で自然な局所増分を先に探す。

$$
Z_2:\quad \tau_i=s_i s_{i+1},
$$

$$
Z_q,\ U(1):\quad \phi_i=\theta_{i+1}-\theta_i.
$$

interaction range や spatial organization を変えたとき、最初に「この局所変数の独立性・遷移則・重みのどれが変わったか」を読む。

### 長距離 memory

局所則をそのまま終点にせず、

$$
C(r),\qquad
\lambda_n/\lambda_0,\qquad
\xi,\qquad
q_{\rm spec}
$$

へつなぐ。

$$
\boxed{
\text{local rule}
\longrightarrow
\text{transfer object}
\longrightarrow
\text{long-distance memory}
}
$$

が各ノートの共通骨格になる。

### 観測量・response

長距離 memory が何として観測されるかを分ける。

$$
\chi(q),\qquad
S(q),\qquad
q_\chi,\qquad
Q_{\rm peak}
$$

などは transfer spectrum と同じ量ではない。各ノートで「内部 spectrum」と「外から読む observable」を区別する。

### 隣接する座標との比較

最後に必ず、一つだけ座標を変えた隣の系と比較する。

$$
R=1\leftrightarrow R=2,
$$

$$
Z_2\leftrightarrow Z_q\leftrightarrow U(1),
$$

$$
\text{uniform}\leftrightarrow\text{periodic}\leftrightarrow\text{quasiperiodic}
$$

のように、一度に複数軸を動かさない。

章末は generic な「まとめ」ではなく

$$
\boxed{\text{得られた見方}}
$$

または、その座標から自然に残る問いで閉じる。

比較ノートは少し役割が異なり、

$$
\boxed{
\text{固定する座標}
\to
\text{比較する memory variable / filter}
\to
\text{共通量}
\to
\text{差が現れる量}
}
$$

の順にする。個別導出は繰り返さない。

---

## 8. 今どの軸まで埋まっているか

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

## 9. その先に残る二つの方向

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
(\text{state space / symmetry},\ R,\ \text{spatial organization})
\quad [\text{cosine family fixed}]
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

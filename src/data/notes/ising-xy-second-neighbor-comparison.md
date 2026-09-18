---
title: "1次元一様第二近接 cosine スピン系 — Z2・Zq・U(1)を三つの解像度で見る"
summary: "第二近接 cosine スピン系を、Z2・Zq・U(1)という局所状態空間の違いだけを動かして比較する。interacting wall、locked 離散ねじれ、連続らせんを、saddle point、局所遷移、転送スペクトルという三つの解像度で対応づける。"
publishedAt: 2026-09-13T22:45:00+09:00
updatedAt: 2026-09-19
area: "Physics"
topics: ["spin model", "clock model", "Ising model", "XY model", "second-neighbor interaction", "chirality", "転送行列"]
status: growing
system:
  dimension: 1
  spatial: uniform
  range: R2
  interaction: cosine
  対称性: [Z2, Zq, U(1)]
  mechanics: classical
  role: 比較
---

第二近接 cosine 系では

$$
\boxed{
H=
-J_1\sum_i\cos(\theta_{i+1}-\theta_i)
-J_2\sum_i\cos(\theta_{i+2}-\theta_i)
}
$$

を固定したまま、

$$
\boxed{
Z_2
\longrightarrow
Z_q
\longrightarrow
U(1)
}
$$

と local 状態空間 だけを変えられる。

個別導出は

- [第二近接 cosine-$Z_2$](/notes/ising-r2-transfer-matrix)
- [第二近接 cosine-$Z_q$](/notes/clock-chain-second-neighbor)
- [第二近接 cosine-$U(1)$](/notes/xy-chain-second-neighbor)

に分け、このノートでは三者を同じ解像度で比較する。

## 比較座標

固定するのは

$$
\boxed{
(d=1,\ \text{uniform},\ R=2,\ \text{cosine},\ \text{classical})
}
$$

である。

動かすのは

状態空間 / 対称性 だけで、

$$
Z_2
\leftrightarrow
Z_q
\leftrightarrow
U(1)
$$

を比較する。

共通の読み順は

$$
\boxed{
\text{defect / texture}
\longleftrightarrow
\text{局所遷移 rule}
\longleftrightarrow
\text{転送スペクトル}
}
$$

である。

## 1. 局所相対変数は三者で同じ形に統一できる

$\phi_i=\theta_{i+1}-\theta_i$ と置けば、

$$
\boxed{
H=
-J_1\sum_i\cos\phi_i
-J_2\sum_i\cos(\phi_i+\phi_{i+1})
}
$$

である。

違うのは $\phi_i$ の状態空間だけで、

$$
\phi_i\in
\begin{cases}
\{0,\pi\}, & Z_2,\\[1mm]
\left\{\dfrac{2\pi a}{q}\right\}, & Z_q,\\[3mm]
S^1, & U(1).
\end{cases}
$$

したがって $R=2$ の本質は三者とも

$$
\boxed{
\text{independent local increment}
\longrightarrow
\text{interacting local increment}
}
$$

である。

## 2. 実空間の構造は wall → locked twist → 連続らせん と変わる

### $Z_2$

$\tau_i=e^{i\phi_i}=\pm1$ とすれば

$$
\boxed{
H=
-J_1\sum_i\tau_i
-J_2\sum_i\tau_i\tau_{i+1}
}
$$

であり、第二近接相互作用は 壁配置 を相互作用させる。

### $Z_q$

$\phi_i=2\pi a_i/q$ なので、一様 twist の候補も離散的である。

$$
\boxed{
q_\ast^{(q)} = \frac{2\pi a_\ast}{q}
}
$$

は

$$
a_\ast = \operatorname*{arg\,min}_{a\in\mathbb Z_q}
\left[
-J_1\cos\frac{2\pi a}{q}
-J_2\cos\frac{4\pi a}{q}
\right]
$$

で決まる。

したがって preferred pitch は staircase 状にロックされる。

### $U(1)$

連続角度では

選好ねじれ は $\cos q_\ast=-J_1/(4J_2)$ に従って連続的に動く。

三者を並べると

$$
\boxed{
\text{相互作用する壁}
\to
\text{locked 離散ねじれs}
\to
\text{連続らせん}
}
$$

となる。

## 3. chirality の出方も 状態空間 に沿って連続化する

非零 選好ねじれ があると、

$+q_\ast$ と $-q_\ast$ という二つの向きが生じる。

$Z_2$ では角度 alphabet が二値なので、独立な continuous chirality sector は持たない。

$Z_q$ では

$$
\boxed{
+q_\ast^{(q)}
\leftrightarrow
-q_\ast^{(q)}
}
$$

という離散 chirality sector が現れる。

$U(1)$ ではその sector の内部に continuous phase fluctuation も残る。

したがって

$$
\boxed{
\text{壁配置}
\to
\text{discrete chirality + locked twist}
\to
\text{continuous phase + chirality}
}
$$

という階層になる。

## 4. saddle point は「どの局所構造が選ばれるか」を見る

三者で saddle-point 的に見る量は異なる。

| 対称性 | saddle-point / energetic object |
| --- | --- |
| $Z_2$ | wall cost / 壁配置 |
| $Z_q$ | locked 選好ねじれ $q_\ast^{(q)}$ |
| $U(1)$ | continuous 選好ねじれ $q_\ast$ / chirality kink |

$Z_q$ では特に

$$
\boxed{
\delta q_{\rm lock} = q_\ast^{(q)}-q_\ast
}
$$

が finite-$q$ 固有の量になる。

これは最近接 $Z_q$ にはなかった、第二近接だからこそ現れる angular discretization の効果である。

## 5. 局所遷移 は 2-state → q-state → continuous kernel へ移る

第二近接では $\phi_i$ は マルコフ連鎖 になる。

### $Z_2$

2-state transition $P(\tau_{i+1}\mid\tau_i)$ である。

### $Z_q$

$$
\boxed{
P(a_{i+1}|a_i),
\qquad
a_i\in\mathbb Z_q
}
$$

という $q$-state transition になる。

### $U(1)$

continuous conditional density $P(\phi_{i+1}\mid\phi_i)$ になる。

したがって

$$
\boxed{
2\text{-state Markov}
\to
q\text{-state Markov}
\to
\text{continuous Markov kernel}
}
$$

と連続化する。

## 6. transfer object も 2×2 → q×q → integral operator になる

increment 表示で対称分割すると、

$$
T_{ab} = \exp\left[
\frac{\beta J_1}{2}
(\cos\phi_a+\cos\phi_b)
+
\beta J_2\cos(\phi_a+\phi_b)
\right].
$$

$Z_2$ では $2\times2$、

$Z_q$ では $q\times q$ の有限行列、

$U(1)$ では $\mathcal T(\phi,\phi')$ という積分作用素になる。

$$
\boxed{
2\times2
\to
q\times q
\to
\text{integral operator}
}
$$

は state-space continuum limit の transfer-space 表現である。

## 7. 長距離 memory は三者とも spectrum の大きさと位相で読める

長距離相関を担う tilted transfer object の支配固有値を

$\Lambda_\ast=|\Lambda_\ast|e^{iq_{\rm corr}}$ とすれば、

$$
\boxed{
\xi^{-1} = -\ln\left|
\frac{\Lambda_\ast}{\Lambda_0}
\right|
}
$$

と

$$
\boxed{
q_{\rm corr} = \arg\Lambda_\ast
}
$$

が得られる。

したがって全て

$$
\boxed{
|\Lambda_\ast|
\longrightarrow
\text{memory length},
\qquad
\arg\Lambda_\ast
\longrightarrow
\text{memory phase}
}
$$

という共通言語で比較できる。

## 8. 「構造波数」は三者で同じ名前でも同じ量ではない

$Z_2$ では $q_{\rm spec}$ が subleading eigenvalue の位相として現れ、$q_\chi$ は 応答 peak の位置である。

$Z_q$ では

$$
\boxed{
q_\ast^{(q)},
\qquad
q_{\rm corr},
\qquad
Q_{\rm peak}
}
$$

を分ける必要がある。

$U(1)$ でも

$$
q_\ast,\qquad
q_{\rm corr},\qquad
Q_{\rm peak}
$$

は原理的に別である。

比較すると、

| 対称性 | local energetic pitch | long-distance pitch | 応答 peak |
| --- | --- | --- | --- |
| $Z_2$ | 壁配置 / ground-state modulation | $q_{\rm spec}$ | $q_\chi$ |
| $Z_q$ | $q_\ast^{(q)}$ | $q_{\rm corr}$ | $Q_{\rm peak}$ |
| $U(1)$ | $q_\ast$ | $q_{\rm corr}$ | $Q_{\rm peak}$ |

となる。

## 9. finite-$q$ は二つの意味で中間にいる

最近接 $R=1$ の $Z_q$ では finite-$q$ 性は主に

$$
\boxed{
\text{angular discretization}
\longleftrightarrow
\text{spectral aliasing}
}
$$

に現れた。

第二近接ではさらに

$$
\boxed{
\text{angular discretization}
\longrightarrow
\text{pitch locking}
}
$$

が加わる。

したがって $R=2$ の $Z_q$ は

$$
\boxed{
\text{spectral interpolation}
+
\text{spatial-structure quantization}
}
$$

という二重の役割を持つ。

## 10. 三つの 情報フィルター を並べる

| 解像度 | $Z_2$ | $Z_q$ | $U(1)$ |
| --- | --- | --- | --- |
| energetic / saddle point | wall cost / 壁配置 | locked twist $q_\ast^{(q)}$ | continuous $q_\ast$ / chirality kink |
| 局所遷移 | $P(\tau'|\tau)$ | $P(a'|a)$ | $P(\phi'|\phi)$ |
| transfer object | $2\times2$ | $q\times q$ | integral operator |
| long-distance memory | $(\xi,q_{\rm spec})$ | $(\xi,q_{\rm corr})$ | $(\xi,q_{\rm corr})$ |
| 応答 | $q_\chi$ | $Q_{\rm peak}$ | $Q_{\rm peak}$ |

この表で $Z_q$ は単なる「中間モデル」ではなく、

$$
\boxed{
\text{discrete defect statistics}
\leftrightarrow
\text{continuous texture statistics}
}
$$

を有限状態 マルコフ連鎖 でつなぐ位置にいる。

## 11. $q\to\infty$ で消えるものと残るもの

$q\to\infty$ では $\Delta\phi=2\pi/q\to0$ なので twist locking は消え、$q_\ast^{(q)}\to q_\ast$ となる。

一方、

$$
\text{選好ねじれ},
\qquad
\text{chirality},
\qquad
\text{correlated increments}
$$

そのものは残る。

つまり continuum limit で消えるのは

$$
\boxed{
\text{角度の離散化によるロッキング}
}
$$

であって、第二近接が作った構造記憶ではない。

## 得られた見方

第二近接 cosine 系の 対称性 軸は

$$
\boxed{
Z_2
\to
Z_q
\to
U(1)
}
$$

に沿って

$$
\boxed{
\text{相互作用する壁}
\to
\text{locked 離散ねじれs}
\to
\text{連続らせん}
}
$$

と変化する。

同時に 情報フィルター 側では

$$
\boxed{
2\text{-state transition}
\to
q\text{-state transition}
\to
\text{continuous kernel}
}
$$

となり、transfer object も

$$
\boxed{
2\times2
\to
q\times q
\to
\text{integral operator}
}
$$

へ連続化する。

したがって $R=2$ に $Z_q$ を入れることで、$Z_2$ と $U(1)$ の差を「離散か連続か」で終わらせず、**角度分解能が 壁配置 を locked twist へ、さらに 連続らせん へどう変形するか**として追えるようになる。

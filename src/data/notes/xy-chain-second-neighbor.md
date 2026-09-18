---
title: "1次元一様第二近接 cosine-U(1) スピン系 — 螺旋・カイラリティ相関と応答"
summary: "第二近接相互作用を持つ1次元U(1) cosineスピン鎖を、相互作用する位相増分、有限ねじれ、連続場、螺旋相関、カイラリティキンク、転送作用素、複数の相関長、一様・周期・回転外場への応答まで一つの模型ノートとして整理する。"
publishedAt: 2026-09-13T22:40:00+09:00
updatedAt: 2026-09-19
area: "Physics"
topics: ["statistical mechanics", "XY model", "second-neighbor interaction", "frustration", "helical order", "chirality", "correlation", "transfer operator", "linear response"]
status: growing
system:
  dimension: 1
  spatial: uniform
  range: R2
  interaction: cosine
  symmetry: [U(1)]
  mechanics: classical
  role: model
---

最近接XY鎖では

$$
\phi_i=\theta_{i+1}-\theta_i
$$

が独立で、遠距離の角度は独立な小回転の和として位相拡散した。

第二近接を加えると

$$
\boxed{
\text{independent 位相増分}
\longrightarrow
\text{相互作用する位相増分}}
$$

となる。

変わるのは相関長だけではない。相互作用自身が有限の回転率を選び、相関と外場応答の中心波数を $q=0$ からfinite-$q$へ移す。

以下では

$$
\beta\equiv\frac{1}{k_{\mathrm B}T},
\qquad
K_1=\beta J_1,
\qquad
K_2=\beta J_2
$$

とする。

## 系の座標

$$
\boxed{
(d=1,\ \text{uniform},\ R=2,\ \text{cosine},\ U(1))
}
$$

Hamiltonian は

$$
H = -J_1\sum_i\cos(\theta_{i+1}-\theta_i)
-J_2\sum_i\cos(\theta_{i+2}-\theta_i),
$$

局所変数 は

$$
\phi_i=\theta_{i+1}-\theta_i.
$$

$R=1$ で独立だった 位相増分 が、$R=2$ で隣接増分 の相関と 有限ねじれ を持つようになる。

## 1. 第二近接は隣接する角度増分を直接結ぶ

$$
H
=-J_1\sum_i\cos(\theta_{i+1}-\theta_i)
-J_2\sum_i\cos(\theta_{i+2}-\theta_i)
$$

に対して

$$
\theta_{i+2}-\theta_i
=\phi_i+\phi_{i+1}
$$

なので

$$
\boxed{
H
=-J_1\sum_i\cos\phi_i
-J_2\sum_i\cos(\phi_i+\phi_{i+1})}
$$

となる。

最近接で独立だった位相増分は、一段の空間相関を持つ相関増分へ変わる。

## 2. $\kappa=1/4$ で一様状態から有限ねじれが分岐する

競合する場合として

$$
J_1>0,
\qquad
J_2<0,
\qquad
\kappa\equiv\frac{|J_2|}{J_1}
$$

を考える。一様ねじれ $\phi_i=q$ なら、1サイトあたりのエネルギーは

$$
e(q)
=-J_1\cos q+\kappa J_1\cos2q
$$

である。

極値条件は

$$
\frac{de}{dq}
=J_1\sin q-2\kappa J_1\sin2q
$$

すなわち

$$
\boxed{
\sin q\left(1-4\kappa\cos q\right)=0}
$$

となる。

$q=0$ のほかに有限ねじれ解が存在するためには

$$
\cos q=\frac{1}{4\kappa}
$$

が実数解を持つ必要がある。したがって

$$
\kappa\ge\frac14
$$

が必要になる。

同時に $q=0$ の曲率は

$$
e''(0)=J_1(1-4\kappa)
$$

なので、$\kappa>1/4$ では一様状態そのものが不安定になる。したがって選ばれるねじれは

$$
\boxed{
q_\ast=
\begin{cases}
0, & \kappa\le 1/4,\\[4pt]
\pm\arccos\left(\dfrac{1}{4\kappa}\right), & \kappa>1/4.
\end{cases}}
$$

となる。

![第二近接XY鎖の選択ねじれと低温stiffness](/figures/xy-second-neighbor/preferred-twist-stiffness.svg)

*有限ねじれは $\kappa=1/4$ から立ち上がり、同じ点で $q=0$ の曲率がsoftになる。*

最近接XYの $q_\ast=0$ に対して、第二近接では相互作用自身が構造波数を選んでいる。

## 3. 連続場は格子模型の長波長展開として出る

$\kappa=1/4$ の近傍では $q_\ast\to0$ なので、局所ねじれ $\phi_i$ 自体が小さく、かつカイラリティ壁のような構造は多数の格子点にまたがってゆっくり変化する。この領域では

$$
\phi_i\longrightarrow\phi(x),
\qquad
\phi_{i+1}=\phi(x+1)
$$

とみなし、格子模型を長波長展開できる。

まず空間的に一様な部分は

$$
V(\phi)
=-J_1\cos\phi+\kappa J_1\cos2\phi
$$

である。$\phi\ll1$ として

$$
V(\phi)
=\text{const}
+J_1\left[
\left(\frac12-2\kappa\right)\phi^2
+
\left(-\frac1{24}+\frac{2\kappa}{3}\right)\phi^4
+\cdots
\right].
$$

$$
\kappa=\frac14+\delta,
\qquad
0<\delta\ll1
$$

とおけば、主要項は

$$
V(\phi)
\simeq
J_1\left[-2\delta\phi^2+\frac18\phi^4\right]
$$

であり、定数を除いて

$$
\boxed{
V(\phi)
=\frac{J_1}{8}
\left(\phi^2-8\delta\right)^2}
$$

と書ける。

二つの極小は

$$
\boxed{
\phi=\pm\sqrt{8\delta}}
$$

である。一方、格子模型の厳密な一様ねじれ

$$
q_\ast=\arccos\left(\frac{1}{4\kappa}\right)
$$

を $\delta\ll1$ で展開すると

$$
q_\ast\simeq\sqrt{8\delta}
$$

となり、二重井戸の極小位置と一致する。

空間変化のコストも元の格子模型から出る。小さな $\phi_i$ の二次部分をFourier空間で書くと

$$
H_2
=\frac12\sum_k A(k)|\phi_k|^2,
$$

$$
A(k)
=J_1\left[1-2\kappa-2\kappa\cos k\right].
$$

小波数では

$$
A(k)
\simeq
J_1\left[1-4\kappa+\kappa k^2\right].
$$

$k^2|\phi_k|^2$ は実空間では $(\partial_x\phi)^2$ に対応するので、臨界点近傍の有効汎関数は

$$
\boxed{
F[\phi]
=\int dx\left[
\frac{J_1\kappa}{2}(\partial_x\phi)^2
+
\frac{J_1}{8}(\phi^2-8\delta)^2
\right]}
$$

となる。

これは独立に仮定したLandau自由エネルギーではなく、**元の格子ハミルトニアンを小振幅・長波長で展開した有効場**である。ただし、この $F[\phi]$ の極値をEuler--Lagrange方程式で求め、熱揺らぎをその周りの補正として扱う段階では、場の経路積分を鞍点で置き換えている。その意味で kink の古典解は **Landau--Ginzburg型の平均場、より正確には鞍点近似**に相当する。

したがってここで使う近似は

$$
\boxed{
\text{small amplitude}
+\text{long wavelength}
+\text{鞍点}}
$$

の三段階に分けて考える方がよい。

## 4. 位相拡散 は drift + correlated diffusion へ変わる

一つのカイラリティセクターで

$$
\phi_i=q_\ast+\delta_i
$$

と書けば

$$
\theta_r-\theta_0
=q_\ast r+
\sum_{i=0}^{r-1}\delta_i.
$$

したがって

$$
\boxed{
\text{位相拡散}
\longrightarrow
\text{drift}+\text{correlated diffusion}}
$$

となる。

平均角度は一定速度 $q_\ast$ で回転し、その上に相関した熱揺らぎが重なる。

## 5. 低温位相相関は ねじれ stiffness で決まる

$\phi_i=q_\ast+\delta_i$ として二次まで展開すると

$$
H_2
=\frac12\sum_i
\left[
J_1\cos q_\ast\,\delta_i^2
+J_2\cos2q_\ast(\delta_i+\delta_{i+1})^2
\right].
$$

Fourier空間では

$$
H_2=\frac12\sum_kA(k)|\delta_k|^2
$$

で

$$
\boxed{
A(k)=J_1\cos q_\ast
+2J_2\cos2q_\ast(1+\cos k)}
$$

となる。

長距離を支配する $k\to0$ stiffness は

$$
\boxed{
A_0
=J_1\cos q_\ast+4J_2\cos2q_\ast
=e''(q_\ast)}
$$

である。

単一カイラリティセクターでは

$$
\left\langle
(\theta_r-\theta_0-q_\ast r)^2
\right\rangle
\simeq r\frac{k_{\mathrm B}T}{A_0}
$$

より

$$
\boxed{
C(r)
\sim
\cos(q_\ast r)e^{-r/\xi_{\rm ph}},
\qquad
\xi_{\rm ph}\simeq\frac{2A_0}{k_{\mathrm B}T}=2\beta A_0}
$$

となる。

$\kappa=1/4$ では $A_0\to0$ なので、このGaussian近似自体がsoftになる。境界近傍では前節の高次項が必要になる。

## 6. 有限ねじれ は離散カイラリティを同時に生む

$e(q)=e(-q)$ なので

$$
\boxed{+q_\ast\quad\text{と}\quad-q_\ast}
$$

が縮退する。

局所カイラリティは

$$
\kappa_i^{\rm ch}
\sim\sin(\theta_{i+1}-\theta_i)
=\sin\phi_i
$$

で見られる。

有限温度では $+q_\ast$ と $-q_\ast$ の領域の間にカイラリティ壁が入りうるため、相関減衰には

$$
\boxed{
\text{連続位相揺らぎ}
+\text{離散カイラリティ反転}}
$$

という二層がある。

## 7. $q_{\rm corr}$ と $\xi$ は別の相関情報である

長距離相関を

$$
C(r)
\sim e^{-r/\xi}\cos(q_{\rm corr}r+\delta)
$$

と書けば

$$
\boxed{q_{\rm corr}:\ \text{どの回転率を覚えているか}}
$$

$$
\boxed{\xi:\ \text{その回転情報をどこまで覚えているか}}
$$

となる。

低温でカイラリティが十分長く保たれるなら $q_{\rm corr}\simeq q_\ast$ である。ただし全系ではカイラリティ correlation lengthも別に存在しうるため、単一の $\xi$ で全距離を閉じるとは限らない。

## 8. 転送作用素 は角度増分の マルコフ核 になる

角度差表示では

$$
\boxed{
\mathcal T(\phi,\phi')
=\exp\left[
\frac{\beta J_1}{2}(\cos\phi+\cos\phi')
+\beta J_2\cos(\phi+\phi')
\right]}
$$

と取れる。

最近接では独立だった $\phi_i$ が、第二近接では

$$
P(\phi_{i+1}|\phi_i)
$$

というMarkov過程になる。

最近接での

$$
I_m(K_1)/I_0(K_1)
$$

という単純な1-step 履歴は、一般の転送作用素スペクトルへ置き換わる。

## 9. スピン相関は 傾斜スペクトル の位相と絶対値を読む

$$
\left\langle e^{i(\theta_r-\theta_0)}\right\rangle = \left\langle\prod_{j=0}^{r-1}e^{i\phi_j}\right\rangle
$$

なので、平衡核だけでなく位相因子を組み込んだ 傾斜転送作用素 が自然になる。

支配固有値を

$$
\Lambda_\ast=|\Lambda_\ast|e^{iq_{\rm corr}}
$$

と書けば

$$
C(r)
\sim
\left|\frac{\Lambda_\ast}{\Lambda_0}\right|^r
\cos(q_{\rm corr}r+\delta)
$$

であり

$$
\boxed{
\xi^{-1}
=-\ln\left|\frac{\Lambda_\ast}{\Lambda_0}\right|,
\qquad
q_{\rm corr}=\arg\Lambda_\ast}
$$

となる。

第二近接XYでは、長距離相関が スペクトルの**大きさと位相**の二つへ分かれている。

## 10. 外場応答の中心は $Q=0$ から $Q=\pm q_{\rm corr}$ へ移る

固定方向の空間変調外場

$$
H_h=-\sum_i h_i\cos\theta_i,
\qquad
h_i=h_Q\cos(Qi)
$$

に対して

$$
\delta m_x(Q)=\chi_{xx}(Q)h_Q.
$$

零外場では

$$
\chi_{xx}(r)
=\frac{\beta}{2}C(r).
$$

したがって

$$
C(r)\sim e^{-|r|/\xi}\cos(q_{\rm corr}r)
$$

なら概念的に

$$
\boxed{
\chi_{xx}(Q)
\propto
\frac{\xi}{1+\xi^2(Q-q_{\rm corr})^2}
+
\frac{\xi}{1+\xi^2(Q+q_{\rm corr})^2}}
$$

となる。

最近接強磁性XYでは $q_{\rm corr}=0$ だったが、螺旋領域では

$$
\boxed{Q\simeq\pm q_{\rm corr}}
$$

が応答ピークになる。

$$
\boxed{
\text{フィルター中心 }Q=0
\longrightarrow
\text{フィルター中心 }Q=\pm q_{\rm corr}}
$$

という質的変化である。

peak position は $q_{\rm corr}$、peak width はおおよそ $\xi^{-1}$ を測る。

## 11. 回転外場 は ピッチとカイラリティ の両方に 位相整合 する

XYでは外場自身を回転させ

$$
\mathbf h_i=h(\cos Qi,\sin Qi)
$$

とできる。

外場項は

$$
\boxed{
H_h^{\rm rot}
=-h\sum_i\cos(\theta_i-Qi)}
$$

となる。

スピンが

$$
\theta_i\simeq q_\ast i+\theta_0
$$

なら、$Q=q_\ast$ で外場とスピンの位相差は空間的にほぼ一定になる。

$$
\boxed{Q=q_\ast}
$$

は空間的な位相整合ing条件である。

さらに $Q=+q_\ast$ と $Q=-q_\ast$ は回転方向が逆なので、回転外場 は二つのカイラリティを区別できる。

固定方向のcosine外場がpitchをprobeするのに対し、回転外場は**pitchとカイラリティを同時にprobeできる**。

## 12. 第二近接XYで外場から読める三つの量

応答で分けて読みたいのは

$$
\boxed{q_{\rm corr},\qquad\xi,\qquad\text{カイラリティ}}
$$

である。

- 応答ピーク position → 構造波数 $q_{\rm corr}$
- peak width → 相関長 $\xi$
- 回転外場 の符号 → カイラリティ

第二近接XYでは外場は絶対方向を揃えるだけでなく、**内部構造波数へ照準を合わせるprobe**になる。

## 13. 最近接から第二近接への変化

最近接では

$$
\boxed{
\text{independent increments}
\to
\text{位相拡散}
\to
\chi(Q)\text{ centered at }0}
$$

だった。

第二近接では

$$
\boxed{
\text{相互作用する増分}
\to
\text{選好ねじれ}
+\text{correlated diffusion}
+\text{カイラリティ}}
$$

となり

$$
\boxed{
\chi(Q)\text{ centered near }\pm q_{\rm corr}}
$$

へ変わる。

この模型で残る中心像は、**どの回転率を選ぶか、その回転情報をどこまで保つか、どの外場波数に最も応答するか**が同じ転送スペクトルからつながることである。

## 14. カイラリティ相関を分離して見る

第二近接 (U(1)) 系では、スピン方向の相関と右巻き・左巻きの相関が同じ長さで減衰するとは限らない。ここからはカイラリティを独立した相関チャネルとして分離して読む。

### 螺旋側では カイラリティ が二重化する

一様 ねじれ $\phi_i=q$ のエネルギー密度は

$$
e(q)=-J_1\cos q-J_2\cos2q
$$

である。

$\kappa>1/4$ では

$$
\boxed{q_\ast=\arccos\frac{1}{4\kappa}}
$$

が選ばれ、$+q_\ast$ と $-q_\ast$ が縮退する。

局所 カイラリティ を

$$
\chi_i=\sin\phi_i
$$

とすれば、低温では

$$
\chi_i\simeq\pm\sin q_\ast.
$$

つまり 連続角度 の中に、右巻き・左巻きという離散自由度が現れる。

### Lifshitz点近傍では kink が広がる

$\kappa=1/4+\delta$、$\delta>0$ として $\phi\ll1$ で展開すると、連続場の自由エネルギーは

$$
F[\phi]
=\int dx\left[
\frac{B}{2}(\partial_x\phi)^2
+\frac{J_1}{8}(\phi^2-\phi_0^2)^2
\right],
$$

$$
B=J_1\kappa,
\qquad
\phi_0^2=8\delta.
$$

カイラリティキンク は

$$
\boxed{
\phi_{\mathrm k}(x)
=\phi_0\tanh\frac{x-x_0}{\ell_{\mathrm k}}
}
$$

で、

$$
\boxed{
\ell_{\mathrm k}
=\sqrt{\frac{\kappa}{2\delta}}
}
$$

となる。

kink energy は

$$
\boxed{
E_{\mathrm k}
=\frac{32\sqrt2}{3}J_1\sqrt\kappa\,\delta^{3/2}
}
$$

であり、$\kappa\simeq1/4$ では

$$
\boxed{
E_{\mathrm k}
\simeq
\frac{16\sqrt2}{3}J_1
\left(\kappa-\frac14\right)^{3/2}
}.
$$

$3/2$ 乗は barrier height $\sim\delta^2$ と kink width $\sim\delta^{-1/2}$ の積から出る。

低温で kink が希薄なら

$$
\xi_\chi\sim\exp\left(\frac{E_{\mathrm k}}{k_{\mathrm B}T}\right).
$$

一方、カイラリティ を固定したセクター 内では位相は Gaussian に拡散し、

$$
\xi_{\mathrm{ph}}
\simeq
\frac{2A_0}{k_{\mathrm B}T},
$$

$$
A_0
=J_1\left(4\kappa-\frac{1}{4\kappa}\right).
$$

したがって十分低温では

$$
\boxed{\xi_\chi\gg\xi_{\mathrm{ph}}}
$$

となりうる。

### 低温有効理論は telegraph + diffusion になる

粗視化すると

$$
\boxed{
\frac{d\theta}{dx}
=q_\ast\sigma(x)+\eta(x)
}
$$

と書ける。$\sigma=\pm1$ は カイラリティ、$\eta$ は 連続位相雑音 である。

カイラリティ flip rate を $\nu$ とすると

$$
\langle\sigma(0)\sigma(r)\rangle=e^{-2\nu r},
$$

したがって

$$
\boxed{\xi_\chi=\frac{1}{2\nu}}.
$$

位相拡散 を

$$
\left\langle
\exp\left(i\int_0^r\eta(x)dx\right)
\right\rangle
=e^{-Dr}
$$

とすると、spin correlation は

$$
C(r)=e^{-Dr}F(r)
$$

で、$F$ は

$$
F''+2\nu F'+q_\ast^2F=0
$$

を満たす。

$q_\ast>\nu$ では

$$
\boxed{
q_{\mathrm{corr}}
=\sqrt{q_\ast^2-\nu^2}
}
$$

で振動し、包絡から

$$
\boxed{
\xi_{\mathrm{spin}}^{-1}
=D+\nu
=\xi_{\mathrm{ph}}^{-1}+\frac{1}{2\xi_\chi}
}
$$

が得られる。

$q_\ast=\nu$ で oscillatory correlation が消える。この境界は局所 選好ねじれ $q_\ast$ が消えたことを意味しない。カイラリティ反転 が速くなり、長距離の位相蓄積が打ち消されただけである。

### 構造因子の peak はさらに別の波数を持つ

$D=0$ なら

$$
S(Q)
=\frac{4\nu q_\ast^2}
{(q_\ast^2-Q^2)^2+4\nu^2Q^2}.
$$

その最大位置は

$$
\boxed{
Q_{\mathrm{peak}}
=\sqrt{q_\ast^2-2\nu^2}
}
$$

である。

したがって

$$
\boxed{
Q_{\mathrm{peak}}<q_{\mathrm{corr}}<q_\ast
}
$$

となり、二峰構造が $Q=0$ に融合する条件

$$
\nu=\frac{q_\ast}{\sqrt2}
$$

と、実空間振動が消える条件

$$
\nu=q_\ast
$$

は一致しない。

つまり

$$
\frac{q_\ast}{\sqrt2}<\nu<q_\ast
$$

では、$S(Q)$ はすでに $Q=0$ 最大なのに、$C(r)$ にはまだ振動が残る。

### ordinary 転送作用素 は カイラリティ 相関 を持つ

$\phi$ を状態変数にすると、核は

$$
\mathcal T(\phi,\phi') = \exp\left[
\frac{\beta J_1}{2}(\cos\phi+\cos\phi')
+\beta J_2\cos(\phi+\phi')
\right].
$$

Fourier basis

$$
|m\rangle=\frac{e^{im\phi}}{\sqrt{2\pi}}
$$

では

$$
\boxed{
T_{mn}
=\sum_{\ell=-\infty}^{\infty}
I_{m-\ell}\left(\frac{\beta J_1}{2}\right)
I_{n+\ell}\left(\frac{\beta J_1}{2}\right)
I_\ell(\beta J_2)
}
$$

となる。

$\mathcal T$ は $\phi\to-\phi$ と可換するため 偶 / 奇セクター に分かれる。最大偶固有値を $\lambda_0$、最大奇固有値を $\lambda_\chi$ とすると

$$
\boxed{
\xi_\chi^{-1}
=-\ln\left|\frac{\lambda_\chi}{\lambda_0}\right|
}.
$$

カイラリティキンク の希薄化は、転送スペクトル では even / odd splitting の指数的小ささとして見える。

### スピン相関 は 傾斜スペクトル に入る

spin correlation は

$$
C_+(r) = \left\langle
\prod_{j=0}^{r-1}e^{i\phi_j}
\right\rangle
$$

なので、multiplication operator

$$
(\mathcal M_+f)(\phi)=e^{i\phi}f(\phi)
$$

を含む tilted operator

$$
\boxed{\mathcal T_{\mathrm{spin}}=\mathcal M_+\mathcal T}
$$

が必要になる。

支配固有値を

$$
z_\ast=|z_\ast|e^{iq_{\mathrm{corr}}}
$$

とすると

$$
\boxed{
\xi_{\mathrm{spin}}^{-1}
=-\ln\left|\frac{z_\ast}{\lambda_0}\right|
}
$$

と

$$
\boxed{q_{\mathrm{corr}}=\arg z_\ast}
$$

が同時に出る。

ordinary 転送作用素 は実対称だが、tilted operator は非Hermitianなので複素固有値を持てる。実空間振動はこの eigenphase に対応する。

### 数値走査では 相関チャネル の分離が直接見える

angle-grid 表現で同じ 積分作用素 を離散化し、$\kappa=0.5$ で走査した。

このとき

$$
q_\ast=\arccos\frac12=\frac{\pi}{3}\simeq1.0472.
$$

| $\beta J_1$ | $q_{\mathrm{corr}}$ | $Q_{\mathrm{peak}}$ | $\xi_\chi$ | $\xi_{\mathrm{spin}}$ |
| ---: | ---: | ---: | ---: | ---: |
| 4 | 1.0297 | 1.0066 | 2.44 | 3.42 |
| 6 | 1.0224 | 1.0158 | 5.38 | 6.08 |
| 8 | 1.0257 | 1.0236 | 12.57 | 10.72 |
| 10 | 1.0298 | 1.0289 | 30.68 | 17.47 |
| 12 | 1.0328 | 1.0328 | 76.82 | 25.45 |
| 16 | 1.0367 | 1.0367 | 502.14 | 41.01 |

低温へ行くと $q_{\mathrm{corr}}$ と $Q_{\mathrm{peak}}$ は $q_\ast$ に近づく一方、$\xi_\chi$ は $\xi_{\mathrm{spin}}$ よりはるかに速く伸びる。$\beta J_1=16$ では

$$
\frac{\xi_\chi}{\xi_{\mathrm{spin}}}\simeq12.2.
$$

spin direction の相関が失われても、右巻きか左巻きかという カイラリティ 相関 はさらに遠くまで残りうる。

### 同じ「波数」「相関長」に見えていたものを分ける

この模型では少なくとも

$$
\boxed{
q_\ast
=\text{局所選好ねじれ}
}
$$

$$
\boxed{
q_{\mathrm{corr}}
=\text{real-space oscillation wave number}
}
$$

$$
\boxed{
Q_{\mathrm{peak}}
=\text{structure/応答ピーク position}
}
$$

を分ける必要がある。

同様に

$$
\boxed{
\xi_{\mathrm{ph}},\qquad
\xi_\chi,\qquad
\xi_{\mathrm{spin}}
}
$$

も別の 相関チャネル である。

第二近接相互作用が作っているのは単なる 有限波数相関 ではない。連続位相拡散 に 離散カイラリティ反転 が重なり、観測量ごとに異なる スペクトル対象 が支配する構造である。


### 外場はスピン相関とカイラリティ相関を別々に選別する

固定方向の外場

$$
H_h =
-\sum_i h_i\cos\theta_i
$$

に対する線形応答はスピン相関を通じて決まり、

$$
\delta\langle\cos\theta_i\rangle =
\sum_j\chi^{\rm spin}_{ij}h_j
$$

となる。

一様外場は \(Q=0\) を、周期外場

$$
h_i=h_Q\cos(Qi+\varphi)
$$

は

$$
\boxed{
\delta\langle\cos\theta_i\rangle =
\chi^{\rm spin}(Q)h_Q\cos(Qi+\varphi)
+O(h_Q^3)
}
$$

として \(Q\) ごとのスピン相関を読む。

一方、回転外場

$$
H_{\rm rot} =
-h\sum_i\cos(\theta_i-Qi-\varphi)
$$

は螺旋位相へ直接整合し、\(Q\simeq q_{\rm corr}\) のチャネルを選択的に励起できる。

ただし通常の磁場が直接結合するのはスピン方向であって、カイラリティそのものではない。したがって

$$
\boxed{
\xi_{\rm spin}
\neq
\xi_\chi
}
$$

という二つの相関長の差は、同じ外場応答だけから自動的に同定できるわけではない。

カイラリティを直接読むには、右巻き・左巻きに非対称な摂動など、\(\kappa_i^{\rm ch}\) に共役な probe を別に導入する必要がある。

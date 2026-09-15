---
title: "第二近接IsingとXY — 平均場・Bethe・transfer spectrumで見る三つの解像度"
summary: "第二近接Ising鎖とXY鎖を、平均場・saddle point、Bethe/cavity、厳密transfer spectrumという三つの方法で比較する。欠陥の形、局所遷移確率、長距離相関の固有値がどう対応するかを通して、Isingのwall statisticsとXYのtwist・chiralityを同じ軸で整理する。"
publishedAt: 2026-09-13T22:45:00+09:00
updatedAt: 2026-09-16
area: "Physics"
topics: ["Ising model", "XY model", "second-neighbor interaction", "chirality"]
status: growing
---

第二近接Ising鎖と第二近接XY鎖は、厳密にはtransfer matrix / transfer operatorで扱える。それでも平均場やBethe/cavityを見る意味は残る。違いは精度の段階ではなく、同じ統計構造のどこを可視化するかにある。

$$
\boxed{
\text{平均場・saddle point}
\longleftrightarrow
\text{Bethe / cavity}
\longleftrightarrow
\text{exact transfer spectrum}
}
$$

平均場は「どんな欠陥・場配置が記憶を壊すか」を見せ、Bethe/cavityは「その局所遷移がどの頻度で起こるか」を見せ、transfer spectrumは「その結果として長距離相関がどう減衰するか」を厳密にまとめる。

以下では

$$
\beta\equiv\frac{1}{k_{\mathrm B}T}
$$

とする。

## 1. 第二近接は局所相対変数どうしを結ぶ

Isingでは

$$
H_{\rm I}
=-J_1\sum_i s_is_{i+1}
-J_2\sum_i s_is_{i+2}
$$

に対して

$$
\tau_i=s_is_{i+1}=\pm1
$$

とおけば

$$
s_is_{i+2}=\tau_i\tau_{i+1}
$$

だから

$$
\boxed{
H_{\rm I}
=-J_1\sum_i\tau_i
-J_2\sum_i\tau_i\tau_{i+1}}
$$

となる。

XYでは

$$
H_{\rm XY}
=-J_1\sum_i\cos(\theta_{i+1}-\theta_i)
-J_2\sum_i\cos(\theta_{i+2}-\theta_i)
$$

に対して

$$
\phi_i=\theta_{i+1}-\theta_i
$$

とおくと

$$
\theta_{i+2}-\theta_i=\phi_i+\phi_{i+1}
$$

より

$$
\boxed{
H_{\rm XY}
=-J_1\sum_i\cos\phi_i
-J_2\sum_i\cos(\phi_i+\phi_{i+1})}
$$

となる。

どちらも、最近接模型で独立だった局所相対変数が第二近接によって相互作用する。

$$
\boxed{
\text{independent local variables}
\longrightarrow
\text{interacting local variables}}
$$

という骨格は共通している。

## 2. 方法I：平均場・saddle pointは欠陥の形を見せる

平均場的な見方では、局所変数そのものより、粗視化した場とその代表配置を見る。

### Ising

$\tau_i=\pm1$ は離散変数なので、microscopicにはdomain wallの配置として見るのが自然である。粗視化したbond order $m_\tau(x)$ を導入すれば

$$
F[m_\tau]
=\int dx\left[
\frac{K}{2}(\partial_xm_\tau)^2+V(m_\tau)
\right]
$$

のようなLandau-Ginzburg型記述は書ける。

ただしIsingではwall自体が格子上の離散欠陥なので、連続profileより

$$
\boxed{
\text{wall cost と wall 配置}
}
$$

に物理が集中する。

### XY

$J_1>0$, $J_2<0$ とし

$$
\kappa\equiv\frac{|J_2|}{J_1}
$$

とおく。一様twist $\phi_i=q$ のエネルギーは

$$
e(q)=-J_1\cos q+\kappa J_1\cos2q.
$$

極値条件は

$$
\sin q\left(1-4\kappa\cos q\right)=0.
$$

$\kappa\le1/4$ では $q_\ast=0$ が安定だが、$\kappa>1/4$ では

$$
\boxed{
q_\ast=\arccos\left(\frac{1}{4\kappa}\right)}
$$

が選ばれ、

$$
+q_\ast,\qquad -q_\ast
$$

という二つのchirality sectorが生じる。

$\kappa=1/4+\delta$、$\delta>0$ を小さく取り、$\phi_i\to\phi(x)$ として小振幅・長波長展開すると

$$
F[\phi]
\simeq
\int dx
\left[
\frac{J_1\kappa}{2}(\partial_x\phi)^2
+
\frac{J_1}{8}(\phi^2-8\delta)^2
\right].
$$

ここまでは長波長展開であり、さらに

$$
\frac{\delta F}{\delta\phi}=0
$$

を解いて代表配置を選ぶ段階がsaddle-point、すなわち平均場的な扱いになる。

kink profileは

$$
\phi_{\rm k}(x)
=\phi_0\tanh\frac{x-x_0}{\ell_{\rm k}},
\qquad
\phi_0=\sqrt{8\delta}
$$

で、

$$
\ell_{\rm k}\propto\delta^{-1/2},
$$

さらに

$$
\boxed{
E_{\rm k}\propto J_1\delta^{3/2}}
$$

となる。

平均場から新しく見えるのは、相関長そのものではなく

$$
\boxed{
\text{kink barrier}
\longrightarrow
\text{rare chirality switching}}
$$

という機構と、そのbarrierのスケーリングである。

## 3. 方法II：Bethe / cavityは局所遷移確率を見せる

Bethe/cavityでは、場の代表配置ではなく条件付き確率を見る。

### Ising

$\tau_i$ 表現では

$$
P(\tau_{i+1}|\tau_i)
$$

が2状態遷移確率になる。

対称な場合を

$$
P=
\begin{pmatrix}
1-p & p\\
p & 1-p
\end{pmatrix}
$$

と書けば

$$
\langle\tau_0\tau_r\rangle=(1-2p)^r
$$

だから

$$
\boxed{
\xi_\tau^{-1}=-\ln|1-2p|}
$$

となる。

第二近接Isingは $\tau$ 表現では1次元最近接Markov鎖なので、このBethe/cavity記述は実質的にexactである。

したがってIsingでは

$$
\boxed{
\text{wall / flip probability}
\longleftrightarrow
\text{correlation length}}
$$

が直接つながる。

### XY

XYでは連続状態の条件付き分布

$$
P(\phi'|\phi)
$$

を考える。

低温の螺旋側で

$$
\phi\simeq\pm q_\ast
$$

の二領域へ粗視化すれば、chirality flip probability

$$
p_{\rm flip}
$$

を定義できる。

そのとき

$$
\boxed{
\xi_\chi^{-1}
\simeq
-\ln(1-2p_{\rm flip})}
$$

であり、$p_{\rm flip}\ll1$ なら

$$
\boxed{
\xi_\chi\simeq\frac{1}{2p_{\rm flip}}}
$$

となる。

平均場で得たkink energyとBethe/cavity側の局所確率は

$$
\boxed{
p_{\rm flip}
\sim
\exp[-\beta\Delta F_{\rm k}]}
$$

でつながる。

$E_{\rm k}$ がsaddle-pointのエネルギー障壁なのに対して、$\Delta F_{\rm k}$ はその周囲の揺らぎによるエントロピーまで含むkink自由エネルギーである。

## 4. 方法III：transfer matrix / operatorは長距離相関を厳密にまとめる

### Ising

$\tau$ 表現では

$$
T_{\tau,\tau'}
=
\exp\left[
\beta J_2\tau\tau'
+
\frac{\beta J_1}{2}(\tau+\tau')
\right]
$$

という $2\times2$ transfer matrixになる。

固有値を $\lambda_0,\lambda_1$ とすれば

$$
\boxed{
\xi_\tau^{-1}
=-\ln\left|\frac{\lambda_1}{\lambda_0}\right|}
$$

である。

Bethe/cavityに現れた $1-2p$ は、この固有値比が表す記憶率と同じ情報である。

### XY

XYでは

$$
\boxed{
\mathcal T(\phi,\phi')
=\exp\left[
\frac{\beta J_1}{2}(\cos\phi+\cos\phi')
+\beta J_2\cos(\phi+\phi')
\right]}
$$

という積分作用素になる。

chirality observable $\sin\phi$ は $\phi\to-\phi$ に対してoddなので、最大even固有値 $\lambda_0$ と最大odd固有値 $\lambda_\chi$ から

$$
\boxed{
\xi_\chi^{-1}
=-\ln\left|\frac{\lambda_\chi}{\lambda_0}\right|}
$$

を得る。

低温で

$$
\lambda_\chi\to\lambda_0
$$

となることは、二つのchirality sector間のswitchingが希薄になることと同じ情報である。

## 5. 三つの方法が見ているものは同じだが、見え方が違う

XYのchirality sectorでは

$$
\boxed{
E_{\rm k}
\longrightarrow
p_{\rm flip}
\longrightarrow
\lambda_\chi/\lambda_0
\longrightarrow
\xi_\chi}
$$

という対応がある。

Isingでは

$$
\boxed{
\text{wall cost}
\longrightarrow
p
\longrightarrow
\lambda_1/\lambda_0
\longrightarrow
\xi_\tau}
$$

となる。

ここで三つの方法の役割を分けると

| 方法 | 主に見えるもの | 強み | 弱み |
| --- | --- | --- | --- |
| 平均場・saddle point | 欠陥の形、幅、barrier | 機構とスケーリングが見える | 揺らぎを落とす |
| Bethe / cavity | 局所遷移確率 | defect frequencyへ直結する | 長いtextureの形は見えにくい |
| transfer spectrum | 長距離減衰率と波数 | 1Dでは厳密 | 機構が固有値に埋もれやすい |

したがって

$$
\boxed{
\text{平均場}<\text{Bethe}<\text{exact}
}
$$

という単純な精度序列として使うのではない。

$$
\boxed{
\text{形}
\longleftrightarrow
\text{頻度}
\longleftrightarrow
\text{長距離スペクトル}}
$$

という異なる解像度を対応させるために三つを並べる。

## 6. XYではchirality memoryとspin memoryが分裂する

XYではchirality memoryだけではspin correlationを決められない。

$$
\theta_r-\theta_0
=\sum_{i=0}^{r-1}\phi_i
$$

だから

$$
\left\langle e^{i(\theta_r-\theta_0)}\right\rangle
=
\left\langle\prod_{i=0}^{r-1}e^{i\phi_i}\right\rangle
$$

という経路積算量になる。

そのためspin correlationには、平衡transfer operatorに位相因子を組み込んだtilted operatorが必要になる。

支配固有値を

$$
z_\ast=|z_\ast|e^{iq_{\rm corr}}
$$

と書けば

$$
\boxed{
\xi_{\rm spin}^{-1}
=-\ln\left|\frac{z_\ast}{\lambda_0}\right|,
\qquad
q_{\rm corr}=\arg z_\ast}
$$

である。

低温では

$$
\phi\simeq q_\ast\sigma+\eta,
\qquad \sigma=\pm1
$$

と分けられ、

$$
\boxed{
\text{continuous phase diffusion}
+
\text{discrete chirality switching}}
$$

が同時にspin memoryを壊す。

これはIsingにはない追加構造である。

## 7. finite-$q$相関でも局所波数・相関波数・応答波数を分ける

Isingではfinite-$q$ correlationが現れても、その $q_{\rm corr}$ は離散wall・spin配置の相関波数である。

XYでは少なくとも

$$
q_\ast,\qquad q_{\rm corr},\qquad Q_{\rm peak}
$$

を区別する必要がある。

$$
\boxed{
q_\ast:\ \text{局所的にエネルギーが選ぶtwist}}
$$

$$
\boxed{
q_{\rm corr}:\ \text{実空間相関の振動波数}}
$$

$$
\boxed{
Q_{\rm peak}:\ \text{構造因子・応答の最大位置}}
$$

である。

chirality switchingが有限なら一般に

$$
Q_{\rm peak}\neq q_{\rm corr}\neq q_\ast
$$

となりうる。

## 8. 外場応答はtransfer spectrumを観測側から読む

両模型とも

$$
C(r)\sim e^{-r/\xi}\cos(q_{\rm corr}r)
$$

なら、Fourier空間では $Q\simeq\pm q_{\rm corr}$ 近傍に応答が集まる。

自然なdetuningは

$$
\boxed{
(Q-q_{\rm corr})\xi}
$$

である。

Isingでは

$$
H_h^{\rm I}
=-\sum_i h_Q\cos(Qi)s_i
$$

というscalar modulated fieldが、離散配置の相関波数をprobeする。

XYではさらに

$$
\mathbf h_i=h(\cos Qi,\sin Qi)
$$

というrotating fieldを使え、

$$
H_h^{\rm rot}
=-h\sum_i\cos(\theta_i-Qi)
$$

となる。

$Q=+q_\ast$ と $Q=-q_\ast$ は回転方向が逆なので、XYではpitchだけでなくchiralityまで直接選別できる。

## 9. IsingとXYの対応

| 観点 | Ising | XY |
| --- | --- | --- |
| 局所相対変数 | $\tau_i=s_is_{i+1}=\pm1$ | $\phi_i=\theta_{i+1}-\theta_i$ |
| 平均場で見えるもの | wall / bond-order texture | twist field / chirality kink |
| Betheで見る量 | $P(\tau'|\tau)$ | $P(\phi'|\phi)$ |
| 局所switching | wall / flip probability | chirality flip probability |
| exact transfer object | $2\times2$ matrix | integral operator |
| defect memory | $\lambda_1/\lambda_0$ | $\lambda_\chi/\lambda_0$ |
| spin correlation | ordinary spectrum | tilted spectrum |
| finite-$q$ の起源 | 離散配置 | local twist + switching |
| 追加自由度 | なし | continuous phase mode |

## 10. 三つの方法を並べる意味

厳密解があるから平均場やBetheが不要になるわけではない。厳密transfer spectrumは結果を与えるが、その固有値差が何の欠陥によって作られ、どの局所過程を通じて長距離減衰へ変換されるかは、別の表現へ移した方が見えやすい。

Isingでは

$$
\boxed{
\text{wall}
\to
\text{local flip probability}
\to
\text{transfer gap}}
$$

XYでは

$$
\boxed{
\text{chirality kink}
\to
\text{chirality switching probability}
\to
\text{even/odd transfer splitting}}
$$

となる。

さらにXYだけはその上にcontinuous phase accumulationが残るため、chirality sectorとspin sectorが分裂する。

三つの方法を並べることで、同じ第二近接相互作用がIsingではwall statisticsとして、XYではtwist・chirality・finite-$q$ responseとして現れる過程を、同じ統計構造の異なる解像度として読める。
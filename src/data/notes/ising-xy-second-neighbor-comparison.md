---
title: "第二近接IsingとXY — 欠陥・局所遷移・transfer spectrumの三つの解像度"
summary: "第二近接Ising鎖とXY鎖を、粗視化された欠陥像、Bethe/cavity型の局所遷移確率、transfer spectrumという三つの解像度で比較する。Isingではwall配置、XYではtwistとchiralityが同じ統計構造の異なる表現として現れ、有限波数相関と応答へつながる。"
publishedAt: 2026-09-13T22:45:00+09:00
updatedAt: 2026-09-15
area: "Physics"
topics: ["Ising model", "XY model", "second-neighbor interaction", "chirality"]
status: growing
---

第二近接相互作用を入れたIsing鎖とXY鎖は、局所自由度の見え方はかなり違う。それでも、同じ現象を

$$
\boxed{
\text{欠陥・粗視化像}
\longleftrightarrow
\text{局所遷移確率}
\longleftrightarrow
\text{transfer spectrum}}
$$

という三つの解像度で読むと、共通構造がはっきりする。

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

どちらも最近接模型で独立だった局所相対変数が、第二近接によって一段の空間記憶を持つ。

$$
\boxed{
\text{independent local variables}
\longrightarrow
\text{interacting local variables}}
$$

という骨格は共通している。

## 2. 第一の解像度：欠陥・粗視化像

Isingの $\tau_i$ は離散変数であり、$\tau_i=-1$ はスピン列のdomain wallに対応する。第二近接相互作用はwallの有無だけでなく、wallどうしの配置統計を変える。

したがってIsingで自然に見えるのは

$$
\boxed{
\text{wall configuration}
}
$$

である。

一方XYの $\phi_i$ は連続角度である。$J_1>0$, $J_2<0$ として

$$
\kappa\equiv\frac{|J_2|}{J_1}
$$

とおくと、一様twist $\phi_i=q$ のエネルギーは

$$
e(q)=-J_1\cos q+\kappa J_1\cos2q.
$$

極値条件は

$$
\sin q\left(1-4\kappa\cos q\right)=0
$$

であり、$\kappa>1/4$ では

$$
\boxed{
q_\ast=\arccos\left(\frac{1}{4\kappa}\right)}
$$

が選ばれる。

ここでは

$$
+q_\ast,\qquad -q_\ast
$$

という二つのchirality sectorが生じる。

XYで自然に見える欠陥は、その二つをつなぐchirality kinkである。

$$
\boxed{
\text{Ising}:\ \text{discrete wall arrangement}}
$$

$$
\boxed{
\text{XY}:\ \text{continuous twist}+\text{chirality kink}}
$$

という違いになる。

## 3. 連続場はXYのchirality kinkを可視化する

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

これは元の格子模型の長波長展開であり、ここからさらに

$$
\frac{\delta F}{\delta\phi}=0
$$

を解いて代表的な場配置を選ぶ段階がsaddle-point、すなわち平均場的な扱いに対応する。

kink profileは

$$
\phi_{\rm k}(x)
=\phi_0\tanh\frac{x-x_0}{\ell_{\rm k}},
\qquad
\phi_0=\sqrt{8\delta}
$$

で、

$$
\ell_{\rm k}\propto\delta^{-1/2}.
$$

kink energyは

$$
\boxed{
E_{\rm k}
\propto
J_1\delta^{3/2}}
$$

となる。

この表示の価値は、相関長そのものを精密に求めることより、なぜchirality memoryが長くなるのかを

$$
\boxed{
\text{kink barrier}
\longrightarrow
\text{rare switching}}
$$

として読めることにある。

Isingでも粗視化したwall密度やbond orderに対する連続場は書けるが、microscopicな自由度自体が離散なので、XYほどkink profileの連続形状に情報が集中しない。

## 4. 第二の解像度：局所遷移確率

第二近接模型は、局所相対変数のMarkov過程としても読める。

Isingでは

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
\langle\tau_0\tau_r\rangle
=(1-2p)^r
$$

なので

$$
\boxed{
\xi_\tau^{-1}
=-\ln|1-2p|}
$$

となる。

1次元最近接Markov鎖では、このBethe/cavity表現は実質的にexactである。したがってIsingでは

$$
\boxed{
\text{local flip probability}
\leftrightarrow
\text{correlation length}}
$$

が直接つながる。

XYでは連続状態の条件付き分布

$$
P(\phi'|\phi)
$$

を考える。

低温の螺旋側で

$$
\phi\simeq\pm q_\ast
$$

の二領域へ粗視化すれば、chiralityの有効遷移確率

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

となり、$p_{\rm flip}\ll1$ なら

$$
\xi_\chi\simeq\frac{1}{2p_{\rm flip}}.
$$

連続場で得た $E_{\rm k}$ と局所確率は概念的に

$$
\boxed{
p_{\rm flip}
\sim
\exp[-\beta\Delta F_{\rm k}]}
$$

で結ばれる。

ここで $\Delta F_{\rm k}$ はkinkの自由エネルギーであり、平均場的な $E_{\rm k}$ に揺らぎのエントロピー補正を含めた量である。

## 5. 第三の解像度：transfer spectrum

Isingの $\tau$ 表現では transfer matrix は

$$
T_{\tau,\tau'}
=
\exp\left[
\beta J_2\tau\tau'
+
\frac{\beta J_1}{2}(\tau+\tau')
\right]
$$

という $2\times2$ 行列になる。

固有値を $\lambda_0,\lambda_1$ とすれば

$$
\boxed{
\xi_\tau^{-1}
=-\ln\left|\frac{\lambda_1}{\lambda_0}\right|}
$$

である。

Bethe/cavityで現れた $1-2p$ は、この固有値比と同じ記憶率を表している。

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

chirality observable $\sin\phi$ は反転 $\phi\to-\phi$ に対してoddなので、最大even固有値 $\lambda_0$ と最大odd固有値 $\lambda_\chi$ から

$$
\boxed{
\xi_\chi^{-1}
=-\ln\left|\frac{\lambda_\chi}{\lambda_0}\right|}
$$

を得る。

低温で $\lambda_\chi\to\lambda_0$ となることは、二つのchirality sector間のswitchingが希薄になることと同じ情報である。

## 6. 三つの解像度は同じ量を別の言葉で読む

chirality sectorを例にすると、XYでは

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

Isingではより直接に

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

平均場・Bethe・transfer matrixのどれか一つが他より多くの情報を持つわけではない。

- 粗視化・saddle pointは、どの欠陥が記憶を壊すかを見せる。
- Bethe/cavityは、その欠陥が局所的にどの確率で現れるかを見せる。
- transfer spectrumは、それらを長距離減衰率として厳密にまとめる。

同じ現象を異なる解像度で読むことで、固有値の変化を物理的な機構へ戻せる。

## 7. XYではspin memoryがさらに別channelになる

XYではchirality memoryだけではspin correlationを決められない。

$$
\theta_r-\theta_0
=\sum_{i=0}^{r-1}\phi_i
$$

だから、spin correlationは

$$
\left\langle e^{i(\theta_r-\theta_0)}\right\rangle
=
\left\langle\prod_{i=0}^{r-1}e^{i\phi_i}\right\rangle
$$

という経路積算量になる。

したがって平衡transfer operatorに位相因子を掛けたtilted operatorが必要になる。

その支配固有値を

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

となる。

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

## 8. finite-$q$相関でも三つの波数を分ける

Isingでは有限波数相関が現れても、その $q_{\rm corr}$ は離散wall・spin配置の相関波数である。

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

## 9. 外場応答はtransfer spectrumの観測側になる

両模型とも

$$
C(r)\sim e^{-r/\xi}\cos(q_{\rm corr}r)
$$

なら、Fourier空間では $Q\simeq\pm q_{\rm corr}$ 近傍に応答が集まる。

したがって自然なdetuningは

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

## 10. IsingとXYの対応表

| 解像度 | Ising | XY |
| --- | --- | --- |
| 局所相対変数 | $\tau_i=s_is_{i+1}=\pm1$ | $\phi_i=\theta_{i+1}-\theta_i$ |
| 粗視化された構造 | wall配置 | twist field + chirality |
| 主要な欠陥 | domain wall配置の乱れ | chirality kink |
| 局所統計 | $P(\tau'|\tau)$ | $P(\phi'|\phi)$ |
| 低温switching | wall/flip probability | chirality flip probability |
| exact object | $2\times2$ transfer matrix | integral transfer operator |
| defect memory | $\lambda_1/\lambda_0$ | $\lambda_\chi/\lambda_0$ |
| spin correlation | ordinary spectrumで扱える | tilted spectrumが必要 |
| finite-$q$ の起源 | 離散配置 | local twist + switching |
| 特有の追加自由度 | なし | continuous phase mode |

## 11. 第二近接模型を見る軸

第二近接を入れたときに見るべきものは、単に「相関長がどう変わるか」ではない。

$$
\boxed{
\text{どの欠陥が記憶を壊すか}
}
$$

$$
\boxed{
\text{その欠陥が局所的にどの頻度で現れるか}
}
$$

$$
\boxed{
\text{その頻度がtransfer spectrumのどのgapになるか}
}
$$

を対応させると、IsingとXYを同じ言葉で比較できる。

Isingではこの対応がほぼ完全に離散Markov鎖へ閉じる。XYではその上にcontinuous phase accumulationが残るため、chirality sectorとspin sectorが分裂する。

この違いが、同じ第二近接相互作用からIsingではwall statistics、XYではtwist・chirality・finite-$q$ responseが現れる理由である。

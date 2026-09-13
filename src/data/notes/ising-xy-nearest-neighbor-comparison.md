---
title: "1次元最近接スピン模型 — IsingとXYから見る空間記憶"
summary: "1次元最近接Ising鎖とXY鎖を比較し、離散的domain wallと連続的phase diffusionという違いを整理したうえで、transfer spectrum、1-step memory、指数相関、相関長という共通構造を抽出する。"
publishedAt: 2026-09-13T01:50:00+09:00
updatedAt: 2026-09-13
area: "Physics"
topics: ["statistical mechanics", "Ising model", "XY model", "correlation", "transfer matrix", "memory", "nearest-neighbor"]
status: growing
---

1次元の最近接Ising鎖とXY鎖は、どちらも有限温度では長距離秩序を持たない。ところが、**秩序を失う機構は同じではない**。

以下では

$$
\boxed{\beta\equiv\frac{1}{k_{\mathrm B}T}}
$$

とする。温度依存を物理的に読む箇所では $k_{\mathrm B}T$ を明示し、計算式では $\beta J$ を用いる。

Isingではスピンは $s_i=\pm1$ しか取れず、XYでは $\mathbf S_i=(\cos\theta_i,\sin\theta_i)$ と連続角度を持つ。この違いは単なる $Z_2$ と $U(1)$ の違いではなく、遠距離の向きを失う方法そのものを変える。

## 1. Isingは稀な大きな反転、XYは至る所の小さな回転

最近接強磁性Ising鎖

$$
H_{\rm I}=-J\sum_i s_i s_{i+1}
$$

で bond 変数 $\tau_i=s_is_{i+1}$ を使うと、$\tau_i=-1$ がdomain wallである。壁1個の生成エネルギーは $2J$ なので、低温では

$$
\boxed{p_{\rm dw}\sim e^{-2\beta J}
=e^{-2J/(k_{\mathrm B}T)}}
$$

と壁が稀になる。

一方XY鎖

$$
H_{\rm XY}=-J\sum_i\cos(\theta_{i+1}-\theta_i)
$$

では角度差 $\phi_i=\theta_{i+1}-\theta_i$ を任意に小さく取れる。低温では

$$
\boxed{
\langle\phi_i^2\rangle
\simeq\frac{1}{\beta J}
=\frac{k_{\mathrm B}T}{J}}
$$

で、一つ一つのbondはほぼ整列している。しかし

$$
\theta_r-\theta_0=\sum_{i=0}^{r-1}\phi_i
$$

が空間方向にrandom walkする。

したがって

$$
\boxed{\text{Ising}:\ \text{rare localized walls}}
$$

に対して

$$
\boxed{\text{XY}:\ \text{distributed small rotations}}
$$

である。

## 2. 相関を壊す数学も違う：符号の積と位相の和

Isingでは

$$
s_0s_r=\prod_{i=0}^{r-1}\tau_i,
$$

なので、途中にあるwallの個数の偶奇が遠距離の符号を決める。これは multiplicative sign process である。

XYでは

$$
\theta_r-\theta_0=\sum_{i=0}^{r-1}\phi_i,
$$

なので、角度差は局所増分の和で作られる。これは additive phase process である。

一方は「局在した符号反転」、もう一方は「分散した位相拡散」であり、同じ1次元最近接系でも記憶喪失の仕方は大きく異なる。

## 3. それでも二点相関は1-step memoryの積になる

Isingでは外場ゼロの開鎖で各 $\tau_i$ が独立だから

$$
\boxed{
C_{\rm I}(r)
=\langle s_0s_r\rangle
=\left[\tanh(\beta J)\right]^r}.
$$

XYでは角度差が独立なので

$$
C_{\rm XY}(r)
=\left\langle e^{i(\theta_r-\theta_0)}\right\rangle
=\left\langle e^{i\phi}\right\rangle^r,
$$

かつ

$$
\left\langle e^{i\phi}\right\rangle
=\frac{I_1(\beta J)}{I_0(\beta J)}.
$$

したがって

$$
\boxed{
C_{\rm XY}(r)
=\left[\frac{I_1(\beta J)}{I_0(\beta J)}\right]^r}.
$$

両者とも

$$
\boxed{C(r)=\lambda^r}
$$

という形を持つ。$\lambda$ は「1 bond進んだときにどれだけ向きの記憶が残るか」を表す量と読める。

## 4. 相関長の形は共通だが、温度依存は模型固有である

$C(r)=\lambda^r=e^{-r/\xi}$ なら

$$
\boxed{\xi^{-1}=-\ln|\lambda|}.
$$

Isingでは

$$
\lambda_{\rm I}=\tanh(\beta J),
\qquad
1-\lambda_{\rm I}\simeq2e^{-2\beta J},
$$

したがって

$$
\boxed{
\xi_{\rm I}\simeq\frac12e^{2\beta J}
=\frac12\exp\left(\frac{2J}{k_{\mathrm B}T}\right)}.
$$

XYでは

$$
\lambda_{\rm XY}=\frac{I_1(\beta J)}{I_0(\beta J)},
\qquad
1-\lambda_{\rm XY}\simeq\frac{1}{2\beta J},
$$

したがって

$$
\boxed{
\xi_{\rm XY}\simeq2\beta J
=\frac{2J}{k_{\mathrm B}T}}.
$$

つまり

$$
\boxed{
\text{指数相関そのものは共通、相関長の温度依存は模型固有}}
$$

である。

## 5. 違いは「1-step memoryが1へ近づく仕方」に集約できる

Isingでは向きを変えるには有限エネルギー $2J$ のwallが必要なので、記憶損失率は activated に

$$
1-\lambda_{\rm I}\sim e^{-2J/(k_{\mathrm B}T)}
$$

まで小さくなる。

XYでは各bondに

$$
\phi_{\rm rms}\sim\sqrt{\frac{k_{\mathrm B}T}{J}}
$$

程度の小さな回転が常に存在する。そのため記憶損失率は

$$
1-\lambda_{\rm XY}\sim\frac{k_{\mathrm B}T}{2J}
$$

と代数的にしか小さくならない。

したがって

$$
\boxed{
\text{activated defect physics}
\quad\leftrightarrow\quad
\text{diffusive fluctuation physics}}
$$

という違いが、そのまま相関長の指数増大と $1/T$ 増大の違いになる。

## 6. transfer spectrumから見ると共通構造がさらに明確になる

Isingでは $2\times2$ transfer matrix、XYでは積分作用素を使う。しかしどちらも、最大固有値 $\lambda_0$ と観測量が結合するsectorの固有値 $\lambda_a$ の比が長距離相関を決める。

$$
\boxed{
C_a(r)\sim\left(\frac{\lambda_a}{\lambda_0}\right)^r,
\qquad
\xi_a^{-1}=-\ln\left|\frac{\lambda_a}{\lambda_0}\right|}.
$$

重要なのは行列の大きさではなく、**局所transfer ruleの反復が空間記憶を作る**ことである。

XYでは

$$
\lambda_m=2\pi I_m(\beta J),
\qquad m=0,\pm1,\pm2,\ldots
$$

と無限個のharmonic sectorがある。低温では

$$
\boxed{
\xi_m\simeq\frac{2\beta J}{m^2}
=\frac{2J}{m^2k_{\mathrm B}T}}
$$

であり、角度情報の解像度ごとに異なる記憶距離を持つ。

## 7. 最近接1次元スピン模型に共通するものはどこまで言えるか

IsingとXYを比べると、少なくとも次の構造は共通している。

- 相互作用は隣接サイト間の局所Boltzmann重みで記述される。
- 空間方向の統計はtransfer matrix / transfer operatorの反復になる。
- 長距離相関はtransfer spectrumの固有値比で決まる。
- relevantなspectral gapが有限なら相関は指数減衰する。
- 相関長は「1 stepごとの記憶損失」の累積として読める。

したがって

$$
\boxed{
\text{nearest-neighbor 1D}
\Longrightarrow
\text{local transfer rule}
\Longrightarrow
\text{spectral memory propagation}}
$$

という見方ができる。

ただし、bond変数が完全に独立になること自体はすべての最近接模型に普遍的ではない。Isingや零外場XYで成立するのは、Hamiltonianが相対変数だけで局所的に分離できるためである。より一般的なのは **transfer operatorによる局所的な情報伝播** の方である。

## 8. 外場を入れると「相対変数だけで閉じる」単純さが壊れる

Isingでは $-h\sum_i s_i$ をdomain-wall変数へ移すと非局所的になる。XYでも $-h\sum_i\cos\theta_i$ は絶対角を見るため、角度差だけでは閉じない。

つまり両者とも

$$
\boxed{
\text{interaction probes relative orientation}
\qquad
\text{field probes absolute orientation}}
$$

という共通構造を持つ。零外場で単純だった局所相対自由度の記述は、外場を入れることで崩れる。

## 9. 比較して初めて見えること

IsingとXYは、どちらも「1次元だから秩序しない」という一言で片づけると本質を失う。

Isingでは

$$
\text{rare walls}
\rightarrow
\text{exponentially long memory},
$$

XYでは

$$
\text{phase diffusion}
\rightarrow
\text{algebraically long memory}
$$

である。

それでも両者の長距離相関は local transfer rule のスペクトルで統一的に記述できる。この「模型固有の励起機構」と「最近接1次元系に共通するtransfer構造」を分けて考えることが、この比較の目的である。
---
title: "1次元最近接スピン模型 — IsingとXYから見る空間記憶"
summary: "1次元最近接Ising鎖とXY鎖を、空間記憶の失われ方・transfer spectrum・空間変調外場への応答という共通軸で比較する。domain wallとphase diffusionの違いが、相関長とqξフィルタの温度発達の違いへどうつながるかを整理する。"
publishedAt: 2026-09-13T01:50:00+09:00
updatedAt: 2026-09-13
area: "Physics"
topics: ["statistical mechanics", "Ising model", "XY model", "correlation", "transfer matrix", "memory", "nearest-neighbor", "linear response"]
status: growing
---

1次元の最近接Ising鎖とXY鎖は、どちらも有限温度では長距離秩序を持たない。しかし、その「向きを忘れる方法」は同じではない。

以下では

$$
\beta\equiv\frac{1}{k_{\mathrm B}T},
\qquad
K\equiv\beta J=\frac{J}{k_{\mathrm B}T}
$$

とする。$K$ が大きいほど低温である。

このノートで見たいのは、単に両模型の公式を並べることではない。

$$
\boxed{
\text{局所的な相互作用が、どのように空間記憶を作り、外場に対する応答へつながるか}
}
$$

を、Ising と XY の比較から整理する。

## 1. Isingは稀なwallで、XYは小さな回転の累積で向きを失う

最近接強磁性Ising鎖は

$$
H_{\mathrm I}=-J\sum_i s_i s_{i+1},
\qquad s_i=\pm1
$$

である。bond変数

$$
\tau_i=s_is_{i+1}
$$

を使うと、$\tau_i=-1$ がdomain wallに対応する。wall 1個の生成エネルギーは $2J$ なので、低温では

$$
p_{\mathrm{dw}}\sim e^{-2K}
=e^{-2J/(k_{\mathrm B}T)}
$$

となり、wall は稀になる。

一方、最近接XY鎖は

$$
H_{\mathrm{XY}}
=-J\sum_i\cos(\theta_{i+1}-\theta_i)
$$

である。角度差

$$
\phi_i=\theta_{i+1}-\theta_i
$$

は連続変数なので、低温でも各bondには小さな回転が残る。

$$
\langle\phi_i^2\rangle
\simeq\frac{1}{K}
=\frac{k_{\mathrm B}T}{J}.
$$

そして

$$
\theta_r-\theta_0
=\sum_{i=0}^{r-1}\phi_i
$$

だから、角度は空間方向にrandom walkする。

したがって最初の対比は

$$
\boxed{\text{Ising}:\ \text{rare localized walls}}
$$

に対して

$$
\boxed{\text{XY}:\ \text{distributed small rotations}}
$$

である。

Isingでは有限エネルギーの欠陥が局所的に記憶を反転させ、XYでは微小な誤差が距離とともに蓄積して記憶を失わせる。

## 2. 相関を作る数学は違うが、1-step memoryという形は共通する

Isingでは

$$
s_0s_r=\prod_{i=0}^{r-1}\tau_i
$$

なので、遠距離の符号は途中のwallの偶奇で決まる。これは multiplicative sign process である。

XYでは

$$
\theta_r-\theta_0
=\sum_{i=0}^{r-1}\phi_i
$$

なので、遠距離の角度差は局所増分の和でできる。これは additive phase process である。

ところが零外場の開鎖では、どちらも局所相対変数が独立になるため、二点相関は「1 bond進むごとの記憶保持率」の積になる。

Isingでは

$$
\boxed{
C_{\mathrm I}(r)
=\langle s_0s_r\rangle
=\left[\tanh K\right]^r
}
$$

である。

XYでは

$$
\boxed{
C_{\mathrm{XY}}(r)
=\left[
\frac{I_1(K)}{I_0(K)}
\right]^r
}
$$

となる。

したがって両者とも

$$
\boxed{C(r)=\lambda^r}
$$

と書ける。ここで $\lambda$ は、1 bond進んだときにどれだけ空間記憶が残るかを表す。

## 3. 相関長は共通の形を持つが、低温での伸び方は異なる

$C(r)=\lambda^r=e^{-r/\xi}$ と比較すれば

$$
\boxed{
\xi^{-1}=-\ln|\lambda|
}
$$

である。

Isingでは

$$
\xi_{\mathrm I}^{-1}
=-\ln(\tanh K),
$$

低温 $K\gg1$ では

$$
\boxed{
\xi_{\mathrm I}
\simeq\frac12 e^{2K}
=\frac12\exp\left(\frac{2J}{k_{\mathrm B}T}\right)
}
$$

となる。

一方XYでは

$$
\xi_{\mathrm{XY}}^{-1}
=-\ln\left[\frac{I_1(K)}{I_0(K)}\right],
$$

低温では

$$
\frac{I_1(K)}{I_0(K)}
\simeq1-\frac{1}{2K}
$$

だから

$$
\boxed{
\xi_{\mathrm{XY}}
\simeq2K
=\frac{2J}{k_{\mathrm B}T}
}
$$

となる。

したがって、指数相関そのものは共通でも、その温度依存は

$$
\boxed{
\text{Ising}:\ \text{activated growth}
\qquad
\text{XY}:\ \text{algebraic growth}
}
$$

と大きく異なる。

この差は、Isingでは稀なwallの間隔が記憶長を決め、XYでは位相拡散の分散成長が記憶長を決めることの直接的な反映である。

## 4. transfer spectrumから見ると、両者の共通骨格が見える

Isingでは$2\times2$ transfer matrix、XYでは積分作用素を使う。しかし長距離相関を決める構造は同じである。

最大固有値を $\lambda_0$、観測量が結合するsectorの固有値を $\lambda_a$ とすれば

$$
\boxed{
C_a(r)
\sim
\left(\frac{\lambda_a}{\lambda_0}\right)^r
}
$$

であり、

$$
\boxed{
\xi_a^{-1}
=-\ln\left|\frac{\lambda_a}{\lambda_0}\right|
}
$$

となる。

ここで重要なのは、行列か積分作用素かという形式の違いではない。

$$
\boxed{
\text{local transfer rule}
\Longrightarrow
\text{spectral decay}
\Longrightarrow
\text{spatial memory length}
}
$$

という構造が共通している。

XYではさらに

$$
\lambda_m=2\pi I_m(K),
\qquad m=0,\pm1,\pm2,\ldots
$$

という無限個のangular sectorがあり、低温では

$$
\xi_m\simeq\frac{2K}{m^2}
$$

となる。したがってXYでは、角度情報の解像度ごとに異なる空間記憶長が存在する。

## 5. 外場は「相対方向だけで閉じる」零外場の単純さを壊す

ここまでは零外場を見てきた。そこではIsingもXYも、相互作用は隣接サイトの相対的な向きだけを見ていた。

Isingでは $s_is_{i+1}$、XYでは $\theta_{i+1}-\theta_i$ が自然な局所変数である。

一方、外場は絶対方向を指定する。

$$
\boxed{
\text{interaction probes relative orientation}
\qquad
\text{field probes absolute orientation}
}
$$

この違いが、零外場で成立していた独立bond描像を壊す。

### Isingではdomain-wall表示が非局所化する

空間依存外場 $h_i$ を入れると

$$
H_{\mathrm I}
=-J\sum_i s_is_{i+1}
-\sum_i h_i s_i.
$$

基準スピン $s_0$ を残せば

$$
s_i=s_0\prod_{j=0}^{i-1}\tau_j
$$

だから、外場項は

$$
-\sum_i h_i s_i
=-s_0\sum_i h_i\prod_{j=0}^{i-1}\tau_j.
$$

つまり、スピン表示では局所的な外場が、wall表示では長い積になって非局所化する。

### XYでも角度差表示が非局所化する

$x$方向の外場を入れると

$$
H_{\mathrm{XY}}
=-J\sum_i\cos(\theta_{i+1}-\theta_i)
-\sum_i h_i\cos\theta_i.
$$

角度差を使えば

$$
\theta_i
=\theta_0+
\sum_{j=0}^{i-1}\phi_j
$$

なので、外場項は

$$
-\sum_i h_i
\cos\left(
\theta_0+\sum_{j=0}^{i-1}\phi_j
\right)
$$

となる。

XYでも、絶対角を測る外場を入れると角度差だけでは局所的に閉じない。

さらに零外場のtransfer kernel

$$
T_0(\theta,\theta')
=\exp[K\cos(\theta'-\theta)]
$$

では $e^{im\theta}$ が独立な固有sectorだったが、外場項の

$$
\cos\theta=\frac12(e^{i\theta}+e^{-i\theta})
$$

によって

$$
\boxed{m\longleftrightarrow m\pm1}
$$

が結合する。つまり外場は $U(1)$ symmetryを壊し、独立だったangular sectorを混ぜる。

## 6. 微小な空間変調外場は、零外場の空間記憶を読み出す

外場が微小なら、有限外場の問題を最初から解き直す必要はない。零外場相関から線形応答が得られる。

Isingでは

$$
\chi_{\mathrm I}(r)
=\beta\langle s_0s_r\rangle
=\beta[\tanh K]^{|r|}.
$$

XYの$x$成分では

$$
\chi_{\mathrm{XY}}^{xx}(r)
=\beta\langle\cos\theta_0\cos\theta_r\rangle.
$$

零外場の回転対称性から

$$
\langle\cos\theta_0\cos\theta_r\rangle
=\frac12\langle\mathbf S_0\cdot\mathbf S_r\rangle
$$

なので

$$
\boxed{
\chi_{\mathrm{XY}}^{xx}(r)
=\frac{\beta}{2}
\left[
\frac{I_1(K)}{I_0(K)}
\right]^{|r|}
}
$$

となる。

外場を

$$
h_i=h_qe^{iqi}
$$

とすれば

$$
\delta m(q)=\chi(q)h_q.
$$

Isingでは厳密に

$$
\boxed{
\chi_{\mathrm I}(q)
=\beta
\frac{1-\rho_{\mathrm I}^2}
{1-2\rho_{\mathrm I}\cos q+\rho_{\mathrm I}^2},
\qquad
\rho_{\mathrm I}=\tanh K
}
$$

である。

XYでは

$$
\boxed{
\chi_{\mathrm{XY}}^{xx}(q)
=\frac{\beta}{2}
\frac{1-\rho_{\mathrm{XY}}^2}
{1-2\rho_{\mathrm{XY}}\cos q+\rho_{\mathrm{XY}}^2},
\qquad
\rho_{\mathrm{XY}}=\frac{I_1(K)}{I_0(K)}
}
$$

となる。

長波長かつ長相関長の極限では、どちらも

$$
\chi(q)
\propto
\frac{\xi}{1+(q\xi)^2}
$$

というLorentzian型へ近づく。

したがって空間変調外場に対して自然な無次元量は

$$
\boxed{q\xi}
$$

である。

$q\xi\ll1$ では、ひとつの相関領域の内部で外場はほぼ一定なので、相関したスピン群が協調して追従できる。

$q\xi\sim1$ では、外場の空間変化と相関領域の大きさが競合する。

$q\xi\gg1$ では、ひとつの相関領域の内部で外場が何度も向きを変えるため、協調して動こうとするスピン群の応答が空間的に相殺される。

この意味で

$$
\boxed{
\xi=\text{系が協調して応答できる代表的な空間スケール}
}
$$

と読むことができる。

## 7. 同じ $q\xi$ 則でも、フィルタの温度発達はIsingとXYで違う

空間フィルタの基本構造は共通している。しかし、その幅を決める $\xi(T)$ が違うため、低温化したときの波数応答は同じではない。

クロスオーバー波数を

$$
\boxed{
q_\times(K)\equiv\frac{1}{\xi(K)}
}
$$

と定義する。

$q\ll q_\times$ なら $q\xi\ll1$ で協調応答しやすく、$q\gg q_\times$ なら短波長抑制が強くなる。

Isingでは

$$
\boxed{
q_\times^{\mathrm I}(K)
=-\ln(\tanh K)
}
$$

であり、低温では

$$
\boxed{
q_\times^{\mathrm I}(K)
\simeq2e^{-2K}
}
$$

となる。

一方XYでは

$$
\boxed{
q_\times^{\mathrm{XY}}(K)
=-\ln\left[\frac{I_1(K)}{I_0(K)}\right]
}
$$

で、低温では

$$
\boxed{
q_\times^{\mathrm{XY}}(K)
\simeq\frac{1}{2K}
}
$$

となる。

したがって、$K=\beta J$ を大きくして低温へ進むと

$$
\boxed{
\text{Ising}:\ q_\times\text{ は指数的に縮む}
}
$$

のに対し

$$
\boxed{
\text{XY}:\ q_\times\text{ は }K^{-1}\text{ で代数的に縮む}
}
$$

という違いが現れる。

![IsingとXYの空間フィルタ幅](/figures/ising-xy-comparison/qxi-temperature-filter.svg)

*クロスオーバー波数 $q_\times=\xi^{-1}$ の $K=\beta J$ 依存性。左はIsing、右はXY。青実線は厳密式、緑破線は低温漸近形。Isingでは $q_\times\sim2e^{-2K}$ と指数的に狭まり、XYでは $q_\times\sim(2K)^{-1}$ と代数的に狭まる。*

固定した波数 $q$ の外場から見れば、クロスオーバー条件は

$$
q\xi(K_\times)\sim1
$$

である。

Isingでは低温近似から

$$
q\sim2e^{-2K_\times}
$$

なので

$$
\boxed{
K_\times^{\mathrm I}
\sim\frac12\ln\left(\frac{2}{q}\right)
}
$$

となる。

XYでは

$$
q\sim\frac{1}{2K_\times}
$$

だから

$$
\boxed{
K_\times^{\mathrm{XY}}
\sim\frac{1}{2q}
}
$$

である。

つまり同じ空間波数の外場を使っても、低温化によって短波長抑制へ入る仕方はIsingとXYで大きく異なる。

## 8. 比較から見える共通構造は「1次元だから秩序しない」より具体的である

IsingとXYは、どちらも有限温度で長距離秩序を持たない。しかし、その事実だけを共通点としてしまうと物理をかなり失う。

Isingでは

$$
\text{rare walls}
\Longrightarrow
\text{activated memory loss}
\Longrightarrow
\xi\sim e^{2K},
$$

XYでは

$$
\text{phase diffusion}
\Longrightarrow
\text{diffusive memory loss}
\Longrightarrow
\xi\sim K
$$

である。

一方、長距離の記憶そのものは

$$
\boxed{
\text{local transfer rule}
\Longrightarrow
\text{spectral decay}
\Longrightarrow
\xi
\Longrightarrow
\chi(q)
}
$$

という共通の流れで整理できる。

したがって比較の要点は

$$
\boxed{
\text{同じ最近接1次元のtransfer構造を持ちながら、}
\text{記憶を失う局所機構が違うため、}\xi(T)\text{ と空間応答の温度発達が異なる}
}
$$

ということである。

外場はこの違いを壊すだけの操作ではない。空間変調を与えることで、系がどの波長まで記憶を保持できるかを読み出すprobeにもなる。
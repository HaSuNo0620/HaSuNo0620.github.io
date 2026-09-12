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

Isingではスピンは

$$
s_i=\pm1
$$

しか取れず、隣接スピンとの関係は「同じ」か「反対」の二択である。XYでは

$$
\mathbf S_i=(\cos\theta_i,\sin\theta_i)
$$

で、隣接スピンは任意に小さな角度だけずれることができる。

この違いは、単なる $Z_2$ と $U(1)$ の対称性の違いではない。遠距離の向きを失う方法そのものを変える。

このノートでは両者を比較することで、

$$
\boxed{
\text{何が模型固有で、何が1次元最近接スピン鎖に共通なのか}
}
$$

を切り分ける。

## 1. Isingは「稀な大きな反転」、XYは「至る所の小さな回転」

最近接強磁性Ising鎖は

$$
H_{\rm I}=-J\sum_i s_i s_{i+1}
$$

である。bond変数

$$
\tau_i=s_i s_{i+1}
$$

を使うと、$\tau_i=-1$ がdomain wallに対応する。壁1個の生成エネルギーは $2J$ なので、低温では

$$
p_{\rm dw}\sim e^{-2J/T}
$$

と壁が稀になる。

一方XY鎖

$$
H_{\rm XY}
=-J\sum_i\cos(\theta_{i+1}-\theta_i)
$$

では、角度差

$$
\phi_i=\theta_{i+1}-\theta_i
$$

を任意に小さく取れる。低温では

$$
\langle\phi_i^2\rangle\simeq\frac{T}{J}
$$

であり、一つ一つのbondはほぼ整列している。しかし遠距離では

$$
\theta_r-\theta_0
=\sum_{i=0}^{r-1}\phi_i
$$

がrandom walkする。

したがって、最も直接的な違いは

$$
\boxed{
\text{Ising}:\ \text{rare localized flips}
}
$$

$$
\boxed{
\text{XY}:\ \text{distributed small rotations}
}
$$

である。

## 2. 相関を壊す数学も違う：符号の積と位相の和

Isingでは

$$
s_0s_r
=\prod_{i=0}^{r-1}\tau_i
$$

なので、相関は途中にあるdomain wallの個数の偶奇を見る。

$$
\boxed{
\text{Ising}:\quad
\text{multiplicative sign process}
}
$$

である。

XYでは

$$
\theta_r-\theta_0
=\sum_{i=0}^{r-1}\phi_i
$$

なので、角度差は局所増分の和として作られる。

$$
\boxed{
\text{XY}:\quad
\text{additive phase process}
}
$$

である。

Isingでは1個の壁が符号を反転させ、XYでは多数の小さな角度ずれが累積して方向を失わせる。

## 3. それでも両者の二点相関は「1-step memoryの積」になる

違いの一方で、最近接・零外場では共通する構造がある。

Isingでは外場ゼロの開鎖で各 $\tau_i$ は独立なので、

$$
C_{\rm I}(r)
=\langle s_0s_r\rangle
=\langle\tau\rangle^r.
$$

ここで

$$
\langle\tau\rangle=\tanh(\beta J).
$$

したがって

$$
\boxed{
C_{\rm I}(r)
=\left[\tanh(\beta J)\right]^r
}
$$

となる。

XYでは角度差が独立なので、

$$
C_{\rm XY}(r)
=\left\langle e^{i(\theta_r-\theta_0)}\right\rangle
=\left\langle e^{i\phi}\right\rangle^r.
$$

1 bondについて

$$
\left\langle e^{i\phi}\right\rangle
=\frac{I_1(\beta J)}{I_0(\beta J)}
$$

だから、

$$
\boxed{
C_{\rm XY}(r)
=\left[
\frac{I_1(\beta J)}{I_0(\beta J)}
\right]^r
}
$$

となる。

つまり両者とも

$$
\boxed{
C(r)=\lambda^r
}
$$

という形を持つ。

ここで $\lambda$ は、**1 bond進んだときにどれだけ向きの記憶が残るか**を表す量と読める。

## 4. 相関長は「1-step memoryが1にどれだけ近いか」で決まる

$C(r)=\lambda^r$ なら

$$
C(r)=e^{-r/\xi}
$$

と比較して

$$
\boxed{
\xi^{-1}=-\ln|\lambda|
}
$$

である。

Isingでは

$$
\lambda_{\rm I}=\tanh(\beta J),
$$

XYでは

$$
\lambda_{\rm XY}=\frac{I_1(\beta J)}{I_0(\beta J)}.
$$

この式の形は共通だが、低温で $\lambda\to1$ へ近づく仕方が違う。

Isingでは

$$
1-\lambda_{\rm I}
\simeq2e^{-2\beta J},
$$

したがって

$$
\boxed{
\xi_{\rm I}\simeq\frac12e^{2\beta J}
}
$$

となる。

XYでは

$$
1-\lambda_{\rm XY}
\simeq\frac{1}{2\beta J},
$$

したがって

$$
\boxed{
\xi_{\rm XY}\simeq2\beta J
}
$$

となる。

つまり

$$
\boxed{
\text{指数相関そのものは共通、相関長の温度依存は模型固有}
}
$$

である。

## 5. なぜIsingだけ相関長が指数的に長くなるのか

Isingで向きを変えるには、有限エネルギー $2J$ を払ってdomain wallを作る必要がある。低温ではその確率がBoltzmann因子で

$$
e^{-2J/T}
$$

まで抑えられるため、壁間隔は指数的に長くなる。

一方XYでは、有限エネルギー障壁を越えて大きな欠陥を作る必要がない。各bondで $O(\sqrt{T/J})$ の微小回転が起こり、それが距離とともに蓄積する。

したがって

$$
\boxed{
\text{activated defect physics}
\quad\leftrightarrow\quad
\text{diffusive fluctuation physics}
}
$$

という違いが、

$$
\xi_{\rm I}\sim e^{2J/T},
\qquad
\xi_{\rm XY}\sim J/T
$$

に直接現れる。

## 6. 転送行列・転送作用素から見ると共通構造がさらに明確になる

Isingではtransfer matrixが $2\times2$ で、その最大固有値を $\lambda_0$、spin observableが結合する非自明なsectorの固有値を $\lambda_1$ とすれば

$$
C(r)\sim
\left(
\frac{\lambda_1}{\lambda_0}
\right)^r.
$$

XYではtransfer operatorの固有関数が $e^{im\theta}$ で、

$$
\lambda_m=2\pi I_m(\beta J).
$$

通常のspin相関は $m=1$ sectorなので

$$
C(r)
=\left(
\frac{\lambda_1}{\lambda_0}
\right)^r.
$$

したがって両者を一つに書けば

$$
\boxed{
C_a(r)
\sim
\left(
\frac{\lambda_a}{\lambda_0}
\right)^r
}
$$

である。

そして

$$
\boxed{
\xi_a^{-1}
=-\ln
\left|
\frac{\lambda_a}{\lambda_0}
\right|
}
$$

となる。

ここで重要なのは、行列が $2\times2$ か積分作用素かではない。**長距離の空間記憶がtransfer spectrumの固有値比で決まる**ことが共通している。

## 7. Isingはほぼ一つの非自明memory channel、XYは無限個のharmonic memoryを持つ

Isingでは局所状態が2値なので、零外場の基本的なspin相関に対応する非自明sectorは実質一つである。

XYでは

$$
m=1,2,3,\ldots
$$

の各Fourier harmonicに対して

$$
\xi_m^{-1}
=-\ln\left|
\frac{I_m(\beta J)}{I_0(\beta J)}
\right|
$$

が存在する。

低温では

$$
\xi_m\simeq\frac{2\beta J}{m^2}.
$$

つまり連続自由度を持つXYでは、単なる「向きを覚えているか」だけではなく、**どの角度分解能の情報がどこまで残るか**というmemory hierarchyが現れる。

この点は、最近接という相互作用範囲を変えず、局所状態空間だけを離散から連続へ変えた結果として読むことができる。

## 8. 最近接1次元スピン模型に共通するものはどこまで言えるか

IsingとXYを比べると、少なくとも次の構造は共通している。

- 相互作用は隣接サイト間の局所Boltzmann重みで記述される。
- 空間方向の統計はtransfer matrix / transfer operatorの反復として表せる。
- 長距離相関はtransfer spectrumの固有値比で決まる。
- 最大固有値と観測量が結合するsectorの間に有限のspectral gapがあれば、相関は指数減衰する。
- 相関長は1 stepごとの記憶損失を距離方向へ積み重ねた量として読める。

したがって

$$
\boxed{
\text{nearest-neighbor 1D}
\Rightarrow
\text{local transfer rule}
\Rightarrow
\text{spectral memory propagation}
}
$$

という見方ができる。

ただし、**bond変数が完全に独立になること自体はすべての最近接スピン模型に普遍的ではない**。Isingや零外場XYでそれが成立するのは、Hamiltonianが相対変数だけで局所的に分離できるためである。

より一般的に普遍的なのは、独立bondそのものではなく、transfer operatorによる局所的な情報伝播である。

## 9. 外場を入れると「相対変数だけで閉じる」単純さが壊れる

Isingでは外場項

$$
-h\sum_i s_i
$$

をdomain-wall変数で書くと非局所的になる。

XYでも

$$
-h\sum_i\cos\theta_i
$$

は絶対角を見るため、角度差 $\phi_i$ だけでは閉じない。

つまり両者とも

$$
\boxed{
\text{interaction is local in relative variables}
}
$$

だが

$$
\boxed{
\text{field probes absolute orientation}
}
$$

という共通構造を持つ。

外場を入れた瞬間、Isingではdomain-wallの独立性が、XYではFourier sectorの独立性が崩れる。

これは、局所相対自由度で単純化された模型に対して、外場が絶対的な向きを持ち込むためである。

## 10. 「有限温度で秩序しない」は同じ結論でも、物理は同じではない

IsingもXYも1次元・有限範囲・有限温度では長距離秩序を持たない。しかし

$$
\boxed{
\text{same asymptotic statement}
\neq
\text{same microscopic mechanism}
}
$$

である。

Isingでは

$$
\text{rare walls}
\rightarrow
\text{sign memory loss}
$$

XYでは

$$
\text{small angular noise}
\rightarrow
\text{phase diffusion}
$$

である。

この比較によって、相関長は単なる「秩序の大きさ」ではなく、**その模型で許された最小の空間揺らぎがどれだけ速く情報を失わせるか**を測っていると理解できる。

## まとめ

1次元最近接Ising鎖とXY鎖は、局所自由度も相関喪失機構も大きく異なる。

$$
\boxed{
\text{Ising}:\ \text{discrete defect}
\qquad
\text{XY}:\ \text{continuous phase diffusion}
}
$$

しかし両者の長距離相関は

$$
\boxed{
C_a(r)
\sim
\left(
\frac{\lambda_a}{\lambda_0}
\right)^r
}
$$

という同じtransfer-spectrum構造を持つ。

したがって、模型固有なのは

$$
\text{どの局所揺らぎがmemoryを壊すか}
$$

であり、より普遍的なのは

$$
\boxed{
\text{local transfer rule}
\rightarrow
\text{spectral decay}
\rightarrow
\text{correlation length}
}
$$

という空間記憶の伝播構造である。

IsingとXYを並べることで、1次元最近接スピン模型を「相転移がない単純な系」ではなく、**局所的な1-step ruleがどのように長距離情報を運び、失うかを比較できる最小の統計力学系**として見ることができる。
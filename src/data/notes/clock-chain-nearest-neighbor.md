---
title: "1次元一様最近接クロック系 — 離散位相増分と角度記憶"
summary: "1次元最近接clock鎖を、Isingの離散的な反転記憶とXYの連続的な位相増分記憶の間を埋める模型として読む。有限qの離散位相増分、transfer spectrum、XY spectrumのaliasing、rare jumpからphase diffusionへのcross-overを通して、Z2→Zq→U(1)で何が連続的に変わるかを整理する。"
publishedAt: 2026-09-17T10:20:00+09:00
updatedAt: 2026-09-19
area: "Physics"
topics: ["statistical mechanics", "clock model", "spin model", "transfer matrix", "phase diffusion", "correlation", "Fourier spectrum"]
status: growing
---

Ising鎖では、隣接スピンの関係は「反転したか、していないか」という二値で記録できる。一方XY鎖では、隣接角度差は連続量であり、小さな位相増分の累積が遠距離の角度記憶を失わせる。

この二つの間で、局所的に記憶できる角度差だけを増やしていくと何が変わるのか。

clock modelでは

$$
\theta_i=\frac{2\pi n_i}{q},
\qquad
n_i\in\mathbb Z_q
$$

とし、最近接Hamiltonianを

$$
H=-J\sum_i\cos(\theta_{i+1}-\theta_i)
$$

とする。以下では

$$
\beta\equiv\frac{1}{k_{\mathrm B}T},
\qquad
K\equiv\beta J
$$

と書く。

$q=2$ではIsing、$q\to\infty$ではXYへ近づく。しかし、重要なのは単に局所状態数が増えることではない。局所角度差の離散性が弱まり、長距離記憶を担うtransfer spectrumの構造そのものが変わる。

## 1. 局所記憶変数は離散化された位相増分である

隣接角度差を

$$
\phi_i\equiv\theta_{i+1}-\theta_i
$$

とする。clock modelでは

$$
\boxed{
\phi_i=\frac{2\pi a_i}{q},
\qquad
a_i\in\mathbb Z_q
}
$$

である。

したがって最近接・零外場では

$$
\boxed{
H=-J\sum_i\cos\phi_i
}
$$

となる。

この形だけを見ればIsing、clock、XYは共通であり、違いは$\phi_i$が取りうる集合にある。

$$
\begin{array}{c|c}
\text{model} & \text{allowed phase increment}\\
\hline
Z_2 & \{0,\pi\}\\[1mm]
Z_q & \left\{\dfrac{2\pi a}{q}\right\}_{a=0}^{q-1}\\[3mm]
U(1) & [0,2\pi)
\end{array}
$$

Isingのdomain wall変数

$$
\tau_i=s_i s_{i+1}=\pm1
$$

は、$q=2$ clockで

$$
e^{i\phi_i}=\pm1
$$

と書いたものに対応する。

この意味で

$$
\boxed{
Z_2\to Z_q\to U(1)
}
$$

は

$$
\boxed{
\text{two-state increment}
\to
\text{discrete phase increment}
\to
\text{continuous phase increment}
}
$$

というmemory alphabetの連続化として読める。

## 2. 遠距離の角度記憶は局所増分の積で決まる

距離$r$だけ離れた角度差は

$$
\theta_r-\theta_0
=\sum_{j=0}^{r-1}\phi_j
$$

なので

$$
\boxed{
e^{im(\theta_r-\theta_0)}
=\prod_{j=0}^{r-1}e^{im\phi_j}
}
$$

となる。

最近接・零外場では各$\phi_j$は独立だから

$$
C_m(r)
\equiv
\left\langle e^{im(\theta_r-\theta_0)}\right\rangle
=
\left\langle e^{im\phi}\right\rangle^r.
$$

したがって1 bond進んだときの$m$次角度情報のretentionを

$$
\boxed{
\rho_m^{(q)}
\equiv
\left\langle e^{im\phi}\right\rangle
}
$$

とすれば

$$
\boxed{
C_m(r)=\left[\rho_m^{(q)}\right]^r
}
$$

である。

通常のスピン相関は$m=1$で

$$
C(r)=\left[\rho_1^{(q)}\right]^r,
\qquad
\boxed{
\xi_1^{-1}=-\ln|\rho_1^{(q)}|
}
$$

となる。

## 3. transfer spectrumは離散Fourier spectrumになる

1 bondのtransfer matrixは

$$
T_{ab}
=
\exp\left[
K\cos\frac{2\pi(a-b)}q
\right]
$$

である。$T_{ab}$は$a-b$だけに依存するcirculant matrixなので、固有vectorは離散Fourier mode

$$
\psi_m(a)=e^{2\pi i m a/q}
$$

となる。

固有値は

$$
\boxed{
\Lambda_m^{(q)}
=
\sum_{a=0}^{q-1}
\exp\left[K\cos\frac{2\pi a}{q}\right]
e^{-2\pi i m a/q}
}
$$

であり、最大固有値は$m=0$である。

したがって

$$
\boxed{
\rho_m^{(q)}
=
\frac{\Lambda_m^{(q)}}{\Lambda_0^{(q)}}
}
$$

となる。

有限$q$では

$$
\Lambda_{m+q}^{(q)}=\Lambda_m^{(q)},
\qquad
\Lambda_{q-m}^{(q)}=\Lambda_m^{(q)}
$$

なので、独立なmemory sectorは有限個しかない。

$$
\boxed{
m\in\mathbb Z
\quad\longrightarrow\quad
m\bmod q
}
$$

という同一視が起きている。

## 4. $q=2$ではIsingの単一memory modeを回収する

$q=2$では角度差は$0$または$\pi$だけで、transfer matrixは

$$
T=
\begin{pmatrix}
e^K&e^{-K}\\
e^{-K}&e^K
\end{pmatrix}.
$$

固有値は

$$
\Lambda_0^{(2)}=2\cosh K,
\qquad
\Lambda_1^{(2)}=2\sinh K
$$

だから

$$
\boxed{
\rho_1^{(2)}=\tanh K
}
$$

となる。

したがって

$$
C(r)=(\tanh K)^r
$$

であり、最近接Ising鎖の結果そのものを回収する。

$q=2$では非自明なsectorが$m=1$の一つしかない。そのため最近接Isingの長距離memoryは単一指数で完全に閉じる。

## 5. $q\to\infty$ではXYの無限harmonic hierarchyへつながる

$q$を大きくすると離散和は円周上の積分へ近づき、

$$
\Lambda_m^{(q)}
\sim
q I_m(K)
$$

となる。ここで

$$
I_m(K)
=\frac1{2\pi}
\int_0^{2\pi}
e^{K\cos\phi}e^{-im\phi}\,d\phi
$$

は修正Bessel関数である。

したがって

$$
\boxed{
\lim_{q\to\infty}\rho_m^{(q)}
=
\frac{I_m(K)}{I_0(K)}
}
$$

となり、最近接XY鎖のmemory spectrumへつながる。

有限$q$では有限個だったmemory sectorが、$q\to\infty$で

$$
m=1,2,3,\ldots
$$

という無限のharmonic hierarchyになる。

## 6. clock spectrumはXY spectrumを折り畳んだものとして書ける

Fourier展開

$$
e^{K\cos\phi}
=\sum_{n=-\infty}^{\infty}I_n(K)e^{in\phi}
$$

をclock角

$$
\phi_a=\frac{2\pi a}{q}
$$

でサンプリングする。

離散Fourier和

$$
\sum_{a=0}^{q-1}
e^{2\pi i(n-m)a/q}
=q\,\delta_{n,m\ ({\rm mod}\ q)}
$$

から

$$
\boxed{
\Lambda_m^{(q)}
=
q\sum_{\ell\in\mathbb Z}I_{m+\ell q}(K)
}
$$

を得る。

よって

$$
\boxed{
\rho_m^{(q)}
=
\frac{
\displaystyle\sum_{\ell\in\mathbb Z}I_{m+\ell q}(K)
}{
\displaystyle\sum_{\ell\in\mathbb Z}I_{\ell q}(K)
}
}
$$

である。

有限$q$のclock spectrumは、XYで本来独立な

$$
\ldots,m-q,m,m+q,\ldots
$$

を一つのsectorへ重ね合わせたものになっている。

$
\boxed{
\text{finite angular discretization}
\longleftrightarrow
\text{harmonic-space aliasing}
}
$

という対応がある。

![有限$q$のmemory spectrumとXY極限](/figures/clock-r1/memory-spectrum-folding.svg)

*$K=20$における$\rho_m^{(q)}$。有限$q$では独立sectorが$m\le q/2$までに折り畳まれる。$q$を増やすと低いharmonicからXYの無限spectrumへ収束し、細かい角度情報ほど有限$q$性を長く残す。*

## 7. 低温では局所位相増分に二つの見え方が現れる

基底状態$\phi=0$に対し、最小非零位相増分は

$$
\Delta\phi=\frac{2\pi}{q}
$$

である。

その励起コストは

$$
\boxed{
\Delta E_q
=J\left(1-\cos\frac{2\pi}{q}\right)
}
$$

であり、大きな$q$では

$$
\Delta E_q
\simeq
\frac{J}{2}\left(\frac{2\pi}{q}\right)^2.
$$

一方、XY低温極限では

$$
K\cos\phi
\simeq
K-\frac K2\phi^2
$$

なので、局所角度揺らぎのthermal widthは

$$
\boxed{
\sigma_T\sim K^{-1/2}
}
$$

である。

clock角の刻みとthermal widthの比を

$$
\boxed{
\eta
\equiv
\frac{\Delta\phi}{\sigma_T}
\sim
\frac{2\pi\sqrt K}{q}
}
$$

とする。

$\eta\gg1$ではthermal windowの中に$\phi=0$以外の状態がほとんど入らない。非零位相増分は稀な離散励起として現れ、局所列は

$$
0,0,0,0,\Delta\phi,0,0,\ldots
$$

のようなsparse jump processになる。

一方

$$
\eta\ll1
$$

ではthermal windowの中に多数のclock statesが入り、各bondは小さな位相増分を頻繁に取る。すると

$$
\theta_r-\theta_0
=\sum_{j=0}^{r-1}\phi_j
$$

は連続的なrandom walkとして見える。

$$
\boxed{
\text{rare discrete jumps}
\longrightarrow
\text{dense small-step phase diffusion}
}
$$

というcross-overの実体は、thermal widthの中にいくつの局所角度状態が解像されるかにある。

## 8. 相関長はactivated型からdiffusive型へ変わる

有限$q$を固定して低温へ行くと、最小非零stepのBoltzmann重みは

$$
\exp\left[
-K\left(1-\cos\frac{2\pi}{q}\right)
\right]
$$

で抑制される。

$q\ge3$ではleading orderで

$$
\rho_1^{(q)}
\simeq
1
-2\left(1-\cos\frac{2\pi}{q}\right)
\exp\left[
-K\left(1-\cos\frac{2\pi}{q}\right)
\right]
$$

なので

$$
\boxed{
\xi_1
\simeq
\frac{
\exp\left[K\left(1-\cos\frac{2\pi}{q}\right)\right]
}{
2\left(1-\cos\frac{2\pi}{q}\right)
}
}
$$

となる。

有限$q$では相関長はactivatedに増大する。

一方XYでは

$$
\frac{I_1(K)}{I_0(K)}
\simeq
\exp\left(-\frac1{2K}\right)
$$

なので

$$
\boxed{
\xi_{\rm XY}\simeq2K
}
$$

である。

有限$q$のactivated memoryと、XYのdiffusive memoryは低温漸近形そのものが異なる。

## 9. cross-over変数は$q/\sqrt K$になる

最小stepの熱コストは

$$
K\left(1-\cos\frac{2\pi}{q}\right)
\simeq
\frac{2\pi^2K}{q^2}.
$$

したがって離散性が熱揺らぎと競合する条件は

$$
\frac{q}{\sqrt K}=O(1)
$$

となる。

相関長の数値評価でも、異なる$K$に対する

$$
\frac{\xi_q}{\xi_{\rm XY}}
$$

は

$$
\boxed{
\frac{q}{\sqrt K}
}
$$

で整理するとほぼ同じcross-overを示す。

実用的に$\xi_q$がXY値の数%以内へ入る条件も

$$
q\sim O(\sqrt K)
$$

となる。

これは$q$の大きさ単独ではXYらしさが決まらないことを意味する。同じ$q$でも低温へ行けば再び角度刻みが見える。

![相関長のclockからXYへのcross-over](/figures/clock-r1/correlation-length-crossover.svg)

*$\xi_q/\xi_{XY}$を$q/\sqrt K$で整理したもの。異なる温度の曲線が同じ領域で急速にXY値へ近づき、局所角度刻み$2\pi/q$とthermal width$K^{-1/2}$の競合がcross-overを支配することが見える。*

## 10. 高いharmonicほど遅くXY化する

XY低温では

$$
\frac{I_m(K)}{I_0(K)}
\simeq
\exp\left(-\frac{m^2}{2K}\right)
$$

だから

$$
\boxed{
\xi_m^{XY}
\simeq
\frac{2K}{m^2}
}
$$

となる。

clock modelではaliasing表示から

$$
\boxed{
\rho_m^{(q)}
\simeq
\frac{
\displaystyle
\sum_{\ell\in\mathbb Z}
\exp\left[-\frac{(m+\ell q)^2}{2K}\right]
}{
\displaystyle
\sum_{\ell\in\mathbb Z}
\exp\left[-\frac{(\ell q)^2}{2K}\right]
}
}
$$

と書ける。

$m$ sectorに対する最も近いaliasは$m-q$なので、本来のXY成分に対するaliasの比は

$$
\boxed{
\epsilon_m
\sim
\exp\left[-\frac{q(q-2m)}{2K}\right]
}
$$

となる。

$m$が大きいほど$q-2m$が小さくなるため、高いharmonicほどfinite-$q$ foldingの影響を強く受ける。

$$
\boxed{
\text{coarse angular memory}
\text{ が先にXY化し、}
\text{fine angular memory}
\text{ は後まで離散性を残す}
}
$$

という階層が現れる。

![harmonicごとのmemory length](/figures/clock-r1/harmonic-memory-hierarchy.svg)

*$K=20$での$\xi_m/\xi_1$。$q$が大きくなるにつれてXY低温則$\xi_m/\xi_1\simeq m^{-2}$が低いharmonicから回復する。有限$q$ではNyquist境界$m\sim q/2$へ近づくほどfoldingの影響が強くなる。*

## 11. $q\to\infty$と$T\to0$は同じ極限ではない

有限$q$を固定して$K\to\infty$とすると

$$
\eta=\frac{2\pi\sqrt K}{q}\to\infty
$$

なので、必ずrare-jump regimeへ戻る。

したがって

$$
\xi_q
\sim
\exp\left[
K\left(1-\cos\frac{2\pi}{q}\right)
\right].
$$

一方、先に$q\to\infty$としてXY模型へ移れば局所励起gapは閉じており、低温でも

$$
\xi_{XY}\simeq2K
$$

である。

有限$q$のclock chainは、どれほど$q$が大きくても十分低温では離散模型として振る舞う。

$$
\boxed{
q=\infty
\text{ は単なる「非常に大きな有限 }q\text{」ではない}
}
$$

という違いは、局所位相増分のgapが本当に閉じているかどうかに現れる。

## 12. 得られた見方

clock modelをIsingとXYの間に置くと、対称性の違いは単なるスピン状態数の違いではなく、局所memoryの角度分解能の違いとして見える。

$$
\boxed{
Z_2
\to
Z_q
\to
U(1)
}
$$

は

$$
\boxed{
\text{one nontrivial memory mode}
\to
\text{finite harmonic memory spectrum}
\to
\text{infinite harmonic hierarchy}
}
$$

という変化でもある。

実空間では

$$
\boxed{
\Delta\phi=\frac{2\pi}{q}
}
$$

という有限刻みがrare discrete jumpを作り、Fourier空間では同じ離散化が

$$
\boxed{
m\sim m+q}
$$

というspectral aliasingを作る。

したがって

$$
\boxed{
\text{angular discretization}
\longleftrightarrow
\text{spectral folding}
}
$$

は同じ有限-$q$性を二つの表示で見たものになる。

$q$を増やしたときに起きるのは、flip memoryがただ滑らかになることではない。thermal widthの中へ利用可能な局所状態が増え、sparse jump processがdense phase diffusionへ変わり、それと同時に有限個へ折り畳まれていたmemory spectrumがXYの無限harmonic hierarchyへ展開されていく。

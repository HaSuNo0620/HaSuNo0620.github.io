---
title: "1次元XY模型 — 位相拡散と角度記憶"
summary: "最近接古典XY鎖を、局所的には整列しているのに遠距離では向きを失う系として読む。独立な角度差、空間方向の位相拡散、修正Bessel関数が現れる理由、harmonicごとの記憶長、compactnessとwindingを通して、連続対称性を持つ1次元系の相関喪失機構を整理する。"
publishedAt: 2026-09-12T03:10:00+09:00
updatedAt: 2026-09-13
area: "Physics"
topics: ["statistical mechanics", "XY model", "phase diffusion", "transfer operator", "correlation", "Bessel function", "compact field"]
status: growing
---

隣り合うスピンがほとんど同じ向きを向いているなら、遠く離れたスピンも同じ向きを覚えていそうに見える。ところが1次元の最近接XY鎖では、有限温度ならどれだけ低温でも遠距離の向きは失われる。

このノートで知りたいのは、XY模型を形式的に解く方法ではなく、**局所整列と長距離秩序がなぜ同じものではないのか**である。

各サイトに平面内の単位ベクトル $\mathbf S_i=(\cos\theta_i,\sin\theta_i)$ を置き、

$$
H=-J\sum_i\cos(\theta_{i+1}-\theta_i)
$$

を考える。以下では

$$
\boxed{\beta\equiv\frac{1}{k_{\mathrm B}T},\qquad K\equiv\beta J=\frac{J}{k_{\mathrm B}T}}
$$

と書く。$J>0$ なら隣接角度差を小さくしたい。しかしXYでは、隣接スピンに**少しだけ**逆らうことができる。この連続性が、1次元での相関喪失の仕方を決める。

## 1. 見るべき変数はスピン角そのものではなく角度差である

開鎖で $\phi_i\equiv\theta_{i+1}-\theta_i$ と置くと、

$$
H=-J\sum_i\cos\phi_i,
\qquad
\theta_n=\theta_1+\sum_{j=1}^{n-1}\phi_j.
$$

したがって $\{\theta_i\}$ と $(\theta_1,\{\phi_i\})$ は同じ情報を持つ。外場ゼロの開鎖では各 bond の $\phi_i$ は互いに独立で、1 bond のBoltzmann重みは

$$
\exp[-\beta(-J\cos\phi)]
=
\exp(K\cos\phi)
$$

である。

ここで最初に重要なのは、分母に何が入るかである。規格化定数は

$$
Z_1=\int_0^{2\pi}e^{K\cos\phi}\,d\phi.
$$

したがって

$$
p(\phi)=\frac{e^{K\cos\phi}}{Z_1}.
$$

## 2. 修正Bessel関数は「円周上のBoltzmann重みのFourier係数」である

$\phi$ は円周上の角度なので、自然な基底は $e^{im\phi}$ である。そこで

$$
e^{K\cos\phi}
=\sum_{m=-\infty}^{\infty}a_m e^{im\phi}
$$

とFourier展開すると、係数は

$$
a_m
=\frac{1}{2\pi}
\int_0^{2\pi}
e^{K\cos\phi}e^{-im\phi}\,d\phi.
$$

この積分が整数次数の修正Bessel関数の積分表示そのもので、

$$
\boxed{
I_m(K)
=\frac{1}{2\pi}
\int_0^{2\pi}
e^{K\cos\phi}e^{-im\phi}\,d\phi
}
$$

である。よって

$$
\boxed{
e^{K\cos\phi}
=\sum_{m=-\infty}^{\infty}I_m(K)e^{im\phi}}
$$

となる。特に $m=0$ では

$$
Z_1=2\pi I_0(K),
$$

だから

$$
\boxed{
p(\phi)=\frac{e^{K\cos\phi}}{2\pi I_0(K)}}.
$$

つまり修正Bessel関数は、特殊関数を後から持ち込んだのではない。

$$
\boxed{
\text{円周上の角度自由度}
+\text{Boltzmann重み }e^{K\cos\phi}
+\text{Fourier分解}
\Longrightarrow I_m(K)
}
$$

という必然である。通常のBessel関数ではなく修正Bessel関数が出るのは、重みが振動的な $e^{iK\cos\phi}$ ではなく、実指数の $e^{K\cos\phi}$ だからである。

## 3. 低温では各bondはよく揃うが、角度は空間方向にrandom walkする

低温 $K\gg1$ では $\phi=0$ 近傍だけが重要なので

$$
1-\cos\phi\simeq\frac{\phi^2}{2}.
$$

Boltzmann重みは

$$
e^{K\cos\phi}
\simeq e^K\exp\left(-\frac{K\phi^2}{2}\right)
$$

となり、1 bond の角度揺らぎは

$$
\boxed{
\langle\phi^2\rangle
\simeq\frac{1}{K}
=\frac{k_{\mathrm B}T}{J}}
$$

である。

一方、距離 $r$ 離れた二点では

$$
\theta_r-\theta_0=\sum_{j=0}^{r-1}\phi_j.
$$

独立な小さな角度差を足し合わせるので、

$$
\boxed{
\left\langle(\theta_r-\theta_0)^2\right\rangle
\simeq r\frac{k_{\mathrm B}T}{J}}
$$

と分散が距離に比例して成長する。

局所的にはどのbondもほぼ整列している。それでも方向の誤差は空間方向に少しずつ蓄積し、最終的には最初の向きを忘れる。この意味で1次元XY鎖の長距離物理は **phase diffusion in space** として読める。

## 4. 位相拡散だけで指数相関と相関長が見える

二点相関を

$$
C(r)=\langle\mathbf S_0\cdot\mathbf S_r\rangle
=\left\langle\cos(\theta_r-\theta_0)\right\rangle
$$

とする。低温Gaussian近似では

$$
\left\langle e^{i(\theta_r-\theta_0)}\right\rangle
=\exp\left[-\frac12
\left\langle(\theta_r-\theta_0)^2\right\rangle\right],
$$

したがって

$$
C(r)
\simeq
\exp\left(-\frac{r k_{\mathrm B}T}{2J}\right).
$$

よって

$$
\boxed{
\xi\simeq\frac{2J}{k_{\mathrm B}T}=2\beta J}
$$

となる。相関を壊しているのは一か所の大きな欠陥ではなく、**至る所にある小さな角度ずれの累積**である。

## 5. 厳密解は角度増分のcharacteristic functionになっている

一般の整数 $m$ に対して、1 bond の characteristic function は

$$
\left\langle e^{im\phi}\right\rangle
=
\frac{1}{2\pi I_0(K)}
\int_0^{2\pi}e^{K\cos\phi}e^{im\phi}\,d\phi
=
\frac{I_m(K)}{I_0(K)}.
$$

距離 $r$ の角度差は独立な増分の和なので、

$$
\boxed{
C_m(r)
\equiv
\left\langle e^{im(\theta_r-\theta_0)}\right\rangle
=
\left[\frac{I_m(K)}{I_0(K)}\right]^r}
$$

となる。通常のスピン相関は $m=1$ の実部だから

$$
\boxed{
C(r)=\left[\frac{I_1(K)}{I_0(K)}\right]^r,
\qquad
\xi_1^{-1}=-\ln\left[\frac{I_1(K)}{I_0(K)}\right]}
$$

である。

ここでは $I_m/I_0$ は、**1 bond進んだときに $m$ 次の角度情報がどれだけ残るか**を直接表している。

## 6. XYには角度情報の解像度ごとの記憶長がある

各 harmonic $e^{im\theta}$ に対して

$$
\xi_m^{-1}
=-\ln\left|\frac{I_m(K)}{I_0(K)}\right|
$$

を定義できる。低温では

$$
\frac{I_m(K)}{I_0(K)}
\simeq
\exp\left(-\frac{m^2}{2K}\right)
$$

だから

$$
\boxed{
\xi_m\simeq\frac{2K}{m^2}
=\frac{2J}{m^2k_{\mathrm B}T}}
$$

となる。高い harmonic ほど短い距離で消える。

$$
\boxed{\xi_m\propto m^{-2}}
$$

は、phase diffusion が角度情報をどの順序で失わせるかを表す。

## 7. 転送作用素の固有modeは、この記憶階層そのものである

転送kernelを

$$
T(\theta,\theta')=e^{K\cos(\theta'-\theta)}
$$

とすると、角度差だけに依存するので Fourier mode $\psi_m(\theta)=e^{im\theta}$ が固有関数になる。

$$
(T\psi_m)(\theta)
=2\pi I_m(K)\psi_m(\theta),
$$

したがって

$$
\boxed{\lambda_m=2\pi I_m(K)}.
$$

最大固有値は $\lambda_0=2\pi I_0(K)$ で、

$$
f=-\frac1\beta\ln[2\pi I_0(K)]
=-k_{\mathrm B}T\ln[2\pi I_0(K)]
$$

を与える。一方、$m$ 次の角度情報は

$$
C_m(r)=\left(\frac{\lambda_m}{\lambda_0}\right)^r
$$

で伝わる。転送作用素の無限個の Fourier sector は、抽象的な固有modeの列ではなく、異なる角度分解能の記憶距離である。

## 8. 外場は相対角だけで閉じる単純さを壊す

$x$ 方向の外場を加えると

$$
H=-J\sum_i\cos(\theta_{i+1}-\theta_i)-\sum_i h_i\cos\theta_i.
$$

外場は絶対角を見るため、角度差 $\phi_i$ だけでは問題が閉じない。一様外場なら

$$
T_h(\theta,\theta')
=
\exp\left[
K\cos(\theta'-\theta)
+\frac{\beta h}{2}(\cos\theta+\cos\theta')
\right].
$$

$\cos\theta=(e^{i\theta}+e^{-i\theta})/2$ なので Fourier 空間では $m\leftrightarrow m\pm1$ が結合する。零外場で独立だった harmonic sector を外場が混ぜる。

線形応答では

$$
\chi_x(r)=\frac\beta2\left[\frac{I_1(K)}{I_0(K)}\right]^{|r|},
$$

したがって

$$
\boxed{
\chi_x(q)
=\frac\beta2
\frac{1-\rho^2}{1-2\rho\cos q+\rho^2},
\qquad
\rho=\frac{I_1(K)}{I_0(K)}}.
$$

これは phase diffusion によって作られた空間記憶を外場が波数ごとに probe していると読める。

## 9. 角度は実数ではなくcompactな変数である

低温Gaussian近似だけを見ると $\theta$ は単なる実数場に見える。しかしXYの角度は

$$
\boxed{\theta\equiv\theta+2\pi}
$$

である。周期境界条件では

$$
\theta_N=\theta_0+2\pi w,
\qquad w\in\mathbb Z,
$$

したがって

$$
\boxed{\sum_{i=0}^{N-1}\phi_i=2\pi w}
$$

という global constraint が現れる。開鎖で見えた局所的 phase diffusion に、環では winding sector が重なる。

## 10. この模型で覚えておきたいこと

1次元XY鎖では、局所的な整列と長距離の方向記憶は同じではない。各 bond の角度ずれは低温で小さいが、その和は空間方向に拡散する。そのため任意の有限温度で長距離秩序は失われる。

そして厳密解に現れる修正Bessel関数は、円周上のBoltzmann重み $e^{K\cos\phi}$ の Fourier 係数である。したがって

$$
\boxed{
\text{phase diffusion}
\longleftrightarrow
\text{Fourier harmonic}
\longleftrightarrow
I_m(K)/I_0(K)
\longleftrightarrow
\xi_m
}
$$

という一本の流れで理解できる。
---
title: "1次元XY模型 — 位相拡散と角度記憶"
summary: "最近接古典XY鎖を、局所的には整列しているのに遠距離では向きを失う系として読む。独立な角度差、空間方向の位相拡散、Bessel関数による厳密相関、harmonicごとの記憶長、compactnessとwindingを通して、連続対称性を持つ1次元系の相関喪失機構を整理する。"
publishedAt: 2026-09-12T03:10:00+09:00
updatedAt: 2026-09-13
area: "Physics"
topics: ["statistical mechanics", "XY model", "phase diffusion", "transfer operator", "correlation", "Bessel function", "compact field"]
status: growing
---

隣り合うスピンがほとんど同じ向きを向いているなら、遠く離れたスピンも同じ向きを覚えていそうに見える。ところが1次元の最近接XY鎖では、有限温度ならどれだけ低温でも遠距離の向きは失われる。

このノートで知りたいのは、XY模型を形式的に解く方法ではなく、**局所整列と長距離秩序がなぜ同じものではないのか**である。

各サイトに平面内の単位ベクトル

$$
\mathbf S_i=(\cos\theta_i,\sin\theta_i)
$$

を置き、最近接相互作用

$$
\boxed{
H=-J\sum_i\cos(\theta_{i+1}-\theta_i)
}
$$

を考える。$J>0$ なら隣接角度差を小さくしたい。しかしXYでは、隣接スピンに**少しだけ**逆らうことができる。この連続性が、1次元での相関喪失の仕方を決める。

## 1. 見るべき変数はスピン角そのものではなく角度差である

開鎖で

$$
\phi_i\equiv\theta_{i+1}-\theta_i
$$

と置くと、Hamiltonian は

$$
\boxed{
H=-J\sum_i\cos\phi_i
}
$$

となる。基準角 $\theta_1$ を一つ残せば

$$
\theta_n=\theta_1+\sum_{j=1}^{n-1}\phi_j
$$

なので、$\{\theta_i\}$ と $(\theta_1,\{\phi_i\})$ は同じ情報を持つ。

外場ゼロの開鎖では、各 bond の $\phi_i$ は互いに独立である。1 bond の分布は

$$
\boxed{
p(\phi)
=\frac{e^{K\cos\phi}}{2\pi I_0(K)},
\qquad K\equiv\beta J
}
$$

である。ここで $I_m$ は修正Bessel関数である。

つまり最近接XY鎖では、複雑に見えるスピン列を

$$
\boxed{
\text{独立な角度増分 }\phi_1,\phi_2,\ldots
}
$$

として読むことができる。

## 2. 低温では各bondはよく揃うが、角度は空間方向にrandom walkする

低温 $K\gg1$ では $\phi=0$ 近傍だけが重要なので

$$
1-\cos\phi\simeq\frac{\phi^2}{2}
$$

と近似できる。1 bond の分布はほぼGaussianになり、

$$
\boxed{
\langle\phi^2\rangle\simeq\frac{T}{J}
}
$$

となる。

重要なのは、各 $\phi_i$ が小さいことと、遠距離の角度差が小さいことは同じではない点である。

距離 $r$ 離れた二点では

$$
\theta_r-\theta_0
=\sum_{j=0}^{r-1}\phi_j.
$$

独立な小さな角度差を足し合わせるので、

$$
\boxed{
\left\langle(\theta_r-\theta_0)^2\right\rangle
\simeq r\frac{T}{J}
}
$$

と分散が距離に比例して成長する。

局所的にはどのbondもほぼ整列している。それでも方向の誤差は空間方向に少しずつ蓄積し、最終的には最初の向きを忘れる。

この意味で1次元XY鎖の長距離物理は

$$
\boxed{
\text{phase diffusion in space}
}
$$

として読める。

## 3. 位相拡散だけで指数相関と $\xi\sim J/T$ が見える

二点相関は

$$
C(r)
\equiv
\langle\mathbf S_0\cdot\mathbf S_r\rangle
=
\left\langle\cos(\theta_r-\theta_0)\right\rangle
$$

である。

低温Gaussian近似では

$$
\left\langle e^{i(\theta_r-\theta_0)}\right\rangle
=
\exp\left[-\frac12
\left\langle(\theta_r-\theta_0)^2\right\rangle\right]
$$

だから、

$$
C(r)
\simeq
\exp\left(-\frac{rT}{2J}\right).
$$

したがって

$$
\boxed{
\xi\simeq\frac{2J}{T}=2\beta J
}
$$

となる。

ここで相関を壊しているのは、一か所の大きな欠陥ではない。**至る所にある小さな角度ずれの累積**である。

有限温度で長距離秩序が失われる理由を、相転移の一般論より先に、この空間random walkとして理解しておく方が物理像は明確である。

## 4. 厳密解はrandom walkのcharacteristic functionになっている

Gaussian近似を外しても、角度差の独立性はそのまま使える。

一般の整数 $m$ に対して

$$
\left\langle e^{im\phi}\right\rangle
=
\frac{I_m(K)}{I_0(K)}.
$$

距離 $r$ の角度差は独立な増分の和なので、characteristic function は積になり、

$$
\boxed{
C_m(r)
\equiv
\left\langle e^{im(\theta_r-\theta_0)}\right\rangle
=
\left[
\frac{I_m(K)}{I_0(K)}
\right]^r
}
$$

となる。

通常のスピン相関は $m=1$ の実部なので

$$
\boxed{
C(r)=
\left[
\frac{I_1(K)}{I_0(K)}
\right]^r
}
$$

である。したがって厳密な相関長は

$$
\boxed{
\xi_1^{-1}
=-\ln\left[
\frac{I_1(K)}{I_0(K)}
\right]
}
$$

となる。

Bessel関数は単に転送作用素を対角化した結果として現れるのではない。ここでは、**1 bond の角度増分のFourier変換そのもの**として現れている。

## 5. XYには「角度情報の解像度」ごとの記憶長がある

$m=1$ だけを見る必要はない。$e^{im\theta}$ は角度を $m$ 倍細かく識別するharmonicであり、各 $m$ に対して

$$
\boxed{
\xi_m^{-1}
=-\ln\left|
\frac{I_m(K)}{I_0(K)}
\right|
}
$$

という記憶長を定義できる。

低温では

$$
\frac{I_m(K)}{I_0(K)}
\simeq
\exp\left(-\frac{m^2}{2K}\right)
$$

なので、

$$
\boxed{
\xi_m\simeq\frac{2K}{m^2}
=
\frac{2J}{m^2T}
}
$$

となる。

つまり高いharmonicほど遠距離まで保持されにくい。

$$
\boxed{
\xi_m\propto m^{-2}
}
$$

は、位相拡散が角度情報をどの順序で失わせるかを示している。粗い方向情報 $m=1$ は比較的長く残るが、細かい角度構造を表す大きな $m$ は短距離で消える。

## 6. 転送作用素の固有modeは、この記憶階層そのものである

局所Boltzmann重み

$$
T(\theta,\theta')
=
\exp[K\cos(\theta'-\theta)]
$$

を積分作用素として見ると、kernel は角度差だけに依存するため、固有関数は

$$
\psi_m(\theta)=e^{im\theta}
$$

である。固有値は

$$
\boxed{
\lambda_m=2\pi I_m(K)
}
$$

となる。

最大固有値は $m=0$ の $\lambda_0=2\pi I_0(K)$ で、

$$
f=-\frac1\beta\ln[2\pi I_0(K)]
$$

を与える。

一方、$m$ 次の角度情報は

$$
C_m(r)=
\left(\frac{\lambda_m}{\lambda_0}\right)^r
$$

で伝わる。

したがって転送作用素の無限個のFourier sectorは、抽象的な固有modeの列ではなく、**異なる角度分解能を持つ情報がどれだけ遠くまで残るか**を表している。

## 7. 外場は独立だった角度modeを混ぜる

$x$ 方向の外場を加えると

$$
H=
-J\sum_i\cos(\theta_{i+1}-\theta_i)
-\sum_i h_i\cos\theta_i.
$$

外場ゼロでは相対角だけでHamiltonianが書けたが、$\cos\theta_i$ は絶対角を見る。そのため角度差変数だけでは問題が閉じなくなる。

一様外場なら転送kernelは

$$
T_h(\theta,\theta')
=
\exp\left[
K\cos(\theta'-\theta)
+\frac{\beta h}{2}
(\cos\theta+\cos\theta')
\right]
$$

と書ける。

$\cos\theta=(e^{i\theta}+e^{-i\theta})/2$ なので、Fourier空間では

$$
\boxed{
m\longleftrightarrow m\pm1}
$$

が結合する。

零外場では独立だったharmonic sectorを、外場が混ぜるわけである。

線形応答だけを見るなら、$m=1$ 相関から

$$
\chi_x(r)
=
\frac\beta2
\left[
\frac{I_1(K)}{I_0(K)}
\right]^{|r|}
$$

となり、Fourier変換すると

$$
\boxed{
\chi_x(q)
=\frac\beta2
\frac{1-\rho^2}
{1-2\rho\cos q+\rho^2},
\qquad
\rho=\frac{I_1(K)}{I_0(K)}
}
$$

を得る。

これはphase diffusionによって作られた空間記憶を、外場が波数ごとにprobeしていると読める。

## 8. 角度は実数ではなくcompactな変数である

低温近似だけを見ると、$\theta$ は単なるGaussian変数のように見える。しかしXYの角度は

$$
\boxed{
\theta\equiv\theta+2\pi
}
$$

である。

つまりXYは単なる調和鎖ではなく、**compactな角度場**を持つ。

周期境界条件では

$$
\theta_N=\theta_0+2\pi w,
\qquad w\in\mathbb Z
$$

が許され、したがって

$$
\boxed{
\sum_{i=0}^{N-1}\phi_i=2\pi w
}
$$

というglobal constraintが現れる。$w$ は鎖を一周したときのwinding numberである。

開鎖では各 $\phi_i$ を独立に扱えたが、環にすると「独立な局所揺らぎ」に「全体として何回巻いたか」という整数sectorが重なる。

この局所的phase diffusionとglobal windingの共存が、XY自由度の重要な特徴である。

## 9. 有限温度で長距離秩序がないことをどう読むか

任意の有限温度では

$$
\left|\frac{I_1(K)}{I_0(K)}\right|<1
$$

なので、

$$
\lim_{r\to\infty}C(r)=0.
$$

したがって純粋な1次元最近接古典XY鎖には有限温度の自発的長距離秩序はない。

ただし重要なのは「1次元だから秩序しない」と暗記することではない。この模型では、その理由を

$$
\boxed{
\text{finite local angular noise}
\rightarrow
\text{variance growing as }r
\rightarrow
\text{loss of directional memory}
}
$$

として直接見ることができる。

低温になるほど各bondは強く整列するが、有限温度なら角度拡散係数はゼロにはならない。そのため十分遠くへ行けば必ず初期方向を失う。

## 10. 実在系では何を表しているか

古典XY模型は、スピンがほぼ一つの平面内に拘束されたeasy-plane磁性体の有効模型として現れる。

実在の準1次元物質では鎖間相互作用が完全にはゼロでないため、十分低温では3次元秩序へ移ることがある。それでも

$$
J_{\parallel}\gg J_{\perp}
$$

なら、その前の広い温度領域で鎖方向の相関は1次元XY的に発達する。

したがってこの模型で見るべきなのは、理想化された「完全な1次元磁石」だけではない。**強い局所整列が、弱い角度ノイズの累積によってどの距離まで保持されるか**という準1次元系の基準問題としても使える。

## まとめ

最近接1次元XY鎖では、外場ゼロなら角度差 $\phi_i$ が独立になる。各bondでは低温ほど $\phi_i$ は小さいが、遠距離の角度差

$$
\theta_r-\theta_0=\sum_i\phi_i
$$

は空間方向にrandom walkする。

その結果、

$$
\boxed{
C_m(r)=
\left[
\frac{I_m(\beta J)}{I_0(\beta J)}
\right]^r
}
$$

となり、低温では

$$
\boxed{
\xi_m\simeq\frac{2J}{m^2T}
}
$$

というharmonicごとの記憶階層が現れる。

したがってこの模型の中心像は

$$
\boxed{
\text{local alignment}
\neq
\text{long-range directional memory}
}
$$

であり、その間をつなぐ機構が **phase diffusion** である。

Ising鎖との違いと、そこから逆に見えてくる1次元最近接スピン系の共通構造は、別ノートで比較する。
---
title: "1次元XY模型 — 最近接相互作用と角度相関"
summary: "古典1次元XY鎖を、角度差変数、積分転送作用素、Bessel関数で表される固有値、相関長、波数依存感受率という流れで整理する。Ising鎖との対応と、離散スピンから連続角度自由度へ移ることで何が変わるかを見る。"
publishedAt: 2026-09-12T03:10:00+09:00
updatedAt: 2026-09-12
area: "Physics"
topics: ["statistical mechanics", "XY model", "transfer operator", "correlation", "linear response", "Bessel function"]
status: growing
---

1次元 Ising 模型では、各サイトの自由度は $s_i=\pm1$ という離散的な二状態だった。次に自由度そのものを連続化し、各サイトに平面内の単位ベクトル

$$
\mathbf S_i=(\cos\theta_i,\sin\theta_i)
$$

を置く。最近接古典 XY 模型は

$$
\boxed{
H=-J\sum_i\cos(\theta_{i+1}-\theta_i)
}
$$

で定義される。

Ising では局所変数が $Z_2$、XY では $U(1)$ 対称性を持つ。相互作用距離は最近接のままだが、局所状態空間が二点から円 $S^1$ へ変わる。このノートでは、離散自由度から連続角度自由度へ移ったとき、転送行列・相関・外場応答がどう変わるかを見る。

## 1. スピンそのものより角度差が自然な変数になる

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

なので、これは情報を失う近似ではなく変数変換である。

外場ゼロの開鎖では異なる $\phi_i$ は独立であり、1 bond の確率分布は

$$
\boxed{
p(\phi)
=\frac{e^{K\cos\phi}}{2\pi I_0(K)},
\qquad K\equiv\beta J
}
$$

となる。$I_n$ は修正 Bessel 関数である。

Ising の bond 変数 $\tau_i=s_i s_{i+1}=\pm1$ と対応させると、

$$
\text{Ising}:\quad \tau_i\in\{\pm1\},
$$

$$
\text{XY}:\quad \phi_i\in(-\pi,\pi]
$$

であり、最近接・外場ゼロではどちらも **bond 自由度が独立**になる。違いは、Ising の欠陥が離散的な domain wall なのに対し、XY では各 bond が連続的な角度ずれを持つ点にある。

## 2. 転送行列は有限行列ではなく積分作用素になる

局所 Boltzmann 重みは

$$
T(\theta,\theta')
=\exp[K\cos(\theta'-\theta)]
$$

である。したがって転送問題は

$$
(T\psi)(\theta)
=\int_0^{2\pi}d\theta'\,
T(\theta,\theta')\psi(\theta')
$$

という積分作用素になる。

kernel は角度差だけに依存するため、固有関数は Fourier mode

$$
\psi_m(\theta)=e^{im\theta},
\qquad m\in\mathbb Z
$$

であり、固有値は

$$
\boxed{
\lambda_m=2\pi I_m(K)
}
$$

となる。最大固有値は $m=0$ の

$$
\lambda_0=2\pi I_0(K)
$$

なので、1サイトあたり自由エネルギーは

$$
\boxed{
f=-\frac1\beta\ln[2\pi I_0(K)]
}
$$

である。

Ising では $2\times2$ 行列の二つの固有値だけを見ればよかった。XY では無限個の Fourier sector $m\in\mathbb Z$ を持つが、回転対称性のおかげで各 sector は完全に分離している。

## 3. 二点相関は $m=1$ sector の固有値比で決まる

回転不変な零外場では $\langle\mathbf S_i\rangle=0$ である。二点相関を

$$
C(r)
\equiv
\langle\mathbf S_0\cdot\mathbf S_r\rangle
=
\langle\cos(\theta_r-\theta_0)\rangle
$$

とする。

角度差表示を使えば

$$
\theta_r-\theta_0
=\sum_{j=0}^{r-1}\phi_j
$$

であり、独立性から characteristic function が積になる。1 bond について

$$
\left\langle e^{i\phi}\right\rangle
=\frac{I_1(K)}{I_0(K)}
$$

だから、

$$
\boxed{
C(r)
=\left[\frac{I_1(K)}{I_0(K)}\right]^r
=\left(\frac{\lambda_1}{\lambda_0}\right)^r
}
$$

となる。

したがって相関長は

$$
\boxed{
\xi^{-1}
=-\ln\left[\frac{I_1(K)}{I_0(K)}\right]
}
$$

である。

Ising では $\lambda_-/\lambda_+=\tanh K$ が相関を支配したのに対し、XY では

$$
\boxed{
\rho(K)\equiv\frac{I_1(K)}{I_0(K)}
}
$$

が同じ役割を担う。

## 4. 低温相関長は Ising と本質的に違う

$K\gg1$ では

$$
\frac{I_1(K)}{I_0(K)}
=1-\frac{1}{2K}+O(K^{-2})
$$

なので、

$$
\boxed{
\xi\simeq 2K=2\beta J
}
$$

となる。

これは Ising 鎖の

$$
\xi_{\rm Ising}\simeq\frac12e^{2\beta J}
$$

とは質的に異なる。

Ising では秩序を壊すには有限エネルギー $2J$ を持つ domain wall を作る必要があり、その密度が Arrhenius 的に小さくなる。一方 XY では、小さな角度ずれを各 bond に少しずつ蓄積するだけで遠距離の向きを失える。低温で

$$
1-\cos\phi\simeq\frac12\phi^2
$$

と近似すれば、bond ごとの角度揺らぎは

$$
\langle\phi^2\rangle\sim\frac{T}{J}
$$

であり、それが random walk 的に積み重なる。

したがって

$$
\boxed{
\text{Ising}:\ \text{rare walls}
\qquad\leftrightarrow\qquad
\text{XY}:\ \text{accumulated angular diffusion}
}
$$

という違いが、低温相関長の指数増大と線形増大の違いとして現れる。

## 5. 波数依存感受率も同じ幾何級数で閉じる

$x$ 方向の微小外場

$$
H_h=-\sum_i h_i\cos\theta_i
$$

を考える。零外場では回転対称性から

$$
\langle\cos\theta_i\cos\theta_j\rangle
=\frac12C(|i-j|)
$$

である。したがって

$$
\chi_x(r)
=\beta\langle\cos\theta_0\cos\theta_r\rangle
=\frac\beta2\rho^{|r|}
$$

となる。

Fourier 変換すると

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

である。

一様感受率は

$$
\boxed{
\chi_x(0)
=\frac\beta2\frac{1+\rho}{1-\rho}
}
$$

となる。形式は Ising の $\chi(q)$ とほぼ同じで、違いは局所自由度の対称性が $\rho(K)$ と prefactor に反映されている。

## 6. 低温では再び $q\xi$ が自然な変数になる

$\xi\gg1$、$q\ll1$ では $\rho=e^{-1/\xi}$ として

$$
\boxed{
\chi_x(q)
\simeq
\frac{\beta\xi}{1+(q\xi)^2}
}
$$

となる。

したがって XY 鎖も、空間振動外場に対して wave-vector filter として働く。外場の波長が相関長より十分長ければ一つの相関領域がほぼ同じ方向へ応答し、短ければ領域内部で応答が相殺される。

Ising と XY で同じ Lorentzian 型が現れるのは、長距離で相関が単一指数に支配されるという共通構造による。

## 7. 外場を有限にすると Fourier sector が混ざる

一様外場 $h$ を加えると

$$
H=-J\sum_i\cos(\theta_{i+1}-\theta_i)
-h\sum_i\cos\theta_i
$$

となる。転送 kernel を対称化して

$$
T_h(\theta,\theta')
=
\exp\left[
K\cos(\theta'-\theta)
+\frac{\beta h}{2}(\cos\theta+\cos\theta')
\right]
$$

と書ける。

$h=0$ では $m$ が保存されていたが、$\cos\theta=(e^{i\theta}+e^{-i\theta})/2$ は $m\to m\pm1$ を結ぶため、有限外場では Fourier sector が混ざる。

これは periodic Ising 鎖で位置依存外場を入れると転送行列が非可換になったことに対応する。ただし XY では、混ざる内部自由度が有限個の sublattice ではなく無限個の角運動量 sector である。

## 8. 1次元では有限温度の長距離秩序は生じない

任意の有限温度で

$$
\frac{I_1(K)}{I_0(K)}<1
$$

なので、

$$
\lim_{r\to\infty}C(r)=0.
$$

したがって有限温度では自発的な XY 長距離秩序は存在しない。2次元 XY 模型で現れる BKT 転移も、純粋な1次元最近接古典 XY 鎖には存在しない。

1次元で見えているのは相転移ではなく、温度低下に伴う相関長の連続的増大である。

## 9. Ising との対応を整理する

|  | 1次元 Ising | 1次元 XY |
| --- | --- | --- |
| 局所自由度 | $s_i=\pm1$ | $\theta_i\in S^1$ |
| 対称性 | $Z_2$ | $U(1)$ |
| bond 変数 | $\tau_i=s_is_{i+1}$ | $\phi_i=\theta_{i+1}-\theta_i$ |
| 零外場の bond | 独立・離散 | 独立・連続 |
| 転送問題 | $2\times2$ 行列 | 積分作用素 |
| 固有基底 | even/odd | Fourier $m\in\mathbb Z$ |
| 相関を支配 | $\tanh K$ | $I_1(K)/I_0(K)$ |
| 低温相関長 | $\sim e^{2\beta J}$ | $\sim2\beta J$ |
| 有限温度秩序 | なし | なし |

両者の最も重要な共通点は、最近接・零外場では bond 自由度が独立になることにある。最も重要な違いは、Ising の秩序破壊が離散的 defect によるのに対し、XY では連続角度の累積揺らぎによる点である。

## 10. 実在系では easy-plane 磁性の最小模型になる

XY 模型は単なる数学的連続化ではない。結晶場や交換異方性によってスピンがほぼ一つの平面内に拘束される easy-plane 磁性体では、低エネルギー自由度を平面内角度 $\theta_i$ として記述できる。

実際の準1次元磁性体では鎖間結合や量子効果が残るため、純粋な古典1次元 XY 模型が全温度域で厳密に成立するわけではない。しかし

$$
J_{\parallel}\gg J_{\perp}
$$

で、かつ温度が量子効果を平均化できる領域では、鎖方向の短距離相関を理解する基準模型として有効である。

## まとめ

1次元最近接 XY 模型では、角度差 $\phi_i$ を使うと零外場の bond 自由度が独立になり、転送問題は Fourier mode で厳密に対角化できる。

中心となる量は

$$
\boxed{
\rho(K)=\frac{I_1(K)}{I_0(K)}
}
$$

であり、

$$
C(r)=\rho^r,
\qquad
\xi^{-1}=-\ln\rho,
$$

$$
\chi_x(q)
=\frac\beta2
\frac{1-\rho^2}{1-2\rho\cos q+\rho^2}
$$

を同時に支配する。

Ising から XY への変更は、相互作用範囲を伸ばす一般化ではなく、**局所自由度と対称性を $Z_2$ から $U(1)$ へ広げる一般化**である。その結果、domain wall による Arrhenius 型の相関長ではなく、連続角度揺らぎの蓄積による $\xi\sim J/T$ が現れる。
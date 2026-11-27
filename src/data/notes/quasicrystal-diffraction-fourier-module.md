---
title: "準結晶の回折測度とFourier加群"
summary: "Fibonacciモデル集合の自己相関と回折を定義し、高次元逆格子の射影および選択窓のFourier変換からBragg強度を求める。"
publishedAt: 2026-09-12T02:48:00+09:00
updatedAt: 2026-11-28
area: "Physics"
field: quasicrystals
kind: theory
prerequisites: ["fibonacci-cut-and-project", "quasiperiodic-functions-torus"]
topics: ["quasicrystals", "diffraction", "Fourier module", "reciprocal space", "cut and project"]
status: growing
---

Fibonacci点列は周期を持たないが、理想的な無限系の回折は鋭いBraggピークからなる。周期格子との違いは、ピークの鋭さではなく、その位置を指定する整数基底の数にある。これを示すには有限点列の散乱振幅と無限系の回折測度を区別する必要がある。

## 有限点列から自己相関測度へ

点集合 $\Lambda$ をDirac測度

$$
\omega=\sum_{x\in\Lambda}\delta_x
$$

で表す。以下、Fourier変換は $\widehat f(k)=\int f(x)e^{-2\pi ikx}dx$ とする。物理でしばしば用いる角波数は $Q=2\pi k$ である。

長さ $2L$ の区間に制限した測度を $\omega_L$ とすると、散乱振幅は $\widehat\omega_L(k)=\sum_{x\in\Lambda\cap[-L,L]}e^{-2\pi ikx}$ である。無限系での強度を得るためには、単位長さ当たりの自己相関

$$
\gamma=\lim_{L\to\infty}\frac{\omega_L*\widetilde\omega_L}{2L}
$$

を測度の弱い意味（コンパクト台を持つ連続試験関数に対する収束）で定義する。ここで $\widetilde\omega_L(B)=\omega_L(-B)$ である。回折測度は $\widehat\gamma$ となる。

周期格子 $\Lambda=a\mathbb Z$ では、各差 $na$ の出現頻度が $1/a$ なので、

$$
\gamma=\frac1a\sum_{n\in\mathbb Z}\delta_{na},
\qquad
\widehat\gamma=\frac1{a^2}\sum_{m\in\mathbb Z}\delta_{m/a}.
$$

後者はPoisson和公式による。回折測度は点質量の和であり、各点の係数が積分強度である。

## Fibonacci点列の自己相関

[Fibonacci点列の射影構成](/notes/fibonacci-cut-and-project/)と同じ座標を使う。$\tau=(1+\sqrt5)/2$、$D=\sqrt{1+\tau^2}$ とし、

$$
\mathcal L=\left\{\left(\frac{m+\tau n}{D},\frac{-\tau m+n}{D}\right):
m,n\in\mathbb Z\right\}
$$

とする。格子密度は1である。内部窓 $W=[0,w)$、$w=(1+\tau)/D$ に対して

$$
\Lambda=\{x:(x,x^\star)\in\mathcal L,\ x^\star\in W\}.
$$

物理方向の射影が単射なので、格子の物理座標 $z$ に対応する内部座標 $z^\star$ が一意に定まる。

差 $z$ を持つ二点がともに採用される条件は、第一の点の内部座標が $W\cap(W-z^\star)$ に属することである。内部座標の一様分布から、単位物理長さ当たりの対の頻度は

$$
\eta(z)=|W\cap(W-z^\star)|=(w-|z^\star|)_+
$$

となる。ただし $(x)_+=\max(x,0)$ である。従って

$$
\gamma=\sum_{z\in\pi_\parallel(\mathcal L)}\eta(z)\delta_z.
$$

$z=0$ の係数は $w$ であり、点密度に等しい。

## 回折と高次元逆格子

逆格子を、全ての $\mathbf r\in\mathcal L$ に対し $\mathbf K\cdot\mathbf r\in\mathbb Z$ となる集合 $\mathcal L^*$ と定義する。今回は整数格子を直交変換しているので $\mathcal L^*=\mathcal L$ である。

正則モデル集合の回折定理によれば、内部窓がコンパクトな閉包を持ち、その境界のLebesgue測度がゼロである場合、回折は純点型になる。今回の区間窓はこの条件を満たす。強度は一般に格子密度の二乗と窓のFourier変換の絶対値二乗の積となる。

具体的には、自己相関の係数を内部空間の窓関数の自己畳み込み

$$
\eta(z)=(1_W*\widetilde{1_W})(z^\star)
$$

と表し、高次元格子にPoisson和公式を適用すると

$$
\widehat\gamma=\sum_{(k,k^\star)\in\mathcal L^*}
|\widehat{1_W}(k^\star)|^2\delta_k
$$

を得る。ここでは格子密度1を用いた。この操作は測度の意味で行う必要があり、通常の絶対収束する関数の級数として扱うことはできない。

区間窓について積分を評価すると

$$
\widehat{1_W}(u)=e^{-\pi iuw}\frac{\sin(\pi uw)}{\pi u}
$$

であり、$u=0$ では極限値 $w$ を取る。従って整数対 $(m,n)$ に対応するピーク位置と強度は

$$
\begin{aligned}
k_{mn}&=\frac{m+\tau n}{D},\\
k^\star_{mn}&=\frac{-\tau m+n}{D},\\
I_{mn}&=w^2\operatorname{sinc}^2(\pi w k^\star_{mn}),
\qquad \operatorname{sinc}(t)=\frac{\sin t}{t}.
\end{aligned}
$$

窓を平行移動してもFourier変換の位相だけが変化するため、強度は変わらない。原点の強度は $I_{00}=w^2$、すなわち点密度の二乗である。

![周期格子と準周期点列の回折](/figures/quasicrystals/diffraction-fourier-module.svg)

*周期格子の等間隔ピークと準周期構造の波数加群の模式的比較。既存図の計算条件は別途照合する。*

## 稠密なピーク候補と純点回折

位置の候補集合

$$
\mathcal M=\frac1D(\mathbb Z+\tau\mathbb Z)
$$

は階数2の整数加群であり、実軸上で稠密である。ただし強度は内部波数によって決まる。物理波数を有限区間に制限すると、大きな整数指標を持つピークでは内部波数が大きくなり、強度は区間窓のFourier変換の減衰に従って小さくなる。

また、窓のFourier変換の零点ではピークは消滅する。したがって許容波数加群、非零の点質量を持つ波数の集合、回折測度の位相的な台を区別する必要がある。純点測度であっても、点質量が稠密なら位相的な台は区間全体になりうる。

Braggピークの存在は全散乱体が厳密に同位相であることを要求しない。Fibonacci点列では高次元逆格子との整合性が平均散乱振幅を非零にする。有限系で観測されるピークの幅は系の大きさや分解能にも依存する。

決定論的な非周期点列が全て純点回折を持つわけではない。ここで純点型となるのは正則モデル集合の条件を満たすためであり、非周期性だけから導かれる性質ではない。

## 参考文献

- M. Baake and U. Grimm, *Aperiodic Order, Vol. 1: A Mathematical Invitation*, Cambridge University Press (2013).
- R. V. Moody, “Model sets: A survey,” in *From Quasicrystals to More Complex Systems* (2000).

正則モデル集合の回折定理を既知の結果として使用した。定理の仮定と書誌の原典照合、既存図の数値再現は公開前に行う。

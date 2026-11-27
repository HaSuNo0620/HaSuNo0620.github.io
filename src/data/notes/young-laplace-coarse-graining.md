---
title: "Young–Laplace式と鋭い界面の力学"
summary: "表面応力による力の釣り合いと面積変分からYoung–Laplace式を導き、鋭い界面近似の成立条件を整理する。"
publishedAt: 2026-09-09T19:06:00+09:00
updatedAt: 2026-11-28
area: "Physics"
field: interfaces
kind: theory
related: ["gibbs-to-tolman-gauge-curvature", "kirkwood-buff-stress-anisotropy"]
topics: ["interfacial physics", "capillarity", "coarse graining", "Young-Laplace"]
status: growing
---

球形液滴の内部圧力が外部より高いのは、界面に沿う張力が曲率によって内向きの合力を持つためである。Young–Laplace式は、この力の釣り合いを界面の厚さを陽に扱わずに記述する。

## 球形界面の力の釣り合い

二つの静止した流体相を $\alpha,\beta$ とし、単位法線 $\mathbf n$ は $\alpha$ から $\beta$ へ向ける。圧力差を $\Delta p=p^\alpha-p^\beta$ と定義する。半径 $R$ の球形液滴では内側を $\alpha$ とする。

赤道面で半球を切り出すと、圧力差による軸方向の力は $\Delta p\,\pi R^2$、切断円周に沿う表面張力の合力は $2\pi R\gamma$ である。重力を無視し、表面張力が一様なら

$$
\Delta p\,\pi R^2=2\pi R\gamma,\qquad
\Delta p=\frac{2\gamma}{R}.
$$

円柱状界面では、単位軸長当たりの半円柱の力の釣り合いから $\Delta p=\gamma/R$ を得る。球と円柱で係数が異なるのは、曲率を持つ方向の数が異なるためである。

![上半球を切り出した模式図](/figures/interfaces/young-laplace-hemisphere.svg)

*上半球を切り出した模式図。赤道面での圧力差による力と、切断円周に沿う表面張力の合力が釣り合う。矢印の長さは力の実測値ではない。*

## 一般曲面における表面応力

曲面上の接線射影を $\mathbf P=\mathbf I-\mathbf n\mathbf n$ とする。等方的な流体界面の表面応力は $\boldsymbol{\tau}_s=\gamma\mathbf P$ と表せる。主曲率の和を $C=\nabla_s\cdot\mathbf n=R_1^{-1}+R_2^{-1}$ と定義する。この規約では外向き法線を持つ球について $C=2/R>0$ である。

曲面片の境界を通して作用する線力の面積当たりの合力は

$$
\nabla_s\cdot\boldsymbol{\tau}_s=\nabla_s\gamma-\gamma C\mathbf n.
$$

流体のCauchy応力を $\boldsymbol{\sigma}^\alpha,\boldsymbol{\sigma}^\beta$ とすれば、界面の慣性と外部からの面力を無視した釣り合いは

$$
(\boldsymbol{\sigma}^\beta-\boldsymbol{\sigma}^\alpha)\mathbf n
+\nabla_s\cdot\boldsymbol{\tau}_s=0.
$$

静止した等方的流体では $\boldsymbol{\sigma}=-p\mathbf I$ であるから、法線成分より

$$
p^\alpha-p^\beta=\gamma C
$$

を得る。接線成分からは $\nabla_s\gamma=0$ が必要となる。表面張力勾配が存在する場合には接線方向の応力差などが必要であり、一般にはMarangoni流を含む流体力学の問題になる。

重力下では各相の圧力は $-\nabla p+\rho_m\mathbf g=0$ を満たす。ここで $\rho_m$ は質量密度である。例えば円管内の毛管上昇では、液面の圧力差と静水圧差が対応する。液体と気体の質量密度差を $\Delta\rho_m$ とすると、上昇高さ $h$ に対する圧力差の大きさは $\Delta\rho_m gh$ である。

## 熱力学的変分

面積当たりの表面自由エネルギー $\gamma$ を一定として、二つの流体相の間の界面を法線方向へ微小変位 $u(\mathbf x)$ だけ動かす。閉じた界面の一次変分は

$$
\delta V^\alpha=\int_A u\,dA,\qquad
\delta A=\int_A C u\,dA.
$$

固定温度・化学ポテンシャルの鋭い界面模型のグランドポテンシャルは

$$
\Omega=-p^\alpha V^\alpha-p^\beta V^\beta+\gamma A.
$$

外部容器の体積を固定すると $\delta V^\beta=-\delta V^\alpha$ なので、

$$
\delta\Omega=\int_A(-\Delta p+\gamma C)u\,dA.
$$

任意の許容変位に対する停留条件から、力学的導出と同じYoung–Laplace式が得られる。これは停留条件であって安定性を保証する条件ではない。例えば過飽和相中の臨界液滴は、半径方向の自由エネルギーの極大に対応しうる。

この導出では、曲率によらない局所面積エネルギーを仮定している。曲率依存の自由エネルギーや曲げモーメントを含む場合、単に $\gamma$ を任意の半径依存関数に置き換えるだけでは変分は完結しない。また、固体界面の表面応力と面積当たりの表面自由エネルギーは一般に異なる。

## 界面内部を省略できる条件

分子系の界面は有限幅を持ち、密度や圧力テンソルが法線方向に変化する。平面流体界面では、適切な局所圧力の定義の下で

$$
\gamma_\infty=\int_{-\infty}^{\infty}[P_N(z)-P_T(z)]\,dz
$$

となる。この積分を分子間力から求める方法は[Kirkwood–Buffの理論](/notes/kirkwood-buff-stress-anisotropy/)で扱う。

界面幅を $w$、曲率半径や面内変化の代表長さを $L$ とすれば、平面界面の張力を用いる鋭い界面近似には $w/L\ll1$ が必要になる。ただし、長距離相互作用、外部場、界面間の相互作用などによる寄与が無視できることも必要である。

Young–Laplace式から密度分布や応力分布を逆に決定することはできない。有限幅の界面を熱力学的な面として定義する方法と、曲率による表面張力の変化は、[Gibbsの界面熱力学](/notes/gibbs-to-tolman-gauge-curvature/)および曲率依存表面張力の記事で扱う。

## 参考文献

- T. Young, *An Essay on the Cohesion of Fluids* (1805).
- P.-S. Laplace, *Mécanique Céleste*, Livre X, supplement on capillary action (1806).
- L. M. Siqveland and S. M. Skjaeveland, “Derivations of the Young-Laplace equation” (2021).

歴史的な記述と文献の詳細は原典照合時に確認する。

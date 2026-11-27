---
title: "周期結合Ising鎖の空間相関と応答モードの混合"
summary: "周期的な最近接結合の厳密相関を求め、AABB鎖の構造因子と単位胞内の感受率行列を解析する。"
publishedAt: 2026-09-12T01:34:00+09:00
updatedAt: 2026-11-28
area: "Physics"
field: statistical-physics
kind: model
prerequisites: ["ising-transfer-matrix"]
related: ["ising-r2-transfer-matrix", "quasiperiodic-functions-torus"]
topics: ["statistical mechanics", "Ising model", "transfer matrix", "correlation", "periodic modulation", "inhomogeneous systems"]
status: growing
system:
  dimension: 1
  spatial: periodic
  range: R1
  interaction: cosine
  symmetry: [Z2]
  mechanics: classical
  role: model
---

最近接Ising鎖の結合を周期的に変調すると、相互作用距離を延ばさなくても有限波数の構造が生じる。零外場では結合変数の独立性が保たれるが、外場応答には単位胞内の結合配置が反映される。ここではAABB型の周期構造を例に、その関係を厳密に調べる。

## 零外場の自由エネルギーと相関

$$
H=-\sum_i J_i s_i s_{i+1},\qquad s_i=\pm1,\quad J_{i+p}=J_i
$$

とし、格子間隔を1、逆温度を $\beta=(k_{\mathrm B}T)^{-1}$ とする。

![一様鎖と周期結合鎖](/figures/ising-r1-periodic/overview-uniform-periodic.svg)

結合変数 $\tau_i=s_i s_{i+1}$ を使えば $H=-\sum_iJ_i\tau_i$ となる。開鎖では結合変数が独立であり、強磁性的な結合 $J_i>0$ にドメイン壁を作る確率は $(1+e^{2\beta J_i})^{-1}$ である。周期境界では $\prod_i\tau_i=1$ の制約が加わる。以下の相関は熱力学極限において考える。

![結合の周期変調とドメイン壁](/figures/ising-r1-periodic/domain-wall-periodic.svg)

零外場の転送行列は

$$
T_i=e^{\beta J_i}I+e^{-\beta J_i}\sigma_x
$$

であり、位置によらず共通の固有ベクトルを持つ。一周期の積の固有値は

$$
\Lambda_\pm=\prod_{i=1}^p(e^{\beta J_i}\pm e^{-\beta J_i}).
$$

自由エネルギー密度 $f=-(\beta p)^{-1}\ln\Lambda_+$ は、一周期に含まれる結合の並び順に依存しない。

一方、二点相関は

$$
C_i(r)=\langle s_i s_{i+r}\rangle=\prod_{n=0}^{r-1}t_{i+n},
\qquad t_i=\tanh(\beta J_i)
$$

なので、単位胞内部での順序に依存する。$B=\prod_{i=1}^p t_i$、$r=mp+s$、$0\le s<p$ とすると

$$
C_i(mp+s)=B^m\prod_{n=0}^{s-1}t_{i+n}.
$$

$0<|B|<1$ なら相関長は $\xi^{-1}=-p^{-1}\ln|B|$ である。$B=0$ の場合はゼロ結合をまたぐ相関が消えるため、指数包絡による表示を別扱いする。

$B>0$ のとき指数包絡を除いた相関は周期 $p$ を持つ。$B<0$ なら一周期進むごとに符号が変化する。両者をまとめると

$$
C_i(r)=e^{-r/\xi}\sum_{m=0}^{p-1}A_m^{(i)}
e^{i(2\pi m+\arg B)r/p},\qquad r\ge0.
$$

ここで $\arg B=0$ または $\pi$ である。これらは相関の周期成分の波数であり、構造因子の最大位置が必ずいずれかに一致するわけではない。

![指数包絡と単位胞内部の変調](/figures/ising-r1-periodic/correlation-envelope-modulation.svg)

## AABB鎖の構造因子

AABBというサイト配列に対応する一周期の結合を $J_{AA},J_{AB},J_{BB},J_{AB}$ とする。

![AABB鎖の結合配置](/figures/ising-r1-periodic/aabb-bond-pattern.svg)

$a=\tanh(\beta J_{AA})$、$b=\tanh(\beta J_{AB})$、$c=\tanh(\beta J_{BB})$ とすれば $B=ab^2c$ である。周期の先頭からの相関は $B^m(1,a,ab,abc)$ という4成分で表される。

特に $J_{AA}=J_{BB}=J>0$、$J_{AB}=-|K|<0$ とする。この場合、結合そのものの最小周期は2であり、AABBの4サイト胞はサイト種別と外場を記述するための胞である。全結合を満たすスピン配置は $++--$ の周期4となる。

$t=\tanh(\beta J)$、$v=\tanh(\beta|K|)$ とおく。原点平均した相関 $\bar C(r)=p^{-1}\sum_i C_i(r)$ は

$$
\bar C(2n)=(-tv)^n,\qquad
\bar C(2n+1)=\frac{t-v}{2}(-tv)^n.
$$

幾何級数を評価すると構造因子は

$$
S(k)=\sum_{r\in\mathbb Z}\bar C(r)e^{-ikr}
=\frac{(1+tv)[1-tv+(t-v)\cos k]}{(1-tv)^2+4tv\cos^2 k}.
$$

$S$ を $x=\cos k$ の関数とみなし、内部の極大を求めると

$$
x_*=\frac{(1-tv)(\sqrt t-\sqrt v)}
{2\sqrt{tv}(\sqrt t+\sqrt v)}.
$$

$t,v>0$ の場合、$x_*$ が区間外なら対応する端点が最大となる。すなわち $k_*=\arccos[\max(-1,\min(1,x_*))]$ である。低温では $t,v\to1$ なので $k_*\to\pi/2$ となる。高温では短距離の結合が相対的に強く反映される。

![AABB鎖の最大構造因子波数](/figures/ising-r1-periodic/kstar-temperature.svg)

一様第二近接Ising鎖の有限波数構造は、同時に満足できない異なる距離の相互作用から生じる。周期結合鎖では各結合を満たす符号配置が空間構造を与える。この二つは同じ周期4の配置を持ちうるが、その起源は異なる。

![周期結合と競合相互作用の比較](/figures/ising-r1-periodic/periodic-r1-vs-uniform-r2.svg)

## 外場下の一周期転送行列

位置依存外場 $-\sum_i h_i s_i$ を加える。結合変数だけでは外場項を局所的に書けないため、絶対スピンを転送状態とする。

$$
T_i(s,s')=\exp\left[\beta J_i ss'+\frac{\beta}{2}(h_i s+h_{i+1}s')\right].
$$

局所行列は一般に可換ではない。しかし結合と外場が共通の整数周期 $p$ を持てば、一周期の積 $M=T_1\cdots T_p$ によって厳密に扱える。

![外場による転送行列の非可換化](/figures/ising-r1-periodic-field/noncommuting-transfer.svg)

$\Theta=\operatorname{Tr}M$、$D=\det M$ とすると、

$$
\Lambda_\pm=\frac{\Theta\pm\sqrt{\Theta^2-4D}}2,\qquad
D=\prod_{i=1}^p2\sinh(2\beta J_i).
$$

行列式は外場に依存しない。単位胞内の磁化は

$$
m_\alpha=\frac1\beta\frac{\partial\ln\Lambda_+}{\partial h_\alpha}
$$

となる。各 $h_\alpha$ は全単位胞で繰り返される外場である。

一般の線形応答を扱う場合、単位胞番号 $n$ と内部サイト $\alpha$ を分け、セル間のBloch波数と内部Fourier成分を区別する。以下ではセル間波数ゼロ、すなわち外場が各4サイト胞で反復する場合の二つの内部モードに限定する。

![単位胞内の外場成分](/figures/ising-r1-periodic-field/field-fourier-coupling.svg)

## 対称AABB鎖の二つの外場モード

$J_{AA}=J_{BB}=J$、$J_{AB}=K$ とし、外場を

$$
(h_1,h_2,h_3,h_4)=h_0(1,1,1,1)+h_d(1,1,-1,-1)
$$

とする。対応する磁化を $m_0=(m_1+m_2+m_3+m_4)/4$、$m_d=(m_1+m_2-m_3-m_4)/4$ と定義する。

![一様外場と周期4外場](/figures/ising-r1-periodic-field/aabb-field-modes.svg)

$\mathcal J=\beta J$、$\mathcal K=\beta K$、$u=\beta h_0$、$d=\beta h_d$ と書くと、一周期のトレースは

$$
\begin{aligned}
\Theta(u,d)={}&4e^{-2\mathcal J}\cosh(2\mathcal K)
+2e^{2\mathcal J+2\mathcal K}\cosh(4u)\\
&+2e^{2\mathcal J-2\mathcal K}\cosh(4d)
+8\cosh(2u)\cosh(2d).
\end{aligned}
$$

これは4サイトの全16配置のBoltzmann重みを合計して求められる。$D=16\sinh^2(2\mathcal J)\sinh^2(2\mathcal K)$、$L=\sqrt{\Theta^2-4D}$ とすれば、$\partial_u\ln\Lambda_+=\partial_u\Theta/L$ である。したがって

$$
m_0=\frac{2e^{2\mathcal J+2\mathcal K}\sinh4u+4\sinh2u\cosh2d}{L},
$$

$$
m_d=\frac{2e^{2\mathcal J-2\mathcal K}\sinh4d+4\cosh2u\sinh2d}{L}.
$$

零外場の感受率は

$$
\chi_{00}=\beta\frac{e^{\mathcal J+\mathcal K}}{\cosh(\mathcal J-\mathcal K)},
\qquad
\chi_{dd}=\beta\frac{e^{\mathcal J-\mathcal K}}{\cosh(\mathcal J+\mathcal K)},
\qquad \chi_{0d}=0.
$$

交差項が消えるのは、2サイト並進で一様モードは不変、周期4モードは符号反転するためである。$K>0$ ではこの二モードのうち一様応答が大きく、$K<0$ では周期4応答が大きい。

![二つの感受率の温度依存性](/figures/ising-r1-periodic-field/susceptibility-channels.svg)

## 非対称AABB鎖でのモード混合

$J_{AA}\ne J_{BB}$ では2サイト並進対称性が失われる。$\mathcal A=\beta J_{AA}$、$\mathcal B=\beta J_{BB}$ と書き、

$$
F=\cosh(\mathcal A+\mathcal B)\cosh2\mathcal K+\cosh(\mathcal A-\mathcal B),
$$

$$
L_0=\sqrt{F^2-\sinh2\mathcal A\,\sinh2\mathcal B\,\sinh^22\mathcal K}
$$

とする。零外場で $\Theta_0=8F$、$\sqrt{\Theta_0^2-4D}=8L_0$ である。トレースを外場について二階微分すると、制限した二モード空間での感受率は

$$
\boldsymbol\chi=\frac{\beta}{L_0}
\begin{pmatrix}
\cosh(\mathcal A-\mathcal B)+e^{\mathcal A+\mathcal B+2\mathcal K}&\sinh(\mathcal A-\mathcal B)\\
\sinh(\mathcal A-\mathcal B)&\cosh(\mathcal A-\mathcal B)+e^{\mathcal A+\mathcal B-2\mathcal K}
\end{pmatrix}.
$$

これは同じスピン胞の外場と磁化の規格化を採用した対称行列である。対角化すると、最大応答の外場方向は一様・周期4モードの線形結合となる。固有値は

$$
\chi_\pm=\frac{\chi_{00}+\chi_{dd}}2
\pm\sqrt{\left(\frac{\chi_{00}-\chi_{dd}}2\right)^2+\chi_{0d}^2}.
$$

最大固有値に対応する方向の角度は

$$
2\vartheta=\operatorname{atan2}(2\chi_{0d},\chi_{00}-\chi_{dd})
$$

で求められる。縮退時には方向は一意ではない。

$\mathcal A=\mathcal B$ で交差項が消え、$\mathcal K=0$ で対角成分が一致する。両条件が同時に成立すれば固有値が縮退する。この分類は感受率行列の構造を表すものであり、有限温度の相図ではない。

![応答モードの構造マップ](/figures/ising-r1-periodic-field/response-structure-map.svg)

## 周期を変える場合

外場下の連結相関は、一周期行列の固有値比 $\Lambda_-/\Lambda_+$ の寄与を含む。振幅が非零なら包絡の相関長は

$$
\xi^{-1}=-p^{-1}\ln|\Lambda_-/\Lambda_+|
$$

となる。結合周期 $p_J$ と外場周期 $p_h$ が異なっても、両者が有限整数なら最小公倍数の周期を使える。

![周期結合鎖と第二近接鎖の外場応答](/figures/ising-r1-periodic-field/periodic-r1-vs-r2-field.svg)

有限単位胞のない準周期結合やランダム結合に対しても、零外場の最近接模型では $\langle s_i s_j\rangle=\prod_{n=i}^{j-1}\tanh(\beta J_n)$ が成立する。周期結合鎖は、この積構造と単位胞内の応答を切り分けて扱える例である。

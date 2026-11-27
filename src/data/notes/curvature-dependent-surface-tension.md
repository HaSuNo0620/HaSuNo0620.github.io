---
title: "曲率依存表面張力とGibbsの代表面"
summary: "固定状態での分割面移動と液滴の物理的なサイズ変化を区別し、張力面、等モル面、Tolman長、局所応力モーメントの関係を整理する。"
publishedAt: 2026-11-28
area: "Physics"
field: interfaces
kind: theory
topics: ["interfacial physics", "surface tension", "Gibbs dividing surface", "Tolman length"]
status: growing
prerequisites: ["gibbs-to-tolman-gauge-curvature", "young-laplace-coarse-graining"]
related: ["kirkwood-buff-stress-anisotropy", "van-der-waals-diffuse-interface"]
---

曲率を持つ有限幅の界面では、表面張力をどの半径で定義するかが問題になる。分割面を移動する操作は同じ液滴の記述を変更するだけだが、液滴自体の大きさを変える操作は熱力学状態を変える。この二つの微分を区別する。

## 球形分割面の移動

一成分の球形液滴を考え、内相を $\alpha$、外相を $\beta$ とする。温度と化学ポテンシャルが共通であり、バルク圧力 $p^\alpha,p^\beta$ が定義できると仮定する。半径 $R$ の仮想分割面に対して

$$
\Omega=-p^\alpha V^\alpha(R)-p^\beta V^\beta(R)+4\pi R^2\gamma(R)
$$

と定義する。全容器体積と物理状態を固定して $R$ だけ変えると $\Omega$ は変化しない。従って

$$
\Delta p=\frac{2\gamma(R)}{R}
+\left[\frac{\partial\gamma}{\partial R}\right]_{\rm state},
\qquad \Delta p=p^\alpha-p^\beta.
$$

張力面の半径 $R_s$ は、この仮想微分がゼロになる半径である。その位置では

$$
\Delta p=\frac{2\gamma_s}{R_s},\qquad \gamma_s=\gamma(R_s).
$$

固定した一つの液滴について、上の微分方程式を積分すると

$$
\gamma(R)=\frac{\Delta p}{3}R+\frac{B}{R^2}
$$

となる。ここで $B$ は物理状態で決まる積分定数である。張力面が存在する場合、$\Delta p=2\gamma_s/R_s$ を代入して

$$
\frac{\gamma(R)}{\gamma_s}=\frac23\frac R{R_s}
+\frac13\left(\frac{R_s}{R}\right)^2
$$

を得る。この式は一つの物理状態について分割面を変更した場合の関係であり、異なる半径の液滴の表面張力を結ぶ曲率依存則ではない。

## 等モル面

分割面に対して過剰粒子数を

$$
N^\sigma(R)=N-\rho^\alpha V^\alpha(R)-\rho^\beta V^\beta(R)
$$

と定義する。等モル半径 $R_e$ は $N^\sigma(R_e)=0$ を満たす半径である。張力面での表面過剰量は

$$
\Gamma_s=\frac{N^\sigma(R_s)}{4\pi R_s^2}
=\frac{\rho^\alpha-\rho^\beta}{3R_s^2}(R_e^3-R_s^3).
$$

$\delta(R_s)=R_e-R_s$ と書けば

$$
\frac{\Gamma_s}{\rho^\alpha-\rho^\beta}
=\delta+\frac{\delta^2}{R_s}+\frac{\delta^3}{3R_s^2}.
$$

等モル面と張力面は異なる条件によって定められる。

## 物理状態の変化とTolmanの関係

次に、一定温度で化学ポテンシャルを変え、球形の平衡液滴の系列を考える。張力面では分割面の仮想微分が消えるため、過剰グランドポテンシャルの微分から

$$
d\gamma_s=-\Gamma_s\,d\mu
$$

を得る。これは分割面を固定状態で動かす微分ではなく、平衡状態の系列に沿う微分である。バルクのGibbs–Duhem関係より

$$
d\Delta p=(\rho^\alpha-\rho^\beta)d\mu.
$$

張力面のLaplace関係を微分すると

$$
d\Delta p=\frac{2}{R_s}d\gamma_s-\frac{2\gamma_s}{R_s^2}dR_s.
$$

$L=\Gamma_s/(\rho^\alpha-\rho^\beta)$ とすれば

$$
\frac{d\ln\gamma_s}{dR_s}
=\frac{2L}{R_s(R_s+2L)}.
$$

平面極限で $\delta(R_s)$ が有限値 $\delta_\infty$ に収束し、十分滑らかな大半径展開が存在すると仮定する。$L\to\delta_\infty$ なので、

$$
\gamma_s(R_s)=\gamma_\infty
\left(1-\frac{2\delta_\infty}{R_s}+o(R_s^{-1})\right).
$$

この $\delta_\infty$ がここでの符号規約におけるTolman長である。有限半径で $\delta$ を一定と仮定することは追加近似であり、熱力学の恒等式から要求されるわけではない。液滴と気泡を比較する場合には法線方向と曲率の符号規約を整合させる必要がある。

## 平面応力のモーメントとの関係

平面界面で $\Pi(z)=P_N(z)-P_T(z)$ とすると、$\gamma_\infty=\int\Pi(z)dz$ である。ある局所応力の規約を選べば一次モーメント

$$
M_1=\int z\Pi(z)dz
$$

を定義できる。座標を $z'=z+a$ と表示し直すと $M_1'=M_1+a\gamma_\infty$ となる。従って $\gamma_\infty\ne0$ なら $z_m=M_1/\gamma_\infty$ はその応力分布の重心に相当する。

しかし局所応力を $\Pi'(z)=\Pi(z)+f'(z)$ と変更できる場合、境界で $f$ が消えれば積分値は変わらず、一次モーメントは $-\int f(z)dz$ だけ変化する。この例は、ゼロ次モーメントが同じであることから一次モーメントの不変性が従わないことを示す。任意の $f$ が分子系で許される応力経路に対応するという主張ではない。

座標原点の変更、Gibbs分割面の変更、局所応力の分配規約の変更は別の操作である。熱力学的に定義した $R_s$ と局所応力の重心を同一視するには、採用した応力の定義と変形仕事の関係を別途検証する必要がある。

## 曲率補正の測定

曲率依存性を数値的に評価するには、異なる平衡液滴について密度から $R_e$ を、圧力差と過剰グランドポテンシャルから張力面と $\gamma_s$ を決定する方法が考えられる。圧力差だけから $R_s$ と $\gamma_s$ の双方を独立に求めることはできない。自由エネルギー測定や別の代表面条件が必要となる。

有限の閉鎖系では、液滴サイズを変えることでバルク密度や化学ポテンシャルも変化しうる。曲率だけを変化させたと解釈する前に、比較する平衡状態の系列と参照バルクの状態を明示する必要がある。

## 参考文献

- R. C. Tolman, “The Effect of Droplet Size on Surface Tension,” *Journal of Chemical Physics* **17**, 333–337 (1949).
- J. S. Rowlinson and B. Widom, *Molecular Theory of Capillarity*, Clarendon Press (1982).

- E. M. Blokhuis and D. Bedeaux, [Pressure Tensor of a Spherical Interface](https://scholarlypublications.universiteitleiden.nl/handle/1887/81494) (1992).
- E. M. Blokhuis and J. Kuipers, [Thermodynamic expressions for the Tolman length](https://doi.org/10.1063/1.2167642) (2006).

有限半径のTolman方程式は既存の熱力学的表現と照合した。BlokhuisとBedeauxの論文の抄録は、力学的代表面の距離と熱力学的Tolman長の単純な同一視を支持しない。原論文全文の式番号単位の照合は未完了である。

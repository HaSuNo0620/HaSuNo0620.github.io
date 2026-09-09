---
title: "GibbsからTolmanへ — 界面のゲージ自由度と曲率"
summary: "Gibbs dividing surfaceの任意性を記述のゲージ冗長性として読み、surface excessの不変量、equimolar surface、surface of tension、Tolman lengthまでを一つの流れで整理する。"
publishedAt: 2026-09-09T20:11:00+09:00
area: "Physics"
topics: ["interfacial physics", "surface thermodynamics", "Gibbs dividing surface", "gauge redundancy", "Tolman length"]
status: growing
---

[前のNote](/notes/young-laplace-coarse-graining/)では、Young–Laplace式を、界面内部の複雑な構造を表面張力 $\gamma$ という一個の量へ縮約した**力学的な界面法則**として捉えた。

$$
\Delta p
=
\gamma\left(\frac{1}{R_1}+\frac{1}{R_2}\right).
$$

ここでは、その次にGibbsが何を加え、さらにTolmanが曲率の問題をどのように持ち込んだのかを一つの流れとして整理する。

自分の中での中心的な見方は次である。

**Gibbsは界面の位置に任意性を許し、その任意性に依存しない熱力学だけを残した。Tolmanは、曲率を入れると異なる物理的条件が異なる代表面を選ぶことを示した。**

## Young–LaplaceからGibbsへ

Young–Laplaceでは、表面張力 $\gamma$ が与えられれば界面の力学は閉じる。

しかし、たとえば溶液の組成を変えたときに、なぜ $\gamma$ が変化するのかはこの式だけでは分からない。

Gibbsが行ったのは、$\gamma$ を単なる力学的パラメータとして使うだけではなく、界面へエネルギー、エントロピー、物質量などの**surface excess**を割り当て、界面を熱力学の中へ組み込むことであった。

ただしGibbsは、界面の密度プロファイルを直接解こうとはしなかった。

実際の界面では密度は有限幅で

$$
\rho^\alpha
\longrightarrow
\rho^\beta
$$

と変化する。そこで「どこまでが相 $\alpha$ で、どこからが相 $\beta$ か」を分子レベルで一意に決めることは難しい。

Gibbsはこの問題に対して、界面領域の境界を決めるのではなく、任意の位置に厚さゼロの数学的な面を置いた。

これが **Gibbs dividing surface** である。

## surface excessは実在する界面層の粒子数ではない

平面界面を考え、dividing surfaceを $z=z_0$ に置く。

成分 $i$ の参照密度を

$$
\rho_{i,\mathrm{ref}}(z)
=
\begin{cases}
\rho_i^\alpha, & z<z_0,\\
\rho_i^\beta, & z>z_0
\end{cases}
$$

とする。

実際の密度 $\rho_i(z)$ との差を積分して、面積あたりのsurface excessを

$$
\Gamma_i(z_0)
=
\int_{-\infty}^{z_0}
\left[\rho_i(z)-\rho_i^\alpha\right]dz
+
\int_{z_0}^{\infty}
\left[\rho_i(z)-\rho_i^\beta\right]dz
$$

と定義する。

ここで重要なのは、$\Gamma_i$ が「界面スラブの中に実際に存在する分子数」ではないことである。

それは

$$
\text{real system}
-
\text{two extrapolated bulk phases}
$$

という**差分量**である。

したがって、厚さゼロのsurface phaseに

$$
N_i^\sigma\neq0
$$

が割り当てられても矛盾しない。

## dividing surfaceを動かすとexcessは変わる

$z_0$ を

$$
z_0\rightarrow z_0+\delta z
$$

と動かすと、実際の界面は何も変わっていないにもかかわらず、surface excessは

$$
\delta\Gamma_i
=
(\rho_i^\beta-\rho_i^\alpha)\,\delta z
$$

だけ変化する。

ここで

$$
\Delta\rho_i
=
\rho_i^\beta-\rho_i^\alpha
$$

と置けば、

$$
\Gamma_i
\rightarrow
\Gamma_i+\Delta\rho_i\,\delta z.
$$

一見すると、界面の吸着量が任意に変わってしまうように見える。

しかし変わっているのは物理状態ではない。

変わっているのは、同じ実在系を

$$
\text{bulk }\alpha
+
\text{surface}
+
\text{bulk }\beta
$$

へどう分配したかだけである。

## dividing-surface freedomはゲージ冗長性と読める

surface excess vectorを

$$
\boldsymbol{\Gamma}
=
(\Gamma_1,\Gamma_2,\ldots,\Gamma_n)
$$

とする。

するとdividing surfaceの移動は

$$
\boldsymbol{\Gamma}
\rightarrow
\boldsymbol{\Gamma}
+
\lambda\,\Delta\boldsymbol{\rho}
$$

と書ける。

ここで $\lambda$ はdividing surfaceの変位である。

実在する界面は同一なので、物理的に意味を持つのは一つの $\boldsymbol{\Gamma}$ そのものではなく、

$$
[\boldsymbol{\Gamma}]
=
\left\{
\boldsymbol{\Gamma}
+
\lambda\Delta\boldsymbol{\rho}
\right\}
$$

という同値類だと考えられる。

したがって、形式的にはsurface-excess spaceを

$$
\mathbb R^n
/
\operatorname{span}\{\Delta\boldsymbol{\rho}\}
$$

で割った空間に物理情報が存在すると見ることができる。

この意味で、Gibbs dividing surfaceの任意性は単なる曖昧さではなく、**記述のゲージ冗長性**と解釈できる。

ただし、これは標準的な場の理論における局所ゲージ場を導入しているという意味ではない。Gibbs自身がこの言葉を用いたわけでもない。このNoteでは、**同じ物理状態を複数の記述が表し、不変な組合せだけが観測に残るという数学的構造**を「ゲージ」と呼んでいる。

## Gibbs adsorption equationが不変になる理由

界面熱力学では

$$
d\gamma
=
-s^\sigma dT
-
\sum_i\Gamma_i\,d\mu_i
$$

というGibbs adsorption equationが得られる。

ところが $\Gamma_i$ はdividing surfaceに依存する。

それでも式全体が物理的に意味を持つのは、bulkのGibbs–Duhem関係があるからである。

各相について

$$
dp^\alpha
=
s^\alpha dT
+
\sum_i\rho_i^\alpha d\mu_i,
$$

$$
dp^\beta
=
s^\beta dT
+
\sum_i\rho_i^\beta d\mu_i.
$$

平面界面の二相共存に沿っては

$$
dp^\alpha=dp^\beta
$$

なので、

$$
(s^\beta-s^\alpha)dT
+
\sum_i
(\rho_i^\beta-\rho_i^\alpha)d\mu_i
=0.
$$

したがってdividing surfaceを動かしたときにsurface excessへ加わる成分は、許された熱力学的変化に対して寄与しない。

定温なら特に

$$
\Delta\boldsymbol{\rho}
\cdot
 d\boldsymbol{\mu}
=0
$$

であり、

$$
(\boldsymbol{\Gamma}+\lambda\Delta\boldsymbol{\rho})
\cdot d\boldsymbol{\mu}
=
\boldsymbol{\Gamma}\cdot d\boldsymbol{\mu}.
$$

つまりGibbs adsorption equationが見るのは、surface excessの**ゲージ不変な成分**だけである。

## relative adsorptionはゲージ不変量になる

二成分系なら、たとえば

$$
\Gamma_2^{(1)}
=
\Gamma_2
-
\frac{\Delta\rho_2}{\Delta\rho_1}\Gamma_1
$$

という組合せを作れる。

dividing surfaceを動かして

$$
\Gamma_i
\rightarrow
\Gamma_i+\lambda\Delta\rho_i
$$

としても、

$$
\Gamma_2^{(1)}
$$

は変化しない。

したがって、物理的な吸着を考えるときには、absoluteな $\Gamma_i$ よりも、このような**relative adsorption**が本質になる。

## equimolar surfaceは一つのgauge fixingと読める

一成分系では、

$$
N^\sigma=0
$$

となるようにdividing surfaceを選ぶことができる。

球形なら、その半径を $R_e$ と書く。

これが **equimolar surface** である。

この条件は、dividing-surface freedomの中から一つの代表面を選んでいる。

したがって構造的には

$$
N^\sigma=0
$$

を一つの**gauge-fixing condition**と読むことができる。

ただし、equimolar surfaceは「物理的な界面の真の位置」を発見したわけではない。物質量のexcessがゼロになるように選んだ、便利で再現可能な代表面である。

## 曲率を入れるとsurface tension自身もdividing surfaceに依存する

平面界面では、dividing surfaceの位置を動かしても表面張力 $\gamma$ は変わらない。

しかし球形界面では事情が変わる。

半径 $R$ の任意のdividing surfaceを選び、液滴のgrand potentialを概念的に

$$
\Omega
=
-p_l V_l(R)
-p_v V_v(R)
+
\gamma(R)A(R)
$$

と分解する。

実在する液滴を変えずに、帳簿上の半径 $R$ だけを動かす。このnotional changeで $\Omega$ は変わってはならない。

球では

$$
\frac{dV_l}{dR}=A,
\qquad
\frac{dA}{dR}=\frac{2A}{R}.
$$

したがって

$$
0
=
-\Delta p\,A
+
\frac{2\gamma(R)}{R}A
+
A\frac{d\gamma(R)}{dR},
$$

すなわち

$$
\boxed{
\Delta p
=
\frac{2\gamma(R)}{R}
+
\frac{d\gamma(R)}{dR}
}
$$

を得る。

ここでの微分は、物理的に液滴を膨張させる微分ではない。

**同じ液滴に対してdividing surfaceだけを動かしたときのnotional derivative**である。

この式を見ると、任意のdividing surfaceでは通常のYoung–Laplace式はそのまま成立しないことが分かる。

## surface of tensionは力学的に特別な代表面である

特別な半径 $R_s$ で

$$
\left.
\frac{d\gamma}{dR}
\right|_{R=R_s}
=0
$$

となる面を選ぶ。

これが **surface of tension** である。

この面では一般化されたLaplace式が

$$
\Delta p
=
\frac{2\gamma_s}{R_s}
$$

へ戻る。

つまりsurface of tensionは、**Young–Laplaceの力学的形を最も単純にするdividing surface**である。

ゲージという見方を採用するなら、

- equimolar surfaceは物質量の条件で代表面を選ぶ
- surface of tensionは力学的条件で代表面を選ぶ

という、二つの異なるgauge fixingだと読むことができる。

## 二つの自然な代表面は一般に一致しない

重要なのは

$$
R_e\neq R_s
$$

でありうることである。

同じ実在する界面に対して、

- excess particle numberをゼロにする面
- Young–Laplaceを単純化する面

が一致する理由はない。

この差を

$$
\delta(R_s)
=
R_e-R_s
$$

と書く。

大きな液滴、すなわち平面極限で

$$
\boxed{
\delta_\infty
=
\lim_{R_s\to\infty}
(R_e-R_s)
}
$$

と定義される量が、通常いう **Tolman length** である。

このNoteでは符号を

$$
\delta_\infty=R_e-R_s
$$

と固定する。文献によって逆の規約が使われる場合があるので、比較時には注意が必要である。

## Tolman lengthは二つのgauge fixingのずれと読める

この見方を取るとTolman lengthの意味がかなり明確になる。

任意のdividing surfaceの位置そのものは物理量ではない。

しかし、

$$
N^\sigma=0
$$

という条件で選んだ代表面と、

$$
\left.d\gamma/dR\right|_{R_s}=0
$$

という条件で選んだ代表面は、それぞれ一意な物理的処方で定まる。

したがって

$$
R_e-R_s
$$

は、任意のgauge artifactではない。

それは**二つの異なる、物理的に動機づけられたgauge fixingが選ぶ代表面の相対的なずれ**である。

この解釈は標準的な用語ではないが、GibbsからTolmanへの論理を理解するにはかなり有用だと思う。

## Tolmanは曲率によるsurface tensionの変化を導入する

Tolmanの議論では、このずれが大きな液滴におけるsurface tensionの曲率補正へつながる。

平面界面の表面張力を $\gamma_\infty$ とすると、十分大きな球形液滴では

$$
\boxed{
\gamma_s(R_s)
=
\gamma_\infty
\left[
1-
\frac{2\delta_\infty}{R_s}
+
O(R_s^{-2})
\right]
}
$$

と展開される。

つまりYoung–Laplaceで定数として扱っていた $\gamma$ に、初めて

$$
\frac{1}{R}
$$

次数の内部構造情報が戻ってくる。

ただしTolman theoryだけから $\delta_\infty$ の値や符号が決まるわけではない。

それを決めるには、界面内部の密度分布や応力分布、分子相関へ踏み込む必要がある。

## Young–Laplace、Gibbs、Tolmanを一つの流れで見る

この三つを自分の中では次のように整理できる。

### Young–Laplace

界面を張力をもつ幾何学的な面へ縮約し、力学を閉じる。

$$
\text{microscopic interface}
\longrightarrow
\gamma
\longrightarrow
\Delta p.
$$

### Gibbs

その幾何学的な面へ熱力学的excessを割り当てる。

ただしdividing surfaceの位置には任意性を残し、surface invariantsだけを物理として扱う。

$$
\text{profile}
\longrightarrow
\text{surface excesses modulo dividing-surface freedom}.
$$

### Tolman

曲率を入れると、異なる物理的条件が異なる代表面を選ぶことに注目し、そのずれをsurface tensionの曲率依存へ結びつける。

$$
R_e-R_s
\longrightarrow
\delta_\infty
\longrightarrow
\gamma(R).
$$

この意味で、Tolmanは単なるYoung–Laplaceへの経験的補正ではない。

**Gibbsが導入したdividing-surface freedomを曲面上で追跡した結果、界面内部の一次の長さ情報がTolman lengthとして現れた**と見ることができる。

## それでもまだ界面内部は解いていない

GibbsもTolmanも、密度プロファイル

$$
\rho(z)
$$

や応力異方性

$$
P_N(z)-P_T(z)
$$

を第一原理的に求めてはいない。

Gibbsはそれらをsurface excessへ積分し、Tolmanは代表面のずれという一つの長さへ圧縮した。

したがって次に問うべきなのは、

> なぜ実際の界面には有限幅が生まれ、その密度プロファイルは何によって決まるのか。

である。

ここで、界面を初めて空間的に連続な密度場として扱う **van der Waalsのdiffuse-interface theory** へ進むことになる。

## References

- J. W. Gibbs, “On the Equilibrium of Heterogeneous Substances,” *Transactions of the Connecticut Academy of Arts and Sciences* (1876, 1878).
- R. C. Tolman, “Consideration of the Gibbs Theory of Surface Tension,” *Journal of Chemical Physics* **16**, 758–774 (1948), DOI: 10.1063/1.1746994.
- R. C. Tolman, “The Superficial Density of Matter at a Liquid-Vapor Boundary,” *Journal of Chemical Physics* **17**, 118–127 (1949), DOI: 10.1063/1.1747204.
- R. C. Tolman, “The Effect of Droplet Size on Surface Tension,” *Journal of Chemical Physics* **17**, 333–337 (1949), DOI: 10.1063/1.1747247.
- J. C. Berg, “Gibbs adsorption equation for planar fluid–fluid interfaces: Invariant formalism,” *Advances in Colloid and Interface Science* **222**, 600–614 (2015), DOI: 10.1016/j.cis.2014.01.001.
- J. S. Rowlinson and B. Widom, *Molecular Theory of Capillarity*, Clarendon Press (1982).

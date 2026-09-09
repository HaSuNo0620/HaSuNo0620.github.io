---
title: "GibbsからTolmanへ — 界面のゲージ自由度と曲率"
summary: "Gibbs dividing surfaceの任意性を記述のゲージ冗長性として読み、surface excessの不変量、equimolar surface、surface of tension、Tolman lengthまでを一つの流れで整理する。"
publishedAt: 2026-09-09T20:11:00+09:00
updatedAt: 2026-09-09
area: "Physics"
topics: ["interfacial physics", "surface thermodynamics", "Gibbs dividing surface", "gauge redundancy", "Tolman length"]
status: growing
---

[前のNote](/notes/young-laplace-coarse-graining/)では、Young–Laplace式を、界面内部の複雑な構造を表面張力 $\gamma$ という一個の量へ縮約した**力学的な界面法則**として捉えた。球面では $R$ を曲率半径とすれば $\Delta p=2\gamma/R$ となる。

ここでは、その次にGibbsが何を加え、さらにTolmanが曲率の問題をどのように持ち込んだのかを一つの流れとして整理する。

自分の中での中心的な見方は次である。

**Gibbsは界面の位置に任意性を許し、その任意性に依存しない熱力学だけを残した。Tolmanは、曲率を入れると異なる物理的条件が異なる代表面を選ぶことを明確にした。**

## Young–LaplaceからGibbsへ

Young–Laplaceでは、表面張力 $\gamma$ が与えられれば界面の力学は閉じる。しかし、溶液の組成を変えたときに、なぜ $\gamma$ が変化するのかはこの式だけでは分からない。

Gibbsが行ったのは、$\gamma$ を単なる力学的パラメータとして使うだけではなく、界面へエネルギー、エントロピー、物質量などの**surface excess**を割り当て、界面を熱力学の中へ組み込むことであった。

ただしGibbsは、界面の密度プロファイルそのものを直接解こうとはしなかった。実際の界面では密度は有限幅で $\rho^\alpha\to\rho^\beta$ と変化する。そのため、「どこまでが相 $\alpha$ で、どこからが相 $\beta$ か」を分子レベルで一意に決めることは難しい。

Gibbsはこの問題に対して、界面領域の境界を決めるのではなく、任意の位置に厚さゼロの数学的な面を置いた。これが **Gibbs dividing surface** である。

## surface excessは実在する界面層の粒子数ではない

平面界面を考え、dividing surfaceを $z=z_0$ に置く。成分 $i$ の参照密度は、左側ではbulk値 $\rho_i^\alpha$、右側ではbulk値 $\rho_i^\beta$ をそのままdividing surfaceまで外挿したものとする。

実際の密度 $\rho_i(z)$ との差を積分すると、面積あたりのsurface excessは

$$\Gamma_i(z_0)=\int_{-\infty}^{z_0}[\rho_i(z)-\rho_i^\alpha]dz+\int_{z_0}^{\infty}[\rho_i(z)-\rho_i^\beta]dz$$

と書ける。

ここで重要なのは、$\Gamma_i$ が「界面スラブの中に実際に存在する分子数」ではないことである。これは、実在系から二つのbulk相を仮想的に外挿した参照系を引いた**差分量**である。

したがって、厚さゼロのsurface phaseに $N_i^\sigma\neq0$ が割り当てられても矛盾しない。$N_i^\sigma$ は幾何学的な薄膜の中の実粒子数ではなく、bulkだけでは勘定できなかったexcessである。

## dividing surfaceを動かすとexcessは変わる

$z_0$ を $z_0\to z_0+\delta z$ と動かしても、実際の界面は何も変わらない。それにもかかわらずsurface excessは

$$\delta\Gamma_i=(\rho_i^\beta-\rho_i^\alpha)\delta z$$

だけ変化する。

密度差を $\Delta\rho_i=\rho_i^\beta-\rho_i^\alpha$ と定義すれば、変換は

$$\Gamma_i\longrightarrow\Gamma_i+\Delta\rho_i\,\delta z$$

と書ける。

一見すると、界面の吸着量が任意に変わってしまうように見える。しかし変わっているのは物理状態ではない。同じ実在系を「bulk $\alpha$ + surface + bulk $\beta$」へどう分配したかだけである。

## dividing-surface freedomはゲージ冗長性と読める

surface excess vectorを $\boldsymbol{\Gamma}=(\Gamma_1,\ldots,\Gamma_n)$、bulk密度差のベクトルを $\Delta\boldsymbol{\rho}$ と書く。dividing surfaceを $\lambda$ だけ動かすと

$$\boldsymbol{\Gamma}\longrightarrow\boldsymbol{\Gamma}+\lambda\Delta\boldsymbol{\rho}$$

となる。

実在する界面は同一なので、物理的に意味を持つのは一つの $\boldsymbol{\Gamma}$ そのものではなく、$\boldsymbol{\Gamma}+\lambda\Delta\boldsymbol{\rho}$ で互いに移り合う記述の同値類だと考えられる。

形式的には、surface-excess spaceからこの冗長な方向を割った

$$\mathbb R^n/\operatorname{span}\{\Delta\boldsymbol{\rho}\}$$

に物理情報が存在すると見ることができる。

この意味で、Gibbs dividing surfaceの任意性は単なる曖昧さではなく、**記述のゲージ冗長性**と解釈できる。

ただし、これは電磁気学やYang–Mills理論のような局所ゲージ場を導入しているという意味ではない。Gibbs自身がこの言葉を使ったわけでもない。このNoteで「ゲージ」と呼んでいるのは、**同じ物理状態を複数の記述が表し、不変な組合せだけが物理に残る**という構造である。

## Gibbs adsorption equationはなぜゲージ不変なのか

界面熱力学では、Gibbs adsorption equation

$$d\gamma=-s^\sigma dT-\sum_i\Gamma_i d\mu_i$$

が得られる。ところが各 $\Gamma_i$ はdividing surfaceに依存する。

それでも式全体が物理的に意味を持つのは、bulkのGibbs–Duhem関係があるからである。各相では

$$\begin{aligned}dp^\alpha&=s^\alpha dT+\sum_i\rho_i^\alpha d\mu_i,\\ dp^\beta&=s^\beta dT+\sum_i\rho_i^\beta d\mu_i\end{aligned}$$

である。

平面界面の二相共存に沿っては $dp^\alpha=dp^\beta$ なので、

$$(s^\beta-s^\alpha)dT+\sum_i(\rho_i^\beta-\rho_i^\alpha)d\mu_i=0$$

となる。

したがって、dividing surfaceを動かしたときにsurface excessへ加わる $\Delta\boldsymbol{\rho}$ 方向の成分は、許された熱力学的変化に寄与しない。定温では $\Delta\boldsymbol{\rho}\cdot d\boldsymbol{\mu}=0$ であり、実際に

$$(\boldsymbol{\Gamma}+\lambda\Delta\boldsymbol{\rho})\cdot d\boldsymbol{\mu}=\boldsymbol{\Gamma}\cdot d\boldsymbol{\mu}$$

となる。

つまりGibbs adsorption equationが見るのは、surface excessの**ゲージ不変な成分**だけである。

## relative adsorptionはゲージ不変量になる

二成分系なら、relative adsorptionを

$$\Gamma_2^{(1)}=\Gamma_2-\frac{\Delta\rho_2}{\Delta\rho_1}\Gamma_1$$

と書ける。

dividing surfaceを動かして $\Gamma_i\to\Gamma_i+\lambda\Delta\rho_i$ としても $\Gamma_2^{(1)}$ は変化しない。したがって、物理的な吸着を考えるときには、absoluteな $\Gamma_i$ よりも、このような**relative adsorption**が本質になる。

## equimolar surfaceは一つのgauge fixingと読める

一成分系では、$N^\sigma=0$ となるようにdividing surfaceを選ぶことができる。球形ならその半径を $R_e$ と書き、これを **equimolar surface** と呼ぶ。

この条件はdividing-surface freedomの中から一つの代表面を選んでいるので、構造的には $N^\sigma=0$ を一つの**gauge-fixing condition**と読むことができる。

ただしequimolar surfaceは「物理的な界面の真の位置」を発見したわけではない。物質量のexcessがゼロになるように選んだ、便利で再現可能な代表面である。

## 曲率を入れるとsurface tension自身もdividing surfaceに依存する

平面界面では、dividing surfaceの位置を動かしても表面張力 $\gamma$ は変わらない。しかし球形界面では事情が変わる。

半径 $R$ の任意のdividing surfaceを選ぶと、液滴のgrand potentialは

$$\Omega=-p_lV_l(R)-p_vV_v(R)+\gamma(R)A(R)$$

と分解できる。

ここで物理的な液滴自体は固定したまま、帳簿上のdividing surfaceだけを動かす。球では

$$\frac{dV_l}{dR}=A,\qquad \frac{dA}{dR}=\frac{2A}{R}$$

なので、notionalな変化に対して $d\Omega/dR=0$ を課すと

$$\Delta p=\frac{2\gamma(R)}{R}+\left[\frac{d\gamma}{dR}\right]_{\mathrm{notional}}$$

を得る。

角括弧で示した微分は、液滴を物理的に膨張させたときの微分ではない。**同じ液滴に対してdividing surfaceだけを動かしたときのnotional derivative**である。

この式を見ると、任意のdividing surfaceでは通常のYoung–Laplace式 $\Delta p=2\gamma/R$ はそのまま成立しないことが分かる。

## surface of tensionは力学的に特別な代表面である

notional derivativeがゼロになる半径を $R_s$ と書き、これを **surface of tension** と呼ぶ。定義条件は $[d\gamma/dR]_{R_s}=0$ である。

この面では一般化されたLaplace式が

$$\Delta p=\frac{2\gamma_s}{R_s}$$

へ戻る。つまりsurface of tensionは、**Young–Laplaceの力学的形を最も単純にするdividing surface**である。

ゲージという見方を採用するなら、equimolar surfaceは物質量の条件で代表面を選び、surface of tensionは力学的条件で代表面を選ぶ。両者は同じdividing-surface freedomに対する、異なる二つの代表面選択だと読むことができる。

## 二つの自然な代表面は一般に一致しない

重要なのは、一般に $R_e\neq R_s$ でありうることである。同じ実在する界面に対して、excess particle numberをゼロにする面と、Young–Laplaceを単純化する面が一致する理由はない。

有限曲率での二つの面の差を $\delta(R_s)=R_e-R_s$ と書く。この符号規約では、equimolar surfaceがsurface of tensionより外側にあれば $\delta>0$ である。

ここで注意したいのは、$R_e-R_s$ を単なるgauge artifactとは呼べないことである。任意のdividing surface同士の差ではなく、**二つの物理的条件によって選ばれた代表面の差**だからである。

## Tolman length

Tolman lengthは、大きな液滴すなわち平面極限での差 $\delta_\infty=\lim_{R_s\to\infty}(R_e-R_s)$ と定義する。このNoteではこの符号規約を用いる。

Tolmanの理論では、$\delta(R_s)$ が十分滑らかに平面極限へ近づくとき、surface of tensionにおける表面張力は大半径で

$$\gamma_s(R_s)=\gamma_\infty\left[1-\frac{2\delta_\infty}{R_s}+O(R_s^{-2})\right]$$

と展開される。

したがってYoung–Laplaceで定数として扱っていた $\gamma$ に、$1/R_s$ 次の曲率補正が現れる。

ただし、この一次式は大半径での漸近形である。Tolman theoryだけから $\delta_\infty$ の数値や符号が決まるわけでもない。それを決めるには、界面内部の密度分布、応力分布、分子相関などへ踏み込む必要がある。

## ゲージという見方でTolmanをどう読むか

ここまでをゲージという言葉で整理すると、dividing surfaceの任意の選択は記述上の冗長性である。その中で $N^\sigma=0$ はequimolar surfaceを選び、$[d\gamma/dR]_{R_s}=0$ はsurface of tensionを選ぶ。

このためTolman length $\delta_\infty$ は「任意のゲージ選択で変わる量」ではなく、**二つの異なる物理的gauge-fixing prescriptionが選ぶ代表面の相対的なずれの平面極限**と解釈できる。

この表現は標準的な界面熱力学の用語ではないが、GibbsからTolmanへの論理を理解するには有用だと思う。

## Young–Laplace、Gibbs、Tolmanを一つの流れで見る

Young–Laplaceでは、界面を張力をもつ幾何学的な面へ縮約し、$\gamma$ が与えられたときの力学を閉じた。

Gibbsでは、その幾何学的な面へsurface excessを割り当てた。ただしdividing surfaceの位置には任意性を残し、その任意性に依存しないsurface invariantだけを物理として扱った。

Tolmanでは、曲率を入れたときにequimolar surfaceとsurface of tensionという二つの自然な代表面が一般にずれることを利用し、その差をsurface tensionの曲率依存へ結びつけた。

つまり、Young–Laplaceで捨てられていた界面内部の情報の一部が、Tolmanでは $\delta_\infty$ という**長さ**として再び有効理論に現れる。

## それでもまだ界面内部は解いていない

GibbsもTolmanも、密度プロファイル $\rho(z)$ や応力異方性 $P_N(z)-P_T(z)$ を第一原理的に求めてはいない。

Gibbsはそれらをsurface excessへ積分し、Tolmanは代表面のずれという一つの長さへ圧縮した。

したがって次に問うべきなのは、

> なぜ実際の界面には有限幅が生まれ、その密度プロファイルは何によって決まるのか。

である。

ここで、界面を空間的に連続な密度場として扱う **van der Waalsのdiffuse-interface theory** へ進むことになる。

## References

- J. W. Gibbs, “On the Equilibrium of Heterogeneous Substances,” *Transactions of the Connecticut Academy of Arts and Sciences* (1876, 1878).
- R. C. Tolman, “Consideration of the Gibbs Theory of Surface Tension,” *Journal of Chemical Physics* **16**, 758–774 (1948), DOI: 10.1063/1.1746994.
- R. C. Tolman, “The Superficial Density of Matter at a Liquid-Vapor Boundary,” *Journal of Chemical Physics* **17**, 118–127 (1949), DOI: 10.1063/1.1747204.
- R. C. Tolman, “The Effect of Droplet Size on Surface Tension,” *Journal of Chemical Physics* **17**, 333–337 (1949), DOI: 10.1063/1.1747247.
- J. C. Berg, “Gibbs adsorption equation for planar fluid–fluid interfaces: Invariant formalism,” *Advances in Colloid and Interface Science* **222**, 600–614 (2015), DOI: 10.1016/j.cis.2014.01.001.
- J. S. Rowlinson and B. Widom, *Molecular Theory of Capillarity*, Clarendon Press (1982).
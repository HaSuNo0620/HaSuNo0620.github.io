---
title: "GibbsからTolmanへ — 界面熱力学から表面張力の曲率依存へ"
summary: "Gibbsが界面をsurface excessをもつ熱力学的部分系として組み込み、Tolmanが巨視的には定数として扱われる表面張力を曲率半径に依存する量へ拡張した流れを整理する。"
publishedAt: 2026-09-09T20:11:00+09:00
updatedAt: 2026-09-09
area: "Physics"
topics: ["interfacial physics", "surface thermodynamics", "Gibbs dividing surface", "curvature dependence", "Tolman length"]
status: growing
---

[前のNote](/notes/young-laplace-coarse-graining/)では、Young–Laplace式を、界面内部の複雑な構造を表面張力 $\gamma$ という一個の量へ縮約した**力学的な界面法則**として捉えた。球形液滴なら、その関係は

$$\Delta p=\frac{2\gamma}{R}$$

である。

この式では、$\gamma$ は界面に与えられた一つの巨視的な量として扱われる。十分大きな液滴やほぼ平坦な界面なら、それでよい。

しかし界面が強く曲がり、曲率半径 $R$ が界面厚さや分子スケールに近づいたときにも、平面界面の表面張力 $\gamma_\infty$ をそのまま使ってよいのだろうか。

この問いへ進むために、まずGibbsが界面を熱力学の中へ組み込み、その後Tolmanが表面張力そのものの**曲率依存**を問題にした流れを整理する。

## Young–LaplaceからGibbsへ

Young–Laplaceでは、表面張力 $\gamma$ が与えられれば界面の力学は閉じる。しかし、温度や溶液組成を変えたときに、なぜ $\gamma$ が変わるのかはYoung–Laplace式だけでは分からない。

Gibbsが行ったのは、$\gamma$ を単なる力学的パラメータとして使うだけでなく、界面へエネルギー、エントロピー、物質量などの**surface excess**を割り当て、界面を熱力学の中へ組み込むことであった。

ただしGibbsは、界面の密度プロファイルそのものを直接解こうとはしなかった。実際の界面では密度は有限幅で $\rho^\alpha\to\rho^\beta$ と変化する。そのため、「どこまでが相 $\alpha$ で、どこからが相 $\beta$ か」を分子レベルで一意に決めることはできない。

Gibbsはこの問題に対して、界面領域の境界を物理的に決めるのではなく、任意の位置に厚さゼロの数学的な面を置いた。これが **Gibbs dividing surface** である。

## surface excessは実在する界面層の粒子数ではない

平面界面を考え、dividing surfaceを $z=z_0$ に置く。成分 $i$ の参照密度は、左側ではbulk値 $\rho_i^\alpha$、右側ではbulk値 $\rho_i^\beta$ をそのままdividing surfaceまで外挿したものとする。

実際の密度 $\rho_i(z)$ との差を積分すると、面積あたりのsurface excessは

$$\Gamma_i(z_0)=\int_{-\infty}^{z_0}[\rho_i(z)-\rho_i^\alpha]dz+\int_{z_0}^{\infty}[\rho_i(z)-\rho_i^\beta]dz$$

と書ける。

ここで $\Gamma_i$ は「界面スラブの中に実際に存在する分子数」ではない。実在系から、二つのbulk相をdividing surfaceまで仮想的に外挿した参照系を引いた**差分量**である。

したがって、厚さゼロのsurface phaseに $N_i^\sigma\neq0$ が割り当てられても矛盾しない。$N_i^\sigma$ は幾何学的な薄膜内の実粒子数ではなく、bulkだけでは勘定できなかったexcessである。

## dividing surfaceを動かすとexcessは変わる

$z_0$ を $z_0\to z_0+\delta z$ と動かしても、実際の界面は何も変わらない。それにもかかわらずsurface excessは

$$\delta\Gamma_i=(\rho_i^\beta-\rho_i^\alpha)\delta z$$

だけ変化する。

密度差を $\Delta\rho_i=\rho_i^\beta-\rho_i^\alpha$ と定義すれば、

$$\Gamma_i\longrightarrow\Gamma_i+\Delta\rho_i\,\delta z$$

である。

変わっているのは物理状態ではない。同じ実在系を「bulk $\alpha$ + surface + bulk $\beta$」へどう分配したかである。

### 補助的な見方：これはゲージ冗長性と読める

surface excess vectorを $\boldsymbol{\Gamma}=(\Gamma_1,\ldots,\Gamma_n)$、bulk密度差のベクトルを $\Delta\boldsymbol{\rho}$ とする。dividing surfaceを $\lambda$ だけ動かすと

$$\boldsymbol{\Gamma}\longrightarrow\boldsymbol{\Gamma}+\lambda\Delta\boldsymbol{\rho}$$

となる。

同じ物理状態を異なる $\boldsymbol{\Gamma}$ が表すので、この自由度を**記述のゲージ冗長性**と読むことはできる。形式的には、物理情報は

$$\mathbb R^n/\operatorname{span}\{\Delta\boldsymbol{\rho}\}$$

のような同値類に対応すると考えられる。

ただし、これはGibbs自身の用語ではなく、電磁気学やYang–Mills理論のようなゲージ場を導入しているわけでもない。このNoteでは、同じ物理状態を複数の記述が表し、不変な組合せだけが物理に残るという構造を理解するための**現代的な補助解釈**として使う。

## Gibbs adsorption equationはdividing surfaceの任意性をどう消すか

界面熱力学では、Gibbs adsorption equation

$$d\gamma=-s^\sigma dT-\sum_i\Gamma_i d\mu_i$$

が得られる。各 $\Gamma_i$ はdividing surfaceに依存するが、式全体は物理的でなければならない。

各bulk相のGibbs–Duhem関係は

$$\begin{aligned}dp^\alpha&=s^\alpha dT+\sum_i\rho_i^\alpha d\mu_i,\\ dp^\beta&=s^\beta dT+\sum_i\rho_i^\beta d\mu_i\end{aligned}$$

である。

平面界面の二相共存に沿っては $dp^\alpha=dp^\beta$ なので、

$$(s^\beta-s^\alpha)dT+\sum_i(\rho_i^\beta-\rho_i^\alpha)d\mu_i=0$$

となる。

したがって、dividing surfaceを動かしたときにsurface excessへ加わる $\Delta\boldsymbol{\rho}$ 方向の成分は、許された熱力学的変化には寄与しない。定温では

$$\Delta\boldsymbol{\rho}\cdot d\boldsymbol{\mu}=0$$

なので、Gibbs adsorption equationが見るのはdividing-surface choiceに依存しない成分だけである。

二成分系なら、relative adsorption

$$\Gamma_2^{(1)}=\Gamma_2-\frac{\Delta\rho_2}{\Delta\rho_1}\Gamma_1$$

はdividing surfaceを動かしても不変である。

## equimolar surface

一成分系では、$N^\sigma=0$ となるようにdividing surfaceを選ぶことができる。球形界面ならその半径を $R_e$ と書き、これを **equimolar surface** と呼ぶ。

これは「物理的な界面の真の位置」を発見したという意味ではない。物質量のsurface excessがゼロになるという条件で選んだ、再現可能な代表面である。

ゲージという補助的な見方を使えば、$N^\sigma=0$ は一つのgauge fixingと読むこともできる。しかし、この見方はGibbs thermodynamicsを理解するための補助線であって、Tolman理論の主役ではない。

## Tolmanの問い：表面張力は本当に一つの定数なのか

ここでTolmanへ進む。

巨視的な毛管理論では、表面張力は平面界面で定義された値 $\gamma_\infty$ を使い、液滴の大きさには依存しないとみなす。

しかし小さな液滴では、界面の曲率そのものが界面内部の構造を変えうる。そうであれば、表面張力も曲率半径の関数として

$$\gamma=\gamma(R)$$

と考えるべきである。

これがTolmanの問題設定の中心である。

Young–LaplaceからTolmanへの概念的な拡張は、まず

$$\gamma_\infty\quad\longrightarrow\quad\gamma(R)$$

と見るのが最も分かりやすい。

## しかし有限幅界面では「半径 \(R\)」自体が自明ではない

ここでGibbsのdividing surfaceが再び必要になる。

界面に有限幅があるなら、液滴に唯一の幾何学的半径が最初から備わっているわけではない。どのdividing surfaceの半径を $R$ と呼ぶかによって、surface excessの分解も変わる。

球形液滴に半径 $R$ の任意のdividing surfaceを置くと、grand potentialは

$$\Omega=-p_lV_l(R)-p_vV_v(R)+\gamma(R)A(R)$$

と分解できる。

物理的な液滴自体を変えず、帳簿上のdividing surfaceだけを動かす。球では

$$\frac{dV_l}{dR}=A,\qquad \frac{dA}{dR}=\frac{2A}{R}$$

だから、notionalな変化に対して $d\Omega/dR=0$ を課すと

$$\Delta p=\frac{2\gamma(R)}{R}+\left[\frac{d\gamma}{dR}\right]_{\mathrm{notional}}$$

を得る。

ここでの微分は、液滴そのものを膨張させたときの物理的なsize dependenceではない。**同じ液滴に対してdividing surfaceだけを動かしたときのnotional derivative**である。

この区別は重要である。Tolmanが問題にする物理的な $\gamma(R)$ のsize dependenceと、同じ液滴に対して代表面を動かしたときのnotionalな $R$ 依存は、同じものではない。

## surface of tension

notional derivativeがゼロになるdividing surfaceの半径を $R_s$ とし、これを **surface of tension** と呼ぶ。

この面では一般化された関係が通常のLaplace形へ戻る。

$$\Delta p=\frac{2\gamma_s}{R_s}$$

したがってTolmanの曲率依存を議論するとき、半径として $R_s$ を使えば、Young–Laplaceの力学的形式を保ったまま

$$\Delta p=\frac{2\gamma_s(R_s)}{R_s}$$

と書ける。

ここで変わったのはLaplaceの幾何学的構造ではなく、**表面張力が定数ではなくなった**ことである。

## equimolar surfaceとsurface of tensionのずれ

同じ液滴に対して、equimolar surfaceの半径 $R_e$ とsurface of tensionの半径 $R_s$ は一般に一致しない。

有限曲率での差を $\delta(R_s)=R_e-R_s$ と書く。このNoteでは、equimolar surfaceがsurface of tensionより外側にあるとき $\delta>0$ となる符号規約を使う。

この差はTolman理論の目的そのものではない。むしろ、**表面張力の曲率依存をGibbsの界面熱力学で定量化するときに現れる幾何学的な長さ**である。

## Tolman lengthと表面張力の曲率展開

平面極限での二つの代表面の差を

$$\delta_\infty=\lim_{R_s\to\infty}(R_e-R_s)$$

と定義する。この $\delta_\infty$ がTolman lengthである。

大きな液滴について、surface of tensionにおける表面張力は

$$\gamma_s(R_s)=\gamma_\infty\left[1-\frac{2\delta_\infty}{R_s}+O(R_s^{-2})\right]$$

と展開される。

したがってTolman lengthは、単に「二つの面の距離」なのではなく、**表面張力の一次の曲率補正を特徴づける長さ**として理解するのがよい。

Tolmanの物理的な主張を一行で書けば、

$$\text{macroscopic capillarity: }\gamma=\gamma_\infty\qquad\longrightarrow\qquad\text{Tolman: }\gamma=\gamma(R)$$

である。

$R_e-R_s$ は、その $\gamma(R)$ をGibbsのdividing-surface formalismの中で具体化すると現れる量である。

## ゲージ解釈はどこに置くべきか

Gibbsのdividing-surface freedomをゲージ冗長性として読むと、equimolar surfaceとsurface of tensionは、同じ記述上の自由度から異なる条件で代表面を選んだものと見ることができる。

その意味では $R_e-R_s$ を「二つの代表面選択の差」と解釈することはできる。

しかし、これをTolman理論の中心に置くと主従が逆になる。

Tolmanの中心問題は、**小さな液滴ではsurface tension自体がcurvature-dependentではないか**ということである。equimolar surface、surface of tension、Tolman lengthは、その問いをGibbsの熱力学の中で定式化するための道具として現れる。

したがってこのNoteでは、ゲージという見方はGibbsの任意性を理解する補助線として残すが、Tolmanの主眼は $\gamma(R)$ に置く。

## Young–Laplace、Gibbs、Tolmanを一つの流れで見る

Young–Laplaceでは、界面を張力をもつ幾何学的な面へ縮約し、$\gamma$ が与えられたときの力学を閉じた。

Gibbsでは、その面へsurface excessを割り当て、$\gamma$ を温度や化学ポテンシャルと関係する**界面熱力学の量**として位置づけた。

Tolmanでは、さらに曲率が強くなったときに $\gamma$ 自体を一つの定数とみなせるのかを問い、

$$\gamma_\infty\longrightarrow\gamma(R)$$

という拡張を行った。

そしてその一次曲率補正を特徴づける長さとして、Tolman length $\delta_\infty$ が現れる。

この順序で見ると、三者の役割はかなり明確になる。

- Young–Laplace：$\gamma$ を与えて界面力学を閉じる
- Gibbs：$\gamma$ を界面熱力学の中へ組み込む
- Tolman：$\gamma$ の曲率依存を考える

## それでもまだ界面内部は解いていない

ただしGibbsもTolmanも、密度プロファイル $\rho(z)$ や応力異方性 $P_N(z)-P_T(z)$ を第一原理的に求めてはいない。

Tolmanは、曲率による界面構造の変化を $\gamma(R)$ や $\delta_\infty$ という少数の有効量へ押し込めている。

したがって次に問うべきなのは、

> そもそも有限幅の界面はなぜ生まれ、その密度プロファイルは何によって決まり、その構造から $\gamma$ やその曲率依存がどう出てくるのか。

である。

ここで、界面を空間的に連続な密度場として扱う **van der Waalsのdiffuse-interface theory** へ進むことになる。

## References

- J. W. Gibbs, “On the Equilibrium of Heterogeneous Substances,” *Transactions of the Connecticut Academy of Arts and Sciences* (1876, 1878).
- R. C. Tolman, “Consideration of the Gibbs Theory of Surface Tension,” *Journal of Chemical Physics* **16**, 758–774 (1948), DOI: 10.1063/1.1746994.
- R. C. Tolman, “The Superficial Density of Matter at a Liquid-Vapor Boundary,” *Journal of Chemical Physics* **17**, 118–127 (1949), DOI: 10.1063/1.1747204.
- R. C. Tolman, “The Effect of Droplet Size on Surface Tension,” *Journal of Chemical Physics* **17**, 333–337 (1949), DOI: 10.1063/1.1747247.
- J. C. Berg, “Gibbs adsorption equation for planar fluid–fluid interfaces: Invariant formalism,” *Advances in Colloid and Interface Science* **222**, 600–614 (2015), DOI: 10.1016/j.cis.2014.01.001.
- J. S. Rowlinson and B. Widom, *Molecular Theory of Capillarity*, Clarendon Press (1982).
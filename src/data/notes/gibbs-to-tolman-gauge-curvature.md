---
title: "Gibbsの界面熱力学 — dividing surfaceと記述の自由度"
summary: "Gibbs dividing surfaceとsurface excessを中心に、界面を熱力学的部分系として扱う方法と、その記述に残る任意性を整理する。Tolmanとの接続は後の展開として短く触れる。"
publishedAt: 2026-09-09T20:11:00+09:00
updatedAt: 2026-09-09
area: "Physics"
topics: ["interfacial physics", "surface thermodynamics", "Gibbs dividing surface", "surface excess", "gauge redundancy"]
status: growing
---

[前のNote](/notes/young-laplace-coarse-graining/)では、Young–Laplace式を、界面内部の複雑な構造を表面張力 $\gamma$ という一個の量へ縮約した**力学的な界面法則**として捉えた。

Gibbsが次に行ったのは、この $\gamma$ を単なる力学的パラメータとして使うだけでなく、界面そのものを熱力学の中へ組み込むことであった。

Young–Laplaceが「界面の力学をどう閉じるか」を扱うのに対し、Gibbsは「界面にどのような熱力学的量を割り当てられるか」を考える。

## 界面の位置はそもそも一意ではない

実際の液体–気体界面では、密度は有限幅で $\rho^\alpha\to\rho^\beta$ と変化する。

そのため、「どこまでが相 $\alpha$ で、どこからが相 $\beta$ か」を分子レベルで一意に決めることはできない。

Gibbsはこの問題に対して、界面領域の物理的な境界を決めるのではなく、任意の位置に厚さゼロの数学的な面を置いた。これが **Gibbs dividing surface** である。

この面は実在する膜ではない。二つのbulk相と界面の寄与を熱力学的に分けるための参照面である。

## surface excess

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

この時点で重要なのは、**surface excessそのものにはdividing surfaceの選び方による任意性がある**ということである。

## 補助的な見方：ゲージ冗長性

surface excess vectorを $\boldsymbol{\Gamma}=(\Gamma_1,\ldots,\Gamma_n)$、bulk密度差のベクトルを $\Delta\boldsymbol{\rho}$ とする。dividing surfaceを $\lambda$ だけ動かすと

$$\boldsymbol{\Gamma}\longrightarrow\boldsymbol{\Gamma}+\lambda\Delta\boldsymbol{\rho}$$

となる。

同じ物理状態を異なる $\boldsymbol{\Gamma}$ が表すので、この自由度を**記述のゲージ冗長性**と読むことはできる。形式的には、物理情報は

$$\mathbb R^n/\operatorname{span}\{\Delta\boldsymbol{\rho}\}$$

のような同値類に対応すると考えられる。

ただし、これはGibbs自身の用語ではない。また電磁気学やYang–Mills理論のような局所ゲージ場を導入しているわけでもない。

ここで「ゲージ」と呼んでいるのは、**同じ物理状態を複数の記述が表し、不変な組合せだけが物理に残る**という構造を理解するための現代的な補助解釈である。

## Gibbs adsorption equationは任意性をどう消すか

界面熱力学では、Gibbs adsorption equation

$$d\gamma=-s^\sigma dT-\sum_i\Gamma_i d\mu_i$$

が得られる。

各 $\Gamma_i$ はdividing surfaceに依存する。それにもかかわらず、この式全体は物理的でなければならない。

各bulk相のGibbs–Duhem関係は

$$\begin{aligned}dp^\alpha&=s^\alpha dT+\sum_i\rho_i^\alpha d\mu_i,\\ dp^\beta&=s^\beta dT+\sum_i\rho_i^\beta d\mu_i\end{aligned}$$

である。

平面界面の二相共存に沿っては $dp^\alpha=dp^\beta$ なので、

$$(s^\beta-s^\alpha)dT+\sum_i(\rho_i^\beta-\rho_i^\alpha)d\mu_i=0$$

となる。

したがって、dividing surfaceを動かしたときにsurface excessへ加わる $\Delta\boldsymbol{\rho}$ 方向の成分は、許された熱力学的変化には寄与しない。

定温では

$$\Delta\boldsymbol{\rho}\cdot d\boldsymbol{\mu}=0$$

であり、Gibbs adsorption equationが見るのはdividing-surface choiceに依存しない成分だけである。

## relative adsorption

二成分系では、relative adsorptionを

$$\Gamma_2^{(1)}=\Gamma_2-\frac{\Delta\rho_2}{\Delta\rho_1}\Gamma_1$$

と書ける。

dividing surfaceを動かしても、この組合せは変わらない。

したがって、物理的な吸着を考えるときには、単独のabsoluteな $\Gamma_i$ よりも、このような**dividing-surface invariantな組合せ**が本質になる。

## equimolar surface

一成分系では、$N^\sigma=0$ となるようにdividing surfaceを選ぶことができる。球形界面ならその半径を $R_e$ と書き、これを **equimolar surface** と呼ぶ。

これは「物理的な界面の真の位置」を発見したという意味ではない。物質量のsurface excessがゼロになるという条件で選んだ、再現可能な代表面である。

ゲージという補助的な見方を使えば、$N^\sigma=0$ は一つのgauge fixingと読むこともできる。

## Gibbsがしたこと、していないこと

Gibbsは界面にsurface excessを割り当て、表面張力を温度や化学ポテンシャルと結びつける熱力学を作った。

しかし、密度プロファイル $\rho(z)$ 自体を求める理論ではない。

つまりGibbsは、有限幅の界面構造を解像する代わりに、その情報をsurface excessや $\gamma$ のような積分的な量へ縮約している。

この意味で、Young–LaplaceとGibbsの違いは次のように整理できる。

- Young–Laplace：界面を**力学的な面**として粗視化する
- Gibbs：界面を**熱力学的な部分系**として粗視化する

どちらも界面内部の空間構造そのものを解いてはいない。

## 後のTolmanへの接続

後にTolmanは、小さな液滴では表面張力を平面界面の一つの定数 $\gamma_\infty$ とみなすだけでは不十分で、曲率半径に依存する $\gamma(R)$ を考えるべきではないか、という問題を扱う。

Gibbsのdividing-surface formalismは、そのとき「どの半径を使うのか」「どの代表面でsurface tensionを定義するのか」を整理するための基盤になる。

また、equimolar surfaceとsurface of tensionという異なる代表面が現れることを、先ほどのゲージ的な見方から「異なる条件で代表面を選んでいる」と解釈することもできる。

ただし、これは**Tolman理論そのものの説明ではなく、Gibbsの枠組みから後の曲率依存問題へどう繋がるかという予告**として捉える。

Tolmanの曲率補正やTolman lengthの詳しい議論は、van der Waalsのdiffuse-interface theoryを見た後に改めて扱う方が、歴史的にも概念的にも自然である。

## 次の疑問

Gibbsは界面の熱力学を非常にうまく閉じた。しかし、依然として密度プロファイルそのものはブラックボックスである。

そこで次に問うべきなのは、

> そもそも有限幅の界面はなぜ生まれ、その密度プロファイルは何によって決まるのか。

である。

ここで、界面を空間的に連続な密度場として扱う **van der Waalsのdiffuse-interface theory** へ進む。

## References

- J. W. Gibbs, “On the Equilibrium of Heterogeneous Substances,” *Transactions of the Connecticut Academy of Arts and Sciences* (1876, 1878).
- J. C. Berg, “Gibbs adsorption equation for planar fluid–fluid interfaces: Invariant formalism,” *Advances in Colloid and Interface Science* **222**, 600–614 (2015), DOI: 10.1016/j.cis.2014.01.001.
- J. S. Rowlinson and B. Widom, *Molecular Theory of Capillarity*, Clarendon Press (1982).
- R. C. Tolman, “The Effect of Droplet Size on Surface Tension,” *Journal of Chemical Physics* **17**, 333–337 (1949), DOI: 10.1063/1.1747247.
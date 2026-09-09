---
title: "Young–Laplace式は何を捨てているのか"
summary: "毛管上昇と分子間凝集力から出発し、Young–Laplace式を界面内部の情報を表面張力ひとつへ縮約した最低次の有効理論として読み直す。"
publishedAt: 2026-09-09T19:06:00+09:00
topics: ["interfacial physics", "capillarity", "coarse graining", "Young-Laplace"]
status: growing
---

Young–Laplace式は

$$
\Delta p
=
\gamma
\left(
\frac{1}{R_1}
+
\frac{1}{R_2}
\right)
$$

と書かれる。

通常は「曲率をもった界面の両側には圧力差が生じる」という公式として習う。しかし、この式について考えているうちに気になったのは、むしろ逆のことであった。

**なぜ、分子間力まで含んだ複雑な界面の問題が、圧力差 $\Delta p$、表面張力 $\gamma$、曲率だけで記述できてしまうのか。**

Young–Laplace式の重要性は、圧力差を与えること以上に、界面について「何を知らなくてもよいか」を示していることにあるのではないか。

## 毛管上昇から始まる

歴史的には、理論より先に毛管現象があった。

細い管を液体に挿すと液面が上昇あるいは下降する。高さを $h$ とすると、静水圧から

$$
\Delta p = \rho g h
$$

と読める。

したがって、界面の両側に圧力計を直接置けなくても、液柱そのものが圧力差の測定器になる。

問題は「圧力差が存在するか」より、

> なぜ界面が曲がると、その圧力差が生じるのか

であった。

Youngの1805年の議論は毛管現象や液体の凝集を主として記述的に扱ったのに対し、Laplaceは1806年にこれをより解析的に扱った。ただしLaplace自身が、現在の教科書のように既知の表面張力 $\gamma$ から出発してYoung–Laplace式を導いたわけではない。分子間の短距離凝集力から毛管現象を説明しようとしたのである。

この点は重要である。

現在のYoung–Laplace式は非常に巨視的に見えるが、その歴史的な出発点には、

$$
\text{分子間力}
\longrightarrow
\text{毛管現象}
$$

というミクロからマクロへの問題があった。

## なぜ分子間力ではなく圧力で考えるのか

原理的には、液体に働く力をすべて分子間力

$$
\mathbf F_{ij}
$$

から計算してもよい。

しかし一様な液体内部では、一個の分子は全方向から強く引かれている。その合力は対称性によってほぼ打ち消される。

つまり、

$$
\sum_j \mathbf F_{ij}\simeq 0
$$

だからといって、分子間力そのものが弱いわけではない。

**巨大な力同士が相殺した結果だけが巨視的に残っている。**

そこで、個々の分子間力を追いかける代わりに、その集団的効果を圧力や応力へ粗視化する。

現代的には、一様で等方的な流体なら応力テンソルは

$$
\boldsymbol{\sigma}=-p\mathbf I
$$

となり、静力学は

$$
-\nabla p+\rho\mathbf g=0
$$

で閉じる。

圧力とはこの意味で、膨大なミクロな力を巨視的な一変数へ圧縮した量である。

界面では周囲の分子配置の対称性が崩れる。さらに界面が曲率をもてば、その不均衡の仕方も平面界面とは異なる。

Laplaceが扱おうとしたのは、このような凝集力の巨視的な残差であったと考えられる。

ただし、Laplaceの毛管理論に現れる巨大な分子的内部圧力と

$$
\Delta p=\frac{2\gamma}{R}
$$

として観測されるLaplace圧は同じものではない。

後者は、複雑な分子間力がほぼ相殺された後に残る、曲率に依存する巨視的な効果である。

## 曲率はなぜ圧力差を生むのか

球形の液滴を考える。

半径を $R$、表面張力を $\gamma$ とする。

半球だけを切り出すと、内外の圧力差による力は投影面積に対して

$$
F_p=\Delta p\,\pi R^2
$$

となる。

一方、赤道の円周には表面張力が働くので、

$$
F_\gamma=2\pi R\gamma.
$$

力学的平衡から

$$
\Delta p\,\pi R^2
=
2\pi R\gamma
$$

したがって

$$
\boxed{
\Delta p=\frac{2\gamma}{R}
}
$$

を得る。

一般の曲面では

$$
\boxed{
\Delta p
=
\gamma
\left(
\frac1{R_1}
+
\frac1{R_2}
\right)
}
$$

となる。

ただ、この力の釣り合いだけでは、まだ「なぜ $\gamma$ と圧力が結びつくのか」という疑問が残る。

## $p$ と $\gamma$ は、それぞれ体積と面積に共役する

現代的には、Young–Laplace式を変分原理として見ると構造がより明瞭になる。

圧力は体積変化に共役し、

$$
p
\sim
-\frac{\partial F}{\partial V},
$$

表面張力は面積変化に共役する。

$$
\gamma
\sim
\frac{\partial F}{\partial A}.
$$

球形液滴なら

$$
A=4\pi R^2,
\qquad
V=\frac43\pi R^3.
$$

半径を $dR$ だけ変化させると、

$$
dA=8\pi R\,dR,
$$

$$
dV=4\pi R^2\,dR.
$$

表面自由エネルギー変化と圧力仕事の平衡は

$$
\gamma\,dA
=
\Delta p\,dV
$$

だから、

$$
\Delta p
=
\gamma\frac{dA}{dV}
=
\frac{2\gamma}{R}.
$$

つまりYoung–Laplace式は、

$$
\boxed{
p\leftrightarrow V
\qquad\text{と}\qquad
\gamma\leftrightarrow A
}
$$

という二つの共役関係が、曲率をもった幾何によって結びついた結果とも理解できる。

一般曲面を法線方向に $\delta h$ だけ動かすと、

$$
\delta V
=
\int_A \delta h\,dA,
$$

一方で面積変化は平均曲率

$$
H=
\frac12
\left(
\frac1{R_1}+\frac1{R_2}
\right)
$$

を用いて

$$
\delta A
=
\int_A 2H\,\delta h\,dA
$$

となる。

したがって

$$
\delta F
=
\gamma\delta A-\Delta p\,\delta V
$$

は

$$
\delta F
=
\int_A
(2\gamma H-\Delta p)
\delta h\,dA.
$$

任意の $\delta h$ に対して平衡であるためには

$$
\boxed{
\Delta p=2\gamma H
}
$$

でなければならない。

## では、$\gamma$ は何を隠しているのか

ここからが本題である。

実際の界面には有限の厚さがある。

液体–気体界面なら密度は

$$
\rho_l
\longrightarrow
\rho_v
$$

へ連続的に変化する。

さらに局所的には、法線方向と接線方向で応力が異なる。

平面液体–気体界面の標準的な機械的表示では、

$$
\gamma
=
\int dz\,
\left[
P_N(z)-P_T(z)
\right].
$$

Young–Laplace式に現れるのは、この積分結果である $\gamma$ だけである。

したがって、たとえば二つの界面AとBについて、

$$
P_N(z)-P_T(z)
$$

の形がまったく違っていたとしても、

$$
\int dz\,[P_N-P_T]
$$

が同じなら、同じ $\gamma$ をもつ。

十分大きな液滴を作れば、どちらも

$$
\Delta p=\frac{2\gamma}{R}
$$

を与える。

Young–Laplace理論の立場から見れば、この二つの界面は区別できない。

ここで初めて、この式が何をしているのかが見えてくる。

$$
\boxed{
\text{界面内部の複雑な情報}
\longrightarrow
\gamma
}
$$

という縮約である。

## Young–Laplace式が捨てるもの

第一に、**界面幅**を捨てる。

界面内部の特徴的な厚さを $\xi$、界面形状が変化する巨視的長さを $L$ とすると、

$$
\epsilon=\frac{\xi}{L}.
$$

Young–Laplace理論は基本的に

$$
\epsilon\ll1
$$

という極限を見ている。

界面が十分薄ければ、有限幅の領域を数学的な面へ潰すことができる。

第二に、**界面内部での位置情報**を捨てる。

Young–Laplace式が知っているのは概念的にはstress anisotropyのゼロ次モーメント

$$
\int dz\,\Pi(z)
$$

だけである。

しかし、

$$
\int dz\,z\Pi(z),
\qquad
\int dz\,z^2\Pi(z)
$$

といった高次モーメントには、「界面のどの位置で力が担われているのか」という追加情報が含まれる。

曲率が界面厚さと比較して無視できなくなると、このような捨てた情報が再び効いてくる可能性がある。

第三に、**界面のミクロ構造**を捨てる。

$$
\rho(z),\qquad
g^{(2)}(\mathbf r,\mathbf r'),\qquad
P_N(z)-P_T(z)
$$

を知らなくても、$\gamma$ さえ与えられればYoung–Laplace式は使える。

これは欠点であると同時に、この理論が強力な理由でもある。

## Young–Laplace式は最低次の有効理論である

この見方をすると、Young–Laplace式は単なる毛管圧の公式ではなくなる。

界面自由エネルギーについて最も単純な近似を

$$
F_{\mathrm{int}}=\gamma A
$$

とする。

これは、界面内部の構造や曲率依存性をすべて捨て、「面積を作るコスト」だけを残した理論である。

より一般には、界面自由エネルギーには曲率に依存する項が入り得る。

概念的には

$$
F_{\mathrm{int}}
=
\int dA\,
\left[
\gamma
+
c_1 H
+
c_2 H^2
+
c_3 K
+\cdots
\right],
$$

と展開できる。ここで $H$ は平均曲率、$K$ はGauss曲率である。対称性などによって許される項は系ごとに異なるが、$\gamma A$ はその最低次に位置する。

したがってYoung–Laplace式は、

$$
\boxed{
\text{薄い界面を、局所的な張力をもつ数学的な面へ粗視化した最低次理論}
}
$$

と読むことができる。

これが今回いちばん腑に落ちた点である。

## 「知らなくても成立する」ということ

Young–Laplace式の普遍性は、界面内部について多くを説明できるからではない。

むしろ逆である。

**界面内部についてほとんど何も知らなくても成立する。**

十分なスケール分離があれば、

$$
\rho(z),
\quad
g^{(2)},
\quad
P_N(z),
\quad
P_T(z)
$$

という情報を全部捨て、

$$
\gamma
$$

という一個の量に押し込めることができる。

そして巨視的な界面形状については、

$$
\Delta p=2\gamma H
$$

だけで閉じる。

これは、ミクロな詳細から独立した有効理論が成立する典型例と見ることができる。

## 次の疑問

ここまで考えると、次に問いたくなるのは

> 捨てた情報を一つずつ戻したら、Young–Laplace理論はどう変わるのか

である。

界面を熱力学的な二次元部分系として扱うならGibbsへ進む。

有限の界面幅を戻すならvan der Waalsへ進む。

分子相関や局所stressを戻すならKirkwood–Buffの方向へ進む。

曲率によって $\gamma$ 自体が変化することを考えればTolmanへ進む。

したがって、界面研究の歴史は単なる理論の精密化としてではなく、

$$
\boxed{
\text{Young--Laplaceで捨てた情報を、必要に応じて一つずつ取り戻してきた歴史}
}
$$

として読むこともできそうである。

この見方がどこまで通用するのかを、次から確かめていきたい。

## References

- T. Young, *An Essay on the Cohesion of Fluids* (1805).
- P.-S. Laplace, *Supplément au dixième livre du Traité de mécanique céleste* (1806).
- K. S. W. Sing and R. T. Williams, “Historical aspects of capillarity and capillary condensation” (2012).
- M. J. Klein, “The historical origins of the Van der Waals equation” (1974).

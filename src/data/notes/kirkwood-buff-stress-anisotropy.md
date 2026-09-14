---
title: "Kirkwood–Buff — 表面張力を界面内部の応力へ戻す"
summary: "表面張力を界面に局在したstress anisotropyの積分として捉え、Kirkwood–Buffの統計力学的描像からYoung–Laplace、van der Waals、Tolmanとのつながりを整理する。"
publishedAt: 2026-09-10T00:26:00+09:00
updatedAt: 2026-09-14
area: "Physics"
topics: ["interfacial physics", "surface tension", "Kirkwood-Buff", "stress tensor", "statistical mechanics"]
status: growing
---

[van der WaalsのNote](/notes/van-der-waals-diffuse-interface/)では、一体密度 $\rho(z)$ まで界面内部を取り戻した。Kirkwood–Buffはさらに一段ミクロへ降り、表面張力を**界面内部に分布する応力異方性とpair statistics**へ戻す。

Young–Laplaceでは一個の係数だった $\gamma$ が、ここでは空間分布の積分として展開される。

## 表面張力は stress anisotropy の zeroth moment である

平坦な液気界面を考え、法線方向を $z$ とする。

bulkでは等方性により

$$
P_{xx}=P_{yy}=P_{zz}=p
$$

である。一方、界面では法線方向だけが特別になるので

$$
P_N(z)=P_{zz}(z),
$$

$$
P_T(z)=\frac{P_{xx}(z)+P_{yy}(z)}{2}
$$

と分けると、一般に $P_N(z)\neq P_T(z)$ となる。

平面界面の表面張力は

$$
\gamma=\int_{-\infty}^{\infty}dz\,[P_N(z)-P_T(z)]
$$

と書ける。

$$
\Pi(z)\equiv P_N(z)-P_T(z)
$$

とおけば

$$
\boxed{\gamma=\int dz\,\Pi(z)}
$$

である。

表面張力は、一枚の面に最初から宿る量というより、界面内部に分布した三次元的な応力構造を厚さ方向へ積分した量と読める。

## 法線・接線差は面積変形への仕事を測る

表面張力は面積を変える変形に対する仕事として定義できる。

bulkが等方的なら、体積一定の変形に対して法線方向と接線方向のmechanical workは互いに打ち消し合う。しかし界面では $P_N$ と $P_T$ が異なるため余分な仕事が残る。

その余分な仕事が

$$
\delta W=\gamma\,\delta A
$$

に対応する。

したがって $P_N-P_T$ は、単なるテンソル成分の差ではなく、**界面を面積変形したときに残る方向依存のmechanical work**を局所化した量と見られる。

## 界面は pair statistics の回転対称性を壊す

単原子流体で中心力型pair potential $u(r)$ を考える。

bulkでは粒子の周囲は平均的に等方的で、pair configurationの角度分布も等方的である。そのため分子間力によるvirial contributionも方向を選ばず、平均すると $P_N=P_T$ になる。

界面付近では、液体側と気体側で隣接粒子数が異なり、pair configurationの分布が法線方向と接線方向で非等価になる。

したがって

$$
\text{interface}
\longrightarrow
\text{rotational symmetry breaking}
\longrightarrow
\rho^{(2)}\text{ の異方性}
\longrightarrow
P_N-P_T
\longrightarrow
\gamma
$$

という流れになる。

表面張力は分子間相互作用だけで決まるのではなく、相互作用と、界面によって生じたpair distributionの異方性の両方から生じる。

## Kirkwood–Buff は pair virial まで降りる

二体密度を $\rho^{(2)}(\mathbf r_1,\mathbf r_2)$ とする。

中心力なら configurational stress には pair virial $r_{12,\alpha}F_{12,\beta}$ が現れる。法線方向と接線方向の差を取ると、pair vector と界面法線のなす角が効いてくる。

平面界面に対するKirkwood–Buff型の式は、規約による係数の違いを除けば概略

$$
\gamma\propto
\int dz_1\int d\mathbf r_{12}\,
\rho^{(2)}(\mathbf r_1,\mathbf r_2)\,
r_{12}u'(r_{12})
\left(1-3\cos^2\theta_{12}\right)
$$

という構造を持つ。

角度因子 $1-3\cos^2\theta$ は、等方的なpair distributionでは角度平均がゼロになる。そのためbulkは表面張力へ寄与せず、界面でのみ非零の寄与が残る。

物理的には

$$
\boxed{
\gamma
\sim
\text{intermolecular force}
\times
\text{anisotropy of pair statistics}
}
$$

と読める。

## van der Waals は一体密度、Kirkwood–Buff は二体統計を見る

van der Waals型のdiffuse-interface theoryでは、一体密度 $\rho(z)$ を主変数とし、現代的なsquare-gradient formでは

$$
F[\rho]
=
\int dz\left[
f_0(\rho)
+\frac{\kappa}{2}\left(\frac{d\rho}{dz}\right)^2
\right]
$$

から

$$
\gamma
=
\int dz\,\kappa\left(\frac{d\rho}{dz}\right)^2
$$

を得る。

Kirkwood–Buffではさらに一段ミクロへ降り、$u(r)$ と $\rho^{(2)}$ から $P_N-P_T$ を構成する。

$$
\text{van der Waals}:\quad
\rho(z)\longrightarrow\gamma
$$

$$
\text{Kirkwood--Buff}:\quad
u(r),\rho^{(2)}\longrightarrow\Pi(z)\longrightarrow\gamma
$$

両者は対立しない。pair structureを十分滑らかに粗視化し、長波長展開すれば、Kirkwood–Buff側のミクロな記述からsquare-gradient型の界面理論へ近づくと考えられる。

## higher moments は力の位置情報を持つ

$\gamma$ は $\Pi(z)$ のzeroth momentである。

したがって、全く異なるstress profileでもzeroth momentが同じなら同じ表面張力を与えうる。

一方 first moment

$$
M_1=\int dz\,z\Pi(z)
$$

は、応力異方性が界面内部のどちら側へ偏っているかという位置情報を持つ。

さらにhigher momentsは、界面内部の幅や非対称性に関する情報を含みうる。

$$
\boxed{
\Pi(z)
\longrightarrow
\{\gamma,M_1,M_2,\ldots\}
}
$$

というmoment hierarchyとして界面を見られる。

Young–Laplaceが使う $\gamma$ は、この階層の最初の一個だけを残した粗視化量である。

## surface of tension は代表面と moment の問題になる

Tolmanでは equimolar radius $R_e$ と surface-of-tension radius $R_s$ が現れ、その差の平面極限がTolman lengthに関係する。

Kirkwood–Buffの見方では、surface of tensionは界面内部に分布したstress anisotropyを一枚の代表面へ縮約する問題として理解できる。

$\Pi(z)$ のzeroth momentだけなら表面張力の大きさしか分からない。first momentまで見ると、「その力がどこに作用していると代表させるか」という位置の問題が現れる。

このため曲率補正とstress momentsは深く関係する。ただしTolman lengthやbending rigidityを単純なlocal stress momentだけから取り出す際には注意が必要である。

## 原点移動と dividing surface は似た自由度を持つ

座標原点を $z\rightarrow z+a$ とずらしても

$$
\gamma=\int dz\,\Pi(z)
$$

は変わらない。

しかしfirst momentは

$$
M_1\rightarrow M_1+a\gamma
$$

と変換される。

zeroth momentは原点に依存しないが、first momentは界面位置の選び方を含む。

これはGibbsのdividing surfaceを動かしたときsurface excessが変換される構造と似ている。表面張力は界面位置の取り方に依存しない積分量だが、その内部構造の「位置」を表すmomentには記述上の自由度が残る。

## local stress は非一意でも $\gamma$ は頑健である

分子系でlocal stress tensorを定義するとき、pair forceを空間のどの経路に沿って配分するかには自由度がある。Irving–Kirkwoodなどの構成は、その一つの系統的な定義を与える。

そのため局所的な $P_T(z)$ やstress profileの形は、microscopic stress prescriptionによって変わりうる。

しかし平面界面の

$$
\gamma=\int dz\,[P_N-P_T]
$$

という積分量は、この局所的な表現の自由度に対してはるかに頑健である。

$$
\boxed{
\text{local representationは一意でなくても、integrated observableは一意になりうる}
}
$$

という構造がここにも現れる。

一方、first momentやsecond momentのようなhigher momentsを使って曲率補正を議論すると、このlocal stressの非一意性がより重要になる。mechanical routeによるTolman lengthやbending rigidityの評価が難しくなる理由の一つである。

## 界面理論の解像度の階層

ここまでを解像度として並べると

- Young–Laplace：界面内部を捨て、$\gamma$ だけを残す
- Gibbs：界面内部をsurface excessへ縮約する
- van der Waals：有限幅の一体密度 $\rho(z)$ を取り戻す
- Tolman：有限幅界面を曲げたときの $\gamma(R)$ と界面位置を問う
- Kirkwood–Buff：pair statistics と stress distribution まで降りる

となる。

Kirkwood–Buffによって

$$
\gamma
\longleftarrow
\Pi(z)
\longleftarrow
\rho^{(2)}(\mathbf r_1,\mathbf r_2),u(r)
$$

というミクロな階層が見える。

表面張力は、界面内部に分布する分子間力とpair structureの異方性を、一つのzeroth momentへ粗視化した量なのである。

## 残る自由度は界面位置そのものの揺らぎである

ここまでの記述では、界面は時間平均された静的なprofileとして扱っている。

有限温度では、界面の位置そのものが面内方向に揺らぐ。そのとき観測される界面幅には、van der Waals型のintrinsic profileだけでなく、界面位置の長波長揺らぎも重なる。

固定された $\Pi(z)$ や $\rho(z)$ だけではなく、高さ場 $h(x,y)$ を自由度として持たせる必要が出る。これはcapillary-wave theoryへつながる。

## References

- J. G. Kirkwood and F. P. Buff, “The Statistical Mechanical Theory of Surface Tension,” *Journal of Chemical Physics* **17**, 338–343 (1949).
- J. H. Irving and J. G. Kirkwood, “The Statistical Mechanical Theory of Transport Processes. IV. The Equations of Hydrodynamics,” *Journal of Chemical Physics* **18**, 817–829 (1950).
- J. S. Rowlinson and B. Widom, *Molecular Theory of Capillarity*, Clarendon Press (1982).

---
title: "Kirkwood–Buffの表面張力と二体密度の異方性"
summary: "体積一定の面積変形から平面界面の力学的表面張力を導き、二体密度と分子間力による表現、局所応力の非一意性を区別する。"
publishedAt: 2026-09-10T00:26:00+09:00
updatedAt: 2026-11-28
area: "Physics"
field: interfaces
kind: theory
related: ["young-laplace-coarse-graining", "van-der-waals-diffuse-interface"]
topics: ["interfacial physics", "surface tension", "Kirkwood-Buff", "stress tensor", "statistical mechanics"]
status: growing
---

平面液気界面の表面張力は、法線方向と接線方向の圧力差を界面にわたって積分することで求められる。この関係を分子間力にまでさかのぼると、表面張力を決めるのは一体密度だけではなく、二体密度の角度依存性であることが分かる。

## 面積変形に対する仕事

温度、粒子数、全体積を一定に保った直方体の流体系を考える。界面は $xy$ 平面に平行とする。微小な体積保存変形

$$
x\mapsto e^{\epsilon/2}x,\quad
y\mapsto e^{\epsilon/2}y,\quad
z\mapsto e^{-\epsilon}z
$$

では界面面積 $A$ が $\delta A=A\epsilon$ だけ増加する。圧力テンソルを正の圧縮応力として定義すると、可逆なHelmholtz自由エネルギー変化は

$$
\delta F=-\int d\mathbf r\,P_{ij}\delta e_{ij}
=A\epsilon\int dz\,[P_N(z)-P_T(z)]
$$

となる。ここで $P_N=P_{zz}$、$P_T=(P_{xx}+P_{yy})/2$ である。孤立した一つの平面流体界面に対し、バルク相が等方的で界面間相互作用が無視できるなら、

$$
\gamma=\int dz\,[P_N(z)-P_T(z)].
$$

周期境界のスラブに等価な界面が二つ存在する場合は、全セルの積分を2で割る。バルクの寄与は等方性により消える。固体を含む系ではバルクの異方的応力や弾性変形の仕事も入りうるため、同じ操作が直ちに固液界面自由エネルギーを与えるとは限らない。

## 分子間力による導出

古典単原子流体で中心力型の対相互作用

$$
U=\sum_{i<j}u(r_{ij})
$$

を仮定する。体積保存変形のJacobianは1なので、カノニカル分配関数の変形微分から

$$
\frac{\partial F}{\partial\epsilon}
=\left\langle\frac{\partial U}{\partial\epsilon}\right\rangle
$$

を得る。運動量積分と配置積分の体積因子は変化しない。

粒子対の距離の変化は

$$
\left.\frac{\partial r_{ij}}{\partial\epsilon}\right|_0
=\frac{x_{ij}^2+y_{ij}^2-2z_{ij}^2}{2r_{ij}}
=\frac{r_{ij}}2(1-3\cos^2\theta_{ij}),
$$

ただし $\theta_{ij}$ は粒子間ベクトルと界面法線のなす角である。したがって一界面の張力は

$$
\gamma=\frac1{2A}\left\langle\sum_{i<j}
r_{ij}u'(r_{ij})(1-3\cos^2\theta_{ij})\right\rangle.
$$

これは全セルのビリアル圧力テンソルの法線・接線差から得られる式と等価である。ポテンシャルの切断に不連続があれば、その変形微分に伴う補正も整合的に扱う必要がある。

## 二体密度による表現

順序付き粒子対の二体密度を

$$
\rho^{(2)}(\mathbf r_1,\mathbf r_2)
=\left\langle\sum_{i\ne j}
\delta(\mathbf r_1-\mathbf r_i)
\delta(\mathbf r_2-\mathbf r_j)\right\rangle
$$

と定義する。面内の並進対称性を用い、面積積分を消去すれば、

$$
\gamma=\frac14\int dz_1\int d\mathbf r_{12}\,
\rho^{(2)}(\mathbf r_1,\mathbf r_2)
r_{12}u'(r_{12})(1-3\cos^2\theta_{12})
$$

となる。ここで $\mathbf r_2=\mathbf r_1+\mathbf r_{12}$ とし、積分は一つの孤立界面に対応する。係数1/4のうち1/2は距離の変形微分、残る1/2は順序付き粒子対の二重計数に由来する。

等方的なバルクでは、二体密度は粒子間距離だけに依存する。角度因子の球面平均はゼロであるため、表面張力へのバルク寄与は消える。界面では法線方向と接線方向の粒子配置が異なるので、角度積分が一般には消えない。

二体密度を $\rho(\mathbf r_1)\rho(\mathbf r_2)g(\mathbf r_1,\mathbf r_2)$ と分解すれば、一体密度が既知でも相関関数 $g$ が未知である限り、上式から張力を決めることはできない。平方勾配模型では一体密度の自由エネルギー汎関数を近似することでこの問題を閉じるが、Kirkwood–Buff式から勾配係数が無条件に導かれるわけではない。

## 局所圧力と積分量

全セルのビリアルは粒子対ごとの力と距離によって決まる。一方、それを局所的な圧力テンソルへ分配するには、粒子対を結ぶ経路などの規約が必要になる。

Irving–Kirkwoodの直線経路による平面平均では、配置寄与は

$$
P_{ab}^{\rm conf}(z)=\frac1A\left\langle
\sum_{i<j}r_{ij,a}F_{ij,b}
\int_0^1\delta(z-z_j-\lambda z_{ij})d\lambda
\right\rangle
$$

と書ける。ここでは $\mathbf r_{ij}=\mathbf r_i-\mathbf r_j$、$\mathbf F_{ij}$ は粒子 $j$ が $i$ に及ぼす力とする。周期境界では相互作用ベクトルと経路の取り方を整合させる。熱平衡における運動学的寄与は $k_{\rm B}T\rho(z)\delta_{ab}$ であり、法線・接線差から消える。

局所圧力の分布は経路によって異なりうるが、適切な境界条件の下で全空間に積分すれば同じ全ビリアルを回収する。従って平面界面の張力は、この種の局所分配の自由度には依存しない。

これは局所応力の任意の高次モーメントも不変であるという意味ではない。応力分布の一次モーメントを曲率補正や張力面の位置と結びつけるには、熱力学的な分割面と局所応力の定義を区別し、別途導出する必要がある。

## 参考文献

- J. G. Kirkwood and F. P. Buff, “The Statistical Mechanical Theory of Surface Tension,” *Journal of Chemical Physics* **17**, 338–343 (1949).
- J. H. Irving and J. G. Kirkwood, “The Statistical Mechanical Theory of Transport Processes. IV. The Equations of Hydrodynamics,” *Journal of Chemical Physics* **18**, 817–829 (1950).
- J. S. Rowlinson and B. Widom, *Molecular Theory of Capillarity*, Clarendon Press (1982).

- [A perspective on the microscopic pressure (stress) tensor: History, current understanding, and future challenges](https://doi.org/10.1063/5.0132487) (2023).

局所圧力の経路依存性について上記レビューと照合した。Kirkwood–BuffおよびIrving–Kirkwoodの原論文の式番号単位の照合は未完了である。

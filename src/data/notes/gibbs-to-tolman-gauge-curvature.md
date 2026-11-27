---
title: "Gibbsの分割面と表面過剰量"
summary: "平面界面の表面過剰量と吸着方程式を熱力学から導き、分割面を移動する自由度と不変量を整理する。"
publishedAt: 2026-09-09T20:11:00+09:00
updatedAt: 2026-11-28
area: "Physics"
field: interfaces
kind: theory
related: ["young-laplace-coarse-graining", "van-der-waals-diffuse-interface"]
topics: ["interfacial physics", "surface thermodynamics", "Gibbs dividing surface", "surface excess", "gauge redundancy"]
status: growing
---

液体と気体の境界では密度が有限の距離にわたって変化する。界面を厚さゼロの面として熱力学的に扱うためには、どこまでを液体の体積とし、どこからを気体の体積とするかを定める必要がある。Gibbsの分割面はこの体積の割り当てを指定する参照面であり、分子系の中に実在する膜ではない。

## 表面過剰量

平面界面を考え、相 $\alpha$ を左、相 $\beta$ を右とする。任意の位置 $z_0$ に分割面を置き、両相のバルク密度をその位置まで外挿する。成分 $i$ の表面過剰粒子数を単位面積当たりで表すと

$$
\Gamma_i(z_0)=
\int_{-\infty}^{z_0}[\rho_i(z)-\rho_i^\alpha]\,dz+
\int_{z_0}^{\infty}[\rho_i(z)-\rho_i^\beta]\,dz.
$$

これは界面近傍の有限幅の領域に含まれる粒子数ではなく、実際の粒子数とバルク参照系の粒子数との差である。面積を $A$ とすると $N_i^\sigma=A\Gamma_i$ であり、全粒子数は

$$
N_i=\rho_i^\alpha V^\alpha+\rho_i^\beta V^\beta+N_i^\sigma
$$

と分解される。エネルギー $U$、エントロピー $S$ についても同様に表面過剰量を定義する。

## 平面界面の表面自由エネルギー

外部場のない平面流体界面が平衡にあるとする。各相で温度、化学ポテンシャル、圧力が等しい。グランドポテンシャルを $\Omega=U-TS-\sum_i\mu_iN_i$ とすれば、

$$
\Omega^\sigma=\Omega+p^\alpha V^\alpha+p^\beta V^\beta.
$$

平面界面の熱力学極限では $\Omega^\sigma=\gamma A$ と書ける。したがって

$$
\gamma=u^\sigma-Ts^\sigma-\sum_i\mu_i\Gamma_i,
$$

ただし $u^\sigma=U^\sigma/A$、$s^\sigma=S^\sigma/A$ である。ここで $\gamma$ は表面過剰グランドポテンシャルの面積密度であり、吸着がある場合には単に $F^\sigma/A$ と等置できない。

## 分割面の移動

物理状態を固定したまま $z_0$ を $\delta z$ だけ右へ移すと、

$$
\delta V^\alpha=A\delta z,\qquad
\delta V^\beta=-A\delta z
$$

となる。全粒子数が変わらないことから

$$
\Gamma_i(z_0+\delta z)-\Gamma_i(z_0)
=(\rho_i^\beta-\rho_i^\alpha)\delta z.
$$

エントロピーのバルク密度を $s^\alpha,s^\beta$ とすれば、同様に $\delta s^\sigma=(s^\beta-s^\alpha)\delta z$ である。表面過剰エネルギーも同じ規則で変換される。

グランドポテンシャルの分解からは

$$
\delta\gamma=(p^\alpha-p^\beta)\delta z
$$

を得る。平面平衡界面では圧力が等しいので、表面過剰粒子数は分割面に依存しても $\gamma$ は依存しない。曲面界面では圧力差が存在し、さらに参照面の面積も変化するので、この不変性はそのまま成立しない。

## Gibbsの吸着方程式

平面界面の過剰グランドポテンシャルを微分する。外部体積を固定し、分割面の規約を固定した熱力学的変化では、

$$
d\Omega=-S\,dT-\sum_iN_i\,d\mu_i+\gamma\,dA
$$

である。バルクのGibbs–Duhem関係

$$
dp^a=s^a\,dT+\sum_i\rho_i^a\,d\mu_i,\qquad a=\alpha,\beta
$$

を使い、バルク寄与を差し引けば

$$
d(\gamma A)=-S^\sigma dT-\sum_i N_i^\sigma d\mu_i+\gamma dA
$$

となる。したがって

$$
d\gamma=-s^\sigma dT-\sum_i\Gamma_i d\mu_i.
$$

平面二相共存に沿っては $dp^\alpha=dp^\beta$ である。密度差を $\Delta s=s^\beta-s^\alpha$、$\Delta\rho_i=\rho_i^\beta-\rho_i^\alpha$ とすれば

$$
\Delta s\,dT+\sum_i\Delta\rho_i\,d\mu_i=0.
$$

分割面を移動したとき、吸着方程式の右辺に加わる項はこの式の $-\delta z$ 倍であり、ゼロとなる。温度が変化する場合はエントロピー過剰量の変換も含める必要がある。

## 相対吸着量と等モル面

参照成分1について $\Delta\rho_1\ne0$ とする。相対吸着量

$$
\Gamma_i^{(1)}=\Gamma_i-\frac{\Delta\rho_i}{\Delta\rho_1}\Gamma_1
$$

は分割面の移動に対して不変である。これは成分1の過剰量がゼロになる分割面での成分 $i$ の過剰量と一致する。

一成分系では、相間の密度差が非零なら $\Gamma(z_e)=0$ を満たす位置 $z_e$ を一意に選べる。これを等モル面と呼ぶ。多成分系では全成分の過剰量を同時にゼロにできるとは限らない。

## 記述の冗長性

固定した物理状態で定温の表面過剰量ベクトルを考えると、分割面移動は

$$
\boldsymbol\Gamma\mapsto\boldsymbol\Gamma+\lambda\Delta\boldsymbol\rho
$$

という一次元の変換である。分割面によらない線形情報は商空間 $\mathbb R^n/\operatorname{span}(\Delta\boldsymbol\rho)$ によって整理できる。ただし、この商空間が界面の物理状態全体を記述するわけではない。密度分布の形や相関などは表面過剰量だけから復元できない。

この冗長性はゲージ自由度に数学的に似ている。等モル条件は代表元を固定する操作とみなせるが、局所ゲージ対称性やゲージ場を導入しているわけではない。

曲面界面では等モル面とは異なる条件で張力面が定義される。分割面の仮想的な移動と、液滴自体の大きさを変える物理的操作を区別することが、曲率依存表面張力の議論に必要になる。

## 参考文献

- J. W. Gibbs, “On the Equilibrium of Heterogeneous Substances,” (1875–1878).
- J. S. Rowlinson and B. Widom, *Molecular Theory of Capillarity*, Clarendon Press (1982).

書誌の詳細と原典の定義との照合は別途行う。

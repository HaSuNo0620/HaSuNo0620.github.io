---
title: "一次元有限範囲スピン系の統計力学"
summary: "零外場のIsing、Clock、XY鎖を局所増分で統一し、転送作用素、マルコフ過程、基底状態、空間相関と線形応答を導く。"
publishedAt: 2026-09-19T03:15:00+09:00
updatedAt: 2026-11-28
area: "Physics"
field: statistical-physics
kind: theory
topics: ["spin models", "transfer matrix", "finite-range interaction", "correlation"]
status: growing
related: ["ising-transfer-matrix", "ising-r2-transfer-matrix", "clock-chain-nearest-neighbor", "clock-chain-second-neighbor", "xy-chain-nearest-neighbor", "xy-chain-second-neighbor"]
---

一次元スピン鎖の相互作用範囲を広げると、転送行列の状態数が増える。ここでは、零外場で全スピンを同時に回転してもエネルギーが変わらない模型に限定し、隣接スピンの角度差を転送状態に選ぶ。この表示ではIsing、Clock、XY模型の違いを局所状態空間の違いとして扱える。

## 局所増分による表示

格子間隔を1とし、最大相互作用距離を $R$ とする。

$$
H=-\sum_i\sum_{r=1}^R J_r\cos(\theta_{i+r}-\theta_i).
$$

角度は加法群 $G=\mathbb Z_2,\mathbb Z_q,S^1$ のいずれかに属する。有限群の角度は $2\pi a/q$ と同一視する。以下では有限群には計数測度、円周には $d\theta/(2\pi)$ を使う。$\beta=1/(k_{\mathrm B}T)$ とする。

隣接角度差 $\phi_i=\theta_{i+1}-\theta_i$ を導入すると、

$$
H=-\sum_i\sum_{r=1}^R J_r
\cos\left(\sum_{j=0}^{r-1}\phi_{i+j}\right).
$$

開鎖では初期角度と全増分から元の配置を一意に復元できる。周期鎖では $\sum_i\phi_i=0\pmod{2\pi}$ という制約が加わる。従って有限の周期鎖の増分を無条件に独立とみなすことはできない。以下のバルクの議論は開鎖の熱力学極限を用いる。

Ising模型では $\tau_i=e^{i\phi_i}=s_i s_{i+1}=\pm1$ であるため、

$$
H=-\sum_i\sum_{r=1}^R J_r\prod_{j=0}^{r-1}\tau_{i+j}.
$$

元のスピンの距離 $r$ の二体相互作用は、増分表示では長さ $r$ の多体相互作用に対応する。

## 転送作用素

$R\ge2$ とする。転送状態を $a=(a_1,\ldots,a_{R-1})\in G^{R-1}$ とし、新しい増分 $b$ を加えた状態を $S_ba=(a_2,\ldots,a_{R-1},b)$ と書く。

末端の増分を含む局所エネルギーを

$$
E(a,b)=-\sum_{r=1}^R J_r\cos\left(\sum_{j=R-r+1}^{R}x_j\right),
\quad (x_1,\ldots,x_R)=(a_1,\ldots,a_{R-1},b)
$$

と置けば、転送作用素は

$$
(Tf)(a)=\int_G e^{-\beta E(a,b)}f(S_ba)\,d\mu(b)
$$

となる。各相互作用項は一度だけ数えられる。端の不足項はバルク自由エネルギーに影響しない。

有限群では行列の次元は $q^{R-1}$ であり、許される遷移だけが非零となる。円周の場合は $(S^1)^{R-1}$ 上の作用素である。$R-1$ 回の遷移後には任意の履歴へ到達できる。有限温度で結合が有限なら、有限群では行列は原始的であり、円周ではその累乗が連続な正の積分核を持つ。従って最大固有値 $\lambda_0>0$ は単純で、正の右固有関数 $v$ を選べる。

自由エネルギー密度は測度の規約を固定して

$$
f=-\beta^{-1}\log\lambda_0
$$

で与えられる。最近接 $R=1$ は履歴を必要とせず、$\lambda_0=\int_G e^{\beta J_1\cos b}d\mu(b)$ となる。

## 平衡分布とマルコフ過程

転送作用素そのものは確率遷移作用素ではない。$Tv=\lambda_0v$ を使い、

$$
P(a,db)=\frac{e^{-\beta E(a,b)}v(S_ba)}{\lambda_0v(a)}\,d\mu(b)
$$

と定義すると $\int_G P(a,db)=1$ が成り立つ。有限群で左固有ベクトルを $u$ とすれば、定常履歴分布は $\pi(a)=u(a)v(a)$（総和を1に規格化）である。円周でも左固有測度との対応で定常分布を得る。

従って増分列は最大 $R-1$ 次のマルコフ過程として表せる。これは条件付き確率を決めるために必要な過去の長さであって、相関がその距離で消えるという意味ではない。

## スピン相関と傾斜転送作用素

角度の $m$ 次相関は

$$
C_m(\ell)=\left\langle e^{im(\theta_\ell-\theta_0)}\right\rangle
=\left\langle \prod_{j=0}^{\ell-1}e^{im\phi_j}\right\rangle.
$$

各遷移に位相因子を付加した作用素

$$
(T_m f)(a)=\int_G e^{-\beta E(a,b)}e^{imb}f(S_ba)d\mu(b)
$$

を導入すると、定常状態で

$$
C_m(\ell)=\lambda_0^{-\ell}\langle u,T_m^\ell v\rangle,
\qquad \langle u,v\rangle=1
$$

と書ける。左固有測度とのペアリングをここでは $\langle\cdot,\cdot\rangle$ で表した。

一方、$\sin\phi_i$ のような局所増分の観測量の相関は通常の平衡転送作用素のスペクトルから求まる。元のスピン方向と増分の相関は異なる固有値を参照する。

支配的な寄与を持つ固有値を $z=|z|e^{ik}$ とすると、

$$
\xi^{-1}=-\log|z/\lambda_0|,\qquad k=\arg z.
$$

孤立した複素共役対が支配し、振幅が消えない場合、実相関の漸近形は $A e^{-\ell/\xi}\cos(k\ell+\delta)$ となる。複数の寄与がある場合はその和を考える。Jordanブロックがある場合には距離の多項式因子が付くため、単純な指数和とは限らない。

最近接では増分が独立なので、

$$
C_m(\ell)=\left[
\frac{\int_G e^{\beta J_1\cos b}e^{imb}d\mu(b)}
{\int_G e^{\beta J_1\cos b}d\mu(b)}
\right]^\ell.
$$

Isingでは $C_1(\ell)=(\tanh\beta J_1)^\ell$、XYでは $C_m(\ell)=[I_m(\beta J_1)/I_0(\beta J_1)]^\ell$ を回収する。

## 基底状態と相互作用範囲

一様ねじれ $\phi_i=\varphi$ のエネルギー密度は

$$
e_R(\varphi)=-\sum_{r=1}^R J_r\cos(r\varphi).
$$

連続角度のXY鎖では周期境界のFourier変換によりエネルギーを各波数の重み付き和に書ける。Parsevalの等式とスピン長の拘束から $H/N\ge\min_k e_R(k)$ が得られ、許容波数の一様螺旋がこの下限を達成する。熱力学極限では波数は連続になる。

有限Clock鎖では一様ねじれだけでは全配置を探索できない。例えばIsingで $J_1=J>0,J_2=-J$ とすると、一様配置の最低エネルギー密度は0だが、周期配置 $++--$ のエネルギー密度は $-J$ である。

有限状態の場合、履歴を頂点、許される遷移を辺、その局所エネルギーを辺の重みとする有限有向グラフを構成できる。無限鎖の基底エネルギー密度は最小平均重み閉路の値に等しい。長い経路から閉路を順次取り除くと、残る単純経路の長さは頂点数未満であるため、境界寄与を除いた平均エネルギーは最小閉路平均を下回らない。逆に最小閉路の反復はその値を達成する。増分列の閉路が元の角度の周期条件を満たさない場合でも、有限群では閉路を有限回反復すれば角度も元に戻る。

## 空間相関と外場応答

観測量 $A_i$ に共役な外場を $H_h=H-\sum_i h_iA_i$ とすると、

$$
\chi_{ij}=\left.\frac{\partial\langle A_i\rangle}{\partial h_j}\right|_{h=0}
=\beta(\langle A_i A_j\rangle-\langle A_i\rangle\langle A_j\rangle).
$$

並進不変な平衡状態では $\chi_{ij}=\chi(i-j)$ なので、波数 $Q$ の外場に対する線形応答は

$$
\chi(Q)=\beta\sum_{\ell\in\mathbb Z}e^{-iQ\ell}
\langle A_\ell A_0\rangle_{\mathrm c}.
$$

Isingの $A_i=s_i$ では零外場で通常のスピン相関を使う。Clock ($q>2$) とXYの $A_i=\cos\theta_i$ では回転対称性により $x$ 成分相関は角度差の余弦相関の半分になる。奇数 $q$ では反転対称性が一般に存在しないため、非線形応答の二次項を無条件に除けない。

基底状態を選ぶ波数、長距離相関の固有値の位相、感受率が最大になる波数は別の量である。後者は全距離の相関に依存する。例えば $C(\ell)\propto e^{-|\ell|/\xi}\cos(k\ell)$ の連続近似では、感受率は中心 $\pm k$ の二つのLorentz型関数の和となり、$k\xi\le1/\sqrt3$ では最大は $Q=0$ に残る。この条件は近似模型の結果であって一般の格子模型の境界ではない。

## 個別模型への展開

- [最近接Ising鎖](/notes/ising-transfer-matrix/)：反転と厳密相関
- [最近接Clock鎖](/notes/clock-chain-nearest-neighbor/)：角度離散化と連続極限
- [最近接XY鎖](/notes/xy-chain-nearest-neighbor/)：位相拡散と高調波
- [第二近接Ising鎖](/notes/ising-r2-transfer-matrix/)：競合相互作用と振動相関
- [第二近接Clock鎖](/notes/clock-chain-second-neighbor/)：離散状態の基底配置
- [第二近接XY鎖](/notes/xy-chain-second-neighbor/)：螺旋とカイラリティ
- [周期結合Ising鎖](/notes/ising-r1-periodic/)：空間的に変化する相互作用

外場が絶対角度に結合する場合は、増分だけでHamiltonianを閉じることができない。有限範囲の絶対スピン履歴を保持する転送作用素などが必要となる。

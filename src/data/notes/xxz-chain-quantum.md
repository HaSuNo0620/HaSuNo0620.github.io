---
title: "量子XXZ鎖の交換異方性と長距離相関"
summary: "Jordan–Wigner変換とXX極限の厳密解から、XXZ鎖の零温度相構造、Luttinger液体、磁場による相関波数の変化を整理する。"
publishedAt: 2026-09-12T03:15:00+09:00
updatedAt: 2026-11-28
area: "Physics"
field: statistical-physics
kind: model
related: ["xy-chain-nearest-neighbor", "ising-transfer-matrix"]
topics: ["quantum magnetism", "XXZ model", "spin chain", "Jordan-Wigner", "Bethe ansatz", "Luttinger liquid"]
status: growing
---

古典XY鎖では局所状態が連続角度である。量子XXZ鎖では各サイトのHilbert空間は二次元だが、交換相互作用によって異なるスピン配置が重ね合わされる。両者は平面内の回転対称性を共有する場合があっても、相関を生む機構は異なる。

## Hamiltonianと保存量

スピン演算子を $\hbar=1$ の規約で定義し、格子間隔を1とする。

$$
H=J\sum_i(S_i^xS_{i+1}^x+S_i^yS_{i+1}^y+
\Delta S_i^zS_{i+1}^z)-h\sum_i S_i^z,
\qquad J>0.
$$

$\Delta=0$ はXX鎖、$\Delta=1$ は等方的Heisenberg鎖である。横交換項は

$$
S_i^xS_{i+1}^x+S_i^yS_{i+1}^y
=\frac12(S_i^+S_{i+1}^-+S_i^-S_{i+1}^+)
$$

となり、隣接する反平行スピンを交換する。個別の $S_i^z$ は保存されないが、全磁化 $S_{\rm tot}^z$ は保存される。これは $z$ 軸周りの $U(1)$ 対称性に対応する。

## Jordan–Wigner変換

開鎖では

$$
S_i^z=n_i-\frac12,\qquad
S_i^+=c_i^\dagger\exp\left(i\pi\sum_{j<i}n_j\right)
$$

によってスピンを反交換関係を持つフェルミオンへ変換できる。隣接交換項では文字列因子が相殺され、

$$
\begin{aligned}
H={}&\frac J2\sum_i(c_i^\dagger c_{i+1}+c_{i+1}^\dagger c_i)\\
&+J\Delta\sum_i(n_i-\tfrac12)(n_{i+1}-\tfrac12)
-h\sum_i(n_i-\tfrac12)
\end{aligned}
$$

となる。周期鎖ではフェルミオン数の偶奇に依存する境界条件が加わる。以下ではバルクの熱力学極限を扱う。

交換異方性 $\Delta$ はフェルミオン間の密度相互作用となる。$\Delta=0$ ではこの相互作用が消える。

## XX鎖の磁化と厳密相関

$c_j=N^{-1/2}\sum_k e^{ikj}c_k$ とFourier変換すれば、分散は $\varepsilon(k)=J\cos k-h$ である。正のホッピングを用いているので、零温度ではBrillouin帯の端を中心とした占有領域が形成される。

$|h|<J$ において負エネルギーの状態を埋めると、密度と磁化は

$$
n=1-\frac1\pi\arccos(h/J),\qquad
m=n-\frac12=\frac1\pi\arcsin(h/J).
$$

従って零磁場での感受率は $1/(\pi J)$ である。$|h|\ge J$ では磁化は飽和する。

偶数サイトと奇数サイトで符号を変える変換 $c_j=(-1)^j d_j$ を使うと、分散は $-J\cos k-h$ となり、占有領域を $[-k_F,k_F]$ と書ける。この規約では $k_F=\pi n$ である。零磁場では $k_F=\pi/2$、Fermi速度は $v=J$ となる。

Wickの定理から $r\ne0$ に対して縦の連結相関は

$$
\langle S_0^zS_r^z\rangle-m^2
=-|\langle d_0^\dagger d_r\rangle|^2
=-\frac{\sin^2(k_Fr)}{\pi^2r^2}.
$$

これは

$$
-\frac1{2\pi^2r^2}+\frac{\cos(2k_Fr)}{2\pi^2r^2}
$$

と分けられる。指数減衰ではなくべき減衰が現れ、その振動波数は粒子密度によって決まる。横相関ではJordan–Wigner文字列が残るため、単純なフェルミオン二点関数とは一致しない。

## 零磁場での相構造

熱力学極限、零温度、零磁場に限定すると、反強磁性的な交換定数 $J>0$ のXXZ鎖は次のように分類できる。

| 異方性 | 基底状態の性質 |
| --- | --- |
| $\Delta<-1$ | 易軸強磁性、励起にギャップ |
| $\Delta=-1$ | 強磁性Heisenberg鎖とユニタリ同値、二次分散 |
| $-1<\Delta<1$ | ギャップレスなLuttinger液体 |
| $\Delta=1$ | SU(2)対称な臨界点 |
| $\Delta>1$ | Néel秩序、励起にギャップ |

$\Delta=-1$ では交互サイトの $z$ 軸周りの $\pi$ 回転により横交換の符号が反転し、等方的強磁性Heisenberg鎖に写る。この境界は通常の線形分散のLuttinger液体とは異なる。

$\Delta=1$ はNéel相へのBerezinskii–Kosterlitz–Thouless型の量子相転移点である。ギャップの存在と相関の指数減衰は同義ではなく、秩序相の非連結相関には長距離秩序の寄与が残る。

## Luttinger液体の相関

$-1<\Delta<1$ において $\Delta=\cos\gamma$、$0<\gamma<\pi$ とする。零磁場でのBethe仮設から得られる低エネルギー定数は

$$
K_L=\frac{\pi}{2(\pi-\gamma)},\qquad
v=\frac{J\pi\sin\gamma}{2\gamma}.
$$

ここではBethe方程式の解法は扱わず、その既知の結果を用いる。低エネルギーHamiltonianの規約を

$$
H_{\rm LL}=\frac{v}{2\pi}\int dx
\left[K_L(\partial_x\vartheta)^2+
K_L^{-1}(\partial_x\varphi)^2\right]
$$

とする。密度の滑らかな部分を $-\partial_x\varphi/\pi$ と表す規約である。

縦相関と横相関の長距離形は、零磁場で

$$
\langle S_0^zS_r^z\rangle\sim
-\frac{K_L}{2\pi^2r^2}+A_z(-1)^r r^{-2K_L},
$$

$$
\langle S_0^+S_r^-\rangle\sim
A_x(-1)^r r^{-1/(2K_L)}.
$$

振幅 $A_z,A_x$ は微視的模型に依存する。XX点の $K_L=1$ を代入すると、縦相関の指数は先ほどの自由フェルミオン解と一致する。$\Delta\to1$ では $K_L\to1/2$、$v\to J\pi/2$ となる。ただし等方点そのものでは周辺的な相互作用により、相関に対数補正が加わる。

## 磁場と相関波数

磁場はフェルミオンの化学ポテンシャルに相当する。Luttinger液体の一様磁化を変えるには、$\partial_x\varphi=-\pi\delta m$ という一様な密度変化を考えればよい。単位長さ当たりのエネルギー変化は

$$
\delta e=\frac{\pi v}{2K_L}(\delta m)^2-h\delta m
$$

となる。最小化して

$$
\chi=\frac{\partial m}{\partial h}=\frac{K_L}{\pi v}
$$

を得る。有限磁化では $K_L,v$ 自体が磁化に依存し、先ほどの零磁場のBethe仮設の式をそのまま使うことはできない。

縦相関の振動成分は $2k_F=2\pi(m+1/2)$（$2\pi$ を法とする）で特徴づけられる。零磁化での交互相関は $2k_F=\pi$ の特殊例である。有限磁化では一般に非整合な波数が現れる。

$\Delta>-1$ での正磁場側の飽和磁場は $h_s=J(1+\Delta)$ である。完全上向き偏極状態の一マグノンの分散は $h-J\Delta+J\cos k$ なので、その最低励起エネルギーがゼロになる条件に一致する。易軸強磁性領域 $\Delta<-1$ にこの式をそのまま適用してはならない。

## 古典鎖との違い

古典最近接Ising鎖やXY鎖の有限温度相関は、局所増分の熱揺らぎによって指数減衰する。量子XXZ鎖のギャップレス基底状態では、量子揺らぎが存在しても長距離相関はべき減衰する。

この比較では古典系の有限温度と量子系の零温度という条件の違いも重要である。量子臨界鎖でも有限温度を導入すれば、低エネルギーの共形場理論において熱的長さ $\beta v$ が現れる。例えばスケーリング次元 $x$ の一次場の等時刻相関は

$$
\langle O(r)O(0)\rangle_T\propto
\left[\frac{\pi/(\beta v)}{\sinh(\pi r/(\beta v))}\right]^{2x}
$$

となる。短距離では零温度のべき則、十分遠距離では指数減衰となる。局所状態空間だけでなく、温度と量子力学的な時間方向を区別して相関を比較する必要がある。

## 参考文献

- T. Giamarchi, *Quantum Physics in One Dimension*, Oxford University Press (2004).
- M. Takahashi, *Thermodynamics of One-Dimensional Solvable Models*, Cambridge University Press (1999).

- S. Lukyanov and V. Terras, [Long-distance asymptotics of spin–spin correlation functions for the XXZ spin chain](https://www.sciencedirect.com/science/article/pii/S0550321302011410), Nuclear Physics B 654 (2003).
- [Dynamical conductivity of disordered quantum chains](https://doi.org/10.1140/epjd/s10053-022-00524-1) (2022).

Luttingerパラメータの規約と等方点の対数補正を上記文献と照合した。Bethe方程式からの速度の独立導出と原典全文の確認は未完了である。

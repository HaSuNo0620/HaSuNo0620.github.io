---
title: "1次元イジング模型 R=1 — 周期的不均一性と空間モード"
summary: "最近接相互作用の範囲は変えず、結合定数だけを周期的に変調した1次元Ising鎖を読む。独立だが非一様なドメイン壁、可換な転送行列、指数包絡と単位胞変調に分かれる相関、構造由来の波数基底を通して、一様R=2系の相互作用競合との違いを整理する。"
publishedAt: 2026-09-12T01:34:00+09:00
updatedAt: 2026-09-12
area: "Physics"
topics: ["statistical mechanics", "Ising model", "transfer matrix", "correlation", "periodic modulation", "inhomogeneous systems"]
status: growing
---

一様な最近接 Ising 鎖

$$
H=-J\sum_i s_i s_{i+1},
\qquad s_i=\pm1
$$

から先へ進む方法は一つではない。相互作用範囲を $R=2$ へ伸ばす方向とは別に、$R=1$ のまま結合の空間的一様性を壊すことができる。このノートでは

$$
\boxed{
H=-\sum_i J_i s_i s_{i+1},
\qquad J_{i+p}=J_i
}
$$

という周期 $p$ の最近接鎖を考える。

相互作用距離は一つしかないが、Hamiltonian 自体が単位胞 $p$ を持つ。したがって今回の一般化は **interaction range の拡張**ではなく、**spatial homogeneity の破れ**として読む。

![一様R=1と周期的不均一R=1](/figures/ising-r1-periodic/overview-uniform-periodic.svg)

*相互作用距離はどちらも最近接だけである。周期的不均一系では bond の重みが位置に依存し、単位胞 $p$ という新しい空間スケールが Hamiltonian に入る。*

## 1. ドメイン壁は独立なまま、場所ごとに重みが変わる

外場ゼロで bond 変数 $\tau_i\equiv s_i s_{i+1}=\pm1$ を導入すると、

$$
\boxed{
H=-\sum_i J_i\tau_i
}
$$

となる。異なる $\tau_i$ の積は現れないため、周期的不均一性を入れてもドメイン壁同士は相互作用しない。

強磁性的な $J_i>0$ では、$\tau_i=+1$ の bond のエネルギーは $-J_i$、$\tau_i=-1$ では $+J_i$ なので、その bond に壁を作るコストは $\Delta E_i=2J_i$ である。壁の存在確率も

$$
p_{{\rm dw},i}
=\frac{1}{1+e^{2\beta J_i}}
$$

と位置によって変化する。

一様 $R=1$ では **independent identical walls** だったのに対し、周期的不均一 $R=1$ では **independent nonidentical walls** になる。

![周期的bondとドメイン壁](/figures/ising-r1-periodic/domain-wall-periodic.svg)

*周期的不均一性は壁同士を相互作用させるのではなく、壁を置く場所ごとの生成コストを変える。一様 $R=2$ で壁同士の相互作用が生じたこととは別の一般化である。*

## 2. 転送行列は位置ごとに変わるが、外場ゼロでは可換である

bond $i$ に対応する転送行列は

$$
T_i=
\begin{pmatrix}
e^{\beta J_i} & e^{-\beta J_i}\\
e^{-\beta J_i} & e^{\beta J_i}
\end{pmatrix}
=e^{\beta J_i}I+e^{-\beta J_i}\sigma_x.
$$

すべての $T_i$ が $I$ と同じ $\sigma_x$ の線形結合なので、任意の $i,j$ に対して $[T_i,T_j]=0$ である。共通固有ベクトルは

$$
|+\rangle=\frac{1}{\sqrt2}
\begin{pmatrix}1\\1\end{pmatrix},
\qquad
|-\rangle=\frac{1}{\sqrt2}
\begin{pmatrix}1\\-1\end{pmatrix},
$$

対応する固有値は $\lambda_i^{(+)}=2\cosh(\beta J_i)$ と $\lambda_i^{(-)}=2\sinh(\beta J_i)$ である。

一周期の転送行列 $\mathcal T_p=T_1T_2\cdots T_p$ の固有値はしたがって

$$
\boxed{
\Lambda_+
=\prod_{\ell=1}^{p}2\cosh(\beta J_\ell),
\qquad
\Lambda_-
=\prod_{\ell=1}^{p}2\sinh(\beta J_\ell)
}
$$

となる。熱力学極限の自由エネルギー密度は

$$
\boxed{
f
=-\frac{1}{\beta p}
\sum_{\ell=1}^{p}
\ln\!\left[2\cosh(\beta J_\ell)\right]
}
$$

である。

外場ゼロでは、自由エネルギーは一周期に含まれる結合の集合 $\{J_1,\ldots,J_p\}$ には依存するが、その並び順には依存しない。これは転送行列が可換であることの直接的な結果である。

## 3. 相関関数には単位胞内部の並び順が残る

自由エネルギーから消えた単位胞内部の配置は、局所相関には残る。外場ゼロの最近接鎖では

$$
\boxed{
C_i(r)
\equiv\langle s_i s_{i+r}\rangle
=\prod_{n=0}^{r-1}\tanh(\beta J_{i+n})
}
$$

が成り立つ。

$t_\ell\equiv\tanh(\beta J_\ell)$ と書き、一周期分の積を

$$
Q\equiv\prod_{\ell=1}^{p}t_\ell
$$

とする。距離を $r=mp+s$、$0\le s<p$ と分解すると、

$$
\boxed{
C_i(mp+s)
=Q^m\prod_{n=0}^{s-1}t_{i+n}
}
$$

である。一周期進むごとに共通因子 $Q$ が掛かり、その上に単位胞内部の位置 $s$ に依存する変調が乗る。

相関長は

$$
\boxed{
\xi^{-1}
=-\frac1p\ln|Q|
=-\frac1p\sum_{\ell=1}^{p}
\ln\left|\tanh(\beta J_\ell)\right|
}
$$

であり、相関関数は

$$
\boxed{
C_i(r)=e^{-r/\xi}P_i(r\bmod p)
}
$$

という形に整理できる。周期的不均一系では、**長距離の指数包絡**と**単位胞内部の周期変調**が自然に分離する。

![指数包絡と単位胞変調](/figures/ising-r1-periodic/correlation-envelope-modulation.svg)

*長距離減衰は一つの相関長 $\xi$ で支配される一方、単位胞内部の結合順序は周期関数 $P_i$ として残る。*

一様系 $J_\ell=J$ では $Q=\tanh^p(\beta J)$ となり、$\xi^{-1}=-\ln|\tanh(\beta J)|$ と $C(r)=\tanh^r(\beta J)$ を回収する。

## 4. 単位胞は波数基底を与える

$P_i(r\bmod p)$ は周期 $p$ の関数なので、

$$
P_i(r)=\sum_{m=0}^{p-1}A_m^{(i)}e^{iG_mr},
\qquad
\boxed{G_m=\frac{2\pi m}{p}}
$$

と離散 Fourier 展開できる。したがって

$$
\boxed{
C_i(r)
=e^{-r/\xi}
\sum_{m=0}^{p-1}A_m^{(i)}e^{iG_mr}
}
$$

である。

周期的不均一系では、有限波数が相互作用距離の競合から新たに生成されるのではない。Hamiltonian に埋め込まれた単位胞が $G=2\pi/p$ という基本波数を与え、その整数倍が高調波として現れる。

したがって「周期 $p$ の構造が一つの波数を持つ」というとき、正確には **one fundamental wave number + its harmonics** という意味である。

一周期因子 $Q$ の符号も重要である。$Q<0$ なら $C(r+p)=-|Q|C(r)$ となり、一周期ごとに相関の符号が反転する。二周期で元に戻るため実効周期は $2p$ となり、波数は

$$
\boxed{
k_m=\frac{(2m+1)\pi}{p}
}
$$

へシフトする。これは $Q>0$ の $G_m=2\pi m/p$ に対して半 reciprocal-lattice vector だけずれた anti-periodic な構造である。

## 5. 具体例：$AABB$ 周期鎖

粒子種を $AABB\,AABB\cdots$ と並べる。最近接 bond の一周期は

$$
J_{AA},\quad J_{AB},\quad J_{BB},\quad J_{AB}
$$

である。

![AABB周期鎖のbond pattern](/figures/ising-r1-periodic/aabb-bond-pattern.svg)

*$AABB$ 配列では4サイトを単位胞とし、$AA,AB,BB,BA$ の4 bond が繰り返される。*

$a\equiv\tanh(\beta J_{AA})$、$b\equiv\tanh(\beta J_{AB})$、$c\equiv\tanh(\beta J_{BB})$ とすると $Q=ab^2c$ である。たとえば単位胞の最初の $A$ サイトを原点に取れば、

$$
\begin{aligned}
C_{A_1}(4m)&=Q^m,\\
C_{A_1}(4m+1)&=aQ^m,\\
C_{A_1}(4m+2)&=abQ^m,\\
C_{A_1}(4m+3)&=abcQ^m.
\end{aligned}
$$

指数包絡の上に周期4の変調が直接現れている。

特に

$$
J_{AA}=J_{BB}=J>0,
\qquad J_{AB}=-|K|<0
$$

とする。低温では $AA$ と $BB$ bond は同方向、$AB$ bond は逆方向を好むため、すべての局所条件を同時に満たす配列は

$$
++--++--++--\cdots
$$

となる。その基本波数は $k_0=\pi/2$ である。

ここで $\pi/2$ は、一様 $R=2$ 系のように異なる相互作用距離の競合から自己選択された波数ではない。$AABB$ という単位胞と bond の符号パターンによって与えられた波数である。

## 6. 有限温度では局所 bond から単位胞へ視野が広がる

同じ対称模型について $t\equiv\tanh(\beta J)$、$v\equiv\tanh(\beta|K|)$ とおくと、原点平均した構造因子は

$$
\boxed{
S(k)
=\frac{(1+tv)\left[1-tv+(t-v)\cos k\right]}
{(1-tv)^2+4tv\cos^2k}
}
$$

と閉形式で書ける。内部に最大値があるとき、その位置は

$$
\boxed{
\cos k_\star
=\frac{(1-tv)(\sqrt t-\sqrt v)}
{2\sqrt{tv}(\sqrt t+\sqrt v)}
}
$$

で決まる。

ただし、この $k_\star$ を別の基底状態波数が自発的に生まれたと読むべきではない。有限温度では相関長が有限であり、単位胞由来の Fourier 成分が有限幅を持って重なるため、構造因子の最大位置が reciprocal wavevector の間へずれることがある。

高温では $t\simeq\beta J$、$v\simeq\beta|K|$ なので

$$
S(k)
=1+\beta(J-|K|)\cos k
-2\beta^2J|K|\cos2k+\cdots.
$$

最短距離の相関が支配的になり、$|K|<J$ では $k_\star\simeq0$、$|K|>J$ では $k_\star\simeq\pi$ となる。一方、低温では $t,v\to1$ となり相関長が伸びるため、局所的な一つの bond ではなく周期4の単位胞全体が見えるようになり、$k_\star\to\pi/2$ へ向かう。

![AABB鎖における優勢波数の温度依存](/figures/ising-r1-periodic/kstar-temperature.svg)

*高温では局所 bond の平均的性質が優勢だが、低温では単位胞全体の周期4構造が支配的になる。これは熱力学的相転移ではなく、local-bond dominated から unit-cell dominated への相関構造のクロスオーバーである。*

## 7. 一様 $R=2$ とは波数の意味が違う

一様 $R=2$ 模型

$$
H=-J_1\sum_i s_i s_{i+1}-J_2\sum_i s_i s_{i+2}
$$

では、波数空間の相互作用は $J(k)=J_1\cos k+J_2\cos2k$ と書ける。$J_1$ と $J_2$ が競合すると、異なる波数を持つ構造が候補となり、相互作用自身が優勢波数を選択する。

周期的不均一 $R=1$ では事情が異なる。$J_{i+p}=J_i$ とした時点で Hamiltonian に単位胞 $p$ が埋め込まれており、$G=2\pi/p$ という空間スケールが先に存在する。

![周期的不均一R=1と一様R=2](/figures/ising-r1-periodic/periodic-r1-vs-uniform-r2.svg)

*周期的不均一 $R=1$ では構造が波数基底を与える。一様 $R=2$ では1サイト並進対称性を保ったまま、異なる相互作用距離の競合が優勢波数を選択する。*

両者の違いは次のように整理できる。

|  | 周期的不均一 $R=1$ | 一様 $R=2$ |
| --- | --- | --- |
| 新しく導入するもの | bond の空間変調 | 第二近接相互作用 |
| ドメイン壁表示 | 独立だが非一様 | 壁同士が相互作用 |
| 新しい長さスケール | 単位胞 $p$ | 相互作用距離 $1,2$ |
| 有限波数の起源 | imposed periodicity | competing interactions |
| 波数の見方 | $2\pi/p$ と高調波 | $J(k)$ の極値から選択 |

同じ有限波数構造が見えても、その物理的起源は同じではない。

$$
\boxed{
R=1\ {\rm periodic}:
\quad \text{structure imposes the wavevector basis}
}
$$

$$
\boxed{
R=2\ {\rm uniform}:
\quad \text{interactions select the wavevector}
}
$$

という対比が中心になる。

## 8. 外場を入れると可換性は一般に失われる

ここまでの単純さは外場ゼロに強く依存している。位置依存外場を加えて

$$
H=-\sum_iJ_i s_i s_{i+1}-\sum_i h_i s_i
$$

とすると、bond $i$ の転送重みは

$$
T_i(s_i,s_{i+1})
=\exp\!\left[
\beta J_i s_i s_{i+1}
+\frac{\beta}{2}(h_i s_i+h_{i+1}s_{i+1})
\right].
$$

この行列は一般に $I$ と $\sigma_x$ だけでは表せず、$[T_i,T_j]\neq0$ となる。すると $T_1T_2\cdots T_p$ では単位胞内部の並び順が熱力学量にも効く。

したがって外場ゼロの周期的不均一鎖は、**inhomogeneous but commuting** という特別に透明な基準問題である。

## 9. 周期的不均一性から先へ

一様 $R=1$ から不均一性の方向へ進む系列は

$$
\boxed{
\text{uniform}
\longrightarrow
\text{periodic}
\longrightarrow
\text{quasiperiodic}
\longrightarrow
\text{random}
}
$$

と見ることができる。

周期系では有限の単位胞が存在するため、相関を $C_i(r)=e^{-r/\xi}P_i(r\bmod p)$ と分離できた。quasiperiodic 系では有限の単位胞が失われ、random 系では $J_i$ 自体を確率変数として扱うことになる。

それでも $R=1$、外場ゼロなら

$$
\langle s_i s_j\rangle
=\prod_{n=i}^{j-1}\tanh(\beta J_n)
$$

という積構造は残る。周期系は、空間的不均一性が相関へどう写るかを最も透明に学べる最初の例である。

相互作用範囲を増やさなくても、bond の空間組織化によって新しい空間モードは現れる。しかし、その波数は一様 $R=2$ のような競合相互作用による自己選択ではない。**構造が波数基底を与える場合**と**相互作用が波数を選ぶ場合**を区別することが、二つの一般化を並べて理解する鍵になる。

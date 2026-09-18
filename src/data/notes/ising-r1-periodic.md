---
title: "1次元周期最近接 cosine-Z2 スピン系 — 構造波数"
summary: "最近接相互作用の範囲は変えず、結合定数だけを周期的に変調した1次元Ising鎖を読む。独立だが非一様なドメイン壁、可換な転送行列、指数包絡と単位胞変調に分かれる相関、構造由来の波数基底を通して、一様な第二近接系の相互作用競合との違いを整理する。"
publishedAt: 2026-09-12T01:34:00+09:00
updatedAt: 2026-09-19
area: "Physics"
topics: ["statistical mechanics", "Ising model", "transfer matrix", "correlation", "periodic modulation", "inhomogeneous systems"]
status: growing
system:
  dimension: 1
  spatial: periodic
  range: R1
  interaction: cosine
  symmetry: [Z2]
  mechanics: classical
  role: model
---

一様な最近接 Ising 鎖から離れる方向は、相互作用距離を伸ばすことだけではない。最近接のまま

$$
\boxed{
H=-\sum_iJ_i s_i s_{i+1},
\qquad
J_{i+p}=J_i
}
$$

とすれば、Hamiltonian 自体に単位胞 $p$ が入る。

ここで変わるのは 相互作用範囲 ではなく 空間的一様性 である。この違いは、有限波数構造の起源を第二近接系と比較するとかなり明瞭になる。

![一様R=1と周期的不均一R=1](/figures/ising-r1-periodic/overview-uniform-periodic.svg)

*相互作用距離はどちらも最近接だけで、周期系では bond の重みだけが空間変調される。*

## 系の座標

$$
\boxed{
(d=1,\ \text{periodic},\ R=1,\ \text{cosine},\ Z_2)
}
$$

Hamiltonian は

$$
H=-\sum_i J_i s_i s_{i+1},
\qquad
J_{i+p}=J_i,
$$

局所 記憶変数 は

$$
\tau_i=s_i s_{i+1}.
$$

一様最近接 $Z_2$ 系から動かすのは 空間構造 だけで、ドメイン壁の独立性は保ったまま生成コストが位置依存になる。


$Z_2$ では $\theta_i\in\{0,\pi\}$ と置けば

$$
\cos(\theta_i-\theta_j)=s_i s_j
$$

なので、標準 bilinear Ising 相互作用と cosine-$Z_2$ 表現は同値である。

## 1. 壁は独立なまま、生成コストだけが周期化する

$$
\tau_i\equiv s_i s_{i+1}=\pm1
$$

を使うと

$$
\boxed{H=-\sum_iJ_i\tau_i}
$$

であり、異なる $\tau_i$ 同士の積は現れない。

したがって周期的不均一性はドメイン壁同士を相互作用させず、壁を置く場所ごとのコストだけを変える。

強磁性的な $J_i>0$ なら

$$
\Delta E_i=2J_i,
\qquad
p_{{\rm dw},i}=\frac{1}{1+e^{2\beta J_i}}.
$$

一様最近接鎖の **independent identical walls** が、周期系では **independent nonidentical walls** へ変わる。

![周期的bondとドメイン壁](/figures/ising-r1-periodic/domain-wall-periodic.svg)

*周期変調は壁の相互作用ではなく、壁生成コストの位置依存性として現れる。*

## 2. 外場ゼロでは不均一でも transfer matrices は可換である

bond $i$ の転送行列は

$$
T_i=
\begin{pmatrix}
e^{\beta J_i}&e^{-\beta J_i}\\
e^{-\beta J_i}&e^{\beta J_i}
\end{pmatrix}
=e^{\beta J_i}I+e^{-\beta J_i}\sigma_x.
$$

全てが同じ $I,\sigma_x$ の線形結合なので

$$
[T_i,T_j]=0.
$$

共通固有ベクトルに対する固有値は

$$
\lambda_i^{(+)}=2\cosh(\beta J_i),
\qquad
\lambda_i^{(-)}=2\sinh(\beta J_i).
$$

一周期の 転送行列

$$
\mathcal T_p=T_1T_2\cdots T_p
$$

の固有値は

$$
\boxed{
\Lambda_+
=\prod_{\ell=1}^{p}2\cosh(\beta J_\ell),
\qquad
\Lambda_-
=\prod_{\ell=1}^{p}2\sinh(\beta J_\ell)
}
$$

となる。

したがって

$$
\boxed{
f
=-\frac{1}{\beta p}
\sum_{\ell=1}^{p}
\ln[2\cosh(\beta J_\ell)]}
$$

である。

外場ゼロの自由エネルギーは一周期に含まれる結合の集合には依存するが、その並び順には依存しない。周期的なのに順序情報が熱力学量から消えるのは、可換性の直接的な結果である。

## 3. 並び順は局所相関に残る

最近接鎖では厳密に

$$
\boxed{
C_i(r)
\equiv\langle s_i s_{i+r}\rangle
=\prod_{n=0}^{r-1}\tanh(\beta J_{i+n})
}
$$

となる。

$$
t_\ell\equiv\tanh(\beta J_\ell),
\qquad
Q\equiv\prod_{\ell=1}^{p}t_\ell
$$

とし、$r=mp+s$、$0\le s<p$ と分けると

$$
\boxed{
C_i(mp+s)
=Q^m\prod_{n=0}^{s-1}t_{i+n}}
$$

である。

一周期進むごとの指数減衰と、単位胞内部の変調が分離する。

$$
\boxed{
\xi^{-1}
=-\frac1p\ln|Q|
=-\frac1p\sum_{\ell=1}^{p}
\ln|\tanh(\beta J_\ell)|}
$$

より

$$
\boxed{C_i(r)=e^{-r/\xi}P_i(r\bmod p)}
$$

と書ける。

![指数包絡と単位胞変調](/figures/ising-r1-periodic/correlation-envelope-modulation.svg)

*長距離減衰は一つの相関長、単位胞内部の情報は周期変調として残る。*

## 4. 単位胞が波数基底を与える

$P_i$ は周期 $p$ なので

$$
P_i(r)=\sum_{m=0}^{p-1}A_m^{(i)}e^{iG_mr},
\qquad
\boxed{G_m=\frac{2\pi m}{p}}.
$$

したがって

$$
\boxed{
C_i(r)
=e^{-r/\xi}
\sum_{m=0}^{p-1}A_m^{(i)}e^{iG_mr}}
$$

となる。

ここで有限波数は相互作用距離の競合から自己選択されたものではない。Hamiltonian に埋め込まれた単位胞が基本波数 $2\pi/p$ とその高調波を先に与えている。

$Q<0$ なら

$$
C(r+p)=-|Q|C(r)
$$

となり、実効的にはanti-periodicな構造になる。その波数は

$$
\boxed{k_m=\frac{(2m+1)\pi}{p}}
$$

へ半 reciprocal-lattice vector だけシフトする。

## 5. AABB 鎖では周期4が相関に直接現れる

$AABB\,AABB\cdots$ と並べると、bond の一周期は

$$
J_{AA},\quad J_{AB},\quad J_{BB},\quad J_{AB}.
$$

![AABB周期鎖のbond pattern](/figures/ising-r1-periodic/aabb-bond-pattern.svg)

$a=\tanh(\beta J_{AA})$、$b=\tanh(\beta J_{AB})$、$c=\tanh(\beta J_{BB})$ とすれば

$$
Q=ab^2c
$$

で、単位胞先頭からの相関は

$$
\begin{aligned}
C(4m)&=Q^m,\\
C(4m+1)&=aQ^m,\\
C(4m+2)&=abQ^m,\\
C(4m+3)&=abcQ^m.
\end{aligned}
$$

特に

$$
J_{AA}=J_{BB}=J>0,
\qquad
J_{AB}=-|K|<0
$$

なら、低温で局所条件を全て満たす配列は

$$
++--++--\cdots
$$

となり、基本波数は $\pi/2$ になる。

この $\pi/2$ は相互作用競合が後から選んだ波数ではなく、AABB構造に埋め込まれた回転率である。

## 6. 有限温度では局所 bond と単位胞のどちらが見えるかが変わる

対称AABB模型について

$$
t\equiv\tanh(\beta J),
\qquad
v\equiv\tanh(\beta|K|)
$$

とおくと、原点平均した構造因子は

$$
\boxed{
S(k)
=\frac{(1+tv)[1-tv+(t-v)\cos k]}
{(1-tv)^2+4tv\cos^2k}}
$$

となる。

内部最大があるとき

$$
\boxed{
\cos k_\star
=\frac{(1-tv)(\sqrt t-\sqrt v)}
{2\sqrt{tv}(\sqrt t+\sqrt v)}}
$$

である。

高温では短距離bond相関が優勢で、低温では相関長が伸びて周期4の単位胞全体が見えるようになる。その結果 $k_\star$ は $\pi/2$ へ近づく。

![AABB鎖における優勢波数の温度依存](/figures/ising-r1-periodic/kstar-temperature.svg)

*局所結合支配 から 単位胞支配 へのクロスオーバーであり、熱力学的相転移ではない。*

## 7. 第二近接系とは「有限波数」の意味が違う

一様な第二近接模型

$$
H=-J_1\sum_i s_is_{i+1}-J_2\sum_i s_is_{i+2}
$$

では、異なる相互作用距離の競合そのものが優勢波数を変える。

周期最近接系では $J_{i+p}=J_i$ とした時点で単位胞 $p$ が存在し、波数基底は構造から与えられる。

![周期的不均一R=1と一様R=2](/figures/ising-r1-periodic/periodic-r1-vs-uniform-r2.svg)

|  | 周期的最近接 | 一様な第二近接 |
| --- | --- | --- |
| 新しく入るもの | bond の空間変調 | 第二近接相互作用 |
| ドメイン壁表示 | 独立だが非一様 | ドメイン壁同士が相互作用 |
| 長さスケール | 単位胞 $p$ | 相互作用距離 $1,2$ |
| finite-$q$ の起源 | imposed periodicity | competing interactions |

$$
\boxed{
\text{periodic nearest neighbor}:
\text{structure imposes the wavevector basis}}
$$

に対して

$$
\boxed{
\text{uniform second neighbor}:
\text{interactions select the wavevector}}
$$

という違いになる。

## 8. 外場は可換性を壊し、単位胞内部の順序を熱力学へ戻す

位置依存外場を加えると

$$
H=-\sum_iJ_i s_i s_{i+1}-\sum_i h_i s_i
$$

で、局所 転送行列 は

$$
T_i(s_i,s_{i+1})
=\exp\left[
\beta J_i s_i s_{i+1}
+\frac{\beta}{2}(h_i s_i+h_{i+1}s_{i+1})
\right].
$$

一般に

$$
[T_i,T_j]\neq0
$$

となるため、一周期の積 $T_1T_2\cdots T_p$ では内部の並び順が熱力学量にも効く。

外場ゼロの周期鎖は、**inhomogeneous but commuting** という特別に透明な基準問題だったと分かる。

## 9. 一様外場と周期外場は単位胞の応答チャネルを読む

外場を

$$
H_h=-\sum_i h_i s_i
$$

として加える。

一様外場 \(h_i=h\) でも、bond が周期的なら単位胞内部の各サイト応答は一般に同一ではない。単位胞内の磁化ベクトルを \(\mathbf m\)、外場を \(\mathbf h\) とすれば、

$$
\boxed{
\delta\mathbf m(Q) =
\boldsymbol\chi(Q)\mathbf h(Q)
}
$$

という行列応答になる。

周期外場

$$
h_i=h_Q\cos(Qi+\varphi)
$$

は、単位胞の逆格子ベクトル \(G\) により

$$
Q,\qquad Q+G,\qquad Q+2G,\ldots
$$

のチャネルを混合しうる。

したがって一様系の単一 \(\chi(Q)\) に対して、周期 bond 系では

$$
\boxed{
\chi(Q)
\longrightarrow
\boldsymbol\chi_{GG'}(Q)
}
$$

と読む方が自然である。

この応答構造の詳細は [1次元周期最近接 cosine-\(Z_2\) スピン系 — 周期外場と応答モード](/notes/ising-r1-periodic-field) で扱う。

## 10. 周期性は不均一性系列の最初の非自明な段階になる

最近接・零外場なら、さらに

$$
\text{uniform}
\longrightarrow
\text{periodic}
\longrightarrow
\text{quasiperiodic}
\longrightarrow
\text{random}
$$

という不均一性の系列を考えられる。

周期系では有限単位胞があるため、指数包絡と周期変調を分離できる。quasiperiodic系では有限単位胞が失われ、random系では $J_i$ 自体が確率変数になる。

それでも最近接・零外場なら

$$
\boxed{
\langle s_i s_j\rangle
=\prod_{n=i}^{j-1}\tanh(\beta J_n)}
$$

という積構造は残る。

周期最近接鎖は、相互作用範囲を増やさずに空間組織化だけを変えたとき、構造がどのように相関と波数基底へ写るかを見る基準点になっている。

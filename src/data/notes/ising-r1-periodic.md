---
title: "1次元周期最近接 cosine-Z2 スピン系 — 構造波数と周期外場応答"
summary: "周期的最近接結合を持つ1次元Z2鎖を、独立だが非一様なドメイン壁、単位胞由来の構造波数、外場による転送行列の非可換化、一様・周期磁化、感受率チャネルとモード混合まで一つの模型ノートとして整理する。"
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

局所変数 は

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

## 8. 周期外場と応答モード

周期外場まで含めると、零外場で見えた「独立だが非一様なドメイン壁」と「単位胞由来の波数基底」が、実際の応答チャネルとして現れる。

### 1. 外場は ドメイン壁表示を非局所化する

零外場では

$$
\tau_i=s_i s_{i+1}
$$

によって

$$
H_0=-\sum_iJ_i\tau_i
$$

と書けた。

しかし

$$
s_i=s_1\prod_{k=1}^{i-1}\tau_k
$$

なので、外場項は

$$
-\sum_i h_i s_i
=-s_1\sum_i h_i\prod_{k=1}^{i-1}\tau_k
$$

となる。

相互作用は ドメイン壁表示で局所化できても、絶対方向を測る外場は長い積へ変わる。ここではスピン表示の方が局所的である。

### 2. 外場は transfer matrices の共通固有軸を壊す

外場をbond両端へ半分ずつ割り振ると

$$
T_i(s_i,s_{i+1})
=\exp\left[
\beta J_i s_i s_{i+1}
+\frac{\beta}{2}(h_i s_i+h_{i+1}s_{i+1})
\right].
$$

行列表現は

$$
\boxed{
T_i=
\begin{pmatrix}
e^{\beta J_i+\frac\beta2(h_i+h_{i+1})}
&e^{-\beta J_i+\frac\beta2(h_i-h_{i+1})}\\
e^{-\beta J_i-\frac\beta2(h_i-h_{i+1})}
&e^{\beta J_i-\frac\beta2(h_i+h_{i+1})}
\end{pmatrix}}
$$

である。

$h_i=0$ では全ての $T_i$ が同じ固有軸を持っていたが、位置依存外場を入れると一般に

$$
[T_i,T_j]\neq0
$$

となる。

![外場による非可換化](/figures/ising-r1-periodic-field/noncommuting-transfer.svg)

*外場は局所転送行列の固有軸を位置ごとに回し、積の順序を物理量へ戻す。*

### 3. 非可換でも有限周期なら $2\times2$ の一周期問題に閉じる

一周期の 転送行列 を

$$
\boxed{
\mathcal T_p=T_1T_2\cdots T_p}
$$

とする。

その固有値は

$$
\boxed{
\Lambda_\pm
=\frac{\operatorname{Tr}\mathcal T_p
\pm\sqrt{(\operatorname{Tr}\mathcal T_p)^2-4\det\mathcal T_p}}{2}}
$$

である。

各局所行列の determinant は

$$
\det T_i=2\sinh(2\beta J_i)
$$

なので

$$
\boxed{
\det\mathcal T_p
=\prod_{\ell=1}^{p}2\sinh(2\beta J_\ell)}
$$

となり、外場には依存しない。

熱力学極限では

$$
\boxed{
f=-\frac{1}{\beta p}\ln\Lambda_+}
$$

である。可換性は失われても、有限周期性が残る限り厳密解は一周期行列へ縮約できる。

### 4. 外場と磁化は単位胞の Fourier channel に分かれる

単位胞内サイトを $\alpha=1,\ldots,p$ とすると

$$
\boxed{
m_\alpha
=\frac{1}{\beta}
\frac{\partial\ln\Lambda_+}{\partial h_\alpha}}
$$

である。

単位胞 reciprocal wavevector

$$
G_n=\frac{2\pi n}{p}
$$

を使えば、外場と磁化を同じ Fourier basis へ分解できる。一様外場は $G_0=0$、周期外場は $G_n\neq0$ の構造modeへ直接結合する。

![周期外場とFourierモード](/figures/ising-r1-periodic-field/field-fourier-coupling.svg)

### 5. 対称 AABB では一様 mode と周期4 mode が自然な座標になる

$$
J_{AA}=J_{BB}=J,
\qquad
J_{AB}=K
$$

とし、外場を

$$
(h_1,h_2,h_3,h_4)=(h_A,h_A,h_B,h_B)
$$

とする。

$$
h_0\equiv\frac{h_A+h_B}{2},
\qquad
h_{\rm AB}\equiv\frac{h_A-h_B}{2}
$$

なら

$$
(h_1,h_2,h_3,h_4)
=h_0(1,1,1,1)+h_{\rm AB}(1,1,-1,-1).
$$

$h_0$ は $q=0$、$h_{\rm AB}$ は $q=\pm\pi/2$ に対応する。

磁化側も

$$
m_0\equiv\frac14(m_1+m_2+m_3+m_4),
$$

$$
m_{\rm AB}\equiv\frac14(m_1+m_2-m_3-m_4)
$$

と分ける。

![AABBの外場モード](/figures/ising-r1-periodic-field/aabb-field-modes.svg)

*一様channelと周期4 channelを、外場と磁化の両側で同じbasisに取る。*

### 6. 対称模型では二つの外場変数で厳密に閉じる

$$
\mathcal J=\beta J,
\qquad
\mathcal K=\beta K,
\qquad
\nu=\beta h_0,
\qquad
d=\beta h_{\rm AB}
$$

とおく。

一周期行列の trace は

$$
\boxed{
\begin{aligned}
\Theta(\nu,d)
={}&4e^{-2\mathcal J}\cosh(2\mathcal K)
+2e^{2\mathcal J+2\mathcal K}\cosh(4\nu)\\
&+2e^{2\mathcal J-2\mathcal K}\cosh(4d)
+8\cosh(2\nu)\cosh(2d)
\end{aligned}}
$$

となる。

$$
D=16\sinh^2(2\mathcal J)\sinh^2(2\mathcal K),
\qquad
\Delta=\sqrt{\Theta^2-4D}
$$

とすれば、磁化は

$$
\boxed{
m_0
=\frac{2e^{2\mathcal J+2\mathcal K}\sinh(4\nu)
+4\sinh(2\nu)\cosh(2d)}{\Delta}}
$$

$$
\boxed{
m_{\rm AB}
=\frac{2e^{2\mathcal J-2\mathcal K}\sinh(4d)
+4\cosh(2\nu)\sinh(2d)}{\Delta}}
$$

となる。

### 7. 対称性が 応答-channel decoupling を作る

零外場では

$$
\boxed{
\chi_{00}
=\beta\frac{e^{\mathcal J+\mathcal K}}
{\cosh(\mathcal J-\mathcal K)}}
$$

$$
\boxed{
\chi_{{\rm AB}{\rm AB}}
=\beta\frac{e^{\mathcal J-\mathcal K}}
{\cosh(\mathcal J+\mathcal K)}}
$$

であり

$$
\boxed{
\chi_{0{\rm AB}}=0}
$$

となる。

周期性があるだけでは線形mode mixingは起こらない。$J_{AA}=J_{BB}$ という対称性が、一様channelと周期4 channelを分離している。

$K>0$ では一様channel、$K<0$ では周期4 channelが強くなる。

![一様・周期感受率の温度依存](/figures/ising-r1-periodic-field/susceptibility-channels.svg)

### 8. $J_{AA}\neq J_{BB}$ は mode mixing を許す対称性破れになる

$$
\mathcal A=\beta J_{AA},
\qquad
\mathcal B=\beta J_{BB},
\qquad
\mathcal K=\beta J_{AB}
$$

とする。

零外場で

$$
\Theta_0
=8\left[
\cosh(\mathcal A+\mathcal B)\cosh(2\mathcal K)
+\cosh(\mathcal A-\mathcal B)
\right]
$$

および

$$
D_0
=16\sinh(2\mathcal A)\sinh(2\mathcal B)\sinh^2(2\mathcal K)
$$

を得る。

$$
\mathcal S\equiv
\sqrt{
\left[
\cosh(\mathcal A+\mathcal B)\cosh(2\mathcal K)
+\cosh(\mathcal A-\mathcal B)
\right]^2
-\sinh(2\mathcal A)\sinh(2\mathcal B)\sinh^2(2\mathcal K)}
$$

とおくと

$$
\boxed{
\chi_{00}
=\beta\frac{
\cosh(\mathcal A-\mathcal B)
+e^{\mathcal A+\mathcal B+2\mathcal K}}
{\mathcal S}}
$$

$$
\boxed{
\chi_{{\rm AB}{\rm AB}}
=\beta\frac{
\cosh(\mathcal A-\mathcal B)
+e^{\mathcal A+\mathcal B-2\mathcal K}}
{\mathcal S}}
$$

$$
\boxed{
\chi_{0{\rm AB}}
=\beta\frac{\sinh(\mathcal A-\mathcal B)}{\mathcal S}}
$$

となる。

最後の式が非対称性の役割を直接表している。$J_{AA}=J_{BB}$ では消える cross 応答 が、差を入れた瞬間に立ち上がる。

$$
\boxed{
J_{AA}-J_{BB}
:\ 
\text{応答-channel decoupling を壊す対称性破れ}}
$$

と読める。

### 9. 固有応答 mode は bare mode の回転になる

感受率行列

$$
\boldsymbol\chi=
\begin{pmatrix}
\chi_{00}&\chi_{0{\rm AB}}\\
\chi_{0{\rm AB}}&\chi_{{\rm AB}{\rm AB}}
\end{pmatrix}
$$

の固有値は

$$
\boxed{
\chi_\pm
=\frac{\chi_{00}+\chi_{{\rm AB}{\rm AB}}}{2}
\pm
\sqrt{
\left(\frac{\chi_{00}-\chi_{{\rm AB}{\rm AB}}}{2}\right)^2
+\chi_{0{\rm AB}}^2}}
$$

である。

混合角 $\theta$ は

$$
\boxed{
\tan(2\theta)
=\frac{\sinh(\mathcal A-\mathcal B)}
{e^{\mathcal A+\mathcal B}\sinh(2\mathcal K)}}
$$

となる。

つまり固有応答は、一様modeと周期4 modeのどちらかではなく、その線形結合になる。

### 10. 応答 map は相図ではない

$$
\bar J\equiv\frac{J_{AA}+J_{BB}}{2},
\qquad
\delta J\equiv\frac{J_{AA}-J_{BB}}{2}
$$

とする。

厳密な二本の線は

$$
\boxed{
\delta J=0
\Longleftrightarrow
\chi_{0{\rm AB}}=0}
$$

と

$$
\boxed{
J_{AB}=0
\Longleftrightarrow
\chi_{00}=\chi_{{\rm AB}{\rm AB}}}
$$

である。

![AABB周期外場系の応答構造マップ](/figures/ising-r1-periodic-field/response-structure-map.svg)

*どのchannelが優勢か、どこで分離し、どこで混ざるかを示す応答構造マップ。有限温度相図ではない。*

$J_{AB}>0$ では一様成分が、$J_{AB}<0$ では周期4成分が優勢になる。$\delta J$ の符号は混合方向を反転させる。

### 11. 長距離相関は一周期スペクトル に残る

外場下では連結相関

$$
C_{ij}^{\rm conn}
=\langle s_i s_j\rangle
-\langle s_i\rangle\langle s_j\rangle
$$

を見る。

一周期 転送行列 の固有値を $\Lambda_+,\Lambda_-$ とすれば

$$
C^{\rm conn}(mp)
\sim
\left(\frac{\Lambda_-}{\Lambda_+}\right)^m
$$

なので

$$
\boxed{
\xi=-\frac{p}{\ln|\Lambda_-/\Lambda_+|}}
$$

となる。

bond積による単純な相関式は失われても、**転送スペクトル が空間相関を運ぶ**という骨格は変わらない。

### 12. bond周期とfield周期の不一致は supercell を作る

bond周期を $p_J$、field周期を $p_h$ とすると、有限整数周期なら全系の周期は通常

$$
\boxed{
p=\operatorname{lcm}(p_J,p_h)}
$$

である。

外場波数がbond reciprocal vectorと一致すれば構造modeへ直接結合し、一致しなければ大きなsupercellの中で複数modeが混ざる。有限共通周期そのものを失うと quasiperiodic 問題へ移る。

### 13. 第二近接系との違いは「波数を誰が決めるか」にある

周期最近接系では単位胞が reciprocal mode を先に与え、外場はその structure-imposed mode を選択的に励起する。

一様な第二近接系では、相互作用競合そのものが応答しやすい有限波数を選ぶ。

![周期R1と一様R2の外場応答](/figures/ising-r1-periodic-field/periodic-r1-vs-r2-field.svg)

$$
\boxed{
\text{periodic structure}
\longrightarrow
\text{mode-selective 応答}
\longrightarrow
\text{対称性-breaking-induced mode mixing}}
$$

という連鎖が、この模型で一番見通しよく残る構造である。


## 9. 周期性は不均一性系列の最初の非自明な段階になる

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

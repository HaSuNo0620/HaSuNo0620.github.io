---
title: "1次元周期最近接 cosine-Z2 スピン系 — 周期外場と応答モード"
summary: "周期的最近接結合を持つ1次元Ising鎖へ周期外場を加える。外場による転送行列の非可換化、一周期転送行列による厳密解、AABB鎖の一様・周期磁化と感受率、さらに J_AA ≠ J_BB で現れる線形mode mixingまで解析し、応答構造マップとして整理する。"
publishedAt: 2026-09-12T01:55:00+09:00
updatedAt: 2026-09-19
area: "Physics"
topics: ["statistical mechanics", "Ising model", "transfer matrix", "periodic modulation", "external field", "linear response"]
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

周期最近接鎖の零外場では、bond変数は独立で transfer matrices も可換だった。そのため自由エネルギーは単位胞内部の並び順を忘れ、相関だけが順序を記憶していた。

位置依存外場を加えると

$$
\boxed{
H=-\sum_iJ_i s_i s_{i+1}-\sum_i h_i s_i,
\qquad
J_{i+p}=J_i,
\quad
h_{i+p}=h_i
}
$$

となる。相互作用範囲は最近接のままだが、外場がスピンの絶対方向を持ち込むことで可換性が壊れ、単位胞内部の順序が熱力学へ戻ってくる。

一方、transfer state は依然として1スピンだけで閉じる。複雑化しているのは状態数ではなく、**一周期の中で異なる局所作用が順序を持って積み重なること**である。

![周期bondと周期外場](/figures/ising-r1-periodic-field/overview-periodic-field.svg)

*周期bondと周期外場の相対配置が、一周期転送行列を通して熱力学へ入る。*

## 系の座標

$$
\boxed{
(d=1,\ \text{periodic},\ R=1,\ \text{cosine},\ Z_2)
}
$$

周期 bond に周期外場を重ね、

$$
H = -\sum_i J_i s_i s_{i+1}
-\sum_i h_i s_i,
$$

$$
J_{i+p_J}=J_i,
\qquad
h_{i+p_h}=h_i
$$

とする。局所ドメイン壁変数は

$$
\tau_i=s_i s_{i+1}
$$

だが、外場は 絶対スピン を読むため ドメイン壁表示を非局所化する。ここでは「同じ模型座標に外場を加えたとき、何の情報が混ざるか」を追う。


$Z_2$ では $\theta_i\in\{0,\pi\}$ と置けば

$$
\cos(\theta_i-\theta_j)=s_i s_j
$$

なので、標準 bilinear Ising 相互作用と cosine-$Z_2$ 表現は同値である。

## 1. 外場は ドメイン壁表示を非局所化する

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

## 2. 外場は transfer matrices の共通固有軸を壊す

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

## 3. 非可換でも有限周期なら $2\times2$ の一周期問題に閉じる

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

## 4. 外場と磁化は単位胞の Fourier channel に分かれる

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

## 5. 対称 AABB では一様 mode と周期4 mode が自然な座標になる

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

## 6. 対称模型では二つの外場変数で厳密に閉じる

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

## 7. 対称性が 応答-channel decoupling を作る

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

## 8. $J_{AA}\neq J_{BB}$ は mode mixing を許す対称性破れになる

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

## 9. 固有応答 mode は bare mode の回転になる

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

## 10. 応答 map は相図ではない

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

![AABB周期外場系の応答構造マップ](/figures/ising-r1-periodic-field/応答-structure-map.svg)

*どのchannelが優勢か、どこで分離し、どこで混ざるかを示す応答構造マップ。有限温度相図ではない。*

$J_{AB}>0$ では一様成分が、$J_{AB}<0$ では周期4成分が優勢になる。$\delta J$ の符号は混合方向を反転させる。

## 11. 長距離記憶は一周期スペクトル に残る

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

bond積による単純な相関式は失われても、**転送スペクトル が空間記憶を運ぶ**という骨格は変わらない。

## 12. bond周期とfield周期の不一致は supercell を作る

bond周期を $p_J$、field周期を $p_h$ とすると、有限整数周期なら全系の周期は通常

$$
\boxed{
p=\operatorname{lcm}(p_J,p_h)}
$$

である。

外場波数がbond reciprocal vectorと一致すれば構造modeへ直接結合し、一致しなければ大きなsupercellの中で複数modeが混ざる。有限共通周期そのものを失うと quasiperiodic 問題へ移る。

## 13. 第二近接系との違いは「波数を誰が決めるか」にある

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

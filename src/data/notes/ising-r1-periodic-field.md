---
title: "1次元イジング模型 — 周期外場と応答モード"
summary: "周期的最近接結合を持つ1次元Ising鎖へ周期外場を加える。外場による転送行列の非可換化、一周期転送行列による厳密解、AABB鎖の一様・周期磁化と感受率、さらに J_AA ≠ J_BB で現れる線形mode mixingまで解析し、応答構造マップとして整理する。"
publishedAt: 2026-09-12T01:55:00+09:00
updatedAt: 2026-09-12
area: "Physics"
topics: ["statistical mechanics", "Ising model", "transfer matrix", "periodic modulation", "external field", "linear response"]
status: growing
---

前のノートでは、最近接相互作用の範囲 $R=1$ を保ったまま結合を周期化し、

$$
H_0=-\sum_i J_i s_i s_{i+1},
\qquad J_{i+p}=J_i
$$

を考えた。外場ゼロでは bond 変数 $\tau_i=s_i s_{i+1}$ が互いに独立で、転送行列も可換だった。その結果、自由エネルギーは一周期内の bond の並び順に依存せず、相関だけが単位胞内部の順序を記憶した。

ここでは位置依存外場を加え、

$$
\boxed{
H=-\sum_i J_i s_i s_{i+1}-\sum_i h_i s_i,
\qquad
J_{i+p}=J_i,
\quad
h_{i+p}=h_i
}
$$

を考える。外場を加えても相互作用範囲は $R=1$ のままであるが、転送行列は一般に非可換になり、単位胞内部の順序が熱力学へ現れる。一方、転送状態は依然として1スピンだけで閉じるため、有限周期なら問題は $2\times2$ の一周期転送行列へ還元できる。

このノートでは一般周期 $p$ の構造を整理した後、$AABB$ 鎖に一様外場と周期外場を同時に入れる。さらに $J_{AA}=J_{BB}$ の対称模型から $J_{AA}\neq J_{BB}$ へ進み、一様 mode と周期4 mode がどの条件で分離し、どの条件で混ざるかまで解析する。

![周期bondと周期外場](/figures/ising-r1-periodic-field/overview-periodic-field.svg)

*周期的 bond に周期外場を重ねる。相互作用距離は増えていないが、bond の単位胞と field の単位胞が同時に現れ、その相対配置が物理量に効く。*

## 1. 外場はドメイン壁表示を非局所化する

外場ゼロでは $\tau_i=s_i s_{i+1}$ によって

$$
H_0=-\sum_i J_i\tau_i
$$

となり、異なる bond 変数は直接結合しなかった。しかし基準スピン $s_1$ を残すと $s_i=s_1\prod_{k=1}^{i-1}\tau_k$ なので、外場項は

$$
-\sum_i h_i s_i
=-s_1\sum_i h_i\prod_{k=1}^{i-1}\tau_k
$$

となる。外場はスピンの絶対的な向きを見るため、ドメイン壁表示では長い積として非局所的に現れる。したがって外場を含む問題では、スピン表示と転送行列へ戻る方が自然である。

## 2. 外場を入れると転送行列は一般に非可換になる

外場を bond の両端へ半分ずつ割り振り、

$$
T_i(s_i,s_{i+1})
=\exp\left[
\beta J_i s_i s_{i+1}
+\frac{\beta}{2}(h_i s_i+h_{i+1}s_{i+1})
\right]
$$

と定義する。行列表現は

$$
\boxed{
T_i=
\begin{pmatrix}
e^{\beta J_i+\frac{\beta}{2}(h_i+h_{i+1})}
& e^{-\beta J_i+\frac{\beta}{2}(h_i-h_{i+1})}\\
e^{-\beta J_i-\frac{\beta}{2}(h_i-h_{i+1})}
& e^{\beta J_i-\frac{\beta}{2}(h_i+h_{i+1})}
\end{pmatrix}
}
$$

である。$h_i=0$ では各 $T_i$ は $I$ と $\sigma_x$ の線形結合だったが、外場があると一般に $[T_i,T_j]\neq0$ となる。

![外場による非可換化](/figures/ising-r1-periodic-field/noncommuting-transfer.svg)

*外場ゼロでは各 bond 転送行列の固有軸が共通だが、位置依存外場を加えると内部空間での向きが変わる。*

## 3. 非可換でも一周期行列は $2\times2$ のままである

一周期の転送行列を

$$
\boxed{
\mathcal T_p=T_1T_2\cdots T_p
}
$$

とする。$\mathcal T_p$ の固有値は

$$
\boxed{
\Lambda_\pm
=\frac{\operatorname{Tr}\mathcal T_p
\pm\sqrt{(\operatorname{Tr}\mathcal T_p)^2-4\det\mathcal T_p}}{2}
}
$$

である。各 bond 行列の行列式は $\det T_i=2\sinh(2\beta J_i)$ なので、

$$
\boxed{
\det\mathcal T_p
=\prod_{\ell=1}^{p}2\sinh(2\beta J_\ell)
}
$$

となり、外場には依存しない。熱力学極限では最大固有値 $\Lambda_+$ が支配し、1サイトあたり自由エネルギーは

$$
\boxed{
f=-\frac{1}{\beta p}\ln\Lambda_+
}
$$

である。したがって可換性は失われても、有限周期なら厳密解は失われない。

## 4. 単位胞内磁化と外場Fourierモード

周期 $p$ の単位胞内サイトを $\alpha=1,\ldots,p$ とする。各 sublattice の磁化は

$$
\boxed{
m_\alpha
=\frac{1}{\beta}
\frac{\partial\ln\Lambda_+}{\partial h_\alpha}
}
$$

で得られる。単位胞内の reciprocal wavevector は $G_n=2\pi n/p$ なので、外場も磁化も離散 Fourier 成分へ分解できる。一様外場は $G_0=0$ へ、周期外場は $G_n\neq0$ の構造モードへ直接結合する。

![周期外場とFourierモード](/figures/ising-r1-periodic-field/field-fourier-coupling.svg)

*一様成分は $G=0$ へ、周期成分は有限 $G$ の磁化へ結合する。*

## 5. 対称 $AABB$ 鎖では一様 mode と周期4 mode を分けられる

まず

$$
J_{AA}=J_{BB}=J,
\qquad J_{AB}=K
$$

とする。外場は $(h_1,h_2,h_3,h_4)=(h_A,h_A,h_B,h_B)$ とし、

$$
h_0\equiv\frac{h_A+h_B}{2},
\qquad
h_{\rm AB}\equiv\frac{h_A-h_B}{2}
$$

を導入する。すると

$$
(h_1,h_2,h_3,h_4)
=h_0(1,1,1,1)+h_{\rm AB}(1,1,-1,-1)
$$

である。$h_0$ は $q=0$ の一様外場、$h_{\rm AB}$ は周期4、すなわち $q=\pm\pi/2$ 成分へ結合する外場である。

対応する磁化を

$$
m_0\equiv\frac14(m_1+m_2+m_3+m_4),
\qquad
m_{\rm AB}\equiv\frac14(m_1+m_2-m_3-m_4)
$$

とする。

![AABBの外場モード](/figures/ising-r1-periodic-field/aabb-field-modes.svg)

*$h_0$ は全サイトを同方向へ押し、$h_{\rm AB}$ は $AA$ と $BB$ を逆向きへ押す。*

## 6. 対称 $AABB$ の一周期行列は二つの外場変数で閉じる

$\mathcal J\equiv\beta J$、$\mathcal K\equiv\beta K$、$\nu\equiv\beta h_0$、$d\equiv\beta h_{\rm AB}$ とする。一周期行列の trace は

$$
\boxed{
\begin{aligned}
\Theta(\nu,d)
={}&4e^{-2\mathcal J}\cosh(2\mathcal K)
+2e^{2\mathcal J+2\mathcal K}\cosh(4\nu)\\
&+2e^{2\mathcal J-2\mathcal K}\cosh(4d)
+8\cosh(2\nu)\cosh(2d)
\end{aligned}
}
$$

となる。determinant は

$$
D=16\sinh^2(2\mathcal J)\sinh^2(2\mathcal K)
$$

である。$\Delta(\nu,d)\equiv\sqrt{\Theta^2-4D}$ とすれば、$\Lambda_+=(\Theta+\Delta)/2$ で熱力学が決まる。

磁化は

$$
\boxed{
m_0
=\frac{2e^{2\mathcal J+2\mathcal K}\sinh(4\nu)
+4\sinh(2\nu)\cosh(2d)}{\Delta(\nu,d)}
}
$$

および

$$
\boxed{
m_{\rm AB}
=\frac{2e^{2\mathcal J-2\mathcal K}\sinh(4d)
+4\cosh(2\nu)\sinh(2d)}{\Delta(\nu,d)}
}
$$

となる。

## 7. 対称模型のゼロ外場では二つの応答channelが分離する

ゼロ外場では

$$
\boxed{
\chi_{00}
=\beta\frac{e^{\mathcal J+\mathcal K}}
{\cosh(\mathcal J-\mathcal K)},
\qquad
\chi_{{\rm AB}{\rm AB}}
=\beta\frac{e^{\mathcal J-\mathcal K}}
{\cosh(\mathcal J+\mathcal K)}
}
$$

であり、対称性から

$$
\boxed{
\chi_{0{\rm AB}}=\chi_{{\rm AB}0}=0
}
$$

となる。したがって periodicity があるだけでは線形 order で mode mixing は起こらない。

$K>0$ では一様 channel が、$K<0$ では周期4 channel が強くなる。$K=J$ の一様強磁性極限では $\chi_{00}=\beta e^{2\mathcal J}$、$\chi_{{\rm AB}{\rm AB}}=\beta/\cosh(2\mathcal J)$ となる。逆に $K=-J$ では両者が入れ替わり、$++--$ 構造に共役な $q=\pi/2$ 応答が低温で増幅される。

![一様・周期感受率の温度依存](/figures/ising-r1-periodic-field/susceptibility-channels.svg)

*対称 $AABB$ 鎖では、$K>0$ で一様 channel、$K<0$ で周期4 channel が優勢になる。*

## 8. $J_{AA}\neq J_{BB}$ にすると線形 mode mixing が現れる

ここから対称条件を外し、

$$
J_{AA}\neq J_{BB},
\qquad J_{AB}=K
$$

を考える。無次元結合を

$$
\mathcal A\equiv\beta J_{AA},
\qquad
\mathcal B\equiv\beta J_{BB},
\qquad
\mathcal K\equiv\beta K
$$

とする。

ゼロ外場では一周期行列の trace は

$$
\boxed{
\Theta_0
=8\left[
\cosh(\mathcal A+\mathcal B)\cosh(2\mathcal K)
+\cosh(\mathcal A-\mathcal B)
\right]
}
$$

であり、

$$
D_0
=16\sinh(2\mathcal A)\sinh(2\mathcal B)\sinh^2(2\mathcal K)
$$

となる。簡単のため

$$
\boxed{
\mathcal S\equiv
\sqrt{
\left[
\cosh(\mathcal A+\mathcal B)\cosh(2\mathcal K)
+\cosh(\mathcal A-\mathcal B)
\right]^2
-\sinh(2\mathcal A)\sinh(2\mathcal B)\sinh^2(2\mathcal K)
}
}
$$

と置く。

このとき、ゼロ外場の $2\times2$ 感受率行列は完全に閉じて

$$
\boxed{
\chi_{00}
=\beta\frac{
\cosh(\mathcal A-\mathcal B)
+e^{\mathcal A+\mathcal B+2\mathcal K}
}{\mathcal S}
}
$$

$$
\boxed{
\chi_{{\rm AB}{\rm AB}}
=\beta\frac{
\cosh(\mathcal A-\mathcal B)
+e^{\mathcal A+\mathcal B-2\mathcal K}
}{\mathcal S}
}
$$

および

$$
\boxed{
\chi_{0{\rm AB}}
=\chi_{{\rm AB}0}
=\beta\frac{
\sinh(\mathcal A-\mathcal B)
}{\mathcal S}
}
$$

となる。

最後の式が $J_{AA}\neq J_{BB}$ の意味を最も直接的に示す。$J_{AA}=J_{BB}$ なら $\chi_{0{\rm AB}}=0$ だが、A/B 内部結合の非対称性を入れると、ゼロ外場の線形応答から一様 mode と周期 mode が混ざる。

つまり $J_{AA}-J_{BB}$ は、単なる追加パラメータではなく、**response-channel decoupling を壊す対称性破れ**として読める。

## 9. 混合した固有応答modeを対角化する

感受率行列を

$$
\boldsymbol\chi=
\begin{pmatrix}
\chi_{00}&\chi_{0{\rm AB}}\\
\chi_{0{\rm AB}}&\chi_{{\rm AB}{\rm AB}}
\end{pmatrix}
$$

とする。固有感受率は

$$
\boxed{
\chi_\pm
=\frac{\chi_{00}+\chi_{{\rm AB}{\rm AB}}}{2}
\pm
\sqrt{
\left(\frac{\chi_{00}-\chi_{{\rm AB}{\rm AB}}}{2}\right)^2
+\chi_{0{\rm AB}}^2
}
}
$$

である。固有vectorを一様 mode から角度 $\theta$ だけ回転したものとすると、

$$
\boxed{
\tan(2\theta)
=\frac{2\chi_{0{\rm AB}}}
{\chi_{00}-\chi_{{\rm AB}{\rm AB}}}
=\frac{
\sinh(\mathcal A-\mathcal B)
}{e^{\mathcal A+\mathcal B}\sinh(2\mathcal K)}
}
$$

となる。

この式から、mode mixing を制御するものが明確になる。

- $J_{AA}=J_{BB}$ では $\theta=0$ で、一様 mode と周期4 mode は分離する。
- $J_{AA}-J_{BB}$ を増やすと $|\theta|$ が大きくなり、固有応答が混合する。
- $J_{AB}$ が大きいと一方の channel が明確に優勢になり、相対的な混合角は小さくなる。
- $J_{AB}=0$ では二つの bare channel の対角感受率が等しくなり、非対称性があれば固有modeは最大限に混ざる。

## 10. 応答構造マップとして整理する

1次元有限範囲 Ising 鎖には有限温度の熱力学的相転移はない。したがって以下を相図と呼ぶのではなく、**ゼロ外場線形応答の構造マップ**として読む。

$\bar J\equiv(J_{AA}+J_{BB})/2>0$ と $\delta J\equiv(J_{AA}-J_{BB})/2$ を用いる。二つの厳密な境界は

$$
\boxed{
\delta J=0
\quad\Longleftrightarrow\quad
\chi_{0{\rm AB}}=0
}
$$

および

$$
\boxed{
J_{AB}=0
\quad\Longleftrightarrow\quad
\chi_{00}=\chi_{{\rm AB}{\rm AB}}
}
$$

である。

また

$$
\chi_{00}-\chi_{{\rm AB}{\rm AB}}
\propto\sinh(2\beta J_{AB})
$$

なので、$J_{AB}>0$ では一様成分が優勢、$J_{AB}<0$ では周期4成分が優勢になる。一方、$\delta J\neq0$ なら両側で mode mixing が存在する。

![AABB周期外場系の応答構造マップ](/figures/ising-r1-periodic-field/response-structure-map.svg)

*横軸は $J_{AB}/\bar J$、縦軸は $\delta J/\bar J$。$\delta J=0$ は一様・周期4 channel の厳密な decoupling line、$J_{AB}=0$ は二つの対角感受率が等しくなる line である。有限温度相転移ではなく、どの response channel が優勢で、どの程度混ざるかを分類した構造マップである。*

この図の四象限は異なる熱力学相ではない。右半面では一様成分を多く含む固有応答が強く、左半面では周期4成分を多く含む固有応答が強い。上下は $J_{AA}-J_{BB}$ の符号によって混合の向きが反転する。

高温ではすべての感受率が $O(\beta)$ へ小さくなるため、領域間の差は量的には消えていく。一方、低温では bond の符号構造と非対称性が強く反映され、この response map の違いが明瞭になる。

## 11. 外場があっても長距離相関は一周期行列の固有値比で決まる

外場があると $\langle s_i\rangle$ が一般に非ゼロなので、連結相関

$$
C_{ij}^{\rm conn}
=\langle s_i s_j\rangle
-\langle s_i\rangle\langle s_j\rangle
$$

を見る。一周期転送行列の二つの固有値を $\Lambda_+$ と $\Lambda_-$ とすれば、長距離では

$$
C^{\rm conn}(mp)
\sim
\left(\frac{\Lambda_-}{\Lambda_+}\right)^m
$$

であり、サイト単位の相関長は

$$
\boxed{
\xi=-\frac{p}{\ln|\Lambda_-/\Lambda_+|}
}
$$

となる。外場を入れると外場ゼロの単純な bond 積表示は失われるが、一周期行列の固有値比が長距離情報を運ぶという構造は変わらない。

## 12. bond周期とfield周期が違う場合

bond の周期を $p_J$、外場の周期を $p_h$ とする。両者が有限整数周期なら、全 Hamiltonian の周期は通常

$$
\boxed{
p=\operatorname{lcm}(p_J,p_h)
}
$$

である。その共通単位胞に対する $\mathcal T_p$ を作れば同じ方法で解ける。外場波数が bond の reciprocal vector と一致すれば構造モードへ直接結合し、一致しなければより大きな supercell の中で複数モードが混ざる。有限単位胞を失うと quasiperiodic 問題へ移る。

## 13. 一様 $R=2$ との違い

一様 $R=2$ では相互作用競合そのものが応答しやすい有限波数を選ぶ。一方、周期的不均一 $R=1$ では Hamiltonian の単位胞が先に reciprocal mode を与え、外場はその structure-imposed mode を選択的に励起する。

| | 周期的不均一 $R=1$ + 周期外場 | 一様 $R=2$ |
| --- | --- | --- |
| 波数基底 | 単位胞が与える | 相互作用競合から選ばれる |
| 転送状態数 | 2 | 4 |
| 外場の役割 | 構造モードを選択的に励起 | interaction-selected mode を probe |
| 非対称性の効果 | response channel の混合 | competing wavelength の再編成 |

![周期R1と一様R2の外場応答](/figures/ising-r1-periodic-field/periodic-r1-vs-r2-field.svg)

*周期 $R=1$ では bond 構造が波数基底を先に与える。一様 $R=2$ では相互作用競合が優勢波数を作る。*

## 14. まとめ

周期外場を加えると、外場ゼロの periodic $R=1$ にあった可換性と局所的ドメイン壁表示は失われる。しかし相互作用範囲は $R=1$ のままなので、一周期転送行列は依然として $2\times2$ であり、有限周期なら厳密解が得られる。

対称 $AABB$ 模型では一様 mode と周期4 mode がゼロ外場線形応答で分離し、$J_{AB}$ の符号がどちらの channel を増幅するかを決める。さらに $J_{AA}\neq J_{BB}$ とすると

$$
\boxed{
\chi_{0{\rm AB}}
=\beta\frac{\sinh[\beta(J_{AA}-J_{BB})]}{\mathcal S}
}
$$

が立ち上がり、一様 mode と周期4 mode が線形 order から混ざる。

したがってこの模型は

$$
\boxed{
\text{periodic structure}
\longrightarrow
\text{mode-selective response}
\longrightarrow
\text{symmetry-breaking-induced mode mixing}
}
$$

という流れを解析的に追える最小の例として読むことができる。最後の応答構造マップは熱力学相図ではないが、どの外場 channel が優勢か、どこで channel が分離し、どこで混ざるかを一枚にまとめている。

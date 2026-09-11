---
title: "1次元イジング模型 R=1 — 周期的不均一性と周期外場"
summary: "周期的最近接結合を持つ1次元Ising鎖へ周期外場を加える。外場による転送行列の非可換化、一周期転送行列による厳密解、AABB鎖の一様・周期磁化と感受率を解析し、構造モードと外場モードの結合を見る。"
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

を考える。

外場を加えても相互作用範囲は $R=1$ のままである。それでも、外場ゼロで成立していた単純さの一部は失われる。特に、転送行列は一般に非可換になり、単位胞内部の順序そのものが熱力学へ現れる。

一方で、転送状態は依然として1スピンだけで閉じるため、有限周期である限り問題は $2\times2$ の一周期転送行列へ還元できる。このノートでは一般周期 $p$ の構造を整理した後、前のノートと同じ $AABB$ 鎖について一様外場と周期外場を同時に入れ、磁化と感受率まで解析的に求める。

![周期bondと周期外場](/figures/ising-r1-periodic-field/overview-periodic-field.svg)

*周期的 bond に周期外場を重ねる。相互作用距離は増えていないが、bond の単位胞と field の単位胞が同時に現れ、その相対配置が物理量に効くようになる。*

## 1. 外場はドメイン壁表示を非局所化する

外場ゼロでは $\tau_i=s_i s_{i+1}$ によって

$$
H_0=-\sum_i J_i\tau_i
$$

となり、異なる bond 変数は直接結合しなかった。

しかし基準スピン $s_1$ を残すと

$$
s_i=s_1\prod_{k=1}^{i-1}\tau_k
$$

なので、外場項は

$$
-\sum_i h_i s_i
=-s_1\sum_i h_i\prod_{k=1}^{i-1}\tau_k
$$

となる。外場はスピンの絶対的な向きを見るため、ドメイン壁表示では長い積として非局所的に現れる。

したがって、外場ゼロでは

$$
\text{interacting spins}
\longrightarrow
\text{independent bond variables}
$$

という読み替えが有効だったのに対し、外場を含む問題ではスピン表示と転送行列へ戻る方が自然である。

## 2. 外場を入れると転送行列は一般に非可換になる

外場を bond の両端へ半分ずつ割り振り、

$$
T_i(s_i,s_{i+1})
=\exp\left[
\beta J_i s_i s_{i+1}
+\frac{\beta}{2}
\left(h_i s_i+h_{i+1}s_{i+1}\right)
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

である。

$h_i=0$ では各 $T_i$ は $I$ と $\sigma_x$ の線形結合だったので、すべて同じ固有基底を持った。外場があると $\sigma_z$ 成分も入り、一般には $[T_i,T_j]\neq0$ となる。

![外場による非可換化](/figures/ising-r1-periodic-field/noncommuting-transfer.svg)

*外場ゼロでは各 bond 転送行列の固有軸が共通だが、位置依存外場を加えると内部空間での向きが変わる。行列積の順序を入れ替えられなくなり、単位胞内部の配置が熱力学にも残る。*

## 3. 非可換でも一周期行列は $2\times2$ のままである

一周期の転送行列を

$$
\boxed{
\mathcal T_p=T_1T_2\cdots T_p
}
$$

とする。相互作用範囲は $R=1$ なので、非可換になっても転送状態の次元は増えない。

$\mathcal T_p$ の固有値は

$$
\boxed{
\Lambda_\pm
=\frac{
\operatorname{Tr}\mathcal T_p
\pm
\sqrt{(\operatorname{Tr}\mathcal T_p)^2-4\det\mathcal T_p}
}{2}
}
$$

である。各 bond 行列の行列式は

$$
\det T_i=2\sinh(2\beta J_i)
$$

なので、

$$
\boxed{
\det\mathcal T_p
=\prod_{\ell=1}^{p}2\sinh(2\beta J_\ell)
}
$$

となり、外場には依存しない。

熱力学極限では最大固有値 $\Lambda_+$ が支配し、1サイトあたり自由エネルギーは

$$
\boxed{
f=-\frac{1}{\beta p}\ln\Lambda_+
}
$$

である。したがって周期外場によって可換性は失われても、有限周期なら厳密解そのものは失われない。

## 4. 一つの磁化ではなく単位胞内磁化を考える

周期 $p$ の単位胞内サイトを $\alpha=1,\ldots,p$ とする。各サイトへ独立な外場 $h_\alpha$ を与えれば、対応する磁化は

$$
\boxed{
m_\alpha
=-p\frac{\partial f}{\partial h_\alpha}
=\frac{1}{\beta}
\frac{\partial\ln\Lambda_+}{\partial h_\alpha}
}
$$

である。ここで $m_\alpha$ は sublattice $\alpha$ 上の1サイトあたり磁化である。

一様系では磁化は一つの数で十分だったが、周期系では $(m_1,\ldots,m_p)$ が自然な変数になる。単位胞内の離散 Fourier 変換を使えば、これを一様成分と有限波数成分へ分けられる。

一周期の reciprocal wavevector は $G_n=2\pi n/p$ なので、外場も

$$
h_\alpha
=\sum_{n=0}^{p-1}\widetilde h_n e^{iG_n\alpha}
$$

と展開できる。一様外場は $G_0=0$ だけを持ち、周期外場は $G_n\neq0$ の構造モードへ直接結合する。

![周期外場とFourierモード](/figures/ising-r1-periodic-field/field-fourier-coupling.svg)

*単位胞内の外場パターンは離散 Fourier モードへ分解できる。一様成分は $G=0$ へ、周期成分は有限 $G$ の磁化へ結合する。*

## 5. $AABB$ 鎖では一様モードと周期4モードを分離できる

前のノートと同じ対称 $AABB$ 模型

$$
J_{AA}=J_{BB}=J,
\qquad
J_{AB}=K
$$

を考える。一周期の bond は $J,K,J,K$ である。

外場は

$$
(h_1,h_2,h_3,h_4)
=(h_A,h_A,h_B,h_B)
$$

とする。平均外場と A/B 差外場を

$$
h_0\equiv\frac{h_A+h_B}{2},
\qquad
h_{\rm AB}\equiv\frac{h_A-h_B}{2}
$$

と定義すると、

$$
(h_1,h_2,h_3,h_4)
=h_0(1,1,1,1)
+h_{\rm AB}(1,1,-1,-1)
$$

である。

前者は $q=0$ の一様外場であり、後者は周期4の外場である。$(1,1,-1,-1)$ は $q=\pm\pi/2$ 成分の実線形結合なので、$h_{\rm AB}$ は AABB 単位胞の基本波数へ直接結合する。

対応する磁化を

$$
m_0\equiv\frac14(m_1+m_2+m_3+m_4),
$$

$$
\boxed{
m_{\rm AB}
\equiv\frac14(m_1+m_2-m_3-m_4)
}
$$

とする。$m_0$ は全体磁化、$m_{\rm AB}$ は周期4の磁化成分である。

![AABBの外場モード](/figures/ising-r1-periodic-field/aabb-field-modes.svg)

*$h_0$ は全サイトを同方向へ押し、$h_{\rm AB}$ は $AA$ と $BB$ を逆向きへ押す。後者は $AABB$ 構造の $q=\pi/2$ モードに直接対応する。*

## 6. $AABB$ の一周期転送行列は二つの外場変数で閉じる

以下では無次元量

$$
\mathcal J\equiv\beta J,
\qquad
\mathcal K\equiv\beta K,
\qquad
u\equiv\beta h_0,
\qquad
d\equiv\beta h_{\rm AB}
$$

を用いる。

一周期転送行列は

$$
\mathcal T_4
=T(J,h_A,h_A)
T(K,h_A,h_B)
T(J,h_B,h_B)
T(K,h_B,h_A)
$$

である。行列要素をすべて展開するより、固有値を決める trace と determinant を見る方が構造が明瞭になる。

trace は

$$
\boxed{
\begin{aligned}
\Theta(\nu,d)
\equiv\operatorname{Tr}\mathcal T_4
={}&4e^{-2\mathcal J}\cosh(2\mathcal K)\\
&+2e^{2\mathcal J+2\mathcal K}\cosh(4\nu)\\
&+2e^{2\mathcal J-2\mathcal K}\cosh(4d)\\
&+8\cosh(2\nu)\cosh(2d)
\end{aligned}
}
$$

となる。一方、determinant は

$$
\boxed{
D\equiv\det\mathcal T_4
=16\sinh^2(2\mathcal J)\sinh^2(2\mathcal K)
}
$$

であり、外場に依存しない。

したがって

$$
\Delta(\nu,d)
\equiv\sqrt{\Theta(\nu,d)^2-4D}
$$

と置けば、

$$
\boxed{
\Lambda_+(\nu,d)
=\frac{\Theta(\nu,d)+\Delta(\nu,d)}{2}
}
$$

だけで熱力学が決まる。

この形から、一様外場 $\nu$ と周期外場 $d$ が同じ式の中に入りながら、異なる指数因子 $e^{2\mathcal J\pm2\mathcal K}$ を伴うことが分かる。

## 7. 一様磁化と周期磁化も閉形式で得られる

自由エネルギーは

$$
f=-\frac{1}{4\beta}\ln\Lambda_+
$$

なので、

$$
m_0=\frac14\frac{\partial\ln\Lambda_+}{\partial\nu},
\qquad
m_{\rm AB}=\frac14\frac{\partial\ln\Lambda_+}{\partial d}
$$

である。$D$ が外場に依存しないため、$\partial\ln\Lambda_+/\partial\Theta=1/\Delta$ が使える。

その結果、

$$
\boxed{
m_0
=\frac{
2e^{2\mathcal J+2\mathcal K}\sinh(4\nu)
+4\sinh(2\nu)\cosh(2d)
}{\Delta(\nu,d)}
}
$$

および

$$
\boxed{
m_{\rm AB}
=\frac{
2e^{2\mathcal J-2\mathcal K}\sinh(4d)
+4\cosh(2\nu)\sinh(2d)
}{\Delta(\nu,d)}
}
$$

を得る。

外場ゼロでは両方ともゼロであり、有限温度で自発磁化は生じない。ただし応答係数は一様 channel と周期 channel で大きく異なりうる。

## 8. ゼロ外場の感受率は特に単純になる

線形応答を

$$
\begin{pmatrix}
\delta m_0\\
\delta m_{\rm AB}
\end{pmatrix}
=
\begin{pmatrix}
\chi_{00}&\chi_{0{\rm AB}}\\
\chi_{{\rm AB}0}&\chi_{{\rm AB}{\rm AB}}
\end{pmatrix}
\begin{pmatrix}
\delta h_0\\
\delta h_{\rm AB}
\end{pmatrix}
$$

と定義する。

$\nu=d=0$ では

$$
\Theta_0=8\left[1+\cosh(2\mathcal J)\cosh(2\mathcal K)\right]
$$

かつ

$$
\boxed{
\Delta_0
=8\left[\cosh(2\mathcal J)+\cosh(2\mathcal K)\right]
}
$$

となる。これを二階微分へ代入すると、感受率は

$$
\boxed{
\chi_{00}
=\beta\frac{e^{\mathcal J+\mathcal K}}
{\cosh(\mathcal J-\mathcal K)}
}
$$

および

$$
\boxed{
\chi_{{\rm AB}{\rm AB}}
=\beta\frac{e^{\mathcal J-\mathcal K}}
{\cosh(\mathcal J+\mathcal K)}
}
$$

となる。

さらに対称模型 $J_{AA}=J_{BB}$ では $\Theta(\nu,d)$ が $\nu$ と $d$ のそれぞれについて偶関数なので、ゼロ外場で

$$
\boxed{
\chi_{0{\rm AB}}
=\chi_{{\rm AB}0}=0
}
$$

である。

これは重要である。周期的不均一性があれば常に線形 order で一様モードと周期モードが混ざるわけではない。対称 $AABB$ 模型では、ゼロ外場まわりの線形応答は二つの channel に分離する。

mode mixing は有限外場での非線形応答には現れうる。また $J_{AA}\neq J_{BB}$ や $h_{A_1}\neq h_{A_2}$ のように単位胞内対称性をさらに壊せば、ゼロ外場の混合感受率も一般に非ゼロになりうる。

## 9. 結合の符号がどちらの外場channelを増幅するかを決める

二つの感受率を比べると物理像が明瞭になる。

$J=K>0$ の一様強磁性鎖では

$$
\chi_{00}=\beta e^{2\mathcal J},
\qquad
\chi_{{\rm AB}{\rm AB}}=\frac{\beta}{\cosh(2\mathcal J)}.
$$

つまり低温ほど $q=0$ の一様 channel が強くなる。

一方、$K=-J$ なら

$$
\chi_{00}=\frac{\beta}{\cosh(2\mathcal J)},
\qquad
\chi_{{\rm AB}{\rm AB}}=\beta e^{2\mathcal J}.
$$

今度は関係が完全に入れ替わり、周期4の $q=\pi/2$ channel が強くなる。

これは低温基底状態が $++--++--\cdots$ になることと整合する。周期 bond 構造に適合した外場モードほど大きな応答を引き出す。

![一様・周期感受率の温度依存](/figures/ising-r1-periodic-field/susceptibility-channels.svg)

*対称 $AABB$ 鎖のゼロ外場感受率。$K>0$ では一様 channel、$K<0$ では周期4 channel が増幅される。有限波数応答は外場が新たな周期を作るのではなく、bond 構造がすでに持つモードを選択的に probe している。*

より一般には

$$
\frac{\chi_{{\rm AB}{\rm AB}}}{\chi_{00}}
=e^{-2\mathcal K}
\frac{\cosh(\mathcal J-\mathcal K)}
{\cosh(\mathcal J+\mathcal K)}
$$

なので、$K$ の符号と強さがどちらの channel が優勢かを連続的に制御する。

## 10. 一様鎖の $\chi(q)$ と整合する

$K=J$ とすると bond の周期性は消え、一様 $R=1$ 鎖へ戻る。このとき $h_{\rm AB}$ のパターン $(1,1,-1,-1)$ は $q=\pi/2$ 成分である。

一様鎖の波数依存感受率は、$t=\tanh\mathcal J$ として

$$
\chi(q)
=\beta\frac{1-t^2}{1-2t\cos q+t^2}
$$

だった。$q=0$ と $q=\pi/2$ を代入すると

$$
\chi(0)=\beta e^{2\mathcal J},
\qquad
\chi\left(\frac{\pi}{2}\right)
=\frac{\beta}{\cosh(2\mathcal J)},
$$

となり、上の $\chi_{00}$ と $\chi_{{\rm AB}{\rm AB}}$ に一致する。

したがって単位胞内の感受率 channel は、一様極限では通常の $\chi(q)$ の特定波数を抽出したものとして解釈できる。

## 11. 外場があっても長距離相関は一周期行列の固有値比で決まる

外場があると $\langle s_i\rangle$ が一般に非ゼロなので、二点量としては連結相関

$$
C_{ij}^{\rm conn}
=\langle s_i s_j\rangle
-\langle s_i\rangle\langle s_j\rangle
$$

を見る。

一周期転送行列の二つの固有値を $\Lambda_+$ と $\Lambda_-$ とすれば、セル間距離 $m$ が大きいとき

$$
C^{\rm conn}(mp)
\sim
\left(\frac{\Lambda_-}{\Lambda_+}\right)^m
$$

である。したがってサイト単位の相関長は

$$
\boxed{
\xi
=-\frac{p}{\ln|\Lambda_-/\Lambda_+|}
}
$$

となる。

外場ゼロでは $\Lambda_-/\Lambda_+$ が各 bond の $\tanh(\beta J_i)$ の積へ分解したが、外場を入れるとその単純な積構造は失われる。それでも「一周期転送行列の固有値比が長距離情報を運ぶ」という transfer-matrix の基本構造は保たれる。

## 12. bond周期とfield周期が違う場合は共通単位胞を取ればよい

bond の周期を $p_J$、外場の周期を $p_h$ とする。両者が可換な整数周期なら、全 Hamiltonian の周期は通常

$$
\boxed{
p=\operatorname{lcm}(p_J,p_h)
}
$$

である。

したがって、その共通単位胞に対する $\mathcal T_p$ を作れば同じ方法で解ける。外場波数が bond の reciprocal vector と一致すれば構造モードへ直接結合し、一致しなければより大きな supercell の中で複数モードが混ざる。

有限周期の範囲ではこの問題も依然として解析的 transfer matrix の枠内にある。一方、外場波数が格子と非整合になり有限単位胞を持たなくなると、quasiperiodic 問題へ移る。

## 13. 周期的不均一 $R=1$ と一様 $R=2$ では外場の意味も違う

一様 $R=2$ では、相互作用競合そのものが応答しやすい有限波数を選ぶ。外場はその interaction-selected mode を probe する。

周期的不均一 $R=1$ では、Hamiltonian の単位胞が先に reciprocal mode を与える。周期外場は、その structure-imposed mode の一つへ直接結合する。

したがって両者は

| | 周期的不均一 $R=1$ + 周期外場 | 一様 $R=2$ |
| --- | --- | --- |
| 波数基底 | 単位胞が与える | 並進対称な相互作用から選ばれる |
| 転送状態数 | 2 | 4 |
| 外場の役割 | 構造モードを選択的に励起 | interaction-selected mode を probe |
| 主な構造 | mode-selective response | competing wavelengths |

と整理できる。

![周期R1と一様R2の外場応答](/figures/ising-r1-periodic-field/periodic-r1-vs-r2-field.svg)

*周期 $R=1$ では bond 構造が波数基底を先に与え、外場はその channel を選ぶ。一様 $R=2$ では相互作用競合が優勢波数を作り、外場はその応答を観測する。*

## 14. 外場を入れて何が変わり、何が残ったか

外場を加えることで、外場ゼロの periodic $R=1$ にあった三つの単純さのうち二つが失われた。

まず、転送行列は一般に非可換になり、単位胞内部の順序が自由エネルギーにも現れる。次に、ドメイン壁表示は外場項によって非局所化する。

一方、相互作用範囲は $R=1$ のままなので転送行列は $2\times2$ のままであり、有限周期なら一周期行列を対角化するだけで厳密解が得られる。

対称 $AABB$ 模型ではさらに、一様外場 $h_0$ と周期4外場 $h_{\rm AB}$ を導入することで、磁化と感受率を二つの response channel に分けられた。ゼロ外場では

$$
\boxed{
\chi_{00}
=\beta\frac{e^{\mathcal J+\mathcal K}}
{\cosh(\mathcal J-\mathcal K)},
\qquad
\chi_{{\rm AB}{\rm AB}}
=\beta\frac{e^{\mathcal J-\mathcal K}}
{\cosh(\mathcal J+\mathcal K)},
\qquad
\chi_{0{\rm AB}}=0
}
$$

という特に単純な結果になる。

この式は、周期 bond が「どの外場波数へ強く応答するか」を直接表している。$K>0$ なら一様 mode、$K<0$ なら周期4 mode が強調され、$K=-J$ では $++--$ 構造に共役な $q=\pi/2$ 応答が低温で指数的に増大する。

したがってこの模型は

$$
\boxed{
\text{periodic structure}
\longrightarrow
\text{periodic response channels}
\longrightarrow
\text{mode-selective field coupling}
}
$$

を解析的に追える最小の例として見ることができる。

次に外場波数を単位胞の reciprocal vector から連続的にずらせば、有限周期の問題から spatially oscillating field、さらに quasiperiodic modulation へ進むことができる。

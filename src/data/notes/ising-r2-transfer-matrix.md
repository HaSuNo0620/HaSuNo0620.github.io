---
title: "第二近接Ising鎖の振動相関と感受率ピーク"
summary: "競合相互作用を持つIsing鎖の転送行列を対角化し、相関の複素化と感受率ピークの分岐を区別する。"
publishedAt: 2026-09-11T02:10:00+09:00
updatedAt: 2026-11-28
area: "Physics"
field: statistical-physics
kind: model
prerequisites: ["finite-range-symmetry-comparison", "ising-transfer-matrix"]
related: ["clock-chain-second-neighbor", "xy-chain-second-neighbor"]
topics: ["statistical mechanics", "Ising model", "transfer matrix", "correlation", "frustration", "information thermodynamics"]
status: growing
system:
  dimension: 1
  spatial: uniform
  range: R2
  interaction: cosine
  symmetry: [Z2]
  mechanics: classical
  role: model
---

第二近接相互作用を持つIsing鎖では、長距離相関が振動し始める条件と、静的感受率が有限波数で最大になる条件が異なる。有限温度におけるこの二つの境界を、転送行列から求める。

## 競合相互作用とドメイン壁

零外場で

$$
H=-J_1\sum_i s_i s_{i+1}-J_2\sum_i s_i s_{i+2},\qquad s_i=\pm1
$$

とする。$J_1>0$、$J_2=-\kappa J_1$、$\kappa\ge0$ とし、$K_i=\beta J_i$、$t=k_{\mathrm B}T/J_1$ と書く。

![最近接と第二近接の比較](/figures/ising-r2/overview-r1-r2.svg)

結合変数 $\tau_i=s_i s_{i+1}$ を用いると

$$
H=-J_1\sum_i\tau_i-J_2\sum_i\tau_i\tau_{i+1}.
$$

最近接鎖で独立だったドメイン壁が相互作用する。有限周期鎖では $\prod_i\tau_i=1$ の制約がある。以下の相関は熱力学極限で考える。

![スピン列とドメイン壁](/figures/ising-r2/domain-wall-map.svg)

![競合する相互作用](/figures/ising-r2/frustration-competition.svg)

基底状態のエネルギーは、隣接結合変数の対称な局所エネルギーを最小化すれば求まる。強磁性状態のエネルギー密度は $-J_1-J_2$、周期4状態 $++--$ では $J_2$ である。他の候補である反強磁性状態は $J_1-J_2$ なので、$\kappa=1/2$ で基底状態が切り替わる。この点では縮退があり、周期4状態と強磁性状態だけに限らない。

## 転送行列の対称性

スピン対 $(a,b)$ を転送状態にすると、

$$
T_{(a,b),(b',c)}=\delta_{b,b'}e^{K_1bc+K_2ac}.
$$

![転送状態ネットワーク](/figures/ising-r2/transfer-state-network.svg)

全スピン反転と可換するため、偶・奇の各二次元部分空間に分解できる。状態の順序を $(++),(+-),(-+),(--)$ とし、それぞれ反転で対応する状態を組に取ると、各ブロックは

$$
T_\pm=\begin{pmatrix}
e^{K_1+K_2}&e^{-K_1-K_2}\\
\pm e^{K_1-K_2}&\pm e^{-K_1+K_2}
\end{pmatrix}
$$

となる。偶ブロックの最大固有値は

$$
\lambda_0=e^{K_2}\cosh K_1+
\sqrt{e^{2K_2}\sinh^2 K_1+e^{-2K_2}}.
$$

自由エネルギー密度は $f=-\beta^{-1}\ln\lambda_0$ である。スピン演算子は反転に対して奇なので、二点スピン相関には奇ブロックの固有値

$$
\lambda_\pm^{(-)}=e^{K_2}\sinh K_1
\pm\sqrt{e^{2K_2}\cosh^2K_1-e^{-2K_2}}
$$

が寄与する。有限温度では最大固有値は単純であり、自由エネルギーに相転移に対応する非解析性は生じない。

## 長距離相関の振動

奇ブロックの判別式

$$
\Delta_-=e^{2K_2}\cosh^2K_1-e^{-2K_2}
$$

が負になると、固有値は複素共役対となる。

![固有値の複素化](/figures/ising-r2/spectrum-complexification.svg)

相関は $\rho^r[A\cos(q_{\rm spec}r)+B\sin(q_{\rm spec}r)]$ の形になり、

$$
\rho=|\lambda_+^{(-)}|/\lambda_0,\qquad
\xi^{-1}=-\ln\rho,
$$

$$
q_{\rm spec}=\arctan
\frac{\sqrt{e^{-2K_2}-e^{2K_2}\cosh^2K_1}}
{e^{K_2}\sinh K_1}.
$$

判別式がゼロになる条件から、Stephensonのdisorder lineは

$$
\kappa_{\rm d}(t)=\frac{t}{2}\ln\cosh(1/t)
$$

となる。

重根では一般に $(A+Br)\rho^r$ の形を許す。複素化直後の振動周期は発散するが、有限距離の相関は連続的に変化する。

## 相関の漸化式と構造因子

正規化固有値を $\mu_\pm=\lambda_\pm^{(-)}/\lambda_0$ とし、

$$
a=\mu_++\mu_-,\qquad b=\mu_+\mu_-
$$

と書く。Cayley–Hamiltonの定理から

$$
C(r+2)=aC(r+1)-bC(r),\qquad C(0)=1.
$$

初期値 $c=C(1)$ は $c=\partial_{K_1}\ln\lambda_0$（$K_2$ を固定）であり、$c=\sinh K_1/\sqrt{\sinh^2K_1+e^{-4K_2}}$ となる。

![三領域の実空間相関](/figures/ising-r2/three-regimes-correlation.svg)

生成関数は

$$
G(z)=\frac{1+(c-a)z}{1-az+bz^2}.
$$

格子間隔を1とし、構造因子を $S(Q)=\sum_{r\in\mathbb Z}C(r)e^{-iQr}$ と定義する。$x=\cos Q$ とすれば

$$
S(Q)=G(e^{iQ})+G(e^{-iQ})-1=\frac{N(x)}{D(x)},
$$

$$
\begin{aligned}
N(x)&=1-b^2-2a(c-a)-2a^2+2[c(1+b)-ab]x\\
&=1-b^2-2ac+2[c(1+b)-ab]x,\\
D(x)&=(1-b)^2+a^2-2a(1+b)x+4bx^2.
\end{aligned}
$$

従って最大位置は $N'D-ND'=0$ の実根のうち $[-1,1]$ に入るものと、両端点を比較して決定できる。

![実空間相関と波数応答](/figures/ising-r2/real-fourier-map.svg)

線形感受率は $\chi(Q)=\beta S(Q)$ なので、その最大波数 $q_\chi$ は相関の全距離の寄与から決まる。長距離を支配する固有値の偏角だけでは決まらない。

## 感受率ピークの分岐

$Q=0$ の極大が分岐する条件は $\partial_Q^2 S(0)=0$、すなわち $N'(1)D(1)-N(1)D'(1)=0$ である。上の係数を代入して整理すると

$$
(\sinh^4K_1-1)e^{8K_2}
+(\sinh^2K_1+2)e^{4K_2}-1=0.
$$

物理的な正根を取れば

$$
\kappa_{\rm L}(t)=\frac{t}{4}\ln
\frac{\sinh^2(1/t)+2+\sinh(1/t)\sqrt{5\sinh^2(1/t)+4}}{2}.
$$

これは有限温度の相転移線ではなく、応答ピークの分岐を表すLifshitz型の境界である。

![三領域の感受率](/figures/ising-r2/three-regimes-susceptibility.svg)

$t=1$ では $\kappa_{\rm d}\simeq0.2169$、$\kappa_{\rm L}\simeq0.3224$ となる。両境界の間では実空間相関が振動するにもかかわらず、感受率の最大は零波数に残る。

![相関構造マップ](/figures/ising-r2/correlation-structure-map.svg)

低温では二つの境界が $\kappa=1/2$ に近づき、その差は

$$
\kappa_{\rm L}-\kappa_{\rm d}\sim\frac{t}{4}\ln\frac{1+\sqrt5}{2}.
$$

高温では $\kappa_{\rm d}\to0$、$\kappa_{\rm L}\to1/4$ となる。これは相互作用比を一定にして高温展開した場合にも、$S(Q)$ の先頭補正が $2K_1\cos Q+2K_2\cos2Q$ になることから理解できる。

![相関波数の競合強度依存性](/figures/ising-r2/qstar-kappa.svg)

![相関長の競合強度依存性](/figures/ising-r2/correlation-length-kappa.svg)

## 外場応答と他の系との関係

位置依存外場 $-\sum_i h_i s_i$ に対して、$h_i=h_Q\cos(Qi+\varphi)$ なら

$$
\langle s_i\rangle=\chi(Q)h_Q\cos(Qi+\varphi)+O(h_Q^3)
$$

となる。$q_\chi$ は線形領域で同じ外場振幅に対する磁化振幅を最大にする波数である。

液体論のFisher–Widom線も、密度相関の長距離漸近形を支配する特異点が変わる現象である。ただし、一般の液体では実軸型の極と複素極の減衰率の競合によって支配極が交代しうる。ここでの二つの実固有値の合体と複素化とは同一の機構ではない。また液体の次元に応じて代数的な減衰因子も加わる。

![転送固有値と液体の相関極の比較](/figures/ising-r2/ising-liquid-correspondence.svg)

情報論的にはドメイン壁が相関した反転過程を構成する。零外場の二点同時確率は最近接鎖と同じく $[1+s_0s_rC(r)]/4$ なので、二点相互情報量は遠距離で $C(r)^2/2$ に近づく。ただし反転過程の多点統計は二点相関だけでは決まらない。

![相関した反転過程](/figures/ising-r2/information-channel.svg)

[第二近接XY鎖](/notes/xy-chain-second-neighbor/)では、角度の連続自由度とカイラリティ反転によっても相関波数と応答ピークの分離が生じる。

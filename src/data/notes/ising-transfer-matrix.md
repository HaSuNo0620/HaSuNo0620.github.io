---
title: "一次元最近接Ising鎖の厳密解と空間相関"
summary: "ドメイン壁の統計から二点相関を導き、転送行列による磁化、波数依存感受率、相互情報量との関係を調べる。"
publishedAt: 2025-05-27T21:25:00+09:00
updatedAt: 2026-11-28
area: "Physics"
field: statistical-physics
kind: model
prerequisites: ["finite-range-symmetry-comparison"]
related: ["ising-r2-transfer-matrix", "ising-r1-periodic", "clock-chain-nearest-neighbor"]
topics: ["statistical mechanics", "Ising model", "transfer matrix", "correlation", "linear response"]
status: growing
system:
  dimension: 1
  spatial: uniform
  range: R1
  interaction: cosine
  symmetry: [Z2]
  mechanics: classical
  role: model
---

一次元最近接Ising鎖では、零外場の二点相関を決める量が、隣接スピンの相関 $\tanh(\beta J)$ に限られる。この結果は転送行列からも、ドメイン壁の確率分布からも導ける。以下では両者の対応を示し、空間的に変化する外場への応答と相互情報量を求める。

## 零外場の分配関数

スピン $s_i=\pm1$ に対して

$$
H=-J\sum_i s_i s_{i+1}-\sum_i h_i s_i,\qquad
\beta=(k_{\mathrm B}T)^{-1},\quad K=\beta J
$$

と定義する。格子間隔は1とする。零外場の転送行列は

$$
T=\begin{pmatrix}e^K&e^{-K}\\e^{-K}&e^K\end{pmatrix}
$$

であり、対称・反対称な固有ベクトルに対応する固有値は $\lambda_+=2\cosh K$、$\lambda_-=2\sinh K$ である。周期鎖では $Z_N=\lambda_+^N+\lambda_-^N$、開鎖では $Z_N=2\lambda_+^{N-1}$ となる。有限温度の熱力学極限では、どちらの境界条件からも自由エネルギー密度 $f=-\beta^{-1}\ln\lambda_+$ を得る。

## ドメイン壁と二点相関

隣接スピンの積 $\tau_i=s_i s_{i+1}$ を導入する。開鎖では初期スピンと全ての $\tau_i$ を与えれば、

$$
s_i=s_1\prod_{j=1}^{i-1}\tau_j
$$

によって配置を一意に復元できる。零外場のエネルギーは $H=-J\sum_i\tau_i$ となり、各結合変数は独立である。周期鎖には $\prod_i\tau_i=1$ という制約があるため、有限サイズでは独立性は厳密には成立しない。以降は開鎖の内部または熱力学極限を考える。

強磁性結合 $J>0$ では $\tau_i=-1$ がドメイン壁であり、その励起エネルギーは $2J$ である。壁の存在確率は

$$
p_{\mathrm{dw}}=\frac{1}{1+e^{2K}},\qquad
\langle\tau_i\rangle=1-2p_{\mathrm{dw}}=\tanh K.
$$

距離 $r$ にわたる壁数を $N_{\mathrm{dw}}$ とすると $s_i s_{i+r}=(-1)^{N_{\mathrm{dw}}}$ である。独立な結合変数の平均を取ると

$$
C(r)=\langle s_i s_{i+r}\rangle
=(\tanh K)^{|r|}.
$$

転送行列の固有値比 $\lambda_-/\lambda_+$ は、この壁数の偶奇の平均を1結合について評価した量に等しい。

![距離に対する二点相関関数](/figures/ising-r1/correlation-distance.svg)

*強磁性鎖における二点相関の距離依存性。*

相関長は $\xi^{-1}=-\ln|\tanh K|$ である。反強磁性 $J<0$ では相関の符号が交互に変わるが、包絡の相関長は同じ式で求まる。$J=0$ では異なるサイトの相関はゼロである。

強磁性低温では $p_{\mathrm{dw}}\simeq e^{-2K}$ なので、

$$
\xi\simeq\frac{1}{2p_{\mathrm{dw}}}\simeq \frac12e^{2K}.
$$

平均壁間隔 $1/p_{\mathrm{dw}}$ と相関長の間に係数2が現れるのは、相関が壁の有無ではなく壁数の偶奇を測るためである。

![相関長の温度依存](/figures/ising-r1/correlation-length-temperature.svg)

*相関長の厳密式と強磁性低温での漸近形。*

## 一様外場における磁化

一様外場 $h$ を加えると、結合変数では外場項が $-hs_1\sum_i\prod_{j<i}\tau_j$ となる。独立性を失うので、絶対スピンを状態とする転送行列を用いる。外場エネルギーを両端に等分すれば

$$
T_h=\begin{pmatrix}e^{K+\beta h}&e^{-K}\\e^{-K}&e^{K-\beta h}\end{pmatrix},
$$

$$
\lambda_\pm=e^K\left[\cosh(\beta h)\pm
\sqrt{\sinh^2(\beta h)+e^{-4K}}\right].
$$

磁化は $m=-\partial f/\partial h$ から

$$
m(h)=\frac{\sinh(\beta h)}{\sqrt{\sinh^2(\beta h)+e^{-4K}}}
$$

となる。有限温度では $h\to0$ で磁化は消失する。一様感受率は

$$
\chi(0)=\left.\frac{\partial m}{\partial h}\right|_{h=0}
=\beta e^{2K}.
$$

![一様外場に対する磁化](/figures/ising-r1/magnetization-field.svg)

*一様外場下の磁化。低温の強磁性鎖では零外場付近の傾きが大きくなる。*

## 波数依存感受率

零外場の線形応答は $\chi_{ij}=\beta C(i-j)$ である。$t=\tanh K$ とおいて幾何級数を評価すると、

$$
\begin{aligned}
\chi(Q)&=\beta\sum_{r\in\mathbb Z}t^{|r|}e^{-iQr}\\
&=\beta\frac{1-t^2}{1-2t\cos Q+t^2}.
\end{aligned}
$$

$Q=0$ では先ほどの一様感受率を回収する。強磁性では $Q=0$、反強磁性では $Q=\pi$ で最大となり、$J=0$ では波数に依存しない。

![波数依存感受率](/figures/ising-r1/susceptibility-q.svg)

*強磁性鎖の波数依存感受率。*

強磁性で $\xi\gg1$、かつ $|Q|\ll1$ なら $t=e^{-1/\xi}$ を展開して

$$
\chi(Q)\simeq\frac{2\beta\xi}{1+(Q\xi)^2}
$$

を得る。外場の変化が相関長に比べて緩やかなら、相関した領域のスピンはほぼ同じ向きの外場を受ける。逆に $Q\xi$ が大きくなると、領域内で外場の符号が変化するため応答が相殺される。

外場 $h_i=h_Q\cos(Qi+\varphi)$ に対しては、スピン反転対称性により

$$
\langle s_i\rangle=\chi(Q)h_Q\cos(Qi+\varphi)+O(h_Q^3)
$$

となる。

![空間振動外場と磁化応答](/figures/ising-r1/spatial-field-response.svg)

*外場の空間変調に対する応答。既存図の条件は $\beta J=1.2$、$h_Q/J=0.05$。*

有限振幅では

$$
T_i(s,s')=\exp\left[Kss'+\frac{\beta}{2}(h_i s+h_{i+1}s')\right]
$$

を用いる。外場に整数周期 $L$ がある場合、一周期の積 $M=T_1\cdots T_L$ の最大固有値 $\Lambda_+$ から $f=-(\beta L)^{-1}\ln\Lambda_+$ を得る。非線形応答では奇数次の高調波が現れうる。格子上では波数を $2\pi$ を法として扱う必要がある。

## 二点相関と相互情報量

零外場の二点同時確率は

$$
P(s_0,s_r)=\frac14[1+s_0s_rC(r)]
$$

である。各スピンの周辺分布は一様なので、自然対数を用いた相互情報量は

$$
I(s_0:s_r)=\frac{1+C(r)}2\ln[1+C(r)]
+\frac{1-C(r)}2\ln[1-C(r)].
$$

ビット単位にするには $\ln2$ で割る。遠距離で $|C(r)|\ll1$ なら

$$
I(s_0:s_r)=\frac12 C(r)^2+O(C(r)^4).
$$

従って相互情報量の漸近減衰長は $\xi/2$ である。壁配置が全て分かれば一方のスピンから他方を完全に復元できるが、壁配置を観測しない場合には二点間の情報量が減少する。

測定とフィードバックを含む熱力学的操作では、相互情報量に由来する仕事の上限に $k_{\mathrm B}TI$ が現れる場合がある。ただし、仕事の収支には操作の条件や測定・記憶の扱いが関わる。平衡スピン鎖の相互情報量だけから利用可能な仕事を決めることはできない。

## 相互作用範囲を広げる場合

第二近接相互作用は結合変数の積 $\tau_i\tau_{i+1}$ となるので、独立な壁の模型ではなくなる。[第二近接Ising鎖](/notes/ising-r2-transfer-matrix/)では、その結果として振動相関と感受率ピークの分岐が生じる。一般の有限範囲における転送状態の構成は[共通理論](/notes/finite-range-symmetry-comparison/)で扱う。

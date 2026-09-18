---
title: "1次元一様最近接 cosine-Z2 スピン系 — 空間記憶と応答"
summary: "最近接相互作用だけを持つ1次元Ising鎖を、有限相互作用範囲系列の基準点として読む。転送行列、ドメイン壁、相関長、一様外場、波数依存感受率、空間振動外場への応答を同じ構造としてつなぐ。"
publishedAt: 2025-05-27T21:25:00+09:00
updatedAt: 2026-09-19
area: "Physics"
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

1次元 Ising 模型は「厳密に解ける簡単な模型」というだけでなく、相互作用範囲を伸ばしたときに何が新しく生まれるかを見る基準点として使いやすい。

有限範囲 $R$ の模型を

$$
H_R=-\sum_i\sum_{r=1}^{R}J_r s_i s_{i+r}-\sum_i h_i s_i,
\qquad s_i=\pm1
$$

と書くと、最近接模型は

$$
\boxed{
H=-J\sum_i s_i s_{i+1}-\sum_i h_i s_i
}
$$

である。以下では

$$
\beta\equiv\frac{1}{k_{\mathrm B}T},
\qquad
K\equiv\beta J=\frac{J}{k_{\mathrm B}T}
$$

とする。

この模型で特別なのは、零外場なら「局所記憶」「欠陥」「相関」「波数応答」がすべて一つの量へ還元されることである。

## 系の座標

$$
\boxed{
(d=1,\ \text{uniform},\ R=1,\ \text{cosine},\ Z_2)
}
$$

基準 Hamiltonian は

$$
H=-J\sum_i s_i s_{i+1},
\qquad s_i=\pm1,
$$

局所 memory variable は

$$
\tau_i=s_i s_{i+1}.
$$

この座標では $\tau_i$ が独立になることが、長距離記憶と応答の基準点になる。


$Z_2$ では $\theta_i\in\{0,\pi\}$ と置けば

$$
\cos(\theta_i-\theta_j)=s_i s_j
$$

なので、標準 bilinear Ising 相互作用と cosine-$Z_2$ 表現は同値である。

## 1. 局所記憶は1スピンで閉じる

零外場では

$$
H=-J\sum_{i=1}^{N-1}s_i s_{i+1}.
$$

最後のスピンを固定した部分分配関数を使えば

$$
\begin{pmatrix}
Z_N^{(+)}\\
Z_N^{(-)}
\end{pmatrix}
=
\begin{pmatrix}
e^K&e^{-K}\\
e^{-K}&e^K
\end{pmatrix}
\begin{pmatrix}
Z_{N-1}^{(+)}\\
Z_{N-1}^{(-)}
\end{pmatrix}.
$$

新しいスピンを加えるとき必要なのは直前の1スピンだけで、転送行列は $2\times2$ で閉じる。

固有値は

$$
\lambda_+=2\cosh K,
\qquad
\lambda_-=2\sinh K,
$$

したがって非自明な固有値比は

$$
\boxed{
\frac{\lambda_-}{\lambda_+}=\tanh K
}
$$

だけである。この比が空間記憶の1-step retentionになる。

## 2. ドメイン壁表示では相互作用が消える

bond変数

$$
\tau_i\equiv s_i s_{i+1}=\pm1
$$

を導入すると、$\tau_i=-1$ がdomain wallに対応する。

基準スピン $s_1$ を残せば

$$
\boxed{
s_i=s_1\prod_{k=1}^{i-1}\tau_k
}
$$

なので、開鎖では

$$
\{s_i\}
\longleftrightarrow
\left(s_1,\{\tau_i\}\right)
$$

は情報を失わない変数変換である。

零外場の Hamiltonian は

$$
\boxed{
H=-J\sum_i\tau_i
}
$$

となり、異なる $\tau_i$ 同士の結合が消える。

$$
\boxed{
\text{interacting spins}
\longrightarrow
\text{independent domain-wall variables}
}
$$

という単純化が最近接鎖の核心である。

強磁性 $J>0$ では壁1個の生成コストは $2J$ なので

$$
p_{\mathrm{dw}}
=\frac{1}{1+e^{2K}}
\simeq e^{-2K}
\qquad(K\gg1).
$$

また

$$
\langle\tau\rangle
=1-2p_{\mathrm{dw}}
=\tanh K,
$$

したがって

$$
\boxed{
\frac{\lambda_-}{\lambda_+}
=\langle\tau\rangle
=1-2p_{\mathrm{dw}}
=\tanh K
}
$$

となる。transfer spectrum と実空間の欠陥密度が同じ量を見ている。

外場項は

$$
-h\sum_i s_i
=-hs_1\sum_i\prod_{k=1}^{i-1}\tau_k
$$

となるので、wall表示は外場に対しては非局所的になる。表示の良し悪しではなく、**何を局所化する変数なのか**が違う。

## 3. 相関は壁数の偶奇を読む

二点間では

$$
s_i s_{i+r}
=\prod_{j=i}^{i+r-1}\tau_j
=(-1)^{N_{\mathrm{wall}}(i,i+r)}.
$$

相関関数は壁の本数そのものではなく、その偶奇を見ている。

$\tau_i$ が独立なので

$$
\boxed{
C(r)
\equiv\langle s_i s_{i+r}\rangle
=(\tanh K)^r
=\left(\frac{\lambda_-}{\lambda_+}\right)^r
}
$$

となる。

![距離に対する二点相関関数](/figures/ising-r1/correlation-distance.svg)

*最近接強磁性鎖の二点相関。非自明な減衰モードは一つだけで、相関は単一指数になる。*

$C(r)=e^{-r/\xi}$ と書けば

$$
\boxed{
\xi^{-1}
=-\ln|\tanh K|
=\ln\left|\frac{\lambda_+}{\lambda_-}\right|
}
$$

であり、低温では

$$
\boxed{
\xi\simeq\frac12e^{2K}
=\frac12\exp\left(\frac{2J}{k_{\mathrm B}T}\right)
}
$$

となる。

![相関長の温度依存](/figures/ising-r1/correlation-length-temperature.svg)

*相関長の厳密式と低温漸近形。$T\to0$ では急速に増大するが、任意の有限温度では有限である。*

低温では平均壁間隔 $\ell_{\mathrm{wall}}\simeq p_{\mathrm{dw}}^{-1}$ なので

$$
\boxed{
\ell_{\mathrm{wall}}\simeq2\xi
}
$$

となる。係数2は、相関が最初の壁ではなく $(-1)^{N_{\mathrm{wall}}}$ を測ることから出る。

## 4. 一様外場は $q=0$ 応答として位置づけられる

一様外場では

$$
H=-J\sum_i s_i s_{i+1}-h\sum_i s_i
$$

で、split-field transfer matrix は

$$
T=
\begin{pmatrix}
e^{K+\beta h}&e^{-K}\\
e^{-K}&e^{K-\beta h}
\end{pmatrix}.
$$

固有値は

$$
\lambda_\pm
=e^K\left[
\cosh(\beta h)
\pm\sqrt{\sinh^2(\beta h)+e^{-4K}}
\right].
$$

熱力学極限で

$$
\boxed{
m(h)
=\frac{\sinh(\beta h)}
{\sqrt{\sinh^2(\beta h)+e^{-4K}}}
}
$$

となる。

![一様外場に対する磁化](/figures/ising-r1/magnetization-field.svg)

*低温ほど $h=0$ 近傍の応答は急になるが、有限温度では自発磁化は生じない。*

零外場感受率は

$$
\boxed{
\chi(0)=\beta e^{2K}
}
$$

である。これは後で波数依存感受率の $q=0$ 成分として回収できる。

## 5. 実空間相関はそのまま波数フィルタになる

微小な位置依存外場に対して

$$
\delta\langle s_i\rangle
=\sum_j\chi_{ij}\delta h_j,
$$

零外場では

$$
\chi_{ij}=\beta C(i-j).
$$

$t\equiv\tanh K$ とおけば

$$
\boxed{
\chi(q)
=\beta\frac{1-t^2}{1-2t\cos q+t^2}
}
$$

となる。

![波数依存感受率](/figures/ising-r1/susceptibility-q.svg)

*$J>0$ では $q=0$ が最大で、低温ほどピークが狭くなる。*

$q=0$ では

$$
\chi(0)=\beta\frac{1+t}{1-t}=\beta e^{2K}
$$

となり、一様外場から得た結果と一致する。

強磁性 $J>0$ では $q_*=0$、反強磁性 $J<0$ では $q_*=\pi$ が選ばれる。最近接模型では自然な構造波数はこの二つに限られる。

## 6. 長波長極限では $q\xi$ が自然な変数になる

強磁性低温で $t=e^{-1/\xi}\simeq1-\xi^{-1}$、$q\ll1$ とすると

$$
\boxed{
\chi(q)
\simeq
\frac{2\beta\xi}{1+(q\xi)^2}
}
$$

となる。

$q^{-1}$ は外場が変化する長さ、$\xi$ は系が内部で相関を保つ長さである。

- $q\xi\ll1$：一つの相関領域の中で外場はほぼ一様
- $q\xi\gg1$：一つの相関領域の内部で外場が何度も符号反転し、応答が相殺

という対応になる。

最近接 Ising 鎖は、空間 Fourier mode に対する単純な **wave-vector filter** として読める。

## 7. 空間振動外場は相関長を直接 probe する

$$
h_i=h_q\cos(qi+\phi)
$$

とすると、線形応答では

$$
\boxed{
\langle s_i\rangle
=\chi(q)h_q\cos(qi+\phi)+O(h_q^3)
}
$$

となる。

![空間振動外場と磁化応答](/figures/ising-r1/spatial-field-response.svg)

*$\beta J=1.2$、$h_q/J=0.05$。長波長では応答が大きく、短波長では強く抑制される。*

同じ外場振幅でも、波数が違えば応答は大きく変わる。これは $\chi(q)$ が実空間の記憶長を Fourier 空間で読んだ量だからである。

有限振幅では位置依存 transfer matrix

$$
T_i(s_i,s_{i+1})
=\exp\left[
\beta J s_i s_{i+1}
+\frac{\beta}{2}
(h_i s_i+h_{i+1}s_{i+1})
\right]
$$

を使える。

外場が周期 $L$ を持つなら

$$
M_L=T_1T_2\cdots T_L
$$

と一周期をまとめ、最大固有値 $\Lambda_+$ から

$$
\boxed{
f=-\frac{1}{\beta L}\ln\Lambda_+}
$$

を得る。

有限振幅では

$$
m_i=m_q\cos(qi)+m_{3q}\cos(3qi)+\cdots
$$

のような高調波も現れうる。

## 8. 相関は情報保持としても読める

左端 $s_0=\pm1$ を1 bitの入力と考える。零外場では

$$
P(s_r=s_0\mid s_0)=\frac{1+C(r)}{2},
\qquad
P(s_r\neq s_0\mid s_0)=\frac{1-C(r)}{2}.
$$

$s_0\to s_r$ は、熱的domain wallが作る binary channel として読める。

ただし壁そのものが情報を消すわけではない。全ての $\tau_i$ が既知なら

$$
s_r=s_0\prod_{k=0}^{r-1}\tau_k
$$

から完全に復元できる。情報損失は、壁配置を観測せず粗視化したときに現れる。

零外場では

$$
P(s_0,s_r)=\frac14[1+s_0s_rC(r)]
$$

なので mutual information は

$$
\boxed{
I(s_0:s_r)
=\frac{1+C(r)}{2}\ln[1+C(r)]
+\frac{1-C(r)}{2}\ln[1-C(r)]
}
$$

となる。

遠距離で $|C(r)|\ll1$ なら

$$
I(s_0:s_r)\simeq\frac12C(r)^2
\sim e^{-2r/\xi}.
$$

相関長 $\xi$ は線形記憶の減衰長であり、二点 mutual information の漸近減衰長は $\xi/2$ になる。相関と情報は同じ量ではない。

測定・フィードバックを別途導入した場合には、残った情報の熱力学的価値を $k_{\mathrm B}TI$ の尺度で読むこともできる。ただし平衡 Ising 鎖そのものが自発的に仕事を生成するという意味ではない。

## 9. 第二近接は「独立な壁」を相互作用させる

第二近接相互作用を加えると

$$
H
=-J_1\sum_i s_i s_{i+1}
-J_2\sum_i s_i s_{i+2}.
$$

$$
s_i s_{i+2}=\tau_i\tau_{i+1}
$$

なので

$$
\boxed{
H
=-J_1\sum_i\tau_i
-J_2\sum_i\tau_i\tau_{i+1}
}
$$

となる。

$$
\boxed{
\text{independent domain walls}
\longrightarrow
\text{interacting domain walls}
}
$$

が、最近接から第二近接への質的な変化である。

一般に

$$
s_i s_{i+r}=\prod_{k=0}^{r-1}\tau_{i+k}
$$

だから、有限範囲 $R$ の模型は

$$
\boxed{
H_R
=-\sum_i\left[
J_1\tau_i
+J_2\tau_i\tau_{i+1}
+\cdots
+J_R\prod_{k=0}^{R-1}\tau_{i+k}
\right]
}
$$

と書ける。

スピン表示では相互作用範囲が伸びるほど transfer state が過去のスピンを多く保持し、wall表示では局所多体結合が増える。

$$
\boxed{
\text{interaction range}
\longleftrightarrow
\text{finite spatial memory}
}
$$

という対応が見える。

最近接鎖は、相互作用範囲、欠陥、相関長、波数応答、情報保持が最も単純な形で一つにつながる基準点になっている。

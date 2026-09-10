---
title: "1次元イジング模型 R=1 — 最近接相互作用と空間応答"
summary: "最近接相互作用だけを持つ1次元Ising鎖を、有限相互作用範囲系列の基準点として読む。転送行列、ドメイン壁、相関長、一様外場、波数依存感受率、空間振動外場への応答を同じ構造としてつなぐ。"
publishedAt: 2025-05-27T21:25:00+09:00
updatedAt: 2026-09-10
area: "Physics"
topics: ["statistical mechanics", "Ising model", "transfer matrix", "correlation", "linear response"]
status: growing
---

1次元 Ising 模型を、単に「厳密に解ける最も簡単な磁性模型」としてではなく、**相互作用範囲を少しずつ伸ばしていく系列の基準点**として見る。

一般に有限範囲 $R$ の1次元 Ising 模型を

$$
H_R
= -\sum_i\sum_{r=1}^{R}J_r s_i s_{i+r}
  -\sum_i h_i s_i,
\qquad s_i=\pm1
$$

と書く。このノートでは最小の場合

$$
\boxed{
H_{R=1}
= -J\sum_i s_i s_{i+1}
  -\sum_i h_i s_i
}
$$

を扱う。

ここで知りたいのは、分配関数を計算できるという事実だけではない。$R=1$ では何が特別に単純なのか、外場に対してどの空間スケールで応答するのか、そして $R=2$ にしたとき何が初めて壊れるのかを見たい。

以下では格子間隔を $a=1$ とし、

$$
K\equiv\beta J,
\qquad
\beta=\frac{1}{k_B T}
$$

と書く。

## 1. $R=1$ では「直前の1スピン」だけで再帰が閉じる

まず外場をゼロとする。

$$
H=-J\sum_{i=1}^{N-1}s_i s_{i+1}.
$$

開境界条件で、最後のスピンを固定した部分分配関数

$$
Z_N^{(+)},\qquad Z_N^{(-)}
$$

を導入すると、

$$
\begin{pmatrix}
Z_N^{(+)}\\
Z_N^{(-)}
\end{pmatrix}
=
\begin{pmatrix}
e^K & e^{-K}\\
e^{-K} & e^K
\end{pmatrix}
\begin{pmatrix}
Z_{N-1}^{(+)}\\
Z_{N-1}^{(-)}
\end{pmatrix}.
$$

新しいスピン $s_N$ を加えるときに必要なのは $s_{N-1}$ だけである。したがって $R=1$ では、局所状態は1スピンで閉じ、転送行列は $2\times2$ になる。

この行列の固有値は

$$
\lambda_+=2\cosh K,
\qquad
\lambda_-=2\sinh K.
$$

したがって、非自明な固有値比は

$$
\boxed{
\frac{\lambda_-}{\lambda_+}=\tanh K
}
$$

ただ一つである。この量が、以下では相関、境界情報の減衰、ドメイン壁密度を同時に支配する。

## 2. ドメイン壁表示では $R=1$ は自由な欠陥系になる

外場ゼロで

$$
\tau_i\equiv s_i s_{i+1}=\pm1
$$

を導入する。$\tau_i=-1$ は $i$ と $i+1$ の間にドメイン壁があることを意味する。

すると

$$
\boxed{
H=-J\sum_i\tau_i
}
$$

となる。開鎖では各 $\tau_i$ は互いに独立であり、分配関数も

$$
Z_N
=2(2\cosh K)^{N-1}
$$

と因数分解する。

1本の結合がドメイン壁になる確率は

$$
p_{\rm dw}
=
\frac{e^{-K}}{e^K+e^{-K}}
=
\frac{1}{1+e^{2K}},
$$

したがって

$$
\langle\tau_i\rangle
=1-2p_{\rm dw}
=\tanh K.
$$

ここで転送行列の固有値比と同じ量が現れる。

$$
\boxed{
\frac{\lambda_-}{\lambda_+}
=
\langle\tau\rangle
=
1-2p_{\rm dw}
=
\tanh K
}
$$

$R=1$ の単純さは、転送行列が小さいことだけではなく、**ドメイン壁が相互作用しない**ことにもある。

## 3. 一様外場は $q=0$ の応答である

次に

$$
h_i=h
$$

という一様外場を加える。

$$
H
=-J\sum_i s_i s_{i+1}
-h\sum_i s_i.
$$

転送行列を

$$
T_{s,s'}
=
\exp\left[
\beta Jss'
+\frac{\beta h}{2}(s+s')
\right]
$$

と定義すると、

$$
T=
\begin{pmatrix}
e^{K+\beta h} & e^{-K}\\
e^{-K} & e^{K-\beta h}
\end{pmatrix}.
$$

固有値は

$$
\lambda_\pm
=e^K\left[
\cosh(\beta h)
\pm
\sqrt{\sinh^2(\beta h)+e^{-4K}}
\right].
$$

熱力学極限では

$$
f
=-\frac{1}{\beta}\ln\lambda_+,
$$

したがって磁化は

$$
\boxed{
m(h)
=-\frac{\partial f}{\partial h}
=
\frac{\sinh(\beta h)}
{\sqrt{\sinh^2(\beta h)+e^{-4K}}}
}
$$

となる。

![一様外場に対する磁化](/figures/ising-r1/magnetization-field.svg)

*一様外場に対する磁化。低温ほど $h=0$ 近傍の応答は急になるが、有限温度では $h=0$ で自発磁化は生じない。*

$h=0$ における一様感受率は

$$
\boxed{
\chi(0)
=
\left.\frac{\partial m}{\partial h}\right|_{h=0}
=
\beta e^{2K}
}
$$

である。ここでは一様外場を特別視せず、後で **波数 $q=0$ の外場**として読み直す。

## 4. 相関関数と相関長

外場ゼロでは

$$
s_i s_{i+r}
=
\tau_i\tau_{i+1}\cdots\tau_{i+r-1}.
$$

$R=1$ ではドメイン壁変数 $\tau_i$ が独立なので、

$$
\begin{aligned}
C(r)
&\equiv\langle s_i s_{i+r}\rangle\\
&=
\prod_{j=i}^{i+r-1}\langle\tau_j\rangle\\
&=(\tanh K)^r.
\end{aligned}
$$

したがって

$$
\boxed{
C(r)
=\left(\frac{\lambda_-}{\lambda_+}\right)^r
=(\tanh K)^r
}
$$

である。

![距離に対する二点相関関数](/figures/ising-r1/correlation-distance.svg)

*最近接強磁性鎖の二点相関。$R=1$ では単一の指数減衰であり、非自明な減衰モードは一つしかない。*

相関長 $\xi$ を

$$
C(r)=e^{-r/\xi}
$$

で定義すれば、

$$
\boxed{
\xi^{-1}
=-\ln|\tanh K|
=\ln\left|\frac{\lambda_+}{\lambda_-}\right|
}
$$

となる。

低温 $K\gg1$ では

$$
\tanh K\simeq1-2e^{-2K}
$$

なので、

$$
\boxed{
\xi\simeq\frac{1}{2}e^{2K}
}
$$

である。

![相関長の温度依存](/figures/ising-r1/correlation-length-temperature.svg)

*相関長の厳密式と低温漸近形。$T\to0$ では急速に増大するが、任意の有限温度では有限である。*

低温では

$$
p_{\rm dw}\simeq e^{-2K}
$$

なので

$$
\xi\simeq\frac{1}{2p_{\rm dw}}.
$$

相関を壊すのは単に「壁が1本あるか」ではなく、区間内に存在する壁の偶奇性である。このため平均ドメイン壁間隔 $p_{\rm dw}^{-1}$ と相関長には係数2の違いが生じる。

## 5. 一様外場から空間依存外場へ

位置依存する微小外場

$$
h_i=\delta h_i
$$

を加える。線形応答では

$$
\delta\langle s_i\rangle
=
\sum_j\chi_{ij}\,\delta h_j,
$$

ここで

$$
\chi_{ij}
=
\beta\left(
\langle s_i s_j\rangle
-\langle s_i\rangle\langle s_j\rangle
\right).
$$

外場ゼロでは $\langle s_i\rangle=0$ なので、

$$
\chi_{ij}
=
\beta C(i-j).
$$

したがって $R=1$ では

$$
\boxed{
\chi(r)
=\beta(\tanh K)^{|r|}
}
$$

となる。

ここで実空間の相関を Fourier 変換して

$$
\chi(q)
=
\sum_{r=-\infty}^{\infty}\chi(r)e^{-iqr}
$$

を考える。$t\equiv\tanh K$ とおけば、

$$
\begin{aligned}
\chi(q)
&=
\beta\left[
1+2\sum_{r=1}^{\infty}t^r\cos(qr)
\right]\\
&=\boxed{
\beta\frac{1-t^2}{1-2t\cos q+t^2}
}.
\end{aligned}
$$

$q=0$ を代入すれば

$$
\chi(0)
=
\beta\frac{1+t}{1-t}
=
\beta e^{2K},
$$

となり、一様外場から得た感受率と一致する。

![波数依存感受率](/figures/ising-r1/susceptibility-q.svg)

*$J>0$ に対する規格化感受率 $\chi(q)/\chi(0)$。低温になるほど $q=0$ 周りのピークが狭くなり、長波長モードへの選択性が強くなる。*

強磁性 $J>0$ では $t>0$ なので $\chi(q)$ は $q=0$ で最大となる。一方、反強磁性 $J<0$ では $t<0$ となり、最大は $q=\pi$ へ移る。したがって最近接模型で自然に選ばれる波数は

$$
q_*=0\quad\text{or}\quad\pi
$$

に限られる。

## 6. $q\xi$：外場の波長と系自身の相関長

強磁性の低温領域では

$$
t=e^{-1/\xi}\simeq1-\frac{1}{\xi},
$$

また $q\ll1$ なら

$$
1-\cos q\simeq\frac{q^2}{2}.
$$

したがって

$$
\chi(q)
=
\beta
\frac{1-t^2}{(1-t)^2+2t(1-\cos q)}
$$

は

$$
\boxed{
\chi(q)
\simeq
\frac{2\beta\xi}{1+(q\xi)^2}
}
$$

となる。

ここで自然に現れる無次元量は

$$
\boxed{q\xi}
$$

である。

$q^{-1}$ は外場が空間的に変化する長さ、$\xi$ は系内部でスピン相関が伝わる長さである。

$$
q\xi\ll1
$$

なら外場は相関長よりゆっくり変化し、系は強く応答できる。逆に

$$
q\xi\gg1
$$

では、外場が相関長より短い距離で符号を変えるため応答は抑制される。

この意味で最近接 Ising 鎖は、空間 Fourier mode に対して単純な **wave-vector filter** として見ることができる。

## 7. 空間振動外場を与える

この見方を直接試すために

$$
\boxed{
h_i=h_q\cos(qi+\phi)
}
$$

という静的な空間振動外場を考える。

線形応答領域では単一 Fourier mode は混ざらないので、

$$
\boxed{
\langle s_i\rangle
=
\chi(q)h_q\cos(qi+\phi)
+O(h_q^3)
}
$$

となる。$h_i=0$ を基準とすれば、全スピン反転と $h_q\to-h_q$ の対称性により磁化は $h_q$ の奇関数であり、二次の補正は現れない。

![空間振動外場と磁化応答](/figures/ising-r1/spatial-field-response.svg)

*$\beta J=1.2$, $h_0/J=0.05$ における線形応答。長波長 $q=\pi/10$ では応答が増幅される一方、短波長 $q=\pi/2$ では強く抑制される。*

この図で重要なのは、応答が単に「外場が強いほど大きい」のではなく、同じ振幅でも **外場の波数によって大きく変わる**ことである。

### 有限振幅ではどうするか

振幅が十分大きく線形応答を外れる場合でも、$R=1$ なら位置依存転送行列で扱える。

$$
T_i(s_i,s_{i+1})
=
\exp\left[
\beta J s_i s_{i+1}
+\frac{\beta}{2}
\left(
h_i s_i+h_{i+1}s_{i+1}
\right)
\right].
$$

外場が格子上で周期 $L$ を持つなら

$$
h_{i+L}=h_i,
$$

1周期分の積

$$
M_L
=T_1T_2\cdots T_L
$$

を導入できる。$N$ が $L$ の整数倍なら

$$
Z
=\operatorname{Tr}M_L^{N/L}.
$$

$M_L$ の最大固有値を $\Lambda_+$ とすれば、熱力学極限の1サイトあたり自由エネルギーは

$$
\boxed{
f
=-\frac{1}{\beta L}\ln\Lambda_+
}
$$

となる。

これは時間発展ではないが、**周期的な空間係数を1周期ごとの行列積に縮約する**という意味で、空間版 Floquet 問題に似た構造を持つ。

有限振幅では応答は一般に純粋な $q$ 成分だけではなく、高調波を含みうる。したがって今後は

$$
m_i
=
m_q\cos(qi)
+m_{3q}\cos(3qi)
+\cdots
$$

のような非線形波数混合も調べられる。

## 8. $R=1$ で何が特別だったのか

ここまでを相互作用範囲の観点から整理すると、$R=1$ には次の特徴がある。

- 新しいスピンを加えるとき、直前の1スピンだけ覚えていればよい。
- 転送行列は $2\times2$ であり、非自明な減衰固有モードは1つだけである。
- 外場ゼロではドメイン壁が独立である。
- 相関関数は単一指数
  $$
  C(r)=(\tanh K)^r
  $$
  で閉じる。
- 強磁性・反強磁性で選ばれる波数は、それぞれ $q=0$ と $q=\pi$ に限られる。

この単純さは $R=2$ にすると崩れ始める。

$$
H_{R=2}
=-J_1\sum_i s_i s_{i+1}
-J_2\sum_i s_i s_{i+2}.
$$

ドメイン壁変数を使えば

$$
s_i s_{i+2}
=(s_i s_{i+1})(s_{i+1}s_{i+2})
=\tau_i\tau_{i+1},
$$

したがって

$$
\boxed{
H_{R=2}
=-J_1\sum_i\tau_i
-J_2\sum_i\tau_i\tau_{i+1}
}
$$

となる。

つまり $R=1$ で自由だったドメイン壁が、第二近接相互作用を入れた瞬間に相互作用し始める。また再帰を閉じるには $(s_{i-1},s_i)$ の2スピンを保持する必要があり、転送状態は4状態へ増える。

次に見るべきなのは、この最小の拡張によって

$$
C(r),\qquad \xi,\qquad \chi(q)
$$

がどう変わるか、そして $q=0,\pi$ 以外の有限波数構造がどのように現れうるかである。

## まとめ

最近接1次元 Ising 模型では、

$$
\boxed{
\frac{\lambda_-}{\lambda_+}
=\tanh(\beta J)
=\langle\tau\rangle
=1-2p_{\rm dw}
}
$$

という一つの量が、転送行列、ドメイン壁、相関減衰をつないでいる。

さらにその実空間相関を Fourier 変換すると

$$
\boxed{
\chi(q)
=
\beta\frac{1-\tanh^2(\beta J)}
{1-2\tanh(\beta J)\cos q+\tanh^2(\beta J)}
}
$$

が得られ、空間振動外場への波数選択的な応答が見える。

したがって $R=1$ は、単に「解ける模型」ではなく、**相互作用範囲、相関長、欠陥、波数応答が最も単純な形で一致する基準点**として使える。
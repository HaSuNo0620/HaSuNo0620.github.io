---
title: "1次元イジング模型 — 最近接相互作用と空間応答"
summary: "最近接相互作用だけを持つ1次元Ising鎖を、有限相互作用範囲系列の基準点として読む。転送行列、ドメイン壁、相関長、一様外場、波数依存感受率、空間振動外場への応答を同じ構造としてつなぐ。"
publishedAt: 2025-05-27T21:25:00+09:00
updatedAt: 2026-09-11
area: "Physics"
topics: ["statistical mechanics", "Ising model", "transfer matrix", "correlation", "linear response"]
status: growing
---

1次元 Ising 模型を、単に「厳密に解ける最も簡単な磁性模型」としてではなく、**相互作用範囲を少しずつ伸ばしていく系列の基準点**として見る。

一般に有限範囲 $R$ の1次元 Ising 模型を

$$
H_R=-\sum_i\sum_{r=1}^{R}J_r s_i s_{i+r}-\sum_i h_i s_i,
\qquad s_i=\pm1
$$

と書く。このノートでは最小の場合

$$
\boxed{
H_{R=1}=-J\sum_i s_i s_{i+1}-\sum_i h_i s_i
}
$$

を扱う。

ここで知りたいのは、分配関数を計算できるという事実だけではない。$R=1$ では何が特別に単純なのか、外場に対してどの空間スケールで応答するのか、そして $R=2$ にしたとき何が初めて壊れるのかを見たい。

以下では格子間隔を $a=1$ とし、$K\equiv\beta J$、$\beta=(k_B T)^{-1}$ と書く。

## 1. $R=1$ では「直前の1スピン」だけで再帰が閉じる

まず外場をゼロとする。

$$
H=-J\sum_{i=1}^{N-1}s_i s_{i+1}.
$$

開境界条件で、最後のスピンを固定した部分分配関数 $Z_N^{(+)}$ と $Z_N^{(-)}$ を導入すると、

$$
\begin{pmatrix}
Z_N^{(+)}\\
Z_N^{(-)}
\end{pmatrix} =
\begin{pmatrix}
e^K & e^{-K}\\
e^{-K} & e^K
\end{pmatrix}
\begin{pmatrix}
Z_{N-1}^{(+)}\\
Z_{N-1}^{(-)}
\end{pmatrix}.
$$

新しいスピン $s_N$ を加えるときに必要なのは $s_{N-1}$ だけである。したがって $R=1$ では局所状態は1スピンで閉じ、転送行列は $2\times2$ になる。

固有値は $\lambda_+=2\cosh K$ と $\lambda_-=2\sinh K$ であり、非自明な固有値比は

$$
\boxed{
\frac{\lambda_-}{\lambda_+}=\tanh K
}
$$

ただ一つである。この量が、以下では相関、境界情報の減衰、ドメイン壁密度を同時に支配する。

## 2. ドメイン壁表示とは何をしているのか

外場ゼロで bond 変数

$$
\tau_i\equiv s_i s_{i+1}=\pm1
$$

を導入する。$\tau_i=+1$ は隣接スピンが同方向、$\tau_i=-1$ は向きが反転していることを意味する。したがって

$$
\boxed{
\tau_i=-1
\quad\Longleftrightarrow\quad
i\text{ と }i+1\text{ の間にドメイン壁がある}
}
$$

と読める。

たとえばスピン列

$$
+\,+\,+\,-\,-\,+\,+ 
$$

では、符号が変わる bond が2か所ある。スピン表示が「各サイトの絶対的な向き」を記録するのに対し、ドメイン壁表示は**隣接サイト間で向きが変わった場所**を記録する。

### ドメイン壁表示は情報を捨てているのか

$\tau_i$ だけからは、全スピン反転で結ばれる

$$
+\,+\,+\,+\quad\text{と}\quad-\,-\,-\,-
$$

を区別できない。しかし基準スピン $s_1$ を一つ残せば、

$$
\boxed{
s_i=s_1\prod_{k=1}^{i-1}\tau_k
}
$$

によって全スピンを復元できる。したがって開鎖では

$$
\{s_i\}
\quad\longleftrightarrow\quad
\left(s_1,\{\tau_i\}\right)
$$

であり、ドメイン壁表示は近似ではなく変数の取り替えである。$\{\tau_i\}$ だけを見ると失われるのは、全体を同時に反転する $Z_2$ の1ビットだけである。

### なぜこの表示にするのか

最近接 Hamiltonian は

$$
\boxed{
H=-J\sum_i\tau_i
}
$$

となる。元のスピン表示では $s_i$ が隣接スピンと相互作用していたのに、$\tau_i$ 表示では異なる $\tau_i$ 同士の結合が消える。つまり外場ゼロの $R=1$ 鎖は

$$
\boxed{
\text{interacting spins}
\quad\longrightarrow\quad
\text{noninteracting domain-wall defects}
}
$$

と読み替えられる。

これがドメイン壁表示の第一の意義である。**どの自由度を選べば相互作用の本体が単純になるか**が見える。

強磁性 $J>0$ では壁のない bond のエネルギーは $-J$、壁のある bond は $+J$ なので、壁1個の生成コストは $2J$ である。したがって1本の bond が壁になる確率は

$$
p_{\mathrm{dw}}
=\frac{e^{-K}}{e^K+e^{-K}}
=\frac{1}{1+e^{2K}},
$$

低温では $p_{\mathrm{dw}}\simeq e^{-2K}$ となる。低温 Ising 鎖は「ほぼ一様な長い domain の中に、熱励起された壁がまばらに存在する系」として見える。

また

$$
\langle\tau_i\rangle
=1-2p_{\mathrm{dw}}
=\tanh K
$$

なので、

$$
\boxed{
\frac{\lambda_-}{\lambda_+}
=\langle\tau\rangle
=1-2p_{\mathrm{dw}}
=\tanh K
}
$$

となる。転送行列の固有値比が、欠陥密度という直接的な実空間像を持つこともこの表示の利点である。

### 表示には向き不向きがある

ドメイン壁表示が常に最善というわけではない。一様外場項は

$$
-h\sum_i s_i
=-hs_1\sum_i\prod_{k=1}^{i-1}\tau_k
$$

となり、$\tau_i$ に対して非局所的になる。

したがってこのノートでは、

- **相互作用・欠陥・相関の起源を見るとき**はドメイン壁表示、
- **磁化・外場応答を見るとき**はスピン表示、

を使い分ける。重要なのは表示を一つに固定することではなく、**各表示が何を局所化し、何を非局所化するか**を見ることである。

## 3. 一様外場は $q=0$ の応答である

一様外場 $h_i=h$ を加えると、

$$
H=-J\sum_i s_i s_{i+1}-h\sum_i s_i.
$$

転送行列を

$$
T_{s,s'}
=\exp\left[
\beta Jss'+\frac{\beta h}{2}(s+s')
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
\pm\sqrt{\sinh^2(\beta h)+e^{-4K}}
\right].
$$

熱力学極限では $f=-\beta^{-1}\ln\lambda_+$ なので、

$$
\boxed{
m(h)
=-\frac{\partial f}{\partial h}
=\frac{\sinh(\beta h)}
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
=\left.\frac{\partial m}{\partial h}\right|_{h=0}
=\beta e^{2K}
}
$$

である。ここでは一様外場を特別視せず、後で**波数 $q=0$ の外場**として読み直す。

## 4. 相関関数は「壁の個数の偶奇」を見ている

ドメイン壁変数を使うと

$$
s_i s_{i+r}
=\tau_i\tau_{i+1}\cdots\tau_{i+r-1}
=(-1)^{N_{\mathrm{wall}}(i,i+r)}
$$

である。つまり二点相関は、2点の間に壁が何本あるかそのものではなく、**壁の本数が偶数か奇数か**を測っている。

$R=1$ では $\tau_i$ が独立なので、

$$
\begin{aligned}
C(r)
&\equiv\langle s_i s_{i+r}\rangle\\
&=\prod_{j=i}^{i+r-1}\langle\tau_j\rangle\\
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

$C(r)=e^{-r/\xi}$ で相関長 $\xi$ を定義すれば、

$$
\boxed{
\xi^{-1}
=-\ln|\tanh K|
=\ln\left|\frac{\lambda_+}{\lambda_-}\right|
}
$$

となる。低温 $K\gg1$ では $\tanh K\simeq1-2e^{-2K}$ なので、

$$
\boxed{
\xi\simeq\frac12 e^{2K}
}
$$

である。

![相関長の温度依存](/figures/ising-r1/correlation-length-temperature.svg)

*相関長の厳密式と低温漸近形。$T\to0$ では急速に増大するが、任意の有限温度では有限である。*

低温では $p_{\mathrm{dw}}\simeq e^{-2K}$ だから $\xi\simeq(2p_{\mathrm{dw}})^{-1}$ である。平均壁間隔は $p_{\mathrm{dw}}^{-1}$ なので、

$$
\boxed{
\ell_{\mathrm{wall}}\simeq2\xi
}
$$

となる。係数2が現れるのは、相関が「最初の壁に遭遇したか」ではなく $(-1)^{N_{\mathrm{wall}}}$、すなわち壁数の偶奇を見ているためである。

## 5. 一様外場から空間依存外場へ

位置依存する微小外場 $\delta h_i$ に対する線形応答は

$$
\delta\langle s_i\rangle
=\sum_j\chi_{ij}\,\delta h_j,
$$

ここで

$$
\chi_{ij}
=\beta\left(
\langle s_i s_j\rangle
-\langle s_i\rangle\langle s_j\rangle
\right).
$$

外場ゼロでは $\langle s_i\rangle=0$ なので $\chi_{ij}=\beta C(i-j)$ であり、

$$
\boxed{
\chi(r)=\beta(\tanh K)^{|r|}
}
$$

となる。

$t\equiv\tanh K$ とおき、実空間応答を Fourier 変換すると、

$$
\begin{aligned}
\chi(q)
&=\sum_{r=-\infty}^{\infty}\chi(r)e^{-iqr}\\
&=\beta\left[1+2\sum_{r=1}^{\infty}t^r\cos(qr)\right]\\
&=\boxed{\beta\frac{1-t^2}{1-2t\cos q+t^2}}.
\end{aligned}
$$

$q=0$ では $\chi(0)=\beta(1+t)/(1-t)=\beta e^{2K}$ となり、一様外場から得た感受率と一致する。

![波数依存感受率](/figures/ising-r1/susceptibility-q.svg)

*$J>0$ に対する規格化感受率 $\chi(q)/\chi(0)$。低温になるほど $q=0$ 周りのピークが狭くなり、長波長モードへの選択性が強くなる。*

強磁性 $J>0$ では $t>0$ なので $\chi(q)$ は $q=0$ で最大となる。一方、反強磁性 $J<0$ では $t<0$ となり、最大は $q=\pi$ へ移る。したがって最近接模型で自然に選ばれる波数は $q_*=0$ または $q_*=\pi$ に限られる。

## 6. $q\xi$：外場の波長と系自身の相関長

強磁性の低温領域では $t=e^{-1/\xi}\simeq1-\xi^{-1}$、また $q\ll1$ なら $1-\cos q\simeq q^2/2$ である。したがって

$$
\chi(q)
=\beta\frac{1-t^2}{(1-t)^2+2t(1-\cos q)}
$$

は

$$
\boxed{
\chi(q)\simeq\frac{2\beta\xi}{1+(q\xi)^2}
}
$$

となる。

自然な無次元量は $q\xi$ である。$q^{-1}$ は外場が空間的に変化する長さ、$\xi$ は系内部でスピン相関が伝わる長さなので、$q\xi\ll1$ では外場は一つの相関領域の中でほぼ一様に見え、強く応答できる。逆に $q\xi\gg1$ では、一つの相関領域の内部で外場が何度も符号を変えるため応答が相殺される。

この意味で最近接 Ising 鎖は、空間 Fourier mode に対して単純な **wave-vector filter** として見ることができる。

## 7. 空間振動外場を与える

静的な空間振動外場

$$
\boxed{
h_i=h_q\cos(qi+\phi)
}
$$

を考える。線形応答領域では異なる Fourier mode は混ざらないので、

$$
\boxed{
\langle s_i\rangle
=\chi(q)h_q\cos(qi+\phi)+O(h_q^3)
}
$$

となる。$h_i=0$ を基準とすれば、全スピン反転と $h_q\to-h_q$ の対称性により磁化は $h_q$ の奇関数であり、二次の補正は現れない。

![空間振動外場と磁化応答](/figures/ising-r1/spatial-field-response.svg)

*$\beta J=1.2$、$h_q/J=0.05$ における線形応答。長波長 $q=\pi/10$ では応答が増幅される一方、短波長 $q=\pi/2$ では強く抑制される。*

重要なのは、応答が単に「外場が強いほど大きい」のではなく、同じ振幅でも**外場の波数によって大きく変わる**ことである。

### 有限振幅ではどうするか

振幅が十分大きく線形応答を外れる場合でも、$R=1$ なら位置依存転送行列で扱える。

$$
T_i(s_i,s_{i+1})
=\exp\left[
\beta J s_i s_{i+1}
+\frac{\beta}{2}
\left(h_i s_i+h_{i+1}s_{i+1}\right)
\right].
$$

外場が格子上で周期 $L$ を持ち $h_{i+L}=h_i$ なら、転送行列も同じ周期で $T_{i+L}=T_i$ を満たす。ここで重要なのは、分配関数が「格子を1サイトずつ進む局所重みの積」でできていることである。したがって、まず1周期に含まれる $L$ 個の局所重みをまとめて

$$
M_L=T_1T_2\cdots T_L
$$

という**1周期の有効転送行列**を定義するのが自然である。

全長が $N=nL$ なら、同じ周期ブロックが $n$ 回繰り返されるので

$$
Z=\operatorname{Tr}M_L^n
=\operatorname{Tr}M_L^{N/L}.
$$

したがって熱力学極限では、1サイトごとの自由エネルギーは $M_L$ の最大固有値 $\Lambda_+$ だけで決まり、

$$
\boxed{
f=-\frac{1}{\beta L}\ln\Lambda_+
}
$$

となる。つまりこの立式は、**空間周期性を持つ系を1周期ごとの粗視化された転送問題へ縮約している**。時間発展との類比を持ち出す必要はなく、周期的な局所 Boltzmann 重みの反復として理解すれば十分である。

有限振幅では応答は純粋な $q$ 成分だけではなく、高調波を含みうる。たとえば対称性が許す場合、

$$
m_i=m_q\cos(qi)+m_{3q}\cos(3qi)+\cdots
$$

のような非線形波数混合が現れる。

## 8. 情報熱力学的に読む：熱雑音の中でどこまで記憶を保持できるか

ここまで「相関」や「境界条件の記憶」という言葉を使ってきたが、これを情報熱力学的な量へ接続することもできる。まず左端のスピン $s_0=\pm1$ を外部から設定した1 bit の入力と考える。ゼロ磁場では $P(s_0=+1)=P(s_0=-1)=1/2$ であり、距離 $r$ のスピンとの二点相関を $C(r)=\langle s_0s_r\rangle$ とすれば、

$$
P(s_r=s_0\mid s_0)=\frac{1+C(r)}{2},
\qquad
P(s_r\neq s_0\mid s_0)=\frac{1-C(r)}{2}.
$$

したがって、$s_0\to s_r$ は熱雑音によって符号反転が起こる binary channel として読める。$R=1$ では1 bond ごとの反転確率はちょうどドメイン壁確率

$$
p_{\mathrm{dw}}=\frac{1}{1+e^{2\beta J}}
$$

である。つまりドメイン壁は、情報そのものを消してしまう物体ではなく、**観測しなければ bit-flip noise として見える熱励起**である。実際、全ての $\tau_i$ を知っていれば

$$
s_r=s_0\prod_{k=0}^{r-1}\tau_k
$$

から $s_r$ は完全に復元できる。情報の損失は、壁配置を追跡せず粗視化したときに現れる。

この点を mutual information で定量化できる。ゼロ磁場では

$$
P(s_0,s_r)=\frac14\left[1+s_0s_r C(r)\right]
$$

なので、自然対数を用いると

$$
\boxed{
I(s_0:s_r)
=\frac{1+C(r)}{2}\ln[1+C(r)]
+\frac{1-C(r)}{2}\ln[1-C(r)]
}
$$

となる。遠距離で $|C(r)|\ll1$ なら

$$
I(s_0:s_r)\simeq\frac12 C(r)^2.
$$

$R=1$ では $C(r)=e^{-r/\xi}$ だから、

$$
\boxed{
I(s_0:s_r)\sim e^{-2r/\xi}
}
$$

である。したがって相関長 $\xi$ は境界条件の**線形な記憶**が減衰する長さであり、二点 mutual information の漸近減衰長は $\xi/2$ になる。相関と情報は同じものではない。

情報熱力学では mutual information は、測定とフィードバックを導入したときに利用可能な熱力学的資源として現れる。適切なフィードバック過程では、得られた情報によって通常の自由エネルギー差を超えて取り出せる仕事の増分は $k_BT I$ を尺度として制約される。したがってこの鎖では、距離 $r$ まで残った情報の潜在的な熱力学的価値も

$$
W_{\mathrm{info}}^{\max}(r)\sim k_BT\,I(s_0:s_r)
$$

という尺度で減衰すると解釈できる。ただしこれは**平衡 Ising 鎖そのものが自発的に仕事を生成するという意味ではない**。測定装置・フィードバック操作・仕事取り出し過程を別途導入したとき、鎖中に残った相関情報がどれだけ資源になりうるかを表す読み方である。

この観点では、$J$ は単なる磁気相互作用ではなく熱雑音に対抗して記憶を保持するエネルギースケールでもある。低温では $p_{\mathrm{dw}}\sim e^{-2\beta J}$ なので、$J/k_BT$ を大きくするほど bit-flip noise は抑えられ、記憶をより遠くまで保持できる。

この解釈は次の $R=2$ にも自然につながる。$R=1$ ではドメイン壁が独立なので熱的 bit-flip も独立だが、$R=2$ で $\tau_i\tau_{i+1}$ 相互作用が入ると、**熱的誤りそのものが相関を持つ**ようになる。すなわち有限相互作用範囲の拡張は、情報論的には memoryless noise から correlated noise への最小の拡張としても読める。

## 9. $R=2$ で最初に何が変わるか

$R=1$ の単純さは、

- 新しいスピンを加えるとき直前の1スピンだけ覚えればよい、
- 転送行列は $2\times2$、
- 外場ゼロではドメイン壁が独立、
- 相関関数は単一指数、
- 強磁性・反強磁性の自然な波数は $q=0,\pi$、

という点にある。

第二近接相互作用を加えると、

$$
H_{R=2}
=-J_1\sum_i s_i s_{i+1}
-J_2\sum_i s_i s_{i+2}.
$$

ここで

$$
s_i s_{i+2}
=(s_i s_{i+1})(s_{i+1}s_{i+2})
=\tau_i\tau_{i+1}
$$

なので、

$$
\boxed{
H_{R=2}
=-J_1\sum_i\tau_i
-J_2\sum_i\tau_i\tau_{i+1}
}
$$

となる。

したがって $R=1\to2$ はドメイン壁表示では

$$
\boxed{
\text{free domain walls}
\quad\longrightarrow\quad
\text{interacting domain walls}
}
$$

である。

これがドメイン壁表示を導入した第二の大きな意義である。**「相互作用範囲を1格子伸ばした」という操作が、欠陥自由度の側では「壁同士に相互作用を入れた」という質的変化として見える。**

さらに一般に

$$
s_i s_{i+r}
=\prod_{k=0}^{r-1}\tau_{i+k},
$$

したがって有限範囲 $R$ の模型は

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

と書ける。相互作用範囲を伸ばすことは、ドメイン壁表示では1体、2体、3体、…の局所結合を順に導入することに対応する。

一方、スピン表示では再帰を閉じるために直前の $R$ スピンを保持する必要がある。したがって転送状態数は $2^R$ へ増える。

$$
\boxed{
\text{interaction range }R
\quad\longleftrightarrow\quad
\text{memory of }R\text{ spins}
}
$$

という対応と、

$$
\boxed{
\text{interaction range }R
\quad\longleftrightarrow\quad
R\text{-body local structure in domain-wall variables}
}
$$

という対応を並べると、有限範囲 Ising 系列の構造がかなり見通しよくなる。

次に見るべきなのは、$R=2$ で壁間相互作用が入った結果、$C(r)$、$\xi$、$\chi(q)$ がどう変わり、$q=0,\pi$ 以外の有限波数構造がどのように現れうるかである。

## まとめ

最近接1次元 Ising 模型では、

$$
\boxed{
\frac{\lambda_-}{\lambda_+}
=\tanh(\beta J)
=\langle\tau\rangle
=1-2p_{\mathrm{dw}}
}
$$

という一つの量が、転送行列、ドメイン壁、相関減衰をつないでいる。

ドメイン壁表示の意義は、単なる別表現にあるのではない。$R=1$ を**自由な熱励起欠陥の系**として読み直し、相関関数を**壁数の偶奇の統計**として理解し、さらに $R=2$ への拡張を**壁同士の相互作用の出現**として見せる点にある。

その実空間相関を Fourier 変換すると、

$$
\boxed{
\chi(q)
=\beta\frac{1-\tanh^2(\beta J)}
{1-2\tanh(\beta J)\cos q+\tanh^2(\beta J)}
}
$$

が得られ、空間振動外場への波数選択的な応答が見える。

したがって $R=1$ は単に「解ける模型」ではなく、**相互作用範囲、局所記憶、欠陥、相関長、波数応答、情報保持が最も単純な形で接続する基準点**として使える。

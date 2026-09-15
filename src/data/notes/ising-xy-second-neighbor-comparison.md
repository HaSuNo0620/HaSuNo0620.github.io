---
title: "第二近接IsingとXY — 平均場・Bethe・transfer spectrumで見る三つの解像度"
summary: "第二近接Ising鎖とXY鎖を、平均場・saddle point、Bethe/cavity、厳密transfer spectrumという三つの方法で比較する。個々のXY導出は第二近接XYノートに譲り、欠陥の形、局所遷移確率、長距離相関の固有値がどう対応するかに焦点を置く。"
publishedAt: 2026-09-13T22:45:00+09:00
updatedAt: 2026-09-16
area: "Physics"
topics: ["Ising model", "XY model", "second-neighbor interaction", "chirality"]
status: growing
---

第二近接Ising鎖と第二近接XY鎖は、どちらも厳密にはtransfer matrix / transfer operatorで扱える。それでも平均場やBethe/cavityを見る意味は残る。三つの方法は精度だけを段階的に上げるものではなく、同じ統計構造の別の断面を見せる。

$$
\boxed{
\text{平均場・saddle point}
\longleftrightarrow
\text{Bethe / cavity}
\longleftrightarrow
\text{exact transfer spectrum}
}
$$

平均場は**どんな欠陥・場配置が記憶を壊すか**、Bethe/cavityは**その局所遷移がどの頻度で起こるか**、transfer spectrumは**その結果として長距離相関がどう減衰するか**を見せる。

第二近接XYそのものの $q_\ast$、連続場、chirality kink、tilted operator、有限波数応答の導出は [第二近接XYノート](/notes/xy-chain-second-neighbor) に置き、この比較ノートではIsingとの対応関係だけを残す。

以下では

$$
\beta\equiv\frac{1}{k_{\mathrm B}T}
$$

とする。

## 1. 両模型とも局所相対変数が相互作用する

Isingでは

$$
H_{\rm I}
=-J_1\sum_i s_is_{i+1}
-J_2\sum_i s_is_{i+2}
$$

に対して

$$
\tau_i=s_is_{i+1}=\pm1
$$

とおけば

$$
\boxed{
H_{\rm I}
=-J_1\sum_i\tau_i
-J_2\sum_i\tau_i\tau_{i+1}}
$$

となる。

XYでは

$$
\phi_i=\theta_{i+1}-\theta_i
$$

を使うと

$$
\boxed{
H_{\rm XY}
=-J_1\sum_i\cos\phi_i
-J_2\sum_i\cos(\phi_i+\phi_{i+1})}
$$

となる。

したがって両方とも

$$
\boxed{
\text{independent local variables}
\longrightarrow
\text{interacting local variables}}
$$

という変化を持つ。ただし、Isingでは局所変数が離散的なwall情報、XYでは連続的なtwist情報である。

## 2. 方法I：平均場・saddle pointは「何が切り替わるか」を見せる

### Ising

$\tau_i=-1$ はspin列のdomain wallに対応する。粗視化したbond order $m_\tau(x)$ を使えば

$$
F[m_\tau]
=\int dx\left[
\frac{K}{2}(\partial_xm_\tau)^2+V(m_\tau)
\right]
$$

のような連続場は書けるが、microscopicなwall自体は格子上の離散欠陥である。

そのためIsingで平均場的描像から読むべき中心量は、滑らかなprofileそのものより

$$
\boxed{
\text{wall cost と competing wall pattern}
}
$$

である。

### XY

競合領域 $J_1>0$, $J_2<0$ では、局所twistが

$$
\phi\simeq +q_\ast,\qquad \phi\simeq-q_\ast
$$

という二つのchirality sectorを持つ。$\kappa\equiv |J_2|/J_1$ とすると、螺旋側は $\kappa>1/4$ で現れ、臨界点近傍の長波長場は二重井戸型になる。

詳細な導出は第二近接XYノートに譲るが、saddle-pointからは

$$
\boxed{
\ell_{\rm k}\propto
\left(\kappa-\frac14\right)^{-1/2}}
$$

と

$$
\boxed{
E_{\rm k}\propto
J_1\left(\kappa-\frac14\right)^{3/2}}
$$

が得られる。

ここで平均場が与える情報は相関長の正確な値ではなく、

$$
\boxed{
\text{chirality kink barrier}
\longrightarrow
\text{rare switching}}
$$

という記憶喪失の機構である。

IsingとXYの差は、欠陥が**離散wallの配置**なのか、**連続twist場の中のchirality kink**なのかに現れる。

## 3. 方法II：Bethe / cavityは「どの頻度で切り替わるか」を見せる

平均場で欠陥の姿を決めても、有限温度でその欠陥がどれだけ現れるかは別の問題である。Bethe/cavityでは局所条件付き確率を読む。

### Ising

$\tau_i$ 表現では

$$
P(\tau_{i+1}|\tau_i)
$$

が2状態遷移確率になる。対称な場合を

$$
P=
\begin{pmatrix}
1-p & p\\
p & 1-p
\end{pmatrix}
$$

と書けば

$$
\langle\tau_0\tau_r\rangle=(1-2p)^r
$$

だから

$$
\boxed{
\xi_\tau^{-1}=-\ln|1-2p|}
$$

となる。

第二近接Isingは $\tau$ 表現では1次元最近接Markov鎖なので、この局所確率記述は本質的にexactである。

### XY

XYでは

$$
P(\phi'|\phi)
$$

という連続状態の条件付き分布になる。低温螺旋側を二つのchirality basinへ粗視化すると、

$$
p_{\rm flip}
$$

というchirality switching probabilityを定義できる。

希薄switching極限では

$$
\boxed{
\xi_\chi^{-1}
\simeq -\ln(1-2p_{\rm flip})}
$$

したがって

$$
\boxed{
\xi_\chi\simeq\frac{1}{2p_{\rm flip}}}
}
$$

となる。

平均場で見えたkink barrierとの対応は

$$
\boxed{
p_{\rm flip}
\sim e^{-\beta\Delta F_{\rm k}}}
$$

である。$E_{\rm k}$ がsaddle-point energyなら、$\Delta F_{\rm k}$ はkink周囲の揺らぎによるentropyも含む。

ここで

$$
\boxed{
\text{欠陥の形}
\longrightarrow
\text{欠陥の出現頻度}}
$$

という一段の橋が架かる。

## 4. 方法III：transfer spectrumは局所統計を長距離記憶へまとめる

### Ising

$\tau$ 表現のtransfer matrixは

$$
T_{\tau,\tau'}
=
\exp\left[
\beta J_2\tau\tau'
+
\frac{\beta J_1}{2}(\tau+\tau')
\right]
$$

である。

固有値を $\lambda_0,\lambda_1$ とすれば

$$
\boxed{
\xi_\tau^{-1}
=-\ln\left|\frac{\lambda_1}{\lambda_0}\right|}
$$

となる。Bethe/cavityに現れた局所遷移率と、transfer matrixの固有値比は同じ記憶率を別の表現で読んでいる。

### XY

XYでは積分transfer operator

$$
\mathcal T(\phi,\phi')
=\exp\left[
\frac{\beta J_1}{2}(\cos\phi+\cos\phi')
+\beta J_2\cos(\phi+\phi')
\right]
$$

を使う。

chiralityは $\phi\to-\phi$ に対してoddなので、最大even固有値 $\lambda_0$ と最大odd固有値 $\lambda_\chi$ のsplittingが

$$
\boxed{
\xi_\chi^{-1}
=-\ln\left|\frac{\lambda_\chi}{\lambda_0}\right|}
$$

を決める。

低温で $\lambda_\chi\to\lambda_0$ となることは、Bethe側では $p_{\rm flip}\to0$、平均場側ではkinkが希薄になることに対応する。

## 5. 三つの方法は「形・頻度・スペクトル」を対応させる

Isingでは

$$
\boxed{
\text{wall cost}
\longrightarrow
p
\longrightarrow
\lambda_1/\lambda_0
\longrightarrow
\xi_\tau}
$$

XYのchirality sectorでは

$$
\boxed{
E_{\rm k}
\longrightarrow
p_{\rm flip}
\longrightarrow
\lambda_\chi/\lambda_0
\longrightarrow
\xi_\chi}
$$

という対応になる。

| 方法 | 主に読む量 | Ising | XY |
| --- | --- | --- | --- |
| 平均場・saddle point | 欠陥の形・cost | wall / bond-order texture | chirality kink |
| Bethe / cavity | 局所遷移確率 | $P(\tau'|\tau)$ | $P(\phi'|\phi)$、$p_{\rm flip}$ |
| exact transfer | 長距離memory | $\lambda_1/\lambda_0$ | $\lambda_\chi/\lambda_0$ |

したがって

$$
\text{平均場}<\text{Bethe}<\text{exact}
$$

という単純な精度序列が中心ではない。

$$
\boxed{
\text{形}
\longleftrightarrow
\text{頻度}
\longleftrightarrow
\text{長距離スペクトル}}
$$

という異なる解像度の対応が中心になる。

## 6. XYではchiralityだけではspin memoryが閉じない

ここから先がIsingとXYの本質的な非対称性になる。

Isingでは離散的な局所変数のMarkov統計がspin memoryへかなり直接につながる。一方XYでは

$$
\theta_r-\theta_0
=\sum_{i=0}^{r-1}\phi_i
$$

なので、chirality switchingのほかにcontinuous phase accumulationが残る。

したがって低温では

$$
\boxed{
\text{continuous phase diffusion}
+
\text{discrete chirality switching}}
$$

という二つのmemory-loss channelがある。

その結果

$$
\boxed{
\xi_\chi\neq\xi_{\rm spin}}
$$

となりうる。spin correlationを支配するtilted operator、$q_{\rm corr}$、$Q_{\rm peak}$ の詳細な導出は第二近接XYノートに置く。

比較上重要なのは、Isingでは主として**離散欠陥統計**へ閉じるのに対し、XYではその上に**連続位相の累積**が残ることにある。

## 7. finite-$q$ の意味も両模型で異なる

両模型とも

$$
C(r)\sim e^{-r/\xi}\cos(q_{\rm corr}r)
$$

のような振動減衰相関を持ちうるが、その波数の物理的意味は同じではない。

Isingでは

$$
\boxed{
q_{\rm corr}=\text{離散wall・spin配置の相関波数}}
$$

である。

XYでは、局所的に相互作用が選ぶtwist $q_\ast$ と、長距離相関の $q_{\rm corr}$、さらに構造因子・応答の最大位置 $Q_{\rm peak}$ が分かれうる。

$$
\boxed{
q_\ast,\qquad q_{\rm corr},\qquad Q_{\rm peak}}
$$

の分離自体はXY固有の詳細なので、ここでは「finite-$q$ の起源がIsingとXYで異なる」という比較だけを残す。

## 8. 比較ノートと個別ノートの役割分担

この比較ノートに残すのは、二つの模型を同じ軸で読むための辞書である。

| 内容 | 比較ノート | 第二近接XYノート |
| --- | --- | --- |
| Ising / XY の局所変数対応 | 詳細 | — |
| 平均場・Bethe・transferの役割比較 | 詳細 | XY側のみ必要箇所 |
| $q_\ast$ の導出 | 結果のみ | 詳細 |
| 長波長 $\phi^4$ 場の導出 | 結果のみ | 詳細 |
| kink profile / $E_{\rm k}$ | scalingのみ | 詳細 |
| XY transfer operator | 比較に必要な定義のみ | 詳細 |
| tilted operator | 概念のみ | 詳細 |
| $q_{\rm corr}$、$Q_{\rm peak}$ | 区別のみ | 詳細 |
| finite-$Q$ 外場応答 | 比較上の意味のみ | 詳細 |

この分離によって、第二近接XYノートは

$$
\boxed{
\text{XY模型そのものを深く解くノート}}
$$

として残り、比較ノートは

$$
\boxed{
\text{IsingとXYを同じ統計力学的な三解像度で読むノート}}
$$

として役割が分かれる。

最終的な対応は

$$
\boxed{
\text{defect / texture}
\longrightarrow
\text{local transition probability}
\longrightarrow
\text{transfer spectral gap}}
$$

である。Isingではこの連鎖がほぼ離散Markov統計だけで閉じる。XYではその上にcontinuous phase accumulationが残るため、chirality memoryとspin memoryが分裂する。
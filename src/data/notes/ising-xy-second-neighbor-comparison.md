---
title: "1次元一様第二近接 cosine スピン系 — Z2・U(1)を三つの解像度で見る"
summary: "第二近接Ising鎖とXY鎖を、平均場・saddle point、Bethe/cavity、厳密transfer spectrumという三つの解像度で比較する。個別模型の導出は各専用ノートに置き、このノートでは欠陥の形、局所遷移確率、長距離相関の固有値がどう対応するかだけを整理する。"
publishedAt: 2026-09-13T22:45:00+09:00
updatedAt: 2026-09-19
area: "Physics"
topics: ["Ising model", "XY model", "second-neighbor interaction", "chirality"]
status: growing
system:
  dimension: 1
  spatial: uniform
  range: R2
  interaction: cosine
  symmetry: [Z2, U(1)]
  mechanics: classical
  role: comparison
---

第二近接Ising鎖と第二近接XY鎖は、どちらも厳密にはtransfer objectで扱える。それでも平均場やBethe/cavityを見る意味は残る。三つの方法は単なる精度の階層ではなく、同じ統計構造の異なる断面を見せる。

$$
\boxed{
\text{平均場・saddle point}
\longleftrightarrow
\text{Bethe / cavity}
\longleftrightarrow
\text{exact transfer spectrum}}
$$

このノートでは比較だけを扱う。個別模型の詳細は

- [第二近接Isingノート](/notes/ising-r2-transfer-matrix)
- [第二近接XYノート](/notes/xy-chain-second-neighbor)

に分ける。

以下では

$$
\beta\equiv\frac{1}{k_{\mathrm B}T}
$$

とする。

## 比較座標

$$
\boxed{
d=1,\qquad
\text{uniform},\qquad
R=2
}
$$

を固定し、

$$
\boxed{
Z_2
\longleftrightarrow
U(1)
}
$$

を比較する。模型そのものの導出ではなく、

$$
\text{defect / texture}
\leftrightarrow
\text{local transition probability}
\leftrightarrow
\text{transfer spectrum}
$$

という information filter 間の対応を読む。

## 1. 共通骨格は局所相対変数の相互作用化にある

Isingでは

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

とおけば

$$
\boxed{
H_{\rm XY}
=-J_1\sum_i\cos\phi_i
-J_2\sum_i\cos(\phi_i+\phi_{i+1})}
$$

となる。

したがって共通して

$$
\boxed{
\text{independent local variables}
\longrightarrow
\text{interacting local variables}}
$$

が起こる。ただし、Isingでは局所変数が離散wall情報、XYでは連続twist情報である。

## 2. 平均場・saddle pointは「何が記憶を壊すか」を見せる

Isingでは主要な欠陥はdomain wallである。粗視化したbond orderの連続場は書けるが、microscopicなwall自体は格子上の離散欠陥なので、平均場的描像で重要なのはwall costとwall patternである。

XYでは競合領域で

$$
\phi\simeq+q_\ast,
\qquad
\phi\simeq-q_\ast
$$

という二つのchirality sectorが生じ、その間をchirality kinkがつなぐ。

第二近接XYノートで導出した臨界点近傍の結果は

$$
\ell_{\rm k}
\propto
\left(\kappa-\frac14\right)^{-1/2},
$$

$$
E_{\rm k}
\propto
J_1\left(\kappa-\frac14\right)^{3/2}.
$$

ここで平均場が見せるのは相関長の正確な値ではなく

$$
\boxed{
\text{defect barrier}
\longrightarrow
\text{rare switching}}
$$

という機構である。

## 3. Bethe / cavityは「どの頻度で切り替わるか」を見せる

Isingの$\tau_i$表現では

$$
P(\tau_{i+1}|\tau_i)
$$

が2状態の局所遷移確率になる。対称な場合を

$$
P=
\begin{pmatrix}
1-p&p\\
p&1-p
\end{pmatrix}
$$

と書けば

$$
\langle\tau_0\tau_r\rangle=(1-2p)^r,
$$

したがって

$$
\boxed{
\xi_\tau^{-1}=-\ln|1-2p|}
$$

となる。

第二近接Isingは$\tau$表現では1次元最近接Markov鎖なので、この局所確率記述は本質的にexactである。

XYでは連続条件付き分布

$$
P(\phi'|\phi)
$$

を考える。低温で二つのchirality basinへ粗視化すれば、chirality flip probability $p_{\rm flip}$ を定義できる。

希薄switching極限では

$$
\boxed{
\xi_\chi^{-1}
\simeq-\ln(1-2p_{\rm flip})}
$$

であり、$p_{\rm flip}\ll1$なら

$$
\boxed{
\xi_\chi\simeq\frac{1}{2p_{\rm flip}}}
$$

となる。

平均場側のkinkと局所確率は概念的に

$$
\boxed{
p_{\rm flip}
\sim e^{-\beta\Delta F_{\rm k}}}
$$

でつながる。

## 4. transfer spectrumは局所統計を長距離memoryへまとめる

Isingではtransfer matrixの固有値比が相関長を決める。

$$
\boxed{
\xi_\tau^{-1}
=-\ln\left|\frac{\lambda_1}{\lambda_0}\right|}
$$

XYではchirality observableが$\phi\to-\phi$に対してoddなので、最大even固有値$\lambda_0$と最大odd固有値$\lambda_\chi$のsplittingから

$$
\boxed{
\xi_\chi^{-1}
=-\ln\left|\frac{\lambda_\chi}{\lambda_0}\right|}
$$

を得る。

低温で$\lambda_\chi\to\lambda_0$となることは、Bethe側では$p_{\rm flip}\to0$、平均場側ではkink switchingが希薄になることと同じ情報である。

## 5. 三つの解像度は「形・頻度・スペクトル」に分かれる

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

となる。

| 解像度 | Ising | XY |
| --- | --- | --- |
| 平均場・saddle point | wall cost / wall pattern | chirality kink / $E_{\rm k}$ |
| Bethe / cavity | $P(\tau'|\tau)$、$p$ | $P(\phi'|\phi)$、$p_{\rm flip}$ |
| exact transfer | $\lambda_1/\lambda_0$ | $\lambda_\chi/\lambda_0$ |

したがって中心は

$$
\boxed{
\text{形}
\longleftrightarrow
\text{頻度}
\longleftrightarrow
\text{長距離スペクトル}}
$$

である。

## 6. XYだけはchirality memoryでspin memoryが閉じない

Isingでは離散的な局所変数のMarkov統計がspin memoryへかなり直接につながる。

一方XYでは

$$
\theta_r-\theta_0
=
\sum_{i=0}^{r-1}\phi_i
$$

なので、chirality switching以外にcontinuous phase accumulationが残る。

したがって

$$
\boxed{
\text{continuous phase diffusion}
+
\text{discrete chirality switching}}
$$

という二つのmemory-loss channelがあり、一般に

$$
\boxed{
\xi_\chi\neq\xi_{\rm spin}}
$$

となりうる。

この先のtilted operator、$q_{\rm corr}$、$Q_{\rm peak}$は第二近接XYノートに置く。

## 7. finite-$q$の詳細は個別ノートに分ける

Isingでは、複素transfer eigenvalueから現れる$q_{\rm spec}$と、感受率最大の$q_\chi$が別の量になる。Stephenson disorder lineとLifshitz-like lineの解析は第二近接Isingノートに置く。

XYでは、局所preferred twist $q_\ast$、実空間相関波数$q_{\rm corr}$、構造因子・応答最大$Q_{\rm peak}$が分かれうる。その導出は第二近接XYノートに置く。

比較上残すべき差は

$$
\boxed{
\text{Ising}:\ finite\text{-}q\text{は離散配置の相関構造}}
$$

に対して

$$
\boxed{
\text{XY}:\ finite\text{-}q\text{はlocal twistとswitchingの合成}}
$$

という点である。

## 8. 三本のノートの役割

| 内容 | 第二近接Ising | 第二近接XY | この比較ノート |
| --- | --- | --- | --- |
| 模型の詳細導出 | 詳細 | 詳細 | 最小限 |
| domain wall / twistの物理 | Ising側を詳細 | XY側を詳細 | 対応だけ |
| disorder / Lifshitz-like line | 詳細 | — | 意味だけ |
| $q_\ast$、長波長$\phi^4$場 | — | 詳細 | 結果だけ |
| chirality kink | — | 詳細 | scalingだけ |
| Bethe / cavityの位置づけ | 補助 | 補助 | 詳細 |
| transfer spectrum | Ising側を詳細 | XY側を詳細 | 対応だけ |
| finite-$q$ response | Ising側を詳細 | XY側を詳細 | 起源の違いだけ |

三本を分ける基準は、**個別模型の導出は個別ノート、方法論上の対応は比較ノート**である。

この分離によって、第二近接Isingノートはwall statisticsとdisorder/Lifshitz構造、第二近接XYノートはtwist・chirality・phase memory、比較ノートは

$$
\boxed{
\text{defect / texture}
\longrightarrow
\text{local transition probability}
\longrightarrow
\text{transfer spectral gap}}
$$

という共通辞書だけを担当する。
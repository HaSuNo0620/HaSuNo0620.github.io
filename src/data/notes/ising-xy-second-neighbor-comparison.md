---
title: "1次元スピン模型 — 第二近接相互作用で見るIsingとXYの共通構造"
summary: "最近接では独立だった局所変数が第二近接相互作用によって相互作用し始めるという共通構造をIsing鎖とXY鎖で比較する。domain wallとphase increment、有限波数相関、transfer spectrum、空間変調外場への応答、XY固有のchirality選択を整理する。"
publishedAt: 2026-09-13T22:45:00+09:00
updatedAt: 2026-09-14
area: "Physics"
topics: ["statistical mechanics", "Ising model", "XY model", "second-neighbor interaction", "frustration", "correlation", "wave number", "memory", "linear response"]
status: growing
---

最近接のIsing鎖とXY鎖では、零外場の自然な局所相対変数が独立だった。

$$
\tau_i=s_is_{i+1}
$$

と

$$
\phi_i=\theta_{i+1}-\theta_i
$$

である。

第二近接を入れると、両方で

$$
\boxed{
\text{independent local variables}
\longrightarrow
\text{interacting local variables}}
$$

が起こる。

共通するのは「有限記憶化」で、その現れ方は離散wallと連続twistで分かれる。

## 1. 第二近接は局所相対変数どうしを結ぶ

Isingでは

$$
H_{\rm I}
=-J_1\sum_i s_is_{i+1}
-J_2\sum_i s_is_{i+2}
$$

に対して

$$
s_is_{i+2}=\tau_i\tau_{i+1}
$$

なので

$$
\boxed{
H_{\rm I}
=-J_1\sum_i\tau_i
-J_2\sum_i\tau_i\tau_{i+1}}
$$

となる。

XYでは

$$
H_{\rm XY}
=-J_1\sum_i\cos(\theta_{i+1}-\theta_i)
-J_2\sum_i\cos(\theta_{i+2}-\theta_i)
$$

と

$$
\theta_{i+2}-\theta_i=\phi_i+\phi_{i+1}
$$

から

$$
\boxed{
H_{\rm XY}
=-J_1\sum_i\cos\phi_i
-J_2\sum_i\cos(\phi_i+\phi_{i+1})}
$$

となる。

$$
\boxed{
\text{independent noise in space}
\longrightarrow
\text{correlated noise in space}}
$$

という構造は同じである。

## 2. 離散wallは配置を変え、連続twistは回転率そのものを選べる

Isingの $\tau_i=\pm1$ は離散変数なので、第二近接はwall配置の統計を組み替える。

XYの $\phi_i$ は連続角度なので、第二近接は

$$
\phi_i\simeq q_\ast
$$

という局所回転率そのものを選べる。

$$
\boxed{\text{Ising}:\ \text{wall arrangement is reorganized}}
$$

$$
\boxed{\text{XY}:\ \text{local twist itself is selected}}
$$

という違いになる。

## 3. finite-$q$ correlation は共通しても $q$ の意味は同じではない

両模型とも

$$
C(r)\sim e^{-r/\xi}\cos(q_{\rm corr}r+\delta)
$$

のような振動減衰相関を持ちうる。

Isingでは $q_{\rm corr}$ は離散スピン・wall配置の相関波数として transfer spectrum から現れる。

XYでは

$$
e(q)=-J_1\cos q-J_2\cos2q
$$

の最小化から

$$
\cos q_\ast=-\frac{J_1}{4J_2}
$$

というfinite twistが直接選ばれる。

$$
\boxed{\text{Ising}:\ q_{\rm corr}\text{ は離散配置の相関波数}}
$$

$$
\boxed{\text{XY}:\ q_\ast\text{ は局所回転率そのもの}}
$$

という区別を残しておく必要がある。

## 4. 記憶の運び方は interacting walls と drifting phase increments に分かれる

最近接Isingでは rare wall が記憶を反転させた。第二近接ではwall列自体が有限記憶を持つ。

最近接XYでは phase diffusion が記憶を失わせた。finite twistが選ばれると

$$
\theta_r-\theta_0
\simeq q_\ast r+\text{fluctuation}
$$

となる。

$$
\boxed{\text{Ising}:\ \text{interacting walls}}
$$

に対して

$$
\boxed{\text{XY}:\ \text{drifting, correlated phase increments}}
$$

である。

## 5. XYでは continuous phase の上に discrete chirality が増える

finite twist状態では

$$
+q_\ast
\quad\text{と}\quad
-q_\ast
$$

が縮退する。

局所chiralityは

$$
\kappa_i^{\rm ch}
\sim\sin(\theta_{i+1}-\theta_i)
$$

で区別できる。

したがって第二近接XYは

$$
\boxed{
\text{continuous phase mode}
+\text{discrete chirality mode}}
$$

を同時に持つ。

これはIsingの離散spin自由度と同一ではない。XYでは連続角度場の上に、回転方向という追加の二値自由度が生じる。

## 6. transfer object は一つ前の局所状態を記憶する

第二近接では現在のサイトだけでは次の局所統計を決められない。

Isingでは $(s_i,s_{i+1})$ を状態とする4×4 transfer matrix、または $\tau_i$ のMarkov過程が自然になる。

XYでは

$$
\mathcal T(\phi,\phi')
=\exp\left[
\frac{\beta J_1}{2}(\cos\phi+\cos\phi')
+\beta J_2\cos(\phi+\phi')
\right]
$$

という積分作用素になる。

$$
\boxed{
\text{interaction range grows}
\longrightarrow
\text{state must carry memory}
\longrightarrow
\text{transfer object becomes larger}}
$$

という骨格は共通している。

## 7. spectrum は decay と oscillation を別々に持つ

概念的に支配modeを

$$
\lambda_\ast=|\lambda_\ast|e^{iq_{\rm corr}}
$$

と書けば

$$
C(r)
\sim
\left|\frac{\lambda_\ast}{\lambda_0}\right|^r
\cos(q_{\rm corr}r+\delta).
$$

したがって

$$
\boxed{
|\lambda_\ast/\lambda_0|\longrightarrow\xi,
\qquad
\arg\lambda_\ast\longrightarrow q_{\rm corr}}
$$

となる。

第二近接では「どれだけ速く忘れるか」と「どんな空間周期を保ちながら忘れるか」が別の情報になる。

XYではスピン相関を測るために、平衡transfer operatorに位相因子を組み込んだtilted operatorが必要になる点がIsingと異なる。

## 8. 外場応答の自然変数は $(Q-q_{\rm corr})\xi$ になる

最近接強磁性鎖では相関の中心が $q=0$ だったため、空間変調外場は $Q\xi$ で整理できた。

finite-$q$ structureが生じると基準点自体が移る。

$$
\boxed{(Q-q_{\rm corr})\xi}
$$

が自然なdetuningになる。

$$
C(r)\sim e^{-|r|/\xi}\cos(q_{\rm corr}r)
$$

なら概念的に

$$
S(Q)
\propto
\frac{\xi}{1+\xi^2(Q-q_{\rm corr})^2}
+
\frac{\xi}{1+\xi^2(Q+q_{\rm corr})^2}.
$$

応答ピークは

$$
\boxed{Q\simeq\pm q_{\rm corr}}
$$

に現れ、幅はおおよそ $\xi^{-1}$ になる。

問題は「外場が長波長か短波長か」から、**外場波数が内部構造波数にどれだけphase-matchしているか**へ変わる。

## 9. Isingでは scalar modulated field が離散配置をprobeする

$$
H_h^{\rm I}
=-\sum_i h_Q\cos(Qi)s_i
$$

に対して

$$
\delta m(Q)=\chi_{\rm I}(Q)h_Q
$$

であり

$$
\chi_{\rm I}(Q)
=\beta\sum_r e^{-iQr}\langle s_0s_r\rangle.
$$

finite-$q$ correlationがあれば、$\chi_{\rm I}(Q)$ もその近くで大きくなる。

ここで $Q$ は離散spin配置の相関波数に照準を合わせる量であり、局所spinが少しずつ回転しているわけではない。

## 10. XYでは rotating field が pitch と chirality の両方に直接結合する

固定方向の変調場でも

$$
H_h^x
=-\sum_i h_Q\cos(Qi)\cos\theta_i
$$

として $Q\simeq\pm q_{\rm corr}$ をprobeできる。

さらにXYでは

$$
\mathbf h_i=h(\cos Qi,\sin Qi)
$$

という rotating field が使える。

$$
\boxed{
H_h^{\rm rot}
=-h\sum_i\cos(\theta_i-Qi)}
$$

となるので、内部構造

$$
\theta_i\simeq q_\ast i+\theta_0
$$

に対して

$$
\boxed{Q=q_\ast}
$$

が直接的なphase-matching条件になる。

しかも $Q=+q_\ast$ と $Q=-q_\ast$ は回転方向が逆なので、chiralityまで選別できる。

$$
\boxed{
\text{XY rotating field}
:\ \text{pitch}+\text{chiralityを同時にprobe}}
$$

という情報はIsingにはない。

## 11. finite-$q$ response の共通部分と模型固有部分

| 観点 | Ising | XY |
| --- | --- | --- |
| 最近接の局所変数 | $\tau_i=s_is_{i+1}$ | $\phi_i=\theta_{i+1}-\theta_i$ |
| 第二近接での結合 | $\tau_i\tau_{i+1}$ | $\cos(\phi_i+\phi_{i+1})$ |
| finite-$q$ の意味 | 離散配置の相関波数 | 局所回転率に対応可能 |
| probe | scalar modulated field | amplitude modulation / rotating field |
| resonance | $Q\simeq q_{\rm corr}$ | $Q\simeq q_{\rm corr}\simeq q_\ast$ |
| $Q$ の符号 | chirality情報を通常持たない | chiralityを選べる |
| peak幅 | $\sim\xi^{-1}$ | $\sim\xi^{-1}$ |

共通して

$$
\boxed{
\text{finite-}q\text{ correlation}
\longrightarrow
\text{finite-}Q\text{ response peak}}
$$

だが、probeが何にphase-matchしているかは違う。

## 12. 第二近接が作るのは internal spatial carrier である

最近接では $Q=0$ が基準だったため

$$
Q\xi
$$

で十分だった。

第二近接では

$$
\boxed{
Q\xi
\longrightarrow
(Q-q_{\rm corr})\xi}
$$

となる。

これは単なる相関長の修正ではなく、系が**内部のcarrier wave**を持つようになったことを表している。

Isingではそのcarrierはwall・spin配置の相関構造として、XYでは局所twistとchiralityとして現れる。

同じ「有限記憶化」が、離散系ではwall structure、連続系ではtwist structureになり、その違いがfinite-$Q$外場への応答に直接現れる。

---
title: "1次元スピン模型 — 第二近接相互作用で見るIsingとXYの共通構造"
summary: "最近接では独立だった局所変数が、第二近接相互作用によって相互作用し始めるという共通構造をIsing鎖とXY鎖で比較する。domain wallとphase increment、有限波数相関、構造波数の選択、chiralityの違いを整理する。"
publishedAt: 2026-09-13T22:45:00+09:00
updatedAt: 2026-09-13
area: "Physics"
topics: ["statistical mechanics", "Ising model", "XY model", "second-neighbor interaction", "frustration", "correlation", "wave number", "memory"]
status: growing
---

最近接の1次元Ising鎖とXY鎖では、零外場の開鎖において自然な局所相対変数が独立だった。

Isingでは

$$
\tau_i=s_is_{i+1}
$$

というbond変数、XYでは

$$
\phi_i=\theta_{i+1}-\theta_i
$$

という角度差である。

第二近接相互作用を入れると、両模型でこの独立性が壊れる。

このノートで見たいのは

$$
\boxed{
\text{independent local variables}
\longrightarrow
\text{interacting local variables}
}
$$

という共通構造と、その先でIsingとXYがどこから分かれるかである。

## 1. 最近接では局所相対変数が独立だった

最近接Ising鎖

$$
H_{\rm I}^{(1)}=-J_1\sum_i s_is_{i+1}
$$

は

$$
H_{\rm I}^{(1)}=-J_1\sum_i\tau_i
$$

と書ける。したがって零外場の開鎖では各 $\tau_i$ は独立である。

最近接XY鎖

$$
H_{\rm XY}^{(1)}
=-J_1\sum_i\cos(\theta_{i+1}-\theta_i)
$$

も

$$
H_{\rm XY}^{(1)}=-J_1\sum_i\cos\phi_i
$$

となり、各 $\phi_i$ は独立である。

したがって最近接では

$$
\boxed{
\text{Ising}:\ \text{independent wall variables}
}
$$

$$
\boxed{
\text{XY}:\ \text{independent phase increments}
}
$$

という対応があった。

## 2. 第二近接は隣り合う局所変数を直接結びつける

Isingに第二近接相互作用を加えると

$$
H_{\rm I}
=-J_1\sum_i s_is_{i+1}
-J_2\sum_i s_is_{i+2}.
$$

ここで

$$
s_is_{i+2}
=(s_is_{i+1})(s_{i+1}s_{i+2})
=\tau_i\tau_{i+1}
$$

だから

$$
\boxed{
H_{\rm I}
=-J_1\sum_i\tau_i
-J_2\sum_i\tau_i\tau_{i+1}
}
$$

となる。

第二近接項はdomain wall変数どうしの最近接相互作用になる。

一方XYでは

$$
H_{\rm XY}
=-J_1\sum_i\cos(\theta_{i+1}-\theta_i)
-J_2\sum_i\cos(\theta_{i+2}-\theta_i)
$$

であり

$$
\theta_{i+2}-\theta_i
=\phi_i+\phi_{i+1}
$$

だから

$$
\boxed{
H_{\rm XY}
=-J_1\sum_i\cos\phi_i
-J_2\sum_i\cos(\phi_i+\phi_{i+1})
}
$$

となる。

したがって第二近接は両模型で

$$
\boxed{
\text{隣り合う局所相対変数を相互作用させる}
}
$$

という同じ役割を果たす。

## 3. 共通する変化は「独立過程」から「有限記憶過程」への移行である

最近接Isingでは、$\tau_i$ は独立な符号変数だった。第二近接では $\tau_i$ と $\tau_{i+1}$ が結びつくため、wall配置に有限の空間記憶が生じる。

最近接XYでは、$\phi_i$ は独立な角度増分だった。第二近接では $\phi_i$ と $\phi_{i+1}$ が結びつくため、phase increment自身に相関が生じる。

したがって共通するのは

$$
\boxed{
\text{independent noise in space}
\longrightarrow
\text{correlated noise in space}
}
$$

という変化である。

Isingでは符号欠陥列が、XYでは角度増分列が、一段のMarkov的な記憶を持つようになる。

## 4. しかし局所変数の性質は離散と連続で根本的に違う

Isingの $\tau_i$ は

$$
\tau_i=\pm1
$$

という離散変数である。したがって第二近接相互作用が変えるのは、wallが隣接して存在しやすいか、離れて存在しやすいかという**欠陥配置の統計**である。

一方XYの $\phi_i$ は連続角度である。第二近接相互作用は、単に「欠陥同士を引きつける・反発させる」のではなく

$$
\phi_i\simeq q_\ast
$$

という**有限の局所回転率そのもの**を選べる。

したがって

$$
\boxed{
\text{Ising}:\ \text{wall arrangement is reorganized}
}
$$

に対して

$$
\boxed{
\text{XY}:\ \text{local twist itself is selected}
}
$$

という違いがある。

## 5. 有限波数構造は両方に現れるが、その起源は同じではない

第二近接相互作用によって、両模型とも単調な相関から振動相関へ進む領域を持ちうる。

一般に

$$
C(r)
\sim
e^{-r/\xi}\cos(q_\ast r+\delta)
$$

という形が現れれば、$\xi$ は記憶距離、$q_\ast$ は空間構造の波数を表す。

ただし $q_\ast$ の意味は模型ごとに異なる。

Isingでは、有限波数はtransfer matrixの固有値構造や競合するwall配置から生じる。スピン自身は $\pm1$ しか取らないので、局所的な「少しずつ回転する角度」は存在しない。

XYでは、基底状態レベルですでに

$$
e(q)=-J_1\cos q-J_2\cos2q
$$

を最小化して

$$
\cos q_\ast=-\frac{J_1}{4J_2}
$$

という有限twistが直接選ばれる。

したがって

$$
\boxed{
\text{Ising}:\ q_\ast\text{ は離散配置の相関波数}
}
$$

$$
\boxed{
\text{XY}:\ q_\ast\text{ は局所回転率そのもの}
}
$$

と読むのがよい。

## 6. Isingではwall、XYではdriftという違いが残る

最近接Isingでは

$$
\text{rare wall}
$$

が空間記憶を壊していた。第二近接ではwall同士が相互作用し、欠陥列の配置そのものに構造が生じる。

最近接XYでは

$$
\text{phase diffusion}
$$

が空間記憶を壊していた。第二近接で有限twistが選ばれると

$$
\theta_r-\theta_0
\simeq q_\ast r+\text{fluctuation}
$$

となり、phase diffusionにdriftが加わる。

したがって第二近接への拡張は

$$
\boxed{
\text{Ising}:\ \text{interacting walls}
}
$$

に対して

$$
\boxed{
\text{XY}:\ \text{drifting, correlated phase increments}
}
$$

という対比になる。

## 7. XYには第二近接で新たにchiralityが現れる

XYの有限twist状態では

$$
q_\ast
\quad\text{と}\quad
-q_\ast
$$

が縮退する。

つまり時計回りと反時計回りという二つのchiralityが生まれる。

局所的には

$$
\kappa_i^{\rm ch}
\sim\sin(\theta_{i+1}-\theta_i)
$$

で区別できる。

この自由度は最近接XYには存在しなかった。また、通常のIsingスピン $s_i=\pm1$ のdomain wallとも同じではない。

興味深いのは、第二近接XYが

$$
\boxed{
\text{continuous phase mode}
+\text{discrete chirality mode}
}
$$

を同時に持つことである。

したがって有限温度では、位相揺らぎによる相関喪失とchirality wallによる相関喪失を分けて考える必要がある。

## 8. transferの構造も同じ方向に複雑化する

最近接では、Isingは $2\times2$ transfer matrix、XYはFourier対角なtransfer operatorであり、局所変数の独立性が直接見えていた。

第二近接では、どちらも「一つ前の局所状態を覚える」必要が生じる。

Isingでは $(s_i,s_{i+1})$ を状態として持つ $4\times4$ transfer matrix、あるいは $\tau_i$ の二状態Markov過程として扱える。

XYでは角度差 $\phi_i$ を状態として持つ積分作用素

$$
\mathcal T(\phi,\phi')
=
\exp\left[
\frac{\beta J_1}{2}(\cos\phi+\cos\phi')
+\beta J_2\cos(\phi+\phi')
\right]
$$

が自然になる。

したがって共通するのは

$$
\boxed{
\text{interaction range grows}
\Longrightarrow
\text{state must carry memory}
\Longrightarrow
\text{transfer object becomes larger}
}
$$

という構造である。

## 9. スペクトルからは減衰長と構造波数を分けて読む

第二近接では、長距離相関を一つの正の固有値比だけで表せない場合がある。

概念的には支配モードを

$$
\lambda_\ast
=|\lambda_\ast|e^{iq_\ast}
$$

と書けば

$$
C(r)
\sim
\left|\frac{\lambda_\ast}{\lambda_0}\right|^r
\cos(q_\ast r+\delta)
$$

となる。

したがって

$$
\boxed{
|\lambda_\ast/\lambda_0|
\longrightarrow\xi
}
$$

と

$$
\boxed{
\arg\lambda_\ast
\longrightarrow q_\ast
}
$$

という二つの情報を分けて読む必要がある。

IsingでもXYでも、この「decay + oscillation」という読み方は共通する。ただし、XYでは元のtransfer operatorが実対称でも、スピン相関を測るためには位相因子を含むtilted operatorを考える必要がある点に注意がいる。

## 10. 第二近接を入れたときの対応表

| 観点 | Ising | XY |
| --- | --- | --- |
| 最近接の局所変数 | $\tau_i=s_is_{i+1}$ | $\phi_i=\theta_{i+1}-\theta_i$ |
| 最近接での性質 | 独立wall | 独立phase increment |
| 第二近接で生じる結合 | $\tau_i\tau_{i+1}$ | $\cos(\phi_i+\phi_{i+1})$ |
| 主な変化 | wall配置が相関 | twist増分が相関 |
| finite-$q$ の意味 | 離散配置の相関波数 | 局所回転率 |
| 新しい自由度 | wall interaction | chirality $\pm q_\ast$ |
| 長距離相関 | decay + oscillation | drift + diffusion + possible chirality switching |

## 11. 比較して見えてくるもの

第二近接を入れたとき、IsingとXYは別々の方向へ複雑化するように見える。しかし根元には共通した構造がある。

$$
\boxed{
\text{interaction range}
\uparrow
\Longrightarrow
\text{local relative variables interact}
\Longrightarrow
\text{spatial memory acquires internal structure}
}
$$

最近接では「1 stepごとの記憶損失率」だけで十分だった。第二近接では、局所変数自身が前の状態を覚えるため、相関長に加えて構造波数や内部モードが必要になる。

ただし、Isingではその内部構造は離散的なwall配置として現れ、XYでは連続的なtwistとchiralityとして現れる。

したがって第二近接比較の中心は

$$
\boxed{
\text{同じ“有限記憶化”が、離散系ではwall構造、連続系ではtwist構造として現れる}
}
$$

という点にある。

---
title: "1次元スピン模型 — 第二近接相互作用で見るIsingとXYの共通構造"
summary: "最近接では独立だった局所変数が第二近接相互作用によって相互作用し始めるという共通構造をIsing鎖とXY鎖で比較する。domain wallとphase increment、有限波数相関、transfer spectrum、空間変調外場への応答、XY固有のchirality選択を整理する。"
publishedAt: 2026-09-13T22:45:00+09:00
updatedAt: 2026-09-13
area: "Physics"
topics: ["statistical mechanics", "Ising model", "XY model", "second-neighbor interaction", "frustration", "correlation", "wave number", "memory", "linear response"]
status: growing
---

最近接の1次元Ising鎖とXY鎖では、零外場の開鎖において自然な局所相対変数が独立だった。

Isingでは

$$
\tau_i=s_is_{i+1},
$$

XYでは

$$
\phi_i=\theta_{i+1}-\theta_i
$$

である。

第二近接相互作用を入れると、両模型でこの独立性が壊れる。

$$
\boxed{
\text{independent local variables}
\longrightarrow
\text{interacting local variables}
}
$$

このノートでは、この共通構造が相関・構造波数・外場応答にどう現れ、その先でIsingとXYがどこから分かれるかを見る。

## 1. 最近接では局所相対変数が独立だった

最近接Ising鎖

$$
H_{\rm I}^{(1)}=-J_1\sum_i s_is_{i+1}
$$

は

$$
H_{\rm I}^{(1)}=-J_1\sum_i\tau_i
$$

と書ける。

最近接XY鎖

$$
H_{\rm XY}^{(1)}
=-J_1\sum_i\cos(\theta_{i+1}-\theta_i)
$$

も

$$
H_{\rm XY}^{(1)}=-J_1\sum_i\cos\phi_i
$$

となる。

したがって零外場の開鎖では

$$
\boxed{\text{Ising}:\ \text{independent wall variables}}
$$

$$
\boxed{\text{XY}:\ \text{independent phase increments}}
$$

という対応があった。

## 2. 第二近接は隣り合う局所変数を直接結びつける

Isingでは

$$
H_{\rm I}
=-J_1\sum_i s_is_{i+1}
-J_2\sum_i s_is_{i+2}.
$$

$s_is_{i+2}=\tau_i\tau_{i+1}$ なので

$$
\boxed{
H_{\rm I}
=-J_1\sum_i\tau_i
-J_2\sum_i\tau_i\tau_{i+1}
}
$$

となる。

XYでは

$$
H_{\rm XY}
=-J_1\sum_i\cos(\theta_{i+1}-\theta_i)
-J_2\sum_i\cos(\theta_{i+2}-\theta_i),
$$

$$
\theta_{i+2}-\theta_i=\phi_i+\phi_{i+1}
$$

より

$$
\boxed{
H_{\rm XY}
=-J_1\sum_i\cos\phi_i
-J_2\sum_i\cos(\phi_i+\phi_{i+1})
}
$$

となる。

したがって共通する変化は

$$
\boxed{
\text{independent noise in space}
\longrightarrow
\text{correlated noise in space}
}
$$

である。

## 3. ただし離散wallと連続twistでは意味が違う

Isingの $\tau_i=\pm1$ は離散変数である。第二近接相互作用が変えるのは、wallがどのような間隔・組み合わせで現れやすいかという欠陥配置の統計である。

一方XYの $\phi_i$ は連続角度である。第二近接相互作用は

$$
\phi_i\simeq q_\ast
$$

という有限の局所回転率そのものを選べる。

したがって

$$
\boxed{\text{Ising}:\ \text{wall arrangement is reorganized}}
$$

に対して

$$
\boxed{\text{XY}:\ \text{local twist itself is selected}}
$$

という違いがある。

## 4. 有限波数構造は共通するが、構造波数の意味は異なる

第二近接相互作用によって、両模型とも

$$
C(r)\sim e^{-r/\xi}\cos(q_{\rm corr}r+\delta)
$$

のような振動減衰相関を持ちうる。

ここで $\xi$ は記憶距離、$q_{\rm corr}$ は相関の構造波数である。

Isingでは $q_{\rm corr}$ は離散的なスピン・wall配置の相関波数としてtransfer spectrumから現れる。局所スピン自身が少しずつ回転しているわけではない。

XYでは競合領域で

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
\boxed{\text{Ising}:\ q_{\rm corr}\text{ は離散配置の相関波数}}
$$

$$
\boxed{\text{XY}:\ q_\ast\text{ は局所回転率そのもの}}
$$

と区別する必要がある。

低温の単一chirality sectorではXYの $q_{\rm corr}$ は $q_\ast$ に近づくが、有限温度では両者を最初から同一視しない方がよい。

## 5. 最近接から第二近接で、記憶の運び方も変わる

最近接Isingでは rare wall が空間記憶を反転させた。第二近接ではwall同士が相互作用し、欠陥列そのものに有限記憶が生じる。

最近接XYでは phase diffusion が記憶を失わせた。第二近接で有限twistが選ばれると

$$
\theta_r-\theta_0
\simeq q_\ast r+\text{fluctuation}
$$

となり、phase diffusionにdriftが加わる。

したがって

$$
\boxed{\text{Ising}:\ \text{interacting walls}}
$$

に対して

$$
\boxed{\text{XY}:\ \text{drifting, correlated phase increments}}
$$

となる。

## 6. XYにはchiralityという新しい離散自由度も現れる

XYの有限twist状態では

$$
+q_\ast
\quad\text{と}\quad
-q_\ast
$$

が縮退する。

局所chiralityは

$$
\kappa_i^{\rm ch}\sim\sin(\theta_{i+1}-\theta_i)
$$

で区別できる。

したがって第二近接XYは

$$
\boxed{
\text{continuous phase mode}
+\text{discrete chirality mode}
}
$$

を同時に持つ。

Isingにも離散自由度はあるが、これはXYのchiralityと同じものではない。XYでは連続角度場の上に、回転方向という追加の二値自由度が生まれる。

## 7. transfer objectは「一つ前の局所状態」を覚えるようになる

第二近接では、どちらも現在のサイトだけでは次の統計を決められない。

Isingでは $(s_i,s_{i+1})$ を状態として持つ $4\times4$ transfer matrix、あるいは $\tau_i$ の二状態Markov過程が自然になる。

XYでは角度差を状態として

$$
\mathcal T(\phi,\phi')
=
\exp\left[
\frac{\beta J_1}{2}(\cos\phi+\cos\phi')
+\beta J_2\cos(\phi+\phi')
\right]
$$

という積分作用素を使える。

したがって

$$
\boxed{
\text{interaction range grows}
\Longrightarrow
\text{state must carry memory}
\Longrightarrow
\text{transfer object becomes larger}
}
$$

という構造は共通する。

## 8. スペクトルから減衰長と構造波数を分けて読む

第二近接では「どれだけ速く忘れるか」だけでなく、「どんな空間周期を保ちながら忘れるか」が必要になる。

概念的に支配モードを

$$
\lambda_\ast=|\lambda_\ast|e^{iq_{\rm corr}}
$$

と書けるなら

$$
C(r)
\sim
\left|\frac{\lambda_\ast}{\lambda_0}\right|^r
\cos(q_{\rm corr}r+\delta).
$$

したがって

$$
\boxed{
|\lambda_\ast/\lambda_0|\to\xi,
\qquad
\arg\lambda_\ast\to q_{\rm corr}
}
$$

という二つの情報を分けて読む必要がある。

XYでは元の平衡transfer operatorが実対称でも、スピン相関を測るには位相因子を含むtilted operatorを考える必要がある点に注意する。

## 9. 外場応答では $q\xi$ ではなく $(Q-q_{\rm corr})\xi$ が自然になる

最近接強磁性鎖では相関ピークが $q=0$ にあったので、空間変調外場に対する応答は $Q\xi$ で整理できた。

第二近接で内部構造波数 $q_{\rm corr}$ が生まれると、基準点そのものが $Q=0$ から移る。

外場波数を $Q$ とすると、本質的なのは

$$
\boxed{
(Q-q_{\rm corr})\xi
}
$$

である。

つまり問題は「外場が短波長か長波長か」ではなく、

$$
\boxed{
\text{外場波数が系自身の構造波数にどれだけphase-matchしているか}
}
$$

へ変わる。

もし

$$
C(r)\sim e^{-|r|/\xi}\cos(q_{\rm corr}r)
$$

なら、そのFourier変換は概念的に

$$
S(Q)
\propto
\frac{\xi}{1+\xi^2(Q-q_{\rm corr})^2}
+
\frac{\xi}{1+\xi^2(Q+q_{\rm corr})^2}
$$

となる。

したがって応答ピークは

$$
\boxed{Q\simeq\pm q_{\rm corr}}
$$

に現れ、ピーク幅はおおよそ $\xi^{-1}$ になる。

## 10. Isingでは変調スカラー場が構造波数をprobeする

Isingに空間変調磁場

$$
H_h^{\rm I}=-\sum_i h_i s_i,
\qquad
h_i=h_Q\cos(Qi)
$$

を加える。

線形応答では

$$
\delta m(Q)=\chi_{\rm I}(Q)h_Q,
$$

零外場なら fluctuation-dissipation relation により

$$
\chi_{\rm I}(Q)
=\beta\sum_r e^{-iQr}\langle s_0s_r\rangle.
$$

したがって第二近接によってスピン相関が有限 $q_{\rm corr}$ を持てば、$\chi_{\rm I}(Q)$ もその近くで大きくなる。

つまり外場は、wall配置の内部構造を逆空間から読み出すprobeになる。

ただしIsingでは $s_i=\pm1$ しかないため、$Q$ はあくまで**離散スピン配置の相関波数に合わせる量**であり、局所スピンが角度 $Q$ ずつ回転しているわけではない。

## 11. XYでは固定方向の変調場に加えて「回転外場」が使える

XYにも固定 $x$ 方向の変調外場

$$
H_h^{x}
=-\sum_i h_Q\cos(Qi)\cos\theta_i
$$

を加えれば、$\chi_{xx}(Q)$ は $Q\simeq\pm q_{\rm corr}$ で大きくなる。

しかしXYでは、さらに外場ベクトルそのものを回転させられる。

$$
\mathbf h_i
=h(\cos Qi,\sin Qi)
$$

とすれば

$$
\boxed{
H_h^{\rm rot}
=-h\sum_i\cos(\theta_i-Qi)
}
$$

である。

内部構造が

$$
\theta_i\simeq q_\ast i+\theta_0
$$

なら、$Q=q_\ast$ の外場は全サイトでほぼ一定の位相差を保つ。

したがってXYでは

$$
\boxed{Q=q_\ast}
$$

が文字どおり**回転外場と内部螺旋のphase-matching条件**になる。

さらに $Q=+q_\ast$ と $Q=-q_\ast$ は回転方向が逆なので、回転外場はchiralityまで選別できる。

$$
\boxed{
\text{XY rotating field}:
\text{pitch}+\text{chiralityを同時にprobe}
}
$$

ここがIsingとの大きな違いである。

## 12. 有限波数応答の共通点と相違点

両模型に共通するのは

$$
\boxed{
\text{finite-}q\text{ correlation}
\Longrightarrow
\text{finite-}Q\text{ response peak}
}
$$

である。

また

$$
\boxed{
\text{peak position}\to q_{\rm corr},
\qquad
\text{peak width}\to\xi^{-1}
}
$$

という読み方も共通する。

一方でprobeの意味は異なる。

| 観点 | Ising | XY |
| --- | --- | --- |
| 最近接の局所変数 | $\tau_i=s_is_{i+1}$ | $\phi_i=\theta_{i+1}-\theta_i$ |
| 第二近接での結合 | $\tau_i\tau_{i+1}$ | $\cos(\phi_i+\phi_{i+1})$ |
| finite-$q$ の意味 | 離散配置の相関波数 | 局所回転率に対応可能 |
| 標準的なprobe | scalar modulated field | vector field / amplitude modulation |
| resonance条件 | $Q\simeq q_{\rm corr}$ | $Q\simeq q_{\rm corr}\simeq q_\ast$ |
| $Q$ の符号 | 通常は独立なchirality情報を持たない | 回転方向を表しchiralityを選べる |
| peak幅 | $\sim\xi^{-1}$ | $\sim\xi^{-1}$ |

## 13. 最近接との比較で最も重要な変化

最近接では、強磁性的なIsingとXYの応答はどちらも $Q=0$ を中心にしていた。そのため

$$
Q\xi
$$

が自然な変数だった。

第二近接によって有限構造波数が生まれると、それは

$$
\boxed{
Q\xi
\longrightarrow
(Q-q_{\rm corr})\xi
}
$$

へ置き換わる。

したがって第二近接の本質は、単に相関長を変えることではない。

$$
\boxed{
\text{the system acquires an internal spatial carrier wave}
}
$$

と見ることができる。

外場はそのcarrier waveに同調したとき最も強く応答する。

Isingではcarrierは離散配置の相関構造として現れ、XYでは実際の局所twistとして現れる。さらにXYではその回転方向まで外場で選べる。

この意味で第二近接比較の中心は

$$
\boxed{
\text{同じ有限記憶化が、Isingではwall構造、XYではtwistとchiralityとして現れ、
その違いが有限波数外場への応答に直接現れる}
}
$$

という点にある。
---
title: "1次元イジング模型 R=2 — disorder line, Lifshitz line, Fisher–Widom との対応"
summary: "R=2 Ising 鎖で現れる単調相関から減衰振動への crossover と、感受率ピークが有限波数へ移る crossover を、Stephenson disorder line、Lifshitz line、Fisher–Widom line との対応から整理する。"
publishedAt: 2026-09-11T15:35:00+09:00
area: "Physics"
topics: ["statistical mechanics", "Ising model", "correlation", "frustration", "liquid theory"]
status: growing
---

R=2 の1次元 Ising 鎖では、有限温度で自由エネルギーが非解析になる通常の相転移は起こらない。それでも、相関関数や波数応答の構造には明確な質的変化が現れる。

ここでは、その二つの crossover を既存の物理用語と対応づける。

## 1. 単調減衰から減衰振動へ：Stephenson disorder line

競合系

$$
H=-J_1\sum_i s_i s_{i+1}-J_2\sum_i s_i s_{i+2},
\qquad J_1>0,\quad J_2<0
$$

では、相関を支配する奇 sector の固有値

$$
\lambda_\pm^{(-)}
=e^{K_2}\sinh K_1
\pm
\sqrt{e^{2K_2}\cosh^2K_1-e^{-2K_2}}
$$

が実数から複素共役対へ変わる。

境界は

$$
\boxed{
 e^{2K_2}\cosh K_1=1
}
$$

であり、$t\equiv k_BT/J_1$、$\kappa\equiv-J_2/J_1$ と書けば

$$
\boxed{
\kappa_{\mathrm d}(t)
=\frac{t}{2}\ln\cosh\!\left(\frac1t\right)
}
$$

となる。

この線を越えると

$$
C(r)\sim e^{-r/\xi}
$$

型の単調減衰から

$$
\boxed{
C(r)\sim e^{-r/\xi}\cos(q_*r+\phi)
}
$$

型の減衰振動へ変わる。

この種の境界は、競合する next-nearest-neighbor Ising 模型について John Stephenson が 1970 年に導入した **disorder point / disorder line** の概念に対応する。Stephenson の定義でも、disordered phase 内部で相関減衰が単調指数型から振動指数型へ変わることが中心になっている。

したがって本ノートの $\kappa_{\mathrm d}(t)$ は、**Stephenson disorder line** と呼ぶのが自然である。

重要なのは、ここでの "disorder" が「秩序相から無秩序相への相転移」という意味ではないことだ。両側とも有限温度では無秩序相であり、変わるのは長距離相関を運ぶモードの性質である。

参考：John Stephenson, *Ising Model with Antiferromagnetic Next-Nearest-Neighbor Coupling: Spin Correlations and Disorder Points*, Phys. Rev. B **1**, 4405 (1970), DOI: 10.1103/PhysRevB.1.4405.

## 2. disorder line は臨界線ではない

熱力学的な critical line では、熱力学極限で自由エネルギーが非解析になる。

一方、disorder line では最大固有値 $\lambda_0$ は滑らかなままで、自由エネルギー

$$
f=-\beta^{-1}\ln\lambda_0
$$

も解析的である。

変化するのは subleading spectrum である。

$$
\boxed{
\text{two real subleading modes}
\longrightarrow
\text{degenerate modes}
\longrightarrow
\text{complex-conjugate modes}
}
$$

境界では二つのモードが縮退するため、相関には一般に

$$
\boxed{
C(r)=(A+Br)\mu^r
}
$$

という重根に特有の形が現れる。

したがって disorder line は、**熱力学的特異点ではなく、相関スペクトルの crossover line** と考えるのがよい。

## 3. 有限波数が「存在する」ことと「最も応答する」ことは別

disorder line を越えれば、長距離 tail は有限波数 $q_{\mathrm{spec}}>0$ を持つ。しかし、静的感受率

$$
\chi(q)
=\beta\left[
1+2\sum_{r=1}^{\infty}C(r)\cos(qr)
\right]
$$

の最大が直ちに有限 $q$ へ移るとは限らない。

そこで

$$
q_{\mathrm{spec}}
\equiv\arg\lambda_+^{(-)},
$$

$$
q_\chi
\equiv\operatorname*{arg\,max}_q\chi(q)
$$

を区別する。

前者は「最も遠くまで残る相関モードの位相」、後者は「全距離相関を積分したとき最も強く応答する波数」である。

R=2 では一般に

$$
\boxed{
q_{\mathrm{spec}}>0
\quad\text{だが}\quad
q_\chi=0
}
$$

となる中間領域が存在する。

## 4. $q_\chi$ が有限値へ移る線：Lifshitz line

$q=0$ 近傍で感受率を展開すると

$$
\chi(q)
=\chi(0)
-\beta q^2\sum_{r\ge1}r^2C(r)
+O(q^4).
$$

したがって $q=0$ の曲率が変わる条件は

$$
\boxed{
\sum_{r\ge1}r^2C(r)=0
}
$$

である。

この線を越えると、$\chi(q)$ の最大が $q=0$ から有限波数へ移る。このように **disordered region 内で structure factor や susceptibility の最大位置が $q=0$ から $q\neq0$ へ移る locus** は、一般に **Lifshitz line** と呼ばれる。

ここでは operational に

$$
\boxed{
q_\chi=0
\longrightarrow
q_\chi\neq0
}
$$

となる線を Lifshitz line と呼ぶ。

したがって R=2 には、有限温度で少なくとも二つの異なる crossover がある。

$$
\boxed{
\begin{aligned}
\text{Stephenson disorder line}:&\quad
\text{long-range correlation becomes oscillatory},\\
\text{Lifshitz line}:&\quad
\text{maximum static response moves to finite }q.
\end{aligned}
}
$$

両者の間では、長距離 tail はすでに振動しているが、系全体としてはまだ $q=0$ が最も応答しやすい。

## 5. 液体論では Fisher–Widom line に近い

液体論では pair correlation function の漸近減衰が

$$
h(r)\sim e^{-\alpha r}
$$

から

$$
\boxed{
h(r)\sim e^{-\alpha r}\cos(kr-\theta)
}
$$

へ切り替わる境界を **Fisher–Widom line** と呼ぶ。

これは Ornstein–Zernike 理論の言葉では、長距離減衰を支配する pole が単調減衰を与えるものから複素共役 pole へ切り替わることに対応する。

したがって数学的構造は R=2 Ising 鎖と非常によく似ている。

$$
\boxed{
\begin{array}{ccc}
\text{R=2 Ising} && \text{liquid theory}\\
\lambda_\mathrm{sub}/\lambda_0
&\longleftrightarrow&
\text{leading OZ pole}\\
-\ln|\lambda_\mathrm{sub}/\lambda_0|
&\longleftrightarrow&
\text{inverse decay length}\\
\arg\lambda_\mathrm{sub}
&\longleftrightarrow&
\text{oscillation wave number}
\end{array}
}
$$

したがって、Stephenson disorder line と Fisher–Widom line は歴史的・モデル的には別の名称だが、どちらも

$$
\boxed{
\text{dominant correlation mode changes from monotone to oscillatory}
}
$$

という **spectral crossover** の同型な現象として理解できる。

Fisher–Widom line は単なる Widom line とは別概念である。前者は相関の漸近形の変化を表し、後者は臨界点上方で応答関数や相関長の極大 locus を指す文脈で使われることが多い。

参考：Fisher–Widom line は、単純流体で total pair correlation function の最長距離減衰が単調型から指数減衰振動型へ切り替わる線として定義されている。例えば P. Mausbach, R. Fingerhut, J. Vrabec, Phys. Rev. E **106**, 034136 (2022), DOI: 10.1103/PhysRevE.106.034136.

## 6. $T=0$, $\kappa=1/2$ は別格である

有限温度の disorder line と Lifshitz line は crossover であり、通常の相転移線ではない。

しかし

$$
T=0,
\qquad
\kappa=\frac12
$$

では事情が違う。

この点では基底状態が

$$
++++\cdots
$$

型から

$$
++--++--\cdots
$$

型へ切り替わる。

したがって $T=0$, $\kappa=1/2$ は **ground-state transition point** であり、有限温度の二つの crossover line が低温極限でこの点へ近づく、と読むのが自然である。

概念図としては

$$
\boxed{
\text{ground-state competition at }(T=0,\kappa=1/2)
\quad\Longrightarrow\quad
\begin{cases}
\text{disorder line},\\
\text{Lifshitz line}
\end{cases}
\text{ at }T>0
}
$$

と整理できる。

## 7. 物理的な読み方

この三つの言葉を混同しないことが重要である。

- **disorder line**：長距離に残る相関モードの種類が変わる。
- **Lifshitz line**：最も強く応答する波数が変わる。
- **critical line**：熱力学ポテンシャルが非解析になる。

今回の1次元有限範囲 R=2 Ising 鎖では、有限温度に前二者はあるが、通常の有限温度 critical line はない。

この意味で R=2 は、**熱力学的相転移がなくても、相関スペクトルと応答の双方に明確な幾何学的・スペクトル的 crossover が存在しうる**ことを示す最小模型である。

---
title: "漸近解析における尺度分離と近似の破綻"
summary: "正則摂動、境界層、WKB法、多重尺度法を具体的な方程式で導出し、一様近似が必要となる理由を比較する。"
publishedAt: 2026-09-09T18:20:00+09:00
updatedAt: 2026-11-28
area: "Mathematics"
field: mathematics
kind: theory
topics: ["asymptotic analysis", "perturbation theory", "mathematical physics"]
status: growing
---

小さなパラメータを含む方程式の解が、そのパラメータをゼロにした方程式の解に近づくとは限らない。極限によって境界条件を満たせなくなったり、局所的に小さな誤差が長時間にわたって累積したりするためである。漸近解析の手法を、こうした近似の破綻の仕方から整理する。

## 正則摂動と解の滑らかな依存性

有限次元の方程式 $F(y,\varepsilon)=0$ を考える。$F(y_0,0)=0$ であり、$F$ が十分滑らかで $\partial_yF(y_0,0)\ne0$ なら、陰関数定理により $y_0$ の近傍に滑らかな解の枝 $y(\varepsilon)$ が存在する。

例えば

$$
y+\varepsilon y^2=1
$$

の $y(0)=1$ を満たす枝に $y=y_0+\varepsilon y_1+\varepsilon^2y_2+\cdots$ を代入すると、各次数から

$$
y_0=1,\qquad y_1=-1,\qquad y_2=2
$$

を得る。従って $y=1-\varepsilon+2\varepsilon^2+O(\varepsilon^3)$ である。厳密解 $2/(1+\sqrt{1+4\varepsilon})$ を展開しても同じ結果になる。

微分方程式では、解を求める作用素の可逆性や境界条件、近似を評価する区間も関係する。最高階微分の係数がゼロにならないことだけでは正則性を保証できない。

## 境界層と接合漸近展開

$0<\varepsilon\ll1$ として境界値問題

$$
\varepsilon y''+y'=0,\qquad y(0)=0,\quad y(1)=1
$$

を考える。$\varepsilon=0$ とすると $y'=0$ となり、両端の境界条件を同時に満たせない。厳密解は

$$
y(x)=\frac{1-e^{-x/\varepsilon}}{1-e^{-1/\varepsilon}}
$$

であり、$x=0$ の近くに厚さ $O(\varepsilon)$ の急変領域がある。

外部領域では $\varepsilon y''$ を落とし、右端の条件から $y_{\rm out}=1$ を得る。左端では $X=x/\varepsilon^\alpha$ と置くと

$$
\varepsilon^{1-2\alpha}Y''+\varepsilon^{-\alpha}Y'=0
$$

となる。二項が同じ次数になるには $\alpha=1$ が必要である。内部方程式は $Y''+Y'=0$ となり、$Y(0)=0$ から $Y=A(1-e^{-X})$ を得る。

重なり領域 $\varepsilon\ll x\ll1$ で内部解を外部解に接合すると $A=1$ となる。共通部分1を引いた合成近似は

$$
y_{\rm comp}=y_{\rm out}+Y(x/\varepsilon)-1=1-e^{-x/\varepsilon}.
$$

厳密解との差は全区間で $O(e^{-1/\varepsilon})$ であり、一様に小さい。固定した $x>0$ での通常のべき展開には、この指数的に小さい項は現れない。しかし $x=O(\varepsilon)$ では同じ項が $O(1)$ になる。

## WKB法と転回点

波動方程式

$$
\varepsilon^2y''+Q(x)y=0
$$

を考える。$Q>0$ で滑らかな領域で $y=A(x)e^{iS(x)/\varepsilon}$ と置くと、

$$
[Q-(S')^2]A+i\varepsilon(2A'S'+AS'')+\varepsilon^2A''=0
$$

となる。先頭次数は $(S')^2=Q$、次の次数は $(A^2S')'=0$ を与える。したがって二つの局所解は

$$
y_\pm(x)\simeq Q(x)^{-1/4}
\exp\left[\pm\frac{i}{\varepsilon}\int^x\sqrt{Q(s)}\,ds\right].
$$

局所波長に比べて $Q$ の変化が緩やかであることが必要で、代表的な条件は $\varepsilon|Q'|/|Q|^{3/2}\ll1$ である。振幅の高階微分に関する条件も必要となる。

単純転回点 $x_t$ で $Q(x_t)=0$、$Q'(x_t)=a\ne0$ とする。$x-x_t=(\varepsilon^2/|a|)^{1/3}X$ と置くと先頭次数で

$$
Y''+\operatorname{sgn}(a)XY=0
$$

を得る。これは符号を変えたAiry方程式である。転回点近傍では通常のWKB振幅が発散するが、Airy解は有限であり、その漸近形を両側のWKB解に接合できる。境界層と同様に、破綻する領域を別の尺度で解いている。

## 多重尺度法と長時間の位相ずれ

弱非線形振動子

$$
\ddot x+x+\varepsilon x^3=0
$$

を考える。通常の摂動展開で $x_0=A\cos t$ とすると、一階補正は

$$
\ddot x_1+x_1=-\frac{A^3}{4}(3\cos t+\cos3t)
$$

を満たす。共振する項から $-(3A^3/8)t\sin t$ が生じ、$\varepsilon t=O(1)$ で補正が先頭項と同程度になる。

速い時間 $t_0=t$ と遅い時間 $t_1=\varepsilon t$ を導入し、$x=x_0(t_0,t_1)+\varepsilon x_1+\cdots$ とする。$d/dt=\partial_0+\varepsilon\partial_1$ を代入すると、

$$
(\partial_0^2+1)x_1=-2\partial_0\partial_1x_0-x_0^3.
$$

$x_0=A(t_1)\cos[t_0+\psi(t_1)]$ と置く。基本振動と共振する正弦・余弦成分を消す条件は

$$
\frac{dA}{dt_1}=0,\qquad
\frac{d\psi}{dt_1}=\frac{3A^2}{8}
$$

となる。したがって先頭近似は

$$
x(t)\simeq A\cos\left[\left(1+\frac{3\varepsilon A^2}{8}\right)t+\psi_0\right].
$$

永年項は振幅の発散ではなく、非線形性による小さな周波数補正が時間とともに蓄積することを表していた。多重尺度法ではその補正を位相の遅い変化に組み込む。

## 手法の適用条件

| 問題 | 通常の展開が破綻する原因 | 用いる構成 |
| --- | --- | --- |
| 正則な代数方程式 | 解の枝が退化しない限り破綻しない | 陰関数と次数展開 |
| 特異な境界値問題 | 極限方程式の階数が低下 | 内部・外部解と接合 |
| 波動方程式 | 位相が速く変化し、転回点で尺度分離が崩れる | WKB解とAiry解 |
| 弱非線形振動子 | 周波数誤差が長時間で累積 | 多重時間尺度と可解条件 |

これらは排他的な分類ではない。WKB法の転回点処理にも接合漸近展開を用いる。近似を選ぶ際には、小さなパラメータだけでなく、誤差をどの領域で一様に評価する必要があるかを定めることが重要になる。

## 参考文献

- C. M. Bender and S. A. Orszag, *Advanced Mathematical Methods for Scientists and Engineers*.
- E. J. Hinch, *Perturbation Methods*, Cambridge University Press (1991).

文献の版・該当節の照合は別途行う。

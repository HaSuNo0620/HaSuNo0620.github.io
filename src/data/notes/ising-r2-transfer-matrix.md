---
title: "1次元一様第二近接 cosine-Z2 スピン系 — 振動相関と有限波数応答"
summary: "第二近接相互作用を加えた1次元Ising鎖を、相互作用するドメイン壁、4状態転送行列、Stephenson disorder line、解析的に求まる q_spec と q_chi、Lifshitz-like line、Fisher–Widom型クロスオーバーという構造で読む。"
publishedAt: 2026-09-11T02:10:00+09:00
updatedAt: 2026-09-19
area: "Physics"
topics: ["statistical mechanics", "Ising model", "transfer matrix", "correlation", "frustration", "information thermodynamics"]
status: growing
---

最近接鎖では零外場のdomain wallが独立だった。第二近接まで伸ばすと

$$
H=-J_1\sum_i s_i s_{i+1}-J_2\sum_i s_i s_{i+2},
\qquad s_i=\pm1
$$

となり、その独立性が最小の形で壊れる。

以下では $J_1>0$、とくに競合する $J_2<0$ を考え、

$$
\beta\equiv\frac{1}{k_{\mathrm B}T},
\qquad
K_1=\beta J_1,
\qquad
K_2=\beta J_2,
$$

$$
\kappa\equiv-\frac{J_2}{J_1}>0,
\qquad
t\equiv\frac{k_{\mathrm B}T}{J_1}
$$

とする。

第二近接の新しさは「行列が4×4になる」ことではなく、**欠陥列そのものが空間記憶を持ち、減衰長と構造波数が別々の情報になること**にある。

![R=1 と R=2 の物理的な違い](/figures/ising-r2/overview-r1-r2.svg)

## 系の座標

$$
\boxed{
(d=1,\ \text{uniform},\ R=2,\ \text{cosine},\ Z_2)
}
$$

Hamiltonian は

$$
H
=
-J_1\sum_i s_i s_{i+1}
-J_2\sum_i s_i s_{i+2},
$$

局所変数を

$$
\tau_i=s_i s_{i+1}
$$

とすると、$R=1$ で独立だった wall が $R=2$ で相互作用する。ここで動かした軸は interaction range だけである。


$Z_2$ では $\theta_i\in\{0,\pi\}$ と置けば

$$
\cos(\theta_i-\theta_j)=s_i s_j
$$

なので、標準 bilinear Ising 相互作用と cosine-$Z_2$ 表現は同値である。

## 1. 第二近接結合は domain wall 間相互作用になる

$$
\tau_i=s_i s_{i+1}=\pm1
$$

とおけば

$$
s_i s_{i+2}=\tau_i\tau_{i+1}
$$

なので

$$
\boxed{
H=-J_1\sum_i\tau_i-J_2\sum_i\tau_i\tau_{i+1}}
$$

となる。

最近接鎖の

$$
\text{independent walls}
$$

が

$$
\boxed{
\text{interacting walls}}
$$

へ変わる。

![スピン列とドメイン壁変数の対応](/figures/ising-r2/domain-wall-map.svg)

$J_1>0$ は隣接スピンを揃え、$J_2<0$ は2サイト離れたスピンを反対にしたがる。この競合が有限波数構造の源になる。

![最近接強磁性と第二近接反強磁性の競合](/figures/ising-r2/frustration-competition.svg)

$T=0$ では強磁性状態

$$
e_{\rm F}=-J_1-J_2
$$

と周期4状態 $++--$ の

$$
e_{++--}=J_2
$$

が

$$
\boxed{\kappa=\frac12}
$$

で競合する。これは零温度の基底状態境界であり、有限温度のdisorder lineとは別である。

## 2. transfer state は2スピンの履歴を持つ

新しいスピン $c=s_{i+1}$ を加えるとき、局所重みには $(a,b)=(s_{i-1},s_i)$ が必要になる。

$$
\boxed{
T_{(a,b),(b',c)}
=\delta_{b,b'}
\exp(K_1bc+K_2ac)}
$$

![R=2 の転送状態ネットワーク](/figures/ising-r2/transfer-state-network.svg)

状態を $(++),(+-),(-+),(--)$ とすれば transfer matrix は4状態になる。これは単なる行列サイズの増大ではなく、**局所重みを決めるために1ステップ前の履歴が必要になった**ことを表している。

最大固有値は

$$
\boxed{
\lambda_0
=e^{K_2}\cosh K_1
+\sqrt{e^{2K_2}\sinh^2K_1+e^{-2K_2}}}
$$

で、自由エネルギーは $f=-\beta^{-1}\ln\lambda_0$ となる。

二点スピン相関を担う奇sectorの固有値は

$$
\boxed{
\lambda_\pm^{(-)}
=e^{K_2}\sinh K_1
\pm\sqrt{e^{2K_2}\cosh^2K_1-e^{-2K_2}}}
$$

である。

## 3. subleading eigenvalue の位相が構造波数になる

奇sectorの判別式

$$
\Delta_-
=e^{2K_2}\cosh^2K_1-e^{-2K_2}
$$

は負になりうる。

![相関を担う転送固有値の複素化](/figures/ising-r2/spectrum-complexification.svg)

$\Delta_-<0$ では

$$
\lambda_\pm^{(-)}=u\pm iv
$$

となるため、長距離相関は

$$
\boxed{
C(r)\sim\rho^r\cos(q_{\rm spec}r+\phi)}
$$

となる。

構造波数は数値fitではなく固有値の偏角から

$$
\boxed{
q_{\rm spec}
=\arg\lambda_+^{(-)}
=\tan^{-1}\left[
\frac{\sqrt{e^{-2K_2}-e^{2K_2}\cosh^2K_1}}
{e^{K_2}\sinh K_1}
\right]}
$$

と直接得られる。

一方、減衰長は

$$
\boxed{
\xi^{-1}
=-\ln\rho,
\qquad
\rho=\left|\frac{\lambda_+^{(-)}}{\lambda_0}\right|}
$$

である。

つまり spectrum の

$$
|\lambda|\longrightarrow\xi,
\qquad
\arg\lambda\longrightarrow q_{\rm spec}
$$

という二つの情報が分離する。

複素化境界は

$$
e^{2K_2}\cosh K_1=1
$$

から

$$
\boxed{
\kappa_{\rm d}(t)
=\frac{t}{2}\ln\cosh\left(\frac1t\right)}
$$

となる。これが Stephenson disorder line である。

## 4. finite-$q$ tail と finite-$q$ response は同時には現れない

有限温度で熱力学的相転移はないが、相関と応答には二本の異なる crossover line がある。

![R=2 Ising鎖の相関構造マップ](/figures/ising-r2/correlation-structure-map.svg)

$$
(q_{\rm spec},q_\chi)
=
\begin{cases}
(0,0), & \kappa<\kappa_{\rm d}(t),\\
(>0,0), & \kappa_{\rm d}(t)<\kappa<\kappa_{\rm L}(t),\\
(>0,>0), & \kappa>\kappa_{\rm L}(t).
\end{cases}
$$

中間領域では長距離tailはすでに振動しているのに、静的感受率の最大はまだ $q=0$ に残る。

この3領域は相ではなく、**相関極とresponse peakの配置による構造分類**である。

## 5. disorder line 直後では最初の節が無限遠から入ってくる

正規化固有値を

$$
\mu_\pm=\frac{\lambda_\pm^{(-)}}{\lambda_0},
\qquad
a=\mu_++\mu_-,
\qquad
b=\mu_+\mu_-
$$

とおくと

$$
\boxed{
C(r+2)=aC(r+1)-bC(r)}
$$

で相関が閉じる。

![3領域の実空間相関](/figures/ising-r2/three-regimes-correlation.svg)

複素化直後は $q_{\rm spec}$ が小さいため、最初のゼロ点

$$
r_0\simeq\frac{\pi/2-\phi}{q_{\rm spec}}
$$

は非常に遠い。

近距離構造が不連続に変わるのではなく、**最初の節が無限遠から近づいてくる**と見るとdisorder lineの意味が分かりやすい。

## 6. $q_\chi$ は全距離相関の Fourier 最大である

静的感受率は

$$
\chi(q)
=\beta\left[1+2\sum_{r=1}^\infty C(r)\cos(qr)\right].
$$

![実空間の相関と波数空間の応答](/figures/ising-r2/real-fourier-map.svg)

$q_{\rm spec}$ は長距離tailを支配する複素極の位相、$q_\chi$ は全距離相関を積分した応答の最大位置である。同じ $C(r)$ から出るが同じ量ではない。

生成関数

$$
G(z)=\sum_{r=0}^\infty C(r)z^r
$$

は recurrence から

$$
\boxed{
G(z)=\frac{1+[C(1)-a]z}{1-az+bz^2}}
$$

となる。

$$
S(q)=\beta^{-1}\chi(q)=G(e^{iq})+G(e^{-iq})-1
$$

とし、$x=\cos q$ と置けば

$$
\boxed{S(x)=\frac{N(x)}{D(x)}}
$$

という1次/2次の有理関数に落ちる。

したがって内部極値は

$$
N'(x)D(x)-N(x)D'(x)=0
$$

という $x$ の二次方程式で決まり、物理的な根 $x_\ast\in[-1,1]$ から

$$
\boxed{q_\chi=\arccos x_\ast}
$$

を得る。

finite-$q$ responseも数値走査で定義する必要はなく、transfer structureから解析的に閉じる。

## 7. Lifshitz-like line は response peak の分岐条件である

$q_\chi$ が0から有限値へ移る条件は

$$
\left.\frac{\partial^2\chi}{\partial q^2}\right|_{q=0}=0.
$$

整理すると

$$
\boxed{
(\sinh^4K_1-1)e^{8K_2}
+(\sinh^2K_1+2)e^{4K_2}
-1=0}
$$

となる。

これから

$$
\boxed{
\kappa_{\rm L}(t)
=\frac{t}{4}
\ln\left[
\frac{
\sinh^2(1/t)+2
+\sinh(1/t)\sqrt{5\sinh^2(1/t)+4}}
{2}
\right]}
$$

を得る。

$t=1$ では

$$
\kappa_{\rm d}\simeq0.2169,
\qquad
\kappa_{\rm L}\simeq0.3224.
$$

![3領域の波数依存感受率](/figures/ising-r2/three-regimes-susceptibility.svg)

## 8. 二本の crossover line の間隔は有限温度で生まれる

$$
\Delta\kappa(t)
=\kappa_{\rm L}(t)-\kappa_{\rm d}(t)
$$

とする。

低温では

$$
\boxed{
\Delta\kappa(t)
\sim\frac{\ln\varphi}{4}t,
\qquad
\varphi=\frac{1+\sqrt5}{2}}
$$

で、$T=0$ では両線とも $\kappa=1/2$ へ収束する。

一方、高温では

$$
\boxed{\Delta\kappa(t)\to\frac14}
$$

となる。

複素極が生じる条件と、有限波数応答が最大になる条件が同じではないことが、この幅として定量化される。

## 9. $q_{\rm spec}>0$ でも $q_\chi=0$ に残れる

振動相関

$$
C(r)\sim A\rho^r\cos(q_{\rm spec}r+\phi)
$$

は Fourier 空間で $\pm q_{\rm spec}$ を中心とする有限幅の寄与を作る。

$q_{\rm spec}$ が小さい、あるいは $\xi$ が短いと、この二つが強く重なり、極はfinite-$q$化していても合成ピークは $q=0$ に残る。

したがって

$$
\boxed{
q_{\rm spec}>0\ \not\Rightarrow\ q_\chi>0}
$$

である。

この区別は、長距離漸近を支配するmodeと、弱い外場で最も励起しやすいmodeが別の問いであることを示している。

## 10. Stephenson disorder line は Fisher–Widom 型の pole crossover と同型である

液体論の Fisher–Widom line でも、pair correlation の長距離形が

$$
h(r)\sim e^{-\alpha r}
$$

から

$$
h(r)\sim e^{-\alpha r}\cos(qr-\theta)
$$

へ変わる。

![Ising の転送スペクトルと液体論の pole 構造の対応](/figures/ising-r2/ising-liquid-correspondence.svg)

Isingではsubleading transfer eigenvalue、液体論ではleading OZ poleが長距離相関を決める。軸上の支配modeが複素対へ移るというスペクトル機構が共通している。

ここでは

- Stephenson disorder line：長距離相関を担う固有値の実→複素化
- Lifshitz-like line：$\chi(q)$ 最大の $q=0\to q>0$ 移動
- $T=0,\kappa=1/2$：基底状態の競合点

を分けておく必要がある。有限温度のcritical lineは存在しない。

## 11. 競合は記憶を消すだけでなく、その空間位相を変える

![支配波数の競合強度依存](/figures/ising-r2/qstar-kappa.svg)

![相関長の競合強度依存](/figures/ising-r2/correlation-length-kappa.svg)

競合を強めると、強磁性的な相関長はいったん短くなるが、その後はfinite-$q$ modeの相関長が伸びる。

第二近接反強磁性は単なる相関破壊ではなく、**どの空間位相が最も遠くまで記憶を運ぶかを組み替える**。

## 12. 情報論的には thermal errors が correlated noise になる

最近接鎖では $\tau_i$ は独立で、domain wallを thermal bit-flip と読めば空間方向の誤りはmemorylessだった。

第二近接では

$$
P(\tau_{i+1}|\tau_i)\neq P(\tau_{i+1})
$$

となる。

![情報熱力学的なチャネル解釈](/figures/ising-r2/information-channel.svg)

熱的反転の並びそのものが1-step memoryを持つ。

この見方では

$$
q_{\rm spec}
$$

は最も遠くまで残る記憶の空間位相、

$$
q_\chi
$$

は弱い外場で最も励起しやすい空間パターンに対応する。

第二近接鎖は、**pole complexification** と **response-peak bifurcation** を同じ最小模型の中で分離して追える点に価値がある。

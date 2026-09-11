---
title: "1次元イジング模型 R=2 — 壁間相互作用・振動相関・有限波数応答"
summary: "第二近接相互作用を加えた1次元Ising鎖を、相互作用するドメイン壁、4状態転送行列、Stephenson disorder line、解析的に求まる q_spec と q_chi、Lifshitz-like line、Fisher–Widom型クロスオーバーという流れで読む。"
publishedAt: 2026-09-11T02:10:00+09:00
updatedAt: 2026-09-11T22:20:00+09:00
area: "Physics"
topics: ["statistical mechanics", "Ising model", "transfer matrix", "correlation", "frustration", "information thermodynamics"]
status: growing
---

最近接だけの $R=1$ では、外場ゼロのドメイン壁は互いに独立だった。相互作用範囲を1格子伸ばして

$$
H=-J_1\sum_i s_i s_{i+1}-J_2\sum_i s_i s_{i+2},
\qquad s_i=\pm1
$$

とすると、この単純さが最小の形で崩れる。このノートでは $J_1>0$ を基準とし、とくに競合する $J_2<0$ を見る。

以下では

$$
K_1\equiv\beta J_1,\qquad
K_2\equiv\beta J_2,\qquad
\kappa\equiv-\frac{J_2}{J_1}>0,\qquad
t\equiv\frac{k_BT}{J_1}
$$

を用いる。したがって $K_1=t^{-1}$、$K_2=-\kappa/t$ である。

![R=1 と R=2 の物理的な違い](/figures/ising-r2/overview-r1-r2.svg)

*第二近接結合の追加は、ドメイン壁表示では「自由な壁を相互作用する壁へ変える」操作になる。R=2 の新しさはここから始まる。*

## 1. 第二近接相互作用は壁間相互作用になる

bond 変数

$$
\tau_i\equiv s_i s_{i+1}=\pm1
$$

を導入する。$\tau_i=-1$ は $i$ と $i+1$ の間にドメイン壁があることを表す。

![スピン列とドメイン壁変数の対応](/figures/ising-r2/domain-wall-map.svg)

*ドメイン壁変数は絶対的なスピン向きではなく、隣接スピンの相対関係を記録する。*

第二近接項は

$$
s_i s_{i+2}=(s_i s_{i+1})(s_{i+1}s_{i+2})=\tau_i\tau_{i+1}
$$

だから、Hamiltonian は

$$
\boxed{
H=-J_1\sum_i\tau_i-J_2\sum_i\tau_i\tau_{i+1}
}
$$

となる。つまり

$$
R=1:\ \text{独立な壁}
\quad\longrightarrow\quad
R=2:\ \text{相互作用する壁}
$$

である。

$J_2<0$ では、最近接強磁性 $J_1>0$ が「隣接スピンを揃えたい」のに対し、第二近接結合は「2サイト離れたスピンを反対にしたい」。この競合が有限波数構造の源になる。

![最近接強磁性と第二近接反強磁性の競合](/figures/ising-r2/frustration-competition.svg)

*二つの局所選好は全結合で同時には満たせない。競合が十分強いと $++--$ の周期4構造が有利になる。*

### $T=0$ の基準点

強磁性状態では

$$
e_{\rm F}=-J_1-J_2,
$$

周期4の $++--++--\cdots$ では

$$
e_{++--}=J_2.
$$

両者は

$$
\boxed{\kappa=\frac12}
$$

で競合する。これは $T=0$ の基底状態境界であり、有限温度で後に現れる disorder line や Lifshitz-like line とは別物である。

## 2. 転送状態には2スピンの記憶が必要になる

新しいスピン $c=s_{i+1}$ を加えるとき、新しく確定する相互作用は $-J_1bc-J_2ac$ である。したがって、直前の2スピン $(a,b)=(s_{i-1},s_i)$ を覚える必要がある。

$$
\boxed{
T_{(a,b),(b',c)}
=\delta_{b,b'}\exp\!\left(K_1bc+K_2ac\right)
}
$$

![R=2 の転送状態ネットワーク](/figures/ising-r2/transfer-state-network.svg)

*$(a,b)\to(b,c)$ と窓を1サイトずつ送る。4状態化は単なる行列サイズの増大ではなく、局所重みを決めるために1ステップの履歴が必要になったことを表す。*

状態を $(++),(+-),(-+),(--)$ の順に並べると

$$
T=
\begin{pmatrix}
e^{K_1+K_2} & e^{-K_1-K_2} & 0 & 0\\
0 & 0 & e^{-K_1+K_2} & e^{K_1-K_2}\\
e^{K_1-K_2} & e^{-K_1+K_2} & 0 & 0\\
0 & 0 & e^{-K_1-K_2} & e^{K_1+K_2}
\end{pmatrix}.
$$

外場ゼロでは全スピン反転対称性があるので、偶 sector と奇 sector の $2\times2$ 問題に分解できる。最大固有値は

$$
\boxed{
\lambda_0
=e^{K_2}\cosh K_1
+\sqrt{e^{2K_2}\sinh^2K_1+e^{-2K_2}}
}
$$

であり、自由エネルギーは $f=-\beta^{-1}\ln\lambda_0$ である。

一方、二点スピン相関を担う奇 sector の固有値は

$$
\boxed{
\lambda_\pm^{(-)}
=e^{K_2}\sinh K_1
\pm\sqrt{e^{2K_2}\cosh^2K_1-e^{-2K_2}}
}
$$

である。

## 3. $q_{\rm spec}$ は転送固有値から解析的に求まる

奇 sector の判別式

$$
\Delta_-=e^{2K_2}\cosh^2K_1-e^{-2K_2}
$$

は負になりうる。

![相関を担う転送固有値の複素化](/figures/ising-r2/spectrum-complexification.svg)

*競合を強めると、相関を担う2本の実固有値が合流し、その先で複素共役対になる。*

$\Delta_-<0$ では

$$
\lambda_\pm^{(-)}=u\pm iv
$$

と書け、

$$
u=e^{K_2}\sinh K_1,
$$

$$
v=\sqrt{e^{-2K_2}-e^{2K_2}\cosh^2K_1}.
$$

したがって、正規化固有値 $\mu_\pm=\lambda_\pm^{(-)}/\lambda_0$ の偏角から

$$
\boxed{
q_{\rm spec}
=\arg\lambda_+^{(-)}
=\tan^{-1}\!\left[
\frac{
\sqrt{e^{-2K_2}-e^{2K_2}\cosh^2K_1}
}{e^{K_2}\sinh K_1}
\right]
}
$$

を直接得る。数値フィットで相関関数の周期を読む必要はない。

長距離相関は

$$
\boxed{
C(r)\sim \rho^r\cos(q_{\rm spec}r+\phi)
}
$$

で、減衰長は

$$
\boxed{
\xi^{-1}=-\ln\rho,
\qquad
\rho=\left|\frac{\lambda_+^{(-)}}{\lambda_0}\right|.
}
$$

複素化の境界は

$$
e^{2K_2}\cosh K_1=1,
$$

すなわち

$$
\boxed{
\kappa_{\rm d}(t)
=\frac{t}{2}\ln\!\cosh\!\left(\frac1t\right)
}
$$

である。これが Stephenson disorder line である。

## 4. 相図ではなく「相関構造マップ」として見る

有限温度では通常の熱力学的相転移はない。しかし、相関の構造には二つの明確な crossover があり、R=2 ではその両方を解析的に記述できる。

![R=2 Ising鎖の相関構造マップ](/figures/ising-r2/correlation-structure-map.svg)

*disorder line を越えると $q_{\rm spec}>0$ となり、Lifshitz-like line を越えると静的感受率の最大が有限波数へ移る。両者の間が「振動 tail はあるが最大応答はまだ $q=0$」の中間領域である。*

図の3領域は

$$
(q_{\rm spec},q_\chi)
=
\begin{cases}
(0,0), & \kappa<\kappa_{\rm d}(t),\\
(>0,0), & \kappa_{\rm d}(t)<\kappa<\kappa_{\rm L}(t),\\
(>0,>0), & \kappa>\kappa_{\rm L}(t)
\end{cases}
$$

と整理できる。これは3つの熱力学的相ではなく、**同じ相の内部にある相関・応答構造の分類**である。

## 5. 実空間では「節が遠方から入る」

正規化固有値を $\mu_\pm=\lambda_\pm^{(-)}/\lambda_0$ とし、

$$
a=\mu_++\mu_-,\qquad b=\mu_+\mu_-
$$

とおけば、有限距離の相関は

$$
\boxed{
C(r+2)=aC(r+1)-bC(r)
}
$$

で閉じる。$C(0)=1$ と

$$
C(1)=\frac{\partial\ln\lambda_0}{\partial K_1}
$$

から全ての $C(r)$ が決まる。

![3領域の実空間相関](/figures/ising-r2/three-regimes-correlation.svg)

*$t=1$。$\kappa=0.15$ は単調減衰、$0.27$ は弱い振動 tail、$0.45$ は近距離から符号反転が明瞭になる。*

複素化直後は $q_{\rm spec}$ が小さいため、最初のゼロ点

$$
r_0\simeq\frac{\pi/2-\phi}{q_{\rm spec}}
$$

は非常に遠い。disorder line を越えた直後は、近距離構造が突然変わるのではなく、**最初の節が無限遠から近づいてくる**と見るのがよい。

## 6. $q_\chi$ も解析的に求まる

静的感受率は

$$
\chi(q)
=\beta\left[1+2\sum_{r=1}^{\infty}C(r)\cos(qr)\right].
$$

![実空間の相関と波数空間の応答](/figures/ising-r2/real-fourier-map.svg)

*$q_{\rm spec}$ は長距離 tail を支配する複素極の位相、$q_\chi$ は全距離相関を Fourier 変換した応答の最大位置である。両者は同じ $C(r)$ から得られるが、同じ量ではない。*

R=2 では recurrence が2次なので、$\chi(q)$ は閉形式にできる。生成関数

$$
G(z)=\sum_{r=0}^{\infty}C(r)z^r
$$

は

$$
\boxed{
G(z)=\frac{1+[C(1)-a]z}{1-az+bz^2}
}
$$

となる。したがって

$$
S(q)\equiv\beta^{-1}\chi(q)
=G(e^{iq})+G(e^{-iq})-1.
$$

ここで

$$
x\equiv\cos q,
\qquad c\equiv C(1)
$$

と置くと

$$
\boxed{
S(x)=\frac{N(x)}{D(x)}
}
$$

で、

$$
N(x)=a^2-2ac-b^2+1+2(-a+bc+c)x,
$$

$$
D(x)=a^2+b^2-2b+1-2a(b+1)x+4bx^2.
$$

つまり $S(q)$ の最大値探索は連続波数を数値走査する問題ではなく、$x=\cos q$ の有理関数の極値問題に帰着する。

内部極値 $0<q<\pi$ では

$$
\frac{dS}{dq}=0
\quad\Longleftrightarrow\quad
\frac{dS}{dx}=0,
$$

したがって

$$
N'(x)D(x)-N(x)D'(x)=0.
$$

$N$ は1次、$D$ は2次なので、これは **$x=\cos q$ に関する二次方程式**である。物理的な根 $x_\ast\in[-1,1]$ を選び、境界 $x=\pm1$ と比較すれば

$$
\boxed{
q_\chi=\arccos x_\ast
}
$$

が解析的に決まる。

したがって、R=2 で $q_{\rm spec}$ と $q_\chi$ を数値的に「推定」する必要はない。数値計算は解析式を可視化・検算するために使えるが、波数選択そのものは転送行列から閉じて求められる。

## 7. Lifshitz-like line も閉形式で得られる

$q_\chi$ が $0$ から有限値へ移る境界は

$$
\left.\frac{\partial^2\chi}{\partial q^2}\right|_{q=0}=0
$$

である。これは

$$
\sum_{r\ge1}r^2C(r)=0
$$

と同値で、上の有理関数を用いると

$$
\boxed{
\left(\sinh^4K_1-1\right)e^{8K_2}
+\left(\sinh^2K_1+2\right)e^{4K_2}
-1=0
}
$$

まで整理できる。

$s=\sinh K_1$、$z=e^{4K_2}$ と置けば

$$
(s^4-1)z^2+(s^2+2)z-1=0,
$$

物理的な根は

$$
\boxed{
z=\frac{2}{s^2+2+s\sqrt{5s^2+4}}
}
$$

である。

$K_1=1/t$、$K_2=-\kappa/t$ を戻すと、Lifshitz-like line は

$$
\boxed{
\kappa_{\rm L}(t)
=\frac{t}{4}
\ln\!\left[
\frac{
\sinh^2(1/t)+2
+\sinh(1/t)\sqrt{5\sinh^2(1/t)+4}
}{2}
\right]
}
$$

となる。

$t=1$ では、この解析式から

$$
\kappa_{\rm d}\simeq0.2169,
\qquad
\kappa_{\rm L}\simeq0.3224
$$

を得る。これらは数値走査で見つける値ではなく、解析式を評価した値である。

![3領域の波数依存感受率](/figures/ising-r2/three-regimes-susceptibility.svg)

*$\kappa=0.15$ と $0.27$ では最大は $q=0$ に残り、$0.45$ で有限波数へ移る。図は解析的に決まる crossover の両側で $\chi(q)$ の形がどう変わるかを可視化したもの。*

## 8. 二つの解析曲線の間隔が有限温度効果を測る

R=2 の内部構造は、二本の解析曲線

$$
\boxed{
\kappa_{\rm d}(t)
=\frac{t}{2}\ln\cosh\frac1t
}
$$

と

$$
\boxed{
\kappa_{\rm L}(t)
=\frac{t}{4}
\ln\!\left[
\frac{
\sinh^2(1/t)+2
+\sinh(1/t)\sqrt{5\sinh^2(1/t)+4}
}{2}
\right]
}
$$

の間隔

$$
\Delta\kappa(t)=\kappa_{\rm L}(t)-\kappa_{\rm d}(t)
$$

で特徴づけられる。

低温では

$$
\kappa_{\rm d}(t)
=\frac12-\frac{t}{2}\ln2+\cdots,
$$

$$
\kappa_{\rm L}(t)
=\frac12-\frac{t}{2}\ln2
+\frac{t}{4}\ln\varphi+\cdots,
\qquad
\varphi=\frac{1+\sqrt5}{2},
$$

したがって

$$
\boxed{
\Delta\kappa(t)
\sim\frac{\ln\varphi}{4}\,t
\qquad(t\to0)
}
$$

である。$T=0$ では両線とも $\kappa=1/2$ に収束し、有限温度で線形に分離する。

一方、高温では

$$
\boxed{
\kappa_{\rm d}(t)
=\frac{1}{4t}-\frac{1}{24t^3}+\cdots
}
$$

に対し、

$$
\boxed{
\kappa_{\rm L}(t)
=\frac14+\frac{5}{32t^2}+\cdots
}
$$

だから

$$
\boxed{
\Delta\kappa(t)\to\frac14
\qquad(t\to\infty)
}
$$

となる。

この分離は、複素極が現れる条件と、有限波数応答が実際に最大になる条件が同じではないことを定量化している。

## 9. $q_{\rm spec}$ と $q_\chi$ が違う理由

oscillatory region では、実相関は一つの damped oscillatory channel として

$$
C(r)\sim A\rho^r\cos(q_{\rm spec}r+\phi)
$$

と書ける。それでも $q_\chi$ は一般に $q_{\rm spec}$ と一致しない。

理由は Fourier 空間で、この有限相関長の振動が有限幅を持つからである。位相を簡単のため無視すると、

$$
C(r)\sim \rho^r\cos(q_{\rm spec}r)
$$

は $q=\pm q_{\rm spec}$ を中心とする二つの broadened contribution を $S(q)$ に与える。$q_{\rm spec}$ が小さい、あるいは $\xi$ が短いと二つは強く重なり、極はすでに有限波数化していても $S(q)$ の最大は $q=0$ に残る。

したがって中間領域

$$
\boxed{
\kappa_{\rm d}(t)<\kappa<\kappa_{\rm L}(t)
}
$$

は、

$$
\boxed{
q_{\rm spec}>0,
\qquad
q_\chi=0
}
$$

という「極は分裂したが応答ピークはまだ分裂していない」領域である。

温度方向から見れば、$\chi(q,T)$ はすべての波数で定義され、

$$
\frac{\partial\chi(q,T)}{\partial T}
$$

は一般に $q$ に依存する。したがって finite-$q$ 側と $q=0$ 側の応答 weight は温度に対して同じようには変化しない。$q_{\rm spec}$ と $q_\chi$ の分離は、固定温度では極と Fourier peak の違いとして、温度発展では波数ごとの異なる thermal evolution の累積として読むことができる。

## 10. Stephenson disorder line と Fisher–Widom 型クロスオーバー

Stephenson disorder line は、disordered phase 内で相関が単調指数減衰から減衰振動へ変わる境界である。

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

*Ising では subleading transfer eigenvalue、液体論では leading OZ pole が長距離相関を決める。軸上の支配モードが複素対へ移ることが、両者に共通するスペクトル機構である。*

ここで区別すべき量は明確である。

- **Stephenson disorder line**：遠方相関を支配する固有値が実から複素へ変わる。
- **Lifshitz-like line**：$\chi(q)$ の最大が $q=0$ から有限 $q$ へ移る。
- **critical line**：自由エネルギーが非解析になる線。この有限温度1次元有限範囲系には存在しない。
- **$T=0,\kappa=1/2$**：強磁性と周期4基底状態の競合点。

したがって $T=0$ の競合点から有限温度側へ出ると、一つの相転移線が伸びるのではなく、異なる解析条件で定義される crossover line に分かれる。

### 参考

- J. Stephenson, *Ising Model with Antiferromagnetic Next-Nearest-Neighbor Coupling: Spin Correlations and Disorder Points*, Phys. Rev. B **1**, 4405 (1970), DOI: 10.1103/PhysRevB.1.4405.
- M. E. Fisher and B. Widom, *Decay of Correlations in Linear Systems*, J. Chem. Phys. **50** (1969), and related literature on the monotonic/oscillatory crossover.

## 11. 相関長と支配波数

同じ転送スペクトルから $q_{\rm spec}$ と $\xi$ を追うと、競合は単純に相関を弱めるのではなく、**どの空間位相が長距離記憶を運ぶか**を変えることが分かる。

![支配波数の競合強度依存](/figures/ising-r2/qstar-kappa.svg)

*disorder line を越えると $q_{\rm spec}$ は0から連続的に立ち上がり、強い競合では周期4構造に対応する $\pi/2$ へ近づく。これは固有値の偏角から直接計算できる。*

![相関長の競合強度依存](/figures/ising-r2/correlation-length-kappa.svg)

*強磁性的相関長はいったん短くなるが、その後は有限波数モードの相関長が伸びる。第二近接反強磁性は単なる「相関破壊」ではない。*

## 12. 情報論的には「熱的反転の並びに記憶が入る」

R=1 では $\tau_i$ は独立であり、ドメイン壁を thermal bit-flip と読めば空間方向の誤りは memoryless である。R=2 では

$$
P(\tau_{i+1}|\tau_i)\neq P(\tau_{i+1})
$$

となる。

![情報熱力学的なチャネル解釈](/figures/ising-r2/information-channel.svg)

*上段のスピン鎖と下段の壁変数は同じ統計を別表示している。R=2 では隣接する壁変数が結合し、熱的反転の並びが1ステップの記憶を持つ。*

ここで重要なのは、「熱雑音が仕事を生む」という意味ではないことだ。測定・feedback を別途導入したとき、残存する相関や mutual information が情報資源になりうる、というのが情報熱力学との接点である。

この見方では、$q_{\rm spec}$ は**最も遠くまで残る記憶の空間位相**、$q_\chi$ は**弱い外場で最も励起しやすい空間パターン**に対応する。

## 13. まとめ

R=2 では、相互作用範囲を1格子伸ばしただけで、長距離相関と有限波数応答の二つを区別する必要が生じる。しかし、そのどちらも数値的な特徴量ではない。転送行列から解析的に閉じる。

$$
\boxed{
\begin{aligned}
\text{spin}:&\quad \text{第二近接競合}\\
\text{wall}:&\quad \text{ドメイン壁間相互作用}\\
\text{transfer}:&\quad \text{2スピン記憶と複素 subleading mode}\\
q_{\rm spec}:&\quad \arg\lambda_+^{(-)}\ \text{から解析的に決定}\\
q_\chi:&\quad S(\cos q)\ \text{の二次極値方程式から解析的に決定}\\
\kappa_{\rm d}:&\quad \text{固有値複素化条件}\\
\kappa_{\rm L}:&\quad \chi''(0)=0\ \text{から閉形式で決定}
\end{aligned}
}
$$

中心となる点は、

$$
\boxed{q_{\rm spec}>0\ \not\Rightarrow\ q_\chi>0}
$$

である。最も遠くまで残る複素極が有限波数化しても、有限相関長による Fourier peak の重なりのため、系全体の最大応答はしばらく $q=0$ に留まる。

R=2 の重要性は、これらを単なる数値現象としてではなく、

$$
\boxed{
\text{pole complexification}
\quad\text{と}\quad
\text{response-peak bifurcation}
}
$$

という二つの解析的に区別された機構として、最小模型の中で完全に追えることにある。
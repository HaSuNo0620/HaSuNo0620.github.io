---
title: "1次元イジング模型 R=2 — 壁間相互作用・振動相関・有限波数応答"
summary: "第二近接相互作用を加えた1次元Ising鎖を、相互作用するドメイン壁、4状態転送行列、Stephenson disorder line、Lifshitz line、Fisher–Widom型クロスオーバー、情報熱力学という流れで読む。"
publishedAt: 2026-09-11T02:10:00+09:00
updatedAt: 2026-09-11T19:10:00+09:00
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

で競合する。これは $T=0$ の基底状態境界であり、有限温度で後に現れる disorder line や Lifshitz line とは別物である。

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

一方、二点スピン相関の長距離構造を担う奇 sector の固有値は

$$
\boxed{
\lambda_\pm^{(-)}
=e^{K_2}\sinh K_1
\pm\sqrt{e^{2K_2}\cosh^2K_1-e^{-2K_2}}
}
$$

である。

## 3. 相関スペクトルが複素化する

奇 sector の判別式

$$
\Delta_-=e^{2K_2}\cosh^2K_1-e^{-2K_2}
$$

は負になりうる。

![相関を担う転送固有値の複素化](/figures/ising-r2/spectrum-complexification.svg)

*競合を強めると、相関を担う2本の実モードが合流し、その先で複素共役対になる。実空間では最初の節が遠方から入り、やがて明瞭な減衰振動になる。*

$\Delta_-<0$ なら

$$
\frac{\lambda_\pm^{(-)}}{\lambda_0}
=\rho e^{\pm iq_{\rm spec}}
$$

と書け、長距離相関は

$$
\boxed{
C(r)\sim \rho^r\cos(q_{\rm spec}r+\phi)
}
$$

となる。減衰長は $\xi^{-1}=-\ln\rho$ である。R=2 では、長距離記憶が「どれだけ残るか」だけでなく「どの空間位相で残るか」まで持つ。

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

有限温度では通常の熱力学的相転移はない。しかし、相関の構造には二つの明確な crossover がある。

![R=2 Ising鎖の相関構造マップ](/figures/ising-r2/correlation-structure-map.svg)

*青実線を越えると遠方相関が振動し始め、緑破線を越えると静的感受率の最大が有限波数へ移る。両者の間が「振動 tail はあるが最大応答はまだ $q=0$」の中間領域である。*

図の3領域は

$$
(q_{\rm spec},q_\chi)
=
\begin{cases}
(0,0), & \text{単調減衰},\\
(>0,0), & \text{遠方のみ振動},\\
(>0,>0), & \text{有限波数応答が支配}
\end{cases}
$$

と整理できる。これは3つの熱力学的相を意味しない。分類しているのは、**相関スペクトルと応答の構造**である。

## 5. 実空間では「節が遠方から入る」

正規化固有値を $\mu_\pm=\lambda_\pm^{(-)}/\lambda_0$ とし、$a=\mu_++\mu_-$、$b=\mu_+\mu_-$ とおけば、有限距離の相関は

$$
\boxed{
C(r+2)=aC(r+1)-bC(r)
}
$$

で閉じる。$C(0)=1$ と $C(1)=\partial\ln\lambda_0/\partial K_1$ から全ての $C(r)$ が決まる。

![3領域の実空間相関](/figures/ising-r2/three-regimes-correlation.svg)

*$t=1$。$\kappa=0.15$ は単調減衰、$0.27$ は弱い振動 tail、$0.45$ は近距離から符号反転が明瞭になる。*

複素化直後は $q_{\rm spec}$ が小さいため、最初のゼロ点

$$
r_0\simeq\frac{\pi/2-\phi}{q_{\rm spec}}
$$

は非常に遠い。disorder line を越えた直後は、近距離構造が突然変わるのではなく、**最初の節が無限遠から近づいてくる**と見るのがよい。

## 6. Fourier 空間では $q_{\rm spec}$ と $q_\chi$ を分ける

静的感受率は

$$
\chi(q)
=\beta\left[1+2\sum_{r=1}^{\infty}C(r)\cos(qr)\right].
$$

![実空間の相関と波数空間の応答](/figures/ising-r2/real-fourier-map.svg)

*$q_{\rm spec}$ は遠方 tail の周期を、$q_\chi$ は全距離の相関を足し合わせた最大応答位置を表す。したがって一般には一致しない。*

$t=1$ では

$$
\kappa_{\rm d}\simeq0.217,
\qquad
\kappa_{\rm L}\simeq0.322.
$$

![3領域の波数依存感受率](/figures/ising-r2/three-regimes-susceptibility.svg)

*$\kappa=0.15$ と $0.27$ では最大は $q=0$ に残り、$0.45$ で有限波数へ移る。実空間 tail の振動開始と有限波数応答の支配化は二段階で起こる。*

$q=0$ 周りでは

$$
\chi''(0)=-2\beta\sum_{r\ge1}r^2C(r),
$$

したがって Lifshitz line は

$$
\boxed{
\sum_{r\ge1}r^2C(r)=0
}
$$

で特徴づけられる。disorder line が**長距離を支配する固有モードの型**を変えるのに対し、Lifshitz line は**全距離を足し合わせた応答の曲率**を変える。この違いが二つの線を分離する。

## 7. Stephenson disorder line と Fisher–Widom 型クロスオーバー

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

- **Stephenson disorder line**：遠方相関を支配するモードが実から複素へ変わる。
- **Lifshitz line**：$\chi(q)$ の最大が $q=0$ から有限 $q$ へ移る。
- **critical line**：自由エネルギーが非解析になる線。この有限温度1次元有限範囲系には存在しない。
- **$T=0,\kappa=1/2$**：強磁性と周期4基底状態の競合点。

したがって $T=0$ の競合点から有限温度側へ出ると、一つの相転移線が伸びるのではなく、異なる観測量に対応する crossover line に分かれる。

### 参考

- J. Stephenson, *Ising Model with Antiferromagnetic Next-Nearest-Neighbor Coupling: Spin Correlations and Disorder Points*, Phys. Rev. B **1**, 4405 (1970), DOI: 10.1103/PhysRevB.1.4405.
- M. E. Fisher and B. Widom, *Decay of Correlations in Linear Systems*, J. Chem. Phys. **50** (1969), and related literature on the monotonic/oscillatory crossover.

## 8. 相関長と支配波数

同じ転送スペクトルから $q_{\rm spec}$ と $\xi$ を追うと、競合は単純に相関を弱めるのではなく、**どの空間モードが長距離記憶を運ぶか**を変えることが分かる。

![支配波数の競合強度依存](/figures/ising-r2/qstar-kappa.svg)

*disorder line を越えると $q_{\rm spec}$ は0から連続的に立ち上がり、強い競合では周期4構造に対応する $\pi/2$ へ近づく。*

![相関長の競合強度依存](/figures/ising-r2/correlation-length-kappa.svg)

*強磁性的相関長はいったん短くなるが、その後は有限波数モードの相関長が伸びる。第二近接反強磁性は単なる「相関破壊」ではない。*

## 9. 情報論的には「熱的反転の並びに記憶が入る」

R=1 では $\tau_i$ は独立であり、ドメイン壁を thermal bit-flip と読めば空間方向の誤りは memoryless である。R=2 では

$$
P(\tau_{i+1}|\tau_i)\neq P(\tau_{i+1})
$$

となる。

![情報熱力学的なチャネル解釈](/figures/ising-r2/information-channel.svg)

*上段のスピン鎖と下段の壁変数は同じ統計を別表示している。R=2 では隣接する壁変数が結合し、熱的反転の並びが1ステップの記憶を持つ。*

ここで重要なのは、「熱雑音が仕事を生む」という意味ではないことだ。測定・feedback を別途導入したとき、残存する相関や mutual information が情報資源になりうる、というのが情報熱力学との接点である。

この見方では、$q_{\rm spec}$ は**最も遠くまで残る記憶の空間位相**、$q_\chi$ は**弱い外場で最も励起しやすい空間パターン**に対応する。

## 10. まとめ

R=2 への最小拡張は、同じ物理を複数の表示で読む問題である。

$$
\boxed{
\begin{aligned}
\text{spin}:&\quad \text{第二近接競合}\\
\text{wall}:&\quad \text{ドメイン壁間相互作用}\\
\text{transfer}:&\quad \text{2スピン記憶と複素 subleading mode}\\
\text{real space}:&\quad \text{単調減衰}\to\text{減衰振動}\\
\text{Fourier}:&\quad q_\chi=0\to q_\chi>0\\
\text{information}:&\quad \text{独立誤り}\to\text{相関した誤り}
\end{aligned}
}
$$

中心となる点は、

$$
\boxed{q_{\rm spec}>0\ \not\Rightarrow\ q_\chi>0}
$$

である。最も遠くまで残るモードが有限波数化しても、系全体の最大応答はしばらく $q=0$ に留まる。

したがって R=2 は、相互作用範囲を1格子伸ばしただけで、長距離記憶の「量」と「それを運ぶ空間モード」を分けて考える必要が生じる最小模型である。
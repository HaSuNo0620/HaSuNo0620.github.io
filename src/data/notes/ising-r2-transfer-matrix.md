---
title: "1次元イジング模型 R=2 — 壁間相互作用・振動相関・有限波数応答"
summary: "第二近接相互作用を加えた1次元Ising鎖を、相互作用するドメイン壁、4状態転送行列、Stephenson disorder line、Lifshitz line、Fisher–Widom型クロスオーバー、情報熱力学という流れで読む。"
publishedAt: 2026-09-11T02:10:00+09:00
updatedAt: 2026-09-11T15:50:00+09:00
area: "Physics"
topics: ["statistical mechanics", "Ising model", "transfer matrix", "correlation", "frustration", "information thermodynamics"]
status: growing
---

最近接だけの $R=1$ では、外場ゼロのドメイン壁は互いに独立だった。相互作用範囲を一つ伸ばして

$$
H=-J_1\sum_i s_i s_{i+1}-J_2\sum_i s_i s_{i+2},
\qquad s_i=\pm1
$$

とすると、その単純さが最小の形で崩れる。このノートでは $J_1>0$ を基準とし、とくに競合する $J_2<0$ を見る。

以下では $K_1\equiv\beta J_1$、$K_2\equiv\beta J_2$、競合強度 $\kappa\equiv-J_2/J_1>0$、無次元温度 $t\equiv k_BT/J_1$ を用いる。したがって $K_1=t^{-1}$、$K_2=-\kappa/t$ である。

![R=1 と R=2 の物理的な違い](/figures/ising-r2/overview-r1-r2.svg)

*相互作用範囲を1格子伸ばす操作は、スピン表示では第二近接結合の追加だが、ドメイン壁表示では自由な壁を相互作用する壁へ変える。R=2 の新しさはこの一点から始まる。*

## 1. ドメイン壁表示：第二近接相互作用は壁間相互作用になる

R=1 と同じく bond 変数

$$
\tau_i\equiv s_i s_{i+1}=\pm1
$$

を導入する。$\tau_i=-1$ は $i$ と $i+1$ の間にドメイン壁があることを表す。

![スピン列とドメイン壁変数の対応](/figures/ising-r2/domain-wall-map.svg)

*ドメイン壁表示は絶対的なスピン向きではなく隣接スピンの相対関係を記録する。一つの基準スピン $s_1$ と全ての $\tau_i$ があれば元のスピン列は復元できる。*

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

となる。したがって

$$
\boxed{
R=1:\ \text{free domain walls}
\quad\longrightarrow\quad
R=2:\ \text{interacting domain walls}
}
$$

である。

$J_2>0$ は隣接する $\tau$ を同符号に、$J_2<0$ は異符号にする傾向を持つ。後者は最近接強磁性 $J_1>0$ と競合し、強磁性とは異なる空間構造を作ろうとする。

### $T=0$ の基準点

強磁性状態 $++++\cdots$ の1サイト当たりエネルギーは $e_{\rm F}=-J_1-J_2$、周期4の $++--++--\cdots$ では $e_{++--}=J_2$ である。したがって両者は

$$
-J_1-J_2=J_2
$$

すなわち

$$
\boxed{\kappa=\frac12}
$$

で競合する。これは $T=0$ の ground-state boundary であり、後で現れる有限温度の disorder line や Lifshitz line とは区別する。

## 2. 転送状態には2スピンの記憶が必要になる

新しいスピン $c=s_{i+1}$ を加えるとき、新しく確定する相互作用は $-J_1bc-J_2ac$ であり、$(a,b)=(s_{i-1},s_i)$ の2スピンを覚えておく必要がある。したがって

$$
\boxed{
T_{(a,b),(b',c)}
=\delta_{b,b'}\exp\!\left(K_1bc+K_2ac\right)
}
$$

と定義する。

![R=2 の転送状態ネットワーク](/figures/ising-r2/transfer-state-network.svg)

*転送状態は $(a,b)\to(b,c)$ と1スピンずつ窓をずらす。4状態化は単なる行列サイズの増大ではなく、局所 Boltzmann 重みを決めるために過去1ステップの履歴が必要になったことを表す。*

状態を $(++),(+-),(-+),(--)$ の順に並べると

$$
\boxed{
T=
\begin{pmatrix}
e^{K_1+K_2} & e^{-K_1-K_2} & 0 & 0\\
0 & 0 & e^{-K_1+K_2} & e^{K_1-K_2}\\
e^{K_1-K_2} & e^{-K_1+K_2} & 0 & 0\\
0 & 0 & e^{-K_1-K_2} & e^{K_1+K_2}
\end{pmatrix}
}
$$

となる。

外場ゼロでは全スピン反転 $s_i\to-s_i$ が対称性である。そこで

$$
|F_\pm\rangle=\frac{|++\rangle\pm|--\rangle}{\sqrt2},
\qquad
|A_\pm\rangle=\frac{|+-\rangle\pm|-+\rangle}{\sqrt2}
$$

を使うと、$4\times4$ 問題は偶 sector と奇 sector の $2\times2$ 問題に分かれる。

最大固有値は偶 sector の

$$
\boxed{
\lambda_0
=e^{K_2}\cosh K_1
+\sqrt{e^{2K_2}\sinh^2K_1+e^{-2K_2}}
}
$$

であり、自由エネルギーは $f=-\beta^{-1}\ln\lambda_0$ である。

一方、スピン演算子は全スピン反転で奇なので、二点相関の長距離構造は奇 sector の

$$
\boxed{
\lambda_\pm^{(-)}
=e^{K_2}\sinh K_1
\pm\sqrt{e^{2K_2}\cosh^2K_1-e^{-2K_2}}
}
$$

によって決まる。

## 3. 相関スペクトルの複素化

R=1 では非自明な相関モードは実固有値比1本であり、相関は単純な指数減衰だった。R=2 では奇 sector の判別式

$$
\Delta_-=e^{2K_2}\cosh^2K_1-e^{-2K_2}
$$

が負になりうる。

![相関を担う転送固有値の複素化](/figures/ising-r2/spectrum-complexification.svg)

*競合を強めると2本の実モードが縮退し、その先で複素共役対になる。境界上では単純な2指数ではなく $(A+Br)\mu^r$ 型が現れ、複素側では減衰振動へ移る。*

$\Delta_-<0$ なら

$$
\frac{\lambda_\pm^{(-)}}{\lambda_0}
=\rho_\mu e^{\pm iq_{\rm spec}}
$$

と書け、相関は

$$
\boxed{
C(r)=2|A|\rho_\mu^r\cos(q_{\rm spec}r+\phi)
}
$$

となる。減衰長は $\xi^{-1}=-\ln\rho_\mu$ である。つまり R=2 では転送スペクトルが「どれだけ残るか」だけでなく「どの空間位相で残るか」まで持つ。

複素化の境界は

$$
e^{2K_2}\cosh K_1=1
$$

であり、$t,\kappa$ で書けば

$$
\boxed{
\kappa_{\rm d}(t)
=\frac{t}{2}\ln\!\cosh\!\left(\frac1t\right)
}
$$

となる。

## 4. 相図ではなく「相関構造マップ」として見る

この系では有限温度に通常の熱力学的相転移線はない。しかし相関の構造には明確な境界がある。そこで、熱力学的 phase diagram と混同しないよう **correlation-structure map** としてまとめる。

![R=2 Ising鎖の相関構造マップ](/figures/ising-r2/correlation-structure-map.svg)

*$t=k_BT/J_1$ と $\kappa=-J_2/J_1$ の平面。青実線は Stephenson disorder line、緑破線は $\chi(q)$ の最大が $q=0$ から有限波数へ移る Lifshitz line。両者の間には「長距離 tail は振動するが、最も強い静的応答はまだ $q=0$」という中間領域が存在する。$T\to0$ では両線は $\kappa=1/2$ の基底状態境界へ近づく。*

3領域は次のように読める。

- disorder line より下：$q_{\rm spec}=0$、$q_\chi=0$。相関は単調に減衰する。
- disorder line と Lifshitz line の間：$q_{\rm spec}>0$、$q_\chi=0$。遠距離 tail は振動するが、総合応答はまだ一様モードが最大である。
- Lifshitz line より上：$q_{\rm spec}>0$、$q_\chi>0$。有限波数構造が静的応答全体を支配する。

この3分割は「相が3つある」という意味ではない。自由エネルギーは有限温度で解析的なままであり、ここで分類しているのは**相関スペクトルと応答の構造**である。

## 5. 実空間では何が変わるのか

正規化した奇 sector 固有値を $\mu_\pm=\lambda_\pm^{(-)}/\lambda_0$ とし、$a=\mu_++\mu_-$、$b=\mu_+\mu_-$ とおけば、有限距離の相関は

$$
\boxed{
C(r+2)=aC(r+1)-bC(r)
}
$$

で閉じる。$C(0)=1$ と $C(1)=\partial\ln\lambda_0/\partial K_1$ を与えれば全ての $C(r)$ を生成できる。

$t=1$ で代表点 $\kappa=0.15,0.27,0.45$ を比較すると、3領域の違いが直接見える。

![3領域の実空間相関](/figures/ising-r2/three-regimes-correlation.svg)

*$\kappa=0.15$ では単調減衰、$0.27$ では弱い振動 tail、$0.45$ では近距離から符号反転が明瞭になる。振動モードの出現は、近距離構造の突然の反転ではなく、まず遠距離側から現れる。*

複素化直後には $q_{\rm spec}$ が小さいだけでなく位相 $\phi$ も効くため、最初のゼロ点

$$
r_0\simeq\frac{\pi/2-\phi}{q_{\rm spec}}
$$

は非常に遠い。したがって disorder line を越えた瞬間には「振動の最初の節が無限遠から入ってくる」と見るのがよい。

## 6. Fourier 空間では何が変わるのか

ゼロ外場の静的感受率は

$$
\chi(q)=\beta\sum_{r=-\infty}^{\infty}C(r)e^{-iqr}
=\beta\left[1+2\sum_{r=1}^{\infty}C(r)\cos(qr)\right]
$$

である。

![実空間の相関と波数空間の応答](/figures/ising-r2/real-fourier-map.svg)

*$q_{\rm spec}$ は遠距離 tail を支配するモードの位相であり、$q_\chi$ は全距離の相関を Fourier 和したときの最大応答波数である。前者は漸近構造、後者は全スケールの総合応答なので一般には一致しない。*

$t=1$ では disorder line が $\kappa_{\rm d}\simeq0.217$、$q_\chi$ が有限値へ動き始める Lifshitz line は $\kappa_{\rm L}\simeq0.322$ にある。

![3領域の波数依存感受率](/figures/ising-r2/three-regimes-susceptibility.svg)

*$\kappa=0.15$ と $0.27$ では $\chi(q)$ の最大はまだ $q=0$ にあるが、$0.45$ では $q_\chi/\pi\simeq0.28$ へ移る。実空間 tail の振動開始と有限波数応答の支配化は二段階で起こる。*

$q=0$ 周りで展開すれば

$$
\chi''(0)=-2\beta\sum_{r\ge1}r^2C(r)
$$

なので、Lifshitz line は

$$
\boxed{
\sum_{r\ge1}r^2C(r)=0
}
$$

で特徴づけられる。disorder line が「固有モードの型」を変えるのに対し、Lifshitz line は「全距離を積分した応答の曲率」を変える。両者が一致しない理由はここにある。

## 7. Stephenson disorder line と Fisher–Widom line

今回の単調減衰から減衰振動への境界には歴史的な名前がある。John Stephenson は 1970 年、反強磁性的 next-nearest-neighbor coupling を持つ Ising 系で、disordered phase 内の相関が monotonic exponential から oscillatory exponential へ変わる **disorder point** を論じた。この R=2 鎖の $\kappa_{\rm d}(t)$ はその最小の例である。

液体論には非常によく似た **Fisher–Widom line** がある。そこでは pair correlation の最長距離減衰が

$$
h(r)\sim e^{-\alpha r}
$$

から

$$
h(r)\sim e^{-\alpha r}\cos(qr-\theta)
$$

へ変わる。歴史的名称と具体的なスペクトルは異なるが、数学的には「最長距離を支配する相関モードが実から複素へ変わる」という同種の spectral crossover である。

![Ising の転送スペクトルと液体論の pole 構造の対応](/figures/ising-r2/ising-liquid-correspondence.svg)

*Ising では subleading transfer eigenvalue、液体論では Ornstein–Zernike 構造に現れる leading pole が長距離相関を決める。実モードから複素モードへの切り替えが、単調減衰から減衰振動への変化を生む。*

したがって、このノートでは次を区別する。

- **Stephenson disorder line**：相関を支配する長距離モードの型が変わる。
- **Lifshitz line**：静的感受率の最大位置が $q=0$ から有限 $q$ へ移る。
- **critical line**：自由エネルギーが非解析になる熱力学的相転移線。今回の有限温度1次元有限範囲系には存在しない。
- **$T=0,\kappa=1/2$**：強磁性と period-4 基底状態が競合する ground-state transition point。

つまり $T=0$ の競合点から有限温度側へ進むと、一つの相転移線が伸びるのではなく、異なる物理量を特徴づける複数の crossover line にほどける。

### 参考

- J. Stephenson, *Ising Model with Antiferromagnetic Next-Nearest-Neighbor Coupling: Spin Correlations and Disorder Points*, Phys. Rev. B **1**, 4405 (1970), DOI: 10.1103/PhysRevB.1.4405.
- M. E. Fisher and B. Widom, *Decay of Correlations in Linear Systems*, J. Chem. Phys. **50** (1969) and related proceedings literature on the monotonic/oscillatory crossover.

## 8. 相関長と支配波数

同じ転送スペクトルから $q_{\rm spec}$ と $\xi$ を追うと、frustration は単純に相関を弱めるのではなく、**どの空間モードが長距離記憶を運ぶか**を変えることが分かる。

![支配波数の競合強度依存](/figures/ising-r2/qstar-kappa.svg)

*disorder line を越えると $q_{\rm spec}$ は0から連続的に立ち上がり、強い競合では period-4 構造に対応する $\pi/2$ へ近づく。*

![相関長の競合強度依存](/figures/ising-r2/correlation-length-kappa.svg)

*競合を強めると強磁性的相関長はいったん短くなるが、その後は有限波数構造の発達とともに別のモードの相関長が伸びる。第二近接反強磁性は単純な「相関破壊」ではない。*

## 9. 情報熱力学的には「熱雑音が記憶を持つ」

R=1 では $\tau_i$ が独立なので、ドメイン壁を未観測の thermal bit-flip と読むと、空間方向の誤りは memoryless である。R=2 では $-J_2\tau_i\tau_{i+1}$ があるため

$$
P(\tau_{i+1}|\tau_i)\neq P(\tau_{i+1})
$$

となり、熱雑音そのものが空間的 memory を持つ。

![情報熱力学的なチャネル解釈](/figures/ising-r2/information-channel.svg)

*R=1 では独立な thermal bit-flip、R=2 では相関した thermal error と読める。転送状態が2スピンの履歴を持つことと、noise channel が memory を持つことは同じ局所統計構造の二つの表現である。*

境界スピン $s_0$ と遠方 $s_r$ の mutual information $I(s_0:s_r)$ は、長距離では $C(r)$ を通じて減衰する。ただし $C(r)$ は符号と位相を持つのに対し、mutual information は予測可能性を測るので両者は同じ量ではない。

また測定と feedback を別途導入するなら、残存 mutual information は $k_BTI$ のスケールで仕事抽出能力を制約する情報資源と解釈できる。これは平衡 Ising 鎖自体が仕事を生むという意味ではなく、**相関として保存された記憶が、情報熱力学的プロトコルを追加したときにどれだけ利用可能か**という意味である。

この観点では、$q_{\rm spec}$ は最も遠くまで残る記憶の空間位相、$q_\chi$ は弱い外場で最も書き込みやすい空間パターンと読める。R=2 では両者が一致しない領域が初めて現れる。

## 10. まとめ

R=2 への最小拡張は、同じ変化を複数の表示で読むことができる。

$$
\boxed{
\begin{aligned}
\text{spin picture}:&\quad \text{second-neighbor competition}\\
\text{wall picture}:&\quad \text{interacting domain walls}\\
\text{transfer picture}:&\quad \text{two-spin memory and complex subleading modes}\\
\text{real space}:&\quad \text{monotone}\to\text{damped oscillatory correlations}\\
\text{Fourier space}:&\quad q_\chi=0\to q_\chi>0\\
\text{information picture}:&\quad \text{memoryless}\to\text{correlated thermal errors}
\end{aligned}
}
$$

ここで最も重要なのは、**disorder line と Lifshitz line が異なる**ことである。最も遠くまで残るモードが有限波数化しても、系全体として最も強く応答するモードはしばらく $q=0$ に留まる。

したがって R=2 は、相互作用範囲を1格子伸ばしただけで、長距離記憶の「量」だけでなく、**その記憶がどの空間モードに乗って運ばれるか**まで分離して考える必要が生じる最小模型である。

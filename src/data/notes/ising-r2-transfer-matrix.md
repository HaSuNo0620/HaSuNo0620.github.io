---
title: "1次元イジング模型 R=2 — 壁間相互作用と振動相関"
summary: "第二近接相互作用を加えた1次元Ising鎖を、相互作用するドメイン壁、4状態転送行列、複素共役固有値、有限波数の減衰振動という流れで読む。"
publishedAt: 2026-09-11T02:10:00+09:00
area: "Physics"
topics: ["statistical mechanics", "Ising model", "transfer matrix", "correlation", "frustration"]
status: growing
---

最近接だけの $R=1$ では、外場ゼロのドメイン壁は互いに独立だった。相互作用範囲を一つだけ伸ばして

$$
\boxed{
H
=-J_1\sum_i s_i s_{i+1}
-J_2\sum_i s_i s_{i+2}
}
$$

とすると、この単純さが最小の形で崩れる。このノートでは $J_1>0$ を基準とし、とくに競合する $J_2<0$ を見る。

以下では

$$
K_1\equiv\beta J_1,
\qquad
K_2\equiv\beta J_2
$$

と書く。また競合強度として $\kappa\equiv-J_2/J_1>0$、無次元温度として $t\equiv k_B T/J_1$ を用いる。このとき $K_1=t^{-1}$、$K_2=-\kappa/t$ である。

## 1. $R=2$ はドメイン壁同士を相互作用させる

$R=1$ と同じく

$$
\tau_i\equiv s_i s_{i+1}=\pm1
$$

を導入する。第二近接項は

$$
s_i s_{i+2}
=(s_i s_{i+1})(s_{i+1}s_{i+2})
=\tau_i\tau_{i+1}
$$

だから、Hamiltonian は

$$
\boxed{
H
=-J_1\sum_i\tau_i
-J_2\sum_i\tau_i\tau_{i+1}
}
$$

となる。

したがって $R=1\to2$ の本質は、スピン表示では「第二近接相互作用を追加する」ことだが、ドメイン壁表示では

$$
\boxed{
\text{free domain walls}
\longrightarrow
\text{interacting domain walls}
}
$$

である。

$J_2>0$ は隣接する $\tau$ を同符号に、$J_2<0$ は異符号にする傾向を持つ。後者は最近接強磁性 $J_1>0$ と競合し、単純な強磁性配列とは異なる空間構造を生む。

### $T=0$ の基準点

強磁性状態 $++++\cdots$ の1サイト当たりエネルギーは

$$
e_{\mathrm F}=-J_1-J_2,
$$

一方、周期4の $++--++--\cdots$ では

$$
e_{++--}=J_2.
$$

両者は $J_2=-J_1/2$、すなわち

$$
\boxed{\kappa=\frac12}
$$

で等しくなる。これは後に現れる有限温度の「振動相関が出始める線」とは同じではないが、その $T\to0$ 極限になっている。

## 2. 転送状態には2スピンの記憶が必要になる

新しいスピン $c=s_{i+1}$ を加えるとき、新たに確定する相互作用エネルギーは

$$
-J_1bc-J_2ac,
\qquad
(a,b)=(s_{i-1},s_i).
$$

したがって転送状態を2スピン組 $(a,b)$ とし、

$$
\boxed{
T_{(a,b),(b',c)}
=\delta_{b,b'}
\exp\!\left[K_1bc+K_2ac\right]
}
$$

とすればよい。状態を

$$
(++),\quad (+-),\quad (-+),\quad (--)
$$

の順に並べると、

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

行列にゼロが多いのは、$(a,b)\to(b,c)$ と1スピンずつ窓をずらすためである。つまり $4\times4$ という次元増大は単なる計算量の増加ではなく、**局所 Boltzmann 重みを決めるために1ステップ余分な履歴が必要になった**ことを表している。

## 3. スピン反転対称性で2つの sector に分かれる

外場ゼロでは全スピン反転 $s_i\to-s_i$ が対称性なので、

$$
++\leftrightarrow--,
\qquad
+-\leftrightarrow-+
$$

である。そこで

$$
|F_\pm\rangle
=\frac{|++\rangle\pm|--\rangle}{\sqrt2},
\qquad
|A_\pm\rangle
=\frac{|+-\rangle\pm|-+\rangle}{\sqrt2}
$$

を使うと、$4\times4$ 問題は偶 sector と奇 sector の $2\times2$ 問題に分かれる。

$$
A=e^{K_1+K_2},\quad
B=e^{-K_1-K_2},\quad
C=e^{-K_1+K_2},\quad
D=e^{K_1-K_2}
$$

とおけば、偶 sector は

$$
T_+=
\begin{pmatrix}
A&B\\
D&C
\end{pmatrix},
$$

奇 sector は

$$
T_-=
\begin{pmatrix}
A&B\\
-D&-C
\end{pmatrix}
$$

である。

最大固有値は偶 sector の

$$
\boxed{
\lambda_0
=e^{K_2}\cosh K_1
+\sqrt{e^{2K_2}\sinh^2K_1+e^{-2K_2}}
}
$$

で、自由エネルギーは $f=-\beta^{-1}\ln\lambda_0$ となる。

一方、スピン演算子は全スピン反転で奇なので、二点スピン相関の長距離減衰を支配するのは奇 sector の固有値である。その2本は

$$
\boxed{
\lambda_\pm^{(-)}
=e^{K_2}\sinh K_1
\pm
\sqrt{e^{2K_2}\cosh^2K_1-e^{-2K_2}}
}
$$

となる。

## 4. 実固有値から複素共役対へ

$R=1$ では相関を支配する非自明な固有値比は実数だった。R=2 では奇 sector の平方根

$$
\Delta_-
=e^{2K_2}\cosh^2K_1-e^{-2K_2}
$$

が負になりうる。

$\Delta_-<0$ なら

$$
\lambda_\pm^{(-)}
=\rho e^{\pm iq_*}
$$

という複素共役対になり、相関の漸近形は

$$
\boxed{
C(r)
\sim
A\,e^{-r/\xi}\cos(q_*r+\phi)
}
$$

となる。ここで

$$
\boxed{
\xi^{-1}=\ln\frac{\lambda_0}{\rho}
}
$$

である。

複素領域では固有値の積から

$$
\rho
=\sqrt{e^{-2K_2}-e^{2K_2}},
$$

また実部から

$$
\boxed{
\cos q_*
=\frac{e^{K_2}\sinh K_1}{\rho}
}
$$

を得る。つまり R=2 では「減衰率」だけでなく「固有の空間位相」まで転送スペクトルが持つ。

## 5. 振動相関が出始める境界

複素化条件 $\Delta_-<0$ は

$$
e^{4K_2}\cosh^2K_1<1
$$

であり、境界は

$$
\boxed{
e^{2K_2}\cosh K_1=1
}
$$

である。$K_1=t^{-1}$、$K_2=-\kappa/t$ を代入すると、

$$
\boxed{
\kappa_{\mathrm d}(t)
=\frac{t}{2}\ln\!\cosh\!\left(\frac1t\right)
}
$$

となる。

![振動相関が出始める境界](/figures/ising-r2/oscillatory-boundary.svg)

*単調減衰から減衰振動へ変わる転送スペクトルの境界。有限温度での相転移線ではなく、相関を支配する奇 sector 固有値が実数から複素共役対へ変わる線である。$t\to0$ では $\kappa_{\mathrm d}\to1/2$。*

ここで重要なのは、この線が熱力学的相転移ではないことだ。有限相互作用範囲の1次元 Ising 鎖では有限温度で通常の秩序化相転移は生じない。しかし**相関の形**は、単調指数減衰から減衰振動へ明確に変わりうる。

## 6. $q_*$ は有限波数構造の直接の指標になる

複素化境界を越えると $q_*$ はゼロから連続的に立ち上がる。

![支配波数の競合強度依存](/figures/ising-r2/qstar-kappa.svg)

*競合強度 $\kappa=-J_2/J_1$ に対する相関の支配波数。境界より弱い競合では $q_*=0$、境界を越えると有限波数が現れ、強い競合では $q_*\to\pi/2$ に近づく。低温ではこの変化が $\kappa=1/2$ 近傍へ集中する。*

$R=1$ の強磁性鎖では自然な長距離モードは $q_*=0$ だった。R=2 では frustration によって

$$
0<q_*<\frac{\pi}{2}
$$

という非自明な波数が連続的に選ばれ、強い競合では周期4構造に対応する $q_*=\pi/2$ へ近づく。

したがって

$$
\boxed{
J_2
\longrightarrow
\text{domain-wall interaction}
\longrightarrow
\text{complex transfer modes}
\longrightarrow
q_*\neq0
}
$$

という因果の流れが見える。

## 7. 相関長は単調には変わらない

同じ固有値から得られる相関長を $\kappa$ に対して描くと、frustration の効果はさらに分かりやすい。

![相関長の競合強度依存](/figures/ising-r2/correlation-length-kappa.svg)

*相関長 $\xi$ の $\kappa$ 依存。最近接強磁性が支配する側では低温ほど長い相関を持つが、競合を強めると境界付近で一度短くなり、その後は周期4傾向の発達とともに再び伸びる。縦軸は対数表示。*

つまり第二近接反強磁性は単純に「相関を壊す」わけではない。弱い競合では強磁性的な長距離記憶を破壊するが、さらに強くすると今度は別の波数 $q_*\simeq\pi/2$ を持つ構造を安定化し、そのモードの相関長が伸びる。

この意味で R=2 で起きているのは

$$
\text{correlation strength の単純な増減}
$$

ではなく、

$$
\boxed{
\text{which spatial mode carries the long-range memory?}
}
$$

という問いの変化である。

## 8. 情報熱力学的には「熱雑音が記憶を持つ」

R=1 では $\tau_i$ が独立だったので、ドメイン壁を未観測の thermal bit-flip と読むと、空間方向の誤りは memoryless だった。

R=2 では

$$
H_\tau
=-J_1\sum_i\tau_i
-J_2\sum_i\tau_i\tau_{i+1}
$$

となるため、隣り合う wall variable は統計的に独立ではない。したがって、境界スピンを入力 bit と見る情報熱力学的解釈では、熱雑音そのものが空間的 memory を持つ。

$$
\boxed{
R=1:\ \text{independent thermal bit flips}
\qquad\longrightarrow\qquad
R=2:\ \text{correlated thermal errors}
}
$$

ここで重要なのは、相関を「情報」と言い換えるだけではないことだ。境界スピン $s_0$ と遠方の $s_r$ の mutual information $I(s_0:s_r)$ は、長距離では支配的な $C(r)$ を通じて減衰する。R=2 の振動領域では $C(r)$ 自体が符号と位相を持って振動する一方、mutual information は相関の符号ではなく予測可能性を測るため、両者は同じ量ではない。

さらに測定と feedback を別途導入するなら、残存 mutual information は $k_BTI$ のスケールで仕事抽出能力を制約する情報資源として解釈できる。ただしこれは平衡 Ising 鎖だけが仕事を生むという意味ではなく、**相関として残った記憶が、適切な情報熱力学プロトコルを追加したときにどの程度の資源になりうるか**という読み方である。

R=2 の新しさは、記憶量の大きさだけでなく、その記憶を運ぶ空間モードが $q=0$ から有限 $q$ へ変わりうる点にある。

## 9. 実空間の振動開始と感受率ピークの移動は同じではない

R=2 では奇 sector に固有値が2本あるため、有限距離の相関関数そのものも2次の空間再帰で閉じる。正規化した奇 sector 固有値を

$$
\mu_\pm\equiv\frac{\lambda_\pm^{(-)}}{\lambda_0}
$$

とし、

$$
a\equiv\mu_++\mu_-,
\qquad
b\equiv\mu_+\mu_-
$$

とおけば、

$$
\boxed{
C(r+2)=aC(r+1)-bC(r)
}
$$

である。$C(0)=1$ と $C(1)=\partial\ln\lambda_0/\partial K_1$ を与えれば、すべての有限距離相関を厳密に生成できる。

ゼロ外場での静的感受率は

$$
\chi(q)
=\beta\sum_{r=-\infty}^{\infty}C(r)e^{-iqr}
=\beta\left[1+2\sum_{r=1}^{\infty}C(r)\cos(qr)\right]
$$

である。ここで二つの波数を区別する必要がある。

- $q_{\mathrm{spec}}\equiv\arg\lambda_+^{(-)}$ は、長距離 tail を支配する転送固有モードの位相である。
- $q_\chi\equiv\operatorname*{arg\,max}_q\chi(q)$ は、全距離の相関を積分した実際の静的応答が最も大きい波数である。

したがって $q_{\mathrm{spec}}$ は漸近的な長距離構造、$q_\chi$ は短距離から長距離までを含めた総合的な応答を表す。両者は一般には一致しない。

$t=1$ では、実固有値が複素共役対へ変わる disorder line は

$$
\kappa_{\mathrm d}\simeq0.217,
$$

一方、$\chi(q)$ の最大が $q=0$ から有限波数へ移る点は数値的に

$$
\kappa_{\mathrm L}\simeq0.322
$$

である。したがって

$$
\boxed{
\kappa_{\mathrm d}<\kappa<\kappa_{\mathrm L}
}
$$

では、実空間相関はすでに減衰振動しているにもかかわらず、静的感受率は依然として $q=0$ で最大となる。

### 3領域を直接比較する

$t=1$ で代表点として $\kappa=0.15,\ 0.27,\ 0.45$ を選ぶ。

![3領域の実空間相関](/figures/ising-r2/three-regimes-correlation.svg)

*$t=1$ における $C(r)$。$\kappa=0.15$ では単調減衰、$\kappa=0.27$ では弱い振動 tail がすでに現れ、$\kappa=0.45$ では符号反転を伴う有限波数構造が明瞭になる。*

$\kappa=0.27$ が重要である。短距離では依然として強磁性的な正相関が支配的だが、遠距離 tail はすでに負へ振れる。つまり「相関が振動するようになった」という変化は、まず長距離側から現れる。

同じ3点について感受率を見ると、

![3領域の波数依存感受率](/figures/ising-r2/three-regimes-susceptibility.svg)

*$t=1$ における規格化感受率。$\kappa=0.15$ と $0.27$ では最大はまだ $q=0$ にあるが、$\kappa=0.45$ では有限波数 $q_\chi/\pi\simeq0.28$ が最も強く応答する。*

したがって R=2 では変化は二段階に分かれる。

$$
\boxed{
\text{monotone correlation}
\longrightarrow
\text{oscillatory tail but }q_\chi=0
\longrightarrow
\text{finite-}q\text{ dominant response}
}
$$

最初の境界では「最も遠くまで残るモード」が変わる。二つ目の境界では、その有限波数モードが短距離構造も含めた総合応答を支配するようになる。

情報熱力学的に言えば、$q_{\mathrm{spec}}$ は**最も遠くまで残る空間的記憶の位相**、$q_\chi$ は**弱い外場によって最も書き込みやすい空間パターン**と読める。R=2 ではその二つが一致しない領域が生まれる。

これは R=1 にはなかった重要な分離である。相互作用範囲を伸ばすことで、単に新しい波数が生まれるだけでなく、**長距離で残る構造と、系全体として最も応答しやすい構造が別々の概念になる**。

## まとめ

$R=2$ への最小拡張は、三つの言葉で同じ構造を表せる。

$$
\boxed{
\begin{aligned}
\text{spin picture}:&\quad \text{second-neighbor competition}\\
\text{wall picture}:&\quad \text{interacting domain walls}\\
\text{transfer spectrum}:&\quad \text{complex subleading modes}
\end{aligned}
}
$$

その結果、相関は単純な指数減衰から

$$
C(r)\sim e^{-r/\xi}\cos(q_*r+\phi)
$$

へ進み、R=1 にはなかった有限波数 $q_*$ が現れる。さらに、長距離 tail の位相 $q_{\mathrm{spec}}$ と感受率ピーク $q_\chi$ は一般には一致せず、実空間の振動開始と有限波数応答の支配化が二段階に分かれる。

したがって R=2 は、**相互作用範囲を一つ伸ばしただけで、長距離記憶の「量」だけでなく「空間的な運び方」まで変わる最小模型**として読むことができる。

---
title: "Nash–Bertrand 均衡 — 値下げ競争はどこで止まるのか"
summary: "イベント会場の水売り場と差別化されたスマートフォン市場を実際に計算しながら、Bertrand競争、供給能力制約、Nash均衡、markup、品質調整価格Zの意味をつなぐ。"
publishedAt: 2026-09-14T00:30:00+09:00
updatedAt: 2026-09-14
area: "Economics"
topics: ["Nash equilibrium", "Bertrand competition", "capacity constraints", "pricing", "product differentiation", "logit model"]
status: growing
---

品質調整価格

$$
Z=p-\theta q
$$

まで考えると、次に残るのは価格そのものの内生性である。

競争が価格を下げるとしても、どこまで下がるかは商品差別化と供給能力で変わる。Nash–Bertrand は、その停止点を**互いの最適反応の固定点**として書く。

## 1. 同質財では $p=c$ が極端な基準になる

同じ水を売るA店とB店を考え、どちらも限界費用を100円とする。

Aが120円、Bが119円なら、完全に同じ商品なら需要はBへ流れる。Aは118円にしたくなり、Bもさらに下げたくなる。

安い側が市場全体を供給できるなら、この圧力は

$$
\boxed{p^*=c}
$$

まで続く。

二社しかなくても完全競争のような価格になる、Bertrand paradox の基準像である。

ただし、この結果には「安い企業が全需要を引き受けられる」という強い仮定が入っている。

## 2. capacity constraint は残余需要を残す

来場者140人、A店は120円だが在庫100本、B店の限界費用は100円とする。全員の支払意思額は180円とする。

Bが120円以下なら140人を取れるので

$$
\pi_B=(p_B-100)\times140.
$$

一方 $120<p_B\le180$ でも、Aは100本で売り切れるため40人の残余需要が残る。

$$
\pi_B=(p_B-100)\times40.
$$

例えば

$$
\pi_B(120)=2800,
\qquad
\pi_B(180)=3200.
$$

となり、Aより高く売る方がBには有利になる。

![供給能力制約がある水市場でのB店の利潤](/figures/nash-bertrand-price-competition/capacity-residual-demand.svg)

*安いA店が売り切れると、B店には残余需要が残る。価格差があっても需要がゼロにならない。*

供給能力 $K_i$ を明示すれば

$$
Q_i\le K_i
$$

という制約が入る。

したがって $p=c$ は競争一般の結論ではなく、**同質財・完全代替・十分な供給能力**がそろった極限である。

## 3. Nash–Bertrand は price best-response の fixed point である

Bertrand は価格を戦略変数にする競争、Nash は互いの戦略が同時に最適反応になっている状態を表す。

二社なら

$$
p_A^{\mathrm{BR}}=R_A(p_B),
\qquad
p_B^{\mathrm{BR}}=R_B(p_A)
$$

で、均衡は

$$
\boxed{
p_A^*=R_A(p_B^*),
\qquad
p_B^*=R_B(p_A^*)}
$$

を満たす。

社会全体の最適価格という意味ではなく、**一社だけ価格を動かしても利潤を増やせない固定点**である。

## 4. 商品差別化は需要を滑らかにする

スマートフォンのように品質・OS・デザイン・ブランドが違えば、1円の値下げで全需要が移るわけではない。

$$
U_i=V_i+\varepsilon_i,
\qquad
V_i=\beta q_i-\alpha p_i
$$

とし、$\varepsilon_i$ をGumbel型にすると

$$
\boxed{
s_i=
\frac{e^{V_i/\lambda}}
{1+\sum_j e^{V_j/\lambda}}}
$$

となる。分母の1はoutside optionである。

値上げしても需要が連続的に減るだけなので、企業には限界費用を上回るmarkupの余地が生まれる。

## 5. markup は own-price sensitivity で決まる

市場規模を $M$、限界費用を $c_i$ とすると

$$
\pi_i=M(p_i-c_i)s_i(\mathbf p).
$$

一階条件は

$$
\boxed{
p_i-c_i
=-\frac{s_i}{\partial s_i/\partial p_i}}
$$

である。

logit では

$$
\frac{\partial s_i}{\partial p_i}
=-\frac{\alpha}{\lambda}s_i(1-s_i)
$$

なので

$$
\boxed{
p_i-c_i
=\frac{\lambda}{\alpha(1-s_i)}}
$$

となる。

値上げしたときにどれだけ需要を失うかが、markupを直接決める。

## 6. 二つのスマホでは best response が交点を作る

例として

|  | A | B |
| --- | ---: | ---: |
| 品質 $q$ | 9 | 7 |
| 限界費用 $c$ | 55 | 40 |

とし

$$
\alpha=0.1,
\qquad
\beta=1,
\qquad
\lambda=1
$$

を置く。

最適反応を同時に解くと

$$
p_A^*\approx74.68,
\qquad
p_B^*\approx56.71
$$

で、シェアは

$$
s_A^*\approx0.492,
\qquad
s_B^*\approx0.402,
\qquad
s_0^*\approx0.106.
$$

markup は

$$
p_A^*-c_A\approx19.68,
\qquad
p_B^*-c_B\approx16.71.
$$

![AとBのbest response曲線](/figures/nash-bertrand-price-competition/best-response-intersection.svg)

*二本のbest response曲線の交点が、双方が同時に最適反応になっているNash–Bertrand均衡。*

競合が値上げすると自社へ需要が流れ、その結果自社にも値上げ余地ができる。

$$
p_B\uparrow
\Rightarrow
s_A\uparrow
\Rightarrow
p_A^{\mathrm{BR}}\uparrow.
$$

価格は

$$
\boxed{
\mathbf p
\longrightarrow
\mathbf s(\mathbf p)
\longrightarrow
\mathbf p}
$$

という固定点を作る。

## 7. $p$ を $Z$ に写すと、価格差の見え方が変わる

この例では

$$
\theta=\frac{\beta}{\alpha}=10
$$

なので

$$
Z_A=p_A^*-10q_A\approx-15.32,
$$

$$
Z_B=p_B^*-10q_B\approx-13.29.
$$

実価格だけを見ると

$$
p_A-p_B\approx17.97
$$

とかなり差がある。一方、品質価値 $\theta q_i$ を差し引いて比較すると

$$
|Z_A-Z_B|\approx2.03
$$

まで縮む。

![実価格から品質調整価格への変換](/figures/nash-bertrand-price-competition/price-vs-quality-adjusted-price.svg)

*実価格の差の多くは品質差を補正すると消える。ただし $Z_A=Z_B$ にはならず、均衡markupや費用差などの寄与が残る。*

ここで重要なのは、$p$ と $Z$ を別々の量として大小比較することではない。見るべきなのは

$$
\boxed{p_i\longrightarrow Z_i=p_i-\theta q_i}
$$

という変換で、商品間の距離がどう変わるかである。

$\gamma=\alpha/\lambda$ とおけば価格条件は

$$
\boxed{
Z_i
=c_i-\theta q_i
+\frac{1}{\gamma(1-s_i)}}
$$

となる。

$$
Z_i
=\underbrace{c_i-\theta q_i}_{\text{費用と品質}}
+\underbrace{\frac{1}{\gamma(1-s_i)}}_{\text{markup}}
$$

という分解である。

したがって観測される $Z$ の分散は、市場が均衡していないことだけでは説明できない。費用、品質、代替可能性、市場支配力が違えば、**均衡そのものに $Z$ の幅が残る**。

## 8. capacity を戻すと価格 fixed point に供給能力も入る

供給能力が有限なら、低い $Z$ を持つ商品でも売り切れた時点で残余需要が他社へ流れる。

短期には

$$
s_i=s_i(\mathbf Z;\mathbf K)
$$

と書く方が自然になる。

長期には $K_i$ も設備投資によって内生化されうる。

つまり価格は

$$
\boxed{
\text{cost}
+\text{substitutability}
+\text{market share}
+\text{capacity}}
$$

の固定点として決まる。

さらに品質 $q_i$ 自体も企業が選ぶなら、戦略変数は $p_i$ だけでなく $(p_i,q_i)$ へ広がる。価格競争と商品設計はそこで同じ最適化問題へつながる。

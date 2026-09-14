---
title: "複数商品企業は競合をどう見るか — 所有構造・diversion・商品ライン設計"
summary: "Basic・Standard・Proを持つ企業Aと、単独商品Xを持つ企業Bを例に、需要の代替関係だけでなく『誰がどの商品を所有しているか』が価格と品質設計をどう変えるかを整理する。ownership matrix、diversion ratio、multi-product pricing を通じて、競争が商品ライン全体へ伝わる理由を見る。"
publishedAt: 2026-09-14T02:15:00+09:00
updatedAt: 2026-09-14
area: "Economics"
topics: ["multiproduct firm", "ownership matrix", "diversion ratio", "product line", "pricing", "product differentiation"]
status: growing
---

一つの企業が Basic・Standard・Pro を同時に売っているとき、三つの商品は単純な競争相手ではない。

Standard の客が Pro へ移っても企業Aの顧客であることは変わらない。一方、競合企業の商品 $X$ へ移れば、その需要は企業Aから失われる。

したがって競争の強さは商品間距離だけでは決まらず

$$
\boxed{
\text{代替先の商品を誰が所有しているか}}
$$

まで含めて考える必要がある。

## 1. 需要構造が同じでも ownership が価格条件を変える

企業Aが Basic・Standard・Pro、企業Bが商品 $X$ を持つとする。

企業Aの利潤は

$$
\pi_A
=\sum_{i\in A}(p_i-c_i)Q_i(\mathbf p)
$$

である。

Standard の価格 $p_S$ を少し上げると、その需要の一部は Basic、Pro、$X$ へ流れる。

自社内の Basic・Pro へ移った需要は企業A全体では回収されるが、$X$ へ移った需要は失われる。

したがって価格条件は

$$
Q_S
+\sum_{i\in A}(p_i-c_i)
\frac{\partial Q_i}{\partial p_S}
=0
$$

となる。

需要関数だけでなく、**どのcross-price effectを自社利潤として内部化するか**が価格を決めている。

## 2. ownership matrix は内部化する代替関係を選ぶ

商品 $i,j$ が同じ企業に属するかを

$$
\Omega_{ij}
=\begin{cases}
1,&i,j\text{ が同じ企業},\\
0,&\text{別企業}
\end{cases}
$$

とする。

商品 $j$ の価格一階条件は

$$
\boxed{
Q_j
+\sum_i\Omega_{ij}(p_i-c_i)
\frac{\partial Q_i}{\partial p_j}
=0}
$$

である。

需要関数や費用を変えなくても $\Omega$ を変えるだけで均衡価格が変わる。

企業合併が価格へ効くのも、代替関係そのものが急に変わるからではなく、**以前は外部だった需要移動が同じ企業内へ取り込まれる**からだと読める。

## 3. diversion ratio は「失った客がどこへ行くか」を測る

Standard の値上げで失われる需要のうち

- 40% が Basic
- 20% が Pro
- 30% が競合 $X$
- 10% が市場退出

するとする。

企業Aが内部で回収できるのは Basic と Pro へ流れた60%である。

需要流出を

$$
\boxed{
D_{j\to i}
=\frac{\partial Q_i/\partial p_j}
{-\partial Q_j/\partial p_j}}
$$

と書けば、競争の強さは単なる品質距離 $|q_i-q_j|$ よりも直接的に表せる。

品質が近くても diversion が小さければ弱い競合であり、品質が多少離れていても diversion が大きければ強い競合になる。

## 4. multi-product markup は portfolio 全体で決まる

単一商品企業なら

$$
Q_j+(p_j-c_j)\frac{\partial Q_j}{\partial p_j}=0
$$

で、自商品の需要損失だけを見ればよい。

複数商品企業では、値上げで失った需要の一部を自社別商品で回収できる。そのため各価格は

$$
\boxed{\text{portfolio profit}}
$$

を最大化する条件で決まる。

競合 $X$ が Standard に近くても、Standard だけを値下げすればよいとは限らない。Standard の価格変更は Basic・Pro との cannibalization も変えるからである。

## 5. 一つの競合参入が商品ライン全体を repricing する

3タイプの消費者を使った数値例では、企業Aだけなら

$$
(p_B,p_S,p_P)
\simeq(4.59,13.13,50.90)
$$

だった。

中間品質の商品 $X$ を一つ入れると

$$
(p_B,p_S,p_P)
\simeq(3.42,7.24,39.09)
$$

へ動いた。

![競合参入前後の価格変化](/figures/multiproduct-competitor-repositioning/competitor-entry-price-response.svg)

*競合がStandard近傍へ入っても、反応はStandard一商品に閉じず、Basic・Proまで同時に動く。*

この変化は

$$
\boxed{
\text{ownership}
\longrightarrow
\text{internalized substitution}
\longrightarrow
\text{portfolio-wide repricing}}
$$

という因果鎖で整理できる。

## 6. 品質を動かすと cannibalization と competitor stealing が競合する

品質 $q_i$ も企業が選ぶなら

$$
\pi_A
=\sum_{i\in A}[p_i-c_i(q_i)]Q_i(\mathbf p,\mathbf q)
$$

である。

商品 $j$ の品質を変えたとき

$$
\frac{\partial\pi_A}{\partial q_j}
=\sum_{i\in A}(p_i-c_i)
\frac{\partial Q_i}{\partial q_j}
-Q_jc_j'(q_j)
$$

となる。

Standard を良くして増えた需要が Basic・Pro から移っただけなら自社内 cannibalization であり、競合 $X$ から奪った需要なら企業A全体の純増になる。

$$
\boxed{
\text{internal cannibalization}
\quad\text{vs}\quad
\text{competitor stealing}}
$$

の釣り合いが商品ラインの品質配置を決める。

## 7. 競合の位置は最寄り商品だけでなくライン全体を動かす

競合 $X$ が低品質側なら Basic、中間なら Standard、高品質側なら Pro が直接競争しやすい。

しかし企業Aは商品単体ではなく portfolio 全体の利潤を見ているため、反応は最寄り商品一つには閉じない。

![競合品質に対する商品ラインの再配置](/figures/multiproduct-competitor-repositioning/competitor-quality-sweep.svg)

*競合品質を動かすと、Basic・Standard・Pro の価格と品質が連動して再配置される。*

$$
\boxed{
\text{競争は product vs product だけでなく portfolio vs product でも起こる}}
$$

という構造がここにある。

## 8. $Z$ 空間では競合が作る地形に自社商品を配置する問題になる

消費者タイプ $t$ にとって

$$
Z_{ti}=p_i-\theta_tq_i
$$

とする。

企業Aは自社商品の

$$
Z_{tB},\qquad Z_{tS},\qquad Z_{tP}
$$

を価格と品質の両方から動かせるが、競合 $X$ の

$$
Z_{tX}
$$

は直接制御できない。

したがって商品ライン設計は

$$
\boxed{
\text{external competitor landscape }Z_{tX}
\text{ の中へ自社の }Z_{ti}\text{ を配置する問題}}
$$

と見られる。

この見方なら

- 競合から距離を取る
- 競合を自社商品の間で挟む
- ある顧客層を競合へ譲る
- 別の顧客層へ集中する

といった戦略を同じ座標で扱える。

## 9. ownership と diversion が product-line design までつながる

単一商品企業では

$$
\pi_i=(p_i-c_i)Q_i
$$

だけだった。

複数商品所有を入れると

$$
\boxed{
\text{demand substitution}
+\text{ownership structure}}
$$

が価格を決める。

品質も内生化すると、同じ代替構造が商品ライン設計まで伝わる。

$$
\boxed{
\text{single-product pricing}
\longrightarrow
\text{ownership matrix}
\longrightarrow
\text{diversion ratios}
\longrightarrow
\text{portfolio pricing}
\longrightarrow
\text{product-line design}}
$$

という一本の構造になる。

企業が「何を売るか」と「いくらで売るか」は別問題ではなく、同じ需要代替ネットワーク上の最適化として結びついている。

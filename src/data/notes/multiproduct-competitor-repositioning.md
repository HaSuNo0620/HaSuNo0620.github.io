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

Standard の客が Pro へ移っても、その客は企業Aから消えたわけではない。一方で Standard の客が別企業の商品 $X$ へ移れば、それは本当の失客になる。

ここで重要なのは、商品の似かたそのものだけではない。

$$
\boxed{\text{代替先の商品を誰が所有しているか}}
$$

である。

この違いをはっきりさせると、複数商品企業の価格設定や商品ライン設計がかなり見通しよくなる。

## 1. 同じ需要構造でも、所有者が違えば価格は変わる

企業Aが Basic・Standard・Pro を持ち、企業Bが商品 $X$ を一つ持つとする。

企業Aの利潤は

$$
\pi_A
=
\sum_{i\in A}(p_i-c_i)Q_i(\mathbf p)
$$

である。

Standard の価格 $p_S$ を少し上げると、Standard の需要は減る。その一部は Basic へ、一部は Pro へ、一部は $X$ へ流れる。

企業Aにとって、Basic や Pro へ移った客は完全な損失ではない。自社内で売上が移っただけだからである。しかし $X$ へ移った客は回収できない。

そのため Standard の価格条件は

$$
Q_S
+
\sum_{i\in A}
(p_i-c_i)
\frac{\partial Q_i}{\partial p_S}
=0
$$

となる。

ここで $X$ の項

$$
(p_X-c_X)\frac{\partial Q_X}{\partial p_S}
$$

は企業Aの利潤には入らない。

同じ需要関数でも、Standard と Pro が同じ会社の商品なのか、別会社の商品なのかで最適価格が変わる。

つまり、価格決定には需要曲線だけでなく**所有構造**が必要になる。

## 2. ownership matrix で所有構造を式に入れる

商品 $i$ と $j$ が同じ企業に属するかどうかを

$$
\Omega_{ij}
=
\begin{cases}
1 & i,j\text{ が同じ企業},\\
0 & \text{別企業}
\end{cases}
$$

で表す。

すると商品 $j$ の価格についての一階条件は

$$
\boxed{
Q_j+
\sum_i
\Omega_{ij}(p_i-c_i)
\frac{\partial Q_i}{\partial p_j}
=0
}
$$

と書ける。

この式の面白いところは、需要関数 $Q_i(\mathbf p)$ を何も変えなくても、$\Omega$ を変えるだけで均衡価格が変わることである。

商品の性能も、消費者も、生産費用も同じまま、二つの商品が同じ会社の所有になっただけで価格設定が変わる。

企業合併が市場価格へ効く理由も、この式の延長にある。

## 3. どこへ客が逃げるかを見るのが diversion ratio

Standard を値上げしたとき、失われた需要がどこへ流れるかを考える。

例えば Standard から離れた客のうち

- 40% が Basic
- 20% が Pro
- 30% が競合 $X$
- 10% が市場から退出

するとする。

企業Aが回収できるのは Basic と Pro へ流れた 60% である。競合 $X$ へ流れた 30% は本当の失客になる。

この「ある商品から失われた需要のうち、どれだけが別の商品へ向かうか」を diversion ratio で表す。

符号を分かりやすく取れば、

$$
\boxed{
D_{j\to i}
=
\frac{\partial Q_i/\partial p_j}
{-\partial Q_j/\partial p_j}
}
$$

である。

すると競合の強さは、単に

$$
|q_X-q_S|
$$

が小さいかどうかではない。

$$
\boxed{\text{Standard を値上げしたとき、どれだけ客が }X\text{ へ流れるか}}
$$

で測る方が経済学的には直接的である。

品質が近くてもほとんど客が移らない商品なら弱い競合であり、多少離れていても大量に客を奪うなら強い競合である。

## 4. 単一商品企業と複数商品企業では markup の意味が違う

単一商品企業なら、商品 $j$ の価格を上げて需要を失えば、その需要はほぼそのまま企業の損失になる。

だから

$$
Q_j+(p_j-c_j)\frac{\partial Q_j}{\partial p_j}=0
$$

という自商品だけの条件になる。

複数商品企業では、値上げで失った需要の一部を自社の別商品で回収できる。

したがって、企業は商品一つずつの利益ではなく、

$$
\boxed{\text{商品ポートフォリオ全体の利益}}
$$

を見て価格を決める。

そのため競合 $X$ が Standard の近くに入ったとしても、Standard だけを値下げすれば済むとは限らない。Standard を値下げすると Basic や Pro とのカニバリゼーションも変わるからである。

一つの競合の参入が

$$
(p_B,p_S,p_P)
$$

全体へ伝わるのはこのためである。

## 5. 数値例では、競合一つでライン全体の価格が動いた

この構造を具体的に見るため、前のノートと同じ3タイプの消費者を使い、A社が Basic・Standard・Pro、B社が単独商品 $X$ を持つ例を計算した。

A社だけなら、あるパラメータでは

$$
(p_B,p_S,p_P)
\simeq
(4.59,13.13,50.90)
$$

だった。

中間品質の商品 $X$ を一つ入れると、

$$
(p_B,p_S,p_P)
\simeq
(3.42,7.24,39.09)
$$

へ下がった。

![競合参入前後の価格変化](/figures/multiproduct-competitor-repositioning/competitor-entry-price-response.svg)

重要なのは Standard だけが反応していないことである。

競合 $X$ は直接には Standard に近くても、A社は三商品の利潤をまとめて見ているため、Basic と Pro の価格も同時に動く。

この数値例は、理論で見た

$$
\text{ownership}
\rightarrow
\text{internalized substitution}
\rightarrow
\text{portfolio-wide repricing}
$$

を具体化したものと読める。

## 6. 品質を動かせると、問題は価格競争から商品ライン設計へ変わる

次に品質 $q_i$ も企業が選べるとする。

企業Aの利潤は

$$
\pi_A
=
\sum_{i\in A}
[p_i-c_i(q_i)]Q_i(\mathbf p,\mathbf q)
$$

である。

商品 $j$ の品質を少し変えたとき、利潤変化は概念的には

$$
\frac{\partial\pi_A}{\partial q_j}
=
\sum_{i\in A}
(p_i-c_i)
\frac{\partial Q_i}{\partial q_j}
-
Q_j c_j'(q_j)
$$

となる。

ここでも、自社商品間の需要移動は内部化される。

Standard を良くすると Standard 自体の需要は増える。しかしその一部は Basic や Pro から奪っただけかもしれない。一方、競合 $X$ から奪った需要なら企業Aにとって純増である。

したがって品質変更には

$$
\boxed{
\text{自社内カニバリゼーション}
\quad\text{vs}\quad
\text{他社からの需要獲得}
}
$$

という二つの効果が同時に入る。

企業は商品単体で最適な品質を選ぶのではなく、商品ライン全体として最適な品質配置を選ぶ。

## 7. 競合の位置によって、守る商品も変わる

競合 $X$ が低品質側にいれば Basic が直接競争しやすい。中間にいれば Standard だけでなく Basic と Pro の両側の需要にも触れる。高品質側なら Pro が直接競争する。

しかし、どの場合も反応は最も近い商品一つには閉じない。

![競合品質に対する商品ラインの再配置](/figures/multiproduct-competitor-repositioning/competitor-quality-sweep.svg)

この数値例では、競合品質を動かすと Basic・Standard・Pro の品質と価格がまとめて動いた。

ここで大事なのは、細かな局所均衡の数値そのものではない。

$$
\boxed{
\text{競争は商品対商品ではなく、ポートフォリオ対商品でも起こる}
}
$$

という構造である。

A社は Standard と $X$ だけを比較しているのではなく、Basic・Standard・Pro 全体を使って、競合に対する需要流出を最小化しようとしている。

## 8. $Z$ で見ると、競合が作る地形に商品を置いている

消費者タイプ $t$ にとっての品質調整価格を

$$
Z_{ti}=p_i-\theta_t q_i
$$

とする。

A社は、自社の

$$
Z_{tB},\qquad Z_{tS},\qquad Z_{tP}
$$

を価格と品質を通じて動かせる。

しかし競合 $X$ の

$$
Z_{tX}
$$

はA社には直接制御できない。

したがってA社の商品ライン設計は、

$$
\boxed{
\text{外部にある }Z_{tX}\text{ を見ながら、自社の }Z_{ti}\text{ を配置する問題}
}
$$

と見られる。

この見方なら、

- 競合から距離を取る
- 競合を自社商品の間で挟む
- ある顧客層は競合へ渡す
- 別の顧客層だけを強く取りに行く

といった商品ライン戦略を同じ枠組みで考えられる。

## 9. ここで見えた一般化

最初は単一商品企業の価格競争だった。

$$
\pi_i=(p_i-c_i)Q_i
$$

そこへ複数商品所有を入れると、代替関係の一部が企業内部へ取り込まれる。

$$
\boxed{
\text{需要の代替構造}
+
\text{所有構造}
}
$$

が価格を決めるようになる。

さらに品質を動かせると、企業は価格だけでなく商品ラインそのものを設計する。

したがって流れは

$$
\boxed{
\text{single-product pricing}
\rightarrow
\text{ownership matrix}
\rightarrow
\text{diversion ratio}
\rightarrow
\text{multi-product pricing}
\rightarrow
\text{product-line design}
}
$$

となる。

ここまで来ると、企業が「何を売るか」と「いくらで売るか」を別々に考えることはできない。

競合が一つ入るだけでも、価格だけではなく商品ライン全体の意味が変わる。

次に進めるなら、diversion ratio を logit モデルから明示的に導いて、ownership matrix と合わせると markup ベクトルがどう決まるかを行列表現で整理するのが自然である。

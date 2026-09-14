---
title: "消費者の商品選択と価格形成 — 最安値を選ばないところから市場均衡まで"
summary: "教科書的な需要供給曲線を基準に、なぜ現実の消費者は最安値だけを選ばないのかを具体例から考え、品質調整価格Z、嗜好差、確率的選択へ広げる。"
publishedAt: 2026-09-13T21:50:00+09:00
updatedAt: 2026-09-14
area: "Economics"
topics: ["consumer choice", "supply and demand", "random utility", "discrete choice", "logit model", "pricing"]
status: growing
---

スーパーの棚に100円、120円、150円の商品が並んでいる。中身が完全に同じなら100円だけが売れそうだが、現実にはそうならない。

違和感の置き場所は「なぜ合理的に最安値を選ばないのか」ではなく、**消費者が何を比較しているのか**にある。

価格だけの市場を基準に置き、品質や嗜好を戻すと、比較変数そのものが変わっていく。

## 1. 同質財では均衡価格 $p^*$ が基準になる

一つの同質な財について

$$
Q_D(p),
\qquad
Q_S(p)
$$

を需要と供給とすると、均衡価格は

$$
\boxed{Q_D(p^*)=Q_S(p^*)}
$$

で決まる。

この理想化では、同じ財なのに店Aは100円、店Bは120円という差は残りにくい。買い手が安い方へ移るからである。

$$
\boxed{p_i\to p^*}
$$

という一物一価の圧力が、最小の基準像になる。

## 2. 品質差は比較変数を $p$ から $Z=p-\theta q$ へ変える

価格だけでなく性能 $q_i$ が違うとする。

| 商品 | 価格 $p$ | 性能 $q$ |
| --- | ---: | ---: |
| A | 100 | 1.0 |
| B | 120 | 1.5 |
| C | 150 | 2.0 |

効用を

$$
U_i=\beta q_i-\alpha p_i
$$

とし

$$
\theta=\frac{\beta}{\alpha}
$$

とおけば、効用最大化は

$$
\boxed{Z_i=p_i-\theta q_i}
$$

の最小化と同じになる。

$Z$ は品質を価格換算して差し引いた「品質調整価格」と読める。

$\theta=40$ なら

$$
Z_A=60,
\qquad
Z_B=60,
\qquad
Z_C=70,
$$

$\theta=60$ なら

$$
Z_A=40,
\qquad
Z_B=30,
\qquad
Z_C=30.
$$

高価格の商品を選ぶこと自体は非合理ではない。比較している量が

$$
\boxed{p\longrightarrow Z=p-\theta q}
$$

へ変わっている。

## 3. 一物一価は理想化すれば $Z_i\to Z^*$ へ移る

全員が同じ $\theta$ を持ち、品質を完全に観測でき、品質以外では商品が完全代替だとする。

もし

$$
Z_A<Z_B
$$

なら、品質調整後でもAの方が割安なので需要はAへ移る。

この理想化を押し切れば

$$
\boxed{Z_i\to Z^*}
$$

という品質調整後の一物一価が考えられる。

したがって

$$
p_i=Z^*+\theta q_i.
$$

高品質な商品ほど高価格でもよいが、品質価値を差し引いた残りは共通になる。

## 4. 品質には限界価値と限界費用の釣り合いが入る

品質 $q$ の生産費用を $C(q)$ とし

$$
p=Z+\theta q
$$

と書けば、1単位あたりの利潤は

$$
\pi=Z+\theta q-C(q)
$$

である。

品質選択の一階条件は

$$
\frac{d\pi}{dq}
=\theta-C'(q)=0
$$

なので

$$
\boxed{C'(q^*)=\theta}
$$

となる。

消費者が品質1単位へ置く限界価値と、企業が品質を1単位増やす限界費用が一致する。

ここでは価格差の問題が、そのまま商品設計の問題へつながっている。

## 5. 嗜好差は共通の $Z$ 軸そのものを壊す

現実には品質を補正しても、商品が一つの $Z^*$ へ潰れるとは限らない。

消費者 $n$ ごとに品質評価が違えば

$$
\boxed{Z_{ni}=p_i-\theta_n q_i}
$$

となる。

AとBのどちらが割安かが人によって変わるため、市場全体に一つの共通 $Z_i$ を割り当てること自体が近似になる。

$$
\boxed{
\text{heterogeneous taste}
\Longrightarrow
\text{comparison axis becomes consumer dependent}}
$$

という変化である。

## 6. random utility は一点選択を確率分布へ変える

ブランド嗜好や細かな仕様差、その日の状況まで全て観測するのは難しい。

そこで

$$
U_i=V_i+\varepsilon_i
$$

と分ける。$V_i$ は観測された価格・品質、$\varepsilon_i$ は未観測成分である。

$\varepsilon_i$ を独立な Gumbel 分布とすると

$$
s_i
=\frac{\exp(V_i/\lambda)}
{\sum_j\exp(V_j/\lambda)}.
$$

$V_i=-\alpha Z_i$、$\gamma=\alpha/\lambda$ とすれば

$$
\boxed{
s_i
=\frac{e^{-\gamma Z_i}}
{\sum_j e^{-\gamma Z_j}}}
$$

となる。

$\gamma\to\infty$ では最小 $Z$ に選択が集中し、有限 $\gamma$ では少し高い $Z$ にも需要が残る。

数学的には Gibbs 型の指数重みと同じ形だが、$\gamma$ を物理的逆温度と同一視する必要はない。

一点の最適商品から

$$
\boxed{\text{choice}\longrightarrow\text{choice distribution}}
$$

へ移ったと見ればよい。

## 7. 選択確率は企業側から見れば需要になる

市場規模を $M$ とすれば

$$
Q_i=Ms_i.
$$

限界費用を $c_i$ とすると

$$
\pi_i=M(p_i-c_i)s_i(\mathbf p).
$$

最適価格条件は

$$
\boxed{
p_i-c_i
=-\frac{s_i}{\partial s_i/\partial p_i}}
$$

である。

ここで価格は外から与える数字ではなくなる。

$$
\boxed{
\mathbf p
\longrightarrow
\mathbf s(\mathbf p)
\longrightarrow
\mathbf p}
$$

という feedback が生じる。

価格が消費者選択を作り、その選択分布が企業の最適価格を作り返す。

## 8. 一点均衡から分布と固定点へ

最初の基準像は

$$
Q_D(p^*)=Q_S(p^*)
$$

だった。

品質差を戻すと

$$
p\longrightarrow Z=p-\theta q,
$$

嗜好差を戻すと $Z$ は消費者依存になり、未観測要因を残すと選択は確率分布になる。

さらに企業最適化まで戻すと

$$
\boxed{
\text{price}
\to
\text{choice probabilities}
\to
\text{demand}
\to
\text{optimal price}}
$$

という fixed-point structure が現れる。

ここでまだ外に置いているのは、消費者が品質 $q_i$ をどれだけ正確に知っているかである。

品質を広告、レビュー、検索、試用を通してしか知れないなら、比較対象は $Z_i$ そのものではなく

$$
P(Z_i\mid\text{information})
$$

になる。

価格形成と情報取得をつなぐなら、この条件付き分布が次の自由度になる。

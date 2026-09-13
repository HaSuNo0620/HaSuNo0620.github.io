---
title: "Nash–Bertrand 均衡 — 複数企業の価格はどう決まるのか"
summary: "Bertrand競争とNash均衡を分けて定義し、複数企業が互いの価格を所与として最適反応を選ぶとき、価格がbest responseの固定点として決まることを見る。"
publishedAt: 2026-09-14T00:30:00+09:00
updatedAt: 2026-09-14
area: "Economics"
topics: ["Nash equilibrium", "Bertrand competition", "pricing", "discrete choice", "logit model", "industrial organization"]
status: growing
---

前のノートでは、同質財の価格 $p$ を品質調整済み価格

$$
Z=p-\theta q
$$

へ一般化した。

次に知りたいのは、複数企業が互いの価格を見ながら価格を決めるとき、均衡がどう決まるかである。

## 1. Bertrand と Nash は何を意味するのか

**Bertrand 競争**は、企業が価格を戦略変数として競争するモデルである。

企業 $i$ の利潤を

$$
\pi_i(p_i,\mathbf p_{-i})
$$

と書く。$\mathbf p_{-i}$ は他社の価格である。企業 $i$ は他社価格を所与として、自社価格を選ぶ。

$$
p_i^{\mathrm{BR}}(\mathbf p_{-i})
=
\operatorname*{arg\,max}_{p_i}\pi_i(p_i,\mathbf p_{-i}).
$$

これが best response である。

一方、**Nash 均衡**は、すべての企業の現在の戦略が互いに最適反応になっている状態である。

$$
\boxed{
p_i^*=p_i^{\mathrm{BR}}(\mathbf p_{-i}^*)
\qquad \forall i
}
$$

したがって Nash–Bertrand 均衡とは、価格を競争変数とした Nash 均衡である。

ここで大事なのは、Nash 均衡は社会全体にとって最適という意味ではないことである。各企業が、自分だけ価格を変えても利潤を増やせない状態にあるだけである。

## 2. 二社なら best response の交点

企業AとBが一商品ずつ売るとする。

$$
\pi_A=(p_A-c_A)Q_A(p_A,p_B),
$$

$$
\pi_B=(p_B-c_B)Q_B(p_A,p_B).
$$

Aは

$$
p_A^*=R_A(p_B)
$$

を選び、Bは

$$
p_B^*=R_B(p_A)
$$

を選ぶ。

均衡では

$$
\boxed{
\begin{aligned}
p_A^*&=R_A(p_B^*),\\
p_B^*&=R_B(p_A^*).
\end{aligned}
}
$$

となる。

つまり Nash–Bertrand 均衡は best response 曲線の交点であり、

$$
\mathbf p=\mathbf F(\mathbf p)
$$

という fixed-point problem として書ける。

## 3. 同質財では価格は限界費用まで下がる

二社が同じ商品を同じ限界費用 $c$ で売り、消費者が安い方から必ず買うとする。

もし $p_A>p_B$ ならAの需要はゼロになる。だからAはBより少しだけ安くしたくなる。Bも同じことをする。

その値下げは、これ以上下げると赤字になるところまで続く。

$$
\boxed{p_A^*=p_B^*=c}
$$

二社しかいなくても完全競争と同じ価格になる。この強い結果は、商品が同質、完全情報、容量制約なし、切替コストなしという仮定に依存する。

## 4. 差別化商品では需要は滑らかになる

現実には少し値上げしただけで全顧客を失うわけではない。

商品 $i$ の効用を

$$
U_i=V_i+\varepsilon_i,
\qquad
V_i=v_i-\alpha p_i
$$

とする。

$\varepsilon_i$ を独立な Gumbel 分布とすれば、logit の市場シェアは

$$
s_i
=
\frac{e^{V_i/\lambda}}
{1+\sum_j e^{V_j/\lambda}}.
$$

価格を少し上げても $s_i$ は急にゼロにならず、滑らかに減る。これが企業に markup を残す。

## 5. 企業の最適価格条件

市場規模を $M$、限界費用を $c_i$ とすると、

$$
\pi_i=M(p_i-c_i)s_i(\mathbf p).
$$

一階条件は

$$
s_i+(p_i-c_i)\frac{\partial s_i}{\partial p_i}=0.
$$

したがって一般に

$$
\boxed{
p_i-c_i
=-\frac{s_i}{\partial s_i/\partial p_i}
}
$$

となる。

logit では

$$
\frac{\partial s_i}{\partial p_i}
=-\frac{\alpha}{\lambda}s_i(1-s_i),
$$

だから

$$
\boxed{
p_i-c_i
=\frac{\lambda}{\alpha(1-s_i)}
}
$$

である。

markup は、値上げしたときにどれだけ顧客を失うかで決まる。

## 6. 価格は自分自身へ戻ってくる

ただし $s_i$ は全企業の価格に依存する。

$$
s_i=s_i(\mathbf p).
$$

したがって

$$
\boxed{
p_i
=c_i+
\frac{\lambda}{\alpha[1-s_i(\mathbf p)]}
}
$$

である。

全企業についてこの条件を同時に満たす価格ベクトルが Nash–Bertrand 均衡になる。

$$
\boxed{
\mathbf p
\longrightarrow
\mathbf s(\mathbf p)
\longrightarrow
\mathbf p
}
$$

価格を変えると需要が変わり、その需要の変化が最適価格を変える。その価格が再び需要へ戻る。

## 7. 競合価格も自社価格に効く

logit では $j\neq i$ に対して

$$
\frac{\partial s_i}{\partial p_j}
=
\frac{\alpha}{\lambda}s_is_j>0.
$$

競合が値上げすると自社シェアが増える。すると自社も高い markup を取りやすくなる。

$$
p_j\uparrow
\Rightarrow
s_i\uparrow
\Rightarrow
p_i^{\mathrm{BR}}\uparrow.
$$

このように、一方の価格上昇が他方の最適価格も押し上げる関係を strategic complementarity と呼ぶ。

## 8. 品質調整価格 $Z$ で書く

前のノートの

$$
Z_i=p_i-\theta q_i
$$

へ戻る。

$V_i=\beta q_i-\alpha p_i$、$\theta=\beta/\alpha$ とすれば

$$
V_i=-\alpha Z_i.
$$

さらに $\gamma=\alpha/\lambda$ とおくと

$$
s_i
=
\frac{e^{-\gamma Z_i}}
{1+\sum_j e^{-\gamma Z_j}}.
$$

価格条件へ $p_i=Z_i+\theta q_i$ を代入すると、

$$
\boxed{
Z_i
=
c_i-\theta q_i
+
\frac{1}{\gamma(1-s_i)}
}
$$

となる。

つまり

$$
\boxed{
Z_i
=
\underbrace{c_i-\theta q_i}_{\text{費用と品質}}
+
\underbrace{\frac{1}{\gamma(1-s_i)}}_{\text{markup}}
}
$$

である。

## 9. $Z$ のばらつきは不均衡とは限らない

完全競争の直感では $Z_i\to Z^*$ へ近づくように見える。

しかし差別化商品では、均衡そのものに

$$
Z_i\neq Z_j
$$

が残りうる。

費用 $c_i$、品質 $q_i$、市場シェア $s_i$ が企業ごとに違うからである。

したがって、観測される $P(Z)$ の幅は、市場が均衡していないからだけでなく、

$$
\boxed{
\text{差別化された Nash 均衡そのもの}
}
$$

からも生じる。

この点は、後で情報制約による分散を考えるときに重要になる。

## 10. 完全競争極限も残っている

$\gamma$ が大きいと、消費者は $Z$ の差に非常に敏感になる。

そのとき markup 項は

$$
\frac{1}{\gamma(1-s_i)}\to0
$$

へ向かい、

$$
Z_i\to c_i-\theta q_i.
$$

さらに $c_i-\theta q_i$ が企業間で同じなら、

$$
\boxed{Z_i\to Z^*}
$$

が回収される。

前のノートで見た一点平衡は捨てられたのではなく、差別化市場モデルの強競争極限として残っている。

## 11. ここで価格競争を一度閉じる

消費者側では

$$
\mathbf Z\longrightarrow\mathbf s(\mathbf Z),
$$

企業側では

$$
\mathbf s\longrightarrow\mathbf Z
$$

である。

したがって市場全体は

$$
\boxed{
\mathbf Z
\longrightarrow
\mathbf s
\longrightarrow
\mathbf Z
}
$$

という fixed-point problem になる。

形式だけ見れば、統計力学で「場が分布を作り、分布が場を作り返す」mean-field 型の構造に近い。ただし、ここで価格を作り返しているのは物理的相互作用ではなく、企業の利潤最大化と戦略的相互作用である。

ここまでで価格競争については一度閉じる。

次のノートでは品質 $q_i$ も外から与えるのをやめて、企業が $(p_i,q_i)$ を同時に選ぶ場合へ進む。そこでは価格競争から一段進んで、商品設計そのものが競争の対象になる。

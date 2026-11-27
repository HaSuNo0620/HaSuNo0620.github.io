---
title: "複数商品企業の価格設定と所有構造"
summary: "需要のJacobianと所有行列から価格条件を導き、自社内代替が価格・品質選択に作用する仕組みを明示する。"
publishedAt: 2026-09-14T02:15:00+09:00
updatedAt: 2026-11-28
area: "Economics"
field: economics
kind: theory
prerequisites: ["consumer-choice-and-price-formation", "nash-bertrand-price-competition", "price-quality-joint-choice"]
topics: ["multiproduct firm", "ownership matrix", "diversion ratio", "product line", "pricing", "product differentiation"]
status: growing
---

複数の商品を販売する企業にとって、ある商品の値上げによる需要減少は、そのまま企業全体の需要減少にはならない。失われた需要の一部が自社の別商品へ移るためである。ただし移転先の利幅が異なれば、販売数量が保存されても利潤は変わる。

## 所有行列と価格条件

企業 $A$ が所有する商品集合を $\mathcal A$ とし、商品 $i$ の価格、限界費用、需要を $p_i,c_i,Q_i(\mathbf p)$ とする。一定限界費用の下で

$$
\pi_A=\sum_{i\in\mathcal A}(p_i-c_i)Q_i.
$$

商品 $j\in\mathcal A$ の価格に関する内部最適条件は

$$
Q_j+\sum_{i\in\mathcal A}(p_i-c_i)
\frac{\partial Q_i}{\partial p_j}=0.
$$

需要のJacobianを $J_{ij}=\partial Q_i/\partial p_j$、所有行列を同一企業なら $\Omega_{ij}=1$、別企業なら0と定義する。利幅ベクトルを $\mathbf m=\mathbf p-\mathbf c$ とすると、全社の一階条件は

$$
\mathbf Q+(\Omega\odot J)^{\mathsf T}\mathbf m=0.
$$

$\odot$ は要素ごとの積である。逆行列が存在する場合は

$$
\mathbf m=-[(\Omega\odot J)^{\mathsf T}]^{-1}\mathbf Q.
$$

これは均衡で満たすべき条件であり、右辺も価格に依存する。一階条件だけでは大域的な最適性や均衡の存在は保証されない。

## 需要流出率と利幅

$\partial_{p_j}Q_j<0$ として、商品 $j$ の値上げから商品 $i$ への需要流出率を

$$
D_{j\to i}=\frac{\partial_{p_j}Q_i}{-\partial_{p_j}Q_j}
$$

と定める。代替財だけからなる固定市場規模の離散選択模型では、外部選択肢も含めた流出率の和は1である。補完財や市場規模が変わる需要では、この解釈は一般には成立しない。

価格条件は

$$
m_j=-\frac{Q_j}{\partial_{p_j}Q_j}
+\sum_{i\in\mathcal A,\ i\ne j}m_iD_{j\to i}
$$

と分解できる。例えばStandardの値上げで失われる需要の40%がBasic、20%がProへ移るなら、自社内移転の寄与は $0.4m_B+0.2m_P$ となる。回収される顧客数だけでなく移転先の利幅が重要である。

![Standardの値上げによる需要の移転を表した模式図](/figures/economics/ownership-diversion.svg)

*Standardの値上げによる需要の移転を表した模式図。例示した自社内の流出率は40%と20%であり、残り40%は企業外に流出する。競合商品と非購入への配分比は指定していない。*

## 同質ロジット需要での厳密な簡約

外部選択肢付きの同質ロジット需要を考える。$Q_i=Ms_i$、価格感応度を $\gamma>0$ とすると

$$
J_{ij}=-M\gamma s_i(\delta_{ij}-s_j).
$$

所有商品についての一階条件を $Ms_j$ で割ると、

$$
1-\gamma m_j+\gamma\sum_{i\in\mathcal A}s_i m_i=0.
$$

従って同一企業の商品は共通の利幅 $m_A$ を持つ。企業シェアを $S_A=\sum_{i\in\mathcal A}s_i$ とすれば、

$$
m_A=\frac1{\gamma(1-S_A)}.
$$

単一商品企業での利幅の式が、企業全体のシェアによって置き換わる。商品ごとの利幅を変えるには、異質な消費者、異なる価格感応度、供給制約など、この単純な需要の仮定を緩める必要がある。

## 競合参入の再現可能な例

企業AがBasic、Standard、Proを所有するとする。品質調整価格の単位で、各商品の品質調整後の費用を $-2,-1,0$、価格感応度を $\gamma=1$ と設定する。競合Bは品質調整後の費用 $-1$ の商品Xを持つ。外部選択肢の効用は0である。

企業ごとの指数重みの和は

$$
B_A=e^2+e+1,\qquad B_B=e.
$$

企業の共通利幅を $m_A,m_B$ とすれば

$$
S_A=\frac{B_Ae^{-m_A}}
{1+B_Ae^{-m_A}+B_Be^{-m_B}},\quad
S_B=\frac{B_Be^{-m_B}}
{1+B_Ae^{-m_A}+B_Be^{-m_B}}.
$$

参入前は $B_B=0$ とし、$m_A=1/(1-S_A)$ を解く。参入後は $m_A=1/(1-S_A),m_B=1/(1-S_B)$ を連立する。以下の擬似コードで再現できる。

    from scipy.optimize import root
    import numpy as np

    B = np.array([np.exp(2)+np.exp(1)+1, np.exp(1)])
    def residual(m, B):
        v = B*np.exp(-m)
        s = v/(1+v.sum())
        return m-1/(1-s)
    before = root(residual, [2.0], args=(B[:1],))
    after = root(residual, [2.0, 1.5], args=(B,))
    for sol, weights in [(before,B[:1]), (after,B)]:
        assert sol.success
        assert np.max(np.abs(residual(sol.x,weights))) < 1e-8
        print(sol.x)

独立に数値計算を実行すると、参入前の利幅は2.21382743、参入後はAが1.92523099、Bが1.28658331となった。連立条件の残差は最大でも5×10⁻¹⁶未満であった。Aのシェアは0.548294から0.480582へ低下し、Bのシェアは0.222748となる。参入によってAの全商品の価格が共通利幅を通じて連動する。ただし、この例では同質ロジットの制約により、Aの商品間の価格差は変化しない。異質な需要を含む場合には商品ごとの値下げ幅が異なりうる。

この例は旧稿の三タイプ消費者の数値例を再現したものではない。旧計算はパラメータと生成コードを確認できなかったため、条件を明記した別の模型に置き換えた。旧図も再現性が確認できるまで本文には掲載しない。

![競合参入前後の品質調整価格](/figures/multiproduct-competitor-repositioning/entry-reproducible.svg)

*本文の同質ロジット模型による計算。競合参入による共通利幅の低下は、既存企業の3商品の品質調整価格を等しく引き下げる。*

## 品質を選択する企業

品質を変数とし、商品ごとの限界費用 $c_i(q_i)$ を導入すると、企業Aの商品 $j$ の品質条件は

$$
\frac{\partial\pi_A}{\partial q_j}
=\sum_{i\in\mathcal A}(p_i-c_i)\partial_{q_j}Q_i
-Q_jc_j'(q_j)=0.
$$

商品品質の改善によって自社商品から需要を奪った場合でも、利幅差によって利潤は変わる。競合商品からの需要移転に加え、購入しなかった消費者の新規購入も区別する必要がある。

すべての消費者が共通の品質評価 $\theta$ を持ち、需要が品質調整価格のみに依存し、費用が商品ごとに分離できるなら、複数商品企業でも固定 $\mathbf Z$ で品質を独立に最適化できる。この場合の品質条件は[単一商品企業の場合](/notes/price-quality-joint-choice/)と同じ $c_j'(q_j)=\theta$ になる。

一方、異質な品質評価を持つ消費者がいる場合、各商品の品質変更が需要の代替関係自体を変える。競合商品の品質だけから最も強い競争相手を特定することはできず、タイプ別の効用と需要微分が必要になる。

## 参考文献

- K. Train, *Discrete Choice Methods with Simulation*, 2nd ed. (2009).
- J. Tirole, *The Theory of Industrial Organization* (1988).

新規数値例の実行検証は済んでいる。文献照合は別途行う。

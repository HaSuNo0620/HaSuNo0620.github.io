---
title: "1次元一様有限範囲 cosine スピン系 — Z2・Zq・U(1)と有限履歴"
summary: "1次元一様有限範囲 cosine スピン系を、Z2・Zq・U(1)という状態空間の違いだけを動かして比較する。有限相互作用範囲 R が作る R-1 ステップ履歴を共通骨格とし、ドメイン壁履歴、離散位相履歴、連続位相履歴、転送対象、複数相関モードを同じ座標で整理する。"
publishedAt: 2026-09-19T03:15:00+09:00
updatedAt: 2026-09-19
area: "Physics"
topics: ["statistical mechanics", "spin models", "transfer matrix", "finite-range interaction", "finite memory", "correlation"]
status: growing
system:
  dimension: 1
  spatial: uniform
  range: Rn
  interaction: cosine
  symmetry: [Z2, Zq, U(1)]
  mechanics: classical
  role: comparison
---

有限範囲まで相互作用を伸ばしても、三つの模型は同じ Hamiltonian 族に置ける。

$$
\boxed{
H=
-\sum_i\sum_{r=1}^{R}
J_r\cos(\theta_{i+r}-\theta_i)
}
$$

固定するのは

$$
\boxed{
d=1,\qquad
\text{一様},\qquad
R=n,\qquad
\text{cosine},\qquad
\text{古典}
}
$$

で、動かすのは局所状態空間だけである。

$$
\boxed{
Z_2
\longrightarrow
Z_q
\longrightarrow
U(1)
}
$$

この比較で中心になるのは、単一サイトの状態空間ではなく、**有限相互作用範囲が作る履歴空間**である。

---

## 1. 共通骨格は $R-1$ ステップの局所履歴である

局所増分を

$$
\phi_i=\theta_{i+1}-\theta_i
$$

とすると、

$$
\theta_{i+r}-\theta_i =
\sum_{m=0}^{r-1}\phi_{i+m}.
$$

したがって

$$
\boxed{
H=
-\sum_i\sum_{r=1}^{R}
J_r
\cos\left(
\sum_{m=0}^{r-1}\phi_{i+m}
\right)
}
$$

となる。

最大距離 $R$ の局所重みを決めるには、直前の $R-1$ 個の増分を保持すればよい。

つまり三者に共通するのは

$$
\boxed{
R
\longrightarrow
R-1\text{ ステップの空間履歴}
}
$$

である。

違うのは、その履歴の各要素が何を取りうるかである。

---

## 2. 履歴アルファベットが $Z_2\to Z_q\to U(1)$ で細かくなる

三者の局所増分は

$$
\phi_i\in
\begin{cases}
\{0,\pi\}, & Z_2,\\[4pt]
\left\{\dfrac{2\pi a}{q}\right\}, & Z_q,\\[8pt]
S^1, & U(1).
\end{cases}
$$

したがって履歴空間は

$$
\boxed{
\{0,\pi\}^{R-1}
\to
\mathbb Z_q^{\,R-1}
\to
(S^1)^{R-1}
}
$$

と連続化する。

$R=1$ では「一つの局所増分の分解能」だけを見ていた。

有限 $R$ ではそれが

$$
\boxed{
\text{履歴長}
\times
\text{各履歴要素の角度分解能}
}
$$

という二つの構造に分かれる。

---

## 3. $Z_2$ では有限履歴は高次ドメイン壁相互作用になる

$Z_2$ では

$$
\tau_i=s_i s_{i+1}=\pm1
$$

として、

$$
s_i s_{i+r} =
\prod_{m=0}^{r-1}\tau_{i+m}.
$$

したがって

$$
\boxed{
H =
-\sum_i\sum_{r=1}^{R}
J_r
\prod_{m=0}^{r-1}\tau_{i+m}
}
$$

となる。

有限範囲化は

$$
\boxed{
\text{単独の壁}
\to
\text{壁対}
\to
\text{高次壁配置}
}
$$

として現れる。

履歴要素は二値のままで、記憶の深さだけが増える。

---

## 4. $Z_q$ では有限履歴は離散ねじれ列になる

$Z_q$ では

$$
\phi_i=\frac{2\pi a_i}{q},
\qquad
a_i\in\mathbb Z_q.
$$

したがって局所状態は

$$
\boxed{
(a_{i-R+2},\ldots,a_i)
\in
\mathbb Z_q^{\,R-1}
}
$$

になる。

これは

$$
\boxed{
\text{有限履歴}
+
\text{有限角度分解能}
}
$$

を同時に持つ。

一様ねじれのエネルギー

$$
e_R(\phi) =
-\sum_{r=1}^{R}J_r\cos(r\phi)
$$

も、許される離散角

$$
\phi_a=\frac{2\pi a}{q}
$$

の上でしか評価できない。

したがって $Z_q$ は、$Z_2$ の有限履歴と $U(1)$ の連続履歴の間を、**離散履歴空間**として埋める。

---

## 5. $U(1)$ では履歴空間全体が連続になる

$U(1)$ では

$$
\phi_i\in S^1
$$

なので、

$$
\boxed{
\boldsymbol\phi_i =
(\phi_{i-R+2},\ldots,\phi_i)
\in
(S^1)^{R-1}
}
$$

となる。

したがって

$$
Z_2
\to
Z_q
\to
U(1)
$$

は有限範囲では、

$$
\boxed{
2^{R-1}\text{ 個の履歴}
\to
q^{R-1}\text{ 個の履歴}
\to
\text{連続履歴多様体 }(S^1)^{R-1}
}
$$

という形になる。

これは最近接で見た単純な状態数の増加よりも一段強い連続化である。

---

## 6. 転送対象は履歴空間をそのまま反映する

増分履歴を転送状態として使えば、

| 対称性 | 履歴状態 | 転送対象 |
| --- | --- | --- |
| $Z_2$ | $\{0,\pi\}^{R-1}$ | $2^{R-1}\times2^{R-1}$ 行列 |
| $Z_q$ | $\mathbb Z_q^{R-1}$ | $q^{R-1}\times q^{R-1}$ 行列 |
| $U(1)$ | $(S^1)^{R-1}$ | $(S^1)^{R-1}$ 上の積分作用素 |

となる。

したがって

$$
\boxed{
2^{R-1}
\to
q^{R-1}
\to
(S^1)^{R-1}
}
$$

は、局所状態空間の違いが転送空間へそのまま持ち上がったものと読める。

---

## 7. 一様ねじれのエネルギーは三者で共通である

連続変数として書けば、

$$
\boxed{
e_R(q) =
-\sum_{r=1}^{R}
J_r\cos(rq)
}
$$

は三者に共通する。

違うのは許される $q$ である。

$Z_2$ では実質

$$
q=0,\pi
$$

しかない。

$Z_q$ では

$$
q=\frac{2\pi a}{q}
$$

という離散格子上で極小を選ぶ。

$U(1)$ では

$$
q\in S^1
$$

を連続的に探索できる。

したがって

$$
\boxed{
\text{二値配置}
\to
\text{離散ねじれロッキング}
\to
\text{連続ねじれ選択}
}
$$

となる。

---

## 8. 有限範囲では複数の構造波数候補を持てる

$R=2$ では一組の非零ねじれが主要な構造だった。

一般の有限 $R$ では

$$
e_R(q) =
-\sum_{r=1}^{R}J_r\cos(rq)
$$

が複数の局所極小を持ちうる。

したがって、

$$
\boxed{
\pm q_1,\qquad
\pm q_2,\qquad
\ldots
}
$$

という複数の候補が現れうる。

三者の違いは、その候補をどの解像度で表現できるかである。

- $Z_2$：極端に粗い二値表現
- $Z_q$：有限個の離散波数へロック
- $U(1)$：連続波数として保持

となる。

---

## 9. 長距離記憶は三者とも複数モードへ一般化される

転送対象の副次固有値を

$$
\Lambda_a =
|\Lambda_a|e^{iq_a}
$$

とすれば、

$$
\xi_a^{-1} =
-\ln\left|
\frac{\Lambda_a}{\Lambda_0}
\right|
$$

である。

したがって長距離相関は一般に

$$
\boxed{
C(r)
\sim
\sum_a
A_a
e^{-r/\xi_a}
\cos(q_a r+\varphi_a)
}
$$

となる。

$Z_2$、$Z_q$、$U(1)$ の違いは、このモード構造を作る履歴空間の分解能にある。

共通して

$$
\boxed{
\text{局所履歴}
\to
\text{転送スペクトル}
\to
(\xi_a,q_a)
}
$$

という流れで読める。

---

## 10. $R$ 軸と対称性軸は有限履歴空間の二方向になる

ここまで来ると、二つの軸の違いが明確になる。

$R$ を変えると、

$$
\boxed{
\text{履歴の長さ}
}
$$

が変わる。

一方、

$$
Z_2\to Z_q\to U(1)
$$

では、

$$
\boxed{
\text{履歴1要素あたりの状態分解能}
}
$$

が変わる。

したがって有限範囲平面は

$$
\boxed{
\text{履歴深さ }(R-1)
\times
\text{履歴アルファベット }(Z_2,Z_q,U(1))
}
$$

として読める。

---

## 得られた見方

有限範囲 cosine 系では、

$$
\boxed{
Z_2
\to
Z_q
\to
U(1)
}
$$

は単なる局所状態空間の連続化ではない。

有限相互作用範囲によって生じた履歴空間全体が

$$
\boxed{
\{0,\pi\}^{R-1}
\to
\mathbb Z_q^{\,R-1}
\to
(S^1)^{R-1}
}
$$

と連続化する。

一方で $R$ を伸ばす操作は、この履歴空間の次元を増やす。

したがって

$$
\boxed{
R =
\text{履歴の深さ},
\qquad
Z_2\to Z_q\to U(1) =
\text{履歴の分解能}
}
$$

という二軸で、有限範囲 cosine スピン系の平面全体を整理できる。

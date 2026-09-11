---
title: "準結晶は何が「結晶」なのか — 周期性を捨てても秩序は残る"
summary: "結晶を周期性だけで定義すると準結晶は矛盾して見える。並進対称性、長距離秩序、Bragg回折を切り分け、周期結晶から準結晶へ何が保存され何が失われるのかを整理する。"
publishedAt: 2026-09-12T02:45:00+09:00
area: "Physics"
topics: ["quasicrystals", "aperiodic order", "diffraction", "crystallography", "long-range order"]
status: growing
---

準結晶を最初に学ぶと、「周期的ではないのになぜ結晶と呼べるのか」というところで一度立ち止まる。これは単なる言葉の問題ではない。**結晶性の本質を、実空間の並進周期性に置くのか、それとも長距離にわたる位相コヒーレンスと回折構造に置くのか**という問題である。

通常の周期結晶では、この二つは同時に成立する。そのため両者を区別する必要がなかった。準結晶はその同一視を壊す。

このノートでは、周期結晶から準結晶へ移るときに、何が失われ、何が残るのかを整理する。

## 1. 周期結晶では三つの性質が重なっている

$d$ 次元の周期結晶の密度を $\rho(\mathbf r)$ とする。独立な格子ベクトル $\mathbf a_1,\ldots,\mathbf a_d$ が存在して

$$
\rho(\mathbf r+\mathbf R)=\rho(\mathbf r),
\qquad
\mathbf R=\sum_{i=1}^{d}n_i\mathbf a_i,
\quad n_i\in\mathbb Z
$$

が成り立つなら、実空間には並進周期性がある。

この周期性から reciprocal lattice が生じ、

$$
\mathbf G=\sum_{i=1}^{d}m_i\mathbf b_i,
\qquad
\mathbf a_i\cdot\mathbf b_j=2\pi\delta_{ij}
$$

で表される波数に Bragg peak が現れる。

したがって周期結晶では、

1. 実空間の並進周期性、
2. 無限遠まで保たれる秩序、
3. 逆空間の鋭い Bragg peak、

が一つの構造の別の表現になっている。

ここで重要なのは、この三つが論理的には同じ概念ではないことである。

## 2. 準結晶が捨てるのは「秩序」ではなく「周期」である

準結晶では、非零の並進ベクトル $\mathbf R$ に対して一般に

$$
\rho(\mathbf r+\mathbf R)=\rho(\mathbf r)
$$

とはならない。したがって通常の意味での単位胞を取れない。

しかし配置はランダムではない。遠く離れた場所の構造にも決定論的な関係があり、Fourier 空間では鋭い Bragg peak が現れる。

このため、

$$
\boxed{
\text{aperiodic}\neq\text{disordered}
}
$$

である。

準結晶を理解するときに最も重要なのは、**周期性と秩序を切り離すこと**だと思う。

ランダム系では、位置を遠くへずらすほど局所構造の位相関係が失われる。一方、理想的な準結晶では並進周期は存在しないにもかかわらず、構造全体を決める規則が無限遠まで続いている。

## 3. 「長距離秩序」は何を意味するのか

密度の Fourier 変換を

$$
\widetilde\rho(\mathbf k)
=\int d^dr\,\rho(\mathbf r)e^{-i\mathbf k\cdot\mathbf r}
$$

とする。

ランダムな配置では一般に散漫な diffraction が現れる。一方、周期結晶では reciprocal lattice 上にデルタ関数的な Bragg 成分が現れる。

準結晶でも理想化された極限では diffraction measure に pure-point 成分があり、鋭い Bragg peak が存在する。したがって、結晶性を「周期単位胞を持つこと」ではなく「長距離秩序に由来する Bragg diffraction を持つこと」と見ると、周期結晶と準結晶を同じ枠に置ける。

ただし、Bragg peak があることだけで任意の構造を準結晶と呼ぶわけではない。準結晶ではさらに、通常の $d$ 次元 reciprocal lattice では生成できない Fourier module が現れる。この点は[回折のノート](/notes/quasicrystal-diffraction-fourier-module/)で整理する。

## 4. なぜ5回・10回対称性が問題になったのか

周期結晶では、格子を回転して自分自身へ重ねるという条件から crystallographic restriction が生じる。

2次元格子で回転角を $\theta$ とすると、格子基底に対する回転は整数行列で表される必要がある。回転行列の trace は $2\cos\theta$ であり、整数行列の trace でもあるため

$$
2\cos\theta\in\mathbb Z
$$

でなければならない。

したがって許される回転対称性は

$$
n=1,2,3,4,6
$$

に限られる。

5回対称性が禁止されるのは、「物質が5角形を好まない」からではない。**周期格子と有限回転対称性を同時に要求した結果**である。

準結晶では前提である並進周期格子を捨てるので、この制限定理の外へ出ることができる。5回、8回、10回、12回などの対称性と鋭い diffraction pattern を両立できる。

つまり5回対称性は準結晶の本質そのものというより、周期結晶の枠組みが破れていることを非常に分かりやすく示す徴候である。

## 5. 単位胞がないなら、何が構造を指定するのか

周期結晶では有限な単位胞と格子ベクトルを与えれば、無限構造を生成できる。

準結晶でも「有限情報から無限構造を生成する」という性質は失われない。ただし生成規則が違う。

代表的には、

- substitution rule、
- cut-and-project、
- inflation / deflation、
- higher-dimensional periodic description、

などによって無限構造を記述する。

例えば Fibonacci chain は

$$
L\mapsto LS,
\qquad
S\mapsto L
$$

という有限な置換則から生成できる。並進周期はないが、配置は完全に決定論的である。

ここで周期結晶との違いを、「有限情報で記述できるかどうか」だと考えると誤る。違いは、**有限情報が単位胞として繰り返されるか、非周期的な生成則として展開されるか**にある。

## 6. 局所構造だけを見ても準結晶性は分からない

準結晶にはしばしば特徴的な局所配位がある。しかし局所的な5回対称クラスターを持つことと、準結晶であることは同じではない。

有限サイズのクラスターなら5回対称性はいくらでも作れる。icosahedral cluster もそれ自体は crystallographic restriction に反しない。制限定理が拘束するのは、その局所構造を**並進格子として空間全体へ周期的に延長すること**である。

したがって準結晶性は本質的に非局所的な概念である。局所配位ではなく、その配位が空間全体でどのような位相関係を保つかを見る必要がある。

## 7. 周期結晶から準結晶へ何が変わるか

周期結晶と準結晶の差を表にすると見通しがよい。

| | 周期結晶 | 準結晶 |
| --- | --- | --- |
| 並進周期 | ある | ない |
| 有限単位胞 | ある | 一般にない |
| 長距離秩序 | ある | ある |
| Bragg peak | ある | ある |
| Fourier 基底の rank | 通常 $D=d$ | $D>d$ が可能 |
| 禁制回転対称性 | 不可 | 可能 |
| 代表的記述 | 格子 + basis | substitution / cut-and-project / higher-dimensional lattice |

この表で重要なのは、準結晶が「結晶と無秩序の中間」ではないことである。

むしろ

$$
\boxed{
\text{periodic order}
\subset
\text{long-range ordered structures}
}
$$

と考えた方がよい。準結晶は、長距離秩序のうち周期格子で表現できない領域にある。

## 8. 自分のための見取り図

準結晶を理解するうえで、今のところ次の分解が最も重要である。

$$
\boxed{
\begin{aligned}
\text{periodicity}
&=\text{exact translational repetition},\\
\text{order}
&=\text{long-range phase coherence},\\
\text{crystallinity}
&\approx\text{sharp diffraction from long-range order}.
\end{aligned}
}
$$

周期結晶では三者がほぼ重なっている。準結晶はこの重なりを解き、**並進周期性がなくても長距離秩序と鋭い回折は残せる**ことを示した。

次に必要なのは、「では非周期なのにどうやって無限遠まで規則性を保つのか」という問いである。その数学的な最小模型が準周期関数であり、[次のノート](/notes/quasiperiodic-functions-torus/)では高次元トーラス上の周期運動として準周期性を見る。

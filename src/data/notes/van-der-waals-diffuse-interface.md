---
title: "van der Waalsのdiffuse interface — 界面を密度場として解く"
summary: "Gibbsが界面をsurface excessへ縮約したのに対し、van der Waalsは密度を空間場として扱い、有限幅界面と表面張力を界面構造から導く道を開いた。square-gradient近似が何を残し、何を捨てるのかまで整理する。"
publishedAt: 2026-09-09T22:30:00+09:00
updatedAt: 2026-09-14
area: "Physics"
topics: ["interfacial physics", "diffuse interface", "van der Waals", "square-gradient theory", "capillarity"]
status: growing
---

[前のNote](/notes/gibbs-to-tolman-gauge-curvature/)では、Gibbsが有限幅をもつ実在界面を直接解く代わりに、厚さゼロのdividing surfaceとsurface excessを用いて界面熱力学を構成した。

van der Waalsの1893年の毛管理論は、その粗視化を逆向きにたどる。**密度が界面を横切って連続的に変化する**と考え、界面を空間的なtransition layerとして扱う。

Gibbsのsurface thermodynamicsと競合するというより、Gibbsが積分量へ縮約した界面内部を、密度場としてもう一度展開する位置づけに近い。

## sharp interface から密度プロファイルへ

Young–LaplaceやGibbsでは、界面は巨視的には厚さゼロの面として扱える。

sharp-interface描像なら、液体と気体の密度は概念的には

$$
\rho(z)=
\begin{cases}
\rho_l,&z<0,\\
\rho_v,&z>0
\end{cases}
$$

のように不連続に切り替わる。

van der Waalsでは

$$
\rho_l\longrightarrow\rho(z)\longrightarrow\rho_v
$$

という連続的なtransition layerが現れる。

界面は幾何学的な境界ではなく、**局所密度そのものが空間的に変化する領域**になる。理論の主役も、界面位置から密度プロファイルへ移る。

## bulk自由エネルギーだけでは有限幅を選べない

一様流体のHelmholtz自由エネルギー密度を $f_0(\rho)$ とする。

非一様系に対して

$$
F[\rho]=\int d\mathbf r\,f_0(\rho(\mathbf r))
$$

とだけ書くと、各点の自由エネルギーはその場所の密度だけで決まる。

二相共存では、液体密度 $\rho_l$ と気体密度 $\rho_v$ はbulkの熱力学的に許された二つの状態である。しかし局所項だけでは、これらを空間的にどれだけ急激に切り替えるかに対する十分なコストがない。

現実の界面には有限の自由エネルギーと有限の厚さがある。したがって自由エネルギーは密度の値だけでなく、**密度が空間的にどのように変化するか**も持つ必要がある。

## square-gradient form は現代語での最小表現

van der Waalsの考えを現代の汎関数記法へ翻訳すると、基本形は

$$
F[\rho]=\int d\mathbf r\left[f_0(\rho)+\frac{\kappa}{2}|\nabla\rho|^2\right]
$$

と書ける。

$\kappa$ は密度の空間変化に対するコストを決める係数である。

これは1893年の原論文をそのまま転記した式ではない。原論文では界面内の局所自由エネルギーへの補正が密度の二階微分を含む形で現れ、後世のsquare-gradient theoryでは部分積分と境界条件を使って $|\nabla\rho|^2$ 型へ整理する。

したがって、ここで使うsquare-gradient formは**van der Waalsの考えを現代語に翻訳したもの**として扱う。

## gradient の二乗は対称性と長波長展開の両方から出る

平面界面で $\rho=\rho(z)$ とする。

界面の向きを反転しても界面自由エネルギーは変わらないため、$d\rho/dz$ に一次の項は使いにくい。最低次のスカラー補正は

$$
\left(\frac{d\rho}{dz}\right)^2
$$

になる。

ただし、この項は対称性だけの便宜的な選択ではない。**非局所分子間相互作用の長波長展開**としても現れる。

## 非局所相互作用の低波数部分だけを残す

mean-field的な引力エネルギーなら、概略

$$
F_{\mathrm{nl}}=\frac12\int d\mathbf r\,d\mathbf r'\,\rho(\mathbf r)w(|\mathbf r-\mathbf r'|)\rho(\mathbf r')
$$

と書ける。

$\mathbf s=\mathbf r'-\mathbf r$ とし、密度が相互作用距離に比べてゆっくり変化すると

$$
\rho(\mathbf r+\mathbf s)
=
\rho(\mathbf r)
+s_i\partial_i\rho
+\frac12s_is_j\partial_i\partial_j\rho
+\cdots
$$

と展開できる。

相互作用が等方的なら一次項は角度積分で消え、二次項から $\rho\nabla^2\rho$ 型の寄与が出る。部分積分すると、境界項を除いて

$$
\int d\mathbf r\,\rho\nabla^2\rho
=-\int d\mathbf r\,|\nabla\rho|^2
$$

となる。

square-gradient termは、**非局所相互作用を長波長で局所化した最低次の項**と読める。

相互作用長を $\ell$、密度変化の代表波数を $k$ とすれば、背後の小さいパラメータは $k\ell\ll1$ である。

## 平衡密度プロファイルは変分で決まる

一定温度・一定化学ポテンシャルでgrand potentialを

$$
\Omega[\rho]
=
\int d\mathbf r\left[f_0(\rho)-\mu\rho+\frac{\kappa}{2}|\nabla\rho|^2\right]
$$

とする。

平衡状態では $\delta\Omega/\delta\rho=0$ なので

$$
\frac{df_0}{d\rho}-\mu-\kappa\nabla^2\rho=0
$$

となる。

ここで $\rho(\mathbf r)$ は説明用の模式図ではなく、**変分原理から決定される未知関数**になっている。

Gibbsでは界面内部を解かずにsurface excessへ縮約した。van der Waalsでは、その内部構造自体を解く。

## first integral は界面を二つのコストの競合として書く

平面界面では $\rho=\rho(z)$ とし、grand-potential densityを $\omega(\rho)=f_0(\rho)-\mu\rho$ と定義する。

平衡方程式は

$$
\kappa\frac{d^2\rho}{dz^2}=\frac{d\omega}{d\rho}
$$

となる。

両辺に $d\rho/dz$ を掛けて積分すると、bulk共存状態での値を $\omega_{\mathrm{coex}}$ として

$$
\frac{\kappa}{2}\left(\frac{d\rho}{dz}\right)^2
=
\omega(\rho)-\omega_{\mathrm{coex}}
$$

を得る。

左辺は密度を急激に変化させるgradient cost、右辺はbulkとしては不利な中間密度を取るthermodynamic costである。

界面は、**二相へ分かれたがるbulk thermodynamicsと、密度を無限に急変させない非局所相互作用の競合**として現れる。界面中の中間密度が、新しいbulk安定相になっているわけではない。

## 界面幅が理論内部の長さになる

後世のLandau型の対称double-wellを例に取ると、order parameterを $\phi$ として

$$
F[\phi]=\int dz\left[-\frac{a}{2}\phi^2+\frac{b}{4}\phi^4+\frac{\kappa}{2}\left(\frac{d\phi}{dz}\right)^2\right]
$$

と書ける。

このとき平衡界面はtanh型になり、代表的な界面幅は

$$
\xi\sim\sqrt{\frac{\kappa}{a}}
$$

で決まる。

この具体形はvan der Waals原論文そのものではなく、後のLandau–Ginzburg/Cahn–Hilliard的な単純化である。ただ、**有限幅がbulk thermodynamicsとgradient costの比から生まれる**ことは明瞭に見える。

Young–Laplaceでは外から見えなかった界面厚さが、ここでは理論内部の長さになる。

## 表面張力が入力値から出力量へ変わる

平面界面のexcess grand potential per unit areaとして

$$
\gamma
=
\int_{-\infty}^{\infty}dz\left[
\omega(\rho)-\omega_{\mathrm{coex}}
+\frac{\kappa}{2}\left(\frac{d\rho}{dz}\right)^2
\right]
$$

と書ける。

平衡時にはfirst integralから

$$
\gamma
=
\int_{-\infty}^{\infty}dz\,\kappa\left(\frac{d\rho}{dz}\right)^2
$$

となる。

さらに積分変数を $z$ から $\rho$ へ変えると

$$
\gamma
=
\int_{\rho_v}^{\rho_l}d\rho\,
\sqrt{2\kappa\left[\omega(\rho)-\omega_{\mathrm{coex}}\right]}
$$

と書ける。

ここで界面理論の役割が変わる。

Young–Laplaceでは $\gamma$ を与えて力学を閉じた。Gibbsでは $\gamma$ を界面熱力学の状態量として扱った。van der Waals型diffuse-interface theoryでは

$$
f_0(\rho),\ \kappa
\quad\longrightarrow\quad
\rho(z)
\quad\longrightarrow\quad
\gamma
$$

という順序で、表面張力を界面構造から計算できる。

## Gibbs と van der Waals は解像度が違う

Gibbsでは、有限幅の実在界面を任意のdividing surfaceとsurface excessへ写像した。

van der Waalsでは、その有限幅界面を密度場として解く。

両者は競合する理論というより、異なる解像度の記述である。

van der Waals型理論から $\rho(z)$ を得たあとでdividing surfaceを選べば、Gibbsのsurface excessを計算できる。

$$
\text{diffuse profile}
\quad\xrightarrow{\text{coarse grain}}\quad
\text{Gibbs surface excess}
$$

という関係になる。

## square-gradient が捨てるもの

van der Waals型のsquare-gradient theoryは、sharp interfaceよりははるかに多くの構造を残す。ただし、分子間相互作用の非局所性をそのまま保持した理論ではない。

出発点では非局所kernel $w(|\mathbf r-\mathbf r'|)$ が二点間の結合をすべて持っていた。それを長波長展開して最低次で切ることで、非局所kernel全体を局所的な係数 $\kappa$ へ圧縮している。

Fourier空間で、密度揺らぎに対する二次の自由エネルギーを

$$
\Delta F^{(2)}
=
\frac12\int\frac{d\mathbf k}{(2\pi)^d}\,A(k)|\delta\rho_{\mathbf k}|^2
$$

と書くと、square-gradient approximationは $A(k)$ の $k=0$ 近傍だけを

$$
A(k)=A_0+A_2k^2+O(k^4)
$$

と残していることに対応する。

実空間の $A_2k^2$ が $|\nabla\rho|^2$ に対応する。保持しているのは、**十分長い波長に対するbulk responseの最初の曲率**であり、それ以外の $k$ 依存は捨てている。

### kernel の詳細な非局所形状

元の非局所理論では、ある点の密度は周囲の有限距離にわたる密度分布と結合している。

square-gradient theoryでは、この情報を $A_0$ と $A_2$、あるいは $f_0(\rho)$ と $\kappa$ のような少数の量へ縮約する。

相互作用距離と同程度のスケールで密度が変化すると、$k\ell\ll1$ という前提そのものが崩れる。

### 分子直径スケールの packing

高密度液体では、排除体積によってpair correlationが分子スケールで振動する。

このpackingは $k=0$ 近傍の情報ではなく、分子間距離に対応する**有限波数**の構造として現れる。

最低次square-gradient theoryでは、このpreferred wavelengthを持てない。

### oscillatory layering

壁や強い界面の近傍では

$$
\rho(z)-\rho_b
\sim
 e^{-\alpha z}\cos(qz+\phi)
$$

のような減衰振動が現れることがある。

一方、square-gradientの線形化から得られる基本的なbulk tailは

$$
\delta\rho(z)\sim e^{-z/\xi}
$$

のような単調減衰である。

$A(k)$ を $A_0+A_2k^2$ までしか残さなければ、有限の実波数を選ぶ構造が消えるためである。

### bulk correlation の有限波数構造

一様液体のstructure factor $S(k)$ は、一般には $k=0$ だけで特徴づけられない。高密度液体では分子間距離に対応する有限 $k$ に第一ピークが現れる。

square-gradient theoryは、そのような有限波数の応答を区別せず、長波長極限へ押し込める。

壁がbulk液体自身のpreferred wavelengthを励起してlayeringを作る、といった現象は最低次の理論からは見えない。

## 残したものと捨てたもの

概念的には

$$
\text{full nonlocal interaction}
\quad\longrightarrow\quad
\text{long-wavelength moments}
\quad\longrightarrow\quad
f_0(\rho),\ \kappa
$$

である。

この操作で残るのは、相分離を生むbulk thermodynamics、滑らかな密度変化、有限の界面幅、そしてそのプロファイルから得られる表面張力である。

一方で捨てられるのは、kernelの細かな形、packing、有限波数のbulk correlation、分子スケールのlayeringである。

したがってvan der Waalsの理論は「界面内部を解く理論」であると同時に、**界面内部のうち長波長成分だけを残した理論**でもある。

残る問いは、$k=0$ 周りだけを見るのをやめ、液体がもつ有限波数の構造を残したとき、界面や壁近傍の密度場がどう変わるかである。

## 歴史の中での位置

Young–Laplaceは界面内部を捨てて $\gamma$ を与え、Gibbsは界面内部を解かずsurface excessとして熱力学へ組み込み、van der Waalsは有限幅の密度場を解いて界面構造から $\gamma$ を導く道を開いた。

後にCahn–Hilliardは、このsquare-gradient型の自由エネルギーを一般の組成場に対する汎関数として整理し、保存則と組み合わせて相分離動力学へ発展させる。静的な界面論の骨格だけを見れば、van der Waalsから続く同じsquare-gradient familyにある。

一方、液体固有のpackingやfinite-$k$ structureを保持する方向は、square-gradientをさらに一般化するというより、そこで捨てた**非局所なbulk correlation**へ戻る方向である。

## References

- J. D. van der Waals, *Thermodynamische theorie der cappillariteit in de onderstelling van continue dichtheidsverandering* (1893).
- J. S. Rowlinson, “Translation of J. D. van der Waals' ‘The thermodynamic theory of capillarity under the hypothesis of a continuous variation of density’,” *Journal of Statistical Physics* **20**, 197–244 (1979), DOI: 10.1007/BF01011514.
- J. S. Rowlinson and B. Widom, *Molecular Theory of Capillarity*, Clarendon Press (1982).

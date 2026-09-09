---
title: "van der Waalsのdiffuse interface — 界面を密度場として解く"
summary: "Gibbsが界面をsurface excessへ縮約したのに対し、van der Waalsは密度を空間場として扱い、有限幅界面と表面張力を界面構造から導く道を開いた。square-gradient近似が何を残し、何を捨てるのかまで整理する。"
publishedAt: 2026-09-09T22:30:00+09:00
updatedAt: 2026-09-09
area: "Physics"
topics: ["interfacial physics", "diffuse interface", "van der Waals", "square-gradient theory", "capillarity"]
status: growing
---

[前のNote](/notes/gibbs-to-tolman-gauge-curvature/)では、Gibbsが有限幅をもつ実在界面を直接解く代わりに、厚さゼロのdividing surfaceとsurface excessを用いて界面熱力学を構成したことを見た。

van der Waalsはそこから別の方向へ進んだ。1893年の毛管理論では、**密度が界面を横切って連続的に変化する**ことを仮定し、界面そのものを空間的なtransition layerとして扱った。

ここでの主題は、Gibbsのsurface thermodynamicsを否定することではない。むしろ、Gibbsが積分量へ縮約した界面内部を、もう一度密度場として展開してみることにある。

## sharp interfaceからdiffuse interfaceへ

Young–LaplaceやGibbsでは、界面は巨視的には厚さゼロの面として扱える。

sharp-interface描像なら、液体と気体の密度は概念的には

$$\rho(z)=\begin{cases}\rho_l,&z<0,\\ \rho_v,&z>0\end{cases}$$

のように不連続に切り替わる。

van der Waalsが導入したのは、これに代わる

$$\rho_l\longrightarrow\rho(z)\longrightarrow\rho_v$$

という連続的なtransition layerである。

つまり界面は、単なる幾何学的な境界ではなく、**局所密度そのものが空間的に変化する領域**になる。

この時点で、界面の位置よりも界面のプロファイルが理論の主役になる。

## bulk自由エネルギーだけでは界面を作れない

一様流体のHelmholtz自由エネルギー密度を $f_0(\rho)$ とする。

非一様系に対して最も素朴に

$$F[\rho]=\int d\mathbf r\,f_0(\rho(\mathbf r))$$

と書くと、各点の自由エネルギーはその場所の密度だけで決まる。

しかし二相共存では、液体密度 $\rho_l$ と気体密度 $\rho_v$ はbulkの熱力学的に許された二つの状態である。局所項だけでは、これらを空間的にどれだけ急激に切り替えるかに対する十分なコストがない。

現実の界面には有限の自由エネルギーと有限の厚さがある。したがって自由エネルギーは、密度の値だけでなく、**密度が空間的にどのように変化するか**も知らなければならない。

## 現代的なsquare-gradient表現

van der Waalsの理論を現代の汎関数記法へ翻訳すると、最も基本的な形は

$$F[\rho]=\int d\mathbf r\left[f_0(\rho)+\frac{\kappa}{2}|\nabla\rho|^2\right]$$

と書ける。

ここで $\kappa$ は密度の空間変化に対するコストを決める係数である。

ただし、これは1893年の原論文をそのまま転記した式ではない。van der Waalsの原論文では、界面内の局所自由エネルギーへの補正が密度の二階微分を含む形で現れる。後世のsquare-gradient theoryでは、それを部分積分と境界条件のもとで整理し、$|\nabla\rho|^2$ 型の汎関数として書くのが標準的である。

したがって、ここでのsquare-gradient formは**van der Waalsの考えを現代語に翻訳したもの**として読むべきである。

## なぜgradientの二乗なのか

平面界面で $\rho=\rho(z)$ とする。

界面の向きを反転しても、界面を作る自由エネルギーそのものは変わるべきではない。したがって $d\rho/dz$ に一次の項は向きの反転で符号が変わってしまう。

最低次のスカラー補正は

$$\left(\frac{d\rho}{dz}\right)^2$$

である。

これは対称性から見た理由である。

しかし、より物理的にはこの項は**非局所分子間相互作用の長波長展開**として理解できる。

## 非局所相互作用からgradient expansionへ

分子間相互作用は本来非局所的である。mean-field的な引力エネルギーなら、概略

$$F_{\mathrm{nl}}=\frac12\int d\mathbf r\,d\mathbf r'\,\rho(\mathbf r)w(|\mathbf r-\mathbf r'|)\rho(\mathbf r')$$

と書ける。

ここで $\mathbf s=\mathbf r'-\mathbf r$ とし、密度が相互作用距離に比べてゆっくり変化すると仮定する。

すると

$$\rho(\mathbf r+\mathbf s)=\rho(\mathbf r)+s_i\partial_i\rho+\frac12s_is_j\partial_i\partial_j\rho+\cdots$$

と展開できる。

相互作用が等方的なら一次項は角度積分で消え、二次項から $\rho\nabla^2\rho$ 型の寄与が現れる。これを部分積分すると、境界項を除いて

$$\int d\mathbf r\,\rho\nabla^2\rho=-\int d\mathbf r\,|\nabla\rho|^2$$

となる。

したがってsquare-gradient termは、単なる経験的な補正ではなく、**非局所相互作用を長波長で局所化した最低次の項**と理解できる。

ここで小さいパラメータになっているのは、相互作用長を $\ell$、密度変化の代表波数を $k$ とすれば $k\ell\ll1$ である。

## 平衡密度プロファイルは変分問題になる

一定温度・一定化学ポテンシャルでgrand potentialを

$$\Omega[\rho]=\int d\mathbf r\left[f_0(\rho)-\mu\rho+\frac{\kappa}{2}|\nabla\rho|^2\right]$$

とする。

平衡状態では $\delta\Omega/\delta\rho=0$ なので、Euler–Lagrange equationは

$$\frac{df_0}{d\rho}-\mu-\kappa\nabla^2\rho=0$$

となる。

ここで重要なのは、$\rho(\mathbf r)$ が単なる説明用の図ではなく、**変分原理から決定される未知関数**になったことである。

Gibbsでは界面内部を解かずにsurface excessへ縮約した。van der Waalsではその内部構造そのものを解く。

## 平面界面のfirst integral

平面界面では $\rho=\rho(z)$ とし、grand-potential densityを $\omega(\rho)=f_0(\rho)-\mu\rho$ と定義する。

平衡方程式は

$$\kappa\frac{d^2\rho}{dz^2}=\frac{d\omega}{d\rho}$$

となる。

両辺に $d\rho/dz$ を掛けて積分すると、bulk共存状態での値を $\omega_{\mathrm{coex}}$ として

$$\frac{\kappa}{2}\left(\frac{d\rho}{dz}\right)^2=\omega(\rho)-\omega_{\mathrm{coex}}$$

を得る。

この式は界面が何で決まるかを非常によく表している。

左辺は密度を急激に変化させるgradient cost、右辺はbulkとしては不利な中間密度を取るthermodynamic costである。

つまり界面は、

> bulk自由エネルギーは二つの相へ分かれたがるが、非局所相互作用は密度を無限に急変させることを許さない。

という競合から生まれる。

界面中の中間密度が、bulkとして新しい安定相になっているわけではない。

## 界面幅が理論内部の長さになる

後世のLandau型の対称double-wellを例に取ると、order parameterを $\phi$ として

$$F[\phi]=\int dz\left[-\frac{a}{2}\phi^2+\frac{b}{4}\phi^4+\frac{\kappa}{2}\left(\frac{d\phi}{dz}\right)^2\right]$$

と書ける。

このとき平衡界面はtanh型になり、代表的な界面幅は

$$\xi\sim\sqrt{\frac{\kappa}{a}}$$

で決まる。

この具体形はvan der Waals原論文そのものではなく、後のLandau–Ginzburg/Cahn–Hilliard的な単純化である。しかし、**有限幅がbulk thermodynamicsとgradient costの比から生まれる**という構造を最も見やすく示している。

Young–Laplaceでは外から見えなかった界面厚さが、ここでは理論の内部変数になる。

## 表面張力が界面構造から導かれる

さらに重要なのは、表面張力 $\gamma$ が単なる入力値ではなくなることである。

平面界面のexcess grand potential per unit areaとして

$$\gamma=\int_{-\infty}^{\infty}dz\left[\omega(\rho)-\omega_{\mathrm{coex}}+\frac{\kappa}{2}\left(\frac{d\rho}{dz}\right)^2\right]$$

と書ける。

平衡時にはfirst integralを使えるので、

$$\gamma=\int_{-\infty}^{\infty}dz\,\kappa\left(\frac{d\rho}{dz}\right)^2$$

となる。

さらに積分変数を $z$ から $\rho$ へ変えると、

$$\gamma=\int_{\rho_v}^{\rho_l}d\rho\,\sqrt{2\kappa\left[\omega(\rho)-\omega_{\mathrm{coex}}\right]}$$

と書ける。

ここで、界面理論の役割が大きく変わる。

Young–Laplaceでは $\gamma$ を与えて力学を閉じた。Gibbsでは $\gamma$ を界面熱力学の状態量として扱った。van der Waals型diffuse-interface theoryでは、

$$f_0(\rho),\ \kappa\quad\longrightarrow\quad\rho(z)\quad\longrightarrow\quad\gamma$$

という順序で、表面張力を界面構造から計算する道が開かれる。

## Gibbsとvan der Waalsは対立しない

Gibbsでは、有限幅の実在界面を任意のdividing surfaceとsurface excessへ写像した。

van der Waalsでは、その有限幅界面を密度場として解く。

したがって両者は競合する理論というより、異なる解像度の記述と考える方が自然である。

van der Waals型理論から $\rho(z)$ を得たあとでdividing surfaceを選べば、Gibbsのsurface excessを計算できる。

つまり概念的には、

$$\text{diffuse profile}\quad\xrightarrow{\text{coarse grain}}\quad\text{Gibbs surface excess}$$

という関係がある。

## square-gradientは何を捨てたのか

van der Waals型のsquare-gradient theoryは、sharp interfaceよりははるかに多くの構造を残した。しかし、分子間相互作用の非局所性をそのまま保持した理論ではない。

出発点では、非局所kernel $w(|\mathbf r-\mathbf r'|)$ が二点間の結合をすべて持っていた。それを長波長展開して最低次で切ることで、非局所kernel全体を局所的な係数 $\kappa$ へ圧縮している。

Fourier空間で見ると、この操作はさらに明瞭になる。密度揺らぎに対する二次の自由エネルギーを概念的に

$$\Delta F^{(2)}=\frac12\int\frac{d\mathbf k}{(2\pi)^d}\,A(k)|\delta\rho_{\mathbf k}|^2$$

と書くと、square-gradient approximationは $A(k)$ の $k=0$ 近傍だけを

$$A(k)=A_0+A_2k^2+O(k^4)$$

と展開していることに対応する。

実空間の $A_2k^2$ が $|\nabla\rho|^2$ に対応する。したがってsquare-gradient theoryが保持しているのは、**十分長い波長に対するbulk responseの最初の曲率**である。

逆に言えば、それ以外の $k$ 依存は捨てている。

### 捨てたもの1：kernelの詳細な非局所形状

元の非局所理論では、ある点の密度は周囲の有限距離にわたる密度分布と結合している。

square-gradient theoryでは、この情報を $A_0$ と $A_2$、あるいは $f_0(\rho)$ と $\kappa$ のような少数の量へ縮約する。

したがって、相互作用距離と同程度のスケールで密度が変化すると、$k\ell\ll1$ という前提そのものが崩れる。

### 捨てたもの2：分子直径スケールのpacking

高密度液体では、粒子は排除体積のために無関係には配置できない。ある粒子の周囲では隣接粒子が好まれる距離が生まれ、pair correlationは分子スケールで振動する。

このようなpackingは、$k=0$ 近傍の情報ではなく、分子間距離に対応する**有限波数**の構造として現れる。

最低次square-gradient theoryでは、このpreferred wavelengthを持つことができない。

### 捨てたもの3：oscillatory layering

壁や強い界面の近傍では、密度は単調にbulkへ戻るとは限らず、

$$\rho(z)-\rho_b\sim e^{-\alpha z}\cos(qz+\phi)$$

のように減衰振動することがある。

ところがsquare-gradientの線形化から得られる基本的なbulk tailは

$$\delta\rho(z)\sim e^{-z/\xi}$$

のような単調減衰である。

これは偶然ではない。$A(k)$ を $A_0+A_2k^2$ までしか残さなければ、有限の実波数を選ぶ構造が消えているからである。

### 捨てたもの4：bulk correlationの有限波数構造

一様液体のstructure factor $S(k)$ は、一般には $k=0$ だけで特徴づけられない。高密度液体では分子間距離に対応する有限 $k$ に第一ピークが現れる。

square-gradient theoryは、そのような有限波数のsoftな応答を区別せず、長波長極限だけへ押し込める。

したがって、壁がbulk液体自身のpreferred wavelengthを励起してlayeringを作る、といった現象は最低次の理論からは見えない。

## 何を残し、何を捨てたか

van der Waalsのdiffuse-interface theoryは、Young–LaplaceやGibbsが表面量へ縮約した界面から、密度場と有限の界面幅を取り戻した。

しかしsquare-gradient approximationを採用した時点で、さらに一段の粗視化を行っている。

概念的には、

$$\text{full nonlocal interaction}\quad\longrightarrow\quad\text{long-wavelength moments}\quad\longrightarrow\quad f_0(\rho),\ \kappa$$

である。

この操作で残るのは、相分離を生むbulk thermodynamics、滑らかな密度変化、有限の界面幅、そしてそのプロファイルから得られる表面張力である。

一方で捨てられるのは、kernelの細かな形、packing、有限波数のbulk correlation、分子スケールのlayeringである。

したがってvan der Waalsの理論は「界面内部を解く理論」であると同時に、**界面内部のうち長波長成分だけを残した理論**でもある。

ここが次の問いを自然に決める。

> $k=0$ 周りだけを見るのをやめ、液体がもつ有限波数の構造を残すと、界面や壁近傍の密度場はどう変わるのか。

この先では、bulk correlation、direct correlation function、structure factor $S(k)$、そしてfinite-$k$ responseを使って、square-gradientで捨てた構造を取り戻していく。

## 歴史の中での位置づけ

ここまでの流れを整理すると、Young–Laplaceは界面内部を捨てて $\gamma$ を与え、Gibbsは界面内部を解かずsurface excessとして熱力学へ組み込み、van der Waalsは有限幅の密度場を解いて界面構造から $\gamma$ を導く道を開いた。

後にCahn–Hilliardは、このsquare-gradient型の自由エネルギーを一般の組成場に対する汎関数として整理し、保存則と組み合わせて相分離動力学へ発展させる。しかし静的な界面論の骨格だけを見れば、van der Waalsから続く同じsquare-gradient familyにある。

一方、液体固有のpackingやfinite-$k$ structureを保持する方向は、square-gradientをさらに一般化するというより、そこで捨てた**非局所なbulk correlation**へ戻る方向である。

## References

- J. D. van der Waals, *Thermodynamische theorie der cappillariteit in de onderstelling van continue dichtheidsverandering* (1893).
- J. S. Rowlinson, “Translation of J. D. van der Waals' ‘The thermodynamic theory of capillarity under the hypothesis of a continuous variation of density’,” *Journal of Statistical Physics* **20**, 197–244 (1979), DOI: 10.1007/BF01011514.
- J. S. Rowlinson and B. Widom, *Molecular Theory of Capillarity*, Clarendon Press (1982).
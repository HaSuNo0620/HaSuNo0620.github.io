---
title: "平方勾配近似による有限幅界面の理論"
summary: "非局所相互作用の長波長展開から平方勾配係数を導き、平面界面の密度分布、表面張力、有限波数応答に対する近似の限界を調べる。"
publishedAt: 2026-09-09T22:30:00+09:00
updatedAt: 2026-11-28
area: "Physics"
field: interfaces
kind: theory
related: ["gibbs-to-tolman-gauge-curvature", "kirkwood-buff-stress-anisotropy"]
topics: ["interfacial physics", "diffuse interface", "van der Waals", "square-gradient theory", "capillarity"]
status: growing
---

液体と気体の共存を局所自由エネルギーだけで記述すると、二相を隔てる密度変化の幅は決まらない。密度場の空間変化に対してエネルギーを割り当てることで、界面幅と表面張力を同じ変分問題から求められる。van der Waalsの連続密度理論を、現代的な平方勾配近似の形式で考える。

## 非局所相互作用から平方勾配項へ

数密度 $\rho(\mathbf r)$ に対する模型自由エネルギーを

$$
F[\rho]=\int f_{\rm ref}(\rho)\,d\mathbf r+
\frac12\int d\mathbf r\,d\mathbf s\,
\rho(\mathbf r)w(s)\rho(\mathbf r+\mathbf s)
$$

とする。$w(s)$ は等方的な有効相互作用核である。これは二体密度を一体密度の積で近似する平均場型の模型であり、一般の分子流体の厳密な自由エネルギー汎関数ではない。

密度変化が相互作用核の代表長さより十分緩やかであれば、$\rho(\mathbf r+\mathbf s)$ を展開できる。$d$ 次元で

$$
W_n=\int |\mathbf s|^n w(s)\,d\mathbf s
$$

とすると、等方性より $\int s_i w(s)d\mathbf s=0$、$\int s_i s_jw(s)d\mathbf s=\delta_{ij}W_2/d$ である。二次まで残し、境界項が消える条件で部分積分すると

$$
F[\rho]\simeq\int d\mathbf r
\left[f_{\rm ref}(\rho)+\frac{W_0}{2}\rho^2
-\frac{W_2}{4d}|\nabla\rho|^2\right].
$$

従って $f_0=f_{\rm ref}+W_0\rho^2/2$ と置けば

$$
F[\rho]=\int d\mathbf r\left[f_0(\rho)+\frac{\kappa}{2}|\nabla\rho|^2\right],
\qquad \kappa_{\rm nl}=-\frac{W_2}{2d}.
$$

引力核が負であればこの寄与は正となる。ただし一般の密度汎関数では参照系の非局所性も勾配係数に寄与しうる。展開には少なくとも核の零次・二次モーメントの絶対収束が必要である。四次まで解析的に展開できるとは限らず、例えば三次元の非切断の $r^{-6}$ 尾では四次モーメントは発散する。

ここで用いる $f_0$ は一様密度を仮定した模型の局所自由エネルギーである。相分離を許した巨視的な平衡自由エネルギーは凸包化されるので、非凸な局所関数をそれと同一視してはならない。

## 平面界面の変分問題

一定温度・化学ポテンシャルの下で

$$
\Omega[\rho]=\int d\mathbf r\left[
\omega(\rho)+\frac{\kappa}{2}|\nabla\rho|^2
\right],\qquad \omega(\rho)=f_0(\rho)-\mu\rho
$$

とする。以下では $\kappa>0$ を密度に依存しない定数とする。変分により

$$
\omega'(\rho)-\kappa\nabla^2\rho=0
$$

を得る。平面界面では $\rho(-\infty)=\rho_v$、$\rho(+\infty)=\rho_l$、両端で $\rho'=0$ とする。共存条件は $\omega'(\rho_v)=\omega'(\rho_l)=0$、$\omega(\rho_v)=\omega(\rho_l)=\omega_b$ である。

方程式に $\rho'$ を掛けて積分すると

$$
\frac{\kappa}{2}(\rho')^2=\omega(\rho)-\omega_b.
$$

右辺が二相間で正なら、単調な界面プロファイルは

$$
z-z_0=\int_{\rho(z_0)}^{\rho(z)}
\sqrt{\frac{\kappa}{2[\omega(u)-\omega_b]}}\,du
$$

から決まる。局所自由エネルギーが中間密度を取ることに伴うコストと、密度勾配のコストが釣り合うことで有限幅の界面が形成される。

## 対称二重井戸の厳密プロファイル

秩序変数 $\phi$ に対し、局所ポテンシャルを

$$
V(\phi)=\frac b4(\phi^2-\phi_b^2)^2,\qquad
\phi_b=\sqrt{a/b},\quad a,b>0
$$

とする。これはvan der Waals原論文そのものではなく、対称化したLandau型模型である。第一積分

$$
\frac{\kappa}{2}(\phi')^2=\frac b4(\phi^2-\phi_b^2)^2
$$

を分離積分すると

$$
\phi(z)=\phi_b\tanh\frac{z-z_0}{\ell},
\qquad \ell=\sqrt{\frac{2\kappa}{a}}
$$

を得る。$\ell$ はtanh関数の引数で定義した幅である。秩序変数の全変化量の10%から90%までの距離を幅とするなら $w_{10-90}=2\ell\operatorname{atanh}(0.8)$ となる。バルク近傍の線形応答の相関長は $\sqrt{\kappa/(2a)}=\ell/2$ であり、界面幅の規約と区別する必要がある。

## 表面張力

平面界面の過剰グランドポテンシャルの面積密度は

$$
\gamma=\int dz\left[\omega(\rho)-\omega_b+\frac{\kappa}{2}(\rho')^2\right].
$$

第一積分を用いれば

$$
\gamma=\int dz\,\kappa(\rho')^2
=\int_{\rho_v}^{\rho_l}\sqrt{2\kappa[\omega(\rho)-\omega_b]}\,d\rho.
$$

対称二重井戸模型では $\phi'=(\phi_b/\ell)\operatorname{sech}^2[(z-z_0)/\ell]$ なので、

$$
\gamma=\frac{4\kappa\phi_b^2}{3\ell}
=\frac{2\sqrt{2\kappa}\,a^{3/2}}{3b}.
$$

したがって界面幅と表面張力は独立の入力値ではない。局所自由エネルギーと勾配係数を与えれば、両者が同時に決まる。求めた密度プロファイルから[Gibbsの表面過剰量](/notes/gibbs-to-tolman-gauge-curvature/)を計算することもできる。

## 密度応答から見た近似の限界

安定な一様相 $\rho_b$ の周りで $\rho=\rho_b+\delta\rho$ とし、二次変分を取ると

$$
\delta^2 F/2=\frac12\int\frac{d^d k}{(2\pi)^d}
[f_0''(\rho_b)+\kappa k^2]|\delta\rho_{\mathbf k}|^2
$$

となる。外部ポテンシャル $V_{\rm ext}$ が $\int\rho V_{\rm ext}\,d\mathbf r$ と結合する場合、線形応答は

$$
\delta\rho_{\mathbf k}=-\frac{V_{{\rm ext},\mathbf k}}
{f_0''(\rho_b)+\kappa k^2}.
$$

Gaussian揺らぎ近似では、通常の粒子数で規格化した構造因子は

$$
S(k)=\frac{k_{\rm B}T}{\rho_b[f_0''(\rho_b)+\kappa k^2]}
$$

となる。正の $\kappa$ と $f_0''(\rho_b)$ の下で、この関数は波数とともに単調減少する。壁近傍で外部ポテンシャルが消える領域の線形方程式も

$$
\kappa\delta\rho''=f_0''(\rho_b)\delta\rho
$$

であり、減衰解は $\exp[-z\sqrt{f_0''(\rho_b)/\kappa}]$ となる。複素波数を持つ減衰振動はこの斉次方程式からは得られない。

高密度液体では排除体積に由来する有限波数の構造因子ピークや、壁に沿った層状の密度振動が現れることがある。これらを扱うには、平方勾配近似より多くの波数依存性を保持した非局所密度汎関数などが必要になる。単純に界面幅のパラメータを調整しても、欠落した有限波数構造は復元できない。

## 参考文献

- J. D. van der Waals, *Thermodynamische theorie der capillariteit in de onderstelling van continue dichtheidsverandering* (1893).
- J. S. Rowlinson, “Translation of J. D. van der Waals' ‘The thermodynamic theory of capillarity under the hypothesis of a continuous variation of density’,” *Journal of Statistical Physics* **20**, 197–244 (1979).
- J. S. Rowlinson and B. Widom, *Molecular Theory of Capillarity*, Clarendon Press (1982).

歴史的な原論文と現代的な平均場・勾配展開は区別した。書誌情報と原典の詳細は別途照合する。

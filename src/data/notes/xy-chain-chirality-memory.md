---
title: "1次元一様第二近接 U(1) スピン系 — chirality kinkと複数の空間記憶"
summary: "第二近接相互作用で生じる ±q* のchirality二重性を、kink、transfer operator、tilted spectrum、telegraph過程の各表示からつなぐ。局所preferred twist q*、実空間相関波数 q_corr、構造因子ピーク Q_peak、および ξ_chi と ξ_spin が一般に一致しないことを整理する。"
publishedAt: 2026-09-15T15:55:00+09:00
updatedAt: 2026-09-19
area: "Physics"
topics: ["XY model", "chirality", "frustration"]
status: growing
---

第二近接XY鎖の螺旋側では、相関関数を単に

$$
C(r)\sim e^{-r/\xi}\cos(qr)
$$

と書くだけでは、どの記憶が失われているのかが混ざる。局所的に好まれる twist、実空間で観測される振動波数、Fourier 空間で最大になる波数は一般に同じではない。相関長も一つではなく、continuous phase fluctuation と chirality switching が別の記憶チャネルを持つ。

モデルは

$$
H=
-J_1\sum_i\cos(\theta_{i+1}-\theta_i)
-J_2\sum_i\cos(\theta_{i+2}-\theta_i)
$$

で、

$$
\phi_i=\theta_{i+1}-\theta_i,
\qquad
\kappa=\frac{|J_2|}{J_1},
\qquad
J_2<0
$$

とする。以後

$$
\beta\equiv\frac{1}{k_{\mathrm B}T}
$$

を使う。

## 系の座標

$$
\boxed{
(d=1,\ \text{uniform},\ R=2,\ U(1))
}
$$

対象は一様第二近接 $U(1)$ 系の螺旋側である。Hamiltonian 自体は

$$
H
=
-J_1\sum_i\cos(\theta_{i+1}-\theta_i)
-J_2\sum_i\cos(\theta_{i+2}-\theta_i)
$$

のままで、ここでは同じ座標点の中に現れる複数の memory channel

$$
\text{phase},\qquad
\text{chirality},\qquad
\text{spin correlation}
$$

を分離して読む。

## 螺旋側では chirality が二重化する

一様 twist $\phi_i=q$ のエネルギー密度は

$$
e(q)=-J_1\cos q-J_2\cos2q
$$

である。

$\kappa>1/4$ では

$$
\boxed{q_\ast=\arccos\frac{1}{4\kappa}}
$$

が選ばれ、$+q_\ast$ と $-q_\ast$ が縮退する。

局所 chirality を

$$
\chi_i=\sin\phi_i
$$

とすれば、低温では

$$
\chi_i\simeq\pm\sin q_\ast.
$$

つまり continuous angle の中に、右巻き・左巻きという離散自由度が現れる。

## Lifshitz点近傍では kink が広がる

$\kappa=1/4+\delta$、$\delta>0$ として $\phi\ll1$ で展開すると、連続場の自由エネルギーは

$$
F[\phi]
=\int dx\left[
\frac{B}{2}(\partial_x\phi)^2
+\frac{J_1}{8}(\phi^2-\phi_0^2)^2
\right],
$$

$$
B=J_1\kappa,
\qquad
\phi_0^2=8\delta.
$$

chirality kink は

$$
\boxed{
\phi_{\mathrm k}(x)
=\phi_0\tanh\frac{x-x_0}{\ell_{\mathrm k}}
}
$$

で、

$$
\boxed{
\ell_{\mathrm k}
=\sqrt{\frac{\kappa}{2\delta}}
}
$$

となる。

kink energy は

$$
\boxed{
E_{\mathrm k}
=\frac{32\sqrt2}{3}J_1\sqrt\kappa\,\delta^{3/2}
}
$$

であり、$\kappa\simeq1/4$ では

$$
\boxed{
E_{\mathrm k}
\simeq
\frac{16\sqrt2}{3}J_1
\left(\kappa-\frac14\right)^{3/2}
}.
$$

$3/2$ 乗は barrier height $\sim\delta^2$ と kink width $\sim\delta^{-1/2}$ の積から出る。

低温で kink が希薄なら

$$
\xi_\chi\sim\exp\left(\frac{E_{\mathrm k}}{k_{\mathrm B}T}\right).
$$

一方、chirality を固定した sector 内では位相は Gaussian に拡散し、

$$
\xi_{\mathrm{ph}}
\simeq
\frac{2A_0}{k_{\mathrm B}T},
$$

$$
A_0
=J_1\left(4\kappa-\frac{1}{4\kappa}\right).
$$

したがって十分低温では

$$
\boxed{\xi_\chi\gg\xi_{\mathrm{ph}}}
$$

となりうる。

## 低温有効理論は telegraph + diffusion になる

粗視化すると

$$
\boxed{
\frac{d\theta}{dx}
=q_\ast\sigma(x)+\eta(x)
}
$$

と書ける。$\sigma=\pm1$ は chirality、$\eta$ は continuous phase noise である。

chirality flip rate を $\nu$ とすると

$$
\langle\sigma(0)\sigma(r)\rangle=e^{-2\nu r},
$$

したがって

$$
\boxed{\xi_\chi=\frac{1}{2\nu}}.
$$

phase diffusion を

$$
\left\langle
\exp\left(i\int_0^r\eta(x)dx\right)
\right\rangle
=e^{-Dr}
$$

とすると、spin correlation は

$$
C(r)=e^{-Dr}F(r)
$$

で、$F$ は

$$
F''+2\nu F'+q_\ast^2F=0
$$

を満たす。

$q_\ast>\nu$ では

$$
\boxed{
q_{\mathrm{corr}}
=\sqrt{q_\ast^2-\nu^2}
}
$$

で振動し、包絡から

$$
\boxed{
\xi_{\mathrm{spin}}^{-1}
=D+\nu
=\xi_{\mathrm{ph}}^{-1}+\frac{1}{2\xi_\chi}
}
$$

が得られる。

$q_\ast=\nu$ で oscillatory correlation が消える。この境界は局所 preferred twist $q_\ast$ が消えたことを意味しない。chirality switching が速くなり、長距離の位相蓄積が打ち消されただけである。

## 構造因子の peak はさらに別の波数を持つ

$D=0$ なら

$$
S(Q)
=\frac{4\nu q_\ast^2}
{(q_\ast^2-Q^2)^2+4\nu^2Q^2}.
$$

その最大位置は

$$
\boxed{
Q_{\mathrm{peak}}
=\sqrt{q_\ast^2-2\nu^2}
}
$$

である。

したがって

$$
\boxed{
Q_{\mathrm{peak}}<q_{\mathrm{corr}}<q_\ast
}
$$

となり、二峰構造が $Q=0$ に融合する条件

$$
\nu=\frac{q_\ast}{\sqrt2}
$$

と、実空間振動が消える条件

$$
\nu=q_\ast
$$

は一致しない。

つまり

$$
\frac{q_\ast}{\sqrt2}<\nu<q_\ast
$$

では、$S(Q)$ はすでに $Q=0$ 最大なのに、$C(r)$ にはまだ振動が残る。

## ordinary transfer operator は chirality memory を持つ

$\phi$ を状態変数にすると、kernel は

$$
\mathcal T(\phi,\phi')
=
\exp\left[
\frac{\beta J_1}{2}(\cos\phi+\cos\phi')
+\beta J_2\cos(\phi+\phi')
\right].
$$

Fourier basis

$$
|m\rangle=\frac{e^{im\phi}}{\sqrt{2\pi}}
$$

では

$$
\boxed{
T_{mn}
=\sum_{\ell=-\infty}^{\infty}
I_{m-\ell}\left(\frac{\beta J_1}{2}\right)
I_{n+\ell}\left(\frac{\beta J_1}{2}\right)
I_\ell(\beta J_2)
}
$$

となる。

$\mathcal T$ は $\phi\to-\phi$ と可換するため even / odd sector に分かれる。最大 even 固有値を $\lambda_0$、最大 odd 固有値を $\lambda_\chi$ とすると

$$
\boxed{
\xi_\chi^{-1}
=-\ln\left|\frac{\lambda_\chi}{\lambda_0}\right|
}.
$$

chirality kink の希薄化は、transfer spectrum では even / odd splitting の指数的小ささとして見える。

## spin memory は tilted spectrum に入る

spin correlation は

$$
C_+(r)
=
\left\langle
\prod_{j=0}^{r-1}e^{i\phi_j}
\right\rangle
$$

なので、multiplication operator

$$
(\mathcal M_+f)(\phi)=e^{i\phi}f(\phi)
$$

を含む tilted operator

$$
\boxed{\mathcal T_{\mathrm{spin}}=\mathcal M_+\mathcal T}
$$

が必要になる。

支配固有値を

$$
z_\ast=|z_\ast|e^{iq_{\mathrm{corr}}}
$$

とすると

$$
\boxed{
\xi_{\mathrm{spin}}^{-1}
=-\ln\left|\frac{z_\ast}{\lambda_0}\right|
}
$$

と

$$
\boxed{q_{\mathrm{corr}}=\arg z_\ast}
$$

が同時に出る。

ordinary transfer operator は実対称だが、tilted operator は非Hermitianなので複素固有値を持てる。実空間振動はこの eigenphase に対応する。

## 数値走査では memory channel の分離が直接見える

angle-grid 表現で同じ integral operator を離散化し、$\kappa=0.5$ で走査した。

このとき

$$
q_\ast=\arccos\frac12=\frac{\pi}{3}\simeq1.0472.
$$

| $\beta J_1$ | $q_{\mathrm{corr}}$ | $Q_{\mathrm{peak}}$ | $\xi_\chi$ | $\xi_{\mathrm{spin}}$ |
| ---: | ---: | ---: | ---: | ---: |
| 4 | 1.0297 | 1.0066 | 2.44 | 3.42 |
| 6 | 1.0224 | 1.0158 | 5.38 | 6.08 |
| 8 | 1.0257 | 1.0236 | 12.57 | 10.72 |
| 10 | 1.0298 | 1.0289 | 30.68 | 17.47 |
| 12 | 1.0328 | 1.0328 | 76.82 | 25.45 |
| 16 | 1.0367 | 1.0367 | 502.14 | 41.01 |

低温へ行くと $q_{\mathrm{corr}}$ と $Q_{\mathrm{peak}}$ は $q_\ast$ に近づく一方、$\xi_\chi$ は $\xi_{\mathrm{spin}}$ よりはるかに速く伸びる。$\beta J_1=16$ では

$$
\frac{\xi_\chi}{\xi_{\mathrm{spin}}}\simeq12.2.
$$

spin direction の記憶が失われても、右巻きか左巻きかという chirality memory はさらに遠くまで残りうる。

## 同じ「波数」「相関長」に見えていたものを分ける

この模型では少なくとも

$$
\boxed{
q_\ast
=\text{local preferred twist}
}
$$

$$
\boxed{
q_{\mathrm{corr}}
=\text{real-space oscillation wave number}
}
$$

$$
\boxed{
Q_{\mathrm{peak}}
=\text{structure/response peak position}
}
$$

を分ける必要がある。

同様に

$$
\boxed{
\xi_{\mathrm{ph}},\qquad
\xi_\chi,\qquad
\xi_{\mathrm{spin}}
}
$$

も別の memory channel である。

第二近接相互作用が作っているのは単なる finite-$q$ correlation ではない。continuous phase diffusion に discrete chirality switching が重なり、観測量ごとに異なる spectral object が支配する構造である。

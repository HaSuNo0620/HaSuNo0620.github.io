---
title: "1次元一様最近接 cosine スピン系 — Z2・Zq・U(1)と相関の連続化"
summary: "1次元一様最近接 cosine スピン系を、Z2・Zq・U(1)という局所状態空間の違いだけを動かして比較する。局所位相増分、1-step retention、転送スペクトル、相関長、波数応答を共通言語にし、稀なドメイン壁からfinite-angle jumpを経て位相拡散へ移る構造を整理する。"
publishedAt: 2026-09-13T01:50:00+09:00
updatedAt: 2026-09-19
area: "Physics"
topics: ["statistical mechanics", "spin model", "clock model", "Ising model", "XY model", "correlation", "transfer matrix", "memory", "nearest-neighbor", "linear response"]
status: growing
system:
  dimension: 1
  spatial: uniform
  range: R1
  interaction: cosine
  symmetry: [Z2, Zq, U(1)]
  mechanics: classical
  role: comparison
---

Ising、clock、XYという名前を外すと、三者は同じ Hamiltonian で書ける。

$$
\boxed{
H=-J\sum_i\cos(\theta_{i+1}-\theta_i)
}
$$

違うのは、各 site で許される角度の集合だけである。

$$
\boxed{
\theta_i\in
\begin{cases}
Z_2={0,\pi\},\\[1mm]
Z_q=\left\{\dfrac{2\pi n}{q}\right\}_{n=0}^{q-1},\\[3mm]
U(1)=S^1.
\end{cases}
}
$$

$Z_2$ では

$$
s_i=\cos\theta_i=\pm1
$$

と書けば

$$
\cos(\theta_{i+1}-\theta_i)=s_i s_{i+1}
$$

なので、標準最近接 Ising 鎖は cosine-$Z_2$ の特殊例そのものである。

以下では

$$
\beta=\frac{1}{k_{\mathrm B}T},
\qquad
K=\beta J
$$

とする。

## 比較座標

固定する座標は

$$
\boxed{
(d=1,\ \text{uniform},\ R=1,\ \text{cosine},\ \text{classical})
}
$$

であり、動かすのは

$$
\boxed{
Z_2
\longrightarrow
Z_q
\longrightarrow
U(1)
}
$$

という 状態空間 / 対称性 だけである。

比較する中心量は

$$
\boxed{
\text{局所増分}
\to
\text{1-step retention}
\to
\text{転送スペクトル}
\to
\xi
\to
\chi(k)
}
$$

とする。

---

## 1. 三者の局所変数はすべて位相増分に統一できる

局所増分を

$$
\boxed{
\phi_i=\theta_{i+1}-\theta_i
}
$$

とする。

許される値は

$$
\phi_i\in
\begin{cases}
\{0,\pi\}, & Z_2,\\[1mm]
\left\{\dfrac{2\pi a}{q}\right\}_{a=0}^{q-1}, & Z_q,\\[3mm]
S^1, & U(1).
\end{cases}
$$

Hamiltonian は三者すべて

$$
\boxed{
H=-J\sum_i\cos\phi_i
}
$$

である。

$Z_2$ では

$$
e^{i\phi_i}
=s_i s_{i+1}
\equiv\tau_i
=\pm1
$$

だから、従来の ドメイン壁変数は位相増分表示の $q=2$ 特殊例になる。

一方 $U(1)$ では $\phi_i$ は連続量である。

したがって

$$
\boxed{
\{0,\pi\}
\to
\left\{\frac{2\pi a}{q}\right\}
\to
S^1
}
$$

は、局所 局所状態の集合 の細分化として読める。

---

## 2. 遠距離相関も同じ積に統一できる

距離 $r$ の角度差は

$$
\theta_r-\theta_0 = \sum_{j=0}^{r-1}\phi_j
$$

なので、

$$
e^{im(\theta_r-\theta_0)} = \prod_{j=0}^{r-1}e^{im\phi_j}.
$$

最近接・零外場では各 $\phi_j$ は独立だから、

$$
C_m(r)
\equiv
\left\langle
e^{im(\theta_r-\theta_0)}
\right\rangle = \left[
\left\langle e^{im\phi}\right\rangle
\right]^r.
$$

そこで

$$
\boxed{
\rho_m
\equiv
\left\langle e^{im\phi}\right\rangle
}
$$

と置けば、

$$
\boxed{
C_m(r)=\rho_m^r
}
$$

となる。

三者の違いは、相関の形式ではなく $\rho_m$ を作る局所 状態空間 にある。

---

## 3. 1-step retention は離散Fourier和から連続Fourier積分へ移る

$Z_q$ では 転送行列 は circulant で、

$$
T_{ab} = \exp\left[
K\cos\frac{2\pi(a-b)}q
\right].
$$

固有値は

$$
\boxed{
\Lambda_m^{(q)} = \sum_{a=0}^{q-1}
e^{K\cos(2\pi a/q)}
e^{-2\pi i ma/q}
}
$$

である。

したがって

$$
\boxed{
\rho_m^{(q)} = \frac{\Lambda_m^{(q)}}{\Lambda_0^{(q)}}
}
$$

となる。

$q=2$ では

$$
\Lambda_0^{(2)}=2\cosh K,
\qquad
\Lambda_1^{(2)}=2\sinh K,
$$

よって

$$
\boxed{
\rho_1^{(2)}=\tanh K
}
$$

となる。

これは最近接 $Z_2$ 鎖の

$$
C(r)=(\tanh K)^r
$$

そのものである。

一方 $q\to\infty$ では離散和が円周積分へ移り、

$$
\Lambda_m^{(q)}
\sim qI_m(K),
$$

したがって

$$
\boxed{
\rho_m^{U(1)} = \frac{I_m(K)}{I_0(K)}
}
$$

を得る。

つまり

$$
\boxed{
\tanh K
\quad\longrightarrow\quad
\rho_1^{(q)}
\quad\longrightarrow\quad
\frac{I_1(K)}{I_0(K)}
}
$$

が同じ 1-step 履歴 の $Z_2\to Z_q\to U(1)$ 変形である。

---

## 4. finite $q$ は $U(1)$ スペクトルを折り畳む

Fourier 展開

$$
e^{K\cos\phi} = \sum_{n=-\infty}^{\infty}
I_n(K)e^{in\phi}
$$

を離散角で sample すると、

$$
\boxed{
\Lambda_m^{(q)} = q\sum_{\ell\in\mathbb Z}
I_{m+\ell q}(K)
}
$$

となる。

したがって

$$
\boxed{
\rho_m^{(q)} = \frac{
\displaystyle\sum_{\ell\in\mathbb Z}
I_{m+\ell q}(K)
}{
\displaystyle\sum_{\ell\in\mathbb Z}
I_{\ell q}(K)
}
}
$$

である。

有限 $q$ では

$$
m\sim m+q
$$

なので、本来 $U(1)$ で独立な 高調波 が同じセクターへ折り畳まれる。

$$
\boxed{
\text{finite 角度分解能}
\longleftrightarrow
\text{高調波-space aliasing}
}
$$

という対応になる。

![有限$q$の相関スペクトルとU(1)極限](/figures/clock-r1/memory-spectrum-folding.svg)

*$K=20$。低い 高調波 は比較的小さい $q$ でも早く $U(1)$ スペクトル へ近づく一方、$m\sim q/2$ の細かい角度情報には finite-$q$ の折り畳み が残る。*

---

## 5. 相関減衰 は 稀なドメイン壁 から 位相拡散 へ連続化する

$Z_2$ で非零増分は

$$
\phi=\pi
$$

だけで、その励起コストは

$$
\Delta E_2=2J.
$$

低温では

$$
p_{\rm wall}\sim e^{-2K}
$$

なので、相関減衰 は 疎な局在ドメイン壁 によって起こる。

$Z_q$ では最小非零増分が

$$
\Delta\phi_q=\frac{2\pi}{q}
$$

となり、そのエネルギーコストは

$$
\boxed{
\Delta E_q = J\left(
1-\cos\frac{2\pi}{q}
\right)
}
$$

である。

大きな $q$ では

$$
\Delta E_q
\simeq
\frac{J}{2}
\left(
\frac{2\pi}{q}
\right)^2.
$$

一方 $U(1)$ の低温局所分布は

$$
P(\phi)
\propto
e^{-K\phi^2/2}
$$

なので 熱揺らぎ幅 は

$$
\sigma_T\sim K^{-1/2}.
$$

clock spacing と 熱揺らぎ幅 の比

$$
\boxed{
\eta = \frac{2\pi/q}{K^{-1/2}} = \frac{2\pi\sqrt K}{q}
}
$$

が離散性を支配する。

$$
\eta\gg1
\quad\Rightarrow\quad
\text{稀な離散ジャンプ},
$$

$$
\eta\ll1
\quad\Rightarrow\quad
\text{dense small-step 位相拡散}.
$$

したがって

$$
\boxed{
Z_2:
\text{稀なドメイン壁}
\to
Z_q:
\text{有限角ジャンプ}
\to
U(1):
\text{位相拡散}
}
$$

という連続的な像が得られる。

---

## 6. 相関長は activated から diffusive へ移る

$m=1$ の相関長は全て

$$
\boxed{
\xi^{-1} = -\ln|\rho_1|
}
$$

で定義できる。

$Z_2$ では

$$
\boxed{
\xi_{Z_2} = \frac{1}{
-\ln(\tanh K)
}
\simeq
\frac12e^{2K}
}
$$

である。

有限 $q\ge3$ を固定して低温へ行くと、

$$
\boxed{
\xi_{Z_q}
\simeq
\frac{
\exp\left[
K\left(1-\cos\dfrac{2\pi}{q}\right)
\right]
}{
2\left(1-\cos\dfrac{2\pi}{q}\right)
}
}
$$

となり、やはり activated である。

一方 $U(1)$ では

$$
\frac{I_1(K)}{I_0(K)}
\simeq
e^{-1/(2K)}
$$

なので

$$
\boxed{
\xi_{U(1)}
\simeq
2K
}
$$

となる。

したがって

$$
\boxed{
\text{finite }q:
\text{活性化型相関}
\qquad
\longrightarrow
\qquad
q=\infty:
\text{拡散型相関}
}
$$

である。

ただし crossover は $q$ 単独では決まらず、

$$
\boxed{
\frac{q}{\sqrt K}
}
$$

で整理される。

![相関長のfinite-qからU(1)へのcross-over](/figures/clock-r1/correlation-length-crossover.svg)

*$q/\sqrt K$ が大きくなると finite-$q$ 相関長は $U(1)$ 値へ急速に近づく。同じ $q$ でも十分低温へ行けば離散性は再び解像される。*

---

## 7. (q	oinfty) と (T	o0) は可換ではない

有限 $q$ を固定して

$$
K\to\infty
$$

とすると

$$
\eta = \frac{2\pi\sqrt K}{q}
\to\infty
$$

なので、どれほど大きな $q$ でも最終的には 離散ジャンプ領域 へ戻る。

一方、先に

$$
q\to\infty
$$

として $U(1)$ に移れば局所励起 gap は閉じており、その後 $K\to\infty$ としても

$$
\xi\sim2K
$$

の diffusive asymptote が残る。

$$
\boxed{
\lim_{K\to\infty}\lim_{q\to\infty}
\neq
\lim_{q\to\infty}\lim_{K\to\infty}
}
$$

という非一様性がある。

この違いは「大きな finite $q$」と「真の $U(1)$」を区別する。

---

## 8. 高調波 相関 は (Z_2) の1本から (U(1)) の無限階層へ開く

$Z_2$ では非自明な 高調波セクター は実質

$$
m=1
$$

の1本だけである。

$Z_q$ では

$$
m=0,1,\ldots,\lfloor q/2\rfloor
$$

程度の独立 sector を持つ。

$U(1)$ では

$$
m=0,1,2,\ldots
$$

と無限に続く。

低温 $U(1)$ では

$$
\rho_m
\simeq
e^{-m^2/(2K)}
$$

なので

$$
\boxed{
\xi_m
\simeq
\frac{2K}{m^2}
}
$$

となる。

![高調波ごとの相関長](/figures/clock-r1/harmonic-memory-hierarchy.svg)

*finite $q$ では低い 高調波 から $m^{-2}$ hierarchy が回復し、高角度分解能の相関 ほど離散性を長く保持する。*

したがって

$$
\boxed{
Z_2:
\text{one nontrivial 相関モード}
\to
Z_q:
\text{finite 高調波 spectrum}
\to
U(1):
\text{infinite hierarchy}
}
$$

という変化が起こる。

---

## 9. 波数応答も同じ 空間フィルター に還元される

$m=1$ 相関が

$$
C(r)=\rho_1^{|r|}
$$

なら、その Fourier 和は

$$
\boxed{
\sum_{r=-\infty}^{\infty}
\rho_1^{|r|}e^{-ikr} = \frac{1-\rho_1^2}
{1-2\rho_1\cos k+\rho_1^2}
}
$$

である。

したがって三者とも、零外場の $m=1$ 相関 を読む 空間応答 は同じ denominator を持つ。

$Z_2$ では スカラー・スピン 自体が $m=1$ 観測量 なので

$$
\chi_{Z_2}(k) = \beta
\frac{1-\rho_1^2}
{1-2\rho_1\cos k+\rho_1^2}.
$$

$Z_q$ と $U(1)$ の planar $x$ 成分では、$q>2$ なら回転対称平均から

$$
\chi^{xx}(k) = \frac{\beta}{2}
\frac{1-\rho_1^2}
{1-2\rho_1\cos k+\rho_1^2}.
$$

振幅は 観測量 の規格化で異なるが、フィルター幅 はすべて

$$
\boxed{
k_\times
\sim
\xi^{-1}
}
$$

で決まる。

長波長・長相関長極限では

$$
\boxed{
\chi(k)
\propto
\frac{\xi}{1+(k\xi)^2}
}
$$

となり、自然な変数は

$$
\boxed{
k\xi
}
$$

である。

したがって 対称性 / 状態空間 の違いは、最終的には

$$
\rho_1(T)
\to
\xi(T)
\to
\text{空間フィルター width}
$$

を通じて 応答 に伝わる。

---

## 10. 三つの系は「別模型」より一つの離散化系列として読める

従来の名称では

$$
\text{Ising}
\to
\text{clock}
\to
\text{XY}
$$

と三つの模型に見える。

しかし cosine family を固定すると、

$$
\boxed{
H=-J\sum_i\cos(\theta_{i+1}-\theta_i)
}
$$

は変わらない。

動いているのは

$$
\boxed{
\text{局所状態空間}
}
$$

だけである。

実空間では

$$
\boxed{
\text{稀なドメイン壁}
\to
\text{有限角ジャンプ}
\to
\text{位相拡散}
}
$$

となり、spectral space では

$$
\boxed{
\text{one mode}
\to
\text{有限の折り畳みスペクトル}
\to
\text{infinite 高調波階層}
}
$$

となる。

さらに 応答 では三者とも

$$
\boxed{
\text{局所転送則}
\to
\rho_1
\to
\xi
\to
\chi(k)
}
$$

という同じ骨格へ戻る。

## 得られた見方

1次元一様最近接 cosine スピン系では、

$$
\boxed{
Z_2\to Z_q\to U(1)
}
$$

は模型を丸ごと取り替える操作ではなく、

$$
\boxed{
\text{同じ 相互作用族 のもとで
局所角度分解能を連続化する操作}
}
$$

として読める。

その連続化は、実空間では defect から diffusion への変化、Fourier 空間では スペクトルの折り畳み の解除、長距離では activated から 拡散型相関 への変化として同時に現れる。

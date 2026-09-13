---
title: "1次元最近接スピン模型 — IsingとXYから見る空間記憶"
summary: "1次元最近接Ising鎖とXY鎖を比較し、離散的domain wallと連続的phase diffusion、transfer spectrum、外場応答の共通構造と相違を整理する。"
publishedAt: 2026-09-13T01:50:00+09:00
updatedAt: 2026-09-13
area: "Physics"
topics: ["statistical mechanics", "Ising model", "XY model", "correlation", "transfer matrix", "memory", "nearest-neighbor"]
status: growing
---

1次元の最近接Ising鎖とXY鎖は、どちらも有限温度では長距離秩序を持たない。ところが、秩序を失う機構は同じではない。

以下では $\beta\equiv1/(k_{\mathrm B}T)$ とする。

## 1. Isingは稀な大きな反転、XYは至る所の小さな回転

最近接強磁性Ising鎖

$$
H_{\rm I}=-J\sum_i s_i s_{i+1}
$$

では bond 変数 $\tau_i=s_is_{i+1}$ を使うと、$\tau_i=-1$ がdomain wallである。壁1個の生成エネルギーは $2J$ なので

$$
p_{\rm dw}\sim e^{-2\beta J}
=e^{-2J/(k_{\mathrm B}T)}.
$$

一方XY鎖

$$
H_{\rm XY}=-J\sum_i\cos(\theta_{i+1}-\theta_i)
$$

では角度差 $\phi_i=\theta_{i+1}-\theta_i$ を任意に小さく取れる。低温では

$$
\langle\phi_i^2\rangle\simeq\frac{1}{\beta J}
=\frac{k_{\mathrm B}T}{J},
$$

だが

$$
\theta_r-\theta_0=\sum_{i=0}^{r-1}\phi_i
$$

が空間方向にrandom walkする。

したがって

$$
\boxed{\text{Ising}:\ \text{rare localized walls}}
$$

に対して

$$
\boxed{\text{XY}:\ \text{distributed small rotations}}
$$

である。

## 2. 相関を壊す数学も違う

Isingでは

$$
s_0s_r=\prod_{i=0}^{r-1}\tau_i,
$$

なので、途中にあるwallの個数の偶奇が遠距離の符号を決める。

XYでは

$$
\theta_r-\theta_0=\sum_{i=0}^{r-1}\phi_i,
$$

なので、角度差は局所増分の和で作られる。

つまり

$$
\boxed{\text{Ising}:\ \text{multiplicative sign process}}
$$

$$
\boxed{\text{XY}:\ \text{additive phase process}}
$$

である。

## 3. それでも二点相関は1-step memoryの積になる

Isingでは

$$
C_{\rm I}(r)=\left[\tanh(\beta J)\right]^r.
$$

XYでは

$$
C_{\rm XY}(r)
=\left[
\frac{I_1(\beta J)}{I_0(\beta J)}
\right]^r.
$$

両者とも

$$
\boxed{C(r)=\lambda^r}
$$

であり、$\lambda$ は1 bond進んだときの記憶保持率と読める。

## 4. 相関長の形は共通だが温度依存は違う

$C(r)=e^{-r/\xi}$ と比較すると

$$
\boxed{\xi^{-1}=-\ln|\lambda|}.
$$

Isingでは

$$
\xi_{\rm I}\simeq\frac12e^{2\beta J}
=\frac12\exp\left(\frac{2J}{k_{\mathrm B}T}\right),
$$

XYでは

$$
\xi_{\rm XY}\simeq2\beta J
=\frac{2J}{k_{\mathrm B}T}.
$$

したがって

$$
\boxed{
\text{指数相関は共通、相関長の温度依存は模型固有}
}
$$

である。

## 5. transfer spectrumから見ると共通構造が明確になる

Isingでは $2\times2$ transfer matrix、XYでは積分作用素を使う。しかしどちらも

$$
\boxed{
C_a(r)\sim\left(\frac{\lambda_a}{\lambda_0}\right)^r,
\qquad
\xi_a^{-1}=-\ln\left|\frac{\lambda_a}{\lambda_0}\right|
}
$$

で長距離相関が決まる。

XYでは

$$
\lambda_m=2\pi I_m(\beta J),
\qquad m=0,\pm1,\pm2,\ldots
$$

で、低温では

$$
\xi_m\simeq\frac{2J}{m^2k_{\mathrm B}T}.
$$

局所自由度が連続になることで、記憶距離にもharmonic階層が現れる。

## 6. 最近接1次元系に共通するもの

IsingとXYを比べると、少なくとも次の構造は共通している。

- 相互作用は隣接サイト間の局所Boltzmann重みで書ける。
- 空間方向の統計はtransfer matrix / transfer operatorの反復になる。
- 長距離相関はtransfer spectrumの固有値比で決まる。
- relevantなspectral gapが有限なら相関は指数減衰する。
- 相関長は1 stepごとの記憶損失の累積として読める。

したがって

$$
\boxed{
\text{nearest-neighbor 1D}
\Longrightarrow
\text{local transfer rule}
\Longrightarrow
\text{spectral memory propagation}
}
$$

という見方ができる。

## 7. 外場は「絶対方向」を持ち込む

零外場では、IsingもXYも相互作用が隣接サイトの相対的な向きだけに依存していた。

Isingでは $s_is_{i+1}$、XYでは $\theta_{i+1}-\theta_i$ が自然な局所変数であり、開鎖ならこれらの相対変数だけで問題がかなり単純になる。

一方、外場は相対方向ではなく絶対方向を見る。

$$
\boxed{
\text{interaction probes relative orientation}
\qquad
\text{field probes absolute orientation}
}
$$

この違いが、零外場で成立していた独立bond描像を壊す。

### 7.1 Isingではdomain-wall表示が非局所化する

一様外場を持つIsing鎖は

$$
H_{\rm I}(h)
=-J\sum_i s_is_{i+1}
-h\sum_i s_i.
$$

基準スピン $s_0$ を残すと

$$
s_i=s_0\prod_{j=0}^{i-1}\tau_j,
$$

だから外場項は

$$
-h\sum_i s_i
=-h s_0\sum_i\prod_{j=0}^{i-1}\tau_j.
$$

つまり、スピン変数では局所的な外場が、wall変数ではそれまで通過した全wallの偶奇に依存する長い積になる。

$$
\boxed{
\text{local field in spin variables}
\Longrightarrow
\text{nonlocal term in wall variables}
}
$$

このとき自然なのはスピン表示に戻り、

$$
T_{\rm I}
=
\begin{pmatrix}
 e^{\beta J+\beta h} & e^{-\beta J}\\
 e^{-\beta J} & e^{\beta J-\beta h}
\end{pmatrix}
$$

というtransfer matrixで解くことである。

### 7.2 XYでも角度差表示が非局所化する

XY鎖に $x$ 方向外場を入れると

$$
H_{\rm XY}(h)
=-J\sum_i\cos(\theta_{i+1}-\theta_i)
-h\sum_i\cos\theta_i.
$$

零外場では $\phi_i=\theta_{i+1}-\theta_i$ が独立だったが、

$$
\theta_i
=\theta_0+
\sum_{j=0}^{i-1}\phi_j
$$

なので、外場項は

$$
-h\sum_i
\cos\left(
\theta_0+\sum_{j=0}^{i-1}\phi_j
\right)
$$

となる。

つまりXYでも、絶対角を測る外場を入れると、角度差だけでは局所的に閉じなくなる。

Isingでは「符号の積」、XYでは「位相の和」と表現は違うが、

$$
\boxed{
\text{relative-variable description becomes nonlocal under a field}
}
$$

という構造は共通している。

### 7.3 XYでは外場がFourier sectorを混ぜる

零外場XYのtransfer kernelは

$$
T_0(\theta,\theta')
=
\exp[\beta J\cos(\theta'-\theta)]
$$

で、角度差だけに依存する。そのため $e^{im\theta}$ が独立な固有sectorだった。

外場を入れると

$$
T_h(\theta,\theta')
=
\exp\left[
\beta J\cos(\theta'-\theta)
+\frac{\beta h}{2}
(\cos\theta+\cos\theta')
\right]
$$

となる。

ここで $\cos\theta=(e^{i\theta}+e^{-i\theta})/2$ だから、Fourier空間では

$$
\boxed{m\longleftrightarrow m\pm1}
$$

が結合する。

したがってXYで外場を入れることは、単なるエネルギー補正ではなく、$U(1)$ symmetryを壊し、独立だったangular sectorを混ぜる操作である。

### 7.4 線形応答では零外場相関がそのまま感受率になる

微小外場なら、有限外場のtransfer spectrumを最初から解き直さなくても、零外場相関から応答を求められる。

Isingでは

$$
\chi_{\rm I}(r)
=\beta\langle s_0s_r\rangle
=\beta[\tanh(\beta J)]^{|r|}.
$$

XYでは

$$
\chi_{\rm XY}^{xx}(r)
=\beta\langle\cos\theta_0\cos\theta_r\rangle
$$

で、回転対称性から

$$
\langle\cos\theta_0\cos\theta_r\rangle
=\frac12\langle\mathbf S_0\cdot\mathbf S_r\rangle.
$$

したがって

$$
\boxed{
\chi_{\rm XY}^{xx}(r)
=\frac{\beta}{2}
\left[
\frac{I_1(\beta J)}{I_0(\beta J)}
\right]^{|r|}
}
$$

となる。

どちらも $\chi(r)\propto e^{-|r|/\xi}$ なので、外場に対する応答も零外場で作られた空間記憶長 $\xi$ をprobeしている。

### 7.5 空間変調外場では $q\xi$ が自然な変数になる

外場を

$$
h_i=h_q e^{iqi}
$$

のように変調すると、線形応答は

$$
\delta m(q)=\chi(q)h_q
$$

で与えられる。

指数相関

$$
\chi(r)\propto e^{-|r|/\xi}
$$

をFourier変換すると、長波長・長相関長の領域では

$$
\boxed{
\chi(q)\propto\frac{\xi}{1+(q\xi)^2}
}
$$

というLorentzian型になる。したがって、空間変調外場に対して本質的なのは $q$ と $\xi$ を別々に見ることではなく、無次元量 $q\xi$ である。

#### $q\xi\ll1$：相関領域全体が外場を追従できる

外場の波長 $\lambda_{\rm ext}=2\pi/q$ が相関長より十分長いとき、ひとつの相関領域の内部では外場はほぼ一定である。

$$
\boxed{q\xi\ll1}
$$

では、相関しているスピン群がほぼ同じ向きへ押されるため、協調的な応答が可能になる。

#### $q\xi\sim1$：空間応答のクロスオーバー

外場の空間変化と相関領域の大きさが同程度になると、相関領域の内部で外場の向きが無視できないほど変化する。

$$
\boxed{q\xi\sim1}
$$

が、長波長外場をよく追従する領域と、短波長変調を平均化してしまう領域の境目になる。

この意味で、$q$ を走査して $\chi(q)$ の幅を測ることは、実空間の相関長 $\xi$ を逆空間から測っていることに対応する。

#### $q\xi\gg1$：相関領域の内部で外場が相殺される

波長が相関長より短いと、一つの相関領域の中で外場は何度も向きを変える。

$$
\boxed{q\xi\gg1}
$$

では、相関によって一緒に動こうとするスピン群に対し、外場は場所ごとに異なる向きを要求する。そのため領域全体としては応答が相殺される。

Lorentzian近似では

$$
\chi(q)\sim\frac{1}{q^2\xi}
\qquad(q\xi\gg1)
$$

となり、短波長成分への応答は強く抑制される。

したがって相関長は

$$
\boxed{
\xi=\text{系が協調して応答できる代表的な空間スケール}
}
$$

と読むことができる。

### 7.6 同じ空間変調外場でもIsingとXYでは温度依存が違う

ここでIsingとXYの違いが再び効いてくる。低温で

$$
\xi_{\rm I}
\simeq\frac12\exp\left(\frac{2J}{k_{\mathrm B}T}\right),
$$

一方

$$
\xi_{\rm XY}
\simeq\frac{2J}{k_{\mathrm B}T}
$$

である。

固定した波数 $q$ の外場を考えると、クロスオーバーは

$$
\boxed{q\xi(T)\sim1}
$$

で起こる。しかし $\xi(T)$ の伸び方が異なるため、同じ $q$ でもそのクロスオーバー温度はIsingとXYで大きく異なる。

Isingでは相関長がactivatedに伸びるため、低温化によって急激に $q\xi\gg1$ 側へ入る。一方XYでは $\xi\propto1/T$ なので、クロスオーバーはより緩やかである。

ここで重要なのは、低温ほどすべての波数に強く応答するわけではないことである。低温化で $\xi$ が伸びると、一様あるいは長波長外場には強く応答する一方、固定された短波長外場は相関領域の内部で平均化されやすくなる。

$$
\boxed{
\text{cooling}
\Longrightarrow
\xi\uparrow
\Longrightarrow
\begin{cases}
\text{long wavelength: collective response grows},\\
\text{short wavelength: spatial cancellation becomes important}.
\end{cases}
}
$$

したがって空間変調外場は、単に磁化を作るための外場ではなく、相関長とその温度依存を波数空間で読み出すprobeである。

## 8. 外場を入れたときに見える共通構造と違い

零外場ではIsingもXYも相対変数が自然だったが、外場は絶対方向を指定するため、その単純さを壊す。この点は共通している。

一方、壊れ方には違いがある。Isingではdomain wallの独立性が失われ、XYでは角度差の独立性に加えてFourier sectorの混合が起こる。

それでも微小外場に限れば、応答は零外場相関から決まり、$\chi(q)$ の波数依存は相関長によって支配される。したがって

$$
\boxed{
\text{zero-field correlation}
\Longrightarrow
\text{finite-}q\text{ susceptibility}
\Longrightarrow
\text{spatial filtering by }q\xi
}
$$

という共通構造がある。

IsingとXYの違いは、このフィルタの基本構造ではなく、フィルタ幅を決める $\xi(T)$ がどの機構で生成されるかにある。

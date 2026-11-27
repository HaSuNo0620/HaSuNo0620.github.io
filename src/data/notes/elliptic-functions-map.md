---
title: "円から楕円関数へ — Gauss・Jacobi・Weierstrass"
summary: "円と楕円の弧長からJacobi関数を構成し、Gaussのレムニスケートと算術幾何平均、Weierstrassの周期格子を経て、三つの形式を統一する。"
publishedAt: 2026-09-09T18:30:00+09:00
updatedAt: 2026-11-28
area: "Mathematics"
field: mathematics
kind: theory
topics: ["elliptic functions", "special functions", "complex analysis"]
status: growing
---

円では角度と弧長が比例する。楕円ではこの関係が失われ、弧長を求めるだけでも初等関数では表せない積分が現れる。円の三角関数に相当するものを楕円について構成できるだろうか。

この問いから出発し、Jacobi、Gauss、Weierstrassの三つの構成を順に考える。最初から三者の同値性を仮定せず、それぞれが何を解決するために導入されるかを明らかにした後で接続する。

## 1. 円から楕円へ

半径 $a$ の円を $(x,y)=(a\sin\phi,a\cos\phi)$ と表すと、弧長要素は $ds=a\,d\phi$ となる。したがって弧長を半径で割った量は角度そのものである。

これに対し、長半径 $a$、短半径 $b$ の楕円を

$$
x=a\sin\phi,\qquad y=b\cos\phi,\qquad k^2=1-b^2/a^2
$$

と書けば、

$$
ds=a\sqrt{1-k^2\sin^2\phi}\,d\phi.
$$

円と異なり、媒介変数 $\phi$ の等間隔の変化は等しい弧長を与えない。原点からの弧長は第二種楕円積分

$$
s=aE(\phi,k),\qquad E(\phi,k)=\int_0^\phi\sqrt{1-k^2\sin^2 t}\,dt
$$

で表される。ここで円からのずれを担う因子を $D(\phi)=\sqrt{1-k^2\sin^2\phi}$ と書く。

## 2. Jacobiの構成：角度を取り直す

楕円の弧長そのものを逆にする代わりに、$D$ を使って角度を再パラメータ化する。目的は正弦・余弦に対応する関数と $D$ が、微分によって閉じた系をなすようにすることである。

新変数 $u$ を $d\phi/du=D(\phi)$、$u(0)=0$ によって定めると、

$$
u=F(\phi,k)=\int_0^\phi\frac{dt}{\sqrt{1-k^2\sin^2 t}}
$$

を得る。これが第一種楕円積分である。$u$ は楕円の幾何学的弧長ではない。逆関数 $\phi=\operatorname{am}(u,k)$ を振幅関数と呼び、

$$
\operatorname{sn}u=\sin\phi,\quad
\operatorname{cn}u=\cos\phi,\quad
\operatorname{dn}u=D(\phi)
$$

と定義する。以下では母数 $k$ を適宜省略する。

二つの代数関係

$$
\operatorname{sn}^2u+\operatorname{cn}^2u=1,\qquad
k^2\operatorname{sn}^2u+\operatorname{dn}^2u=1
$$

に加えて、連鎖律から

$$
\begin{aligned}
\operatorname{sn}'&=\operatorname{cn}\operatorname{dn},\\
\operatorname{cn}'&=-\operatorname{sn}\operatorname{dn},\\
\operatorname{dn}'&=-k^2\operatorname{sn}\operatorname{cn}
\end{aligned}
$$

が得られる。三角関数の二関数系に第三の関数が加わる理由は、楕円に固有の因子 $D$ も微分系に取り込むためである。

特に

$$
(\operatorname{sn}')^2=(1-\operatorname{sn}^2)(1-k^2\operatorname{sn}^2).
$$

この式を変数分離しても第一種楕円積分に戻る。一方、第二種楕円積分は

$$
E(\operatorname{am}u,k)=\int_0^u\operatorname{dn}^2v\,dv
$$

となる。第一種は新しい変数を定め、第二種はその変数を使って幾何学的弧長を表す。

第三種楕円積分はさらに有理因子を含む：

$$
\Pi(n;\phi,k)=\int_0^\phi
\frac{dt}{(1-n\sin^2t)\sqrt{1-k^2\sin^2t}}.
$$

以下の関数構成では主として第一種を使う。

## 3. 周期と加法定理

$0<k<1$ とし、完全第一種楕円積分を $K(k)=F(\pi/2,k)$ とする。角度 $\phi$ が $2\pi$ 増えると $u$ は $4K$ 増えるので、$\operatorname{sn}$ と $\operatorname{cn}$ の実基本周期は $4K$、$\operatorname{dn}$ の実基本周期は $2K$ である。

三角関数との類似は周期だけではない。例えば正弦の加法定理に対応する式は

$$
\operatorname{sn}(u+v)=
\frac{\operatorname{sn}u\operatorname{cn}v\operatorname{dn}v+
\operatorname{sn}v\operatorname{cn}u\operatorname{dn}u}
{1-k^2\operatorname{sn}^2u\operatorname{sn}^2v}.
$$

余弦と第三の関数にも対応する式がある：

$$
\begin{aligned}
\operatorname{cn}(u+v)&=
\frac{\operatorname{cn}u\operatorname{cn}v-
\operatorname{sn}u\operatorname{sn}v\operatorname{dn}u\operatorname{dn}v}
{1-k^2\operatorname{sn}^2u\operatorname{sn}^2v},\\
\operatorname{dn}(u+v)&=
\frac{\operatorname{dn}u\operatorname{dn}v-
k^2\operatorname{sn}u\operatorname{sn}v\operatorname{cn}u\operatorname{cn}v}
{1-k^2\operatorname{sn}^2u\operatorname{sn}^2v}.
\end{aligned}
$$

右辺の三関数が $u$ に関して上の微分系を満たし、$u=0$ で左辺と同じ初期値を持つことを確かめれば、局所解の一意性から導ける。解析接続によって成立範囲が拡張される。$k=0$ では通常の三角関数の加法定理に戻る。

## 4. Gaussの構成：レムニスケート

楕円とは異なる曲線からも、同じ種類の積分が現れる。Bernoulliのレムニスケートを極座標で $r^2=\cos 2\theta$ と書く（長さは最大半径で無次元化する）。一つの枝で微分すると

$$
\left(\frac{d\theta}{dr}\right)^2=\frac{r^2}{1-r^4}.
$$

極座標の弧長公式 $ds^2=dr^2+r^2d\theta^2$ より、原点から最大半径へ向かう枝では

$$
s=\int_0^r\frac{dt}{\sqrt{1-t^4}}.
$$

ここでは弧長の逆関数を直接取ることができる。これをレムニスケート正弦 $\operatorname{sl}(s)$ と呼ぶ。原点近傍で

$$
(\operatorname{sl}')^2=1-\operatorname{sl}^4,\qquad
\operatorname{sl}(0)=0,\quad \operatorname{sl}'(0)=1
$$

を満たす。$\ell=\int_0^1 dt/\sqrt{1-t^4}$ と置けば実周期は $4\ell$ である。レムニスケート余弦を $\operatorname{cl}(u)=\operatorname{sl}(\ell-u)$ と定めると、

$$
\operatorname{cl}^2u=\frac{1-\operatorname{sl}^2u}{1+\operatorname{sl}^2u}.
$$

Jacobiの構成では楕円の弧長から別の変数を導入したが、Gaussの構成ではレムニスケートの弧長そのものが新しい関数の引数となる。

## 5. 算術幾何平均とLanden変換

完全楕円積分はどのように計算できるのか。正数 $a,b$ に対し

$$
I(a,b)=\int_0^{\pi/2}\frac{d\theta}{\sqrt{a^2\cos^2\theta+b^2\sin^2\theta}}
$$

を考える。Landen変換による積分の不変性は

$$
I(a,b)=I\left(\frac{a+b}{2},\sqrt{ab}\right)
$$

である。この恒等式は、積分を $\int_0^\infty dx/\sqrt{(x^2+a^2)(x^2+b^2)}$ と表し、$t=x-ab/x$ と置換すると得られる。実際、分母は $x\sqrt{t^2+(a+b)^2}$、$dx/x=dt/\sqrt{t^2+4ab}$ となり、偶対称性と $t=2y$ の置換で右辺に一致する。

算術平均と幾何平均を反復する：

$$
a_{j+1}=\frac{a_j+b_j}{2},\qquad b_{j+1}=\sqrt{a_jb_j}.
$$

両列は共通の極限 $M(a,b)$（算術幾何平均、AGM）に収束する。積分の不変性から

$$
I(a,b)=I(M,M)=\frac{\pi}{2M(a,b)}
$$

となる。補母数 $k'=\sqrt{1-k^2}$ を使えば

$$
K(k)=I(1,k')=\frac{\pi}{2M(1,k')}.
$$

また母数を $k_1=(1-k')/(1+k')$ と置くと

$$
K(k)=\frac{2}{1+k'}K(k_1).
$$

これは降下型Landen変換である。$k$ が小さくなると $k_1\sim k^2/4$ となるため、反復によって急速に三角関数の極限に近づく。積分を保存しながら母数を変えることが、高速計算を可能にする。

## 6. Weierstrassの構成：複素平面の周期格子

ここでは積分の逆関数から出発せず、周期性そのものを指定する。実線形独立な複素数 $\omega_1,\omega_2$ により

$$
\Lambda=\mathbb Z\omega_1+\mathbb Z\omega_2
$$

を定める。$\Lambda$ の平行移動で不変な有理型関数を楕円関数と呼ぶ。基本平行四辺形の対辺を同一視した空間は複素トーラス $\mathbb C/\Lambda$ である。

非定数の楕円関数は極を持たなければならない。極がなければ基本領域上で有界であり、周期性から複素平面全体で有界となるため、Liouvilleの定理により定数になる。また基本領域内の留数の和は、対辺の積分が相殺するためゼロである。従って単純極ただ一つでは構成できない。

最も簡単な候補は各格子点に二位の極を持つ関数である。ただし単純な格子和は絶対収束しないため、定数項を差し引く：

$$
\wp(z)=\frac1{z^2}+
\sum_{\omega\in\Lambda\setminus\{0\}}
\left[\frac1{(z-\omega)^2}-\frac1{\omega^2}\right].
$$

差は大きな $|\omega|$ に対し $O(|\omega|^{-3})$ であり、二次元格子上で局所一様に絶対収束する。$\wp$ は偶関数である。微分した級数は絶対収束し、添字の移動から $\wp'$ の周期性が従う。したがって基本周期だけずらした $\wp$ の差は定数だが、偶性を用いればその定数もゼロと分かる。

## 7. 格子から三次曲線が生まれる

原点付近で格子和を展開すると、

$$
\wp(z)=z^{-2}+\frac{g_2}{20}z^2+\frac{g_3}{28}z^4+O(z^6),
$$

$$
g_2=60\sum_{\omega\ne0}\omega^{-4},\qquad
g_3=140\sum_{\omega\ne0}\omega^{-6}.
$$

$\wp$ と $\wp'$ の極の次数はそれぞれ2と3なので、$(\wp')^2$ と $\wp^3$ はともに6位の極を持つ。主要部を相殺する組合せを順に選ぶと、

$$
H=(\wp')^2-4\wp^3+g_2\wp+g_3
$$

には極がなく、原点での極限もゼロになる。正則な楕円関数は定数であることから

$$
(\wp')^2=4\wp^3-g_2\wp-g_3.
$$

こうして周期格子から三次曲線

$$
y^2=4x^3-g_2x-g_3
$$

が現れる。格子に由来する不変量では判別式 $g_2^3-27g_3^2$ はゼロでない。逆に非特異な複素三次曲線は、無限遠点を加えると適切な格子の複素トーラスとして一様化できる。写像は $z\mapsto(\wp(z),\wp'(z))$ であり、格子点は無限遠点に対応する。

## 8. 三つの構成を接続する

### GaussとJacobi

$k=1/\sqrt2$ のJacobi関数を用いて

$$
r(u)=\frac{1}{\sqrt2}
\frac{\operatorname{sn}(\sqrt2 u,k)}{\operatorname{dn}(\sqrt2 u,k)}
$$

と置く。Jacobiの微分系と代数関係を使うと $(r')^2=1-r^4$、$r(0)=0$、$r'(0)=1$ が得られる。したがって

$$
\operatorname{sl}(u)=\frac{\operatorname{sn}(\sqrt2 u,1/\sqrt2)}
{\sqrt2\,\operatorname{dn}(\sqrt2 u,1/\sqrt2)}.
$$

同じ微分方程式と初期条件を満たすという事実が、二つの構成を結びつける。特に $\ell=K(1/\sqrt2)/\sqrt2$ である。

### JacobiとWeierstrass

三次式が実根 $e_1>e_2>e_3$ を持つ場合を考える。$A=e_1-e_3$、$k^2=(e_2-e_3)/A$ と置く。

$$
x=e_3+\frac{A}{s^2}
$$

を $(dx/dz)^2=4(x-e_1)(x-e_2)(x-e_3)$ に代入すれば、

$$
\left(\frac{ds}{dz}\right)^2=A(1-s^2)(1-k^2s^2).
$$

原点で $s\sim\sqrt A z$ となる枝を取ると、

$$
\wp(z)=e_3+
\frac{A}{\operatorname{sn}^2(\sqrt A z,k)}.
$$

四次式と三次式は別々の問題ではなく、変数変換によって結びつく。一般の複素根の場合は根の選択と平方根の枝を指定する必要がある。

Gaussの四次式についても $x=1/\operatorname{sl}^2u$ と置けば

$$
(x')^2=4x^3-4x,
$$

したがって $x=\wp(u;4,0)$ となる。これは正方形型の周期格子に対応する。

### 複素周期と積分

Jacobi関数を複素変数へ解析接続すると、$\operatorname{sn}$ の基本周期は $4K$ と $2iK'$（$K'=K(k')$）となる。$\operatorname{sn}^2$ の周期格子は $2K$ と $2iK'$ で生成され、上の変換に対応するWeierstrass関数の格子を与える。関数を二乗すると周期格子が変わることに注意したい。

代数曲線上の微分 $dx/y$ を積分すると局所的に複素変数 $z$ が得られ、その積分の閉路に沿う値が周期を与える。逆に $z$ から曲線上の点を復元するのが楕円関数である。こうして積分、二重周期性、代数曲線という三つの記述がつながる。

## 9. 退化極限と非線形振動

$k\to0$ では $K\to\pi/2$、$K'\to\infty$ となり、Jacobi関数は三角関数へ退化する。$k\to1$ では $K\to\infty$ となり、固定した実引数で

$$
\operatorname{sn}u\to\tanh u,\qquad
\operatorname{cn}u,\operatorname{dn}u\to\operatorname{sech}u.
$$

この極限は周期格子の一方向が無限に伸びることに対応する。

応用として単振り子 $\ddot\theta+\omega_0^2\sin\theta=0$ を考える。最大振幅 $\theta_{\max}$ に対して $k=\sin(\theta_{\max}/2)$ とすると、エネルギー保存則は

$$
\dot\theta^2=4\omega_0^2[k^2-\sin^2(\theta/2)].
$$

$x=\sin(\theta/2)/k$ と置けば

$$
\dot x^2=\omega_0^2(1-x^2)(1-k^2x^2)
$$

となる。これは既に導いたJacobi関数の微分方程式である。$\theta=0$ を正の速度で通過する時刻を原点に選べば

$$
\theta(t)=2\arcsin[k\operatorname{sn}(\omega_0t,k)],
\qquad T=\frac{4K(k)}{\omega_0}.
$$

![振り子の最大振幅と周期](/figures/mathematics/pendulum-period.svg)

*完全第一種楕円積分による振り子の周期。小振幅で調和振動の周期に戻り、分離軌道に近づくと発散する。*

## 参考文献

- [NIST Digital Library of Mathematical Functions, Chapter 19: Elliptic Integrals](https://dlmf.nist.gov/19)
- [Chapter 22: Jacobian Elliptic Functions](https://dlmf.nist.gov/22)
- [Chapter 23: Weierstrass Elliptic and Modular Functions](https://dlmf.nist.gov/23)
- E. T. Whittaker and G. N. Watson, *A Course of Modern Analysis*.

---
title: "円から楕円関数へ — 楕円積分の幾何学"
summary: "円と楕円の弧長からJacobi関数を構成し、Gaussのレムニスケート、算術幾何平均と非線形振動へ進む。"
publishedAt: 2026-09-09T18:30:00+09:00
updatedAt: 2026-11-28
area: "Mathematics"
field: mathematics
kind: theory
topics: ["elliptic functions", "special functions", "complex analysis"]
status: growing
---

円では角度と弧長が比例する。楕円ではこの関係が失われ、弧長を求めるだけでも初等関数では表せない積分が現れる。円の三角関数に相当するものを楕円について構成できるだろうか。

この問いから出発し、楕円とレムニスケートという二つの曲線からJacobiとGaussの関数を構成する。実変数の積分と幾何学を主題とし、複素周期格子との接続は別稿に譲る。

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

円と異なり、媒介変数 $\phi$ の等間隔の変化は等しい弧長を与えない。媒介角 $\phi=0$ の点からの弧長は第二種楕円積分

$$
s=aE(\phi,k),\qquad E(\phi,k)=\int_0^\phi\sqrt{1-k^2\sin^2 t}\,dt
$$

で表される。ここで円からのずれを担う因子を $D(\phi)=\sqrt{1-k^2\sin^2\phi}$ と書く。

![円と楕円における等しい媒介角の間隔](/figures/mathematics/ellipse-arc.svg)

*同じ媒介角の増分でも、楕円では弧長が位置によって異なる。青い弧は等しい角度幅を示す。*

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

![レムニスケートの半径と弧長](/figures/mathematics/lemniscate-arc.svg)

*レムニスケートの一枝に沿う弧長（青）と原点からの半径（緑の破線）。曲線は本文の極方程式から生成した。*

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

## 6. 応用：非線形振動

単振り子 $\ddot\theta+\omega_0^2\sin\theta=0$ を考える。最大振幅 $\theta_{\max}$ に対して $k=\sin(\theta_{\max}/2)$ とすると、エネルギー保存則は

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

## 7. 複素関数への接続

ここまで実変数の幾何学と積分から関数を構成した。これらを複素変数へ拡張すると、実周期とは独立なもう一つの周期が現れる。周期格子から直接関数を構成する方法は [因数分解から楕円関数へ](./elliptic-factorization) で、二つの構成の対応と退化極限は [楕円関数の統一](./elliptic-unification) で扱う。

## 参考文献

- [NIST Digital Library of Mathematical Functions, Chapter 19: Elliptic Integrals](https://dlmf.nist.gov/19)
- [Chapter 22: Jacobian Elliptic Functions](https://dlmf.nist.gov/22)
- E. T. Whittaker and G. N. Watson, *A Course of Modern Analysis*.

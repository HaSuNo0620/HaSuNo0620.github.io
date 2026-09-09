---
title: "1次元イジング模型の厳密解 (1) — 転送行列法"
summary: "周期境界条件の1次元イジング模型を転送行列で書き、固有値から熱力学極限の自由エネルギーを得る。"
publishedAt: 2025-05-27T21:25:00+09:00
area: "Physics"
topics: ["statistical mechanics", "Ising model", "linear algebra"]
status: growing
---

## モデルの定義

一次元イジング模型（鎖長 $N$）のハミルトニアンを

$$
H = -J \sum_{i=1}^{N} s_i s_{i+1} - h \sum_{i=1}^{N} s_i,
$$

とする。ここで

- $s_i=\pm1$ は各格子点のスピン、
- $J$ は隣接スピン間の相互作用、
- $h$ は外部磁場、
- $s_{N+1}=s_1$ として周期境界条件を課す。

## 分配関数

$\beta = 1/(k_B T)$ とすると、分配関数は

$$
Z = \sum_{\{s_i=\pm1\}} \exp\left[
\beta J \sum_{i=1}^{N} s_i s_{i+1}
+ \beta h \sum_{i=1}^{N} s_i
\right]
$$

である。この式は局所的な因子の積へ分解でき、転送行列法で扱える。

## 転送行列

$s,s'\in\{+1,-1\}$ に対し

$$
T_{s,s'} = \exp\left[\beta Jss' + \frac{\beta h}{2}(s+s')\right]
$$

と定義する。$s=+1,-1$ の順に並べれば

$$
T =
\begin{pmatrix}
e^{\beta J+\beta h} & e^{-\beta J} \\
e^{-\beta J} & e^{\beta J-\beta h}
\end{pmatrix}.
$$

周期境界条件によって

$$
Z = \operatorname{Tr}(T^N)
$$

となる。

## 固有値による評価

$T$ の固有値を $\lambda_+,\lambda_-$ とすると

$$
Z = \lambda_+^N + \lambda_-^N,
$$

かつ

$$
\lambda_{\pm}
= e^{\beta J}
\left[
\cosh(\beta h)
\pm
\sqrt{\sinh^2(\beta h)+e^{-4\beta J}}
\right].
$$

## 熱力学極限

$N\to\infty$ では最大固有値 $\lambda_+$ が支配的なので、一サイトあたりの自由エネルギーは

$$
f
= -\frac{1}{\beta}
\lim_{N\to\infty}\frac{1}{N}\log Z
= -\frac{1}{\beta}\log\lambda_+.
$$

同じ模型を開境界条件から再帰的に構成する見方は、[帰納法のノート](/notes/ising-recursion/)に続きます。

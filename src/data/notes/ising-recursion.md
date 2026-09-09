---
title: "1次元イジング模型の厳密解 (2) — 再帰的構成"
summary: "開境界条件で最後のスピンを固定した部分分配関数を導入し、分配関数を再帰的に構成する。"
publishedAt: 2025-05-27T21:30:00+09:00
area: "Physics"
topics: ["statistical mechanics", "Ising model", "recursion"]
status: growing
---

一次元イジング模型を、今度は周期境界条件ではなく **開境界条件** のもとで考える。分配関数 $Z_N$ を、$N-1$ スピン系から逐次的に構成する。

## モデルとハミルトニアン

$$
H = -J \sum_{i=1}^{N-1} s_i s_{i+1} - h \sum_{i=1}^{N} s_i.
$$

分配関数は

$$
Z_N = \sum_{\{s_i=\pm1\}}
\exp\left[
\beta J \sum_{i=1}^{N-1}s_is_{i+1}
+ \beta h \sum_{i=1}^{N}s_i
\right].
$$

## 最後のスピンで分類する

最後のスピンを固定した部分分配関数を

- $Z_N^{(+)}$: $s_N=+1$ に固定、
- $Z_N^{(-)}$: $s_N=-1$ に固定

と定義する。このとき

$$
\begin{aligned}
Z_N^{(+)}
&=e^{\beta h}
\left(
Z_{N-1}^{(+)}e^{\beta J}
+Z_{N-1}^{(-)}e^{-\beta J}
\right),\\
Z_N^{(-)}
&=e^{-\beta h}
\left(
Z_{N-1}^{(+)}e^{-\beta J}
+Z_{N-1}^{(-)}e^{\beta J}
\right).
\end{aligned}
$$

したがって、初期条件から任意の $N$ へ再帰的に進める。

## 初期条件

$N=1$ では

$$
Z_1^{(+)}=e^{\beta h},\qquad
Z_1^{(-)}=e^{-\beta h},
$$

ゆえに

$$
Z_1 = Z_1^{(+)}+Z_1^{(-)} = 2\cosh(\beta h).
$$

一般に

$$
Z_N = Z_N^{(+)}+Z_N^{(-)}.
$$

## 行列形式

再帰関係は

$$
\begin{pmatrix}
Z_N^{(+)}\\
Z_N^{(-)}
\end{pmatrix}
=
\begin{pmatrix}
e^{\beta h+\beta J} & e^{\beta h-\beta J}\\
e^{-\beta h-\beta J} & e^{-\beta h+\beta J}
\end{pmatrix}
\begin{pmatrix}
Z_{N-1}^{(+)}\\
Z_{N-1}^{(-)}
\end{pmatrix}
$$

と書ける。これは転送行列法と同じ線形代数構造を持つ。ただし、ここでは「系へスピンを一つ付け加える」という再帰的な構築から自然に行列が現れている。

## 見方の違い

開境界の有限系では、この再帰形式は逐次計算に直接使いやすい。一方、周期境界条件や熱力学極限では、固有値を直接扱う[転送行列の見方](/notes/ising-transfer-matrix/)がより簡潔である。

# Math Style v1.1

HaSuNo0620.github.io の本文・キャプション・図で用いる数式表記の共通ルール。目的は、数式を強調しすぎず本文へ自然に埋め込みつつ、物理量・条件・関係式を通常文と視覚的に区別することである。

## 1. Inline math を標準にする

本文中に現れる変数、物理量、添字付き記号、短い条件、短い関係式は原則として inline math `$...$` で書く。

良い例：

- 相互作用範囲 $R=1$ では、相関長 $\xi$ は有限である。
- 強磁性 $J>0$ では $\chi(q)$ は $q=0$ で最大になる。
- 低温条件 $K\gg1$ では $p_{\mathrm{dw}}\simeq e^{-2K}$ である。

避ける例：

- `q=0` のように code span で数式を書く。
- β, χ, ξ のような物理量を通常の Unicode 文字として本文へ直接書く。
- `q\xi\ll1` のような短い条件だけを独立 display にして本文を分断する。

## 2. Display math を使う場合

`$$...$$` は次の場合に優先する。

- その節の中心となる式
- 複数行の導出
- 行列・総和・積分など、inline では読みにくい式
- 後の議論で繰り返し参照する式
- `\boxed{...}` で結果として強調する価値がある式

単一記号、短い条件、短い代入式だけを display にしない。たとえば $q\xi\ll1$ と $q\xi\gg1$ は文章の一部として inline に置く。

## 3. 本文と数式の役割を分ける

数式は関係を示し、文章は物理的意味を説明する。同じ内容を「式を置いた直後にその式をそのまま読み上げる」形で重複させない。

短い定義は文章へ統合してよい。たとえば「$t\equiv\tanh K$ とおく」のように書き、定義だけの display block は作らない。

## 4. LaTeX の細則

- 物理量・変数は通常の数式イタリックを使う：$J$, $T$, $q$, $\xi$。
- 説明的な添字は roman にする：$p_{\mathrm{dw}}$, $F_{\mathrm{visc}}$。
- 演算子は `\operatorname{}` または標準コマンドを使う：$\operatorname{Tr}$, $\ln$, $\cos$。
- 単位や語としてのラベルは `\mathrm{}` を使う。
- 数字・演算子・括弧まで手動で italic にしない。通常の TeX の math class に任せる。
- 日本語の句読点は原則として数式の外側に置く。

## 5. Markdown / MathJax の処理順

このサイトでは `remark-math` を使い、Markdown が通常文として解釈する前に `$...$` と `$$...$$` を math node として保護する。その後 `rehype-mathjax/browser` を介して既存の MathJax に渡す。

この構成により、行列や `aligned` で使う TeX の行区切り `\\` が CommonMark の backslash escape として潰れない。著者側では通常の LaTeX と同じ書き方を使う。

### 行列

```text
$$
\begin{pmatrix}
a & b\\
c & d
\end{pmatrix}
$$
```

### 複数行の式

```text
$$
\begin{aligned}
A&=B\\
 &=C.
\end{aligned}
$$
```

Markdown 対策のために `\\` をさらに二重化するような特殊記法は使わない。

## 6. Setext heading との衝突を避ける

math node として保護されるため以前より安全だが、可読性のため display math 内で `=` だけの行は作らない。

避ける：

```text
$$
A
=
B
$$
```

使う：

```text
$$
A=B
$$
```

## 7. Captions

図キャプション中の物理量も本文と同じく inline math を使う。たとえば「$q=0$ 周辺に応答が集中する」と書き、code span や raw Unicode で代用しない。

## 8. Headings

見出しに物理量を含める場合も `$R=1$`, `$q\xi$` のように inline math を使う。ただし見出し全体を数式にしない。

## 9. Figure labels

図中の変数・式は本文の数式と同じ視覚言語にする。ただし SVG を `<img>` として読み込む場合 MathJax は SVG 内部を組版しないので、Figure Style 側で役割を明示的に分ける。

- variable identifier: italic
- number / operator / punctuation / unit / prose: upright

「数式フォントを使う」ことと「全体を斜体にする」ことは同義ではない。詳細は [`docs/figure-style.md`](figure-style.md) を参照する。

## 10. Pre-publish checklist

- [ ] 本文中の物理量・短い式が `$...$` になっている
- [ ] code span を数式代わりに使っていない
- [ ] 短い条件だけの不要な display math がない
- [ ] display math は中心式・導出・行列などに限定されている
- [ ] 行列・`aligned` の行区切りが通常の `\\` で書かれている
- [ ] display math 内に `=` 単独行がない
- [ ] 説明的添字が roman になっている
- [ ] caption と figure label の数式表記が本文と一致している

この文書を **Math Style v1.1** の基準とする。

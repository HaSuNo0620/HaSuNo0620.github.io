# Math Style v1

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
- 日本語の句読点は原則として数式の外側に置く。

## 5. Markdown / MathJax 安全規則

Markdown の Setext heading 誤認を避けるため、display math 内で `=` だけの行を作らない。

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

複数行なら `aligned` を使う。

```text
$$
\begin{aligned}
A&=B\\
 &=C.
\end{aligned}
$$
```

## 6. Captions

図キャプション中の物理量も本文と同じく inline math を使う。たとえば「$q=0$ 周辺に応答が集中する」と書き、code span や raw Unicode で代用しない。

## 7. Headings

見出しに物理量を含める場合も `$R=1$`, `$q\xi$` のように inline math を使う。ただし見出し全体を数式にしない。

## 8. Figure labels

図中の変数・式は本文の数式と同じ視覚言語にする。SVG を `<img>` として読み込む場合 MathJax は SVG 内部を組版しないため、変数・式ラベルには数式用 serif / italic font stack を使い、説明語は通常の sans-serif と分ける。

例：軸の $h/J$, $C(r)$, $\chi(q)/\chi(0)$ は math style、`exact`, `low-T asymptote` は text style とする。

## 9. Pre-publish checklist

- [ ] 本文中の物理量・短い式が `$...$` になっている
- [ ] code span を数式代わりに使っていない
- [ ] 短い条件だけの不要な display math がない
- [ ] display math は中心式・導出・行列などに限定されている
- [ ] display math 内に `=` 単独行がない
- [ ] 説明的添字が roman になっている
- [ ] caption と figure label の数式表記が本文と一致している

この文書を **Math Style v1** の基準とする。

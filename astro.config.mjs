import { defineConfig } from 'astro/config';
import remarkMath from 'remark-math';
import rehypeMathjaxBrowser from 'rehype-mathjax/browser';

export default defineConfig({
  site: 'https://HaSuNo0620.github.io',
  output: 'static',
  trailingSlash: 'always',
  markdown: {
    // Parse TeX before CommonMark can consume backslashes used by matrices,
    // aligned equations, and other multiline math environments.
    remarkPlugins: [remarkMath],
    // Keep the existing client-side MathJax renderer, but hand it protected
    // math nodes rather than already-mutated Markdown text.
    rehypePlugins: [rehypeMathjaxBrowser],
  },
});

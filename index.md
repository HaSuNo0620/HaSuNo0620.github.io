---
layout: default
title: Home
---

<section class="garden-hero">
  <div class="garden-hero-copy">
    <p class="site-kicker">HaSuNo0620 / somewhere on the web</p>
    <h1>気になったものを、<br>気になったまま置いておく。</h1>
    <p class="garden-lead">
      物理、数学、コード、作品について考えたこと。
      まとまったものも、まだ途中のものも、あとで拾い直せるように残しています。
    </p>
  </div>

  <aside class="now-note" aria-label="このサイトにあるもの">
    <p class="scribble-label">on this desk</p>
    <ul>
      <li>physics / math</li>
      <li>simulation / code</li>
      <li>anime / manga</li>
      <li>unfinished thoughts</li>
    </ul>
    <span class="now-note-mark" aria-hidden="true">↘</span>
  </aside>
</section>

<nav class="garden-paths" aria-label="サイトの入口">
  <a href="{{ '/notes/' | relative_url }}">
    <span class="path-no">01</span>
    <span class="path-main">Notes</span>
    <span class="path-sub">勉強、計算、実装、考察</span>
    <span class="path-arrow" aria-hidden="true">→</span>
  </a>
  <a href="{{ '/about/' | relative_url }}">
    <span class="path-no">02</span>
    <span class="path-main">About</span>
    <span class="path-sub">この場所と、いまの興味</span>
    <span class="path-arrow" aria-hidden="true">→</span>
  </a>
  <a href="https://github.com/HaSuNo0620">
    <span class="path-no">03</span>
    <span class="path-main">GitHub</span>
    <span class="path-sub">コードと制作物の置き場</span>
    <span class="path-arrow" aria-hidden="true">↗</span>
  </a>
</nav>

<section class="interest-strip" aria-label="興味の領域">
  <p class="scribble-label">things keep crossing</p>
  <div class="interest-line">
    <span>statistical mechanics</span>
    <i>×</i>
    <span>soft matter</span>
    <i>×</i>
    <span>mathematics</span>
    <i>×</i>
    <span>simulation</span>
    <i>×</i>
    <span>code</span>
    <i>×</i>
    <span>anime & manga</span>
  </div>
</section>

<section class="recent-notes garden-recent">
  <div class="section-heading-row">
    <div>
      <p class="scribble-label">recent fragments</p>
      <h2>最近の Notes</h2>
    </div>
    <a class="text-link" href="{{ '/notes/' | relative_url }}">archive →</a>
  </div>

  <div class="note-list-simple">
    {% for post in site.posts limit:4 %}
      <a class="note-row" href="{{ post.url | relative_url }}">
        <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%Y.%m.%d" }}</time>
        <span>
          <span class="note-row-title">{{ post.title | escape }}</span>
          {% if post.categories.size > 0 or post.tags.size > 0 %}
            <span class="note-row-meta">
              {% if post.categories.size > 0 %}{{ post.categories | join: " / " }}{% endif %}
              {% if post.categories.size > 0 and post.tags.size > 0 %} · {% endif %}
              {% if post.tags.size > 0 %}{{ post.tags | join: " / " }}{% endif %}
            </span>
          {% endif %}
        </span>
        <span class="note-arrow" aria-hidden="true">↗</span>
      </a>
    {% endfor %}
  </div>
</section>

<section class="site-note">
  <p class="scribble-label">note</p>
  <p>
    このサイトは完成させるものというより、使いながら少しずつ形を変えていく場所です。
    古いノートも、そのとき何を考えていたかの記録として残しています。
  </p>
</section>

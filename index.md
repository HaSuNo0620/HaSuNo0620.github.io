---
layout: default
title: Home
---

<section class="hero">
  <p class="eyebrow">HaSuNo0620 / personal notes & experiments</p>
  <h1>考えたこと、作ったもの、<br>途中のもの。</h1>
  <p class="hero-lead">
    物理や数学を考えたり、コードを書いたり、作品について考えたり。
    ここは、完成品だけでなく途中の思考も置いておくための個人的な場所です。
  </p>
  <div class="hero-actions">
    <a class="button button-primary" href="{{ '/notes/' | relative_url }}">Notes を読む</a>
    <a class="button button-ghost" href="{{ '/about/' | relative_url }}">About</a>
  </div>
</section>

<section class="home-grid" aria-label="このサイトについて">
  <article class="home-card">
    <span class="card-index">01</span>
    <h2>考える</h2>
    <p>物理、数学、統計力学、その周辺。理解したことだけでなく、考えている途中も残します。</p>
  </article>
  <article class="home-card">
    <span class="card-index">02</span>
    <h2>作る</h2>
    <p>コード、小さなツール、実験的なプロジェクト。完成度よりも、試したことを記録します。</p>
  </article>
  <article class="home-card">
    <span class="card-index">03</span>
    <h2>眺める</h2>
    <p>アニメや漫画をはじめ、気になったものを自分なりの視点で眺め直します。</p>
  </article>
</section>

<section class="recent-notes">
  <div class="section-heading-row">
    <div>
      <p class="eyebrow">Recent</p>
      <h2>最近の Notes</h2>
    </div>
    <a class="text-link" href="{{ '/notes/' | relative_url }}">すべて見る →</a>
  </div>

  <div class="note-list-simple">
    {% for post in site.posts limit:3 %}
      <a class="note-row" href="{{ post.url | relative_url }}">
        <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%Y.%m.%d" }}</time>
        <span class="note-row-title">{{ post.title | escape }}</span>
        <span class="note-arrow" aria-hidden="true">↗</span>
      </a>
    {% endfor %}
  </div>
</section>

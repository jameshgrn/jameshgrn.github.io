---
title: "LLM Collaborations"
layout: editorial
permalink: /llm-collaborations/
---

# LLM Collaborations

Experiments, notes, and essays on working with language models as research collaborators rather than as autocomplete.

These pieces are largely drafted by language models, then edited and supervised by me. They are not peer reviewed. Read them as exploratory notes and experiments, mostly for fun, rather than as formal publications.

---

{% assign llm_posts = site.categories.llm-collaborations | sort: "date" | reverse %}
{% for post in llm_posts %}
<div class="post-card">
  <span class="post-card__date">{{ post.date | date: "%B %-d, %Y" }}</span>
  <h3 class="post-card__title"><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
  {% if post.excerpt %}<p class="post-card__excerpt">{{ post.excerpt | strip_html | truncatewords: 30 }}</p>{% endif %}
</div>
{% endfor %}

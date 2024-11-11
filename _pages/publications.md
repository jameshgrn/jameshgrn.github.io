---
layout: single
title: "Publications & Academic Impact"
permalink: /publications/
author_profile: true
---

{% if site.data.scholar_metrics %}
## Impact Metrics
<div class="metrics-container">
  <div class="metric-box">
    <h3>{{ site.data.scholar_metrics.total_citations }}</h3>
    <p>Total Citations</p>
  </div>
  <div class="metric-box">
    <h3>{{ site.data.scholar_metrics.h_index }}</h3>
    <p>h-index</p>
  </div>
  <div class="metric-box">
    <h3>{{ site.data.scholar_metrics.i10_index }}</h3>
    <p>i10-index</p>
  </div>
</div>
{% endif %}

## Featured Publications

{% for post in site.publications reversed %}
  {% if post.venue contains 'Nature' or post.venue contains 'Science' or post.venue contains 'PNAS' %}
    <div class="publication-item featured">
      <div class="pub-image">
        {% if post.header.teaser %}
          <img src="{{ post.header.teaser }}" alt="{{ post.title }}">
        {% endif %}
      </div>
      <div class="pub-content">
        <h3><a href="{{ post.paperurl }}">{{ post.title }}</a></h3>
        <p class="pub-authors">{{ post.citation | split: '.' | first }}.</p>
        <p class="pub-venue"><i>{{ post.venue }}</i>, {{ post.date | date: "%Y" }}</p>
        {% if post.excerpt %}<p class="pub-excerpt">{{ post.excerpt }}</p>{% endif %}
        <div class="pub-links">
          {% if post.paperurl %}<a href="{{ post.paperurl }}" class="btn btn--primary">PDF</a>{% endif %}
          {% if post.code %}<a href="{{ post.code }}" class="btn btn--info">Code</a>{% endif %}
          {% if post.dataset %}<a href="{{ post.dataset }}" class="btn btn--info">Data</a>{% endif %}
        </div>
      </div>
    </div>
  {% endif %}
{% endfor %}

## All Publications

{% assign grouped_publications = site.publications | group_by_exp: "pub", "pub.date | date: '%Y'" | sort: "name" | reverse %}

{% for year in grouped_publications %}
### {{ year.name }}
  {% for post in year.items %}
    <div class="publication-item">
      <div class="pub-content">
        <h4><a href="{{ post.paperurl }}">{{ post.title }}</a></h4>
        <p class="pub-authors">{{ post.citation | split: '.' | first }}.</p>
        <p class="pub-venue"><i>{{ post.venue }}</i></p>
        <div class="pub-links">
          {% if post.paperurl %}<a href="{{ post.paperurl }}" class="btn btn--primary">PDF</a>{% endif %}
          {% if post.code %}<a href="{{ post.code }}" class="btn btn--info">Code</a>{% endif %}
          {% if post.dataset %}<a href="{{ post.dataset }}" class="btn btn--info">Data</a>{% endif %}
        </div>
      </div>
    </div>
  {% endfor %}
{% endfor %}

<div class="page__footer">
  <p><a href="{{ site.author.googlescholar }}">View all publications on Google Scholar</a></p>
</div>
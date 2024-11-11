---
layout: single
title: "Publications"
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

## Publications

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
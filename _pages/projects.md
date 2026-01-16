---
layout: editorial
title: "Projects"
permalink: /projects/
---

[home](/) / [publications](/#publications) / [cv](/pdf/Gearon_James_CV.pdf)

---

{% for project in site.projects %}
## {{ project.title }}

{{ project.content }}

---

{% endfor %}

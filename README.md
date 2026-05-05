# jameshgrn.github.io

Personal academic site for **James H. Gearon** — postdoc at UNC Chapel Hill's [Global Hydrology Lab](https://uncglobalhydrology.org/), studying fluvial sedimentology and geoinformatics.

Live site: <https://jameshgrn.github.io>

## Stack

- [Jekyll](https://jekyllrb.com/) static site generator
- Custom retrofuturistic editorial theme (forked from [Academic Pages](https://github.com/academicpages/academicpages.github.io), substantially rewritten)
- Hosted on GitHub Pages, built server-side from `master`

## Repo layout

```
index.md                  Homepage (bio, questions, publications list)
_pages/                   Standalone pages (CV, projects, etc.)
_publications/            Per-paper Markdown entries (collection)
_posts/                   Blog/notes posts
_data/                    Site data (navigation, etc.)
_includes/ _layouts/      Theme partials and layouts
_sass/ assets/            Styles and JS
images/ files/ pdf/       Static assets
_config.yml               Site-wide configuration
```

## Local development

Requires Ruby + Bundler + Node.

```bash
bundle install
bundle exec jekyll serve -l -H localhost
# open http://localhost:4000
```

For a one-off build (output goes to `_site/`, which is gitignored):

```bash
bundle exec jekyll build
```

### Docker

```bash
docker build -t jekyll-site .
docker run -p 4000:4000 --rm -v $(pwd):/usr/src/app jekyll-site
```

## Adding a publication

1. Add a Markdown file under `_publications/` following the `YYYY-venue-topic.md` pattern. See existing entries for the frontmatter schema (`title`, `date`, `venue`, `paperurl`, `citation`).
2. Add the corresponding `<li class="publication-item">` block to the publications list in `index.md`.
3. If the PDF is hosted locally, drop it in `files/publications/` using the `YYYY_Venue_LeadAuthor_topic.pdf` convention.

## Attribution

This site originated as a fork of the [Academic Pages](https://github.com/academicpages/academicpages.github.io) Jekyll template (itself derived from the [Minimal Mistakes](https://mmistakes.github.io/minimal-mistakes/) theme, © 2016 Michael Rose, MIT). Subsequent layout, styling, and content are © James H. Gearon. Template portions remain MIT-licensed — see `LICENSE`.

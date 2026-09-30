#!/usr/bin/env bash
# Pull the latest CI-built public CV (no phone number or students' current
# employers) from the private jamesgearon-cv-canonical repo
# into the site's pdf/ directory. Requires an authenticated `gh` CLI.
# Usage: scripts/update_cv.sh   (then review, commit, and push the site)
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

gh release download latest \
  --repo jameshgrn/jamesgearon-cv-canonical \
  --pattern JamesGearonCV_public.pdf \
  --output "${repo_root}/pdf/Gearon_James_CV.pdf" \
  --clobber

echo "Updated ${repo_root}/pdf/Gearon_James_CV.pdf"

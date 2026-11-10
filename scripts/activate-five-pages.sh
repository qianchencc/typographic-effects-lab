#!/usr/bin/env bash
# One-time administrator setup for the five repositories created on 2026-11-10.
# Requires an authenticated GitHub CLI session: gh auth login
# Does not use or print authentication tokens.
set -uo pipefail

OWNER="qianchencc"
REPOS=(lineform living-ascii umbra-roma typographic-effects-lab wind-motion)
FAILED=0

if ! command -v gh >/dev/null 2>&1; then
  echo "GitHub CLI is required: https://cli.github.com/" >&2
  exit 1
fi
if ! gh auth status >/dev/null 2>&1; then
  echo "Please authenticate first using: gh auth login" >&2
  exit 1
fi

for name in "${REPOS[@]}"; do
  base="repos/${OWNER}/${name}"
  url="https://${OWNER}.github.io/${name}/"
  echo "----- ${OWNER}/${name} -----"

  if gh api "${base}/pages" >/dev/null 2>&1; then
    if ! gh api --method PUT "${base}/pages" -f build_type=workflow >/dev/null; then
      echo "Could not configure Pages. Leaving this repository unchanged." >&2
      FAILED=$((FAILED + 1))
      continue
    fi
  elif ! gh api --method POST "${base}/pages" -f build_type=workflow >/dev/null; then
    echo "Could not enable Pages; private repositories may need an eligible GitHub plan." >&2
    FAILED=$((FAILED + 1))
    continue
  fi

  if gh api --method PATCH "${base}" -f "homepage=${url}" >/dev/null; then
    echo "Website: ${url}"
  else
    echo "Could not update the repository's About → Website field." >&2
    FAILED=$((FAILED + 1))
  fi

  if gh api --method POST "${base}/actions/workflows/pages.yml/dispatches" -f ref=main >/dev/null; then
    echo "Deployment workflow dispatched."
  else
    echo "Failed to dispatch Pages workflow; rerun it manually from Actions." >&2
    FAILED=$((FAILED + 1))
  fi
done

if ((FAILED > 0)); then
  echo "Completed with ${FAILED} action(s) needing manual attention." >&2
  exit 1
fi
echo "Pages configuration, repository Website links, and deployments requested for all five."

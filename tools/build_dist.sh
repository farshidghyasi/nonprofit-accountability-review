#!/usr/bin/env bash
# Rebuild everything in dist/ from the skill folder. Run from the repo root:
#   bash tools/build_dist.sh
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SKILL="$ROOT/skills/nonprofit-accountability-review"
DIST="$ROOT/dist"
mkdir -p "$DIST"
find "$SKILL" -name __pycache__ -type d -prune -exec rm -rf {} +

# 1. Skill zip for Claude.ai upload (folder name must match the skill name)
rm -f "$DIST/nonprofit-accountability-review.zip"
(cd "$ROOT/skills" && zip -qr "$DIST/nonprofit-accountability-review.zip" nonprofit-accountability-review)

# 2. Single-file knowledge pack for assistants that take one file or few files
PACK="$DIST/knowledge-pack.md"
{
  echo "# Nonprofit Accountability Review - knowledge pack"
  echo
  echo "All reference files of the skill in one document. Upload this as a knowledge/source file"
  echo "alongside the instructions in instructions/INSTRUCTIONS.md (works for any assistant)."
  for f in references/jurisdictions.md references/us-form-990-guide.md references/scoring-rubric.md \
           references/report-templates.md references/ethics-and-safety.md references/verification.md \
           templates/right-of-reply.md; do
    echo; echo "---"; echo; echo "<!-- file: $f -->"; echo
    cat "$SKILL/$f"
  done
  echo; echo "---"; echo; echo "<!-- file: templates/source-register.csv (column headers) -->"; echo
  echo '```csv'; cat "$SKILL/templates/source-register.csv"; echo '```'
} > "$PACK"

echo "Built:"; ls -l "$DIST"

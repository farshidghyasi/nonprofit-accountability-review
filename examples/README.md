# Examples

Everything here is **fictional**. The organisations, EIN and people do not exist.

- `sample_990/` - a minimal, made-up Form 990 e-file XML to try the parser:
  `python3 ../skills/nonprofit-accountability-review/scripts/parse_990_xml.py sample_990 --out out/`
- `sample_scores.csv` - a made-up scores sheet to try the scorer:
  `python3 ../skills/nonprofit-accountability-review/scripts/score.py sample_scores.csv --out scored.csv`

Expected scorer result: one tier one (45%), two tier three, and one "insufficient record to tier" (only three applicable tests).

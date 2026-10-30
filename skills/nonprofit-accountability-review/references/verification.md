# Independent verification

The person or agent who wrote the analysis must not be the only one checking it. In past runs of this method, a blind re-check found several material errors per report - a schedule wrongly called missing, a state misplaced, a share off by a factor of six, a sentence implying someone else's money belonged to the organisation. The headline barely moved; the credibility did.

## Protocol
1. **Extract claims.** List every factual statement in the draft as a numbered claim with its cited source. Remove scores, tiers, verdicts and interpretation so the checker is not anchored.
2. **Hand off blind.** Give the claim list (not the report) to a separate agent, a fresh chat, or a second person. Split by source type if useful: one checker re-derives US figures from the raw XML with its own code; another opens UK/European/Canadian/Australian records itself.
3. **Mark each claim:** CONFIRMED / PARTLY RIGHT (say what is right) / WRONG (give the correct fact and source) / UNVERIFIABLE (source unreachable or does not say).
4. **Apply corrections.** Fix the draft, re-run any score whose fact changed (`scripts/score.py`), and log every change with the claim number.
5. **Second check of High and Medium flags.** Every High or Medium finding goes to a checker that has not seen the scoring rationale. Apply its downgrades.
6. **Report the verification** in the output: how many claims, how many confirmed / corrected / removed, and what changed.

## Checker prompt (paste into a fresh session)

```
You are a fact-checker. Below is a numbered list of factual claims about a nonprofit, each with a cited source.
For every claim, open the source yourself (do not rely on memory or on the claim's wording) and mark it:
CONFIRMED, PARTLY RIGHT, WRONG, or UNVERIFIABLE.
For PARTLY RIGHT and WRONG, give the correct fact, the exact location (form, year, part, line or page), and the URL.
For figures, recompute them yourself. Do not judge whether the organisation did anything wrong; only check facts.
Return a table: # | verdict | correct fact (if any) | location | URL.

[paste claims]
```

## Reliability check for population studies
Draw a random sample of about 30 scored organisations (record the seed). A second rater scores them blind from the rulebook and the raw records only. Report agreement per test and tighten the wording of any test with poor agreement.

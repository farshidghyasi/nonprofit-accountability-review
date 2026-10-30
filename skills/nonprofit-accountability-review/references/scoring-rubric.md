# Scoring rubric: the ten tests

**What a score means.** A score counts the questions an organisation's own public record leaves open, under rules fixed before scoring. It is **not** a rating of quality, impact or honesty, and it is not evidence of wrongdoing. Small organisations score higher on some tests simply because they are small - always show scale beside the score.

## General rules
- Each test scores **0** (no concern on the available record), **1** (a gap or partial concern), **2** (a documented contradiction, concentration or absence), or **n/a** with one reason: *not required* (the law does not ask), *not available* (not reachable), *not assessed*.
- **Missing data is never scored** unless the law demonstrably required it for that jurisdiction, year and entity size.
- Run the **innocent-explanation protocol** before any 1 or 2: write the strongest innocent reading, test it, and record the result.
- Every score has a written basis, an evidence tag and a source link.
- Write your rulebook (this file plus any clarifications) **before** scoring. Any clarification during scoring becomes a dated amendment applied to everyone, including those already scored.

## The tests

| Code | Question | Scoring |
|---|---|---|
| **GEO** | Does the money go where donors are told? | Traceable share = spending the filing itself places in the stated area of benefit ÷ total expenses for the period. **0** if ≥ 50%, or appeals state where money goes and the filings match, or the organisation serves people in its home country (e.g. refugee or diaspora services) as it says. **1** if 20-50% while appeals describe work in that area. **2** if < 20% while the name, mission or appeals describe work there. **n/a** without geographic data. US: Schedule F amounts for the relevant region, plus spending Part III/Schedule O locates there. Say when a region covers several countries. |
| **SCHED** | Is the foreign-activity reporting complete and consistent? | US full-990 only (other countries: n/a unless an equivalent schedule is required). A part is missing only if its Part IV trigger is Yes. A region contradicting the programme the return itself describes counts (after the innocent reading). **0** none; **1** one year or one inconsistency; **2** two or more. |
| **INTERNAL** | Do the organisation's own numbers agree? | Restatement > 10% on amendment; assets − liabilities ≠ net assets; negative liabilities; register vs accounts contradictions; checklist answers contradicting other parts; annual report vs filing differences that fail the innocent reading. **1** one material item; **2** two or more, or an impossible return. |
| **GOV** | How concentrated is control? | Count: no conflict-of-interest policy; no whistleblower policy; no document-retention policy; founder holds 2+ officer roles; fewer than 5 independent voting members; return not provided to the board; no audit/review/compilation with expenses > $1m (or local equivalent); conflict disclosures routed to the founder. **0** = 0-1 items; **1** = 2-3; **2** = 4+. Outside the US use local items: fewer than 3 trustees/directors; register vs accounts trustee mismatch not explained by timing; required examination or audit missing. |
| **FAMILY** | Disclosed family and related-party ties | **0** none, or one disclosed relationship with no transaction. **1** family members hold 2+ posts, or a related-party transaction. **2** family hold 2+ officer posts AND a family member is paid or a related party transacts; or the filing shows a relationship that should have been disclosed and was not. **Shared surnames are never evidence.** |
| **RESERVES** | Unrestricted funds out of proportion? | (Net assets without donor restriction − (net fixed assets − secured debt on them)) ÷ latest full year's expenses. **0** ≤ 3 years; **1** > 3-5; **2** > 5. Subtract 1 if a published reserves policy explains the level. If only total net assets are known it is an upper bound - cap at 1. Under 3 months is reported as a solvency signal, not scored. Endowments and funds for a documented building are not "hoarding" - note them. |
| **UNNAMED** | Are recipients of grants identifiable? | **0** named (on the return or publicly), or spent through the organisation's own staff/offices. **1** unnamed with a stated reason (e.g. security), or unnamed but < 50% of expenses. **2** unnamed, no reason, > 50% of expenses. |
| **CLAIMS** | Are beneficiary numbers consistent? | After innocent readings: **0** consistent, or no claims. **1** figures differ, innocent reading untested. **2** > 2× apart for the same programme and period; or a metric marked "no longer tracked" still used in appeals; or an identical count filed 3+ consecutive years while programme spending changed by > 50%; or appeals for services with no evidence of delivery. |
| **PAY** | Is compensation out of line? | Highest-paid person's total pay vs a **peer benchmark you build and cite** (median top executive pay for organisations of similar revenue in the same country, from e-file data or a published compensation study) and as % of total expenses. **0** ≤ 1.25× benchmark and ≤ 15% of expenses; **1** 1.25-2× or 15-25%; **2** > 2× or > 25%, or unusual components (housing, travel stipends, gross-ups, large bonuses) with no comparability process disclosed. n/a where pay is not disclosed and not required. |
| **PUBLIC** | What is missing, and was it required? | **2** a legally required filing missing or > 60 days after the (extended) deadline, a revocation or removal from register, or a register fact contradicting the organisation's own account. **1** required items on time, nothing beyond the minimum. **0** on time plus voluntary disclosure (published audited accounts, annual report with financials, a recognised seal). If the law imposes no duty to publish, the maximum is 1. |

Always state lateness in days. Never write "on time" unless the filing date is on or before the due date.

## Score, tiers and placement
- **Score** = points ÷ (2 × tests applied), as a percentage.
- **Tier one** ≥ 40%; **tier two** 20-39%; **tier three** < 20%.
- **Fewer than five applicable tests → "insufficient record to tier".** Show what could be tested.
- Order within a tier by percentage, then scale, then name. **No organisation is moved by hand.**
- **Scale** beside the score (not part of it): A ≥ $10m raised in the period; B $1-10m; C < $1m (or local-currency equivalent, stated).
- **Placement rule P1:** an external formal finding (regulator inquiry, inspector-general audit, attorney-general action) whose final disposition is not public → listed beside tier one.
- **Placement rule P2:** named grantee of two or more institutional funders that publishes no financial statement of any kind → listed beside tier one, unscored.
- **No cross-jurisdiction league tables.** Show tiers within record type (US full 990; US 990-EZ/PF; UK accounts; Canadian T3010; Australian AIS; continental Europe).

`scripts/score.py` applies these rules from a CSV.

## Flags and severity
Every flag gets one category:
- **L** potential legal non-compliance - only after the requirement is confirmed for that jurisdiction, year and entity;
- **R** reconciliation question;
- **D** voluntary disclosure gap;
- **G** governance weakness;
- **N** withdrawn (kept on record with the reason).

Severity:
- **High:** a confirmed L, or an unreconciled amount > 10% of the period's expenses and ≥ $25,000.
- **Medium:** an R, or a material G.
- **Low:** otherwise.
Severity never rests on shared surnames, a founder not being a trustee, or reserves held for a documented purpose.

## Evidence chain
For each organisation rate four stages as Documented (independent) / Documented (filing) / Claimed (organisation only) / None found:
- **S1** money received
- **S2** money allocated or transferred
- **S3** activities delivered
- **S4** outcomes achieved

A tax return can evidence S1-S2 only. Audits by funders, regulator inspections and independent evaluations can evidence S3-S4.

Also record **coverage** (years of primary record actually read) and **confidence** (High / Moderate / Low).

## Register-only scoring
Where accounts cannot be read, score only from the regulator's structured data, and only on the tests it carries (e.g. Canada T3010 open data: GOV by director count, FAMILY by arm's-length flag, RESERVES capped at 1, PUBLIC by missing years; Australia AIS: GEO by overseas grants, INTERNAL by balance-sheet identity, GOV, FAMILY by related-party flag, PAY by KMP share, PUBLIC by lateness; England & Wales register: GOV by trustee count, PUBLIC by days late). Everything else is n/a - not assessed; confidence Low.

## Population studies (Mode B)
- Define inclusion and exclusion rules **before** the census, using objective criteria (cause, jurisdiction, legal form, period, role of founder/leader). Never use protected characteristics such as ethnicity or religion as search terms or criteria.
- Use whole-register routes (bulk files, area-of-operation filters, full-text search, funders' grantee lists), not only name searches. Record which route found each candidate and every in/out decision with its reason.
- Grade any attribute that defines the population (e.g. "founder based in country X") as Verified (a primary source states it) / Likely / Unverified / No. A name alone is never Verified.
- Score a **control group** chosen by rule (every census entity meeting the cause test but not the population-defining attribute) with the same code. Treat the comparison as descriptive.
- Report sensitivity: re-run key figures with each contestable rule changed, and have a second rater score a random sample blind (record the seed).
- Freeze the population before scoring; log every later change.

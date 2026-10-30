# Report structures

Every output starts with a short disclosure block:

> **How this was made.** AI-assisted research from public filings, independently re-checked against the sources on [date]. AI can make mistakes; the filings govern. **This is not an allegation of wrongdoing.** A red flag is a question the public record leaves open. Conflicts of interest: [author's ties, or "none"]. Corrections: [address]. Replies from the organisation will be published in full.

---

## Mode A - "[Organisation] under the microscope"

1. **Bottom line** - three to six sentences: what the record shows, the biggest open questions, what is done well, confidence level.
2. **Red-flag scorecard** - table: test · finding · score (0 green / 1 amber / 2 red / n/a) · source. Total and tier.
3. **Scope and method** - period, records read (by year), what could not be reached, rules used (link to the rubric).
4. **Organisation profile and legal status** - legal name(s), identifiers, legal form, registration and exemption status, related entities.
5. **Governance, board and related parties** - board size and independence, policies, audit, disclosed relationships and transactions.
6. **Founder / chief executive profile and linked entities** - public roles, other organisations and companies they control (from registers), no private life.
7. **Money in** - revenue by year and type; identifiable funders from funder-side records; donor-advised fund share.
8. **Money out** - expenses by function; grants; payments to subsidiaries and related parties; reserves; executive pay by component vs benchmark; cost per beneficiary (estimate).
9. **Where the money went** - spending the filing places in each country/region vs what donors are told; assessment (see below).
10. **Donation channels** - how money is solicited (own site, DAFs, crowdfunding, fiscal sponsors), and what each appeal promises.
11. **Programmes and reach** - every published reach figure, source and date; internal consistency; evaluations.
12. **Transparency benchmark** - what the law in that country requires vs what good practice (seals, audited accounts, annual report with financials) looks like, and where this organisation sits.
13. **Controversies** - attributed; state clearly what is proven, what is alleged, what is rumour or a harassment campaign.
14. **Testing the misuse hypothesis** - table of specific tests · evidence · Supported / Not supported / Unresolved.
15. **Right-of-reply questions** - numbered, tied to line items, with the organisation's contact address and reply status.
16. **Comparison** (optional) - same tests for peer organisations.
17. **Limitations** - what was not read and why; what could change the picture.
18. **Sources** - every document with a link, form/year/part/line where relevant.

**Assessment of "where the money went"** (for US full-990 filers it must match the GEO score):
- *Spent in the stated area, as stated* (≥ 50% traceable)
- *Spent mainly elsewhere, as stated* (e.g. services in the home country the organisation describes openly)
- *Partly traceable* (20-50%)
- *Stated for the area; under 20% traceable there*
- *Cannot be determined from the public record* (no split required or available - not a finding against the organisation)

---

## Mode B - Landscape / population working paper

- **Title page:** title, author, date and data cut-off; boxes for "How to read this paper", "Conflicts of interest", "Safety".
1. **Summary** - headline findings, each with confidence; what should happen next.
2. **Scope and population** - inclusion rule, grade table, counts, what the population is not, period.
3. **Method** - score meaning, evidence tags, innocent-explanation protocol, missing data, a table of what each jurisdiction requires by size, the ten tests, flags/severity/evidence chain, tiers and placement rules, amendments.
4. **The population at a glance** - funnel (screened → in scope → scored); record types; largest fundraisers; revenue by year (stacked).
5. **Findings across the population** - tests most often scored; heatmap; flags by category and severity; evidence chain; reserves; pay vs benchmark; governance vs a well-governed benchmark; control group.
6. **Was the money spent on its purpose and in the stated place?** - assessment counts by organisations and by money; "where the money went" stacked bars; landscape table of every member, largest first.
7. **Scoring matrix** by record type, largest first.
8. **Tier one entries** (plus P1/P2 placements) - full entries.
9. **Tier two entries** - one compact paragraph each.
10. **Other organisations of note** - largest, best documented, not tiered, withdrawn conclusions, safety holds.
11. **Control group.**
12. **Independent verification** - claims checked, confirmed, partly right, refuted, not checked; what changed.
13. **Right of reply** - the standard request; table of High/Medium flags with questions and contact channel; replies received.
14. **What changed, limits and notice** - review points and responses, public criticism and what changed because of it (do not name critics without consent), limits, corrections address, legal notice, revision log.
- **Appendices:** census routes and search terms; descriptive attributes (no conclusions); members not tiered; borderline organisations; sources and reproduction instructions.

**Ordering rule:** wherever organisations are listed, sort by amount raised in the period, largest first; no public amount goes last, alphabetically.

**Charts:** one consistent palette (tier one red, tier two amber, tier three blue, not tiered grey, one accent colour for "in the stated area"); a source note under every chart.

---

## Mode C - Claims vs facts

| # | Claim (quoted briefly, with who made it and where) | What the record shows | Sources | Verdict |
|---|---|---|---|---|
| 1 | ... | ... | ... | Supported / Partly supported / Not supported / Unresolved |

Then: what remains open, and the questions to put to the organisation.

---

## Mode D - Comparison
One table per theme (money in, money out and place, pay, governance, transparency, claims), same tests, same period, fiscal-year mismatches flagged. A short "how to read this" note: different models (direct delivery vs grant-making, in-country vs home-country services) justify different ratios.

---

## Social-media thread (on request)
- One post per finding, each under the platform's limit; first post states what was studied and links the full report.
- One image card per post with the figure, its source on the card, and no personal data.
- Final post: the disclosure (AI-assisted, verified, not an allegation), the corrections address, and an invitation to reply.
- Do not post that questions were sent until they were.

## Source register (.csv / .xlsx)
Use `templates/source-register.csv`. Sheets for a full study: Register (one row per organisation), Purpose and place, Score basis, Flags, Evidence chain, Right of reply, Returns (one row per filing with IDs, links, filed vs due date), Controls, Screening, Verification log, Rulebook and amendments.

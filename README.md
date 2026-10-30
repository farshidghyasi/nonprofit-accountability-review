# Nonprofit Accountability Review

An open-source AI research skill for **filings-based accountability research on nonprofits, charities, foundations and NGOs** - with a focus on the **United States, Canada, the United Kingdom, Ireland, the European Union, Switzerland, Norway and Australia**.

Give it the name of an organisation (or a whole cause or sector) and it works the way a careful investigative researcher would: it pulls the organisation's **own public record** - tax returns, regulator registers, statutory and audited accounts, funders' grant records - and reports what that record shows and what it leaves unanswered:

- where the money came from, and where it went (and whether that matches what donors are told);
- how much is held in reserve, and what the leadership is paid;
- who controls the organisation and whether related-party ties are disclosed;
- whether its own beneficiary numbers agree with each other;
- what the law required it to publish, and whether it did.

It produces neutral, sourced reports with a **red-flag scorecard**, a **right-of-reply letter** for the organisation, and a **source register** so every figure can be checked.

Works with **Claude** (as an installable skill), **ChatGPT**, **Grok**, **Gemini**, **Perplexity** and **Microsoft Copilot** (as a custom assistant with instructions and a knowledge file), and **any other capable AI assistant** (as a single paste-in prompt).

> **Important.** This is a research method, not a verdict machine. A red flag is a question the public record leaves open, **not evidence of wrongdoing**. AI can misread filings and sound more certain than the evidence allows. Every output must be checked against the primary documents before it is relied on or published. Nothing here is legal, tax or financial advice.

---

## Contents

- [What it can do](#what-it-can-do)
- [Quick start](#quick-start)
- [User guide (every assistant, step by step)](docs/GUIDE.md)
- [How to ask for a review](#how-to-ask-for-a-review)
- [What you get back](#what-you-get-back)
- [The method in brief](#the-method-in-brief)
- [The ten red-flag tests](#the-ten-red-flag-tests)
- [Using the scripts](#using-the-scripts)
- [Before you publish anything](#before-you-publish-anything)
- [Repository layout](#repository-layout)
- [Limitations](#limitations)
- [Contributing](#contributing)
- [Licence](#licence)

---

## What it can do

| Mode | Ask for it when | Output |
|---|---|---|
| **A. Deep dive** | You want to understand one named organisation | "[Organisation] under the microscope" - an 18-section report with scorecard |
| **B. Landscape study** | You want to map a cause, sector, country focus or list of organisations | A working paper with a scoring matrix across every organisation, a control group and sensitivity checks |
| **C. Claims vs facts** | A specific claim is circulating (a viral post, a news story, the organisation's own appeal) | A claim-by-claim table: Supported / Partly supported / Not supported / Unresolved |
| **D. Comparison** | You want two to ten organisations side by side | Comparison tables using identical tests |

Optional extras on request: Word/PDF versions, a spreadsheet source register, a web page, or a social-media thread with one image card per post.

---

## Quick start

**Full step-by-step instructions for every assistant are in the [User guide](docs/GUIDE.md).** The short version:

| Assistant | Setup | Files |
|---|---|---|
| **Claude** (web, desktop, mobile) | Customize → Skills → **+** → Upload a skill (code execution on) | [`dist/nonprofit-accountability-review.zip`](dist/nonprofit-accountability-review.zip) |
| **Claude Code** | Copy the skill folder to `~/.claude/skills/` | [`skills/nonprofit-accountability-review/`](skills/nonprofit-accountability-review/) |
| **Claude API / Agent SDK** | Upload via the Skills API | same folder |
| **ChatGPT** | Custom GPT or Project: instructions + knowledge; web search and code interpreter on | [`instructions/INSTRUCTIONS.md`](instructions/INSTRUCTIONS.md) + [`dist/knowledge-pack.md`](dist/knowledge-pack.md) |
| **Grok** | Project (or custom instructions) + knowledge pack; DeepSearch on | same two files |
| **Gemini** | Gem: instructions + knowledge | same two files |
| **Perplexity** | Space: custom instructions + file | same two files |
| **Microsoft Copilot** | Microsoft 365 agent (instructions + knowledge), or paste-in prompt | same two files, or [`PROMPT.md`](PROMPT.md) |
| **Anything else** (Mistral, DeepSeek, local models…) | Paste the prompt into a new chat | [`PROMPT.md`](PROMPT.md) |

### Claude in 60 seconds
1. Download [`dist/nonprofit-accountability-review.zip`](dist/nonprofit-accountability-review.zip).
2. In Claude: **Settings → Capabilities** → make sure code execution is on.
3. **Customize → Skills → + → Create skill → Upload a skill** → choose the zip.
4. In a chat with web search on, ask: *"Review [organisation], [country], FY2020-FY2024, with a scorecard and right-of-reply questions."*

See [Use skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude) for current menu names.

### Claude Code
```bash
git clone https://github.com/farshidghyasi/nonprofit-accountability-review.git
cp -r nonprofit-accountability-review/skills/nonprofit-accountability-review ~/.claude/skills/
```

### ChatGPT, Grok, Gemini, Perplexity, Copilot
Create a custom GPT / Project / Gem / Space / agent, paste [`instructions/INSTRUCTIONS.md`](instructions/INSTRUCTIONS.md) into its **instructions**, upload [`dist/knowledge-pack.md`](dist/knowledge-pack.md) as **knowledge**, and turn on web search (and code execution where offered). Details for each in the [User guide](docs/GUIDE.md).

### No setup at all
Open [`PROMPT.md`](PROMPT.md), copy everything below the line into a new chat in any assistant, and add your request.

**What matters most:** the assistant must be able to **search the web and open pages**. Running code (for IRS XML and arithmetic) and a real browser (several registries block automated fetching) both help a lot.

---

## How to ask for a review

Be specific about the organisation, the country, the period and the output. Examples:

```
Mode A. Review "Example Children's Fund" (US, EIN 00-0000000), FY2020-FY2024.
I'm concerned about how much reaches the programmes overseas. Give me a report with
the scorecard, the misuse-hypothesis table and right-of-reply questions.
```

```
Mode B. Map UK-registered charities raising money for flood relief in [country] since 2021.
Use the Charity Commission register and OSCR. Score every organisation with at least
five applicable tests and include a control group. Output: working paper + source register.
```

```
Mode C. A viral post says "[Organisation] spends 80% of donations on salaries".
Check it against the filings and give me a claims-vs-facts table.
```

```
Mode D. Compare these three Canadian registered charities on money in, money out,
pay and governance, FY2021-FY2024: [A], [B], [C].
```

If you have documents already (PDF accounts, XML returns, annual reports), attach them - the skill will use them first.

---

## What you get back

A deep dive (Mode A) is structured like this:

1. Bottom line, with a confidence statement
2. Red-flag scorecard
3. Scope and method
4. Organisation profile and legal status
5. Governance, board and related parties
6. Founder / chief executive and linked entities
7. Money in
8. Money out, reserves, pay, cost per beneficiary
9. Where the money went vs what donors are told
10. Donation channels
11. Programmes and reach (claims vs evidence)
12. Transparency benchmark (legal duty vs good practice)
13. Controversies - with what is proven and what is not
14. Testing the misuse hypothesis
15. Right-of-reply questions
16. Comparison with peers (optional)
17. Limitations
18. Sources

Every substantive statement carries an evidence tag:

| Tag | Meaning |
|---|---|
| **F** | Filing fact (tax return, accounts, regulator record) with form, year, part, line |
| **F-A** | Fact from independently audited accounts |
| **C** | Computed from filing facts, formula shown |
| **O** | The organisation's own claim |
| **T** | Third-party record (regulator, funder, rating agency, press) |
| **I** | Interpretation - never the sole basis for a score |

Full structures for every mode are in [`references/report-templates.md`](skills/nonprofit-accountability-review/references/report-templates.md).

---

## The method in brief

1. **Identify the entity exactly** - legal names, registration numbers, legal form, subsidiaries, fiscal sponsors, founders' companies.
2. **Collect every year of primary records** - see the country guide in [`references/jurisdictions.md`](skills/nonprofit-accountability-review/references/jurisdictions.md). US returns are parsed from IRS e-file XML by code, never retyped.
3. **Build the money picture** - money in, money out, where it went, what is left, pay.
4. **Check governance and related parties** - only relationships the filing discloses count; shared surnames never do.
5. **Check programme claims** for internal consistency.
6. **Score the ten tests**, each with a written basis and source, after testing the strongest innocent explanation.
7. **Test the misuse hypothesis** explicitly - and say "no evidence of misuse was found" when that is the result.
8. **Independent verification** - a separate agent or fresh chat re-checks every factual claim blind ([`references/verification.md`](skills/nonprofit-accountability-review/references/verification.md)).
9. **Right of reply** - specific questions tied to line items, a fixed reply date, replies published in full. *You* send the letter.
10. **Write the outputs** with the disclosure block at the top.

Core principles: primary records first; missing data is never scored unless the law required it; the same rulebook for everyone, written before scoring; protected characteristics are never criteria; privacy and safety for people in fragile settings. See [`references/ethics-and-safety.md`](skills/nonprofit-accountability-review/references/ethics-and-safety.md).

---

## The ten red-flag tests

Each scores 0 (green), 1 (amber), 2 (red) or n/a. Score = points ÷ (2 × tests applied). **Tier one ≥ 40%, tier two 20-39%, tier three < 20%.** Fewer than five applicable tests → "insufficient record to tier".

| Code | Question |
|---|---|
| **GEO** | Does the money go where donors are told? |
| **SCHED** | Is foreign-activity reporting complete and consistent? (US Schedule F) |
| **INTERNAL** | Do the organisation's own numbers agree? |
| **GOV** | How concentrated is control? |
| **FAMILY** | Are family / related-party ties disclosed, and do they involve money? |
| **RESERVES** | Are unrestricted reserves out of proportion to spending? |
| **UNNAMED** | Are grant recipients identifiable? |
| **CLAIMS** | Are beneficiary numbers consistent? |
| **PAY** | Is leadership pay out of line with peers? |
| **PUBLIC** | Was everything the law required filed on time - and anything more? |

Exact thresholds, placement rules, flag severity and the evidence chain are in [`references/scoring-rubric.md`](skills/nonprofit-accountability-review/references/scoring-rubric.md). **A high score means more open questions, not a worse organisation.** Small organisations score higher on some tests simply because they are small, so scale is always shown beside the score.

---

## Using the scripts

Python 3, standard library only.

**Parse IRS Form 990 XML** (from ProPublica Nonprofit Explorer or the GivingTuesday 990 data lake):

```bash
python3 skills/nonprofit-accountability-review/scripts/parse_990_xml.py path/to/xml_folder --out out/
```

Writes `returns.csv` (one row per return: revenue, expenses, functional split, net assets, Part IV triggers, Part VI governance answers, audit flag, balance-sheet check, programme share, reserves in years, top pay and its share of expenses), `people.csv` (Part VII), `schedule_f.csv` (spending and grants by world region) and `returns.json`.

**Compute scores and tiers** from your scores sheet:

```bash
python3 skills/nonprofit-accountability-review/scripts/score.py examples/sample_scores.csv --out scored.csv
```

Try both on the fictional examples in [`examples/`](examples/).

---

## Before you publish anything

- [ ] Every figure traced to a document a reader can open
- [ ] Independent verification run in a separate session; corrections logged
- [ ] Right-of-reply letter **sent by you**, reply period passed, replies included in full
- [ ] No private family members, beneficiaries, local staff or at-risk locations named
- [ ] No words like "fraud", "theft" or "illegal" unless a court or regulator has said so - and then attributed
- [ ] Disclosure block at the top: AI-assisted, verified, not an allegation, your conflicts of interest, a corrections address
- [ ] For anything that could damage a named organisation or person, consider a media-law review in that jurisdiction

---

## Repository layout

```
nonprofit-accountability-review/
├── README.md
├── LICENSE
├── PROMPT.md                          one-paste prompt for any AI assistant
├── docs/
│   └── GUIDE.md                       step-by-step guide for every assistant
├── instructions/
│   └── INSTRUCTIONS.md                instructions box for GPTs, Projects, Gems, Spaces, agents
├── dist/
│   ├── nonprofit-accountability-review.zip   the Claude skill, ready to upload
│   └── knowledge-pack.md              all reference files in one document
├── examples/                          fictional data for trying the scripts
├── tools/
│   └── build_dist.sh                  rebuilds dist/ from the skill folder
└── skills/
    └── nonprofit-accountability-review/
        ├── SKILL.md                   the skill (entry point)
        ├── references/
        │   ├── jurisdictions.md       registers, thresholds and deadlines by country
        │   ├── us-form-990-guide.md   reading Form 990, XML element names, traps
        │   ├── scoring-rubric.md      the ten tests, tiers, severity, evidence chain
        │   ├── report-templates.md    structures for every mode and format
        │   ├── ethics-and-safety.md   language, privacy, safety, conflicts, AI disclosure
        │   └── verification.md        blind fact-check protocol and prompt
        ├── templates/
        │   ├── right-of-reply.md
        │   └── source-register.csv
        └── scripts/
            ├── parse_990_xml.py
            └── score.py
```

---

## Limitations

- **Filings show allocation, not delivery.** A tax return can show money was sent; only audits, inspections and evaluations show it was used as intended.
- **Disclosure duties differ hugely.** A US 501(c)(3) publishes far more than a German *e.V.* or a Canadian non-charity not-for-profit. The skill marks "not required" as such and never compares raw scores across jurisdictions.
- **Thresholds and deadlines change.** The country guide is a starting point; confirm the rule in force for the year before calling anything a breach.
- **Access.** Some registries block automated access, charge per document or need a real browser. When something cannot be reached, the output says so.
- **AI error.** Misread lines, missed schedules and overconfident wording all happen. The verification step exists because of this.

---

## Contributing

Corrections and improvements are welcome - especially:
- registry guides for more countries, and updated thresholds (with a link to the regulator's page);
- better XML coverage in the parser (older schemas, 990-PF detail);
- worked examples using **fictional** organisations.

If you edit anything in `skills/`, run `bash tools/build_dist.sh` so the zip and knowledge pack stay in sync. Open an issue or a pull request. Please do not add reports about real organisations to this repository; it is a method, not a publication.

---

## Licence

[MIT](LICENSE). Use it, adapt it, build on it. If you publish research made with it, saying which version of the method you used helps others reproduce your work.

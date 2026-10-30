# Nonprofit Accountability Review

An open-source AI research skill for **filings-based accountability research on nonprofits, charities, foundations and NGOs** - with a focus on the **United States, Canada, the United Kingdom, Ireland, the European Union, Switzerland, Norway and Australia**.

Give it the name of an organisation (or a whole cause or sector) and it works the way a careful investigative researcher would: it pulls the organisation's **own public record** - tax returns, regulator registers, statutory and audited accounts, funders' grant records - and reports what that record shows and what it leaves unanswered:

- where the money came from, and where it went (and whether that matches what donors are told);
- how much is held in reserve, and what the leadership is paid;
- who controls the organisation and whether related-party ties are disclosed;
- whether its own beneficiary numbers agree with each other;
- what the law required it to publish, and whether it did.

It produces neutral, sourced reports with a **red-flag scorecard**, a **right-of-reply letter** for the organisation, and a **source register** so every figure can be checked.

Works with **Claude** (as an installable skill), **ChatGPT** (as a custom GPT or project), and **any capable AI assistant** (as a single paste-in prompt).

> **Important.** This is a research method, not a verdict machine. A red flag is a question the public record leaves open, **not evidence of wrongdoing**. AI can misread filings and sound more certain than the evidence allows. Every output must be checked against the primary documents before it is relied on or published. Nothing here is legal, tax or financial advice.

---

## Contents

- [What it can do](#what-it-can-do)
- [Quick start](#quick-start)
  - [Claude.ai (web, desktop, mobile)](#1-claudeai-web-desktop-mobile)
  - [Claude Code](#2-claude-code)
  - [Claude API / Agent SDK](#3-claude-api--agent-sdk)
  - [ChatGPT](#4-chatgpt)
  - [Any other AI assistant](#5-any-other-ai-assistant)
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

First download the skill: on this page click **Code → Download ZIP**, or grab the ready-made **`dist/nonprofit-accountability-review.zip`** (the skill folder only, packaged for upload).

### 1. Claude.ai (web, desktop, mobile)

1. Make sure **code execution** is on: **Settings → Capabilities** (Free, Pro and Max). On Team and Enterprise plans your organisation owner may need to enable skills.
2. Go to **Customize → Skills**, click **+**, choose **Create skill → Upload a skill**.
3. Upload **`dist/nonprofit-accountability-review.zip`**.
4. Make sure the skill is toggled **on**. Turn on **web search** for the chat.
5. Ask: *"Use the nonprofit accountability review skill to review [organisation] for FY2020-FY2024."*

Claude loads the skill automatically whenever you ask for nonprofit research. See Anthropic's help article [Use skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude) for the current menu names.

**Tip:** if you have the Claude desktop app with a browser extension or computer use, Claude can open registries that block automated fetching (several do). It will never bypass a CAPTCHA.

### 2. Claude Code

Copy the skill folder into your personal or project skills directory:

```bash
git clone https://github.com/<owner>/nonprofit-accountability-review.git
# personal (all projects)
cp -r nonprofit-accountability-review/skills/nonprofit-accountability-review ~/.claude/skills/
# or project-only
mkdir -p .claude/skills && cp -r nonprofit-accountability-review/skills/nonprofit-accountability-review .claude/skills/
```

Start Claude Code and ask for a review. The skill's scripts run locally with Python 3 (standard library only).

### 3. Claude API / Agent SDK

Upload the skill folder through the Skills API and attach it to your requests, or place it in your agent's skills directory. See Anthropic's [Agent Skills documentation](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview). Give the agent web search, web fetch and code execution tools.

### 4. ChatGPT

Follow [`chatgpt/SETUP.md`](chatgpt/SETUP.md). In short:
- **Custom GPT:** paste [`chatgpt/GPT_INSTRUCTIONS.md`](chatgpt/GPT_INSTRUCTIONS.md) into *Instructions*, upload the files in `skills/nonprofit-accountability-review/references/` and `templates/` as *Knowledge*, and enable **Web search** and **Code interpreter**.
- **Project:** put the same instructions in the project and the same files in project files.

### 5. Any other AI assistant

Open [`PROMPT.md`](PROMPT.md), copy everything below the line into a new chat (Gemini, Copilot, Perplexity, Mistral, a local model…), and add your request at the end. Use a tool that can search the web and open pages.

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
├── PROMPT.md                         one-paste prompt for any AI assistant
├── chatgpt/
│   ├── GPT_INSTRUCTIONS.md           custom GPT / project instructions
│   └── SETUP.md                      step-by-step ChatGPT setup
├── dist/
│   └── nonprofit-accountability-review.zip   ready to upload to Claude.ai
├── examples/                         fictional data for trying the scripts
└── skills/
    └── nonprofit-accountability-review/
        ├── SKILL.md                  the skill (entry point)
        ├── references/
        │   ├── jurisdictions.md      registers, thresholds and deadlines by country
        │   ├── us-form-990-guide.md  reading Form 990, XML element names, traps
        │   ├── scoring-rubric.md     the ten tests, tiers, severity, evidence chain
        │   ├── report-templates.md   structures for every mode and format
        │   ├── ethics-and-safety.md  language, privacy, safety, conflicts, AI disclosure
        │   └── verification.md       blind fact-check protocol and prompt
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

Open an issue or a pull request. Please do not add reports about real organisations to this repository; it is a method, not a publication.

---

## Licence

[MIT](LICENSE). Use it, adapt it, build on it. If you publish research made with it, saying which version of the method you used helps others reproduce your work.

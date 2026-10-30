# User guide

How to set up and run **Nonprofit Accountability Review** with Claude, ChatGPT, Grok, Gemini, Perplexity, Microsoft Copilot and other AI assistants - and how to run a review from first question to publication.

App menus change often. If a label below doesn't match what you see, look for the nearest equivalent ("Projects", "Gems", "Spaces", "custom instructions", "knowledge", "sources").

---

## Contents

1. [Pick your setup](#1-pick-your-setup)
2. [The four files you will use](#2-the-four-files-you-will-use)
3. [Claude](#3-claude)
4. [ChatGPT](#4-chatgpt)
5. [Grok](#5-grok)
6. [Google Gemini](#6-google-gemini)
7. [Perplexity](#7-perplexity)
8. [Microsoft Copilot](#8-microsoft-copilot)
9. [Other assistants and local models](#9-other-assistants-and-local-models)
10. [Running a review, step by step](#10-running-a-review-step-by-step)
11. [When the AI can't reach a registry](#11-when-the-ai-cant-reach-a-registry)
12. [Running the scripts yourself](#12-running-the-scripts-yourself)
13. [Troubleshooting](#13-troubleshooting)

---

## 1. Pick your setup

| Assistant | Best setup | What it needs to work well |
|---|---|---|
| **Claude** (claude.ai, desktop, mobile) | Install the **skill** (zip upload) | Code execution and web search on |
| **Claude Code** | Copy the **skill folder** into `~/.claude/skills/` | Python 3 for the scripts |
| **Claude API / Agent SDK** | Upload the **skill** via the Skills API | Web search, web fetch and code execution tools |
| **ChatGPT** | A **custom GPT** or a **Project** with instructions + knowledge | Web search and code interpreter on |
| **Grok** | A **Project** with instructions + knowledge pack, or custom instructions | Web/DeepSearch on |
| **Gemini** | A **Gem** with instructions + knowledge pack | Use Deep Research for long reviews |
| **Perplexity** | A **Space** with instructions + knowledge pack | Pro search |
| **Microsoft Copilot** | A Copilot **agent** (Microsoft 365) or paste-in prompt | Web grounding on |
| **Anything else** | Paste **`PROMPT.md`** into a new chat | Web access |

**What matters most, in order:** (1) the assistant can **search the web and open pages**; (2) it can **run code** (to parse IRS XML and do arithmetic reliably); (3) it can use a **real browser** (several registries block automated fetching). Without web access the assistant can only work from documents you upload.

---

## 2. The four files you will use

| File | What it is | Used for |
|---|---|---|
| [`dist/nonprofit-accountability-review.zip`](../dist/nonprofit-accountability-review.zip) | The Claude skill, packaged | Claude.ai upload |
| [`instructions/INSTRUCTIONS.md`](../instructions/INSTRUCTIONS.md) | The method's core rules and workflow (~5,000 characters) | The "instructions" box of a GPT, Project, Gem, Space or agent |
| [`dist/knowledge-pack.md`](../dist/knowledge-pack.md) | Every reference file in one document (country guide, 990 guide, scoring rubric, report templates, ethics, verification, right-of-reply letter) | The "knowledge" / "files" / "sources" of a GPT, Project, Gem, Space or agent |
| [`PROMPT.md`](../PROMPT.md) | A self-contained prompt with the rubric appended | Any chat with no setup |

To download: on the repository page click a file, then the **download** icon; or **Code → Download ZIP** for everything.

---

## 3. Claude

### 3a. Claude.ai - web, desktop and mobile apps (recommended)

1. **Turn on code execution.** Settings → Capabilities (Free, Pro, Max). On Team and Enterprise plans an owner may need to enable skills for the organisation.
2. **Upload the skill.** Customize → Skills → **+** → Create skill → **Upload a skill** → choose `nonprofit-accountability-review.zip`.
3. **Check it's on.** The skill appears in your list with a toggle.
4. **Start a chat** with web search enabled and ask, for example:
   > Use the nonprofit accountability review skill. Mode A: review [organisation], [country], FY2020-FY2024.

Claude reads the skill automatically whenever you ask for nonprofit research, so you can also just ask naturally. Anthropic's help page: [Use skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude).

**Make it stronger:**
- **Desktop app + browser:** if you connect a browser (Claude in Chrome) or computer use, Claude can open registries that refuse automated requests (the UK Charity Commission accounts, some European registers). It never solves CAPTCHAs.
- **Use a Project for a long study.** Put your scope and conflicts of interest in the project instructions; upload the filings you have; every chat in the project shares them.
- **Verification:** Claude can run the blind fact-check with a separate agent where available; otherwise run the checker prompt in a new chat.

**Alternative without the skill upload:** create a Project, paste `instructions/INSTRUCTIONS.md` into its instructions and add `dist/knowledge-pack.md` as a project file.

### 3b. Claude Code

```bash
git clone https://github.com/farshidghyasi/nonprofit-accountability-review.git
cp -r nonprofit-accountability-review/skills/nonprofit-accountability-review ~/.claude/skills/        # all projects
# or, for one project:
mkdir -p .claude/skills && cp -r nonprofit-accountability-review/skills/nonprofit-accountability-review .claude/skills/
```

Then start Claude Code in a working folder and ask for a review. The scripts run locally with Python 3 (no extra packages). Keep each study in its own folder so the source register, XML files and outputs stay together.

### 3c. Claude API and Agent SDK

Upload the skill folder via the Skills API (or place it in your agent's skills directory) and give the agent web search, web fetch and code execution. See Anthropic's [Agent Skills overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview).

---

## 4. ChatGPT

### 4a. Custom GPT (best)
1. **Explore GPTs → Create** (or My GPTs → Create a GPT) → **Configure** tab.
2. **Name:** Nonprofit Accountability Reviewer. **Description:** Filings-based research on nonprofits and charities.
3. **Instructions:** paste all of `instructions/INSTRUCTIONS.md`. (It fits the instructions limit.)
4. **Knowledge:** upload `dist/knowledge-pack.md`. Optionally also upload `skills/nonprofit-accountability-review/scripts/parse_990_xml.py` and `score.py` so the GPT can run them.
5. **Capabilities:** turn on **Web search** and **Code interpreter & data analysis**. Image generation only if you want social cards.
6. **Conversation starters** (optional):
   - "Mode A: review an organisation"
   - "Mode C: check a claim about a charity"
   - "Mode B: map a cause or sector"
7. **Save** - keep it private, share by link, or publish it.

### 4b. ChatGPT Project
Create a Project → add `instructions/INSTRUCTIONS.md` as the project instructions → add `dist/knowledge-pack.md` to project files. Useful when you want to keep all chats and uploaded filings for one study together.

### 4c. Plain chat
Paste `PROMPT.md` (everything below the line), then your request.

**Tips:** for long reviews, use ChatGPT's deep-research mode for the source-gathering step, then switch back to a normal chat with code interpreter for the arithmetic and scoring. Ask it to *open* each filing, not to recall it.

---

## 5. Grok

### 5a. Grok Project (if your plan offers Projects)
1. In grok.com (or the app) open **Projects** → create a new project, e.g. "Nonprofit reviews".
2. Paste `instructions/INSTRUCTIONS.md` into the project's **instructions**.
3. Upload `dist/knowledge-pack.md` as a project file/source.
4. Start chats inside the project. Turn on web search / **DeepSearch** for gathering filings.

### 5b. Custom instructions
If Projects aren't available, paste `instructions/INSTRUCTIONS.md` into Grok's **customize / custom instructions** setting and attach `dist/knowledge-pack.md` to the first message of each review.

### 5c. Plain chat
Paste `PROMPT.md`, then your request.

**Grok-specific tips:**
- Grok can search X (Twitter) posts. Treat posts as **claims (O or T)**, never as evidence; the method keeps them separate from filings.
- Ask Grok to give the URL of every filing it relies on, and open a few yourself.

---

## 6. Google Gemini

1. In Gemini open **Gems** → **+ New Gem**.
2. **Name:** Nonprofit Accountability Reviewer.
3. **Instructions:** paste `instructions/INSTRUCTIONS.md`.
4. **Knowledge:** add `dist/knowledge-pack.md` (from your computer or Google Drive). Wait for it to finish processing.
5. **Save**, then open the Gem and ask for a review.

**Tips:** use **Deep Research** for the census or source-gathering step of a large study, then bring the source list back into the Gem for scoring. If your organisation's filings are in Google Drive, attach them directly.

---

## 7. Perplexity

1. Open **Spaces** → **Create a Space** → title it "Nonprofit reviews".
2. Paste `instructions/INSTRUCTIONS.md` into the Space's **custom instructions**.
3. Add `dist/knowledge-pack.md` as a Space file. (Upload limits depend on your plan.)
4. Ask questions inside the Space.

**Tips:** Perplexity is strong at finding sources and weaker at long structured documents. A good pattern: use the Space to find and cite the filings, then do the scoring and write-up in an assistant with code execution.

---

## 8. Microsoft Copilot

- **Microsoft 365 Copilot (work accounts):** create an **agent** (Copilot Studio or the agent builder) → paste `instructions/INSTRUCTIONS.md` into its instructions → add `dist/knowledge-pack.md` as knowledge → allow web search. Your organisation's admin may control whether agents and web grounding are available.
- **Consumer Copilot:** paste `PROMPT.md` into a new conversation, then your request.

---

## 9. Other assistants and local models

**Mistral Le Chat, DeepSeek, Meta AI, Kimi, Qwen and others:** paste `PROMPT.md` into a new chat. If the assistant supports agents/custom instructions and document libraries, use `instructions/INSTRUCTIONS.md` + `dist/knowledge-pack.md` instead.

**Local models (Open WebUI, LM Studio, Ollama front-ends, AnythingLLM):** put `instructions/INSTRUCTIONS.md` in the system prompt and `dist/knowledge-pack.md` in the document/knowledge store. Local models usually have no live web access, so download the filings yourself (section 11) and attach them. Use the largest model you can run; small models misread financial tables.

**Agent frameworks** (any that support the open `SKILL.md` format, or custom tools): point them at `skills/nonprofit-accountability-review/`.

---

## 10. Running a review, step by step

These prompts work in any assistant set up as above.

### Step 1 - Scope
> Mode A. Organisation: [name]. Country: [country]. Identifier if known: [EIN / charity number]. Period: FY2020-FY2024. My concern: [e.g. how much reaches programmes abroad]. Output: report with scorecard, misuse-hypothesis table and right-of-reply questions. My conflicts of interest: [none / describe].

Always state your **conflicts of interest** - the method puts them on the first page.

### Step 2 - Records
> List every filing in the period with its year, form type and link. Tell me which you could open and which you couldn't.

Check the list. If years are missing, download them yourself (section 11) and upload.

### Step 3 - Money picture
> Build the money-in / money-out / where-it-went / reserves / pay tables, by year and in total, with the source line for every number.

### Step 4 - Governance and claims
> Now governance, related parties and every published beneficiary figure, with sources and dates.

### Step 5 - Scores
> Score the ten tests. For each: score, basis, evidence tag, source, and the innocent explanation you tested.

### Step 6 - Draft
> Write the full Mode A report.

### Step 7 - Blind verification (do this in a **new chat**)
In the original chat:
> Extract every factual claim from the report as a numbered list with its source. Remove all scores, verdicts and interpretation.

Open a **fresh chat** (ideally a different assistant), paste the checker prompt from the knowledge pack's verification section and the claim list. Bring the results back:
> Here are the fact-check results. Apply every correction, re-score where a fact changed, and log the changes.

### Step 8 - Right of reply
> Draft the right-of-reply letter with questions tied to specific lines.

**You** send it, by email or the organisation's contact form. Record the date. Wait for the reply period (10-14 days is common).

### Step 9 - Final
> The organisation [replied - text attached / did not reply by date]. Update the report and add the reply in full.

Then go through the **before you publish** checklist in the [README](../README.md#before-you-publish-anything).

### Other modes - starter prompts
- **Mode B (landscape):** "Map [cause] organisations registered in [countries] since [year]. Define the inclusion rule first, show me the census routes, then score every member and a control group chosen by rule."
- **Mode C (claim check):** "This claim is circulating: '[quote]' (source: [link]). Check it against the filings and give me a claims-vs-facts table."
- **Mode D (comparison):** "Compare [A], [B] and [C] on the same tests for FY2021-FY2024, and explain differences in operating model."

---

## 11. When the AI can't reach a registry

Many regulators block automated requests. You can fetch the documents yourself in a normal browser and upload them:

| Country | Where to download | What to download |
|---|---|---|
| US | `projects.propublica.org/nonprofits/organizations/<EIN>` | Each year's **XML** (best) or PDF |
| England & Wales | Charity Commission "Register of charities" → the charity → Accounts and annual returns | Accounts PDF for each year |
| Scotland | OSCR register → the charity | Accounts |
| Canada | CRA Charities Listings → the charity → T3010 information returns | Each year's return |
| Australia | ACNC register → the charity → Documents | AIS and financial reports |
| Europe | See the country table in the knowledge pack | Register extract, accounts |

Upload the files and say: *"Use only these files and tell me if anything I need is missing."* The assistant should tag figures from scans as such.

---

## 12. Running the scripts yourself

Python 3, no extra packages.

```bash
# Parse IRS 990 XML files (one folder, any number of years)
python3 skills/nonprofit-accountability-review/scripts/parse_990_xml.py my_xml_folder --out out/

# Score organisations from a scores sheet
python3 skills/nonprofit-accountability-review/scripts/score.py my_scores.csv --out scored.csv
```

`out/returns.csv`, `people.csv` and `schedule_f.csv` can be uploaded to any assistant: *"Here are the parsed returns - use these figures, not your own reading of the PDFs."* Try both scripts on the fictional data in [`examples/`](../examples/).

To rebuild the zip and knowledge pack after editing the skill: `bash tools/build_dist.sh`.

---

## 13. Troubleshooting

| Problem | Fix |
|---|---|
| Claude.ai upload fails | The zip must contain the folder `nonprofit-accountability-review/` with `SKILL.md` inside. Use the zip in `dist/` unchanged. Make sure code execution is on. |
| The assistant invents figures or links | Tell it: "Only use figures from documents you opened in this chat; give the URL and line for each." Upload the filings yourself. Run the verification step. |
| "I can't access that site" | Download the document yourself (section 11) and upload it. |
| Numbers don't add up between tables | Ask it to keep one master table and generate every other table from it; or run the scripts and give it the CSVs. |
| The report sounds accusatory | Remind it: "Follow the ethics rules - no 'fraud' or 'misuse'; flags are questions." |
| Instructions are too long for the box | Use `instructions/INSTRUCTIONS.md` (about 5,000 characters), not `PROMPT.md`. |
| The assistant ignores the knowledge file | Mention it explicitly: "Use the scoring rubric in the knowledge pack." |
| Scores look wrong | Put the scores in a CSV and run `score.py`; the tiers then follow the rules exactly. |

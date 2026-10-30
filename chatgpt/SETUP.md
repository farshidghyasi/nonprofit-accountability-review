# Using this with ChatGPT

ChatGPT does not read Claude's skill format directly, but the same method works in two ways.

## Option 1 - A custom GPT (recommended, needs a plan that can create GPTs)

1. In ChatGPT open **Explore GPTs → Create** (or **My GPTs → Create a GPT**), then the **Configure** tab.
2. **Name:** Nonprofit Accountability Reviewer. **Description:** Filings-based research on nonprofits and charities.
3. **Instructions:** paste the whole of [`GPT_INSTRUCTIONS.md`](GPT_INSTRUCTIONS.md) (about 5,000 characters - under the limit).
4. **Knowledge:** upload these files from `skills/nonprofit-accountability-review/`:
   - `references/jurisdictions.md`
   - `references/us-form-990-guide.md`
   - `references/scoring-rubric.md`
   - `references/report-templates.md`
   - `references/ethics-and-safety.md`
   - `references/verification.md`
   - `templates/right-of-reply.md`
   - `templates/source-register.csv`
   - optionally `scripts/parse_990_xml.py` and `scripts/score.py` (the GPT can run them with its code tool)
5. **Capabilities:** turn on **Web search** and **Code interpreter / data analysis**. Image generation is optional (for social cards).
6. Save. Keep it private, share by link, or publish it - your choice.

Menu names change from time to time; if a label differs, look for the GPT builder's "Configure" view.

## Option 2 - A ChatGPT Project

Create a Project, paste `GPT_INSTRUCTIONS.md` into the project instructions, and add the same reference files to the project files. Every chat in the project then follows the method.

## Option 3 - No setup

Paste [`../PROMPT.md`](../PROMPT.md) into a new chat and add your request at the end.

## Tips for ChatGPT
- Ask it to **open** each filing, not to recall it. Say: *"Open the ProPublica page for EIN XX-XXXXXXX and list every return with its year and link."*
- If it cannot reach a registry, download the PDF or XML yourself and upload it to the chat.
- Run the verification step in a **separate chat** so the checker has not seen the analysis.

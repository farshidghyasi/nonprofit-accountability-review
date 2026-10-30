# Nonprofit Accountability Review - knowledge pack

All reference files of the skill in one document. Upload this as a knowledge/source file
alongside the instructions in instructions/INSTRUCTIONS.md (works for any assistant).

---

<!-- file: references/jurisdictions.md -->

# Where to find the records, country by country

Thresholds, deadlines and URLs change. **Before you score anything as a legal breach, confirm the rule that was in force for that entity, that financial year and that size** on the regulator's own site, and cite it. The figures below are a starting point, not legal advice.

Universal rule: the organisation's own website is a **claim (O)**; the regulator's record and filed accounts are **facts (F / F-A)**.

---

## United States

**Who files what (IRS)**
- Form **990-N** (e-Postcard): small organisations with gross receipts normally ≤ $50,000. Gives only name, address, principal officer.
- Form **990-EZ**: gross receipts < $200,000 and total assets < $500,000. No functional expense split, few governance questions.
- Form **990**: everyone above those limits. Full governance (Part VI), pay (Part VII), functional expenses (Part IX), balance sheet (Part X) and schedules.
- Form **990-PF**: private foundations, whatever their size. Grants paid listed in Part XIV (tax year 2022 onward; Part XV on older returns) - the best source for tracing who funds a charity.
- Due the 15th day of the 5th month after year end; an automatic 6-month extension is available (Form 8868).
- **Automatic revocation** of exemption after three consecutive years of not filing.

**Where**
- ProPublica Nonprofit Explorer - `projects.propublica.org/nonprofits/organizations/<EIN>` - filing index, PDFs, links to XML and full-text schedules.
- IRS e-file XML (public): GivingTuesday 990 Data Lake (`gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/<object_id>_public.xml`); ProPublica's `download-xml?object_id=` link.
- IRS Tax Exempt Organization Search (TEOS): Pub 78 deductibility, determination letters, auto-revocation list, 990-N, bulk downloads. IRS Business Master File (EO BMF) extracts.
- Candid (GuideStar), Charity Navigator, BBB Wise Giving Alliance - third-party (T).
- **State regulators:** charity registries and filed audits - e.g. California Attorney General Registry of Charities, New York Charities Bureau (CHAR500 with audited statements above thresholds), and other states' Secretary of State / Attorney General registries. State audit thresholds differ; check the state and year.
- **Federal money:** USAspending.gov (awards and sub-awards), SAM.gov, Federal Audit Clearinghouse (single audits). Single audit is triggered by **federal awards expended** of $750,000 (fiscal years beginning before 1 Oct 2024) or $1,000,000 (fiscal years beginning on or after 1 Oct 2024) - not by total government revenue.
- **Courts and regulators:** state AG settlements, IRS revocations, inspector-general audits (e.g. agency OIGs) - formal findings.

See `us-form-990-guide.md` for line-by-line guidance.

---

## Canada

- **Registered charities** file the **T3010** within six months of year end. The CRA "Charities Listings" and the **List of charities open data** (open.canada.ca) give directors (with an arm's-length flag), revenue and expenditure lines, compensation bands, countries where activities took place, and gifts to qualified donees.
- T3010 Schedule 2 (activities outside Canada) and Schedule 3 (compensation) where filed.
- **Disbursement quota** applies to registered charities (3.5%, rising to 5% on the portion of property above $1 million for fiscal periods beginning on or after 1 Jan 2023) - check the year.
- **Non-charity not-for-profits** (NPOs) file tax returns that are **not public**. Their corporate record is with **Corporations Canada** (federal, under the CNCA - annual return due within 60 days of the anniversary) or the province (e.g. Ontario Business Registry, Registraire des entreprises du Québec). Absence of public accounts for an NPO is usually *not required*, not a breach.
- Imagine Canada Standards Program (accreditation, T).

---

## United Kingdom

**England & Wales - Charity Commission**
- Charities with income > £5,000 must register (exceptions apply).
- Annual return for income > £10,000; accounts and trustees' annual report filed with the Commission for income > £25,000.
- Scrutiny thresholds depend on the year end:
  - financial years ending **before 30 Sep 2026**: independent examination above £25,000 income; **audit** above £1 million income, or above £250,000 income with gross assets over £3.26 million;
  - financial years ending **on or after 30 Sep 2026**: independent examination above £40,000; **audit** above £1.5 million income, or above £500,000 income with gross assets over £5 million (the qualified-examiner and accruals thresholds also move from £250,000 to £500,000). Source: gov.uk "Charity accounts: threshold changes at a glance".
- Deadline: **10 months** after year end. The register shows days late and "overdue" status.
- Register pages: trustees, income/expenditure history, area of operation, governing document, linked charities. Accounts PDFs are downloadable from the register (often only in a real browser).
- Charitable companies also file at **Companies House** (accounts, officers, persons with significant control, filing history).
- Commission regulatory alerts, statutory inquiries and published case reports are formal findings (T).

**Scotland - OSCR**: every charity files an annual return and accounts within **9 months**; register includes income/expenditure and links to accounts.
**Northern Ireland - Charity Commission for Northern Ireland (CCNI)**: register with annual monitoring returns and accounts.

**Funder data:** 360Giving GrantNav (UK grants from hundreds of funders), National Lottery and government grant registers.
**Fundraising:** Fundraising Regulator (directory of levy payers, complaints).

---

## Ireland

- **Charities Regulator** register (registered charity number, trustees, annual reports - due within 10 months of year end).
- Most charities are companies limited by guarantee: **CRO** (Companies Registration Office) holds financial statements and directors (small fee per document).
- Revenue's list of charities with tax-exempt status (CHY number). Charities Institute Ireland Triple Lock (T).

---

## Australia

- **ACNC** register: responsible persons, governing documents, financial reports, AIS (Annual Information Statement), revocations. ACNC entity API and AIS open data on data.gov.au.
- Size (from 2022-23 reporting): small < A$500,000 revenue; medium A$500,000 - < A$3 million (reviewed or audited financial report); large ≥ A$3 million (audited). Confirm the year.
- AIS due six months after year end.
- AIS fields useful for scoring: grants for use outside Australia, related-party transactions, key management personnel remuneration, net assets.
- Overseas aid: Overseas Aid Gift Deduction Scheme (DFAT); ACFID Code of Conduct signatories (T).

---

## European Union, Switzerland and Norway

Public disclosure duties vary widely. **In many countries associations have no duty to publish accounts**; record such gaps as "not required", never as a breach.

| Country | Registers and records | Notes |
|---|---|---|
| **Germany** | Gemeinsames Registerportal (Vereinsregister for e.V.; Handelsregister for gGmbH); Unternehmensregister (filed accounts of gGmbH/companies); Transparenzregister; Bundestag **Lobbyregister** (grants by funder, uploaded accounts for registered interest groups); foundation registers by Land | e.V. have no general duty to publish accounts. **DZI Spendensiegel** and **Initiative Transparente Zivilgesellschaft** are voluntary transparency signals. |
| **France** | RNA (associations register), SIRENE / recherche-entreprises.api.gouv.fr, **Journal officiel - associations** | Associations receiving more than €153,000 in donations or public subsidies must publish accounts in the JO. **Don en Confiance** label. Cour des comptes reports on public-appeal charities. |
| **Netherlands** | KvK (Chamber of Commerce); Belastingdienst **ANBI** register (API) | ANBIs must publish set items on their own website (policy, board, pay policy, activity report, financial statement). **CBF Erkenning** seal. |
| **Belgium** | Crossroads Bank for Enterprises (KBO/BCE); **National Bank of Belgium Central Balance Sheet Office** (accounts of ASBL/VZW above size thresholds) | Moniteur belge for statutes and board changes. |
| **Luxembourg** | RCS / LBR (asbl and fondations file accounts) | |
| **Switzerland** | **Zefix** and cantonal commercial registers (extracts can state nationality/place of origin of board members); federal/cantonal foundation supervisory authorities | Associations need not register unless commercial; **ZEWO** seal. |
| **Austria** | ZVR (central register of associations); BMF list of tax-deductible donation recipients | **Österreichisches Spendengütesiegel**. |
| **Italy** | **RUNTS** (Registro Unico Nazionale del Terzo Settore) - ETS financial statements deposited there | 5x1000 recipient lists (Agenzia delle Entrate). |
| **Spain** | Registro Nacional de Asociaciones; Registro de Fundaciones (accounts filed with the protectorate) | **Fundación Lealtad** accreditation. |
| **Portugal** | RNPC; IPSS register | |
| **Sweden** | Bolagsverket; county administrative boards for foundations | **Svensk Insamlingskontroll** 90-account holders publish key figures. |
| **Denmark** | CVR; **Indsamlingsnævnet** (fundraising board - collection accounts) | |
| **Finland** | Patentti- ja rekisterihallitus (associations and foundations registers) | Fundraising licences (Police). |
| **Norway** | **Brønnøysund** Enhetsregisteret (API, roles), Regnskapsregisteret (accounts for those required to file), Frivillighetsregisteret | **Innsamlingskontrollen** registered fundraisers publish accounts. Many associations have no duty to file accounts. |
| **Poland** | KRS (National Court Register); public benefit organisations (OPP) publish reports in the NIW database | 1.5% tax-designation list. |
| **Ireland** | see above | |

**EU-level money:** EU **Financial Transparency System** (FTS) for EU grants; **EU Transparency Register** (lobbying, declared budgets and funding); ECHO partner lists; Erasmus+/CERV project results platforms.

**International funders:** IATI d-portal (aid activity data), UN OCHA Financial Tracking Service, UN agencies' implementing-partner lists, foundations' published grants databases.

---

## Other places worth checking (all T, never sole basis)

- Ratings and seals: Charity Navigator, Candid seals of transparency, BBB WGA (20 standards), GiveWell / Giving What We Can (outcomes), national seals above.
- Press archives, court records (PACER in the US; national court portals), Wayback Machine for changed web claims (date each capture).
- Social media appeals and crowdfunding pages (GoFundMe, GlobalGiving, HelloAsso, betterplace) - record the claim and the date.

## Currency and periods
- State the original currency; convert at a stated rate and date.
- Report non-calendar year ends as filed. Never sum mismatched years without saying so.

---

<!-- file: references/us-form-990-guide.md -->

# Reading the US Form 990

## Getting the returns
1. Find the EIN (ProPublica name search, IRS TEOS, the organisation's donation page or Pub 78).
2. Open `https://projects.propublica.org/nonprofits/organizations/<EIN>` - it lists every return with its **object ID** and links to the PDF and XML.
3. Download the XML for every year in the period (ProPublica `download-xml?object_id=<id>` or the GivingTuesday data lake `https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/<object_id>_public.xml`).
4. Parse with `scripts/parse_990_xml.py`. Paper-filed or very old returns exist only as PDF scans - read those page by page and tag the figures as read from a scan.

If the sandbox cannot reach these hosts, open them in a real browser and save the raw file unchanged.

## What each part tells you

| Part / Schedule | What it gives you | Watch for |
|---|---|---|
| Part I | Summary: revenue, expenses, net assets, employee counts | Prior-year vs current-year columns |
| Part III | Programme accomplishments - the organisation's own description of where and what | Use it to locate spending (e.g. "teacher salaries in country X") |
| Part IV | Checklist of which schedules are required | **A schedule is only "missing" if its Part IV trigger is Yes** |
| Part V | Other IRS filings, foreign bank accounts (line 4) | |
| Part VI | Board size, independent members, family/business relationships among officers (line 2), delegation of management, policies (COI, whistleblower, retention), whether the board saw the return, how pay was set | |
| Part VII | Officers, directors, key employees and highest-paid staff with hours and pay from the organisation and related organisations | Part VII is **calendar-year reportable pay**; Part IX is fiscal-year expense incl. benefits - they differ legitimately |
| Part VIII | Revenue by type; contributions incl. government grants, fundraising events | Non-cash gifts; pledges booked when made |
| Part IX | Functional expenses: column A total, B programme, C management, D fundraising; line 3 grants to foreign organisations and individuals | 990-EZ has no functional split by law |
| Part X | Balance sheet: cash, investments, land/buildings (net), liabilities, net assets with/without donor restriction | Net assets are **not** cash in the bank |
| Part XI-XII | Reconciliation; whether accounts were compiled, reviewed or audited; single audit | |
| Schedule A | Public support test | |
| Schedule B | Major donors - **names are redacted in public copies** for most filers | |
| Schedule D | Endowments, donor-advised funds held, board-designated funds | |
| **Schedule F** | Activities outside the US by **world region** (not country): Part I offices, employees, expenditures; Part II grants to foreign organisations; Part III grants to foreign individuals (cash and non-cash) | Regions are broad ("South Asia" includes several countries). Public copies **never name foreign grantees**. Matching a row to a known partner is an inference |
| Schedule I | Grants to US organisations and individuals > $5,000 - names recipients | Useful for money sent to fiscal sponsors or "friends of" bodies |
| Schedule J | Pay detail where anyone's reportable plus other compensation exceeds $150,000 (also triggered by listed former officers and pay from unrelated organisations): base, bonus, other, deferred, non-taxable benefits; first-class travel, housing, tax gross-ups, how pay was set | |
| Schedule L | Transactions with interested persons: loans, grants, business transactions with officers, family members and their companies | |
| Schedule O | Free-text explanations - often the most informative part | |
| Schedule R | Related organisations: subsidiaries, controlled entities, disregarded entities, foreign affiliates | Watch for entities that move from "controlled" to "not controlled" |

## XML element names (2013+ e-file schema)
The parser looks these up by local name, so namespace prefixes do not matter.

- Header: `ReturnTypeCd`, `TaxPeriodBeginDt`, `TaxPeriodEndDt`, `Filer/EIN`, `BusinessNameLine1Txt`, `AmendedReturnInd`, `ReturnTs` (filing timestamp)
- Part I: `CYTotalRevenueAmt`, `CYTotalExpensesAmt`, `CYContributionsGrantsAmt`, `CYProgramServiceRevenueAmt`, `CYInvestmentIncomeAmt`, `CYGrantsAndSimilarPaidAmt`, `CYSalariesCompEmpBnftPaidAmt`, `TotalAssetsEOYAmt`, `TotalLiabilitiesEOYAmt`, `NetAssetsOrFundBalancesEOYAmt`, `TotalEmployeeCnt`
- Part IV triggers: `ForeignOfficeInd` (14a), `ForeignActivitiesInd` (14b), `MoreThan5000KToOrgInd` (15), `MoreThan5000KToIndividualsInd` (16), `ScheduleJRequiredInd`; Schedule L triggers (lines 25-28) include `LoanOutstandingInd`, `GrantToRelatedPersonInd`, `BusinessRlnWithOrgMemInd`, `BusinessRlnWithFamMemInd`, `BusinessRlnWithOfficerEntInd`
- Part VI: `GoverningBodyVotingMembersCnt`, `IndependentVotingMemberCnt`, `FamilyOrBusinessRlnInd` (line 2), `ConflictOfInterestPolicyInd`, `WhistleblowerPolicyInd`, `DocumentRetentionPolicyInd`, `Form990ProvidedToGvrnBodyInd` (line 11). Older schemas drop the `Ind`/abbreviations (e.g. `FamilyOrBusinessRelationship`, `Form990ProvidedToGoverningBody`); the parser checks both
- Part VII: `Form990PartVIISectionAGrp` with `PersonNm`, `TitleTxt`, `AverageHoursPerWeekRt`, `ReportableCompFromOrgAmt`, `ReportableCompFromRltdOrgAmt`, `OtherCompensationAmt`
- Part IX: `TotalFunctionalExpensesGrp` with `TotalAmt`, `ProgramServicesAmt`, `ManagementAndGeneralAmt`, `FundraisingAmt`
- Part X: `NoDonorRestrictionNetAssetsGrp` / `UnrestrictedNetAssetsGrp` (older), `LandBldgEquipBasisNetGrp`, each with `EOYAmt`
- Part XII: `FSAuditedInd`, `FederalGrantAuditRequiredInd`
- Schedule F: `IRS990ScheduleF` → `AccountActivitiesOutsideUSGrp` (Part I: `RegionTxt`, `OfficesCnt`, `EmployeeCnt`, `TypeOfActivitiesConductedTxt`, `RegionTotalExpendituresAmt`), `GrantsToOrgOutsideUSGrp` (Part II: `RegionTxt`, `PurposeOfGrantTxt`, `CashGrantAmt`, `NonCashAssistanceAmt`), `ForeignIndividualsGrantsGrp` (Part III - counts non-cash assistance as well as cash)
- 990-EZ: `TotalRevenueAmt`, `TotalExpensesAmt`, `NetAssetsOrFundBalancesEOYAmt`

Schemas change between years; if a field is missing, look at the raw XML before concluding the organisation left it blank.

## Common traps (innocent explanations to test)
- **Amended returns:** use the amendment for figures, the original for lateness; a restatement > 10% is worth a question.
- **Short years** (change of fiscal year) produce odd-looking pay or revenue - "$0 salary" in a short year is not "took no salary".
- **Duplicate returns** for one period can be an e-file correction, not two sets of books.
- **Multi-year pledges** inflate revenue in the year pledged and create apparent deficits later.
- **Board counts** at year end vs people serving during the year.
- **Part VII vs Part IX vs Schedule J pay** measure different things.
- **Schedule F regions** are broad and sometimes mislabelled; check Part III's own programme description.
- **Security reasons** for not naming foreign partners in fragile states are legitimate; record the reason.
- **Donor-advised funds** hide the original donor - a DAF sponsor (e.g. a community foundation) is the legal grantor.
- **Fiscal sponsorship:** a project's money may appear on the sponsor's return, not the project's.
- **Reserves held for a documented building or restricted purpose** are not "hoarding".

## Tracing money in from the funder side
Grantmakers' 990-PF (Part XIV "Supplementary information - grants and contributions paid" on the redesigned form from tax year 2022; Part XV on older returns) and public charities' Schedule I name recipients. Search the full-text of 990s (ProPublica full-text search) for the organisation's name or EIN to build a list of funders and amounts by year.

---

<!-- file: references/scoring-rubric.md -->

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

---

<!-- file: references/report-templates.md -->

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

---

<!-- file: references/ethics-and-safety.md -->

# Ethics, legal risk and safety

This research names real organisations and people. Getting a fact wrong, or phrasing a question as an accusation, can harm them and expose the author to legal claims. These rules exist to prevent that.

## Language
| Avoid | Use instead |
|---|---|
| fraud, scam, theft, embezzlement, stole, laundering | "unreconciled", "not disclosed", "the return does not say", "the figures do not match" |
| "they are hiding" | "the organisation has not published" |
| "misuse of funds" | "spending that donors may not expect, which the organisation discloses" / "a question for the organisation" |
| "illegal" | "the [law] requires X; the record does not show X" - only after confirming the requirement |
| "sitting in the bank" | "held as net assets (not all of it is cash)" |
| "took no salary" (from one $0 year) | "reported $0 in a [short / transition] year" |

Name the **record**, not the motive. Do not speculate about intentions.

## Facts, inferences and opinions
- Label every substantive claim. Keep the label next to the claim, not only in the methodology.
- Your opinions, if the user wants them, go in a separate, clearly labelled section.
- "No evidence of misuse was found" is a legitimate and important finding. Say it.

## Sources
- Primary records first. Press, social media, anonymous leaflets and partisan sources are context; attribute them and never let them carry a flag alone.
- Keep **harassment campaigns** and **politically motivated attacks** on an organisation or its founder clearly apart from documented findings, and say which is which.
- If you cannot open a source, do not describe its contents.

## Right of reply
- Before anything is published as a finding, the organisation receives specific questions tied to line items, the draft entry where possible, and a fixed reply period (commonly 10-14 days).
- Publish replies in full beside the entry. Record non-response factually ("did not respond by [date]"), never as an admission.
- The AI drafts the letter; **the human sends it**. Never claim it was sent.

## Privacy
- Do not name: private family members (even if a filing discloses a relationship, describe the role - "a family member of the CEO" - not the name, unless the person holds a public office in the organisation); beneficiaries; students; local staff; anonymous partners.
- No home addresses, personal phone numbers, dates of birth, or ID numbers.
- Officer names and pay on public tax returns are public by law; you may report them, but do not compile personal dossiers beyond the person's role in the organisation.
- Do not trace a person's private life, relationships, religion, ethnicity, health or immigration status.

## Safety in fragile and conflict settings
- Never publish operating locations below region/province level (schools, clinics, safe houses, offices) where staff or beneficiaries could be targeted.
- Do not name board members, staff or partners living under a hostile authority.
- Where staff or partners are detained or threatened, pause scrutiny of that operation and say so.
- Do not reference sanctions lists or link a person to sanctioned parties without direct evidence connecting them to the organisation.

## Fairness
- Apply the same rulebook to every organisation. Write it before scoring.
- Protected characteristics (ethnicity, religion, gender, nationality used as identity, sexual orientation) are never search terms, criteria or test inputs. If the population is defined by an attribute (e.g. "founded by people from country X"), define it neutrally and score a control group by rule.
- Credit what organisations do well. Include organisations that deliver, not only those with questions.
- If critics say the research is biased, record the criticism, what changed because of it, and any organisations added at their request with the outcome. Do not name critics without consent.

## Conflicts of interest
Before scoring, the author lists their own ties (employer, donations, board seats, business relationships, personal relationships, rivalries) to any organisation or person in scope. Search officer and trustee lists for the author's own name and organisations. Disclose every match on the first page. An entry where the author has a conflict should be judged by someone else.

## AI disclosure
State that the research is AI-assisted, which steps the AI did (search, extraction, arithmetic, drafting), which steps a human did (rules, checks, publication decisions), and that independent verification was run. Say plainly that AI can misread a line, miss a schedule or sound more certain than the evidence allows.

## Corrections
Publish a corrections address. Keep a dated revision log; keep superseded text so what was live on any date stays auditable.

## Not legal advice
This method describes a research practice. Before publishing anything that could be read as damaging to a named organisation or person, consider a review by a media lawyer in the relevant jurisdiction.

---

<!-- file: references/verification.md -->

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

---

<!-- file: templates/right-of-reply.md -->

# Right-of-reply letter (template)

Subject: Questions about [Organisation]'s public filings - reply requested by [date]

Dear [Chair / Executive Director],

I am preparing an independent, filings-based review of [Organisation] ([identifier, e.g. EIN / charity number]). It is based only on public records: [list - e.g. Forms 990 for FY2021-FY2025, the Charity Commission register, your annual reports]. It does not allege wrongdoing. Where your public record leaves a question open, I want to give you the chance to answer before anything is published.

I would be grateful for replies to the questions below by **[date - allow at least 10 working days]**. I will publish your reply in full alongside the review. If you do not reply, the review will say so, without drawing any conclusion from it.

**Specific questions** (each tied to a line in your filings)

1. [Form/accounts, year, part and line]: [the figure]. [The question - e.g. "Your annual report gives total expenses of $X for the same year. Which figure is correct, and what explains the difference?"]
2. ...

**Standard requests** (answer any that apply)

1. Audited or independently examined financial statements for each year since [year], or confirmation that none exist.
2. Complete filings as submitted, with all schedules.
3. Spending by country per year, reconciled to total expenses.
4. Recipients of funds outside your home country, or the reason they cannot be named.
5. Your board list with appointment dates, and your conflict-of-interest, whistleblower and document-retention policies.
6. Family or business relationships among directors, officers, key employees and contractors, and any related-party transactions.
7. Pay of the founder, the chief executive and any family member, by year and component, and how it was set.
8. One beneficiary figure per programme per year, with the counting method.
9. Your reserves policy.
10. Any external review, audit management letter, regulator correspondence or funder evaluation since [year].

The draft entry is attached [if applicable]. Corrections of fact are welcome at any time at [corrections address].

Yours sincerely,
[Name]
[Contact]

---
*Send this yourself. Record the date sent, the channel and the address used.*

---

<!-- file: templates/source-register.csv (column headers) -->

```csv
organisation,legal_name,jurisdiction,identifier,legal_form,period,record_type,raised,spent,net_assets_end,currency,scale,GEO,SCHED,INTERNAL,GOV,FAMILY,RESERVES,UNNAMED,CLAIMS,PAY,PUBLIC,placement,highest_flag_severity,flag_categories,evidence_S1,evidence_S2,evidence_S3,evidence_S4,coverage_years_read,confidence,contact,reply_status,score_basis_notes,sources
```

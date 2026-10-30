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

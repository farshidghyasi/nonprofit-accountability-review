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

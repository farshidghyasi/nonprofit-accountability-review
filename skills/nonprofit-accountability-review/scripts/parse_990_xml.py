#!/usr/bin/env python3
"""
Parse IRS Form 990 / 990-EZ / 990-PF e-file XML into tidy tables.

Usage:
    python3 parse_990_xml.py RETURN.xml [MORE.xml ...] --out OUTDIR
    python3 parse_990_xml.py path/to/folder_of_xml --out OUTDIR

Writes to OUTDIR:
    returns.csv     one row per return (header, Part I, IV triggers, VI, IX, X, XII,
                    plus computed checks)
    people.csv      Part VII Section A rows (officers, directors, key employees)
    schedule_f.csv  Schedule F Part I, II and III rows by region
    returns.json    everything above, nested per return

Standard library only. Elements are matched by local name, so XML namespaces
and minor schema-version differences do not matter. A blank cell means the
element was absent from the XML, not that the value was zero.
"""
import argparse
import csv
import json
import os
import sys
import xml.etree.ElementTree as ET


def local(tag):
    return tag.rsplit("}", 1)[-1]


def find_first(node, name):
    for el in node.iter():
        if local(el.tag) == name:
            return el
    return None


def text_of(node, name):
    el = find_first(node, name) if node is not None else None
    if el is None or el.text is None:
        return None
    return el.text.strip()


def num(node, name):
    t = text_of(node, name)
    if t is None:
        return None
    try:
        return float(t) if "." in t else int(t)
    except ValueError:
        return None


def flag(node, *names):
    t = None
    for name in names:
        t = text_of(node, name)
        if t is not None:
            break
    if t is None:
        return None
    return t.lower() in ("1", "true", "x", "yes")


def child_num(group, name):
    if group is None:
        return None
    return num(group, name)


def find_all(node, name):
    return [el for el in node.iter() if local(el.tag) == name]


def parse_return(path):
    tree = ET.parse(path)
    root = tree.getroot()
    header = find_first(root, "ReturnHeader")
    data = find_first(root, "ReturnData")
    if data is None:
        raise ValueError("no ReturnData element")

    form_type = text_of(header, "ReturnTypeCd")
    filer = find_first(header, "Filer")
    r = {
        "file": os.path.basename(path),
        "form": form_type,
        "ein": text_of(filer, "EIN"),
        "name": text_of(filer, "BusinessNameLine1Txt"),
        "tax_period_begin": text_of(header, "TaxPeriodBeginDt"),
        "tax_period_end": text_of(header, "TaxPeriodEndDt"),
        "return_timestamp": text_of(header, "ReturnTs"),
        "amended": flag(data, "AmendedReturnInd"),
    }

    if form_type and form_type.startswith("990EZ"):
        r.update({
            "total_revenue": num(data, "TotalRevenueAmt"),
            "total_expenses": num(data, "TotalExpensesAmt"),
            "net_assets_eoy": num(data, "NetAssetsOrFundBalancesEOYAmt"),
            "total_assets_eoy": child_num(find_first(data, "Form990TotalAssetsGrp"), "EOYAmt"),
            "total_liabilities_eoy": child_num(find_first(data, "SumOfTotalLiabilitiesGrp"), "EOYAmt"),
        })
    elif form_type and form_type.startswith("990PF"):
        r.update({
            "total_revenue": num(data, "TotalRevAndExpnssAmt"),
            "total_expenses": num(data, "TotalExpensesRevAndExpnssAmt"),
            "contributions_paid": num(data, "ContriPaidRevAndExpnssAmt"),
            "net_assets_eoy": num(data, "TotNetAstOrFundBalancesEOYAmt"),
        })
    else:
        func = find_first(data, "TotalFunctionalExpensesGrp")
        unres = find_first(data, "NoDonorRestrictionNetAssetsGrp")
        if unres is None:
            unres = find_first(data, "UnrestrictedNetAssetsGrp")
        land = find_first(data, "LandBldgEquipBasisNetGrp")
        r.update({
            # Part I
            "total_revenue": num(data, "CYTotalRevenueAmt"),
            "contributions": num(data, "CYContributionsGrantsAmt"),
            "program_service_revenue": num(data, "CYProgramServiceRevenueAmt"),
            "investment_income": num(data, "CYInvestmentIncomeAmt"),
            "total_expenses": num(data, "CYTotalExpensesAmt"),
            "grants_paid": num(data, "CYGrantsAndSimilarPaidAmt"),
            "salaries_benefits": num(data, "CYSalariesCompEmpBnftPaidAmt"),
            "total_assets_eoy": num(data, "TotalAssetsEOYAmt"),
            "total_liabilities_eoy": num(data, "TotalLiabilitiesEOYAmt"),
            "net_assets_eoy": num(data, "NetAssetsOrFundBalancesEOYAmt"),
            "employees": num(data, "TotalEmployeeCnt"),
            # Part IV triggers for Schedule F
            "iv_14a_foreign_office": flag(data, "ForeignOfficeInd"),
            "iv_14b_foreign_activities": flag(data, "ForeignActivitiesInd"),
            "iv_15_foreign_org_grants": flag(data, "MoreThan5000KToOrgInd"),
            "iv_16_foreign_indiv_grants": flag(data, "MoreThan5000KToIndividualsInd"),
            # Part VI
            "voting_members": num(data, "GoverningBodyVotingMembersCnt"),
            "independent_members": num(data, "IndependentVotingMemberCnt"),
            "family_business_relationship": flag(data, "FamilyOrBusinessRlnInd", "FamilyOrBusinessRelationship"),
            "coi_policy": flag(data, "ConflictOfInterestPolicyInd", "ConflictOfInterestPolicy"),
            "whistleblower_policy": flag(data, "WhistleblowerPolicyInd", "WhistleblowerPolicy"),
            "retention_policy": flag(data, "DocumentRetentionPolicyInd", "DocumentRetentionPolicy"),
            "return_to_board": flag(data, "Form990ProvidedToGvrnBodyInd", "Form990ProvidedToGoverningBody"),
            # Part IX
            "fx_total": child_num(func, "TotalAmt"),
            "fx_program": child_num(func, "ProgramServicesAmt"),
            "fx_management": child_num(func, "ManagementAndGeneralAmt"),
            "fx_fundraising": child_num(func, "FundraisingAmt"),
            # Part X
            "unrestricted_net_assets_eoy": child_num(unres, "EOYAmt"),
            "land_bldg_equip_net_eoy": child_num(land, "EOYAmt"),
            # Part XII
            "fs_audited": flag(data, "FSAuditedInd"),
            "single_audit_required": flag(data, "FederalGrantAuditRequiredInd"),
        })

    # Computed checks
    ta, tl, na = r.get("total_assets_eoy"), r.get("total_liabilities_eoy"), r.get("net_assets_eoy")
    if None not in (ta, tl, na):
        r["check_balance_sheet_diff"] = round(ta - tl - na, 2)
    if r.get("fx_total") and r.get("fx_program") is not None:
        r["program_share"] = round(r["fx_program"] / r["fx_total"], 4)
    exp = r.get("total_expenses")
    unr = r.get("unrestricted_net_assets_eoy")
    if exp and unr is not None:
        r["reserves_years_upper_bound"] = round((unr - (r.get("land_bldg_equip_net_eoy") or 0)) / exp, 2)

    # Part VII people
    people = []
    for g in find_all(data, "Form990PartVIISectionAGrp"):
        nm = text_of(g, "PersonNm") or text_of(g, "BusinessNameLine1Txt")
        rep = child_num(g, "ReportableCompFromOrgAmt") or 0
        rel = child_num(g, "ReportableCompFromRltdOrgAmt") or 0
        oth = child_num(g, "OtherCompensationAmt") or 0
        people.append({
            "file": r["file"], "ein": r["ein"], "tax_period_end": r["tax_period_end"],
            "person": nm, "title": text_of(g, "TitleTxt"),
            "hours": num(g, "AverageHoursPerWeekRt"),
            "reportable_org": rep, "reportable_related": rel, "other": oth,
            "total": rep + rel + oth,
        })
    if people:
        top = max(people, key=lambda p: p["total"])
        r["highest_paid_total"] = top["total"]
        r["highest_paid_title"] = top["title"]
        if exp:
            r["highest_paid_share_of_expenses"] = round(top["total"] / exp, 4)

    # Schedule F
    sched_f_rows = []
    sf = find_first(data, "IRS990ScheduleF")
    r["schedule_f_present"] = sf is not None
    if sf is not None:
        for part, grp in (("I", "AccountActivitiesOutsideUSGrp"),
                          ("II", "GrantsToOrgOutsideUSGrp"),
                          ("III", "ForeignIndividualsGrantsGrp")):
            for g in find_all(sf, grp):
                amount = (child_num(g, "RegionTotalExpendituresAmt")
                          if part == "I" else
                          (child_num(g, "CashGrantAmt") or 0) + (child_num(g, "NonCashAssistanceAmt") or 0))
                sched_f_rows.append({
                    "file": r["file"], "ein": r["ein"], "tax_period_end": r["tax_period_end"],
                    "part": part, "region": text_of(g, "RegionTxt"),
                    "activity_or_purpose": text_of(g, "TypeOfActivitiesConductedTxt") or text_of(g, "PurposeOfGrantTxt") or text_of(g, "TypeOfAssistanceTxt"),
                    "amount": amount,
                })
    r["schedule_l_present"] = find_first(data, "IRS990ScheduleL") is not None
    r["schedule_j_present"] = find_first(data, "IRS990ScheduleJ") is not None
    r["schedule_o_present"] = find_first(data, "IRS990ScheduleO") is not None
    return r, people, sched_f_rows


def write_csv(path, rows):
    if not rows:
        return
    keys = []
    for row in rows:
        for k in row:
            if k not in keys:
                keys.append(k)
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=keys)
        w.writeheader()
        w.writerows(rows)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("inputs", nargs="+", help="XML files or folders")
    ap.add_argument("--out", default="990_out", help="output folder")
    a = ap.parse_args()

    files = []
    for p in a.inputs:
        if os.path.isdir(p):
            files += [os.path.join(p, f) for f in sorted(os.listdir(p)) if f.lower().endswith(".xml")]
        else:
            files.append(p)
    os.makedirs(a.out, exist_ok=True)

    returns, people, sched_f, errors = [], [], [], []
    for f in files:
        try:
            r, ppl, sf = parse_return(f)
            returns.append(r)
            people += ppl
            sched_f += sf
        except Exception as e:  # keep going; report at the end
            errors.append(f"{f}: {e}")

    returns.sort(key=lambda r: (r.get("ein") or "", r.get("tax_period_end") or "", r.get("return_timestamp") or ""))
    write_csv(os.path.join(a.out, "returns.csv"), returns)
    write_csv(os.path.join(a.out, "people.csv"), people)
    write_csv(os.path.join(a.out, "schedule_f.csv"), sched_f)
    with open(os.path.join(a.out, "returns.json"), "w", encoding="utf-8") as f:
        json.dump({"returns": returns, "people": people, "schedule_f": sched_f, "errors": errors}, f, indent=2)

    print(f"Parsed {len(returns)} return(s), {len(people)} Part VII row(s), {len(sched_f)} Schedule F row(s) -> {a.out}")
    for e in errors:
        print("ERROR", e, file=sys.stderr)


if __name__ == "__main__":
    main()

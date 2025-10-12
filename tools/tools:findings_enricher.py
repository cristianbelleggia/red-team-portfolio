#!/usr/bin/env python3
"""
findings_enricher.py
A simple utility that scores/enriches findings from a CSV and exports JSON+CSV.

CSV input required columns: id,title,description
Optional column: severity_hint (low/medium/high)

Usage:
  python3 tools/findings_enricher.py -i data/findings.csv -o reports/findings_enriched.json
"""
import csv
import json
import argparse
from pathlib import Path

SCORE_MAP = {
    "critical": 90,
    "high": 70,
    "medium": 40,
    "low": 10,
    "unknown": 30
}

def guess_score(text, hint=None):
    # naive scoring: use hint if provided, otherwise simple keyword heuristics
    if hint:
        return SCORE_MAP.get(hint.lower(), SCORE_MAP["unknown"])
    t = text.lower()
    if "privilege" in t or "lateral" in t or "exfil" in t or "admin" in t:
        return 80
    if "sensitive" in t or "credentials" in t:
        return 75
    if "weak" in t or "misconfig" in t or "vulnerab" in t:
        return 50
    return SCORE_MAP["unknown"]

def enrich(input_csv, output_json, output_csv=None):
    findings = []
    with open(input_csv, newline='', encoding='utf-8') as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            fid = row.get("id") or row.get("Id") or str(len(findings)+1)
            title = row.get("title") or row.get("Title") or ""
            desc = row.get("description") or row.get("Description") or ""
            hint = row.get("severity_hint") or row.get("severity") or None
            score = guess_score(desc, hint)
            priority = "High" if score >= 70 else ("Medium" if score >= 40 else "Low")
            findings.append({
                "id": fid,
                "title": title,
                "description": desc,
                "severity_hint": hint,
                "score": score,
                "priority": priority
            })

    outp = Path(output_json)
    outp.parent.mkdir(parents=True, exist_ok=True)
    outp.write_text(json.dumps(findings, indent=2), encoding="utf-8")
    print(f"[+] Wrote enriched JSON to {outp}")

    if output_csv:
        keys = ["id","title","description","severity_hint","score","priority"]
        with open(output_csv, "w", newline='', encoding='utf-8') as fh:
            writer = csv.DictWriter(fh, fieldnames=keys)
            writer.writeheader()
            for r in findings:
                writer.writerow(r)
        print(f"[+] Wrote enriched CSV to {output_csv}")

def main():
    parser = argparse.ArgumentParser(description="Enrich findings CSV with scores/priorities")
    parser.add_argument("-i","--input", required=True, help="Input CSV path")
    parser.add_argument("-o","--output", required=True, help="Output JSON path")
    parser.add_argument("--out-csv", help="Also write enriched CSV")
    args = parser.parse_args()
    enrich(args.input, args.output, args.out_csv)

if __name__ == "__main__":
    main()

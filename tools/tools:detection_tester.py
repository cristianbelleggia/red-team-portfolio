#!/usr/bin/env python3
"""
detection_tester.py
Load simple Sigma-like YAML rules (very small subset) and test them against a plain text log file.

Rule format (YAML, minimal):
- title: Example
  id: ex-1
  detection:
    selection:
      Message|contains:
        - 'failed login'
        - 'authentication failure'

Usage:
  python3 tools/detection_tester.py -r detection/sigma_example.yml -l sample_logs/example.log -o reports/detection_matches.json
"""
import yaml
import argparse
from pathlib import Path
import json

def load_rules(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    # Support single-doc or list
    if isinstance(data, dict):
        return [data]
    return data

def match_rule_on_line(rule, line):
    det = rule.get("detection", {})
    selection = det.get("selection", {})
    for key, vals in selection.items():
        # support "Message|contains" style
        if "|contains" in key:
            for v in vals:
                if v.lower() in line.lower():
                    return True
    return False

def run(rules_path, log_path):
    rules = load_rules(rules_path)
    matches = []
    with open(log_path, 'r', errors='ignore', encoding='utf-8') as fh:
        for lineno, line in enumerate(fh, start=1):
            for rule in rules:
                if match_rule_on_line(rule, line):
                    matches.append({
                        "rule_id": rule.get("id"),
                        "rule_title": rule.get("title"),
                        "line_no": lineno,
                        "line": line.strip()
                    })
    return matches

def main():
    parser = argparse.ArgumentParser(description="Very small Sigma-like rule tester")
    parser.add_argument("-r","--rules", required=True, help="YAML rule file")
    parser.add_argument("-l","--log", required=True, help="Log file (text)")
    parser.add_argument("-o","--output", help="Output JSON file for matches")
    args = parser.parse_args()
    matches = run(args.rules, args.log)
    if args.output:
        out = Path(args.output)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(matches, indent=2), encoding='utf-8')
        print(f"[+] Wrote {len(matches)} matches to {out}")
    else:
        for m in matches:
            print(f"{m['rule_id']} [{m['line_no']}]: {m['line']}")

if __name__ == "__main__":
    main()

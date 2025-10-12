"""Benign: simple log parser to extract potentially interesting events.
This script is an example of automation/reporting for a portfolio:
- loads a plain-text log
- searches for indicative patterns (failed logins, escalation keywords)
- produces a small JSON report with counts and hit lines
USE ONLY FOR LEGAL AND AUTHORIZED ANALYSIS.
"""
import re, json, argparse
from collections import defaultdict

SUSPICIOUS_PATTERNS = {
    'failed_login': re.compile(r'failed login|authentication failure', re.I),
    'privilege_escalation': re.compile(r'privilege escalation|sudo:.*incorrect|su:.*failure', re.I),
    'recon': re.compile(r'nmap|masscan|enum|enumeration', re.I),
}

def analyze_log(path):
    counts = defaultdict(int)
    hits = defaultdict(list)
    with open(path, 'r', errors="ignore") as f:
        for i,line in enumerate(f, start=1):
            for key,pat in SUSPICIOUS_PATTERNS.items():
                if pat.search(line):
                    counts[key] += 1
                    hits[key].append({'line_no': i, 'line': line.strip()})
    return {'counts': counts, 'hits': hits}

def main():
    parser = argparse.ArgumentParser(description='Simple log parser example')
    parser.add_argument('logfile')
    parser.add_argument('-o','--out', default='log_report.json')
    args = parser.parse_args()
    report = analyze_log(args.logfile)
    # convert defaultdict to normal dict
    report['counts'] = dict(report['counts'])
    with open(args.out, 'w') as f:
        json.dump(report, f, indent=2)
    print(f'Report written to {args.out}')

if __name__ == '__main__':
    main()

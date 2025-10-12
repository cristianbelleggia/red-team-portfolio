# Executive Report — Two TryHackMe "Insane" Machines Assessment
**Author:** Cristian Belleggia  
**Date:** 2025-10-12

---

## Executive Summary
Two high-difficulty lab machines were analyzed to evaluate detection coverage and potential attack paths. Key findings include misconfigurations, insufficient detection of privileged account activity, and exposed web application errors. Immediate remediation and enhanced logging will significantly reduce risk.

---

## Top Findings
1. **Undocumented privilege paths** (Machine Alpha) — high risk: allows escalation from low-privileged account to domain-level.  
2. **Exposed web app internals** (Machine Omega) — medium/high risk: stack traces reveal technical details.  
3. **Insufficient detection and logging** — SOC cannot reliably detect anomalous behavior or attack attempts.

---

## Business Impact
- Potential compromise of administrative accounts, operational disruption, and data exposure.  
- Attackers exploiting web errors could pivot faster, increasing time to detection and remediation cost.

---

## Immediate Recommendations (Top 5)
1. Review and enforce least-privilege policies for all accounts and groups.  
2. Deploy centralized logging and endpoint telemetry (Sysmon) forwarded to SIEM.  
3. Implement SIEM detection rules for failed admin logins, SMB enumeration, and stacktrace exposure.  
4. Harden web applications: remove stack traces, enforce input validation, and WAF rules.  
5. Apply rate limiting and MFA on critical endpoints.

---

## Remediation Plan & Timeline
| Phase | Activity | Owner | ETA |
|-------|---------|-------|-----|
| 0–2 weeks | Deploy Sysmon & forward logs | IT/SecOps | 2 weeks |
| 2–4 weeks | SIEM rule implementation & tuning | SOC/SecOps | 2 weeks |
| 3–6 weeks | Review and remediate privileged accounts | IT Admins | 2–3 weeks |
| Ongoing | Quarterly AD assessment; web app review | SecOps | Continuous |

---

## KPIs to Track
- Number of privileged accounts with multi-group membership reduced by 50% in 3 months.  
- Mean Time to Detect lateral movement indicators < 30 minutes.  
- Number of critical web errors returned to clients = 0.

---

## Contact
- Author: Cristian Belleggia — cristian.redteam@gmail.com

---

## Notes
All findings are derived from authorized lab environments. No production systems or real client data were accessed.

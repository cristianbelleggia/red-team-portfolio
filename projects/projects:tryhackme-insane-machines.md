# Case Study — TryHackMe: Two "Insane" Machines
**Author:** Cristian Belleggia  
**Date:** 2025-10-12  
**Environment:** TryHackMe lab (authorized environment)

---

## Summary
This case study covers two high-difficulty "Insane" machines on TryHackMe. The goal was to simulate advanced reconnaissance, privilege escalation analysis, and post-exploitation detection in a controlled environment.

Machines analyzed:  
- **Machine Alpha** — simulated Windows Active Directory environment with multiple services exposed.  
- **Machine Omega** — web application with custom services and weak authentication mechanisms.

---

## 1) Context & Authorization
- Platform: TryHackMe (authorized lab).  
- Purpose: advanced training and evaluation of detection gaps, with focus on generating actionable SOC indicators.  
- Ethical note: no production systems were involved; all testing was in isolated lab environments.

---

## 2) Objectives
- **Machine Alpha:** identify lateral movement paths, privilege escalation possibilities, and generate detection rules for Kerberos/SMB/AD anomalies.  
- **Machine Omega:** analyze web application endpoints to derive Indicators of Compromise (IOC) and detection rules for WAF/SIEM to identify suspicious activity.

---

## 3) Methodology
1. **Reconnaissance:** service enumeration, banner grabbing, collecting visible configurations (lab only).  
2. **Detailed enumeration:** identify exposed services, user accounts, AD groups, and network endpoints.  
3. **Attack surface analysis:** review potential vectors (web, SMB, Kerberos).  
4. **Controlled simulation and evidence collection:** test movements in isolated lab, generate logs.  
5. **Log analysis & report generation:** use `log_parser.py` and `report_generator.py` to aggregate logs and produce HTML reports. Create Sigma-like detection rules and recommendations.

---

## 4) Machine Alpha — Technical Summary
**Description:** Windows AD lab with multiple users, groups, and SMB shares.  

**Activities (high-level):**
- SMB share enumeration and permissions review.  
- AD group membership review and lateral movement path identification.  
- Simulated post-exploitation to generate logs (lab only).

**Findings & Evidence:**
- Two privilege escalation paths identified via group memberships and excessive SMB permissions.  
- Sample logs (anonymized):
2025-10-10T12:05:01Z alpha SMB: Connection from 10.9.0.15 to \FILESRV\shared - user: svc_backup
2025-10-10T12:05:12Z alpha auth: failed login for user testuser from 10.9.0.20
2025-10-10T12:06:05Z alpha kerberos: TGS-REQ anomaly observed for user svc_admin

**Suggested Detection (high-level):**
- Alert on repeated failed logins to privileged accounts.  
- Detect SMB enumeration patterns.  
- Monitor Kerberos anomalies (unusual AS/TGS requests).

**Recommendations:**
- Apply least-privilege principle to all groups.  
- Audit and restrict SMB shares.  
- Deploy Sysmon and forward critical events to SIEM.  

---

## 5) Machine Omega — Technical Summary
**Description:** Web application with custom endpoints and weak authentication (lab).  

**Activities (high-level):**
- Collected headers and response patterns.  
- Tested input handling to generate anonymized logs.  
- Identified endpoints leaking technical information via errors.

**Findings & Evidence:**
- Endpoints return stack traces exposing internal details.  
- Anonymized log snippet:
2025-10-11T09:12:33Z omega HTTP: POST /login 200 - user: - - payload: {'username':'admin','password':'***'}
2025-10-11T09:12:35Z omega AppError: NullReferenceException at /api/user/details line 123
2025-10-11T09:12:40Z omega HTTP: 500 /api/user/details - stacktrace included


**Suggested Detection:**
- Alert on spikes of POST /login from single IPs (credential stuffing).  
- Alert on 500 responses containing "Exception" or "StackTrace".  
- Monitor unusual user agents and request rates.

**Recommendations:**
- Remove stack traces from responses; log internally.  
- Implement rate limiting and MFA on login endpoints.  
- Configure WAF to detect suspicious input patterns.

---

## 6) Sample Sigma-like Rules (Educational)
**Rule A — Multiple failed logins to privileged accounts:**  
> Trigger if >10 failed login events on admin accounts from same IP within 10 minutes.

**Rule B — Web app error stacktrace exposure:**  
> Trigger if HTTP 500 response contains 'Exception' or 'StackTrace'.

---

## 7) Conclusions
These two “Insane” machines demonstrate that even controlled lab environments can contain privilege escalation paths and detectable misconfigurations. Proper logging, detection rules, and least-privilege policies significantly reduce risk.

---

## Appendix
- Generated outputs: `reports/log_report.json` and `reports/log_report.html`.  
- Screenshots and diagrams anonymized in `assets/`.  
- All activities executed exclusively in authorized TryHackMe lab environments.

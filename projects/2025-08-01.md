# Write-up: Simulated AD Engagement (Lab)
**Date:** 2025-08-01
**Environment:** Personal lab / authorized environment

## Objective
Simulate privilege escalation paths and identify detection gaps on endpoints and SIEM.

## Tools used
- Kali (legitimate tooling for labs)
- BloodHound (AD graph analysis)
- PowerView (recon) *only used in authorized labs*

## Steps performed (summary)
1. Reconnaissance: enumerated users and shares.
2. Attack path analysis using BloodHound.
3. Post-exploitation simulation in a controlled environment and evidence collection.

## Results
- Identified 3 undocumented privilege paths.
- Suggested 5 immediate mitigations (policy adjustments, audit, segmentation).

## Lessons & remediation
- Implement detection for lateral movement techniques and monitor Kerberos/SMB logs.
- Reduce privileged account exposure and improve credential hygiene.

## Ethics note
All activities were performed in an authorized environment for educational purposes.

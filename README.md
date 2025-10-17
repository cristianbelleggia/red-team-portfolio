# Red Team Portfolio — Cristian Belleggia

This repository contains authorized lab write-ups, benign analysis tools, and example detection rules aimed at improving detection and response capabilities.

## About me
- **Name:** Cristian Belleggia  
- **Age:** 18  
- **Background:** Computer Science student (in progress) with strong programming skills and extensive hands-on experience on TryHackMe and HackTheBox.  
- **Contact:** cristian.redteam@gmail.com — https://www.linkedin.com/in/cristian-belleggia-170a20369/

## Certifications
- laurea informatica(in corso)
- eJPT — eLearnSecurity Junior Penetration Tester  


## Repository structure
- `projects/` — case studies and lab write-ups (authorized lab environments only).  
- `tools/` — safe automation and analysis utilities (no offensive payloads).  
- `detection/` — example Sigma‑like detection rules for SIEMs.  
- `reports/` — case study and executive report templates.  
- `assets/` — anonymized screenshots and diagrams.

## Quick example: run the log analysis tool
This repo contains a benign example script for parsing logs.

```bash
python3 tools/log_parser.py sample_logs/example.log -o reports/log_report.json

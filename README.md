# CAPSTONE PROJECT IVS-OWASP

IVS-OWASP (Intelligent Vulnerability Scanner) is a modular web vulnerability scanner developed as a cybersecurity capstone project.

The scanner is designed to detect common OWASP vulnerabilities such as:

- Cross-Site Scripting (XSS)
- SQL Injection (SQLi)

The project demonstrates how automated vulnerability scanners work by performing:

- Input discovery through web crawling
- Payload injection
- HTTP request handling
- Response analysis
- Vulnerability reporting

The scanner automatically identifies form inputs, injects malicious payloads, sends crafted requests to the target server, and analyzes the responses to detect vulnerabilities.

---

# Project Architecture

```text
                    ┌──────────────────────┐
                    │   Target Website     │
                    │  Vulnerable Flask App│
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │      scanner.py      │
                    │    Main Controller   │
                    └──────────┬───────────┘
                               │
        ┌──────────────────────┼──────────────────────┐
        │                      │                      │
        ▼                      ▼                      ▼
┌────────────────┐   ┌────────────────┐   ┌────────────────┐
│   crawler.py   │   │     xss.py     │   │    sqli.py     │
│ Input Discovery│   │   XSS Tester   │   │  SQLi Tester   │
└────────┬───────┘   └────────┬───────┘   └────────┬───────┘
         │                    │                    │
         ▼                    ▼                    ▼
┌──────────────────────────────────────────────────────────┐
│                     utils.py                             │
│           Payload & Test Case Generator                  │
└──────────────────────────────────────────────────────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   HTTP Requests      │
                    │ Payload Injection    │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Response Analysis    │
                    │ Vulnerability Detect │
                    └──────────────────────┘
```

---

# Features

- Automated input field discovery
- Reflected XSS detection
- Error-based SQL Injection detection
- Parameter-wise payload injection
- Modular architecture
- CLI-based scanner
- OWASP-inspired testing methodology
- Professional ASCII banner
- Structured scan phases
- Detailed vulnerability reporting

---

# Technologies Used

- Python 3
- Flask
- SQLite3
- Requests
- BeautifulSoup4

---

# Project Structure

```text
IVS-OWASP/
│
├── scanner.py       # Main controller
├── crawler.py       # Form/input discovery
├── utils.py         # Payload generation
├── xss.py           # XSS testing module
├── sqli.py          # SQL Injection testing module
├── test_app.py      # Vulnerable Flask application
├── users.db         # SQLite database
└── README.md
```

---

# Module Explanation

## scanner.py

The main controller responsible for:

- Starting scans
- Coordinating modules
- Running vulnerability tests
- Printing final reports

---

## crawler.py

Responsible for discovering:

- Forms
- Input fields
- Form methods
- Action URLs

Example discovered target:

```json
{
    "url": "http://target/login",
    "method": "post",
    "inputs": ["username", "password"]
}
```

---

## utils.py

Generates parameter-wise payload combinations for testing.

Example:

```json
{
    "username": "<script>alert(1)</script>",
    "password": "test"
}
```

This allows one-input-at-a-time fuzzing.

---

## xss.py

Tests for reflected Cross-Site Scripting vulnerabilities.

### Payloads Used

```text
<script>alert(1)</script>
<img src=x onerror=alert(1)>
```

### Detection Logic

- Inject payload
- Send HTTP request
- Check if payload is reflected in response

---

## sqli.py

Tests for SQL Injection vulnerabilities.

### Payloads Used

```text
' OR '1'='1
' OR 1=1--
" OR "1"="1
```

### Detection Logic

- Inject SQL payloads
- Analyze server response
- Detect SQL error messages

---

## test_app.py

A deliberately vulnerable Flask application created for testing the scanner.

### Vulnerabilities Included

#### SQL Injection

```python
query = f"SELECT * FROM users WHERE username = '{user}'"
```

#### Reflected XSS

```python
return f"Welcome {user}"
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/IVS-OWASP.git
cd IVS-OWASP
```

## Install Dependencies

```bash
pip install flask requests beautifulsoup4
```

---

# Running the Vulnerable Application

```bash
python3 test_app.py
```

The application will run on:

```text
http://127.0.0.1:5000
```

---

# Running the Scanner

```bash
python3 scanner.py http://127.0.0.1:5000
```

---

# Example Output

```text
=============================================================
[ PHASE 1 ] XSS Testing (OWASP A7)
=============================================================

[!!!] XSS Vulnerability Found
URL: http://127.0.0.1:5000/login
Payload: <script>alert(1)</script>

=============================================================
[ PHASE 2 ] SQL Injection Testing (OWASP A1)
=============================================================

[!!!] SQL Injection Vulnerability Found
URL: http://127.0.0.1:5000/login
Payload: ' OR 1=1--
```

---

# Scanner Workflow

```text
Discover Inputs
       ↓
Generate Payloads
       ↓
Inject Payloads
       ↓
Send HTTP Requests
       ↓
Analyze Responses
       ↓
Detect Vulnerabilities
       ↓
Generate Report
```

---

# OWASP Vulnerabilities Covered

| Vulnerability | Description |
|--------------|-------------|
| XSS | Detects reflected Cross-Site Scripting |
| SQLi | Detects error-based SQL Injection |

---

# Learning Objectives

This project demonstrates:

- Web application vulnerability scanning
- Automated security testing
- HTTP request manipulation
- Payload fuzzing
- Response analysis
- Secure coding awareness
- OWASP Top 10 concepts

---

# Future Improvements

- POST request support
- Multi-threaded scanning
- CSRF testing
- Authentication handling
- HTML reporting
- Stored XSS detection
- Advanced payload database
- WAF bypass techniques
- Export scan results to JSON/PDF

---

# Disclaimer

This project is created strictly for:

- Educational purposes
- Security research
- Authorized penetration testing

**Do NOT use this tool against systems without proper authorization.**

---

# Author

**Nithin P Mathew**

Cybersecurity Capstone Project

IVS - Intelligent Vulnerability Scanner (OWASP Inspired)

# License

This project is licensed under the MIT License.

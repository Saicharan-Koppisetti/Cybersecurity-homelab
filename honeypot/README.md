# SSH Honeypot - Fake Login Portal

A deception-based security tool that mimics a corporate admin login page to capture attacker credentials. Built using Python and Flask as part of a cybersecurity internship project.

---

## What it does

A honeypot is a fake system designed to look real. Anyone who tries to log in is already suspicious, so every attempt gets logged silently without the attacker knowing.

This project sets up a fake "Company Admin Portal" that:
- Looks like a legitimate internal system
- Accepts login attempts but never actually authenticates anyone
- Logs every attempt with timestamp, IP address, username, and password tried
- Always returns "Invalid credentials" so the attacker keeps trying

---

## How to run it

**Requirements:** Python 3, Flask

```bash
pip install flask
python honeypot.py
```

Then open your browser and go to `http://localhost:5000`

The server listens on all interfaces (`0.0.0.0:5000`) so it can be accessed from other devices on the same network too.

---

## Sample log output

```
[2026-03-31 03:03:39] SUSPICIOUS ACTIVITY | IP: 127.0.0.1 | Username: admin | Password: password123
[2026-03-31 03:03:55] SUSPICIOUS ACTIVITY | IP: 127.0.0.1 | Username: admin | Password: passwd
[2026-03-31 03:34:29] SUSPICIOUS ACTIVITY | IP: 127.0.0.1 | Username: Admin | Password: Passord1234
```

You can see repeated attempts, username variations (admin vs Admin), and common password guesses. This is exactly what a brute force or credential stuffing attack looks like in real logs.

---

## Files

| File | Purpose |
|------|---------|
| `honeypot.py` | Flask server, handles requests and logging |
| `templates/login.html` | Fake login page UI |
| `honeypot_log.txt` | Captured attack attempts |

> Note: Flask requires the HTML file to be inside a folder called `templates/`

---

## What the logs reveal

Looking at the captured attempts, you can spot real attack patterns:
- Same password tried multiple times back to back
- Attacker testing case variations (admin, Admin)
- Common default passwords used (password123, passwd, admin)
- Manual typing indicated by typos (PPassword, Passord)

In a real deployment, these logs feed into a SIEM or alerting system to trigger incident response.

---

## Limitation

Currently logs to a local text file. A production honeypot would forward logs to a centralized system in real time and also capture browser fingerprints, user agents, and geolocation data from the IP.

---

## Concepts covered

- Deception-based defense (honeypot technique)
- Credential harvesting detection
- Attacker behavior analysis
- Flask web framework
- Log analysis

---

## Environment

- Tested on Kali Linux (running as VM on Windows 11 host)
- Python 3, Flask

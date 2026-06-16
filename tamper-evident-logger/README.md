# Tamper-Evident Logging System

A Python-based logging system that detects if log entries have been modified or deleted. Built as part of a cybersecurity internship project.

---

## What it does

Most log files are just plain text. Anyone with file access can edit them and cover their tracks. This project solves that by chaining every log entry together using SHA256 hashes, similar to how a blockchain works.

Each log entry stores:
- Its own data (ID, timestamp, event type, description)
- The hash of the previous entry
- Its own hash calculated from all the above

If someone edits any entry, its hash changes, which breaks the chain. The verify function catches this immediately and tells you exactly which entry was tampered with.

---

## How to run it

**Requirements:** Python 3 (no external libraries needed)

```bash
python logger.py
```

You'll get a menu:
```
1. Add Log Entry
2. View All Logs
3. Verify Log Integrity
4. Exit
```

---

## Demo

**Normal run — all entries clean:**
```
[OK] Entry #1 - LOGIN - Clean
[OK] Entry #2 - TRANSACTION - Clean
[OK] Entry #3 - LOGOUT - Clean
[+] All logs verified. No tampering detected.
```

**After manually editing logs.json:**
```
[OK] Entry #1 - LOGIN - Clean
[OK] Entry #2 - TRANSACTION - Clean
[OK] Entry #3 - LOGOUT - Clean
[!!!] TAMPERED: Entry #4 has been modified!
[!!!] WARNING: Log tampering detected!
```

---

## Files

| File | Purpose |
|------|---------|
| `logger.py` | Main script with all functions |
| `logs.json` | Where log entries are stored |

---

## Limitation

Logs are stored locally. If an attacker has full system access, they could replace the entire file. In real SOC environments, logs are forwarded to a separate, write-protected SIEM system for this reason.

---

## Concepts covered

- SHA256 hashing
- Hash chaining (same concept as blockchain)
- Log integrity verification
- Forensic evidence handling

---

## Environment

- Tested on Kali Linux (running as VM on Windows 11 host)
- Python 3, standard library only

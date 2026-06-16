# Cybersecurity Home Lab

A collection of hands-on cybersecurity projects built and tested in a personal home lab environment. All projects were implemented from scratch in Python and tested on Kali Linux.

-----

## Projects

### 1. Tamper-Evident Logging System

A logging tool that uses SHA256 hash chaining to detect if any log entry has been modified or deleted after the fact. Think of it as a lightweight version of what SIEMs do to protect log integrity.

**Concepts:** Hashing, chain of custody, log integrity, forensics  
**Tools:** Python (standard library only)  
[View Project](./tamper-evident-logger/)

-----

### 2. Honeypot - Fake Login Portal

A deception-based trap disguised as a corporate admin portal. Silently logs every login attempt including IP, username, and password without the attacker knowing anything is being recorded.

**Concepts:** Honeypots, deception defense, attacker behavior, log analysis  
**Tools:** Python, Flask  
[View Project](./honeypot/)

-----

## Lab Environment

- Host: Windows 11 (Acer Predator Helios 300)
- VM: Kali Linux
- Network: Host-only / NAT setup

-----

## About

These projects were built during a cybersecurity internship focused on network security and defensive techniques. Goal was to understand how core security concepts actually work by building them, not just reading about them.
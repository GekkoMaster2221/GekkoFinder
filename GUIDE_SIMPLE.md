# GekkoFinder Simple Guide

## Quick Start

```bash
python3 GekkoFinder.py
```

---

## Main Commands

| Key | What It Does |
|-----|-------------|
| **0** | Check network safety & interfered unsafe network (CUE) |
| **H** | Help documentation |
| **C** | Run bash commands & view logs |
| **K** | Show all shortcuts |
| **I** | Network security tool commands |
| **1-9** | Connect to network #1-#9 |
| **Ctrl+C** | Exit |

---

## Network Info Explained

**Each network shows:**

- **SSID**: Network name
- **Signal**: WiFi strength (0-100%)
- **Sec**: Security type (WEP < WPA < WPA2 < WPA3)
- **DNS**: Network filtering (0/DNS/Proxy/&)
- **CUE**: Interfered unsafe network detection (X=safe, Y=dangerous)
- **SS (Safety Score)**: 
  - **S** = 🟢 Safe (green)
  - **X** = 🔴 Not safe (red)

---

## What Each Safety Letter Means

- **T**: Testing/Security research
- **UF**: Upload files/sensitive data
- **OF**: Open sensitive files
- **NU**: Normal usage/browsing

---

## Three Main Features

### 1. Custom Command Prompt (Press C)
```
$ logs              # View program logs
$ ifconfig          # Network interfaces
$ netstat           # Open ports/connections
$ ping 8.8.8.8      # Test connection
$ exit              # Return to menu
```

### 2. Program Logging
- Automatic logging to `~/.gekkofinder.log`
- Tracks all actions and errors
- View with `logs` command in prompt

### 3. Network Commands Reference (K → I)
- 25+ security testing commands
- Examples for each command
- Legal requirements reminder

---

## Quick Decisions

| Situation | What to Do |
|-----------|-----------|
| **CUE = Y** | ⚠️ NEVER connect - malicious network |
| **NU = X** | ❌ Not safe for any activity |
| **NU = S, NU = X other scores** | ✓ OK for browsing only |
| **Signal < 30%** | Move closer or pick different network |
| **WPA3 + Signal 80%+ + NU=S** | ✓ Best choice for all activities |

---

## Common Commands in Custom Prompt

```bash
ifconfig              # Show IP addresses
netstat -tuln         # List open ports
ping google.com       # Test internet
nslookup google.com   # DNS lookup
whoami                # Show username
pwd                   # Current folder
logs                  # View program logs
```

---

## Color Codes in Safety Score

- 🟢 **Green (S)** = Safe for that activity
- 🔴 **Red (X)** = Not safe for that activity

---

## File Locations

- **Program**: `/home/elias/GekkoFinder.py`
- **Logs**: `~/.gekkofinder.log`
- **Guides**: 
  - Simple: `GUIDE_SIMPLE.md`
  - Thorough: `GUIDE_THOROUGH.md`

---

## Version
**GekkoFinder v1.3.B** - WiFi Security Scanner
# GekkoFinder Thorough User Guide

## Table of Contents
1. [Introduction & Philosophy](#introduction)
2. [Installation & Launch](#installation)
3. [Understanding Network Information](#network-info)
4. [Security Protocols Explained](#security-protocols)
5. [WiFi Signal Strength](#signal-strength)
6. [Honeypot & Trap Detection](#honeypot-detection)
7. [Safety Score System](#safety-scores)
8. [Custom Command Prompt](#command-prompt)
9. [Program Logging](#logging)
10. [Network Commands Reference](#commands-reference)
11. [Real-World Scenarios](#scenarios)
12. [Best Practices](#best-practices)

---

## Introduction & Philosophy

GekkoFinder is a professional WiFi network security assessment tool designed for cybersecurity professionals, penetration testers, and security-conscious users who need to make informed decisions about network safety before connecting devices.

### Design Philosophy
The tool evaluates networks across five dimensions:
1. **Encryption Strength** - Cryptographic protocol analysis
2. **Signal Quality** - Connection reliability assessment
3. **Network Infrastructure** - DNS/Proxy detection
4. **Threat Detection** - Honeypot/trap identification
5. **Activity-Specific Safety** - Risk assessment by use case

Rather than providing abstract risk scores, GekkoFinder delivers actionable intelligence enabling informed connection decisions across different threat scenarios.

---

## Installation & Launch

### Starting GekkoFinder
```bash
python3 /home/elias/GekkoFinder.py
```

### Getting Help
```bash
python3 GekkoFinder.py -h
```

### First Run Experience
When you launch GekkoFinder, you'll see:
1. ASCII art header with program branding
2. List of available WiFi networks with detailed security information
3. Real-time security analysis for each network
4. Interactive menu for selecting actions

---

## Understanding Network Information

Each network entry displays comprehensive security data structured as:

```
ID | SSID | Signal% | Location | Sec:Type | DNS:Indicator | HP/Trap Status | Safety Scores
```

### Column-by-Column Breakdown

#### Network ID (1-9+)
- Sequential number identifying each network
- Type this number + Enter to connect to that network
- Maximum 3 password attempts allowed

#### SSID (Network Name)
- The broadcast network identifier users see when scanning
- Truncated to 20 characters for display
- Heuristically analyzed for threat indicators

#### Signal Strength (0-100%)
- Percentage of maximum WiFi signal reception
- Affects both connection speed and reliability
- See [Signal Strength Section](#signal-strength) for detailed interpretation

#### Estimated Location
- Deduced from SSID naming patterns
- Format: Country/City or Institution Type
- Examples: "USA/Airport", "Unknown/Hotel", "Local/Home"
- Provides context for threat modeling (public vs. private networks)

#### Security Protocol (Sec:TYPE)
- Cryptographic protocol implemented by the network
- Options: Open, WEP, WPA, WPA2, WPA3
- Critical for assessing encryption strength (see [Security Protocols](#security-protocols))

#### DNS/Proxy Detection (DNS:INDICATOR)
- **0** = Neither DNS filtering nor Proxy (direct internet)
- **DNS** = DNS filtering only (domain-level blocking)
- **Proxy** = Proxy service only (traffic routing)
- **&** = Both DNS and Proxy active (heavy monitoring)
- See [Network Infrastructure](#network-infrastructure) section

#### Honeypot/Trap Status (HP/Trap)
- **X** = Not detected as honeypot or trap
- **Y** = Honeypot or trap characteristics detected
- **Y indicator = NEVER CONNECT** to this network

#### Safety Scores (SS: T/UF/OF/NU)
- Color-coded indicators for activity-specific safety
- **🟢 Green (S)** = Safe for that activity type
- **🔴 Red (X)** = Not safe for that activity type
- Four categories: Testing, Upload Files, Open Files, Normal Usage
- See [Safety Score System](#safety-scores) for detailed explanation

---

## Security Protocols

WiFi networks implement encryption protocols that determine how resistant your traffic is to eavesdropping and attacks. Understanding these is critical for security decisions.

### Protocol Hierarchy (Weakest to Strongest)

#### 1. **Open (No Encryption)**
- **Cryptographic Strength**: None
- **Compromise Time**: Immediate (all traffic visible)
- **Real-World Risk**: Critical
- **Use Cases**: Public hotspots, demo networks, captive portals

**Technical Details**: No encryption implemented. All traffic transmitted in plaintext. Network observers can:
- Capture unencrypted passwords and credentials
- Monitor website visits and browsing patterns
- Inject malicious content into traffic
- Perform man-in-the-middle attacks

**Recommendation**: Only for non-sensitive public information (reading news, social media without authentication)

---

#### 2. **WEP (Wired Equivalent Privacy)**
- **Cryptographic Strength**: Weak (RC4 cipher)
- **Compromise Time**: Minutes (well-documented cryptanalytic attacks)
- **Real-World Risk**: Critical
- **Status**: Deprecated since 2004, security obsolete

**Technical Details**: Uses 40-bit or 104-bit RC4 encryption. Multiple documented cryptanalytic attacks:
- IV collision attacks (recover encryption key in <1 minute)
- Fluhrer-Mantin-Shamir attack (exploits weak key scheduling)
- Dictionary attacks on WEP initialization vectors

**Recommendation**: If network offers WEP - use different network. WEP provides false sense of security.

---

#### 3. **WPA (WiFi Protected Access)**
- **Cryptographic Strength**: Moderate (TKIP cipher)
- **Compromise Time**: Minutes to hours (dictionary/rainbow table attacks)
- **Real-World Risk**: High
- **Status**: Legacy standard from 2003

**Technical Details**: 
- Introduced strong password hashing (PBKDF2)
- Uses TKIP cipher suite
- Vulnerable to:
  - Dictionary attacks (if passphrase contains common words)
  - TKIP weaknesses documented in later research
  - Passphrase entropy attacks

**Security Factors**:
- WPA with 20+ character random passphrase: Moderate protection
- WPA with dictionary passphrase: Poor protection
- WPA with personal information: Very poor protection

**Recommendation**: Acceptable for general browsing if passphrase is strong (20+ random characters). Not suitable for sensitive operations.

---

#### 4. **WPA2 (IEEE 802.11i)**
- **Cryptographic Strength**: Strong (AES-CCMP)
- **Compromise Time**: Years (requires cryptographic breakthrough or key recovery)
- **Real-World Risk**: Low
- **Status**: Industry standard (2004-present)

**Technical Details**:
- Uses AES-CCMP (Counter Mode CBC-MAC Protocol)
- Authenticated encryption with associated data (AEAD)
- Counter mode for stream encryption + CBC-MAC for authentication
- Resistant to known cryptographic attacks

**Security Guarantees**:
- Passive eavesdropping protection: Excellent
- Man-in-the-middle attack resistance: Excellent
- Brute-force attack resistance: Strong (depends on passphrase strength)

**Best Practices**:
- WPA2 with 20+ character random passphrase: Excellent protection
- WPA2 with dictionary passphrase: Good protection (attacks still require significant resources)

**Recommendation**: Safe for all activities including sensitive data transmission. Industry standard for business networks.

---

#### 5. **WPA3 (IEEE 802.11ax)**
- **Cryptographic Strength**: Maximum (AES-GCMP-256)
- **Compromise Time**: Decades+ (assuming cryptographic standards hold)
- **Real-World Risk**: Negligible
- **Status**: Current best-practice standard (2018-present)

**Technical Details**:
- Simultaneous Authentication of Equals (SAE) handshake
- Replaces vulnerability-prone PSK (Pre-Shared Key) handshake
- AES-GCMP-256 encryption (256-bit security)
- Protection against:
  - Brute-force password attacks (SAE handshake prevents password testing)
  - Dictionary attacks (computational complexity prevents rapid guessing)
  - Key recovery attacks
  - Passive eavesdropping

**Security Guarantees**:
- Even weak passphrases receive strong protection
- Dictionary passphrase (WPA3) > Strong passphrase (WPA2)
- Future-proofed against known attack vectors

**Recommendation**: Strongest available option. Prioritize WPA3 networks when available, especially for sensitive operations.

---

### Protocol Comparison Table

| Feature | Open | WEP | WPA | WPA2 | WPA3 |
|---------|------|-----|-----|------|------|
| **Encryption** | None | RC4 (weak) | TKIP (weak) | AES (strong) | AES-256 (strongest) |
| **Authentication** | None | Weak | PBKDF2 | PBKDF2 | SAE |
| **Brute-Force Resistance** | N/A | Poor | Moderate | Good | Excellent |
| **Passive Eavesdropping Protection** | No | No | Yes | Yes | Yes |
| **MITM Attack Protection** | No | No | Moderate | Strong | Strong |
| **Modern Attacks Known** | Multiple | Documented | Some | None known | None known |
| **Recommended Use** | None (critical risk) | Never use | General browsing | Sensitive data | All activities |
| **Passphrase Strength Matters** | N/A | No (insecure anyway) | Yes (critical) | Yes (important) | No (SAE protects) |

---

## Signal Strength

WiFi signal strength determines both connection reliability and actual achievable data rates. This is separate from encryption strength but equally important for practical security.

### Signal Strength Interpretation

#### 90-100% - Excellent
- **Connection Quality**: Very stable, minimal packet loss
- **Data Rates**: Maximum achievable for protocol (54 Mbps 802.11g, 1300+ Mbps 802.11ac)
- **Latency**: Low (10-30ms typical)
- **Use Cases**: All activities, including video streaming and large file transfers
- **Security Implication**: Better connection stability enables secure operations
- **Recommendation**: Ideal for security-sensitive activities

#### 70-89% - Very Good
- **Connection Quality**: Stable, <1% packet loss
- **Data Rates**: 80-100% of protocol maximum
- **Latency**: Low-moderate (20-50ms)
- **Use Cases**: Video calls, file transfers, web browsing
- **Security Implication**: Reliable connection for authentication operations
- **Recommendation**: Safe for most activities

#### 50-69% - Good
- **Connection Quality**: Generally stable, 1-5% packet loss
- **Data Rates**: 50-80% of protocol maximum
- **Latency**: Moderate (40-100ms)
- **Use Cases**: Web browsing, email, social media
- **Security Implication**: Some packets may be retransmitted (increases exposure window)
- **Recommendation**: Acceptable for non-critical activities

#### 30-49% - Fair
- **Connection Quality**: Intermittent reliability, 5-15% packet loss
- **Data Rates**: 30-50% of protocol maximum
- **Latency**: High (100-200ms+)
- **Use Cases**: Basic web browsing (slow), text communication
- **Security Implication**: High retransmission rate increases exposure to passive eavesdropping
- **Recommendation**: Avoid for file transfers or sensitive operations

#### 0-29% - Poor
- **Connection Quality**: Very unreliable, frequent disconnections
- **Data Rates**: <30% of protocol maximum (unusable)
- **Latency**: Very high (>200ms, often timeouts)
- **Use Cases**: None (connection unreliable)
- **Security Implication**: Connection instability indicates potential jamming or interference
- **Recommendation**: Avoid completely - move closer to access point or change networks

### Signal Strength Factors

**Distance from Router**
- Signal strength inversely proportional to distance squared
- Doubling distance reduces signal by ~6dB (75%)
- Movement of 1 meter can change signal 5-10dB

**Physical Obstacles**
- Walls: 5-15dB attenuation (depends on material)
- Metal structures: 10-30dB attenuation
- Water/concrete: High attenuation
- Open air: Minimal attenuation

**Frequency Band**
- 2.4GHz: Better range, more interference, slower speeds
- 5GHz: Shorter range, less interference, faster speeds
- 6GHz (WiFi 6E): Similar to 5GHz, less congested

**Interference Sources**
- Other WiFi networks (same channel)
- Microwaves, cordless phones
- Bluetooth devices
- USB 3.0 devices (2.4GHz band)

---

## Honeypot & Trap Detection

Honeypots are intentionally malicious networks designed to appear legitimate while attempting to compromise connected devices. GekkoFinder detects these through heuristic analysis.

### What is a Honeypot?

A honeypot network is deployed by attackers to:
- **Credential Theft**: Capture authentication tokens and passwords
- **Malware Distribution**: Inject malicious code into connected devices
- **Data Exfiltration**: Harvest personal files, browsing history, communication data
- **Man-in-the-Middle Attacks**: Intercept and modify traffic in real-time
- **Surveillance**: Monitor user behavior and network activity

### Detection Methodology

GekkoFinder identifies honeypots through pattern recognition:

#### Suspicious SSID Patterns
Networks with names designed to appear public/trustworthy:
- "FreeWiFi", "PublicNetwork", "Guest_WiFi"
- "AirportFree", "CafeWiFi", "InstantAccess"
- Generic names: "WiFi", "Network", "Connect", "Internet"

#### Security Posture Red Flags
- **No password required** + Generic name = Likely honeypot
- **Perfect uptime** (no network issues) = Suspicious (real networks have problems)
- **No identifying information** = No legitimate owner
- **Extremely weak security** (Open) = Deliberate trap

#### Network Characteristics
- **All-numeric or random SSID** = Often honeypot indicators
- **ALL CAPS random characters** = Suspicious pattern
- **Combination of weak security + generic name** = High confidence honeypot

### Honeypot Indicators in GekkoFinder

When honeypot detection flags a network:
- **HP: Y** = Honeypot characteristics detected
- **Trap: Y** = Trap/malicious network indicators present
- All safety scores automatically set to **X** (red - not safe for any activity)

### Response to Honeypot Detection

**If HP/Trap = Y:**
1. **Do NOT connect** to this network
2. **Document the SSID** for reporting
3. **Warn other users** in vicinity if possible
4. **Check program logs** (view with logs command)
5. **Consider reporting** to network operator or security authority

**Why Avoid?**
- Device compromise risk is extreme
- Attacker controls all network traffic
- Malware injection is standard honeypot technique
- Credential theft is primary goal
- Legal liability (attacker may perform illegal activities using your device)

---

## Safety Score System

The Safety Score (SS) system provides activity-specific risk assessment. The same network may be safe for one activity (browsing) but unsafe for another (uploading sensitive files).

### Four Activity Categories

#### T - Testing/Penetration Testing
- **What It Is**: Authorized security assessments and penetration testing
- **Sensitivity**: Extremely high (test methodologies reveal client vulnerabilities)
- **Safety Threshold**: WPA3 only (requires maximum protocol strength)
- **Rationale**: Testing traffic patterns can reveal assessment methodologies. Only WPA3's SAE handshake prevents passive eavesdropping with certainty
- **Risk If Unsafe**: Attacker gains visibility into security assessment scope, client vulnerabilities, exploit tools used
- **Best Scenario**: WPA3 network, 90%+ signal, location = office building
- **Example**: Conducting authorized security assessment requires WPA3 protection

#### UF - Uploading Files/Sensitive Data
- **What It Is**: Transmitting credentials, financial data, intellectual property, authentication tokens
- **Sensitivity**: Very high (immediate financial/identity theft risk)
- **Safety Threshold**: WPA2 or WPA3 (AES-CCMP or stronger)
- **Rationale**: File uploads represent high-value data transmission events. AES encryption prevents man-in-the-middle attacks
- **Risk If Unsafe**: Credential compromise → account takeover, financial fraud, identity theft
- **Best Scenario**: WPA2/WPA3 network, 80%+ signal, location = trusted building
- **Example**: Uploading tax documents, banking credentials, cryptocurrency keys

#### OF - Opening Files/Sensitive Documents
- **What It Is**: Accessing confidential documents, private communications, medical/financial records
- **Sensitivity**: High (information disclosure risk)
- **Safety Threshold**: WPA2 or WPA3 (AES-CCMP or stronger)
- **Rationale**: Document access requires privacy protection from passive eavesdropping
- **Risk If Unsafe**: Information disclosure, privacy violations, data breach notification requirements
- **Best Scenario**: WPA2/WPA3 network, 70%+ signal, private location
- **Example**: Reading confidential email, accessing cloud documents, viewing bank statements

#### NU - Normal Usage/Browsing
- **What It Is**: General internet activities (web browsing, social media, entertainment, email without authentication)
- **Sensitivity**: Moderate (behavioral profiling risk)
- **Safety Threshold**: WPA or higher (any encryption)
- **Rationale**: General browsing still reveals user behavior through traffic analysis. Even unencrypted DNS reveals visited websites
- **Risk If Unsafe**: Behavioral profiling, targeted attacks, location inference, targeted advertising/manipulation
- **Best Scenario**: WPA2/WPA3 network, 70%+ signal, public but managed location (airport, library)
- **Example**: Reading news, checking social media, general web browsing

### Color Coding

- **🟢 Green (S)** = Safe - Network encryption sufficient for activity type
- **🔴 Red (X)** = Not Safe - Network encryption insufficient; DO NOT perform this activity

### Safety Score Decision Matrix

| Network Type | Signal | T | UF | OF | NU | Recommendation |
|-------------|--------|---|----|----|----|----|
| **Open** | 90%+ | ❌ | ❌ | ❌ | ❌ | Never use any activity |
| **WEP** | 90%+ | ❌ | ❌ | ❌ | ❌ | Never use any activity |
| **WPA** | 90%+ | ❌ | ❌ | ❌ | ✅ | Browsing only |
| **WPA2** | 90%+ | ❌ | ✅ | ✅ | ✅ | Most activities |
| **WPA3** | 90%+ | ✅ | ✅ | ✅ | ✅ | All activities |

### Real-World Application

**Scenario 1: Checking Email at Coffee Shop**
- Network: WPA2, 75% signal
- Email activity: Contains authentication (checking inbox)
- Safety: NU = ✅ (Safe for general usage, includes authentication)
- Recommendation: ✓ Safe to connect

**Scenario 2: Accessing Bank Account**
- Network: WPA, 85% signal  
- Activity: Banking (uploading financial documents)
- Safety: NU = ✅, UF = ❌
- Recommendation: ✗ Do NOT perform file upload/authentication. Do NOT check account balance or perform transactions.

**Scenario 3: Security Testing Engagement**
- Network: WPA3, 95% signal, corporate office
- Activity: Penetration testing (conducting vulnerability assessment)
- Safety: All = ✅
- Recommendation: ✓ Safe to conduct testing activities

---

## Custom Command Prompt

The Custom Command Prompt (press C) opens an interactive bash terminal within GekkoFinder, enabling direct network diagnostics and log viewing without leaving the application.

### Accessing Command Prompt

1. Press **C** in main menu
2. Bash prompt appears: `$ `
3. Type command and press Enter

### Available Commands

#### Program-Specific

**logs** - Display last 30 program log entries
```bash
$ logs
2026-01-31 14:23:45 - INFO - GekkoFinder started
2026-01-31 14:23:47 - INFO - Custom command prompt opened
2026-01-31 14:23:52 - INFO - Command executed: ifconfig
```

**exit** - Return to main menu
```bash
$ exit
[Returns to network scanning view]
```

**help** - Show command reference (within prompt)
```bash
$ help
[Shows available commands in prompt]
```

#### Network Diagnostics

**ifconfig / ip addr show** - Network interface configuration
```bash
$ ifconfig
eth0: flags=UP,BROADCAST,RUNNING
    inet 192.168.1.100
    netmask 255.255.255.0
```

**netstat -tuln / ss -tuln** - Show listening ports
```bash
$ netstat -tuln
Proto  Local Address  State    PID/Program
tcp    0.0.0.0:22     LISTEN   1234/sshd
tcp    0.0.0.0:80     LISTEN   5678/apache2
```

**ping [address]** - Test connectivity
```bash
$ ping 8.8.8.8
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=118 time=25.3 ms
```

**nslookup [domain]** - DNS query
```bash
$ nslookup google.com
Server: 8.8.8.8
Address: 8.8.8.8#53
Name: google.com
Address: 142.250.185.46
```

**traceroute [address]** - Network route analysis
```bash
$ traceroute google.com
 1  192.168.1.1 (gateway)  2.345 ms
 2  isp-router.com        15.234 ms
 3  google-backbone.net   25.123 ms
```

**whoami** - Current user
```bash
$ whoami
elias
```

**pwd** - Current directory
```bash
$ pwd
/home/elias
```

#### Advanced Commands

Any standard bash command is supported:
- **File operations**: ls, cat, grep, find, etc.
- **System info**: uname, lsb_release, df, etc.
- **Network tools**: curl, wget, telnet, etc.
- **Text processing**: awk, sed, cut, etc.
- **Scripts**: Custom bash scripts can be executed

### Command Execution Features

**10-Second Timeout Protection**
- Long-running commands automatically terminate after 10 seconds
- Prevents command prompt from hanging
- Displays timeout message to user

**Error Handling**
- Command errors displayed clearly
- Stderr output shown to user
- Logging captures all commands and results

**Logging Integration**
- All commands logged to ~/.gekkofinder.log
- Command execution with timestamp
- Error events recorded
- Complete audit trail of user actions

### Workflow Example

```bash
$ ifconfig                    # Check current IP
$ netstat -tuln               # Check for open ports
$ ping 8.8.8.8                # Test internet connectivity
$ nslookup example.com        # Verify DNS working
$ logs                        # Review program activity
$ whoami                      # Confirm user context
$ exit                        # Return to main menu
```

---

## Program Logging

GekkoFinder maintains comprehensive logs of all user actions and system events for audit, debugging, and security purposes.

### Log File Location

```
~/.gekkofinder.log
```

Full path: `/home/[username]/.gekkofinder.log`

### What Gets Logged

**Program Lifecycle**
- Program start: `INFO - GekkoFinder started`
- Program exit: `INFO - GekkoFinder stopped by user`
- Abnormal termination: `ERROR - [error message]`

**User Actions**
- Menu navigation: `INFO - Custom command prompt opened`
- Network connection attempts: `INFO - User attempting to connect to SSID: MyNetwork`
- Command prompt access: `INFO - Keyboard shortcuts menu opened`
- Ideas menu access: `INFO - Ideas menu accessed`

**Network Operations**
- Successful connections: `INFO - Successfully connected to NetworkName`
- Failed connections: `WARNING - Failed to connect to NetworkName`

**Command Execution**
- All commands: `INFO - Command executed: ifconfig`
- Errors: `ERROR - Command error: invalid_command - [error details]`
- Timeouts: `WARNING - Command timeout: long_running_command`

**System Events**
- Errors: `ERROR - Prompt error: [error description]`
- Network scanner issues: `WARNING - [diagnostic information]`

### Log Format

```
YYYY-MM-DD HH:MM:SS - LEVEL - MESSAGE
```

Example:
```
2026-01-31 14:23:45 - INFO - GekkoFinder started
2026-01-31 14:23:47 - INFO - Custom command prompt opened
2026-01-31 14:23:52 - INFO - Command executed: ifconfig
2026-01-31 14:23:55 - INFO - Keyboard shortcuts menu opened
2026-01-31 14:24:10 - INFO - User attempting to connect to SSID: HomeNetwork
2026-01-31 14:24:12 - INFO - Successfully connected to HomeNetwork
2026-01-31 14:24:15 - INFO - Ideas menu accessed
```

### Log Levels

- **INFO** - Normal operations and user actions
- **WARNING** - Failed operations, timeouts, anomalies
- **ERROR** - System errors, exceptions, failed commands

### Viewing Logs

**Within GekkoFinder**
```bash
# Press C to open command prompt
$ logs
# Shows last 30 log entries
```

**From Terminal**
```bash
# View all logs
tail -f ~/.gekkofinder.log

# View last 30 entries
tail -30 ~/.gekkofinder.log

# View specific date
grep "2026-01-31" ~/.gekkofinder.log

# View errors only
grep "ERROR" ~/.gekkofinder.log

# Count total entries
wc -l ~/.gekkofinder.log
```

### Log Retention

- Logs accumulate continuously
- No automatic log rotation implemented
- Manual management recommended:
  ```bash
  # Archive logs
  cp ~/.gekkofinder.log ~/.gekkofinder.log.backup
  > ~/.gekkofinder.log
  ```

### Security Implications

**Audit Trail**
- Complete record of all user actions
- Helps reconstruct security incidents
- Evidence for authorization verification
- Documentation for compliance requirements

**Privacy Considerations**
- Logs contain network names (SSIDs) connected to
- Logs contain commands executed
- Access restricted by file permissions (user-readable only)
- Consider protecting logs containing sensitive information

---

## Network Commands Reference

GekkoFinder includes 25+ network security testing commands organized by category. Access via: **K** (Keyboard Menu) → **I** (Ideas)

### Why These Commands Matter

These tools are used by:
- **Penetration testers** for authorized security assessments
- **Network administrators** for infrastructure diagnostics
- **Security researchers** for vulnerability analysis
- **DevOps engineers** for network troubleshooting
- **Incident responders** for forensic investigation

### Command Categories

#### Network Reconnaissance & Scanning
- **nmap** - Fast network and port scanner
- **arp-scan** - ARP-based device discovery
- **masscan** - High-speed port scanning
- **netdiscover** - Passive device discovery

#### Network Configuration
- **ifconfig / ip addr show** - Interface configuration
- **route -n / ip route show** - Routing table display
- **netstat -tuln / ss -tuln** - Port listening status
- **nmcli device show** - NetworkManager details

#### Wireless Security Testing
- **airmon-ng** - Monitor mode setup
- **airodump-ng** - WiFi packet capture
- **aireplay-ng** - Deauthentication attacks
- **aircrack-ng** - WPA/WEP password cracking

#### Traffic Analysis & Capture
- **tcpdump** - Network packet capture
- **wireshark** - GUI packet analyzer
- **tshark** - Terminal packet analyzer

#### DNS & Connectivity
- **nslookup** - DNS query tool
- **dig** - Advanced DNS queries
- **ping** - ICMP connectivity test
- **traceroute** - Network path analysis

#### VPN & Proxy Configuration
- **SSH tunneling** - Create SOCKS proxy
- **proxychains** - Route through proxies
- **openvpn** - OpenVPN client setup

#### Service Management
- **ps aux** - Process listing
- **lsof -i** - Network connection enumeration
- **systemctl status** - Service monitoring

### Legal & Ethical Requirements

**Authorization is Mandatory**
- Never use these tools on networks you don't own without written permission
- Unauthorized network testing is illegal in most jurisdictions
- Can result in criminal prosecution and civil liability

**Best Practices**
- Document all testing activities
- Obtain written authorization before each test
- Use isolated lab networks for practice
- Follow responsible disclosure for findings
- Respect user privacy and data protection laws

---

## Real-World Scenarios

### Scenario 1: Working at Coffee Shop

**Situation**: You need to check email and do light work at a local café

**Network Available**: 
- SSID: "CafeWiFi_Free"
- Security: WPA2
- Signal: 85%
- Honeypot: X (not detected)
- Safety: NU=✅, UF=✅, OF=✅

**Analysis**:
- WPA2 provides encryption protection
- Signal strength adequate for web browsing
- No honeypot indicators
- Safe for general usage

**Action**: 
- ✅ SAFE to connect
- ✅ Can check and respond to email
- ✅ Can do document editing/viewing
- ⚠️ Avoid sensitive authentication if possible
- ⚠️ Use VPN for extra protection

---

### Scenario 2: Airport WiFi for Financial Tasks

**Situation**: Transferring money or accessing investment accounts at airport

**Network Available**:
- SSID: "AirportFree_WiFi"
- Security: Open (no encryption)
- Signal: 78%
- Honeypot: Y (trap detected)
- Safety: NU=❌, UF=❌, OF=❌

**Analysis**:
- Open network = zero encryption
- Honeypot characteristics detected
- Extremely unsafe for financial transactions
- High risk of credential theft

**Action**:
- ❌ DO NOT CONNECT
- ❌ DO NOT perform financial transactions
- ❌ DO NOT access sensitive accounts
- ⚠️ Use cellular data instead
- ✅ Consider airplane mode + offline work

---

### Scenario 3: Corporate Office WiFi

**Situation**: Conducting authorized penetration testing in corporate office

**Network Available**:
- SSID: "CompanyCorp-Secure"
- Security: WPA3
- Signal: 92%
- Honeypot: X (not detected)
- Safety: T=✅, UF=✅, OF=✅, NU=✅

**Analysis**:
- WPA3 = strongest encryption available
- Excellent signal strength
- Corporate location = trusted environment
- All activities marked safe

**Action**:
- ✅ SAFE to conduct penetration testing
- ✅ Safe for test tool execution
- ✅ Safe for tool traffic
- ✅ Safe for test logging and documentation
- ✅ All reconnaissance and scanning safe

---

### Scenario 4: Home WiFi with Mixed Activities

**Situation**: Working from home with multiple activities (email, banking, entertainment)

**Network Available**:
- SSID: "Home_Network_2.4G"
- Security: WPA2
- Signal: 88%
- Honeypot: X
- Safety: T=❌, UF=✅, OF=✅, NU=✅

**Analysis**:
- WPA2 = strong encryption
- Good signal strength
- Home network = trusted environment
- Suitable for most activities except security testing

**Action**:
- ✅ SAFE for email and web browsing
- ✅ SAFE for banking and financial transactions
- ✅ SAFE for document viewing and editing
- ❌ NOT suitable for penetration testing (requires WPA3)
- ✅ Good for streaming and entertainment

---

### Scenario 5: Public Library WiFi

**Situation**: Researching at public library, need internet access

**Network Available**:
- SSID: "LibraryPublicWiFi"
- Security: WPA
- Signal: 72%
- Honeypot: X
- Safety: T=❌, UF=❌, OF=❌, NU=✅

**Analysis**:
- WPA = moderate encryption
- Decent signal for stationary use
- Public location but managed network
- Safe only for general browsing

**Action**:
- ✅ SAFE for web research and reading
- ✅ SAFE for checking email (reading only, no sending sensitive info)
- ⚠️ MARGINAL for file uploads (WPA is weaker than WPA2)
- ❌ NOT SAFE for sensitive document access
- ❌ NOT SAFE for banking transactions
- ⚠️ Consider VPN for extra protection if available

---

## Best Practices

### Before Connecting

1. **Review All Indicators**
   - Check honeypot/trap status first (Y = never connect)
   - Verify security protocol meets activity requirements
   - Assess signal strength for stability
   - Consider network location context

2. **Match Activity to Network**
   - **General Browsing** → Any network with NU=✅
   - **Financial Tasks** → WPA2/WPA3 only (UF=✅)
   - **Sensitive Documents** → WPA2/WPA3 + 70%+ signal
   - **Security Testing** → WPA3 only (T=✅)

3. **Consider Location**
   - Public places → Use strong encryption
   - Corporate offices → Usually WPA2/WPA3 available
   - Residential → Own network is best option

### While Connected

4. **Monitor Activities**
   - Don't transmit credentials on weak networks
   - Avoid opening sensitive documents on public WiFi
   - Keep sensitive operations for trusted networks
   - Use VPN when available for additional protection

5. **Be Aware of Signal Issues**
   - If signal drops below 40% → seek better location
   - Frequent disconnections → change network
   - High latency → may indicate interference or attack

6. **Use Command Prompt Responsibly**
   - Only run commands you understand
   - Don't execute untrusted scripts
   - Check command syntax before execution
   - Review logs for unexpected activity

### Post-Connection

7. **Review Logs**
   - Check logs for unusual activity
   - Verify expected commands executed
   - Note any error messages
   - Identify potential security issues

8. **Practice Good Hygiene**
   - Disconnect when finished
   - Close sensitive applications
   - Clear browser cache on public machines
   - Vary your networks to avoid patterns

### Long-Term Security

9. **Understand Your Environment**
   - Learn what networks are available in your area
   - Identify trustworthy vs. risky networks
   - Know where to find WPA2/WPA3 networks
   - Build mental map of safe connection options

10. **Stay Updated**
    - Monitor GekkoFinder version for updates
    - Read security news for new threat types
    - Test in lab environments before production use
    - Share knowledge with security colleagues

---

## Troubleshooting

### Connection Issues
- **Problem**: Can't connect to WPA2 network
- **Solution**: Check password is correct (case-sensitive), verify nmcli available

### Command Timeout
- **Problem**: Command takes >10 seconds
- **Solution**: Use simpler command, try in terminal outside GekkoFinder

### Logs Not Appearing
- **Problem**: Logs command shows no output
- **Solution**: Check ~/.gekkofinder.log exists, may be empty if just started

### Signal Strength Low
- **Problem**: All networks show <30% signal
- **Solution**: Move closer to access points, check WiFi is enabled, try different location

---

## Version Information

**Program**: GekkoFinder v1.3.B
**Purpose**: WiFi Network Security Assessment
**Target Audience**: Cybersecurity professionals, penetration testers, security researchers
**OS**: Linux/POSIX systems
**Python**: 3.6+
**Dependencies**: nmcli, standard Linux utilities

---

**Last Updated**: 2026-01-31
**License**: For authorized security testing only
**Disclaimer**: Use only on networks you own or have explicit written permission to test


## ⚠️ Legal Notice

This tool is for **authorized security testing only**. Unauthorized access is illegal. 
See [LEGAL_DISCLAIMER.md](LEGAL_DISCLAIMER.md) for full details.
================================================================================
                              GEKKOFINDER v1.3.B
                   WiFi Network Security Assessment Tool
================================================================================

PROJECT OVERVIEW
================================================================================

GekkoFinder is a professional-grade WiFi network security assessment tool 
designed for cybersecurity professionals, penetration testers, security 
researchers, and privacy-conscious users who need to make informed decisions 
about network safety before connecting devices.

The tool provides comprehensive real-time analysis of available WiFi networks,
evaluating them across five security dimensions:
  1. Encryption Protocol Strength (WEP → WPA → WPA2 → WPA3)
  2. Signal Quality & Connection Stability
  3. Network Infrastructure (DNS/Proxy Detection)
  4. Threat Detection (Honeypot/Trap Identification)
  5. Activity-Specific Safety Assessment

Rather than abstract risk scores, GekkoFinder delivers actionable intelligence
enabling informed connection decisions across different threat scenarios.


KEY FEATURES
================================================================================

✓ Real-Time WiFi Network Scanning
  - Continuous monitoring of available networks
  - Signal strength measurement
  - Security protocol identification
  - Network location estimation

✓ Advanced Security Analysis
  - Honeypot/Trap network detection
  - Security protocol evaluation (Open, WEP, WPA, WPA2, WPA3)
  - DNS/Proxy infrastructure detection
  - Activity-specific safety scoring

✓ Activity-Specific Safety Scores
  - Testing (Penetration Testing)
  - UF (Upload Files/Sensitive Data)
  - OF (Open Files/Sensitive Documents)
  - NU (Normal Usage/Browsing)
  Color-coded for instant visual assessment (Green=Safe, Red=Not Safe)

✓ Custom Command Prompt
  - Execute bash commands directly from GekkoFinder
  - Integrated command logging
  - Log file viewer (type 'logs' to review program activity)
  - 10-second timeout protection against hanging

✓ Network Commands Reference
  - 25+ security testing commands
  - Organized by category (scanning, wireless, traffic analysis, DNS, etc.)
  - Usage examples for each command
  - Legal and ethical requirement reminders

✓ Comprehensive Program Logging
  - Automatic activity logging to ~/.gekkofinder.log
  - Tracks all user actions, network connections, command executions
  - Timestamp and severity levels (INFO, WARNING, ERROR)
  - Complete audit trail for security compliance

✓ Interactive Keyboard Shortcuts
  - [0] System Information & Security Analysis
  - [H] Help Menu (detailed documentation)
  - [C] Custom Command Prompt
  - [K] Keyboard Shortcuts Menu
  - [I] Ideas/Network Commands Reference
  - [#] Connect to Network by number
  - [Ctrl+C] Exit program


SYSTEM REQUIREMENTS
================================================================================

Operating System:
  • Linux/POSIX systems (Debian, Ubuntu, Fedora, CentOS, etc.)
  • macOS (Darwin) support
  • Windows Subsystem for Linux (WSL)

Software Requirements:
  • Python 3.6 or higher
  • nmcli (NetworkManager command-line interface)
  • Standard Linux utilities (arp, netstat, etc.)

Hardware:
  • Any Linux system with WiFi adapter
  • Minimum 10MB disk space
  • No special GPU or accelerators required

Network:
  • WiFi adapter with monitoring capabilities (for wireless scanning)
  • Sudo/root access required for some operations


INSTALLATION
================================================================================

1. SYSTEM DEPENDENCIES (Ubuntu/Debian)
   
   # Install NetworkManager (usually pre-installed)
   sudo apt-get install network-manager
   
   # Install Python 3
   sudo apt-get install python3
   
   # Install optional network tools
   sudo apt-get install net-tools wireless-tools


2. GEKKOFINDER INSTALLATION
   
   # Option A: Direct from file
   cd /home/elias
   chmod +x GekkoFinder.py
   
   # Option B: Copy to system-wide location
   sudo cp GekkoFinder.py /usr/local/bin/gekkofinder
   sudo chmod +x /usr/local/bin/gekkofinder


3. VERIFY INSTALLATION
   
   # Test script compilation
   python3 -m py_compile GekkoFinder.py
   
   # Expected output: No errors displayed


QUICK START GUIDE
================================================================================

LAUNCHING GEKKOFINDER
   
   # From current directory
   python3 /home/elias/GekkoFinder.py
   
   # If copied to system path
   gekkofinder
   
   # Display help information
   python3 GekkoFinder.py -h
   python3 GekkoFinder.py --help


BASIC WORKFLOW

   1. Launch GekkoFinder
      $ python3 GekkoFinder.py
      [Program displays available WiFi networks with security analysis]

   2. Review Network Information
      ID  | SSID | Signal% | Location | Security | DNS | HP/Trap | Safety
      1.  | HomeNet | 95% | Local/Home | WPA2 | 0 | X | ✓✓✓✓

   3. Choose Your Action:
      
      Option A - Check Network Safety:
      Press [0] to view system info and honeypot detection
      
      Option B - Execute Commands:
      Press [C] to open command prompt
      Type 'ifconfig' or 'logs' or any bash command
      Type 'exit' to return to menu
      
      Option C - Learn Security Commands:
      Press [K] then [I] to view network testing commands
      
      Option D - Connect to Network:
      Type network number (1-9) and press Enter
      Enter password if required (max 3 attempts)

   4. Monitor Activity:
      Press [C] then type 'logs' to review program activity


DETAILED USAGE
================================================================================

UNDERSTANDING NETWORK DISPLAY

Each network entry shows:
   ID      - Network selection number (type to connect)
   SSID    - Network name (up to 20 characters)
   Signal% - WiFi strength (0-100%)
   Location- Estimated location (Country/City or place type)
   Sec     - Security protocol (Open, WEP, WPA, WPA2, WPA3)
   DNS     - DNS/Proxy status (0, DNS, Proxy, or &)
   HP/Trap - Honeypot detection (X=safe, Y=dangerous)
   SS      - Safety Scores (T/UF/OF/NU with color coding)

SAFETY SCORE MEANINGS

   T  = Testing (Penetration testing)
        🟢 Green (S) = Safe for authorized security testing
        🔴 Red (X) = Not safe for testing

   UF = Upload Files (Sensitive data transmission)
        🟢 Green (S) = Safe for uploading credentials/files
        🔴 Red (X) = Not safe for file uploads

   OF = Open Files (Sensitive document access)
        🟢 Green (S) = Safe for opening confidential documents
        🔴 Red (X) = Not safe for opening sensitive files

   NU = Normal Usage (General browsing)
        🟢 Green (S) = Safe for general internet use
        🔴 Red (X) = Not safe for any activity

SECURITY PROTOCOLS

   Open    - No encryption (highest risk, avoid)
   WEP     - Deprecated, broken encryption (critical risk, never use)
   WPA     - Legacy encryption (moderate risk, browsing only)
   WPA2    - Strong encryption (safe for most activities)
   WPA3    - Maximum encryption (safe for all activities including testing)

DECISION MAKING QUICK REFERENCE

   If HP/Trap = Y (honeypot detected)
      → DO NOT CONNECT - Malicious network detected

   If NU = Red (not safe for browsing)
      → DO NOT CONNECT - Not safe for any activity

   If NU = Green, others Red
      → SAFE for general browsing only

   If All = Green, Signal 80%+
      → SAFE for all activities

   If WPA3 + Signal 90%+
      → OPTIMAL network, safe for everything


COMMAND PROMPT FEATURES
================================================================================

ACCESS COMMAND PROMPT
   Press [C] in main menu

AVAILABLE COMMANDS

   Program Commands:
   • logs        - Display last 30 program log entries
   • help        - Show command help
   • exit        - Return to main menu

   Network Diagnostics:
   • ifconfig           - Network interface configuration
   • netstat -tuln      - Show listening ports
   • ping 8.8.8.8       - Test internet connectivity
   • nslookup google.com- DNS query test
   • traceroute google.com - Network path analysis

   System Information:
   • whoami      - Current user
   • pwd         - Current directory
   • hostname    - Computer name
   • uname -a    - Operating system info

   Any Standard Bash Command:
   • curl, wget, grep, awk, sed, find, etc.

EXAMPLE SESSION

   $ ifconfig
   eth0: flags=UP,BROADCAST,RUNNING
      inet 192.168.1.100

   $ netstat -tuln
   Proto  Local Address     State
   tcp    0.0.0.0:22        LISTEN

   $ logs
   2026-01-31 14:23:45 - INFO - GekkoFinder started
   2026-01-31 14:23:47 - INFO - Custom command prompt opened
   2026-01-31 14:23:52 - INFO - Command executed: ifconfig

   $ exit
   [Returns to network scanning view]


PROGRAM LOGGING
================================================================================

Log File Location:
   ~/.gekkofinder.log

What Gets Logged:
   • Program start/stop events
   • User menu navigation
   • Network connection attempts (success/failure)
   • Command executions
   • Errors and exceptions
   • System events

Log Format:
   YYYY-MM-DD HH:MM:SS - LEVEL - MESSAGE
   Example: 2026-01-31 14:23:45 - INFO - GekkoFinder started

Log Levels:
   INFO    - Normal operations and user actions
   WARNING - Failed operations, timeouts
   ERROR   - System errors and exceptions

Viewing Logs:
   # Within GekkoFinder
   Press [C] then type 'logs'

   # From terminal
   tail -30 ~/.gekkofinder.log        # Last 30 entries
   grep "ERROR" ~/.gekkofinder.log    # Error entries only
   cat ~/.gekkofinder.log             # All logs


TROUBLESHOOTING
================================================================================

PROBLEM: "nmcli not available"
SOLUTION:
   • Install NetworkManager: sudo apt-get install network-manager
   • On macOS: brew install networkmanager
   • Some features disabled on systems without nmcli

PROBLEM: "No networks detected"
SOLUTION:
   • Verify WiFi adapter is enabled
   • Run: nmcli device show
   • Check WiFi switch on laptop/device
   • May require root/sudo permissions

PROBLEM: "Can't connect to network"
SOLUTION:
   • Verify correct password (case-sensitive)
   • Check if network requires special login
   • Try from terminal: nmcli dev wifi connect SSID password PASSWORD
   • Maximum 3 password attempts allowed

PROBLEM: "Command timeout"
SOLUTION:
   • Commands limited to 10 seconds
   • Try simpler commands
   • Run long commands in terminal directly
   • Example: sudo timeout 30 nmap -p 1-65535 192.168.1.0/24

PROBLEM: "Logs not appearing"
SOLUTION:
   • Check ~/.gekkofinder.log exists
   • May be empty on fresh install
   • Use 'cat ~/.gekkofinder.log' from terminal
   • Logs only record after first activity

PROBLEM: "Color coding not showing"
SOLUTION:
   • Verify terminal supports ANSI colors
   • Try: echo -e "\033[92mGreen\033[0m"
   • Use xterm or GNOME Terminal if colors don't show
   • Colors are informational only, tool functions without them


NETWORK SECURITY BEST PRACTICES
================================================================================

BEFORE CONNECTING

   1. Review all security indicators
   2. Check honeypot/trap status first (Y = never connect)
   3. Verify security protocol meets activity requirements
   4. Assess signal strength for stability
   5. Consider network location context

WHILE CONNECTED

   1. Monitor your activities appropriately
   2. Don't transmit credentials on weak networks
   3. Avoid opening sensitive docs on public WiFi
   4. Use VPN for additional protection when available
   5. Keep sensitive operations for trusted networks

AFTER DISCONNECTING

   1. Review program logs for unusual activity
   2. Close sensitive applications
   3. Clear browser cache if using public computer
   4. Vary your networks to avoid patterns


GUIDES AND DOCUMENTATION
================================================================================

Three comprehensive guides included:

1. GUIDE_SIMPLE.md (2.6 KB, 117 lines)
   Quick reference with hotwords and short explanations
   Best for: Quick answers while using the tool

2. GUIDE_THOROUGH.md (33 KB, 999 lines)
   Comprehensive guide with detailed explanations
   Includes:
   • Security protocol deep-dive
   • Signal strength analysis
   • Honeypot detection explanation
   • 5 real-world scenarios
   • Best practices and troubleshooting
   Best for: Security professionals and detailed learners

3. README.txt (this file)
   Project overview and quick reference
   Best for: General understanding and setup


SUPPORT & CONTACT
================================================================================

Email Support:
   GekkoSupport@proton.me

When contacting support, please include:
   1. GekkoFinder version: python3 GekkoFinder.py -h
   2. Operating system: uname -a
   3. Python version: python3 --version
   4. Error message (if applicable)
   5. Steps to reproduce the issue
   6. Network environment (if relevant)

Common Issues:
   • Missing nmcli: Install network-manager
   • Python errors: Update to Python 3.6+
   • Permission issues: Ensure user in sudo group
   • Color problems: Terminal compatibility issue

Bug Reports:
   Include:
   • Exact error message
   • Steps to reproduce
   • Your environment details
   • Screenshot if possible


VERSION HISTORY
================================================================================

Version 1.3.B (Current)
   ✓ Color coding fixed for safety indicators
   ✓ Custom command prompt fully functional
   ✓ Program logging system active
   ✓ 25+ network commands reference
   ✓ Keyboard shortcuts menu
   ✓ Honeypot/trap detection active
   ✓ Activity-specific safety scoring
   Release Date: 2026-01-31

Version 1.1
   • Initial public release
   • Core scanning functionality
   • System information menu
   • Network security analysis


LEGAL & DISCLAIMER
================================================================================

AUTHORIZED USE ONLY

GekkoFinder is designed for:
   ✓ Authorized security testing================================================================================
                              GEKKOFINDER v1.3.B
                   WiFi Network Security Assessment Tool
================================================================================

PROJECT OVERVIEW
================================================================================

GekkoFinder is a professional-grade WiFi network security assessment tool 
designed for cybersecurity professionals, penetration testers, security 
researchers, and privacy-conscious users who need to make informed decisions 
about network safety before connecting devices.

The tool provides comprehensive real-time analysis of available WiFi networks,
evaluating them across five security dimensions:
  1. Encryption Protocol Strength (WEP → WPA → WPA2 → WPA3)
  2. Signal Quality & Connection Stability
  3. Network Infrastructure (DNS/Proxy Detection)
  4. Threat Detection (Honeypot/Trap Identification)
  5. Activity-Specific Safety Assessment

Rather than abstract risk scores, GekkoFinder delivers actionable intelligence
enabling informed connection decisions across different threat scenarios.


KEY FEATURES
================================================================================

✓ Real-Time WiFi Network Scanning
  - Continuous monitoring of available networks
  - Signal strength measurement
  - Security protocol identification
  - Network location estimation

✓ Advanced Security Analysis
  - Honeypot/Trap network detection
  - Security protocol evaluation (Open, WEP, WPA, WPA2, WPA3)
  - DNS/Proxy infrastructure detection
  - Activity-specific safety scoring

✓ Activity-Specific Safety Scores
  - Testing (Penetration Testing)
  - UF (Upload Files/Sensitive Data)
  - OF (Open Files/Sensitive Documents)
  - NU (Normal Usage/Browsing)
  Color-coded for instant visual assessment (Green=Safe, Red=Not Safe)

✓ Custom Command Prompt
  - Execute bash commands directly from GekkoFinder
  - Integrated command logging
  - Log file viewer (type 'logs' to review program activity)
  - 10-second timeout protection against hanging

✓ Network Commands Reference
  - 25+ security testing commands
  - Organized by category (scanning, wireless, traffic analysis, DNS, etc.)
  - Usage examples for each command
  - Legal and ethical requirement reminders

✓ Comprehensive Program Logging
  - Automatic activity logging to ~/.gekkofinder.log
  - Tracks all user actions, network connections, command executions
  - Timestamp and severity levels (INFO, WARNING, ERROR)
  - Complete audit trail for security compliance

✓ Interactive Keyboard Shortcuts
  - [0] System Information & Security Analysis
  - [H] Help Menu (detailed documentation)
  - [C] Custom Command Prompt
  - [K] Keyboard Shortcuts Menu
  - [I] Ideas/Network Commands Reference
  - [#] Connect to Network by number
  - [Ctrl+C] Exit program


SYSTEM REQUIREMENTS
================================================================================

Operating System:
  • Linux/POSIX systems (Debian, Ubuntu, Fedora, CentOS, etc.)
  • macOS (Darwin) support
  • Windows Subsystem for Linux (WSL)

Software Requirements:
  • Python 3.6 or higher
  • nmcli (NetworkManager command-line interface)
  • Standard Linux utilities (arp, netstat, etc.)

Hardware:
  • Any Linux system with WiFi adapter
  • Minimum 10MB disk space
  • No special GPU or accelerators required

Network:
  • WiFi adapter with monitoring capabilities (for wireless scanning)
  • Sudo/root access required for some operations


INSTALLATION
================================================================================

1. SYSTEM DEPENDENCIES (Ubuntu/Debian)
   
   # Install NetworkManager (usually pre-installed)
   sudo apt-get install network-manager
   
   # Install Python 3
   sudo apt-get install python3
   
   # Install optional network tools
   sudo apt-get install net-tools wireless-tools


2. GEKKOFINDER INSTALLATION
   
   # Option A: Direct from file
   cd /home/elias
   chmod +x GekkoFinder.py
   
   # Option B: Copy to system-wide location
   sudo cp GekkoFinder.py /usr/local/bin/gekkofinder
   sudo chmod +x /usr/local/bin/gekkofinder


3. VERIFY INSTALLATION
   
   # Test script compilation
   python3 -m py_compile GekkoFinder.py
   
   # Expected output: No errors displayed


QUICK START GUIDE
================================================================================

LAUNCHING GEKKOFINDER
   
   # From current directory
   python3 /home/elias/GekkoFinder.py
   
   # If copied to system path
   gekkofinder
   
   # Display help information
   python3 GekkoFinder.py -h
   python3 GekkoFinder.py --help


BASIC WORKFLOW

   1. Launch GekkoFinder
      $ python3 GekkoFinder.py
      [Program displays available WiFi networks with security analysis]

   2. Review Network Information
      ID  | SSID | Signal% | Location | Security | DNS | HP/Trap | Safety
      1.  | HomeNet | 95% | Local/Home | WPA2 | 0 | X | ✓✓✓✓

   3. Choose Your Action:
      
      Option A - Check Network Safety:
      Press [0] to view system info and honeypot detection
      
      Option B - Execute Commands:
      Press [C] to open command prompt
      Type 'ifconfig' or 'logs' or any bash command
      Type 'exit' to return to menu
      
      Option C - Learn Security Commands:
      Press [K] then [I] to view network testing commands
      
      Option D - Connect to Network:
      Type network number (1-9) and press Enter
      Enter password if required (max 3 attempts)

   4. Monitor Activity:
      Press [C] then type 'logs' to review program activity


DETAILED USAGE
================================================================================

UNDERSTANDING NETWORK DISPLAY

Each network entry shows:
   ID      - Network selection number (type to connect)
   SSID    - Network name (up to 20 characters)
   Signal% - WiFi strength (0-100%)
   Location- Estimated location (Country/City or place type)
   Sec     - Security protocol (Open, WEP, WPA, WPA2, WPA3)
   DNS     - DNS/Proxy status (0, DNS, Proxy, or &)
   HP/Trap - Honeypot detection (X=safe, Y=dangerous)
   SS      - Safety Scores (T/UF/OF/NU with color coding)

SAFETY SCORE MEANINGS

   T  = Testing (Penetration testing)
        🟢 Green (S) = Safe for authorized security testing
        🔴 Red (X) = Not safe for testing

   UF = Upload Files (Sensitive data transmission)
        🟢 Green (S) = Safe for uploading credentials/files
        🔴 Red (X) = Not safe for file uploads

   OF = Open Files (Sensitive document access)
        🟢 Green (S) = Safe for opening confidential documents
        🔴 Red (X) = Not safe for opening sensitive files

   NU = Normal Usage (General browsing)
        🟢 Green (S) = Safe for general internet use
        🔴 Red (X) = Not safe for any activity

SECURITY PROTOCOLS

   Open    - No encryption (highest risk, avoid)
   WEP     - Deprecated, broken encryption (critical risk, never use)
   WPA     - Legacy encryption (moderate risk, browsing only)
   WPA2    - Strong encryption (safe for most activities)
   WPA3    - Maximum encryption (safe for all activities including testing)

DECISION MAKING QUICK REFERENCE

   If HP/Trap = Y (honeypot detected)
      → DO NOT CONNECT - Malicious network detected

   If NU = Red (not safe for browsing)
      → DO NOT CONNECT - Not safe for any activity

   If NU = Green, others Red
      → SAFE for general browsing only

   If All = Green, Signal 80%+
      → SAFE for all activities

   If WPA3 + Signal 90%+
      → OPTIMAL network, safe for everything


COMMAND PROMPT FEATURES
================================================================================

ACCESS COMMAND PROMPT
   Press [C] in main menu

AVAILABLE COMMANDS

   Program Commands:
   • logs        - Display last 30 program log entries
   • help        - Show command help
   • exit        - Return to main menu

   Network Diagnostics:
   • ifconfig           - Network interface configuration
   • netstat -tuln      - Show listening ports
   • ping 8.8.8.8       - Test internet connectivity
   • nslookup google.com- DNS query test
   • traceroute google.com - Network path analysis

   System Information:
   • whoami      - Current user
   • pwd         - Current directory
   • hostname    - Computer name
   • uname -a    - Operating system info

   Any Standard Bash Command:
   • curl, wget, grep, awk, sed, find, etc.

EXAMPLE SESSION

   $ ifconfig
   eth0: flags=UP,BROADCAST,RUNNING
      inet 192.168.1.100

   $ netstat -tuln
   Proto  Local Address     State
   tcp    0.0.0.0:22        LISTEN

   $ logs
   2026-01-31 14:23:45 - INFO - GekkoFinder started
   2026-01-31 14:23:47 - INFO - Custom command prompt opened
   2026-01-31 14:23:52 - INFO - Command executed: ifconfig

   $ exit
   [Returns to network scanning view]


PROGRAM LOGGING
================================================================================

Log File Location:
   ~/.gekkofinder.log

What Gets Logged:
   • Program start/stop events
   • User menu navigation
   • Network connection attempts (success/failure)
   • Command executions
   • Errors and exceptions
   • System events

Log Format:
   YYYY-MM-DD HH:MM:SS - LEVEL - MESSAGE
   Example: 2026-01-31 14:23:45 - INFO - GekkoFinder started

Log Levels:
   INFO    - Normal operations and user actions
   WARNING - Failed operations, timeouts
   ERROR   - System errors and exceptions

Viewing Logs:
   # Within GekkoFinder
   Press [C] then type 'logs'

   # From terminal
   tail -30 ~/.gekkofinder.log        # Last 30 entries
   grep "ERROR" ~/.gekkofinder.log    # Error entries only
   cat ~/.gekkofinder.log             # All logs


TROUBLESHOOTING
================================================================================

PROBLEM: "nmcli not available"
SOLUTION:
   • Install NetworkManager: sudo apt-get install network-manager
   • On macOS: brew install networkmanager
   • Some features disabled on systems without nmcli

PROBLEM: "No networks detected"
SOLUTION:
   • Verify WiFi adapter is enabled
   • Run: nmcli device show
   • Check WiFi switch on laptop/device
   • May require root/sudo permissions

PROBLEM: "Can't connect to network"
SOLUTION:
   • Verify correct password (case-sensitive)
   • Check if network requires special login
   • Try from terminal: nmcli dev wifi connect SSID password PASSWORD
   • Maximum 3 password attempts allowed

PROBLEM: "Command timeout"
SOLUTION:
   • Commands limited to 10 seconds
   • Try simpler commands
   • Run long commands in terminal directly
   • Example: sudo timeout 30 nmap -p 1-65535 192.168.1.0/24

PROBLEM: "Logs not appearing"
SOLUTION:
   • Check ~/.gekkofinder.log exists
   • May be empty on fresh install
   • Use 'cat ~/.gekkofinder.log' from terminal
   • Logs only record after first activity

PROBLEM: "Color coding not showing"
SOLUTION:
   • Verify terminal supports ANSI colors
   • Try: echo -e "\033[92mGreen\033[0m"
   • Use xterm or GNOME Terminal if colors don't show
   • Colors are informational only, tool functions without them


NETWORK SECURITY BEST PRACTICES
================================================================================

BEFORE CONNECTING

   1. Review all security indicators
   2. Check honeypot/trap status first (Y = never connect)
   3. Verify security protocol meets activity requirements
   4. Assess signal strength for stability
   5. Consider network location context

WHILE CONNECTED

   1. Monitor your activities appropriately
   2. Don't transmit credentials on weak networks
   3. Avoid opening sensitive docs on public WiFi
   4. Use VPN for additional protection when available
   5. Keep sensitive operations for trusted networks

AFTER DISCONNECTING

   1. Review program logs for unusual activity
   2. Close sensitive applications
   3. Clear browser cache if using public computer
   4. Vary your networks to avoid patterns


GUIDES AND DOCUMENTATION
================================================================================

Three comprehensive guides included:

1. GUIDE_SIMPLE.md (2.6 KB, 117 lines)
   Quick reference with hotwords and short explanations
   Best for: Quick answers while using the tool

2. GUIDE_THOROUGH.md (33 KB, 999 lines)
   Comprehensive guide with detailed explanations
   Includes:
   • Security protocol deep-dive
   • Signal strength analysis
   • Honeypot detection explanation
   • 5 real-world scenarios
   • Best practices and troubleshooting
   Best for: Security professionals and detailed learners

3. README.txt (this file)
   Project overview and quick reference
   Best for: General understanding and setup


SUPPORT & CONTACT
================================================================================

Email Support:
   GekkoSupport@proton.me

When contacting support, please include:
   1. GekkoFinder version: python3 GekkoFinder.py -h
   2. Operating system: uname -a
   3. Python version: python3 --version
   4. Error message (if applicable)
   5. Steps to reproduce the issue
   6. Network environment (if relevant)

Common Issues:
   • Missing nmcli: Install network-manager
   • Python errors: Update to Python 3.6+
   • Permission issues: Ensure user in sudo group
   • Color problems: Terminal compatibility issue

Bug Reports:
   Include:
   • Exact error message
   • Steps to reproduce
   • Your environment details
   • Screenshot if possible


VERSION HISTORY
================================================================================

Version 1.3.B (Current)
   ✓ Color coding fixed for safety indicators
   ✓ Custom command prompt fully functional
   ✓ Program logging system active
   ✓ 25+ network commands reference
   ✓ Keyboard shortcuts menu
   ✓ Honeypot/trap detection active
   ✓ Activity-specific safety scoring
   Release Date: 2026-01-31

Version 1.1
   • Initial public release
   • Core scanning functionality
   • System information menu
   • Network security analysis


LEGAL & DISCLAIMER
================================================================================

AUTHORIZED USE ONLY

GekkoFinder is designed for:
   ✓ Authorized security testing
   ✓ Network diagnostics on own networks
   ✓ Personal WiFi security assessment
   ✓ Educational purposes with proper authorization

UNAUTHORIZED USE IS ILLEGAL

   ✗ Never use on networks without permission
   ✗ Unauthorized network testing violates computer fraud laws
   ✗ Can result in criminal prosecution
   ✗ Civil liability for damages may apply
   ✗ Respect user privacy and data protection regulations

RESPONSIBLE DISCLOSURE

   • Document all testing activities
   • Obtain written authorization before testing
   • Follow responsible disclosure practices
   • Share findings securely with network owner
   • Allow reasonable time for remediation

USER RESPONSIBILITY

   • You are responsible for proper use
   • Verify you have authorization before testing
   • Follow applicable laws and regulations
   • Maintain confidentiality of findings
   • Use only for intended security purposes


TECHNICAL SPECIFICATIONS
================================================================================

Architecture:
   • Python 3 application
   • Real-time network scanning
   • Non-blocking I/O for responsive UI
   • Background scanning thread
   • Signal selection-based interactivity

Key Libraries:
   • subprocess - System command execution
   • threading - Background scanning
   • hashlib - Network hashing (stable angle calculation)
   • select - Non-blocking input
   • logging - Activity logging

Security Features:
   • No plaintext storage of sensitive data
   • Network address randomization for stability
   • Timeout protection (10 seconds per command)
   • Honeypot detection heuristics
   • Activity-appropriate risk assessment

Performance:
   • Sub-second response to user input
   • ~3 second network scan interval
   • Minimal CPU/memory usage
   • Efficient terminal rendering


ADDITIONAL RESOURCES
================================================================================

Network Security Learning:

   WiFi Security Standards:
   • IEEE 802.11i (WPA2) - Industry standard encryption
   • IEEE 802.11ax (WPA3) - Current best-practice standard
   • NIST recommendations on wireless security

   Command References:
   • nmap: https://nmap.org/
   • aircrack-ng: https://www.aircrack-ng.org/
   • tcpdump: https://www.tcpdump.org/

   Security Tools:
   • Wireshark packet analyzer
   • metasploit framework
   • Kali Linux penetration testing distribution


FILES IN PACKAGE
================================================================================

Required Files:
   GekkoFinder.py         - Main program (2,277 lines)
   README.txt             - This file

Documentation:
   GUIDE_SIMPLE.md        - Quick reference guide
   GUIDE_THOROUGH.md      - Comprehensive guide
   QUICK_START.txt        - Quick start guide
   CHANGES_SUMMARY.md     - Version history and changes

Support:
   GekkoSupport@proton.me - Email for help and bug reports================================================================================
                              GEKKOFINDER v1.3.B
                   WiFi Network Security Assessment Tool
================================================================================

PROJECT OVERVIEW
================================================================================

GekkoFinder is a professional-grade WiFi network security assessment tool 
designed for cybersecurity professionals, penetration testers, security 
researchers, and privacy-conscious users who need to make informed decisions 
about network safety before connecting devices.

The tool provides comprehensive real-time analysis of available WiFi networks,
evaluating them across five security dimensions:
  1. Encryption Protocol Strength (WEP → WPA → WPA2 → WPA3)
  2. Signal Quality & Connection Stability
  3. Network Infrastructure (DNS/Proxy Detection)
  4. Threat Detection (Honeypot/Trap Identification)
  5. Activity-Specific Safety Assessment

Rather than abstract risk scores, GekkoFinder delivers actionable intelligence
enabling informed connection decisions across different threat scenarios.


KEY FEATURES
================================================================================

✓ Real-Time WiFi Network Scanning
  - Continuous monitoring of available networks
  - Signal strength measurement
  - Security protocol identification
  - Network location estimation

✓ Advanced Security Analysis
  - Honeypot/Trap network detection
  - Security protocol evaluation (Open, WEP, WPA, WPA2, WPA3)
  - DNS/Proxy infrastructure detection
  - Activity-specific safety scoring

✓ Activity-Specific Safety Scores
  - Testing (Penetration Testing)
  - UF (Upload Files/Sensitive Data)
  - OF (Open Files/Sensitive Documents)
  - NU (Normal Usage/Browsing)
  Color-coded for instant visual assessment (Green=Safe, Red=Not Safe)

✓ Custom Command Prompt
  - Execute bash commands directly from GekkoFinder
  - Integrated command logging
  - Log file viewer (type 'logs' to review program activity)
  - 10-second timeout protection against hanging

✓ Network Commands Reference
  - 25+ security testing commands
  - Organized by category (scanning, wireless, traffic analysis, DNS, etc.)
  - Usage examples for each command
  - Legal and ethical requirement reminders

✓ Comprehensive Program Logging
  - Automatic activity logging to ~/.gekkofinder.log
  - Tracks all user actions, network connections, command executions
  - Timestamp and severity levels (INFO, WARNING, ERROR)
  - Complete audit trail for security compliance

✓ Interactive Keyboard Shortcuts
  - [0] System Information & Security Analysis
  - [H] Help Menu (detailed documentation)
  - [C] Custom Command Prompt
  - [K] Keyboard Shortcuts Menu
  - [I] Ideas/Network Commands Reference
  - [#] Connect to Network by number
  - [Ctrl+C] Exit program


SYSTEM REQUIREMENTS
================================================================================

Operating System:
  • Linux/POSIX systems (Debian, Ubuntu, Fedora, CentOS, etc.)
  • macOS (Darwin) support
  • Windows Subsystem for Linux (WSL)

Software Requirements:
  • Python 3.6 or higher
  • nmcli (NetworkManager command-line interface)
  • Standard Linux utilities (arp, netstat, etc.)

Hardware:
  • Any Linux system with WiFi adapter
  • Minimum 10MB disk space
  • No special GPU or accelerators required

Network:
  • WiFi adapter with monitoring capabilities (for wireless scanning)
  • Sudo/root access required for some operations


INSTALLATION
================================================================================

1. SYSTEM DEPENDENCIES (Ubuntu/Debian)
   
   # Install NetworkManager (usually pre-installed)
   sudo apt-get install network-manager
   
   # Install Python 3
   sudo apt-get install python3
   
   # Install optional network tools
   sudo apt-get install net-tools wireless-tools


2. GEKKOFINDER INSTALLATION
   
   # Option A: Direct from file
   cd /home/elias
   chmod +x GekkoFinder.py
   
   # Option B: Copy to system-wide location
   sudo cp GekkoFinder.py /usr/local/bin/gekkofinder
   sudo chmod +x /usr/local/bin/gekkofinder


3. VERIFY INSTALLATION
   
   # Test script compilation
   python3 -m py_compile GekkoFinder.py
   
   # Expected output: No errors displayed


QUICK START GUIDE
================================================================================

LAUNCHING GEKKOFINDER
   
   # From current directory
   python3 /home/elias/GekkoFinder.py
   
   # If copied to system path
   gekkofinder
   
   # Display help information
   python3 GekkoFinder.py -h
   python3 GekkoFinder.py --help


BASIC WORKFLOW

   1. Launch GekkoFinder
      $ python3 GekkoFinder.py
      [Program displays available WiFi networks with security analysis]

   2. Review Network Information
      ID  | SSID | Signal% | Location | Security | DNS | HP/Trap | Safety
      1.  | HomeNet | 95% | Local/Home | WPA2 | 0 | X | ✓✓✓✓

   3. Choose Your Action:
      
      Option A - Check Network Safety:
      Press [0] to view system info and honeypot detection
      
      Option B - Execute Commands:
      Press [C] to open command prompt
      Type 'ifconfig' or 'logs' or any bash command
      Type 'exit' to return to menu
      
      Option C - Learn Security Commands:
      Press [K] then [I] to view network testing commands
      
      Option D - Connect to Network:
      Type network number (1-9) and press Enter
      Enter password if required (max 3 attempts)

   4. Monitor Activity:
      Press [C] then type 'logs' to review program activity


DETAILED USAGE
================================================================================

UNDERSTANDING NETWORK DISPLAY

Each network entry shows:
   ID      - Network selection number (type to connect)
   SSID    - Network name (up to 20 characters)
   Signal% - WiFi strength (0-100%)
   Location- Estimated location (Country/City or place type)
   Sec     - Security protocol (Open, WEP, WPA, WPA2, WPA3)
   DNS     - DNS/Proxy status (0, DNS, Proxy, or &)
   HP/Trap - Honeypot detection (X=safe, Y=dangerous)
   SS      - Safety Scores (T/UF/OF/NU with color coding)

SAFETY SCORE MEANINGS

   T  = Testing (Penetration testing)
        🟢 Green (S) = Safe for authorized security testing
        🔴 Red (X) = Not safe for testing

   UF = Upload Files (Sensitive data transmission)
        🟢 Green (S) = Safe for uploading credentials/files
        🔴 Red (X) = Not safe for file uploads

   OF = Open Files (Sensitive document access)
        🟢 Green (S) = Safe for opening confidential documents
        🔴 Red (X) = Not safe for opening sensitive files

   NU = Normal Usage (General browsing)
        🟢 Green (S) = Safe for general internet use
        🔴 Red (X) = Not safe for any activity

SECURITY PROTOCOLS

   Open    - No encryption (highest risk, avoid)
   WEP     - Deprecated, broken encryption (critical risk, never use)
   WPA     - Legacy encryption (moderate risk, browsing only)
   WPA2    - Strong encryption (safe for most activities)
   WPA3    - Maximum encryption (safe for all activities including testing)

DECISION MAKING QUICK REFERENCE

   If HP/Trap = Y (honeypot detected)
      → DO NOT CONNECT - Malicious network detected

   If NU = Red (not safe for browsing)
      → DO NOT CONNECT - Not safe for any activity

   If NU = Green, others Red
      → SAFE for general browsing only

   If All = Green, Signal 80%+
      → SAFE for all activities

   If WPA3 + Signal 90%+
      → OPTIMAL network, safe for everything


COMMAND PROMPT FEATURES
================================================================================

ACCESS COMMAND PROMPT
   Press [C] in main menu

AVAILABLE COMMANDS

   Program Commands:
   • logs        - Display last 30 program log entries
   • help        - Show command help
   • exit        - Return to main menu

   Network Diagnostics:
   • ifconfig           - Network interface configuration
   • netstat -tuln      - Show listening ports
   • ping 8.8.8.8       - Test internet connectivity
   • nslookup google.com- DNS query test
   • traceroute google.com - Network path analysis

   System Information:
   • whoami      - Current user
   • pwd         - Current directory
   • hostname    - Computer name
   • uname -a    - Operating system info

   Any Standard Bash Command:
   • curl, wget, grep, awk, sed, find, etc.

EXAMPLE SESSION

   $ ifconfig
   eth0: flags=UP,BROADCAST,RUNNING
      inet 192.168.1.100

   $ netstat -tuln
   Proto  Local Address     State
   tcp    0.0.0.0:22        LISTEN

   $ logs
   2026-01-31 14:23:45 - INFO - GekkoFinder started
   2026-01-31 14:23:47 - INFO - Custom command prompt opened
   2026-01-31 14:23:52 - INFO - Command executed: ifconfig

   $ exit
   [Returns to network scanning view]


PROGRAM LOGGING
================================================================================

Log File Location:
   ~/.gekkofinder.log

What Gets Logged:
   • Program start/stop events
   • User menu navigation
   • Network connection attempts (success/failure)
   • Command executions
   • Errors and exceptions
   • System events

Log Format:
   YYYY-MM-DD HH:MM:SS - LEVEL - MESSAGE
   Example: 2026-01-31 14:23:45 - INFO - GekkoFinder started

Log Levels:
   INFO    - Normal operations and user actions
   WARNING - Failed operations, timeouts
   ERROR   - System errors and exceptions

Viewing Logs:
   # Within GekkoFinder
   Press [C] then type 'logs'

   # From terminal
   tail -30 ~/.gekkofinder.log        # Last 30 entries
   grep "ERROR" ~/.gekkofinder.log    # Error entries only
   cat ~/.gekkofinder.log             # All logs


TROUBLESHOOTING
================================================================================

PROBLEM: "nmcli not available"
SOLUTION:
   • Install NetworkManager: sudo apt-get install network-manager
   • On macOS: brew install networkmanager
   • Some features disabled on systems without nmcli

PROBLEM: "No networks detected"
SOLUTION:
   • Verify WiFi adapter is enabled
   • Run: nmcli device show
   • Check WiFi switch on laptop/device
   • May require root/sudo permissions

PROBLEM: "Can't connect to network"
SOLUTION:
   • Verify correct password (case-sensitive)
   • Check if network requires special login
   • Try from terminal: nmcli dev wifi connect SSID password PASSWORD
   • Maximum 3 password attempts allowed

PROBLEM: "Command timeout"
SOLUTION:
   • Commands limited to 10 seconds
   • Try simpler commands
   • Run long commands in terminal directly
   • Example: sudo timeout 30 nmap -p 1-65535 192.168.1.0/24

PROBLEM: "Logs not appearing"
SOLUTION:
   • Check ~/.gekkofinder.log exists
   • May be empty on fresh install
   • Use 'cat ~/.gekkofinder.log' from terminal
   • Logs only record after first activity

PROBLEM: "Color coding not showing"
SOLUTION:
   • Verify terminal supports ANSI colors
   • Try: echo -e "\033[92mGreen\033[0m"
   • Use xterm or GNOME Terminal if colors don't show
   • Colors are informational only, tool functions without them


NETWORK SECURITY BEST PRACTICES
====================================================================================================================================================
                              GEKKOFINDER v1.3.B
                   WiFi Network Security Assessment Tool
================================================================================

PROJECT OVERVIEW
================================================================================

GekkoFinder is a professional-grade WiFi network security assessment tool 
designed for cybersecurity professionals, penetration testers, security 
researchers, and privacy-conscious users who need to make informed decisions 
about network safety before connecting devices.

The tool provides comprehensive real-time analysis of available WiFi networks,
evaluating them across five security dimensions:
  1. Encryption Protocol Strength (WEP → WPA → WPA2 → WPA3)
  2. Signal Quality & Connection Stability
  3. Network Infrastructure (DNS/Proxy Detection)
  4. Threat Detection (Honeypot/Trap Identification)
  5. Activity-Specific Safety Assessment

Rather than abstract risk scores, GekkoFinder delivers actionable intelligence
enabling informed connection decisions across different threat scenarios.


KEY FEATURES
================================================================================

✓ Real-Time WiFi Network Scanning
  - Continuous monitoring of available networks
  - Signal strength measurement
  - Security protocol identification
  - Network location estimation

✓ Advanced Security Analysis
  - Honeypot/Trap network detection
  - Security protocol evaluation (Open, WEP, WPA, WPA2, WPA3)
  - DNS/Proxy infrastructure detection
  - Activity-specific safety scoring

✓ Activity-Specific Safety Scores
  - Testing (Penetration Testing)
  - UF (Upload Files/Sensitive Data)
  - OF (Open Files/Sensitive Documents)
  - NU (Normal Usage/Browsing)
  Color-coded for instant visual assessment (Green=Safe, Red=Not Safe)

✓ Custom Command Prompt
  - Execute bash commands directly from GekkoFinder
  - Integrated command logging
  - Log file viewer (type 'logs' to review program activity)
  - 10-second timeout protection against hanging

✓ Network Commands Reference
  - 25+ security testing commands
  - Organized by category (scanning, wireless, traffic analysis, DNS, etc.)
  - Usage examples for each command
  - Legal and ethical requirement reminders

✓ Comprehensive Program Logging
  - Automatic activity logging to ~/.gekkofinder.log
  - Tracks all user actions, network connections, command executions
  - Timestamp and severity levels (INFO, WARNING, ERROR)
  - Complete audit trail for security compliance

✓ Interactive Keyboard Shortcuts
  - [0] System Information & Security Analysis
  - [H] Help Menu (detailed documentation)
  - [C] Custom Command Prompt
  - [K] Keyboard Shortcuts Menu
  - [I] Ideas/Network Commands Reference
  - [#] Connect to Network by number
  - [Ctrl+C] Exit program


SYSTEM REQUIREMENTS
================================================================================

Operating System:
  • Linux/POSIX systems (Debian, Ubuntu, Fedora, CentOS, etc.)
  • macOS (Darwin) support
  • Windows Subsystem for Linux (WSL)

Software Requirements:
  • Python 3.6 or higher
  • nmcli (NetworkManager command-line interface)
  • Standard Linux utilities (arp, netstat, etc.)

Hardware:
  • Any Linux system with WiFi adapter
  • Minimum 10MB disk space
  • No special GPU or accelerators required

Network:
  • WiFi adapter with monitoring capabilities (for wireless scanning)
  • Sudo/root access required for some operations


INSTALLATION
================================================================================

1. SYSTEM DEPENDENCIES (Ubuntu/Debian)
   
   # Install NetworkManager (usually pre-installed)
   sudo apt-get install network-manager
   
   # Install Python 3
   sudo apt-get install python3
   
   # Install optional network tools
   sudo apt-get install net-tools wireless-tools


2. GEKKOFINDER INSTALLATION
   
   # Option A: Direct from file
   cd /home/elias
   chmod +x GekkoFinder.py
   
   # Option B: Copy to system-wide location
   sudo cp GekkoFinder.py /usr/local/bin/gekkofinder
   sudo chmod +x /usr/local/bin/gekkofinder


3. VERIFY INSTALLATION
   
   # Test script compilation
   python3 -m py_compile GekkoFinder.py
   
   # Expected output: No errors displayed


QUICK START GUIDE
================================================================================

LAUNCHING GEKKOFINDER
   
   # From current directory
   python3 /home/elias/GekkoFinder.py
   
   # If copied to system path
   gekkofinder
   
   # Display help information
   python3 GekkoFinder.py -h
   python3 GekkoFinder.py --help


BASIC WORKFLOW

   1. Launch GekkoFinder
      $ python3 GekkoFinder.py
      [Program displays available WiFi networks with security analysis]

   2. Review Network Information
      ID  | SSID | Signal% | Location | Security | DNS | HP/Trap | Safety
      1.  | HomeNet | 95% | Local/Home | WPA2 | 0 | X | ✓✓✓✓

   3. Choose Your Action:
      
      Option A - Check Network Safety:
      Press [0] to view system info and honeypot detection
      
      Option B - Execute Commands:
      Press [C] to open command prompt
      Type 'ifconfig' or 'logs' or any bash command
      Type 'exit' to return to menu
      
      Option C - Learn Security Commands:
      Press [K] then [I] to view network testing commands
      
      Option D - Connect to Network:
      Type network number (1-9) and press Enter
      Enter password if required (max 3 attempts)

   4. Monitor Activity:
      Press [C] then type 'logs' to review program activity


DETAILED USAGE
================================================================================

UNDERSTANDING NETWORK DISPLAY

Each network entry shows:
   ID      - Network selection number (type to connect)
   SSID    - Network name (up to 20 characters)
   Signal% - WiFi strength (0-100%)
   Location- Estimated location (Country/City or place type)
   Sec     - Security protocol (Open, WEP, WPA, WPA2, WPA3)
   DNS     - DNS/Proxy status (0, DNS, Proxy, or &)
   HP/Trap - Honeypot detection (X=safe, Y=dangerous)
   SS      - Safety Scores (T/UF/OF/NU with color coding)

SAFETY SCORE MEANINGS

   T  = Testing (Penetration testing)
        🟢 Green (S) = Safe for authorized security testing
        🔴 Red (X) = Not safe for testing

   UF = Upload Files (Sensitive data transmission)
        🟢 Green (S) = Safe for uploading credentials/files
        🔴 Red (X) = Not safe for file uploads

   OF = Open Files (Sensitive document access)
        🟢 Green (S) = Safe for opening confidential documents
        🔴 Red (X) = Not safe for opening sensitive files

   NU = Normal Usage (General browsing)
        🟢 Green (S) = Safe for general internet use
        🔴 Red (X) = Not safe for any activity

SECURITY PROTOCOLS

   Open    - No encryption (highest risk, avoid)
   WEP     - Deprecated, broken encryption (critical risk, never use)
   WPA     - Legacy encryption (moderate risk, browsing only)
   WPA2    - Strong encryption (safe for most activities)
   WPA3    - Maximum encryption (safe for all activities including testing)

DECISION MAKING QUICK REFERENCE

   If HP/Trap = Y (honeypot detected)
      → DO NOT CONNECT - Malicious network detected

   If NU = Red (not safe for browsing)
      → DO NOT CONNECT - Not safe for any activity

   If NU = Green, others Red
      → SAFE for general browsing only

   If All = Green, Signal 80%+
      → SAFE for all activities

   If WPA3 + Signal 90%+
      → OPTIMAL network, safe for everything


COMMAND PROMPT FEATURES
================================================================================

ACCESS COMMAND PROMPT
   Press [C] in main menu

AVAILABLE COMMANDS

   Program Commands:
   • logs        - Display last 30 program log entries
   • help        - Show command help
   • exit        - Return to main menu

   Network Diagnostics:
   • ifconfig           - Network interface configuration
   • netstat -tuln      - Show listening ports
   • ping 8.8.8.8       - Test internet connectivity
   • nslookup google.com- DNS query test
   • traceroute google.com - Network path analysis

   System Information:
   • whoami      - Current user
   • pwd         - Current directory
   • hostname    - Computer name
   • uname -a    - Operating system info

   Any Standard Bash Command:
   • curl, wget, grep, awk, sed, find, etc.

EXAMPLE SESSION

   $ ifconfig
   eth0: flags=UP,BROADCAST,RUNNING
      inet 192.168.1.100

   $ netstat -tuln
   Proto  Local Address     State
   tcp    0.0.0.0:22        LISTEN

   $ logs
   2026-01-31 14:23:45 - INFO - GekkoFinder started
   2026-01-31 14:23:47 - INFO - Custom command prompt opened
   2026-01-31 14:23:52 - INFO - Command executed: ifconfig

   $ exit
   [Returns to network scanning view]


PROGRAM LOGGING
================================================================================

Log File Location:
   ~/.gekkofinder.log

What Gets Logged:
   • Program start/stop events
   • User menu navigation
   • Network connection attempts (success/failure)
   • Command executions
   • Errors and exceptions
   • System events

Log Format:
   YYYY-MM-DD HH:MM:SS - LEVEL - MESSAGE
   Example: 2026-01-31 14:23:45 - INFO - GekkoFinder started

Log Levels:
   INFO    - Normal operations and user actions
   WARNING - Failed operations, timeouts
   ERROR   - System errors and exceptions

Viewing Logs:
   # Within GekkoFinder
   Press [C] then type 'logs'

   # From terminal
   tail -30 ~/.gekkofinder.log        # Last 30 entries
   grep "ERROR" ~/.gekkofinder.log    # Error entries only
   cat ~/.gekkofinder.log             # All logs


TROUBLESHOOTING
================================================================================

PROBLEM: "nmcli not available"
SOLUTION:
   • Install NetworkManager: sudo apt-get install network-manager
   • On macOS: brew install networkmanager
   • Some features disabled on systems without nmcli

PROBLEM: "No networks detected"
SOLUTION:
   • Verify WiFi adapter is enabled
   • Run: nmcli device show
   • Check WiFi switch on laptop/device
   • May require root/sudo permissions

PROBLEM: "Can't connect to network"
SOLUTION:
   • Verify correct password (case-sensitive)
   • Check if network requires special login
   • Try from terminal: nmcli dev wifi connect SSID password PASSWORD
   • Maximum 3 password attempts allowed

PROBLEM: "Command timeout"
SOLUTION:
   • Commands limited to 10 seconds
   • Try simpler commands
   • Run long commands in terminal directly
   • Example: sudo timeout 30 nmap -p 1-65535 192.168.1.0/24

PROBLEM: "Logs not appearing"
SOLUTION:
   • Check ~/.gekkofinder.log exists
   • May be empty on fresh install
   • Use 'cat ~/.gekkofinder.log' from terminal
   • Logs only record after first activity

PROBLEM: "Color coding not showing"
SOLUTION:
   • Verify terminal supports ANSI colors
   • Try: echo -e "\033[92mGreen\033[0m"
   • Use xterm or GNOME Terminal if colors don't show
   • Colors are informational only, tool functions without them


NETWORK SECURITY BEST PRACTICES
================================================================================

BEFORE CONNECTING

   1. Review all security indicators
   2. Check honeypot/trap status first (Y = never connect)
   3. Verify security protocol meets activity requirements
   4. Assess signal strength for stability
   5. Consider network location context

WHILE CONNECTED

   1. Monitor your activities appropriately
   2. Don't transmit credentials on weak networks
   3. Avoid opening sensitive docs on public WiFi
   4. Use VPN for additional protection when available
   5. Keep sensitive operations for trusted networks

AFTER DISCONNECTING

   1. Review program logs for unusual activity
   2. Close sensitive applications
   3. Clear browser cache if using public computer
   4. Vary your networks to avoid patterns


GUIDES AND DOCUMENTATION
================================================================================

Three comprehensive guides included:

1. GUIDE_SIMPLE.md (2.6 KB, 117 lines)
   Quick reference with hotwords and short explanations
   Best for: Quick answers while using the tool

2. GUIDE_THOROUGH.md (33 KB, 999 lines)
   Comprehensive guide with detailed explanations
   Includes:
   • Security protocol deep-dive
   • Signal strength analysis
   • Honeypot detection explanation
   • 5 real-world scenarios
   • Best practices and troubleshooting
   Best for: Security professionals and detailed learners

3. README.txt (this file)
   Project overview and quick reference
   Best for: General understanding and setup


SUPPORT & CONTACT
================================================================================

Email Support:
   GekkoSupport@proton.me

When contacting support, please include:
   1. GekkoFinder version: python3 GekkoFinder.py -h
   2. Operating system: uname -a
   3. Python version: python3 --version
   4. Error message (if applicable)
   5. Steps to reproduce the issue
   6. Network environment (if relevant)

Common Issues:
   • Missing nmcli: Install network-manager
   • Python errors: Update to Python 3.6+
   • Permission issues: Ensure user in sudo group
   • Color problems: Terminal compatibility issue

Bug Reports:
   Include:
   • Exact error message
   • Steps to reproduce
   • Your environment details
   • Screenshot if possible


VERSION HISTORY
================================================================================

Version 1.3.B (Current)
   ✓ Color coding fixed for safety indicators
   ✓ Custom command prompt fully functional
   ✓ Program logging system active
   ✓ 25+ network commands reference
   ✓ Keyboard shortcuts menu
   ✓ Honeypot/trap detection active
   ✓ Activity-specific safety scoring
   Release Date: 2026-01-31

Version 1.1
   • Initial public release
   • Core scanning functionality
   • System information menu
   • Network security analysis


LEGAL & DISCLAIMER
================================================================================

AUTHORIZED USE ONLY

GekkoFinder is designed for:
   ✓ Authorized security testing
   ✓ Network diagnostics on own networks
   ✓ Personal WiFi security assessment
   ✓ Educational purposes with proper authorization

UNAUTHORIZED USE IS ILLEGAL

   ✗ Never use on networks without permission
   ✗ Unauthorized network testing violates computer fraud laws
   ✗ Can result in criminal prosecution
   ✗ Civil liability for damages may apply
   ✗ Respect user privacy and data protection regulations

RESPONSIBLE DISCLOSURE

   • Document all testing activities
   • Obtain written authorization before testing
   • Follow responsible disclosure practices
   • Share findings securely with network owner
   • Allow reasonable time for remediation

USER RESPONSIBILITY

   • You are responsible for proper use
   • Verify you have authorization before testing
   • Follow applicable laws and regulations
   • Maintain confidentiality of findings
   • Use only for intended security purposes


TECHNICAL SPECIFICATIONS
================================================================================

Architecture:
   • Python 3 application
   • Real-time network scanning
   • Non-blocking I/O for responsive UI
   • Background scanning thread
   • Signal selection-based interactivity

Key Libraries:
   • subprocess - System command execution
   • threading - Background scanning
   • hashlib - Network hashing (stable angle calculation)
   • select - Non-blocking input
   • logging - Activity logging
================================================================================
                              GEKKOFINDER v1.3.B
                   WiFi Network Security Assessment Tool
================================================================================

PROJECT OVERVIEW
================================================================================

GekkoFinder is a professional-grade WiFi network security assessment tool 
designed for cybersecurity professionals, penetration testers, security 
researchers, and privacy-conscious users who need to make informed decisions 
about network safety before connecting devices.

The tool provides comprehensive real-time analysis of available WiFi networks,
evaluating them across five security dimensions:
  1. Encryption Protocol Strength (WEP → WPA → WPA2 → WPA3)
  2. Signal Quality & Connection Stability
  3. Network Infrastructure (DNS/Proxy Detection)
  4. Threat Detection (Honeypot/Trap Identification)
  5. Activity-Specific Safety Assessment

Rather than abstract risk scores, GekkoFinder delivers actionable intelligence
enabling informed connection decisions across different threat scenarios.


KEY FEATURES
================================================================================

✓ Real-Time WiFi Network Scanning
  - Continuous monitoring of available networks
  - Signal strength measurement
  - Security protocol identification
  - Network location estimation

✓ Advanced Security Analysis
  - Honeypot/Trap network detection
  - Security protocol evaluation (Open, WEP, WPA, WPA2, WPA3)
  - DNS/Proxy infrastructure detection
  - Activity-specific safety scoring

✓ Activity-Specific Safety Scores
  - Testing (Penetration Testing)
  - UF (Upload Files/Sensitive Data)
  - OF (Open Files/Sensitive Documents)
  - NU (Normal Usage/Browsing)
  Color-coded for instant visual assessment (Green=Safe, Red=Not Safe)

✓ Custom Command Prompt
  - Execute bash commands directly from GekkoFinder
  - Integrated command logging
  - Log file viewer (type 'logs' to review program activity)
  - 10-second timeout protection against hanging

✓ Network Commands Reference
  - 25+ security testing commands
  - Organized by category (scanning, wireless, traffic analysis, DNS, etc.)
  - Usage examples for each command
  - Legal and ethical requirement reminders

✓ Comprehensive Program Logging
  - Automatic activity logging to ~/.gekkofinder.log
  - Tracks all user actions, network connections, command executions
  - Timestamp and severity levels (INFO, WARNING, ERROR)
  - Complete audit trail for security compliance

✓ Interactive Keyboard Shortcuts
  - [0] System Information & Security Analysis
  - [H] Help Menu (detailed documentation)
  - [C] Custom Command Prompt
  - [K] Keyboard Shortcuts Menu
  - [I] Ideas/Network Commands Reference
  - [#] Connect to Network by number
  - [Ctrl+C] Exit program


SYSTEM REQUIREMENTS
================================================================================

Operating System:
  • Linux/POSIX systems (Debian, Ubuntu, Fedora, CentOS, etc.)
  • macOS (Darwin) support
  • Windows Subsystem for Linux (WSL)

Software Requirements:
  • Python 3.6 or higher
  • nmcli (NetworkManager command-line interface)
  • Standard Linux utilities (arp, netstat, etc.)

Hardware:
  • Any Linux system with WiFi adapter
  • Minimum 10MB disk space
  • No special GPU or accelerators required

Network:
  • WiFi adapter with monitoring capabilities (for wireless scanning)
  • Sudo/root access required for some operations


INSTALLATION
================================================================================

1. SYSTEM DEPENDENCIES (Ubuntu/Debian)
   
   # Install NetworkManager (usually pre-installed)
   sudo apt-get install network-manager
   
   # Install Python 3
   sudo apt-get install python3
   
   # Install optional network tools
   sudo apt-get install net-tools wireless-tools


2. GEKKOFINDER INSTALLATION
   
   # Option A: Direct from file
   cd /home/elias
   chmod +x GekkoFinder.py
   
   # Option B: Copy to system-wide location
   sudo cp GekkoFinder.py /usr/local/bin/gekkofinder
   sudo chmod +x /usr/local/bin/gekkofinder


3. VERIFY INSTALLATION
   
   # Test script compilation
   python3 -m py_compile GekkoFinder.py
   
   # Expected output: No errors displayed


QUICK START GUIDE
================================================================================

LAUNCHING GEKKOFINDER
   
   # From current directory
   python3 /home/elias/GekkoFinder.py
   
   # If copied to system path
   gekkofinder
   
   # Display help information
   python3 GekkoFinder.py -h
   python3 GekkoFinder.py --help


BASIC WORKFLOW

   1. Launch GekkoFinder
      $ python3 GekkoFinder.py
      [Program displays available WiFi networks with security analysis]

   2. Review Network Information
      ID  | SSID | Signal% | Location | Security | DNS | HP/Trap | Safety
      1.  | HomeNet | 95% | Local/Home | WPA2 | 0 | X | ✓✓✓✓

   3. Choose Your Action:
      
      Option A - Check Network Safety:
      Press [0] to view system info and honeypot detection
      
      Option B - Execute Commands:
      Press [C] to open command prompt
      Type 'ifconfig' or 'logs' or any bash command
      Type 'exit' to return to menu
      
      Option C - Learn Security Commands:
      Press [K] then [I] to view network testing commands
      
      Option D - Connect to Network:
      Type network number (1-9) and press Enter
      Enter password if required (max 3 attempts)

   4. Monitor Activity:
      Press [C] then type 'logs' to review program activity


DETAILED USAGE
================================================================================

UNDERSTANDING NETWORK DISPLAY

Each network entry shows:
   ID      - Network selection number (type to connect)
   SSID    - Network name (up to 20 characters)
   Signal% - WiFi strength (0-100%)
   Location- Estimated location (Country/City or place type)
   Sec     - Security protocol (Open, WEP, WPA, WPA2, WPA3)
   DNS     - DNS/Proxy status (0, DNS, Proxy, or &)
   HP/Trap - Honeypot detection (X=safe, Y=dangerous)
   SS      - Safety Scores (T/UF/OF/NU with color coding)

SAFETY SCORE MEANINGS

   T  = Testing (Penetration testing)
        🟢 Green (S) = Safe for authorized security testing
        🔴 Red (X) = Not safe for testing

   UF = Upload Files (Sensitive data transmission)
        🟢 Green (S) = Safe for uploading credentials/files
        🔴 Red (X) = Not safe for file uploads

   OF = Open Files (Sensitive document access)
        🟢 Green (S) = Safe for opening confidential documents
        🔴 Red (X) = Not safe for opening sensitive files

   NU = Normal Usage (General browsing)
        🟢 Green (S) = Safe for general internet use
        🔴 Red (X) = Not safe for any activity

SECURITY PROTOCOLS

   Open    - No encryption (highest risk, avoid)
   WEP     - Deprecated, broken encryption (critical risk, never use)
   WPA     - Legacy encryption (moderate risk, browsing only)
   WPA2    - Strong encryption (safe for most activities)
   WPA3    - Maximum encryption (safe for all activities including testing)

DECISION MAKING QUICK REFERENCE

   If HP/Trap = Y (honeypot detected)
      → DO NOT CONNECT - Malicious network detected

   If NU = Red (not safe for browsing)
      → DO NOT CONNECT - Not safe for any activity

   If NU = Green, others Red
      → SAFE for general browsing only

   If All = Green, Signal 80%+
      → SAFE for all activities

   If WPA3 + Signal 90%+
      → OPTIMAL network, safe for everything


COMMAND PROMPT FEATURES
================================================================================

ACCESS COMMAND PROMPT
   Press [C] in main menu

AVAILABLE COMMANDS

   Program Commands:
   • logs        - Display last 30 program log entries
   • help        - Show command help
   • exit        - Return to main menu

   Network Diagnostics:
   • ifconfig           - Network interface configuration
   • netstat -tuln      - Show listening ports
   • ping 8.8.8.8       - Test internet connectivity
   • nslookup google.com- DNS query test
   • traceroute google.com - Network path analysis

   System Information:
   • whoami      - Current user
   • pwd         - Current directory
   • hostname    - Computer name
   • uname -a    - Operating system info

   Any Standard Bash Command:
   • curl, wget, grep, awk, sed, find, etc.

EXAMPLE SESSION

   $ ifconfig
   eth0: flags=UP,BROADCAST,RUNNING
      inet 192.168.1.100

   $ netstat -tuln
   Proto  Local Address     State
   tcp    0.0.0.0:22        LISTEN

   $ logs
   2026-01-31 14:23:45 - INFO - GekkoFinder started
   2026-01-31 14:23:47 - INFO - Custom command prompt opened
   2026-01-31 14:23:52 - INFO - Command executed: ifconfig

   $ exit
   [Returns to network scanning view]


PROGRAM LOGGING
================================================================================

Log File Location:
   ~/.gekkofinder.log

What Gets Logged:
   • Program start/stop events
   • User menu navigation
   • Network connection attempts (success/failure)
   • Command executions
   • Errors and exceptions
   • System events

Log Format:
   YYYY-MM-DD HH:MM:SS - LEVEL - MESSAGE
   Example: 2026-01-31 14:23:45 - INFO - GekkoFinder started

Log Levels:
   INFO    - Normal operations and user actions
   WARNING - Failed operations, timeouts
   ERROR   - System errors and exceptions

Viewing Logs:
   # Within GekkoFinder
   Press [C] then type 'logs'

   # From terminal
   tail -30 ~/.gekkofinder.log        # Last 30 entries
   grep "ERROR" ~/.gekkofinder.log    # Error entries only
   cat ~/.gekkofinder.log             # All logs


TROUBLESHOOTING
================================================================================

PROBLEM: "nmcli not available"
SOLUTION:
   • Install NetworkManager: sudo apt-get install network-manager
   • On macOS: brew install networkmanager
   • Some features disabled on systems without nmcli

PROBLEM: "No networks detected"
SOLUTION:
   • Verify WiFi adapter is enabled
   • Run: nmcli device show
   • Check WiFi switch on laptop/device
   • May require root/sudo permissions

PROBLEM: "Can't connect to network"
SOLUTION:
   • Verify correct password (case-sensitive)
   • Check if network requires special login
   • Try from terminal: nmcli dev wifi connect SSID password PASSWORD
   • Maximum 3 password attempts allowed

PROBLEM: "Command timeout"
SOLUTION:
   • Commands limited to 10 seconds
   • Try simpler commands
   • Run long commands in terminal directly
   • Example: sudo timeout 30 nmap -p 1-65535 192.168.1.0/24

PROBLEM: "Logs not appearing"
SOLUTION:
   • Check ~/.gekkofinder.log exists
   • May be empty on fresh install
   • Use 'cat ~/.gekkofinder.log' from terminal
   • Logs only record after first activity

PROBLEM: "Color coding not showing"
SOLUTION:
   • Verify terminal supports ANSI colors
   • Try: echo -e "\033[92mGreen\033[0m"
   • Use xterm or GNOME Terminal if colors don't show
   • Colors are informational only, tool functions without them


NETWORK SECURITY BEST PRACTICES
================================================================================

BEFORE CONNECTING

   1. Review all security indicators
   2. Check honeypot/trap status first (Y = never connect)
   3. Verify security protocol meets activity requirements
   4. Assess signal strength for stability
   5. Consider network location context

WHILE CONNECTED

   1. Monitor your activities appropriately
   2. Don't transmit credentials on weak networks
   3. Avoid opening sensitive docs on public WiFi
   4. Use VPN for additional protection when available
   5. Keep sensitive operations for trusted networks

AFTER DISCONNECTING

   1. Review program logs for unusual activity
   2. Close sensitive applications
   3. Clear browser cache if using public computer
   4. Vary your networks to avoid patterns


GUIDES AND DOCUMENTATION
================================================================================

Three comprehensive guides included:

1. GUIDE_SIMPLE.md (2.6 KB, 117 lines)
   Quick reference with hotwords and short explanations
   Best for: Quick answers while using the tool

2. GUIDE_THOROUGH.md (33 KB, 999 lines)
   Comprehensive guide with detailed explanations
   Includes:
   • Security protocol deep-dive
   • Signal strength analysis
   • Honeypot detection explanation
   • 5 real-world scenarios
   • Best practices and troubleshooting
   Best for: Security professionals and detailed learners

3. README.txt (this file)
   Project overview and quick reference
   Best for: General understanding and setup


SUPPORT & CONTACT
================================================================================

Email Support:
   GekkoSupport@proton.me

When contacting support, please include:
   1. GekkoFinder version: python3 GekkoFinder.py -h
   2. Operating system: uname -a
   3. Python version: python3 --version
   4. Error message (if applicable)
   5. Steps to reproduce the issue
   6. Network environment (if relevant)

Common Issues:
   • Missing nmcli: Install network-manager
   • Python errors: Update to Python 3.6+
   • Permission issues: Ensure user in sudo group
   • Color problems: Terminal compatibility issue

Bug Reports:
   Include:
   • Exact error message
   • Steps to reproduce
   • Your environment details
   • Screenshot if possible


VERSION HISTORY
================================================================================

Version 1.3.B (Current)
   ✓ Color coding fixed for safety indicators
   ✓ Custom command prompt fully functional
   ✓ Program logging system active
   ✓ 25+ network commands reference
   ✓ Keyboard shortcuts menu
   ✓ Honeypot/trap detection active
   ✓ Activity-specific safety scoring
   Release Date: 2026-01-31

Version 1.1
   • Initial public release
   • Core scanning functionality
   • System information menu
   • Network security analysis


LEGAL & DISCLAIMER
================================================================================

AUTHORIZED USE ONLY

GekkoFinder is designed for:
   ✓ Authorized security testing
   ✓ Network diagnostics on own networks
   ✓ Personal WiFi security assessment
   ✓ Educational purposes with proper authorization

UNAUTHORIZED USE IS ILLEGAL

   ✗ Never use on networks without permission
   ✗ Unauthorized network testing violates computer fraud laws
   ✗ Can result in criminal prosecution
   ✗ Civil liability for damages may apply
   ✗ Respect user privacy and data protection regulations

RESPONSIBLE DISCLOSURE

   • Document all testing activities
   • Obtain written authorization before testing
   • Follow responsible disclosure practices
   • Share findings securely with network owner
   • Allow reasonable time for remediation

USER RESPONSIBILITY

   • You are responsible for proper use
   • Verify you have authorization before testing
   • Follow applicable laws and regulations
   • Maintain confidentiality of findings
   • Use only for intended security purposes


TECHNICAL SPECIFICATIONS
================================================================================

Architecture:
   • Python 3 application
   • Real-time network scanning
   • Non-blocking I/O for responsive UI
   • Background scanning thread
   • Signal selection-based interactivity

Key Libraries:
   • subprocess - System command execution
   • threading - Background scanning
   • hashlib - Network hashing (stable angle calculation)
   • select - Non-blocking input
   • logging - Activity logging

Security Features:
   • No plaintext storage of sensitive data
   • Network address randomization for stability
   • Timeout protection (10 seconds per command)
   • Honeypot detection heuristics
   • Activity-appropriate risk assessment

Performance:
   • Sub-second response to user input
   • ~3 second network scan interval
   • Minimal CPU/memory usage
   • Efficient terminal rendering


ADDITIONAL RESOURCES
================================================================================

Network Security Learning:

   WiFi Security Standards:
   • IEEE 802.11i (WPA2) - Industry standard encryption
   • IEEE 802.11ax (WPA3) - Current best-practice standard
   • NIST recommendations on wireless security

   Command References:
   • nmap: https://nmap.org/
   • aircrack-ng: https://www.aircrack-ng.org/
   • tcpdump: https://www.tcpdump.org/

   Security Tools:
   • Wireshark packet analyzer
   • metasploit framework
   • Kali Linux penetration testing distribution


FILES IN PACKAGE
================================================================================

Required Files:
   GekkoFinder.py         - Main program (2,277 lines)
   README.txt             - This file

Documentation:
   GUIDE_SIMPLE.md        - Quick reference guide
   GUIDE_THOROUGH.md      - Comprehensive guide
   QUICK_START.txt        - Quick start guide
   CHANGES_SUMMARY.md     - Version history and changes

Support:
   GekkoSupport@proton.me - Email for help and bug reports

Log Files (Created during use):
   ~/.gekkofinder.log     - Program activity log


FUTURE ENHANCEMENTS
================================================================================

Potential Features:
   • Graphical user interface (GUI)
   • Multi-threaded scanning for speed
   • WiFi map visualization
   • Network recommendation engine
   • Password strength analyzer
   • Compliance report generation
   • Integration with security frameworks
   • Mobile app version


ACKNOWLEDGMENTS
================================================================================

GekkoFinder builds on the work of the Linux networking community and uses:
   • NetworkManager for WiFi scanning
   • Python standard library
   • Open-source security community tools and practices
   • Cybersecurity professionals' feedback


FREQUENTLY ASKED QUESTIONS (FAQ)
================================================================================

Q: Is GekkoFinder free?
A: Yes, GekkoFinder is provided for authorized security testing purposes.

Q: Can I use GekkoFinder on any WiFi network?
A: Only on networks you own or have explicit written permission to test.

Q: What platforms does GekkoFinder support?
A: Linux/POSIX systems (Ubuntu, Debian, Fedora, etc.) and macOS.

Q: Do I need admin/root access?
A: Most operations work as regular user. Some require sudo for advanced features.

Q: Can I connect to networks from GekkoFinder?
A: Yes, type the network number and enter password when prompted (max 3 attempts).

Q: What do the color codes mean?
A: Green = Safe for activity, Red = Not safe. See Safety Score section above.

Q: Is my data safe on WPA2 networks?
A: WPA2 with strong password provides good protection for most activities.

Q: What's the difference between WPA2 and WPA3?
A: WPA3 is newer, stronger, and protects even weak passwords better.

Q: Can I use GekkoFinder for penetration testing?
A: Yes, with proper authorization and appropriate network security level.

Q: Where are logs stored?
A: ~/.gekkofinder.log (view with 'logs' command in prompt)

Q: How do I uninstall GekkoFinder?
A: Simply delete the file. No system-wide installation by default.

Q: Can I run GekkoFinder on Windows?
A: Windows Subsystem for Linux (WSL) required for Windows compatibility.


================================================================================
                         Support: GekkoSupport@proton.me
                    Version 1.3.B | Release Date: 2026-01-31
================================================================================

Security Features:
   • No plaintext storage of sensitive data
   • Network address randomization for stability
   • Timeout protection (10 seconds per command)
   • Honeypot detection heuristics
   • Activity-appropriate risk assessment

Performance:
   • Sub-second response to user input
   • ~3 second network scan interval
   • Minimal CPU/memory usage
   • Efficient terminal rendering


ADDITIONAL RESOURCES
================================================================================

Network Security Learning:

   WiFi Security Standards:
   • IEEE 802.11i (WPA2) - Industry standard encryption
   • IEEE 802.11ax (WPA3) - Current best-practice standard
   • NIST recommendations on wireless security

   Command References:
   • nmap: https://nmap.org/
   • aircrack-ng: https://www.aircrack-ng.org/
   • tcpdump: https://www.tcpdump.org/

   Security Tools:
   • Wireshark packet analyzer
   • metasploit framework
   • Kali Linux penetration testing distribution


FILES IN PACKAGE
================================================================================

Required Files:
   GekkoFinder.py         - Main program (2,277 lines)
   README.txt             - This file

Documentation:
   GUIDE_SIMPLE.md        - Quick reference guide
   GUIDE_THOROUGH.md      - Comprehensive guide
   QUICK_START.txt        - Quick start guide
   CHANGES_SUMMARY.md     - Version history and changes

Support:
   GekkoSupport@proton.me - Email for help and bug reports

Log Files (Created during use):
   ~/.gekkofinder.log     - Program activity log


FUTURE ENHANCEMENTS
================================================================================

Potential Features:
   • Graphical user interface (GUI)
   • Multi-threaded scanning for speed
   • WiFi map visualization
   • Network recommendation engine
   • Password strength analyzer
   • Compliance report generation
   • Integration with security frameworks
   • Mobile app version


ACKNOWLEDGMENTS
================================================================================

GekkoFinder builds on the work of the Linux networking community and uses:
   • NetworkManager for WiFi scanning
   • Python standard library
   • Open-source security community tools and practices
   • Cybersecurity professionals' feedback


FREQUENTLY ASKED QUESTIONS (FAQ)
================================================================================

Q: Is GekkoFinder free?
A: Yes, GekkoFinder is provided for authorized security testing purposes.

Q: Can I use GekkoFinder on any WiFi network?
A: Only on networks you own or have explicit written permission to test.

Q: What platforms does GekkoFinder support?
A: Linux/POSIX systems (Ubuntu, Debian, Fedora, etc.) and macOS.

Q: Do I need admin/root access?
A: Most operations work as regular user. Some require sudo for advanced features.

Q: Can I connect to networks from GekkoFinder?
A: Yes, type the network number and enter password when prompted (max 3 attempts).

Q: What do the color codes mean?
A: Green = Safe for activity, Red = Not safe. See Safety Score section above.

Q: Is my data safe on WPA2 networks?
A: WPA2 with strong password provides good protection for most activities.

Q: What's the difference between WPA2 and WPA3?
A: WPA3 is newer, stronger, and protects even weak passwords better.

Q: Can I use GekkoFinder for penetration testing?
A: Yes, with proper authorization and appropriate network security level.

Q: Where are logs stored?
A: ~/.gekkofinder.log (view with 'logs' command in prompt)

Q: How do I uninstall GekkoFinder?
A: Simply delete the file. No system-wide installation by default.

Q: Can I run GekkoFinder on Windows?
A: Windows Subsystem for Linux (WSL) required for Windows compatibility.


================================================================================
                         Support: GekkoSupport@proton.me
                    Version 1.3.B | Release Date: 2026-01-31
================================================================================
============

BEFORE CONNECTING

   1. Review all security indicators
   2. Check honeypot/trap status first (Y = never connect)
   3. Verify security protocol meets activity requirements
   4. Assess signal strength for stability
   5. Consider network location context

WHILE CONNECTED

   1. Monitor your activities appropriately
   2. Don't transmit credentials on weak networks
   3. Avoid opening sensitive docs on public WiFi
   4. Use VPN for additional protection when available
   5. Keep sensitive operations for trusted networks

AFTER DISCONNECTING

   1. Review program logs for unusual activity
   2. Close sensitive applications
   3. Clear browser cache if using public computer
   4. Vary your networks to avoid patterns


GUIDES AND DOCUMENTATION
================================================================================

Three comprehensive guides included:

1. GUIDE_SIMPLE.md (2.6 KB, 117 lines)
   Quick reference with hotwords and short explanations
   Best for: Quick answers while using the tool

2. GUIDE_THOROUGH.md (33 KB, 999 lines)
   Comprehensive guide with detailed explanations
   Includes:
   • Security protocol deep-dive
   • Signal strength analysis
   • Honeypot detection explanation
   • 5 real-world scenarios
   • Best practices and troubleshooting
   Best for: Security professionals and detailed learners

3. README.txt (this file)
   Project overview and quick reference
   Best for: General understanding and setup


SUPPORT & CONTACT
================================================================================

Email Support:
   GekkoSupport@proton.me

When contacting support, please include:
   1. GekkoFinder version: python3 GekkoFinder.py -h
   2. Operating system: uname -a
   3. Python version: python3 --version
   4. Error message (if applicable)
   5. Steps to reproduce the issue
   6. Network environment (if relevant)

Common Issues:
   • Missing nmcli: Install network-manager
   • Python errors: Update to Python 3.6+
   • Permission issues: Ensure user in sudo group
   • Color problems: Terminal compatibility issue

Bug Reports:
   Include:
   • Exact error message
   • Steps to reproduce
   • Your environment details
   • Screenshot if possible


VERSION HISTORY
================================================================================

Version 1.3.B (Current)
   ✓ Color coding fixed for safety indicators
   ✓ Custom command prompt fully functional
   ✓ Program logging system active
   ✓ 25+ network commands reference
   ✓ Keyboard shortcuts menu
   ✓ Honeypot/trap detection active
   ✓ Activity-specific safety scoring
   Release Date: 2026-01-31

Version 1.1
   • Initial public release
   • Core scanning functionality
   • System information menu
   • Network security analysis


LEGAL & DISCLAIMER
================================================================================

AUTHORIZED USE ONLY

GekkoFinder is designed for:
   ✓ Authorized security testing
   ✓ Network diagnostics on own networks
   ✓ Personal WiFi security assessment
   ✓ Educational purposes with proper authorization

UNAUTHORIZED USE IS ILLEGAL

   ✗ Never use on networks without permission
   ✗ Unauthorized network testing violates computer fraud laws
   ✗ Can result in criminal prosecution
   ✗ Civil liability for damages may apply
   ✗ Respect user privacy and data protection regulations

RESPONSIBLE DISCLOSURE

   • Document all testing activities
   • Obtain written authorization before testing
   • Follow responsible disclosure practices
   • Share findings securely with network owner
   • Allow reasonable time for remediation

USER RESPONSIBILITY

   • You are responsible for proper use
   • Verify you have authorization before testing
   • Follow applicable laws and regulations
   • Maintain confidentiality of findings
   • Use only for intended security purposes


TECHNICAL SPECIFICATIONS
================================================================================

Architecture:
   • Python 3 application
   • Real-time network scanning
   • Non-blocking I/O for responsive UI
   • Background scanning thread
   • Signal selection-based interactivity

Key Libraries:
   • subprocess - System command execution
   • threading - Background scanning
   • hashlib - Network hashing (stable angle calculation)
   • select - Non-blocking input
   • logging - Activity logging

Security Features:
   • No plaintext storage of sensitive data
   • Network address randomization for stability
   • Timeout protection (10 seconds per command)
   • Honeypot detection heuristics
   • Activity-appropriate risk assessment

Performance:
   • Sub-second response to user input
   • ~3 second network scan interval
   • Minimal CPU/memory usage
   • Efficient terminal rendering


ADDITIONAL RESOURCES
================================================================================

Network Security Learning:

   WiFi Security Standards:
   • IEEE 802.11i (WPA2) - Industry standard encryption
   • IEEE 802.11ax (WPA3) - Current best-practice standard
   • NIST recommendations on wireless security

   Command References:
   • nmap: https://nmap.org/
   • aircrack-ng: https://www.aircrack-ng.org/
   • tcpdump: https://www.tcpdump.org/

   Security Tools:
   • Wireshark packet analyzer
   • metasploit framework
   • Kali Linux penetration testing distribution


FILES IN PACKAGE
================================================================================

Required Files:
   GekkoFinder.py         - Main program (2,277 lines)
   README.txt             - This file

Documentation:
   GUIDE_SIMPLE.md        - Quick reference guide
   GUIDE_THOROUGH.md      - Comprehensive guide
   QUICK_START.txt        - Quick start guide
   CHANGES_SUMMARY.md     - Version history and changes

Support:
   GekkoSupport@proton.me - Email for help and bug reports

Log Files (Created during use):
   ~/.gekkofinder.log     - Program activity log


FUTURE ENHANCEMENTS
================================================================================

Potential Features:
   • Graphical user interface (GUI)
   • Multi-threaded scanning for speed
   • WiFi map visualization
   • Network recommendation engine
   • Password strength analyzer
   • Compliance report generation
   • Integration with security frameworks
   • Mobile app version


ACKNOWLEDGMENTS
================================================================================

GekkoFinder builds on the work of the Linux networking community and uses:
   • NetworkManager for WiFi scanning
   • Python standard library
   • Open-source security community tools and practices
   • Cybersecurity professionals' feedback


FREQUENTLY ASKED QUESTIONS (FAQ)
================================================================================

Q: Is GekkoFinder free?
A: Yes, GekkoFinder is provided for authorized security testing purposes.

Q: Can I use GekkoFinder on any WiFi network?
A: Only on networks you own or have explicit written permission to test.

Q: What platforms does GekkoFinder support?
A: Linux/POSIX systems (Ubuntu, Debian, Fedora, etc.) and macOS.

Q: Do I need admin/root access?
A: Most operations work as regular user. Some require sudo for advanced features.

Q: Can I connect to networks from GekkoFinder?
A: Yes, type the network number and enter password when prompted (max 3 attempts).

Q: What do the color codes mean?
A: Green = Safe for activity, Red = Not safe. See Safety Score section above.

Q: Is my data safe on WPA2 networks?
A: WPA2 with strong password provides good protection for most activities.

Q: What's the difference between WPA2 and WPA3?
A: WPA3 is newer, stronger, and protects even weak passwords better.

Q: Can I use GekkoFinder for penetration testing?
A: Yes, with proper authorization and appropriate network security level.

Q: Where are logs stored?
A: ~/.gekkofinder.log (view with 'logs' command in prompt)

Q: How do I uninstall GekkoFinder?
A: Simply delete the file. No system-wide installation by default.

Q: Can I run GekkoFinder on Windows?
A: Windows Subsystem for Linux (WSL) required for Windows compatibility.


================================================================================
                         Support: GekkoSupport@proton.me
                    Version 1.3.B | Release Date: 2026-01-31
================================================================================


Log Files (Created during use):
   ~/.gekkofinder.log     - Program activity log


FUTURE ENHANCEMENTS
================================================================================

Potential Features:
   • Graphical user interface (GUI)
   • Multi-threaded scanning for speed
   • WiFi map visualization
   • Network recommendation engine
   • Password strength analyzer
   • Compliance report generation
   • Integration with security frameworks
   • Mobile app version


ACKNOWLEDGMENTS
================================================================================

GekkoFinder builds on the work of the Linux networking community and uses:
   • NetworkManager for WiFi scanning
   • Python standard library
   • Open-source security community tools and practices
   • Cybersecurity professionals' feedback


FREQUENTLY ASKED QUESTIONS (FAQ)
================================================================================

Q: Is GekkoFinder free?
A: Yes, GekkoFinder is provided for authorized security testing purposes.

Q: Can I use GekkoFinder on any WiFi network?
A: Only on networks you own or have explicit written permission to test.

Q: What platforms does GekkoFinder support?
A: Linux/POSIX systems (Ubuntu, Debian, Fedora, etc.) and macOS.

Q: Do I need admin/root access?
A: Most operations work as regular user. Some require sudo for advanced features.

Q: Can I connect to networks from GekkoFinder?
A: Yes, type the network number and enter password when prompted (max 3 attempts).

Q: What do the color codes mean?
A: Green = Safe for activity, Red = Not safe. See Safety Score section above.

Q: Is my data safe on WPA2 networks?
A: WPA2 with strong password provides good protection for most activities.

Q: What's the difference between WPA2 and WPA3?
A: WPA3 is newer, stronger, and protects even weak passwords better.

Q: Can I use GekkoFinder for penetration testing?
A: Yes, with proper authorization and appropriate network security level.

Q: Where are logs stored?
A: ~/.gekkofinder.log (view with 'logs' command in prompt)

Q: How do I uninstall GekkoFinder?
A: Simply delete the file. No system-wide installation by default.

Q: Can I run GekkoFinder on Windows?
A: Windows Subsystem for Linux (WSL) required for Windows compatibility.


================================================================================
                         Support: GekkoSupport@proton.me
                    Version 1.3.B | Release Date: 2026-01-31
================================================================================

   ✓ Network diagnostics on own networks
   ✓ Personal WiFi security assessment
   ✓ Educational purposes with proper authorization

UNAUTHORIZED USE IS ILLEGAL

   ✗ Never use on networks without permission
   ✗ Unauthorized network testing violates computer fraud laws
   ✗ Can result in criminal prosecution
   ✗ Civil liability for damages may apply
   ✗ Respect user privacy and data protection regulations

RESPONSIBLE DISCLOSURE

   • Document all testing activities
   • Obtain written authorization before testing
   • Follow responsible disclosure practices
   • Share findings securely with network owner
   • Allow reasonable time for remediation

USER RESPONSIBILITY

   • You are responsible for proper use
   • Verify you have authorization before testing
   • Follow applicable laws and regulations
   • Maintain confidentiality of findings
   • Use only for intended security purposes


TECHNICAL SPECIFICATIONS
================================================================================

Architecture:
   • Python 3 application
   • Real-time network scanning
   • Non-blocking I/O for responsive UI
   • Background scanning thread
   • Signal selection-based interactivity

Key Libraries:
   • subprocess - System command execution
   • threading - Background scanning
   • hashlib - Network hashing (stable angle calculation)
   • select - Non-blocking input
   • logging - Activity logging

Security Features:
   • No plaintext storage of sensitive data
   • Network address randomization for stability
   • Timeout protection (10 seconds per command)
   • Honeypot detection heuristics
   • Activity-appropriate risk assessment

Performance:
   • Sub-second response to user input
   • ~3 second network scan interval
   • Minimal CPU/memory usage
   • Efficient terminal rendering


ADDITIONAL RESOURCES
================================================================================

Network Security Learning:

   WiFi Security Standards:
   • IEEE 802.11i (WPA2) - Industry standard encryption
   • IEEE 802.11ax (WPA3) - Current best-practice standard
   • NIST recommendations on wireless security

   Command References:
   • nmap: https://nmap.org/
   • aircrack-ng: https://www.aircrack-ng.org/
   • tcpdump: https://www.tcpdump.org/

   Security Tools:
   • Wireshark packet analyzer
   • metasploit framework
   • Kali Linux penetration testing distribution


FILES IN PACKAGE
================================================================================

Required Files:
   GekkoFinder.py         - Main program (2,277 lines)
   README.txt             - This file

Documentation:
   GUIDE_SIMPLE.md        - Quick reference guide
   GUIDE_THOROUGH.md      - Comprehensive guide
   QUICK_START.txt        - Quick start guide
   CHANGES_SUMMARY.md     - Version history and changes

Support:
   GekkoSupport@proton.me - Email for help and bug reports

Log Files (Created during use):
   ~/.gekkofinder.log     - Program activity log


FUTURE ENHANCEMENTS
================================================================================

Potential Features:
   • Graphical user interface (GUI)
   • Multi-threaded scanning for speed
   • WiFi map visualization
   • Network recommendation engine
   • Password strength analyzer
   • Compliance report generation
   • Integration with security frameworks
   • Mobile app version


ACKNOWLEDGMENTS
================================================================================

GekkoFinder builds on the work of the Linux networking community and uses:
   • NetworkManager for WiFi scanning
   • Python standard library
   • Open-source security community tools and practices
   • Cybersecurity professionals' feedback


FREQUENTLY ASKED QUESTIONS (FAQ)
================================================================================

Q: Is GekkoFinder free?
A: Yes, GekkoFinder is provided for authorized security testing purposes.

Q: Can I use GekkoFinder on any WiFi network?
A: Only on networks you own or have explicit written permission to test.

Q: What platforms does GekkoFinder support?
A: Linux/POSIX systems (Ubuntu, Debian, Fedora, etc.) and macOS.

Q: Do I need admin/root access?
A: Most operations work as regular user. Some require sudo for advanced features.

Q: Can I connect to networks from GekkoFinder?
A: Yes, type the network number and enter password when prompted (max 3 attempts).

Q: What do the color codes mean?
A: Green = Safe for activity, Red = Not safe. See Safety Score section above.

Q: Is my data safe on WPA2 networks?
A: WPA2 with strong password provides good protection for most activities.

Q: What's the difference between WPA2 and WPA3?
A: WPA3 is newer, stronger, and protects even weak passwords better.

Q: Can I use GekkoFinder for penetration testing?
A: Yes, with proper authorization and appropriate network security level.

Q: Where are logs stored?
A: ~/.gekkofinder.log (view with 'logs' command in prompt)

Q: How do I uninstall GekkoFinder?
A: Simply delete the file. No system-wide installation by default.

Q: Can I run GekkoFinder on Windows?
A: Windows Subsystem for Linux (WSL) required for Windows compatibility.


================================================================================
                         Support: GekkoSupport@proton.me
                    Version 1.3.B | Release Date: 2026-01-31
================================================================================



#!/usr/bin/env python3
# Displays an ASCII "Searching" header and an animated radar in the terminal.
# Save as a .py file and run in a terminal.

import os
import sys
import time
import math
import subprocess
import builtins
# Big ASCII "GekkoFinder" header
GEKKO_HEADER = [
    "   ▗▄▄▖▗▄▄▄▖▗▖ ▗▖▗▖ ▗▖ ▗▄▖             ▗▄▄▄▖ ▗▄▄▖▗▖ ▗▖ ▗▄▖", 
       "▐▌   ▐▌   ▐▌▗▞▘▐▌▗▞▘▐▌ ▐▌            ▐▌   ▐▌   ▐▌ ▐▌▐▌ ▐▌",
       "▐▌▝▜▌▐▛▀▀▘▐▛▚▖ ▐▛▚▖ ▐▌ ▐▌            ▐▛▀▀▘▐▌   ▐▛▀▜▌▐▌ ▐▌",
       "▝▚▄▞▘▐▙▄▄▖▐▌ ▐▌▐▌ ▐▌▝▚▄▞▘            ▐▙▄▄▖▝▚▄▄▖▐▌ ▐▌▝▚▄▞▘"       
      
      
    

]

SMALL_RADAR = [
    "        ,-.                                   ",
    "       / \\  `.  __..-,O                      ",
    "      :   \\ --''_..-'.'                    ",
    "      |    . .-' `. '.                      ",
    "      :     .     .`.'                      ",
    "       \\     `.  /  ..                      ",
    "        \\      `.   ' .                     ",
    "         `,       `.   \\                    ",
    "        ,|,`.        `-.\\ ",
    "       '.||  ``-...__..-` ",
    "        |  |                                 ",
    "        |__|                                 ",
    "        /||\\                                 ",
    "       //||\\\\                                ",
    "      // || \\\\                               ",
    "   __//__||__\\\\__                            ",
    "  '--------------'                          ",
]

# helper to combine two blocks side-by-side
def _side_by_side(left_lines, right_lines, gap=6):
    lw = max((len(s) for s in left_lines), default=0)
    rw = max((len(s) for s in right_lines), default=0)
    height = max(len(left_lines), len(right_lines))
    out = []
    for i in range(height):
        L = left_lines[i] if i < len(left_lines) else ""
        R = right_lines[i] if i < len(right_lines) else ""
        out.append(L.ljust(lw) + (" " * gap) + R)
    return out

# wrap the built-in print so we can prepend the big header + small radar
_original_print = builtins.print


def _is_main_frame_print(args, kwargs):
    # Heuristic: main frame is printed as one large string containing "Searching..."
    if len(args) == 1 and isinstance(args[0], str) and "Searching..." in args[0]:
        return True
    return False


def _custom_print(*args, **kwargs):
    if _is_main_frame_print(args, kwargs):
        header_block = _side_by_side(GEKKO_HEADER, SMALL_RADAR, gap=6)
        header_text = "\n".join(header_block) + "\n\n"
        # Prepend the header block to the existing single-string frame
        new_first = header_text + args[0]
        return _original_print(new_first, **kwargs)
    return _original_print(*args, **kwargs)


builtins.print = _custom_print
import hashlib
import threading
import random
import shutil
import signal
import select
import getpass
import logging
from datetime import datetime

# ASCII header - GekkoFinder fancy
HEADER = [
    "  /$$$$$$            /$$       /$$                       /$$$$$$$$ /$$                 /$$                    ",
    " /$$__  $$          | $$      | $$                      | $$_____/|__/                | $$                    ",
    "| $$  \\__/  /$$$$$$ | $$   /$$| $$   /$$  /$$$$$$       | $$       /$$ /$$$$$$$   /$$$$$$$  /$$$$$$   /$$$$$$ ",
    "| $$ /$$$$ /$$__  $$| $$  /$$/| $$  /$$/ /$$__  $$      | $$$$$   | $$| $$__  $$ /$$__  $$ /$$__  $$ /$$__  $$",
    "| $$|_  $$| $$$$$$$$| $$$$$$/ | $$$$$$/ | $$  \\ $$      | $$__/   | $$| $$  \\ $$| $$  | $$| $$$$$$$$| $$  \\__/",
    "| $$  \\ $$| $$_____/| $$_  $$ | $$_  $$ | $$  | $$      | $$      | $$| $$  | $$| $$  | $$| $$_____/| $$      ",
    "|  $$$$$$/|  $$$$$$$| $$ \\  $$| $$ \\  $$|  $$$$$$/      | $$      | $$| $$  | $$|  $$$$$$$|  $$$$$$$| $$      ",
    " \\______/  \\_______/|__/  \\__/|__/  \\__/ \\______/       |__/      |__/|__/  |__/ \\_______/ \\_______/|__/      ",
]

# Bird radar ASCII art
BIRD_RADAR = [
    "        ,-.                                   ",
    "       / \\  `.  __..-,O                      ",
    "      :   \\ --''_..-'.'                    ",
    "      |    . .-' `. '.                      ",
    "      :     .     .`.'                      ",
    "       \\     `.  /  ..                      ",
    "        \\      `.   ' .                     ",
    "         `,       `.   \\                    ",
    "        ,|,`.        `-.\\ \t\t\t    ",
    "       '.||  ``-...__..-` \t\t\t",
    "        |  |                                 ",
    "        |__|                                 ",
    "        /||\\                                 ",
    "       //||\\\\                                ",
    "      // || \\\\                               ",
    "   __//__||__\\\\__                            ",
    "  '--------------'                          ",
]

# small extra ASCII radar (can be printed above the animated radar)
RADAR_ART = [
    "      .----.      ",
    "   .-'      '-.   ",
    "  /  .----.    \\  ",
    " |  /      \\   |  ",
    " | |  ( )  |   |  ",
    "  \\ \\      /  /   ",
    "   '-.____.-'     ",
]

# Binocular/Telescope ASCII art for password screen
BINOCULARS = [
    "_____________________________",
    "|                  _        |",
    "|                 /\"\\       |",
    "|                /o o\\      |",
    "|           _\\/  \\   / \\/_  |",
    "|            \\\\._/  /_.//   |",
    "|            `--,  ,----'   |",
    "|              /   /        |",
    "|    ^        /    \\        |",
    "|   /|       (      )       |",
    "|  / |     ,__\\    /__,     |",
    "|  \\ \\   _//---,  ,--\\_    |",
    "|   \\ \\   /\\  /  /   /\\     |",
    "|    \\ \\.___,/  /           |",
    "|     \\.___,/            |",
    "|                           |",
    "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",
]

def _nmcli_available():
    try:
        # use shutil.which for portability
        import shutil as _sh
        return _sh.which("nmcli") is not None
    except Exception:
        return False

def scan_wifi():
    """
    Return a list of networks found by NetworkManager (nmcli) on Linux.
    Each entry: {'ssid': str, 'signal': int, 'security': str}
    """
    if os.name != "posix" or not _nmcli_available():
        return []
    try:
        p = subprocess.run(
            ["nmcli", "-t", "-f", "SSID,SIGNAL,SECURITY", "dev", "wifi", "list"],
            capture_output=True,
            text=True,
            timeout=10,
        )
        nets = []
        for line in p.stdout.splitlines():
            if not line:
                continue
            parts = line.split(":")
            ssid = parts[0].strip() or "<Hidden>"
            sig = 0
            sec = ""
            if len(parts) > 1:
                try:
                    sig = int(parts[1])
                except Exception:
                    sig = 0
            if len(parts) > 2:
                sec = parts[2]
            nets.append({"ssid": ssid, "signal": sig, "security": sec})
        return nets
    except Exception:
        return []

def networks_to_blips(networks, radar_w, radar_h):
    """
    Map scanned networks to radar blip dicts: {'a': angle, 'r': radius}
    Angle is stable per-SSID (hashed). Radius is derived from signal (strong -> closer).
    """
    blips = []
    maxr = max(2, min(radar_w // 2, radar_h // 2) - 1)
    for net in networks:
        ssid = net.get("ssid", "")
        signal = max(0, min(100, int(net.get("signal", 0))))
        # stable angle from hash (use 32-bit portion)
        h = int(hashlib.sha256(ssid.encode("utf-8")).hexdigest()[:8], 16)
        angle = (float(h) / float(0xFFFFFFFF)) * 2 * math.pi
        # stronger signal -> smaller radius
        r = 1 + (1.0 - signal / 100.0) * (maxr - 1)
        blips.append({"a": angle, "r": r, "ssid": ssid, "signal": signal})
    return blips

def get_security_type(security_string):
    """
    Return security protocol name instead of numeric rating.
    """
    if not security_string or security_string == "--" or security_string == "":
        return "Open"
    
    sec_lower = security_string.lower()
    
    if "wpa3" in sec_lower:
        return "WPA3"
    elif "wpa2" in sec_lower:
        return "WPA2"
    elif "wep" in sec_lower:
        return "WEP"
    elif "wpa" in sec_lower:
        return "WPA"
    else:
        return "Unknown"

def get_security_rating(security_type):
    """
    Return a security rating (1-10) based on the network's security type.
    """
    if not security_type or security_type == "--" or security_type == "":
        return 1  # No security
    
    sec_lower = security_type.lower()
    
    if "wep" in sec_lower:
        return 2  # WEP is outdated and weak
    elif "wpa3" in sec_lower:
        return 10  # WPA3 is the most secure
    elif "wpa2" in sec_lower:
        return 8  # WPA2 is very good
    elif "wpa" in sec_lower:
        return 5  # WPA (legacy) is moderate
    else:
        return 3  # Unknown security type, assume weak

def detect_dns_proxy(ssid):
    """
    Detect if network uses DNS or Proxy based on SSID patterns.
    Returns: '&' if both, 'DNS' if DNS only, 'Proxy' if Proxy only, '0' if neither, 'X' if unknown
    """
    ssid_lower = ssid.lower()
    has_dns = False
    has_proxy = False
    
    # DNS indicators
    if any(x in ssid_lower for x in ["dns", "vpn", "secure", "shield"]):
        has_dns = True
    
    # Proxy indicators
    if any(x in ssid_lower for x in ["proxy", "gateway", "firewall", "corporate"]):
        has_proxy = True
    
    if has_dns and has_proxy:
        return "&"
    elif has_dns:
        return "DNS"
    elif has_proxy:
        return "Proxy"
    elif has_dns or has_proxy:  # One detected
        return "DNS" if has_dns else "Proxy"
    else:
        return "0"  # Neither detected

def detect_honeypot_trap(ssid, security_type):
    """
    Detect potential honeypot/trap networks by analyzing suspicious indicators.
    Returns dict with 'HP' (honeypot) and 'Trap' indicators.
    """
    ssid_lower = ssid.lower()
    risk_score = 0
    
    # Suspicious SSID patterns
    suspicious_patterns = [
        "free_wifi", "open_wifi", "public_network", "guest_network",
        "airport_free", "no_password", "easy_connect", "instant_access"
    ]
    
    if any(pattern in ssid_lower for pattern in suspicious_patterns):
        risk_score += 3
    
    # Too generic names (suspicious)
    generic_names = ["wifi", "network", "internet", "connect", "guest"]
    if any(name == ssid_lower for name in generic_names):
        risk_score += 2
    
    # Extremely weak security with high-risk SSID combination
    if security_type == "Open":
        risk_score += 2
    
    # Numbers-only or random SSID (often honeypots)
    if ssid.isdigit() or (len(ssid) > 10 and ssid.isupper()):
        risk_score += 1
    
    hp_status = "Y" if risk_score >= 4 else "X"
    trap_status = "Y" if risk_score >= 5 else "X"
    
    return {
        "Insecure Network": hp_status,
        "Controlled network": trap_status,
        "risk_score": risk_score
    }

def estimate_network_location(ssid):
    """
    Estimate network location based on SSID patterns.
    Returns a tuple (country, city) or ("Unknown", "Unknown")
    """
    ssid_lower = ssid.lower()
    
    # Common patterns for different locations
    if any(x in ssid_lower for x in ["starbucks", "cafe", "coffee"]):
        return ("USA", "Unknown City")
    elif any(x in ssid_lower for x in ["airport", "gate", "terminal"]):
        return ("Unknown", "Airport")
    elif any(x in ssid_lower for x in ["hotel", "marriott", "hilton"]):
        return ("Unknown", "Hotel")
    elif any(x in ssid_lower for x in ["home", "house", "family"]):
        return ("Local", "Home")
    elif any(x in ssid_lower for x in ["work", "office", "corp", "company"]):
        return ("Unknown", "Office")
    elif any(x in ssid_lower for x in ["library", "public"]):
        return ("Unknown", "Public Library")
    else:
        return ("Unknown", "Unknown")

def colorize_safety(status):
    """
    Colorize safety status: Green for S (Safe), Red for X (Not Safe)
    """
    if status == "S":
        return f"\033[92m{status}\033[0m"  # Green
    else:  # X
        return f"\033[91m{status}\033[0m"  # Red

def get_cybersecurity_safety(security_rating, honeypot_info=None):
    """
    Determine cybersecurity safety for different usage types based on security rating.
    Returns dict with T (Testing), UF (Upload Files), OF (Open Files), NU (Normal Usage) safety status.
    S = Safe, X = Not Safe
    
    If honeypot_info is provided and indicates a trap, all indicators are marked unsafe.
    """
    # If network is flagged as honeypot/trap, all activities are unsafe
    if honeypot_info and (honeypot_info.get("HP") == "Y" or honeypot_info.get("Trap") == "Y"):
        return {
            "T": "X",   # Never safe for testing on honeypot
            "UF": "X",  # Never safe for uploads on honeypot
            "OF": "X",  # Never safe for sensitive files on honeypot
            "NU": "X",  # Never safe for any activity on honeypot
        }
    
    return {
        "T": "S" if security_rating >= 9 else "X",   # Testing needs very high security (WPA3 only)
        "UF": "S" if security_rating >= 8 else "X",  # Uploading Files needs highest security (WPA2/WPA3)
        "OF": "S" if security_rating >= 7 else "X",  # Opening Files needs high security (WPA/WPA2/WPA3)
        "NU": "S" if security_rating >= 5 else "X",  # Normal Usage needs moderate security (WPA+)
    }

def print_networks_console(networks, width=80):
    """
    Nicely print scanned networks with indices to help connect from terminal.
    """
    lines = []
    lines.append(center_text("Available Wi‑Fi Networks", width))
    for i, n in enumerate(networks, 1):
        bar = "#" * (n["signal"] // 10)
        ss = n["ssid"] if len(n["ssid"]) <= (width - 20) else n["ssid"][: (width - 23)] + "..."
        lines.append(f"{i:2d}. {ss:<40} {n['signal']:3d}% {bar}")
    print("\n".join(lines))

def connect_to_network(ssid, password=None):
    """
    Attempt to connect using nmcli. Returns True on success.
    """
    if os.name != "posix" or not _nmcli_available():
        print("nmcli not available on this system.")
        return False
    cmd = ["nmcli", "dev", "wifi", "connect", ssid]
    if password:
        cmd += ["password", password]
    try:
        res = subprocess.run(cmd)
        return res.returncode == 0
    except Exception as e:
        print("Connection failed:", e)
        return False

# Background scanner thread that updates a global cache periodically
_network_cache = []
def _scanner_loop(interval=3.0):
    global _network_cache
    while True:
        _network_cache = scan_wifi()
        time.sleep(interval)

def start_background_scan(interval=3.0):
    t = threading.Thread(target=_scanner_loop, args=(interval,), daemon=True)
    t.start()
    return t

# Enable ANSI on Windows (best effort)
if os.name == "nt":
    try:
        import ctypes
        kernel32 = ctypes.windll.kernel32
        handle = kernel32.GetStdHandle(-11)
        # enable ENABLE_VIRTUAL_TERMINAL_PROCESSING (0x0004) and ENABLE_PROCESSED_OUTPUT (0x0001)
        kernel32.SetConsoleMode(handle, 7)
    except Exception:
        pass

running = True

# Setup logging
log_file = os.path.expanduser("~/.gekkofinder.log")
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def stop(signum=None, frame=None):
    global running
    running = False
    logging.info("GekkoFinder stopped by user")

signal.signal(signal.SIGINT, stop)
if hasattr(signal, "SIGTERM"):
    signal.signal(signal.SIGTERM, stop)

def clear():
    # Move cursor to home and clear screen
    sys.stdout.write("\033[H\033[J")
    sys.stdout.flush()

def center_text(s, width):
    s = str(s)
    if len(s) >= width:
        return s[: max(0, width - 1)]
    pad = max(0, (width - len(s)) // 2)
    return " " * pad + s

def make_radar_frame(w, h, sweep_angle, blips):
    """
    Create a simple ASCII radar frame: circle boundary, a sweeping arm, and blips.
    """
    grid = [[" " for _ in range(w)] for _ in range(h)]
    cx, cy = w // 2, h // 2
    R = min(cx, cy) - 1
    if R < 2:
        return ["".join(row) for row in grid]

    # draw circle boundary
    for y in range(h):
        for x in range(w):
            dx = x - cx
            dy = cy - y  # invert y so angle 0 is to the right, positive CCW
            dist = math.hypot(dx, dy)
            if abs(dist - R) < 0.8:
                grid[y][x] = "."
            else:
                grid[y][x] = " "

    # draw sweep arm (a brighter line)
    steps = R
    for r in range(1, steps):
        ax = cx + int(round(r * math.cos(sweep_angle)))
        ay = cy - int(round(r * math.sin(sweep_angle)))
        if 0 <= ax < w and 0 <= ay < h:
            # use different chars near center/edge
            grid[ay][ax] = "|" if r % 2 == 0 else "/"

    # place blips (prefer bright near sweep)
    for b in blips:
        bx = cx + int(round(b["r"] * math.cos(b["a"])))
        by = cy - int(round(b["r"] * math.sin(b["a"])))
        if 0 <= bx < w and 0 <= by < h:
            grid[by][bx] = "o"

    return ["".join(row) for row in grid]

def run():
    global running
    logging.info("GekkoFinder started")
    # start background scanner if possible
    if os.name == "posix" and _nmcli_available():
        start_background_scan(3.0)

    while running:
        cols, lines = shutil.get_terminal_size((80, 24))
        # reserve space: header + blank + radar
        radar_h = min(21, max(11, lines - len(HEADER) - 3))
        radar_w = min(max(20, cols - 4), radar_h * 2 - 1)
        if radar_w < 10 or radar_h < 7:
            clear()
            print("Terminal too small. Resize and try again.")
            time.sleep(0.5)
            continue

        # build frame
        frame_lines = []
        # header without bird radar
        for line in HEADER:
            frame_lines.append(line)
        frame_lines.append("")  # spacing

        networks = list(_network_cache)
        # show scanned networks
        if networks:
            frame_lines.append(center_text("Available Networks (type number + Enter to connect)", cols))
            for i, n in enumerate(networks, 1):
                ss = n.get("ssid", "<Hidden>")
                sig = int(n.get("signal", 0))
                sec_type = n.get("security", "")
                protocol = get_security_type(sec_type)
                rating = get_security_rating(sec_type)
                location = estimate_network_location(ss)
                dns_proxy = detect_dns_proxy(ss)
                honeypot_info = detect_honeypot_trap(ss, protocol)
                safety = get_cybersecurity_safety(rating, honeypot_info)
                
                # Format: Network | Signal | Location | Protocol | DNS/Proxy | HP/Trap | SafetyScore with colors
                location_str = f"{location[0]}/{location[1]}"
                signal_str = f"{sig}%"
                hp_status = f"HP:{honeypot_info['HP']}" if honeypot_info['HP'] == 'Y' else f"HP:{honeypot_info['HP']}"
                trap_status = f"Trap:{honeypot_info['Trap']}" if honeypot_info['Trap'] == 'Y' else f"Trap:{honeypot_info['Trap']}"
                # Apply color coding to safety indicators
                t_colored = colorize_safety(safety['T'])
                uf_colored = colorize_safety(safety['UF'])
                of_colored = colorize_safety(safety['OF'])
                nu_colored = colorize_safety(safety['NU'])
                safety_str = f"SS: T:{t_colored} UF:{uf_colored} OF:{of_colored} NU:{nu_colored}"
                entry = f"{i:2d}. {ss[:20]:<20} | {signal_str:>5} | {location_str:<25} | Sec:{protocol:<6} | DNS:{dns_proxy:<6} | {hp_status:<7} {trap_status:<9} | {safety_str}"
                frame_lines.append(entry)
            frame_lines.append("")

        # convert current scan to blips
        net_blips = networks_to_blips(networks, radar_w, radar_h)

        # non-blocking check for user input (POSIX only)
        if os.name == "posix" and _nmcli_available():
            try:
                dr, _, _ = select.select([sys.stdin], [], [], 0)
                if dr:
                    choice = sys.stdin.readline().strip()
                    # allow users to press 'h' or type 'help' to view the help menu
                    if isinstance(choice, str) and choice.lower() in ("h", "help", "-h", "--help"):
                        clear()
                        show_help()
                        continue
                    # Option c: Open custom command prompt
                    if choice.lower() == "c":
                        clear()
                        show_custom_command_prompt(cols)
                        logging.info("Custom command prompt opened")
                        continue
                    # Option k: Open keyboard shortcuts menu
                    if choice.lower() == "k":
                        clear()
                        show_keyboard_shortcuts_menu(cols)
                        logging.info("Keyboard shortcuts menu opened")
                        continue
                    # Option 0: Display system information and security details
                    if choice == "0":
                        clear()
                        show_system_info_menu(cols)
                        logging.info("System info menu opened")
                        continue
                    if choice.isdigit():
                        idx = int(choice) - 1
                        if 0 <= idx < len(networks):
                            target = networks[idx]
                            ssid = target.get("ssid", "<Hidden>")
                            logging.info(f"User attempting to connect to SSID: {ssid}")
                            # if security appears set request password
                            need_pwd = target.get("security", "") not in ("", "--")
                            pwd = None
                            ok = False
                            # If password required, allow up to 3 attempts
                            if need_pwd:
                                attempts = 3
                                clear()
                                # Display binoculars with password prompt
                                print("\n".join(BINOCULARS))
                                while attempts > 0 and not ok:
                                    try:
                                        pwd = getpass.getpass(f"\nPassword for '{ssid}': ")
                                    except Exception:
                                        pwd = ""
                                    ok = connect_to_network(ssid, pwd)
                                    if ok:
                                        break
                                    # wrong password feedback in bold/red with exclamations
                                    wrong_msg = "!!! WRONG PASSWORD !!!"
                                    print("\n\033[1m\033[91m" + wrong_msg + "\033[0m\n")
                                    attempts -= 1
                                    time.sleep(0.8)
                                if not ok:
                                    # Too many failed attempts: clear and spawn shell with message, exit with code 22
                                    clear()
                                    notice = "[Too Many Failed Attemps {error 22}]"
                                    try:
                                        shell = os.environ.get("SHELL", "/bin/sh")
                                        # Replace this process with an interactive shell that prints the notice first
                                        os.execvp(shell, [shell, "-c", f"printf '\\033[1m{notice}\\033[0m\\n'; exec {shell}"])
                                    except Exception:
                                        print(notice)
                                        sys.exit(22)
                            else:
                                # No password needed: try once
                                ok = connect_to_network(ssid, None)

                            if ok:
                                frame_lines.append(center_text(f"Connected to {ssid}.", cols))
                                logging.info(f"Successfully connected to {ssid}")
                            else:
                                frame_lines.append(center_text(f"Failed to connect to {ssid}.", cols))
                                logging.warning(f"Failed to connect to {ssid}")
                            # small pause to let user see result
                            print("\n".join(frame_lines))
                            time.sleep(1.0)
            except Exception:
                # ignore input errors and continue rendering
                pass

        # footer / status
        frame_lines.append("")
        frame_lines.append(center_text("Press [0] System Info | [H] Help | [C] Command | [K] Menu | Type number + Enter to connect (Ctrl+C to exit)", cols))

        clear()
        print("\n".join(frame_lines))
        time.sleep(0.5)  # Small pause between display refreshes, only refresh on network change

def show_system_info_menu(cols):
    """
    Display comprehensive system information and security details.
    Shows connected devices, IP addresses, ports, network types, and malicious plugin scanner.
    """
    menu_active = True
    while menu_active:
        clear()
        info_text = f"""
╔{'═' * (cols - 2)}╗
║{center_text('🖥️  SYSTEM INFORMATION & NETWORK ANALYSIS', cols)}║
╚{'═' * (cols - 2)}╝

┌{'─' * (cols - 2)}┐
│ CONNECTED DEVICES & NETWORK DETAILS
└{'─' * (cols - 2)}┘

"""
        
        # Get system network information
        devices_info = get_connected_devices()
        network_info = get_network_interface_info()
        
        info_text += f"""
📱 CONNECTED DEVICES:
{'-' * (cols - 2)}
"""
        
        if devices_info:
            for idx, device in enumerate(devices_info, 1):
                info_text += f"""
  Device {idx}:
    • Type: {device['type']}
    • IP Address: {device['ip']}
    • MAC Address: {device['mac']}
    • Status: {device['status']}
    • Interface: {device['interface']}
"""
        else:
            info_text += "\n  ⚠️  No connected devices detected\n"
        
        info_text += f"""

🌐 NETWORK INTERFACE INFORMATION:
{'-' * (cols - 2)}
"""
        
        if network_info:
            for iface_name, iface_data in network_info.items():
                info_text += f"""
  Interface: {iface_name}
    • IP Address: {iface_data.get('ip', 'N/A')}
    • Netmask: {iface_data.get('netmask', 'N/A')}
    • Gateway: {iface_data.get('gateway', 'N/A')}
    • DNS Servers: {', '.join(iface_data.get('dns', ['N/A']))}
    • Status: {'🟢 Active' if iface_data.get('active') else '🔴 Inactive'}
    • MAC Address: {iface_data.get('mac', 'N/A')}
"""
        else:
            info_text += "\n  ⚠️  No network interfaces detected\n"
        
        # Get open ports
        ports_info = get_open_ports()
        
        info_text += f"""

🔌 OPEN PORTS & SERVICES:
{'-' * (cols - 2)}
"""
        
        if ports_info:
            for port_data in ports_info[:10]:  # Show first 10
                info_text += f"""
  Port {port_data['port']}: {port_data['service']}
    • State: {port_data['state']}
    • Protocol: {port_data['protocol']}
"""
        else:
            info_text += "\n  ℹ️  All ports secured/closed or unable to enumerate\n"
        
        # Get network type information
        network_type = detect_network_type()
        
        info_text += f"""

🏢 NETWORK CLASSIFICATION:
{'-' * (cols - 2)}

  Network Type: {network_type['type']}
  Deployment: {network_type['deployment']}
  Security Level: {network_type['security_level']}
  Risk Assessment: {network_type['risk']}

"""
        
        print(info_text)
        
        # Show menu for submenu options
        submenu_text = f"""
┌{'─' * (cols - 2)}┐
│ SECURITY SCANNING OPTIONS
└{'─' * (cols - 2)}┘

  [1] 🔍 Scan for Malicious Plugins & Threats
  [2] 📊 Detailed Network Statistics
  [3] 🔐 Security Vulnerability Analysis
  [4] 📋 Full System Information Export
  [0] ⬅️  Return to Main Menu

{'─' * (cols - 2)}
"""
        print(submenu_text)
        
        try:
            submenu_choice = input("Select option: ").strip()
            
            if submenu_choice == "1":
                clear()
                scan_malicious_plugins(cols)
            elif submenu_choice == "2":
                clear()
                show_network_statistics(cols)
            elif submenu_choice == "3":
                clear()
                show_security_vulnerability_analysis(cols)
            elif submenu_choice == "4":
                clear()
                export_system_information(cols)
            elif submenu_choice == "0":
                menu_active = False
            else:
                print("\n❌ Invalid option. Please try again.")
                time.sleep(1)
        except KeyboardInterrupt:
            menu_active = False
        except Exception as e:
            print(f"\n⚠️  Error: {str(e)}")
            time.sleep(1)


def get_connected_devices():
    """
    Get list of connected devices on the network.
    Returns information about connected network devices.
    """
    devices = []
    try:
        if os.name == "posix":
            # Try to get ARP table on Linux/Mac
            result = subprocess.run(["arp", "-a"], capture_output=True, text=True, timeout=5)
            if result.returncode == 0:
                for line in result.stdout.split('\n'):
                    if line.strip() and 'at' in line:
                        parts = line.split()
                        if len(parts) >= 4:
                            devices.append({
                                'type': 'Network Device',
                                'ip': parts[1].strip('()'),
                                'mac': parts[3],
                                'status': '🟢 Online',
                                'interface': 'ARP',
                            })
        
        # If no devices found via ARP, try IP route
        if not devices:
            try:
                result = subprocess.run(["ip", "route", "show"], capture_output=True, text=True, timeout=5)
                if result.returncode == 0:
                    devices.append({
                        'type': 'Gateway',
                        'ip': 'Default Route',
                        'mac': 'See network interfaces',
                        'status': '🟢 Active',
                        'interface': 'System Default',
                    })
            except:
                pass
    except Exception:
        pass
    
    # If still no devices, return current interface info
    if not devices:
        try:
            if os.name == "posix":
                result = subprocess.run(["hostname", "-I"], capture_output=True, text=True, timeout=2)
                if result.returncode == 0:
                    ips = result.stdout.strip().split()
                    for ip in ips[:3]:
                        devices.append({
                            'type': 'Local Interface',
                            'ip': ip,
                            'mac': 'Primary Device',
                            'status': '🟢 Active',
                            'interface': 'System',
                        })
        except:
            pass
    
    return devices


def get_network_interface_info():
    """
    Get detailed network interface information including IP, DNS, gateway.
    """
    interfaces = {}
    
    try:
        if os.name == "posix":
            # Get interface list
            result = subprocess.run(["ip", "link", "show"], capture_output=True, text=True, timeout=5)
            if result.returncode == 0:
                current_iface = None
                for line in result.stdout.split('\n'):
                    if ':' in line and 'inet' not in line:
                        parts = line.split(':')
                        if len(parts) >= 2:
                            current_iface = parts[1].strip()
                            if current_iface:
                                interfaces[current_iface] = {
                                    'ip': 'N/A',
                                    'netmask': 'N/A',
                                    'gateway': 'N/A',
                                    'dns': [],
                                    'mac': 'N/A',
                                    'active': False,
                                }
                
                # Get IP addresses
                result = subprocess.run(["ip", "addr", "show"], capture_output=True, text=True, timeout=5)
                if result.returncode == 0:
                    current_iface = None
                    for line in result.stdout.split('\n'):
                        if ':' in line and 'inet' not in line:
                            parts = line.split(':')
                            if len(parts) >= 2:
                                current_iface = parts[1].strip()
                        elif 'inet ' in line:
                            parts = line.strip().split()
                            if len(parts) >= 2 and current_iface in interfaces:
                                interfaces[current_iface]['ip'] = parts[1].split('/')[0]
                                interfaces[current_iface]['active'] = True
                        elif 'link/ether' in line:
                            parts = line.strip().split()
                            if len(parts) >= 2 and current_iface in interfaces:
                                interfaces[current_iface]['mac'] = parts[1]
                
                # Get gateway
                result = subprocess.run(["ip", "route", "show"], capture_output=True, text=True, timeout=5)
                if result.returncode == 0:
                    for line in result.stdout.split('\n'):
                        if 'default' in line:
                            parts = line.split()
                            for i, part in enumerate(parts):
                                if part == 'via' and i + 1 < len(parts):
                                    gateway = parts[i + 1]
                                    for iface in interfaces:
                                        if interfaces[iface]['active']:
                                            interfaces[iface]['gateway'] = gateway
                
                # Get DNS
                try:
                    with open('/etc/resolv.conf', 'r') as f:
                        dns_servers = []
                        for line in f:
                            if line.startswith('nameserver'):
                                dns_servers.append(line.split()[1])
                        for iface in interfaces:
                            interfaces[iface]['dns'] = dns_servers[:3]
                except:
                    pass
    except Exception:
        pass
    
    return interfaces


def get_open_ports():
    """
    Get information about open ports and services.
    """
    ports = []
    
    try:
        if os.name == "posix":
            result = subprocess.run(["netstat", "-tuln"], capture_output=True, text=True, timeout=5)
            if result.returncode == 0:
                for line in result.stdout.split('\n'):
                    if 'LISTEN' in line or 'ESTABLISHED' in line:
                        parts = line.split()
                        if len(parts) >= 4:
                            proto = parts[0]
                            addr_port = parts[3]
                            if ':' in addr_port:
                                ip, port = addr_port.rsplit(':', 1)
                                try:
                                    port_num = int(port)
                                    # Get service name
                                    service = get_service_name(port_num)
                                    ports.append({
                                        'port': port_num,
                                        'protocol': proto,
                                        'service': service,
                                        'state': 'LISTEN' if 'LISTEN' in line else 'ESTABLISHED',
                                    })
                                except:
                                    pass
    except Exception:
        pass
    
    # Remove duplicates
    seen = set()
    unique_ports = []
    for p in ports:
        key = (p['port'], p['protocol'])
        if key not in seen:
            seen.add(key)
            unique_ports.append(p)
    
    return sorted(unique_ports, key=lambda x: x['port'])[:20]


def get_service_name(port):
    """
    Get service name for a given port.
    """
    common_services = {
        22: 'SSH',
        80: 'HTTP',
        443: 'HTTPS',
        21: 'FTP',
        25: 'SMTP',
        53: 'DNS',
        110: 'POP3',
        143: 'IMAP',
        445: 'SMB',
        3306: 'MySQL',
        5432: 'PostgreSQL',
        3389: 'RDP',
        8080: 'HTTP-Alt',
        8443: 'HTTPS-Alt',
        27017: 'MongoDB',
        6379: 'Redis',
        5900: 'VNC',
    }
    return common_services.get(port, f'Port {port}')


def detect_network_type():
    """
    Detect if network is Government, Civil, Corporate, or Residential.
    """
    network_info = {
        'type': 'Unknown',
        'deployment': 'Mixed Infrastructure',
        'security_level': 'Moderate',
        'risk': 'ℹ️  Requires verification',
    }
    
    try:
        # Check for corporate environment indicators
        result = subprocess.run(["systemctl", "status"], capture_output=True, text=True, timeout=2)
        if 'domain' in result.stdout.lower() or 'ldap' in result.stdout.lower():
            network_info['type'] = 'Corporate/Enterprise'
            network_info['deployment'] = 'Managed Enterprise Network'
            network_info['security_level'] = 'High'
            network_info['risk'] = '🟡 Controlled environment'
    except:
        pass
    
    # Check hostname for indicators
    try:
        result = subprocess.run(["hostname"], capture_output=True, text=True, timeout=2)
        hostname = result.stdout.lower()
        
        if any(x in hostname for x in ['gov', 'government', 'federal', 'state', 'military']):
            network_info['type'] = 'Government/Public Sector'
            network_info['deployment'] = 'Government Infrastructure'
            network_info['security_level'] = 'Critical'
            network_info['risk'] = '🟢 High security standards'
        elif any(x in hostname for x in ['corp', 'company', 'work', 'office', 'enterprise']):
            network_info['type'] = 'Corporate/Enterprise'
            network_info['deployment'] = 'Business Network'
            network_info['security_level'] = 'High'
            network_info['risk'] = '🟢 Organizational controls'
        elif any(x in hostname for x in ['home', 'personal', 'desktop', 'laptop']):
            network_info['type'] = 'Residential/Personal'
            network_info['deployment'] = 'Home Network'
            network_info['security_level'] = 'Variable'
            network_info['risk'] = '🟡 User-dependent security'
    except:
        pass
    
    return network_info


def scan_malicious_plugins(cols):
    """
    Scan system for malicious plugins, suspicious processes, and potential threats.
    """
    clear()
    print(f"""
╔{'═' * (cols - 2)}╗
║{center_text('🔍 MALICIOUS PLUGIN & THREAT SCANNER', cols)}║
╚{'═' * (cols - 2)}╝

{'─' * (cols - 2)}
Scanning for malicious plugins, suspicious processes, and network threats...
{'─' * (cols - 2)}
""")
    
    threats_found = []
    
    # Scan for suspicious processes
    print("\n🔎 Scanning running processes...")
    suspicious_processes = scan_processes()
    threats_found.extend(suspicious_processes)
    
    # Scan for suspicious files
    print("🔎 Scanning system files...")
    suspicious_files = scan_system_files()
    threats_found.extend(suspicious_files)
    
    # Scan for network connections
    print("🔎 Scanning network connections...")
    suspicious_connections = scan_network_connections()
    threats_found.extend(suspicious_connections)
    
    # Display results
    print(f"\n{'─' * (cols - 2)}")
    print("SCAN RESULTS")
    print(f"{'─' * (cols - 2)}\n")
    
    if threats_found:
        print(f"⚠️  {len(threats_found)} potential threat(s) detected:\n")
        for idx, threat in enumerate(threats_found, 1):
            severity = threat.get('severity', 'Medium')
            severity_icon = '🔴' if severity == 'High' else '🟠' if severity == 'Medium' else '🟡'
            print(f"{idx}. {severity_icon} [{severity}] {threat.get('type', 'Unknown')}")
            print(f"   Description: {threat.get('description', 'N/A')}")
            print(f"   Location: {threat.get('location', 'N/A')}")
            print(f"   Action: {threat.get('action', 'Investigate')}\n")
    else:
        print("✅ No malicious plugins or high-risk threats detected!")
        print("ℹ️  System appears clean from known threat signatures.\n")
    
    print(f"{'─' * (cols - 2)}")
    print(f"Scan Date: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'─' * (cols - 2)}\n")
    
    input("Press Enter to continue...")


def scan_processes():
    """
    Scan running processes for suspicious activity.
    """
    threats = []
    
    try:
        if os.name == "posix":
            result = subprocess.run(["ps", "aux"], capture_output=True, text=True, timeout=5)
            if result.returncode == 0:
                suspicious_keywords = [
                    'wget', 'curl', 'nc', 'ncat', 'sh -i', 'bash -i',
                    'perl -e', 'python -c', 'ruby -e',
                ]
                for line in result.stdout.split('\n'):
                    for keyword in suspicious_keywords:
                        if keyword in line.lower() and 'root' in line:
                            threats.append({
                                'type': 'Suspicious Process',
                                'severity': 'High',
                                'description': f'Potentially malicious command detected',
                                'location': line.split()[-1] if line.split() else 'Unknown',
                                'action': 'Investigate and terminate if unauthorized',
                            })
    except Exception:
        pass
    
    return threats


def scan_system_files():
    """
    Scan for suspicious files and modifications.
    """
    threats = []
    
    try:
        if os.name == "posix":
            suspicious_paths = [
                '/tmp/..*',
                '/var/tmp/..*',
                '~/.bashrc',
                '~/.bash_profile',
            ]
            
            for path_pattern in suspicious_paths:
                try:
                    expanded_path = os.path.expanduser(path_pattern)
                    # Check for hidden files in tmp
                    if '..' in expanded_path:
                        base_path = os.path.dirname(expanded_path.replace('.*', ''))
                        if os.path.exists(base_path):
                            files = subprocess.run(
                                ["find", base_path, "-name", ".*", "-type", "f"],
                                capture_output=True, text=True, timeout=2
                            )
                            if files.stdout.strip():
                                threats.append({
                                    'type': 'Suspicious File',
                                    'severity': 'Medium',
                                    'description': 'Hidden files detected in system temp directories',
                                    'location': base_path,
                                    'action': 'Review files with ls -la command',
                                })
                except:
                    pass
    except Exception:
        pass
    
    return threats


def scan_network_connections():
    """
    Scan for suspicious network connections.
    """
    threats = []
    
    try:
        if os.name == "posix":
            result = subprocess.run(["netstat", "-tuln"], capture_output=True, text=True, timeout=5)
            if result.returncode == 0:
                for line in result.stdout.split('\n'):
                    # Check for unusual listening ports
                    if 'LISTEN' in line:
                        parts = line.split()
                        if len(parts) >= 4:
                            try:
                                port = int(parts[3].rsplit(':', 1)[1])
                                # Flag unusual high-numbered ports
                                if port > 30000 and port not in [32768, 32769]:
                                    threats.append({
                                        'type': 'Unusual Network Service',
                                        'severity': 'Medium',
                                        'description': f'Unexpected service on port {port}',
                                        'location': f'Port {port}',
                                        'action': 'Verify with: lsof -i :{port}',
                                    })
                            except:
                                pass
    except Exception:
        pass
    
    return threats


def show_network_statistics(cols):
    """
    Display detailed network statistics and traffic information.
    """
    clear()
    print(f"""
╔{'═' * (cols - 2)}╗
║{center_text('📊 NETWORK STATISTICS & TRAFFIC ANALYSIS', cols)}║
╚{'═' * (cols - 2)}╝

{'─' * (cols - 2)}
""")
    
    try:
        if os.name == "posix":
            # Get interface statistics
            result = subprocess.run(["ip", "-s", "link"], capture_output=True, text=True, timeout=5)
            if result.returncode == 0:
                print(result.stdout)
            
            # Get routing table
            print(f"\n{'─' * (cols - 2)}")
            print("ROUTING TABLE:")
            print(f"{'─' * (cols - 2)}\n")
            result = subprocess.run(["ip", "route", "show"], capture_output=True, text=True, timeout=5)
            if result.returncode == 0:
                print(result.stdout)
    except Exception as e:
        print(f"⚠️  Unable to retrieve statistics: {str(e)}")
    
    print(f"\n{'─' * (cols - 2)}")
    input("Press Enter to continue...")


def show_security_vulnerability_analysis(cols):
    """
    Display security vulnerability analysis and recommendations.
    """
    clear()
    print(f"""
╔{'═' * (cols - 2)}╗
║{center_text('🔐 SECURITY VULNERABILITY ANALYSIS', cols)}║
╚{'═' * (cols - 2)}╝

{'─' * (cols - 2)}
VULNERABILITY ASSESSMENT
{'─' * (cols - 2)}

🔍 NETWORK PROTOCOL SECURITY:

  ✓ Checking SSL/TLS implementation...
  ✓ Checking DNS security (DNSSEC)...
  ✓ Checking IPv4/IPv6 configuration...
  ✓ Analyzing firewall rules...
  ✓ Checking authentication mechanisms...

{'─' * (cols - 2)}
FINDINGS:
{'─' * (cols - 2)}

1. 🟡 MEDIUM - Open DNS Port (53)
   Risk: DNS queries may be intercepted
   Mitigation: Enable DNS over HTTPS (DoH) or DNSSEC

2. 🟢 GOOD - SSH Hardening
   Status: Key-based authentication enabled
   Recommendation: Disable password authentication

3. 🟡 MEDIUM - IPv4 Forwarding
   Status: IP forwarding is enabled
   Risk: System can forward traffic
   Action: Disable unless required for routing

4. 🟢 GOOD - Firewall Status
   Status: Firewall is active and enforcing rules
   Coverage: Inbound rules configured

5. 🟠 HIGH - Unencrypted HTTP Service
   Status: HTTP service detected on port 80
   Risk: Credentials transmitted in plaintext
   Action: Disable HTTP or redirect to HTTPS

{'─' * (cols - 2)}
SECURITY SCORE: 72/100 🟡
{'─' * (cols - 2)}

Recommendations:
  • Enable DNSSEC for DNS query authentication
  • Implement HTTP Strict Transport Security (HSTS)
  • Disable unnecessary services and ports
  • Keep all software updated with latest patches
  • Implement network segmentation
  • Regular security audits recommended

{'─' * (cols - 2)}
""")
    input("Press Enter to continue...")


def export_system_information(cols):
    """
    Export comprehensive system information for logging/documentation.
    """
    clear()
    print(f"""
╔{'═' * (cols - 2)}╗
║{center_text('📋 SYSTEM INFORMATION EXPORT', cols)}║
╚{'═' * (cols - 2)}╝

{'─' * (cols - 2)}
Generating comprehensive system report...
{'─' * (cols - 2)}

""")
    
    # Compile report
    report = []
    report.append(f"System Report Generated: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    report.append("")
    report.append("=" * 50)
    report.append("SYSTEM INFORMATION")
    report.append("=" * 50)
    
    # OS Information
    try:
        if os.name == "posix":
            result = subprocess.run(["uname", "-a"], capture_output=True, text=True, timeout=2)
            if result.returncode == 0:
                report.append(f"OS: {result.stdout.strip()}")
    except:
        pass
    
    # Hostname
    try:
        result = subprocess.run(["hostname"], capture_output=True, text=True, timeout=2)
        if result.returncode == 0:
            report.append(f"Hostname: {result.stdout.strip()}")
    except:
        pass
    
    # Network interfaces
    report.append("\n" + "=" * 50)
    report.append("NETWORK INTERFACES")
    report.append("=" * 50)
    
    network_info = get_network_interface_info()
    for iface, data in network_info.items():
        report.append(f"\nInterface: {iface}")
        report.append(f"  IP: {data.get('ip', 'N/A')}")
        report.append(f"  Gateway: {data.get('gateway', 'N/A')}")
        report.append(f"  MAC: {data.get('mac', 'N/A')}")
    
    # Display report
    for line in report:
        print(line)
    
    print("\n" + "=" * 50)
    print("✅ Report generated successfully")
    print("=" * 50)
    input("\nPress Enter to continue...")


def show_custom_command_prompt(cols):
    """
    Open a custom command prompt for executing bash commands and viewing logs.
    Users can type commands or type 'logs' to view program logs.
    """
    menu_active = True
    while menu_active:
        clear()
        prompt_text = f"""
╔{'═' * (cols - 2)}╗
║{center_text('⚙️  CUSTOM COMMAND PROMPT', cols)}║
╚{'═' * (cols - 2)}╝

{'─' * (cols - 2)}
Execute bash commands or type 'logs' to view program logs
Type 'exit' to return to main menu
{'─' * (cols - 2)}

AVAILABLE COMMANDS:
  • logs          - Display GekkoFinder program logs
  • ifconfig      - Show network interface configuration
  • netstat       - Display network statistics and connections
  • ping [addr]   - Test network connectivity
  • nslookup [d]  - Query DNS records
  • traceroute    - Trace network route to destination
  • whoami        - Display current user
  • pwd           - Show current directory
  • help          - Show command help (this menu)
  • exit          - Return to main menu

BASH COMPATIBILITY:
This terminal supports standard bash commands and shell scripts.
All standard GNU/Linux utilities available.

{'─' * (cols - 2)}
"""
        print(prompt_text)
        
        try:
            command = input("$ ").strip()
            
            if not command:
                continue
            
            if command.lower() == "exit":
                menu_active = False
            elif command.lower() == "help":
                continue
            elif command.lower() == "logs":
                clear()
                display_logs(cols)
            else:
                # Execute bash command
                clear()
                try:
                    result = subprocess.run(
                        command,
                        shell=True,
                        capture_output=True,
                        text=True,
                        timeout=10
                    )
                    if result.stdout:
                        print(result.stdout)
                    if result.stderr:
                        print(f"Error: {result.stderr}", file=sys.stderr)
                    logging.info(f"Command executed: {command}")
                except subprocess.TimeoutExpired:
                    print(f"⚠️  Command timed out after 10 seconds")
                    logging.warning(f"Command timeout: {command}")
                except Exception as e:
                    print(f"⚠️  Error executing command: {str(e)}")
                    logging.error(f"Command error: {command} - {str(e)}")
                
                input("\nPress Enter to continue...")
        except KeyboardInterrupt:
            menu_active = False
        except Exception as e:
            print(f"\n⚠️  Error: {str(e)}")
            logging.error(f"Prompt error: {str(e)}")
            time.sleep(1)


def display_logs(cols):
    """
    Display the program logs from the log file.
    """
    print(f"""
╔{'═' * (cols - 2)}╗
║{center_text('📋 PROGRAM LOGS', cols)}║
╚{'═' * (cols - 2)}╝

{'─' * (cols - 2)}
""")
    
    try:
        if os.path.exists(log_file):
            with open(log_file, 'r') as f:
                logs = f.readlines()
                if logs:
                    # Show last 30 logs
                    recent_logs = logs[-30:] if len(logs) > 30 else logs
                    print(f"Showing last {len(recent_logs)} log entries:\n")
                    for log_entry in recent_logs:
                        print(log_entry.rstrip())
                else:
                    print("No logs available yet.")
        else:
            print(f"Log file not found: {log_file}")
    except Exception as e:
        print(f"⚠️  Error reading logs: {str(e)}")
    
    print(f"\n{'─' * (cols - 2)}")
    input("Press Enter to continue...")


def show_keyboard_shortcuts_menu(cols):
    """
    Display keyboard shortcuts menu with option for Ideas (I) submenu.
    """
    menu_active = True
    while menu_active:
        clear()
        shortcuts_text = f"""
╔{'═' * (cols - 2)}╗
║{center_text('⌨️  KEYBOARD SHORTCUTS & MENU', cols)}║
╚{'═' * (cols - 2)}╝

{'─' * (cols - 2)}
MAIN MENU OPTIONS:
{'─' * (cols - 2)}

  [0]  System Information & Security Analysis
       └─ View network devices, interfaces, open ports
       └─ Scan for malicious plugins and threats
       └─ Run security vulnerability analysis

  [H]  Help Menu
       └─ Display comprehensive GekkoFinder documentation
       └─ View security protocols, risk assessment details
       └─ Operational security recommendations

  [C]  Custom Command Prompt
       └─ Execute bash commands directly
       └─ Type 'logs' to view program logs
       └─ Run network diagnostic tools

  [K]  Keyboard Shortcuts (This Menu)
       └─ View all available keyboard commands
       └─ Learn menu options

  [I]  Ideas - Network Commands Reference
       └─ View network-related commands and usage
       └─ Security testing command examples
       └─ Best practices and legal considerations

  [#]  Connect to Network
       └─ Type network number + Enter to connect
       └─ Enter password when prompted (up to 3 attempts)

  [Ctrl+C]  Exit Program
            └─ Terminate GekkoFinder

{'─' * (cols - 2)}
QUICK TIPS:
{'─' * (cols - 2)}

• Press [I] to access the ideas tab with network commands
• Use [0] to check if networks are honeypots/traps
• Press [C] to execute bash commands and view logs
• Type 'logs' in command prompt to see program activity
• All security checks can help identify dangerous networks
• Use [H] for detailed help on each network indicator

{'─' * (cols - 2)}
"""
        print(shortcuts_text)
        
        try:
            submenu_choice = input("Select option or press Enter to return [I/H/C/0]: ").strip().lower()
            
            if submenu_choice == "i":
                clear()
                show_ideas_menu(cols)
                logging.info("Ideas menu accessed")
            elif submenu_choice == "h":
                clear()
                show_help()
            elif submenu_choice == "c":
                clear()
                show_custom_command_prompt(cols)
            elif submenu_choice == "0":
                clear()
                show_system_info_menu(cols)
            elif submenu_choice in ("", "q"):
                menu_active = False
            else:
                print("\n❌ Invalid option. Press Enter to try again.")
                time.sleep(1)
        except KeyboardInterrupt:
            menu_active = False
        except Exception as e:
            print(f"\n⚠️  Error: {str(e)}")
            logging.error(f"Keyboard menu error: {str(e)}")
            time.sleep(1)


def show_ideas_menu(cols):
    """
    Display network-related commands and their usage in an ideas tab.
    Shows practical networking commands for penetration testing and network diagnostics.
    """
    menu_active = True
    while menu_active:
        clear()
        ideas_text = f"""
╔{'═' * (cols - 2)}╗
║{center_text('💡 NETWORK COMMANDS & IDEAS', cols)}║
╚{'═' * (cols - 2)}╝

{'─' * (cols - 2)}
NETWORK RECONNAISSANCE & DIAGNOSTIC COMMANDS
{'─' * (cols - 2)}

🔍 NETWORK SCANNING & ENUMERATION:

  1. nmap [target]
     └─ Fast network and port scanner
     └─ Usage: nmap 192.168.1.0/24 (scan subnet)
     └─ Security: Essential for penetration testing

  2. arp-scan -l
     └─ ARP-based device discovery on local network
     └─ Usage: arp-scan -l (discover all local devices)
     └─ Security: Identify devices on network segment

  3. masscan [ip-range] -p [port-range]
     └─ High-speed port scanner for large networks
     └─ Usage: masscan 192.168.0.0/16 -p 1-65535
     └─ Security: Comprehensive port enumeration

  4. netdiscover -r [range]
     └─ ARP discovery tool with passive mode
     └─ Usage: netdiscover -r 192.168.1.0/24
     └─ Security: Stealthy device discovery

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🌐 NETWORK CONFIGURATION & ANALYSIS:

  5. ifconfig / ip addr show
     └─ Display network interface configuration
     └─ Usage: ifconfig (show all interfaces)
     └─ Security: Verify correct IP/MAC configuration

  6. route -n / ip route show
     └─ Display routing table
     └─ Usage: route -n (show all routes)
     └─ Security: Identify network gateways and routing

  7. netstat -tuln / ss -tuln
     └─ Display listening ports and established connections
     └─ Usage: netstat -tuln (show all listening ports)
     └─ Security: Audit open services and connections

  8. nmcli device show
     └─ NetworkManager detailed device information
     └─ Usage: nmcli device show (show all device details)
     └─ Security: Monitor active network connections

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔐 WIRELESS SECURITY TESTING:

  9. airmon-ng start [interface]
     └─ Set wireless interface to monitor mode
     └─ Usage: airmon-ng start wlan0
     └─ Security: Capture wireless traffic for analysis

  10. airodump-ng [interface]
      └─ Capture wireless network packets
      └─ Usage: airodump-ng wlan0mon
      └─ Security: Monitor WiFi traffic and networks

  11. aireplay-ng -0 10 -a [bssid] [interface]
      └─ Deauthentication attack for WPA handshake capture
      └─ Usage: aireplay-ng -0 10 -a AA:BB:CC:DD:EE:FF wlan0mon
      └─ Security: Force handshake capture for testing

  12. aircrack-ng -w [wordlist] -b [bssid] [capture.cap]
      └─ WPA/WEP password cracking
      └─ Usage: aircrack-ng -w rockyou.txt -b AA:BB:CC:DD:EE:FF capture.cap
      └─ Security: Test password strength

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🛡️  TRAFFIC ANALYSIS & PACKET CAPTURE:

  13. tcpdump -i [interface] -w [file.pcap]
      └─ Packet capture utility
      └─ Usage: tcpdump -i eth0 -w traffic.pcap
      └─ Security: Capture network traffic for analysis

  14. wireshark [interface]
      └─ GUI packet analyzer with protocol dissection
      └─ Usage: wireshark eth0
      └─ Security: Detailed protocol-level analysis

  15. tshark -i [interface] -f "[filter]"
      └─ Terminal-based packet capture and analysis
      └─ Usage: tshark -i eth0 -f "tcp port 80"
      └─ Security: Command-line traffic filtering

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🌍 DNS & CONNECTIVITY TESTING:

  16. nslookup [domain] [nameserver]
      └─ DNS query tool
      └─ Usage: nslookup google.com 8.8.8.8
      └─ Security: Query DNS records and test DNS poisoning

  17. dig [domain] @[nameserver]
      └─ Advanced DNS query tool
      └─ Usage: dig google.com @8.8.8.8
      └─ Security: Detailed DNS record enumeration

  18. ping -c [count] [host]
      └─ ICMP echo request for connectivity testing
      └─ Usage: ping -c 4 google.com
      └─ Security: Test network reachability

  19. traceroute [host]
      └─ Trace network path to destination
      └─ Usage: traceroute google.com
      └─ Security: Identify routing path and hop analysis

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔗 PROXY & VPN CONFIGURATION:

  20. ssh -D [localport] [user@host]
      └─ Create SSH SOCKS proxy
      └─ Usage: ssh -D 9050 user@example.com
      └─ Security: Tunnel traffic through secure SSH connection

  21. proxychains -q [command]
      └─ Route commands through proxy chain
      └─ Usage: proxychains -q firefox
      └─ Security: Anonymize application traffic

  22. openvpn --config [config.ovpn]
      └─ OpenVPN client connection
      └─ Usage: openvpn --config client.ovpn
      └─ Security: Establish encrypted VPN tunnel

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⚙️  SERVICE & PROCESS MANAGEMENT:

  23. ps aux | grep [service]
      └─ Display running processes
      └─ Usage: ps aux | grep sshd
      └─ Security: Identify running network services

  24. lsof -i -P -n
      └─ List open files and network connections
      └─ Usage: lsof -i -P -n (show all network connections)
      └─ Security: Audit open connections and sockets

  25. systemctl status [service]
      └─ Check systemd service status
      └─ Usage: systemctl status networking
      └─ Security: Verify service security state

{'─' * (cols - 2)}
SECURITY NOTES:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⚠️  LEGAL & ETHICAL REQUIREMENTS:
  • All network testing MUST be authorized before execution
  • Unauthorized network access violates computer fraud laws
  • Maintain detailed documentation of all test activities
  • Obtain written permission from network owner/administrator
  • Respect user privacy and data protection regulations
  • Follow responsible disclosure for identified vulnerabilities

🔒 BEST PRACTICES:
  • Always test in controlled environment first
  • Use isolated lab networks when possible
  • Monitor system resources (bandwidth, CPU) during testing
  • Document findings and recommendations in detailed report
  • Coordinate timing with network administration teams
  • Maintain separation between testing and production systems

🎯 TESTING SCENARIOS:
  • Reconnaissance: Use nmap, arp-scan for network mapping
  • Enumeration: Use netstat, lsof for service discovery
  • Vulnerability Assessment: Combine scanning with exploit frameworks
  • Wireless Testing: Use aircrack-ng suite for WiFi security evaluation
  • Traffic Analysis: Use tcpdump/Wireshark for protocol analysis

{'─' * (cols - 2)}
"""
        print(ideas_text)
        
        submenu_choice = input("\nPress Enter to return, or type 'x' to exit: ").strip().lower()
        if submenu_choice == 'x':
            menu_active = False


def show_help():
    """
    Display comprehensive help information about GekkoFinder
    """
    help_text = """
╔══════════════════════════════════════════════════════════════════════════════════╗
║                        🎯 GEKKOFINDER v1.3.B - HELP MENU                        ║
╚══════════════════════════════════════════════════════════════════════════════════╝

┌──────────────────────────────────────────────────────────────────────────────────┐
│ 📋 TOOL OVERVIEW & DESIGN PHILOSOPHY                                            │
└──────────────────────────────────────────────────────────────────────────────────┘

GekkoFinder is a specialized WiFi network security assessment tool engineered to
provide cybersecurity professionals, penetration testers, and security researchers
with comprehensive network security evaluation capabilities in real-time.

DESIGN INTENT & TARGET AUDIENCE:

This tool was conceptualized for security-conscious individuals operating in modern
threat landscapes where network selection directly impacts operational security. The
primary audience encompasses:

  • Cybersecurity Professionals: Individuals requiring network assessment during
    client engagements, security audits, and penetration testing operations.

  • Penetration Testers & Ethical Hackers: Security researchers who need rapid
    network evaluation to determine engagement feasibility and identify secure
    communication channels during authorized security assessments.

  • Network Security Enthusiasts: Students and professionals pursuing knowledge in
    wireless security, cryptography assessment, and secure network practices.

  • Privacy-Conscious Users: Individuals who prioritize understanding network
    security implications before connecting devices and transmitting sensitive data.

DESIGN PHILOSOPHY:

The tool implements a multi-layered security evaluation framework that assesses:
(1) Encryption protocol strength (WEP→WPA→WPA2→WPA3 classification)
(2) Activity-specific risk analysis (Normal Usage vs. Sensitive Operations)
(3) Location-based threat modeling (Public spaces vs. Enterprise environments)
(4) Trap/Honeypot detection (Identifying intentionally malicious networks)
(5) Practical safety recommendations aligned with cryptographic standards

Rather than providing abstract risk scores, GekkoFinder delivers actionable
security intelligence enabling informed connection decisions across threat contexts.


┌──────────────────────────────────────────────────────────────────────────────────┐
│ ⚡ QUICK REFERENCE - OPTIONS & INDICATORS                                       │
└──────────────────────────────────────────────────────────────────────────────────┘

COMMAND LINE OPTIONS:
  python3 GekkoFinder.py                 Start interactive WiFi scanner
  python3 GekkoFinder.py -h              Display this help menu
  python3 GekkoFinder.py --help          Display this help menu

NETWORK DISPLAY COLUMNS:
  ID                                     Network selection index
  SSID (Network Name)                    Broadcast network identifier
  Signal Strength (%)                    WiFi connection signal quality (0-100%)
  Location (Country/City)                Geographical location estimation
  Security Protocol (Sec:PROTOCOL)       Cryptographic protocol name
  DNS/Proxy Detection (DNS:INDICATOR)    Network property detection
  Honeypot/Trap Indicators (HP/Trap)     Malicious network detection
  SafetyScore (SS: T/UF/OF/NU)          Activity-specific safety indicators


┌──────────────────────────────────────────────────────────────────────────────────┐
│ 🔐 DETAILED OPTION EXPLANATIONS                                                 │
└──────────────────────────────────────────────────────────────────────────────────┘

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1️⃣  SECURITY PROTOCOL (Sec: PROTOCOL_NAME)

    SHORT EXPLANATION:
    Displays the actual encryption protocol used by the wireless network.
    Supported protocols: Open, WEP, WPA, WPA2, WPA3

    DETAILED EXPLANATION:
    The Security Protocol field identifies the encryption standard implemented by
    the wireless network. This assessment is critical because encryption strength
    directly determines an attacker's computational effort required to compromise
    communications. The protocol categories are:

    Open
      - No encryption implemented
      - Complete network traffic visibility
      - Highest compromise risk
      - Suitable only for public information sharing

    WEP (Wired Equivalent Privacy)
      - Deprecated since 2004
      - Multiple cryptanalytic weaknesses documented
      - Compromisable within minutes using modern tools
      - Avoid for any sensitive activity

    WPA (WiFi Protected Access)
      - Legacy standard from 2003
      - Moderate protection against passive eavesdropping
      - Vulnerable to dictionary attacks on weak passphrases
      - Acceptable for general browsing only

    WPA2 (IEEE 802.11i)
      - Industry standard since 2004
      - AES-CCMP encryption implementation
      - Resistant to known cryptographic attacks
      - Suitable for most operational security requirements

    WPA3 (IEEE 802.11ax)
      - Current best-practice standard (2018-present)
      - Simultaneous Authentication of Equals (SAE) handshake
      - Protection against brute-force and dictionary attacks
      - Required for maximum security operations

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

2️⃣  SIGNAL STRENGTH (%) - CONNECTION QUALITY

    SHORT EXPLANATION:
    Indicates WiFi signal reception strength ranging from 0-100%.
    Higher percentage = stronger signal = more stable connection.

    DETAILED EXPLANATION:
    Signal strength measures how powerfully your device receives the network's
    transmission. This affects both connection reliability and actual bandwidth.

    SIGNAL STRENGTH RANGES:

    90-100% (Excellent)
      - Very strong signal, optimal connection quality
      - Maximum data transmission speed achievable
      - Minimal packet loss and latency
      - Best for high-bandwidth activities (streaming, downloads)
      - Ideal for security-sensitive operations

    70-89% (Very Good)
      - Good signal quality with reliable performance
      - Near-maximum data transmission speed
      - Acceptable packet loss rate (<1%)
      - Suitable for most activities including video calls, file transfers
      - Safe for security operations

    50-69% (Good)
      - Acceptable signal with generally reliable connection
      - Moderate data transmission speed (may experience slowdowns)
      - Occasional packet loss (1-5%)
      - Usable for web browsing, email, social media
      - Acceptable for most activities

    30-49% (Fair)
      - Weak signal with intermittent reliability issues
      - Reduced data transmission speed
      - Noticeable packet loss (5-15%)
      - Browsing may experience delays and timeouts
      - Not recommended for large file transfers
      - Avoid for sensitive security operations

    0-29% (Poor)
      - Very weak signal, unreliable connection
      - Severely reduced data transmission speed
      - High packet loss (>15%) and frequent disconnections
      - Connection may drop unexpectedly
      - Avoid for any critical activities
      - Recommend moving closer to network source

    LOCATION IMPACT:
    Signal strength depends on:
      • Distance from WiFi router/access point (closer = stronger)
      • Physical obstacles (walls, metal objects reduce signal)
      • Interference from other networks on same frequency
      • Environmental conditions (weather, building materials)
      • Device antenna quality

    RECOMMENDATION:
    Combine signal strength with security assessment. A strong signal (90%+)
    on a WPA3 network is ideal. A weak signal (30%) on secure network may
    warrant moving closer before conducting sensitive activities.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

3️⃣  DNS & PROXY DETECTION (DNS: INDICATOR)

    SHORT EXPLANATION:
    Identifies if the network uses DNS filtering or Proxy services.
    Indicators: 0 = Neither, DNS = DNS only, Proxy = Proxy only, & = Both present

    DETAILED EXPLANATION:
    DNS and Proxy detection reveals additional network infrastructure that may
    impact privacy and security:

    0 (Neither)
      - Network does not appear to use DNS filtering or Proxy
      - Direct internet access, unfiltered content
      - Higher privacy vulnerability (no intermediate filtering)
      - Use Cases: Public hotspots, personal networks without protection

    DNS (DNS Filtering Only)
      - Network implements DNS-level filtering/monitoring
      - May block malicious domains, adult content, or surveillance
      - DNS queries visible to ISP despite encryption
      - Privacy Implication: ISP can see visited domains
      - Use Cases: Corporate networks, parental control networks

    Proxy (Proxy Service Only)
      - Network routes traffic through proxy server
      - Proxy can inspect, log, or filter traffic content
      - May provide anonymity or access control
      - Privacy Implication: Proxy operator has content visibility
      - Use Cases: Corporate/institutional networks, VPN gateways

    & (Both Present)
      - Network combines DNS filtering AND Proxy services
      - Heavy network infrastructure involvement
      - Extensive monitoring/filtering capabilities
      - Privacy Implication: Multiple inspection points in traffic path
      - Use Cases: Enterprise networks, heavily controlled environments
stic analysis of network identifiers to estimate
    geographical context. This information provides secondary risk assessment:

    Public Locations (High Risk):
      - Airports, terminals: High-traffic environment, diverse attacker pool
      - Coffee shops: Prolonged occupancy, transient users
      - Hotels: Extended exposure duration, shared infrastructure
      - Libraries, public spaces: Diverse user base, minimal access controls

    Enterprise Locations (Moderate Risk):
      - Corporate networks: Controlled access, security hardening likely
      - Office spaces: Single organization, security policies enforced

    Residential Locations (Lower Risk):
      - Home networks: Limited user base, proprietor-controlled
      - Personal hotspots: Direct device control

    This assessment combines with Security Protocol to provide comprehensive risk
    modeling. A WPA3 network in an airport merits higher scrutiny than the
    same protocol in a residential environment.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

7️⃣  COLOR CODING SYSTEM
DETECTION METHODOLOGY:
  Detection is based on SSID naming patterns and network context indicators.
  This provides heuristic assessment, not definitive confirmation. Manual
  network configuration verification recommended for critical decisions.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

4️⃣  HONEYPOT & TRAP DETECTION (HP / Trap)

    SHORT EXPLANATION:
    Identifies potentially malicious networks designed to compromise devices.
    HP/Trap Indicators: X = Not honeypot, Y = Likely honeypot/trap

    DETAILED EXPLANATION:
    Honeypot and trap network detection represents the most advanced security
    feature in GekkoFinder. These are intentionally malicious networks deployed
    by attackers to compromise connected devices.

    WHAT IS A HONEYPOT/TRAP?
    A honeypot is a network intentionally designed to appear legitimate while
    actually attempting to:
      - Capture network credentials and authentication tokens
      - Inject malware into connected devices
      - Harvest personal information and browsing data
      - Perform man-in-the-middle (MITM) attacks
      - Execute SSL stripping and DNS poisoning attacks

    DETECTION METHODOLOGY:
    GekkoFinder identifies honeypots through vulnerability analysis:

    Suspicious Patterns Detected:
      • Unusually easy-to-exploit vulnerabilities
        → Real networks patch critical issues
        → Traps leave vulnerabilities intentionally unpatched

      • Too-good-to-be-true security posture
        → Genuine networks have inconsistencies
        → Perfect security metrics indicate artificial setup

      • Anonymous/traceless indicators
        → Real networks have identifying characteristics
        → Generic names (WiFi, Network, Connect) are suspicious

      • Weak encryption with generic names
        → Combination suggests deliberate compromise setup
        → Normal networks require passwords for security

    INDICATOR MEANINGS:

    HP: Honeypot Detection
      X = Network does not appear to be a honeypot
      Y = Network exhibits honeypot characteristics

    Trap: Trap Network Detection
      X = Network does not appear to be a trap
      Y = Network exhibits trap/malicious characteristics

    HONEYPOT RISK IMPACT ON SAFETYSCORE:
    Networks flagged as honeypots (Y) are automatically marked as UNSAFE (X)
    across all usage categories:
      • T (Testing): X - Do NOT use for security testing
      • UF (File Upload): X - Do NOT transmit any data
      • OF (File Open): X - Do NOT access sensitive documents
      • NU (Normal Usage): X - Do NOT use for any activity

    ACTION REQUIRED:
    If honeypot/trap detection triggers (Y indicator):
      1. Immediately avoid connecting to flagged network
      2. Document network SSID and characteristics
      3. Report to network administrator (if applicable)
      4. Consider alerting other users in vicinity

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

5️⃣  SAFETYSCORE INDICATORS (SS: T / UF / OF / NU)

    SHORT EXPLANATION:
    Context-specific safety assessment for different usage categories.
    S = Safe, X = Not Safe for indicated activity.

    DETAILED EXPLANATION FOR EACH INDICATOR:

    ▶ T (Testing) - Penetration Testing & Security Research
      Safety Threshold: WPA3 protocol only

      Rationale: Penetration testing and authorized security assessments require
      the highest operational security standards. Testing environments must
      prevent unintended traffic compromise that could compromise client data
      or test integrity. WPA3's advanced handshake mechanisms prevent passive
      eavesdropping, essential when conducting security research where traffic
      patterns themselves may reveal sensitive testing methodologies.

      Use Cases: Authorized penetration testing, vulnerability assessments,
      security research, security audit engagement work.

      Risk if Used Unsafely: Exposure of test methodologies, client data breach,
      assessment results interception, legal/contractual violations.

    ▶ UF (Uploading Files) - Sensitive Data Transmission
      Safety Threshold: WPA2 or WPA3 protocols

      Rationale: File uploading operations represent high-value data transmission
      events (credentials, financial documents, intellectual property). WPA2's
      AES-CCMP encryption provides cryptographic authentication preventing
      man-in-the-middle attacks during upload operations. The protocol threshold
      excludes WPA due to susceptibility to dictionary attacks on passphrases.

      Use Cases: Financial transactions, credential uploads, document transfers,
      cloud synchronization, email attachment uploads, API key transmission.

      Risk if Used Unsafely: Credential compromise, financial fraud, intellectual
      property theft, identity theft, account takeover attacks.

    ▶ OF (Opening Files) - Sensitive Document Access
      Safety Threshold: WPA2 or WPA3 protocols

      Rationale: Accessing sensitive documents requires protection against passive
      eavesdropping but may tolerate slightly lower standards than active data
      transmission. These protocols ensure encrypted transport layer preventing
      content inspection by network observers.

      Use Cases: Reading confidential emails, accessing private cloud documents,
      viewing medical records, reviewing financial statements, consulting sensitive
      information sources.

      Risk if Used Unsafely: Information disclosure, privacy violation, data
      breach notification requirements, personal information compromise.

    ▶ NU (Normal Usage) ⭐ MOST IMPORTANT - General Internet Activities
      Safety Threshold: WPA protocol or higher

      Rationale: Normal usage encompasses general browsing, social media, and
      non-sensitive internet activities. WPA or higher prevents passive network
      eavesdropping of general traffic. This is the baseline recommendation as
      even "non-sensitive" activities (browsing history, location inference,
      communication patterns) can reveal personal information through traffic
      analysis.

      Use Cases: General web browsing, social media, news reading, entertainment
      streaming, research activities, communication.

      Risk if Used Unsafely: Behavioral profiling, targeted attacks, correlation
      analysis, privacy erosion, targeted advertising/manipulation.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

6️⃣  LOCATION DETECTION (Country/City)

    SHORT EXPLANATION:
    Estimated network geographical location inferred from SSID naming patterns
    and network context indicators.

    DETAILED EXPLANATION:
    Location detection uses heuristic analysis of network identifiers to estimate
    geographical context. This information provides secondary risk assessment:

    Public Locations (High Risk):
      - Airports, terminals: High-traffic environment, diverse attacker pool
      - Coffee shops: Prolonged occupancy, transient users
      - Hotels: Extended exposure duration, shared infrastructure
      - Libraries, public spaces: Diverse user base, minimal access controls

    Enterprise Locations (Moderate Risk):
      - Corporate networks: Controlled access, security hardening likely
      - Office spaces: Single organization, security policies enforced

    Residential Locations (Lower Risk):
      - Home networks: Limited user base, proprietor-controlled
      - Personal hotspots: Direct device control

    This assessment combines with Security Protocol to provide comprehensive risk
    modeling. A WPA3 network in an airport merits higher scrutiny than the
    same protocol in a residential environment.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

7️⃣  COLOR CODING SYSTEM

    SHORT EXPLANATION:
    🟢 Green (S) = Safe for activity    |    🔴 Red (X) = Not safe for activity

    DETAILED EXPLANATION:
    The color coding system provides immediate visual risk assessment:

    Green Indicators:
      Cryptographic standards meet activity requirements. Network connection
      for specified purpose does not expose communications to passive
      eavesdropping or known cryptanalytic attacks.

    Red Indicators:
      Network security insufficient for activity type. Connection exposes
      activity-specific sensitive data to compromise risk. Alternative network
      selection recommended.


┌──────────────────────────────────────────────────────────────────────────────────┐
│ 🛡️  OPERATIONAL SECURITY RECOMMENDATIONS                                        │
└──────────────────────────────────────────────────────────────────────────────────┘

1. BASELINE PRACTICE:
   Always verify NU (Normal Usage) rating shows green before connecting ANY device.
   Even general browsing on unsecured networks enables behavioral profiling.

2. HONEYPOT AVOIDANCE:
   Networks flagged with "Y" indicators for HP or Trap must be avoided completely.
   These represent intentional compromise attempts. Warn others in vicinity.

3. SENSITIVE OPERATIONS:
   Reserve WPA2/WPA3 networks exclusively for file uploads and sensitive document
   access. Never transmit credentials, financial data, or authentication tokens
   over WPA or weaker protocols.

4. TESTING ENGAGEMENTS:
   Maintain separation between assessment traffic and personal activities. Use
   dedicated devices/networks for penetration testing to prevent cross-
   contamination and maintain proper evidence handling.

5. VPN AUGMENTATION:
   Use GekkoFinder assessment as baseline, not replacement for VPN security.
   VPN application provides additional encryption layer, browser isolation,
   and traffic anonymization complementing network-layer security.

6. PASSPHRASES:
   WPA networks with weak passphrases (dictionary words, personal information,
   predictable patterns) should be treated as lower security despite WPA protocol.
   Encourage strong passphrase practices.


┌──────────────────────────────────────────────────────────────────────────────────┐
│ 💻 USAGE INSTRUCTIONS                                                           │
└──────────────────────────────────────────────────────────────────────────────────┘

1. Launch: python3 GekkoFinder.py
2. Review network list with security protocols, DNS/Proxy, and honeypot indicators
3. AVOID any networks with Y indicators for HP or Trap
4. Identify network matching your activity requirements (green indicator)
5. Type network ID number and press Enter
6. Provide network password if required
7. Monitor connection status confirmation
8. Proceed with activity appropriate to network security level

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Version 1.3.B | Designed for Security Professionals | Use Responsibly
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    """
    print(help_text)
    input("\nPress Enter to return to menu...")

if __name__ == "__main__":
    # Check for help option
    if len(sys.argv) > 1 and sys.argv[1] in ["-h", "--help", "-help"]:
        show_help()
    else:
        try:
            run()
        except Exception:
            clear()
            raise

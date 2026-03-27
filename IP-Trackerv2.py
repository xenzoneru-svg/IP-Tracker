#!/usr/bin/env python3
"""
IP to Location Tracker v3.0 – Hacker Edition
Created by @xenzoneru | https://t.me/XenzoNeRu
"""

import os
import sys
import time
import random
import json
import requests
import socket
from datetime import datetime

# ========== HACKER COLORS ==========
G = "\033[92m"   # Matrix Green
R = "\033[91m"   # Red Alert
Y = "\033[93m"   # Warning
C = "\033[96m"   # Cyan
B = "\033[94m"   # Blue
M = "\033[95m"   # Magenta
W = "\033[97m"   # White
BOLD = "\033[1m"
BLINK = "\033[5m"
RESET = "\033[0m"

# ========== BRANDING ==========
CH = "https://t.me/XenzoNeRu"
CR = "@xenzoneru"
VER = "3.0 HACKER EDITION"

def clear():
    os.system('clear')

def hacker_typer(text, delay=0.03):
    """Type like a hacker"""
    for ch in text:
        print(ch, end='', flush=True)
        time.sleep(random.uniform(0.01, 0.05))
    print()

def matrix_rain(duration=1):
    """Matrix rain effect"""
    for _ in range(duration * 15):
        line = ''.join(random.choice('01') for _ in range(60))
        colors = [G, C, W]
        print(f"{random.choice(colors)}{line}{RESET}", end='\r')
        time.sleep(0.03)
    print()

def glitch_text(text):
    """Glitch effect text"""
    glitch_chars = "!@#$%^&*"
    result = ""
    for ch in text:
        if random.random() < 0.2:
            result += random.choice(glitch_chars)
        else:
            result += ch
    return result

def loading_hacker(text, sec=1):
    """Hacker-style loading with progress bar"""
    print(f"{Y}[{BOLD}*{RESET}{Y}] {text}{RESET}")
    for i in range(11):
        bar = f"{G}█{RESET}" * i + f"{R}░{RESET}" * (10 - i)
        print(f"\r{Y}  [{bar}] {i*10}%{RESET}", end='')
        time.sleep(sec/10)
    print()

def banner():
    clear()
    matrix_rain(0.5)
    
    print(f"""{G}
╔══════════════════════════════════════════════════════════════════╗
║  {W}██╗{G}  ██╗{W}███████╗{G}███╗{W}   ██╗{G}███████╗{W} ██████╗{G}                ║
║  {W}╚██╗{G}██╔╝{W}██╔════╝{G}████╗{W}  ██║{G}╚══███╔╝{W}██╔═══██╗{G}               ║
║   {W}╚███╔╝{G} █████╗ {W}██╔██╗{G} ██║{W}  ███╔╝{G} ██║{W}   ██║{G}               ║
║   {W}██╔██╗{G} ██╔══╝ {W}██║╚██╗{G}██║{W} ███╔╝{G}  ██║{W}   ██║{G}               ║
║  {W}██╔╝{G} ██╗{W}███████╗{G}██║{W} ╚████║{G}███████╗{W}╚██████╔╝{G}               ║
║  {W}╚═╝{G}  ╚═╝{W}╚══════╝{G}╚═╝{W}  ╚═══╝{G}╚══════╝{W} ╚═════╝{G}                ║
║                                                                  ║
║       {W}IP TRACKER {BLINK}{R}{VER}{RESET}{W}                             ║
║       {Y}>> HACKER EDITION <<{W}                                      ║
║       {C}{CR} | {CH[:30]}{W}            ║
╚══════════════════════════════════════════════════════════════════╝{RESET}""")
    
    print(f"\n{Y}{BOLD}[!] SYSTEM READY{RESET} {G}>> TRACK ANY IP <<{RESET}")
    print(f"{R}{BOLD}[!] FOR EDUCATIONAL USE ONLY{RESET}\n")

def enter():
    input(f"\n{Y}[{BOLD}*{RESET}{Y}] Press Enter to continue...{RESET}")

def hacker_animation():
    """Hacker-style animation before tracking"""
    print(f"{G}{BOLD}╔══════════════════════════════════════════════════════════╗")
    print(f"║  {W}INITIALIZING TRACKING SEQUENCE...{G}                        ║")
    print(f"║  {W}[{G}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓{W}] 100%{G}               ║")
    print(f"║  {W}>> ESTABLISHING SECURE CONNECTION...{G}                      ║")
    print(f"║  {W}>> DECODING GEOLOCATION DATA...{G}                           ║")
    print(f"║  {W}>> CALCULATING COORDINATES...{G}                             ║")
    print(f"╚══════════════════════════════════════════════════════════╝{RESET}")
    time.sleep(1.5)

def get_ip_info(ip):
    try:
        r = requests.get(f'http://ip-api.com/json/{ip}?fields=status,country,city,lat,lon,isp,org,as,query,proxy,mobile,hosting', timeout=8)
        return r.json()
    except:
        return {'status': 'fail', 'message': 'CONNECTION FAILED'}

def show_result(data, ip):
    if data.get('status') != 'success':
        print(f"\n{R}{BOLD}[!] ERROR: {data.get('message', 'Unknown')}{RESET}")
        return
    
    lat, lon = data.get('lat'), data.get('lon')
    maps = f"https://www.google.com/maps?q={lat},{lon}" if lat and lon else None
    
    print(f"\n{G}{BOLD}╔══════════════════════════════════════════════════════════╗")
    print(f"║  {W}📍 TARGET LOCATION ACQUIRED{RESET}{G}                             ║")
    print(f"╠══════════════════════════════════════════════════════════╣")
    print(f"║  {W}IP ADDRESS:{RESET} {C}{data.get('query', ip):<45}{RESET}{G}║")
    print(f"║  {W}COUNTRY:{RESET} {Y}{data.get('country', '?'):<49}{RESET}{G}║")
    print(f"║  {W}CITY:{RESET} {Y}{data.get('city', '?'):<51}{RESET}{G}║")
    print(f"║  {W}ISP:{RESET} {Y}{data.get('isp', '?')[:45]:<48}{RESET}{G}║")
    if lat and lon:
        print(f"║  {W}COORDINATES:{RESET} {M}{lat}, {lon:<41}{RESET}{G}║")
        print(f"║  {W}MAP LINK:{RESET} {C}{maps[:45]:<45}{RESET}{G}║")
    print(f"╚══════════════════════════════════════════════════════════╝{RESET}")
    
    if maps:
        print(f"\n{M}{BOLD}[+] GOOGLE MAPS LOCATION:{RESET}")
        print(f"{C}{maps}{RESET}")
    
    # Hacker-style flags
    print(f"\n{Y}{BOLD}[+] TARGET ANALYSIS:{RESET}")
    if data.get('mobile'):
        print(f"  {G}[✓]{RESET} Mobile Device Detected {W}[HIGH RISK]{RESET}")
    if data.get('proxy'):
        print(f"  {R}[!]{RESET} Proxy/VPN Active {W}[ANONYMIZED]{RESET}")
    if data.get('hosting'):
        print(f"  {C}[~]{RESET} Hosting Server {W}[DATA CENTER]{RESET}")
    if not data.get('mobile') and not data.get('proxy') and not data.get('hosting'):
        print(f"  {G}[✓]{RESET} Residential Connection {W}[DIRECT TARGET]{RESET}")

def main():
    # Hacker intro
    clear()
    hacker_typer(f"\n{G}[SYSTEM] Xenzo IP Tracker v{VER} Loading...{RESET}", 0.03)
    time.sleep(0.5)
    hacker_typer(f"{Y}[WARNING] This tool is for educational purposes only{RESET}", 0.03)
    time.sleep(1)
    
    banner()
    
    while True:
        print(f"\n{Y}{BOLD}┌────────────────────────────────────────────────────────────┐")
        print(f"│  {W}[1]{RESET} {G}TRACK MY IP{RESET}          {W}[2]{RESET} {G}TRACK CUSTOM IP{RESET}          │")
        print(f"│  {W}[3]{RESET} {G}RESOLVE DOMAIN{RESET}        {W}[0]{RESET} {R}ABORT MISSION{RESET}              │")
        print(f"└────────────────────────────────────────────────────────────┘{RESET}")
        
        ch = input(f"\n{C}{BOLD}>> SELECT TARGET: {RESET}").strip()
        
        if ch == '0':
            print(f"\n{R}{BOLD}[!] ABORTING MISSION...{RESET}")
            hacker_typer(f"{G}Connection terminated. Stay secure!{RESET}", 0.02)
            time.sleep(1)
            break
        
        elif ch == '1':
            loading_hacker("Locating your position", 0.6)
            try:
                ip = requests.get('https://api.ipify.org', timeout=5).text
                print(f"{G}{BOLD}[✓] TARGET IDENTIFIED: {ip}{RESET}")
            except:
                print(f"{R}{BOLD}[!] ERROR: Network connection failed{RESET}")
                enter()
                continue
        
        elif ch == '2':
            ip = input(f"{Y}{BOLD}>> ENTER IP ADDRESS: {RESET}").strip()
            if not ip.replace('.','').isdigit() or len(ip.split('.')) != 4:
                print(f"{R}{BOLD}[!] INVALID IP FORMAT{RESET}")
                enter()
                continue
            loading_hacker(f"Tracking {ip}", 0.5)
        
        elif ch == '3':
            dom = input(f"{Y}{BOLD}>> ENTER DOMAIN: {RESET}").strip()
            loading_hacker(f"Resolving {dom}", 0.5)
            try:
                ip = socket.gethostbyname(dom)
                print(f"{G}{BOLD}[✓] RESOLVED: {dom} → {ip}{RESET}")
            except:
                print(f"{R}{BOLD}[!] DOMAIN NOT FOUND{RESET}")
                enter()
                continue
        
        else:
            print(f"{R}{BOLD}[!] INVALID COMMAND{RESET}")
            time.sleep(1)
            continue
        
        # Hacker animation
        print()
        hacker_animation()
        matrix_rain(0.3)
        
        # Fetch data
        loading_hacker("Decrypting geolocation data", 0.5)
        data = get_ip_info(ip)
        
        # Show result
        show_result(data, ip)
        
        # Final hacker touch
        print(f"\n{Y}{BOLD}[+] TRACKING COMPLETE | {datetime.now().strftime('%H:%M:%S')}{RESET}")
        print(f"{R}{BOLD}[!] EDUCATIONAL PURPOSE ONLY - USE RESPONSIBLY{RESET}")
        enter()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{R}{BOLD}[!] MISSION ABORTED BY USER{RESET}")
        print(f"{G}Stay secure! Join {CH}{RESET}")
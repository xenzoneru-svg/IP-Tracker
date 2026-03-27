#!/usr/bin/env python3
"""
IP to Location Tracker v2.0 – Lightweight Edition
Created by @xenzoneru | https://t.me/XenzoNeRu
"""

import os
import sys
import time
import json
import requests
import socket
from datetime import datetime

# ========== LIGHTWEIGHT COLORS ==========
G = "\033[92m"   # Green
R = "\033[91m"   # Red
Y = "\033[93m"   # Yellow
C = "\033[96m"   # Cyan
B = "\033[94m"   # Blue
M = "\033[95m"   # Magenta
BOLD = "\033[1m"
RESET = "\033[0m"

# ========== BRANDING ==========
CH = "https://t.me/XenzoNeRu"
CR = "@xenzoneru"
VER = "2.0"

def clear():
    os.system('clear')

def type_effect(text, delay=0.02):
    for ch in text:
        print(ch, end='', flush=True)
        time.sleep(delay)
    print()

def matrix_load(sec=0.5):
    chars = "01"
    for _ in range(int(sec * 10)):
        line = ''.join(chars[random.randint(0,1)] for _ in range(40))
        print(f"\033[32m{line}\033[0m", end='\r')
        time.sleep(0.05)
    print()

def spinner(text, sec=0.8):
    spin = ['⣾', '⣽', '⣻', '⢿', '⡿', '⣟', '⣯', '⣷']
    for i in range(int(sec * 10)):
        print(f"\r{Y}{text} {spin[i % 8]}{RESET}", end='')
        time.sleep(0.1)
    print("\r" + " " * (len(text)+5), end='\r')

def banner():
    clear()
    print(f"""{C}
╔══════════════════════════════════════════════════════════╗
║  ██╗  ██╗███████╗███╗   ██╗███████╗ ██████╗             ║
║  ╚██╗██╔╝██╔════╝████╗  ██║╚══███╔╝██╔═══██╗            ║
║   ╚███╔╝ █████╗  ██╔██╗ ██║  ███╔╝ ██║   ██║            ║
║   ██╔██╗ ██╔══╝  ██║╚██╗██║ ███╔╝  ██║   ██║            ║
║  ██╔╝ ██╗███████╗██║ ╚████║███████╗╚██████╔╝            ║
║  ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝╚══════╝ ╚═════╝             ║
║                                                          ║
║       IP TRACKER {VER} – LIGHTWEIGHT EDITION             ║
║       {CR} | {CH[:30]}            ║
╚══════════════════════════════════════════════════════════╝{RESET}""")
    print(f"{Y}[!] Track any IP with live location & Google Maps{RESET}\n")

def enter():
    input(f"\n{Y}[Press Enter]{RESET}")

def get_ip_info(ip):
    try:
        r = requests.get(f'http://ip-api.com/json/{ip}?fields=status,country,city,lat,lon,isp,org,as,query,proxy,mobile,hosting', timeout=6)
        return r.json()
    except:
        return {'status': 'fail', 'message': 'No internet'}

def show_result(data, ip):
    if data.get('status') != 'success':
        print(f"\n{R}❌ {data.get('message', 'Failed')}{RESET}")
        return
    
    lat, lon = data.get('lat'), data.get('lon')
    maps = f"https://www.google.com/maps?q={lat},{lon}" if lat and lon else None
    
    print(f"\n{G}📍 LOCATION REPORT{RESET}")
    print(f"{C}┌{'─'*52}┐")
    print(f"│  IP: {data.get('query', ip):<47}│")
    print(f"│  {BOLD}Country:{RESET} {data.get('country', '?'):<46}│")
    print(f"│  {BOLD}City:{RESET} {data.get('city', '?'):<50}│")
    print(f"│  {BOLD}ISP:{RESET} {data.get('isp', '?')[:45]:<45}│")
    if lat and lon:
        print(f"│  {BOLD}📍 Coordinates:{RESET} {lat}, {lon:<39}│")
    print(f"└{'─'*52}┘{RESET}")
    
    if maps:
        print(f"\n{M}🗺️  MAP LINK:{RESET}")
        print(f"{C}{maps}{RESET}")
        print(f"{Y}💡 Open in browser to see exact location{RESET}")
    
    # Flags
    flags = []
    if data.get('mobile'): flags.append(f"{G}📱 Mobile{RESET}")
    if data.get('proxy'): flags.append(f"{R}⚠️ Proxy/VPN{RESET}")
    if data.get('hosting'): flags.append(f"{C}☁️ Hosting{RESET}")
    if flags:
        print(f"\n{B}⚡ FLAGS:{RESET} {' | '.join(flags)}")

def main():
    import random
    banner()
    
    while True:
        print(f"{Y}┌──────────────────────────────────────────────────────┐")
        print(f"│  [1] My IP     [2] Custom IP     [3] Domain     [0] Exit │")
        print(f"└──────────────────────────────────────────────────────┘{RESET}")
        
        ch = input(f"\n{C}Select: {RESET}").strip()
        
        if ch == '0':
            type_effect(f"\n✨ Thanks for using IP Tracker! Join {CH}", 0.03)
            time.sleep(1)
            break
        
        elif ch == '1':
            spinner("Getting your IP", 0.6)
            try:
                ip = requests.get('https://api.ipify.org', timeout=4).text
                print(f"{G}✅ Your IP: {ip}{RESET}")
            except:
                print(f"{R}❌ Check internet{RESET}")
                enter()
                continue
        
        elif ch == '2':
            ip = input(f"{Y}Enter IP: {RESET}").strip()
            if not ip.replace('.','').isdigit() or len(ip.split('.')) != 4:
                print(f"{R}❌ Invalid IP{RESET}")
                enter()
                continue
        
        elif ch == '3':
            dom = input(f"{Y}Enter domain: {RESET}").strip()
            spinner(f"Resolving {dom}", 0.5)
            try:
                ip = socket.gethostbyname(dom)
                print(f"{G}✅ {dom} → {ip}{RESET}")
            except:
                print(f"{R}❌ Domain not found{RESET}")
                enter()
                continue
        
        else:
            print(f"{R}❌ Invalid{RESET}")
            time.sleep(1)
            continue
        
        print()
        matrix_load(0.4)
        spinner("Fetching location", 0.6)
        data = get_ip_info(ip)
        show_result(data, ip)
        enter()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Y}Goodbye!{RESET}")
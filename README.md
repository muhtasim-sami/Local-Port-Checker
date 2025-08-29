# Local-Port-Checker
A Python utility to check the status (open/closed) of local ports on your machine.
This tool helps in troubleshooting network connectivity and verifying which ports are currently available or in use.

## Features
- Check if a specific port is open or closed
- Simple usage and output
- Written entirely in Python

## Usage
1. Clone the repository:
  ```
  git clone https://github.com/muhtasim-sami/Local-Port-Checker.git
  ```
2. Library
   - **requests** is an external library and must be installed via pip:
     ```
     pip install requests
     ```
   - **subprocess** is part of Python’s standard library and does not require installation. You can import it directly in your code:
     ```
     import subprocess
     ```
4. Run the script:
   ```
   python portChecker.py
   ```

## Requirements
- Python 3.x

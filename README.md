# Web Application Firewall Bypass

This project features a Python script designed to bypass web application firewall (WAF) and is specifically used for force browsing in penetration testing. The script performs automated requests with various payloads to test the firewall's handling of different inputs and to extract cookies if the firewall indicates a need for them.

## Features

- **Fuzzing Payloads**: Loads a list of fuzzing payloads from a file and sends them as part of the URL.
- **Cookie Handling**: Detects and extracts cookies if the firewall's response indicates a new cookie is required.

## Requirements

- Python 3.x
- `requests` library
- `pythonmonkey` library

Install the required libraries using pip:

```bash
pip install requests pythonmonkey
```

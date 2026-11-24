# CloudIAM Guard 🛡️

### Cloud IAM Security Policy Scanner

CloudIAM Guard is a Python-based security tool designed to identify potentially dangerous permissions in cloud IAM policies.

## Project Overview

CloudIAM Guard analyzes JSON policy files and detects risky permission configurations that could expose cloud resources to security threats.

## Key Features

- Detects Wildcard Actions.
- Detects Wildcard Resources.
- Scans JSON policy files.
- Generates security warnings.
- Helps identify potentially excessive permissions.

## Technologies Used

- Python
- JSON
- Visual Studio Code
- Git & GitHub

## Security Risks Detected

The current test identifies:

1. **Wildcard Action:** Allows overly broad actions.
2. **Wildcard Resource:** Applies permissions across overly broad resources.

## Project Structure

```text
CloudIAM-Guard/
├── main.py
├── policy.json
├── README.md
└── screenshots/
    └── cloudiam-report.png
```

## How to Run

1. Clone this repository.
2. Open the project folder.
3. Run:

```bash
python main.py policy.json
```

## Example Output

```text
=== CloudIAM Guard Report ===
WARNING: Security risks found!

[!] Statement 1: Wildcard Action
[!] Statement 1: Wildcard Resource
```

## Screenshot

![CloudIAM Guard Report](screenshots/cloudiam-report.png)

## Project Purpose

This project demonstrates practical cloud security concepts, particularly IAM permission analysis and the identification of potentially risky access configurations.

## Author

Najma Abdullahi

Cybersecurity | Cloud Security | Python
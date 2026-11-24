
import json
import sys

def scan_policy(filename):
    with open(filename, "r") as file:
        policy = json.load(file)

    statements = policy.get("Statement", [])

    if isinstance(statements, dict):
        statements = [statements]

    findings = []

    for number, statement in enumerate(statements, 1):

        if statement.get("Effect") != "Allow":
            continue

        actions = statement.get("Action", [])
        resources = statement.get("Resource", [])

        if isinstance(actions, str):
            actions = [actions]

        if isinstance(resources, str):
            resources = [resources]

        if "*" in actions:
            findings.append(
                f"Statement {number}: Wildcard Action"
            )

        if "*" in resources:
            findings.append(
                f"Statement {number}: Wildcard Resource"
            )

        principal = statement.get("Principal")

        if principal == "*":
            findings.append(
                f"Statement {number}: Public Principal"
            )

        elif isinstance(principal, dict):
            if any(
                value == "*"
                for value in principal.values()
            ):
                findings.append(
                    f"Statement {number}: "
                    "Wildcard Principal"
                )

    print("\n=== CloudIAM Guard Report ===")

    if findings:
        print("WARNING: Security risks found!\n")

        for finding in findings:
            print("[!] " + finding)
    else:
        print("No targeted wildcard risks detected.")

if __name__ == "__main__":
    filename = sys.argv[1] if len(sys.argv) > 1 else "policy.json"
    scan_policy(filename)

import os
import subprocess
from slither.slither import Slither

# Specify the directory path
DIRECTORY_PATH = "../Contracts"

def get_installed_versions():
    result = subprocess.run(["solc-select", "versions"], capture_output=True, text=True)
    lines = result.stdout.splitlines()
    versions = [line.split()[0] for line in lines]
    return versions

def get_used_versions(directory_path):
    versions = set()

    # Loop over all files in the directory
    for file_name in os.listdir(directory_path):
        if file_name.endswith(".sol"):
            file_path = os.path.join(directory_path, file_name)
            with open(file_path, "r") as file:
                lines = file.readlines()
                for line in lines:
                    if line.startswith("pragma solidity"):
                        version = line.split("^")[1].strip().replace(";", "")
                        versions.add(version)
                        break

    return versions

def get_missing_versions(installed_versions, used_versions):
    return used_versions - set(installed_versions)

def install_versions(versions):
    for version in versions:
        print(f"Installing solc version {version}...")
        subprocess.run(["solc-select", "install", version])

# Test the get_installed_versions function
installed_versions = get_installed_versions()
print(f"Installed versions: {installed_versions}")

# Test the get_used_versions function
used_versions = get_used_versions(DIRECTORY_PATH)
print(f"Versions used in contracts: {used_versions}")

# Test the get_missing_versions function
missing_versions = get_missing_versions(installed_versions, used_versions)

if not missing_versions:
    print("You have all needed versions installed.")
    exit(0)
else:
    # Install the missing versions
    install_versions(missing_versions)

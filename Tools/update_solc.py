import os
import subprocess
from slither.slither import Slither
from benchmark import print_benchmark_results,function_benchmark
import re

# Specify the directory path
DIRECTORY_PATH = 'C:/Github/DAppSCAN/DAppSCAN-source/contracts/Ackee_Blockchain-GoodGhosting'
# DIRECTORY_PATH = "../Contracts"

def get_installed_versions():
    result = subprocess.run(["solc-select", "versions"], capture_output=True, text=True)
    lines = result.stdout.splitlines()
    versions = [line.split()[0] for line in lines]
    return versions

@function_benchmark
def get_used_versions(directory_path):
    versions = set()
    version_pattern = re.compile(r"\d+\.\d+\.\d+")

    # Use os.walk to go through all files in directory_path
    for root, _, files in os.walk(directory_path):
        # Loop through all files
        for file in files:
            # Check and open .sol files
            if file.endswith('.sol'):
                file_path = os.path.join(root, file)
                with open(file_path, "r",encoding='utf-8') as file:
                    lines = file.readlines()
                    for line in lines:
                        if line.startswith("pragma solidity"):
                            version_match = version_pattern.search(line)
                            if version_match:
                                # Add only the first (lowest) version in the list
                                versions.add(version_match.group())
                                # Break out of the inner loop as soon as a match is found
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
else:
    # Install the missing versions, Commented until local host shut down is fixed.
    # install_versions(missing_versions)
    print("Missing Versions ",missing_versions)

print_benchmark_results()
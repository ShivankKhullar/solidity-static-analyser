import subprocess
from slither.slither import Slither
import os

# Specify the directory path
directory_path = "../Contracts"

current_version = None

def process_directory(directory_path):
    results = []

    # Loop over all files in the directory
    for file_name in os.listdir(directory_path):
        if file_name.endswith(".sol"):
            file_path = os.path.join(directory_path, file_name)
            contract_count = count_contracts(file_path)
            results.append((file_name, contract_count))

    return results
    
def count_contracts(file_path):   
    with open(file_path, "r") as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith("pragma solidity"):
                # Use the solc version specified in the contract file
                version = line.split("^")[1].strip().replace(";", "")
                use_solc(version)
                break

    # Initialize Slither
    slither = Slither(file_path)

    # Get the list of contracts
    contracts = slither.contracts
    print(contracts)

    # Return the number of contracts
    return len(contracts)

# This Function is used to change the Soliditity compiler version to match the contract.
def use_solc(version):
    global current_version
    # Optamisation if version is same don't change.
    if current_version != version:
        subprocess.run(["solc-select", "use", version])
        current_version = version

 
results = process_directory(directory_path)

# Print the results
print("{:<20} | {}".format("File Name", "Number of Contracts"))
print("------------------------------------------------")
for file_name, contract_count in results:
    print("{:<20} | {}".format(file_name, contract_count))

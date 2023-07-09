import subprocess
from slither.slither import Slither
import os
from prettytable import PrettyTable

# Specify the directory path
directory_path = "../Contracts"

current_version = None

def process_directory(directory_path):
    results = {}

    # Loop over all files in the directory
    for file_name in os.listdir(directory_path):
        if file_name.endswith(".sol"):
            file_path = os.path.join(directory_path, file_name)
            contract_results = process_contracts(file_path)
            results[file_name] = contract_results

    return results

def process_contracts(file_path):
    contract_results = {}

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

    for contract in contracts:
        # Get the list of functions
        functions = contract.functions
        function_results = {}
        for function in functions:
            # Get the list of parameters
            parameters = function.parameters
            function_results[function.name] = len(parameters)
        contract_results[contract.name] = function_results

    return contract_results

def calculate_nesting_depth(function):
    # Get the control flow graph of the function
    cfg = function.cfg

    # Initialize the maximum depth to 0
    max_depth = 0

    # Define a recursive function to traverse the CFG
    def traverse(node, current_depth):
        nonlocal max_depth
        # Update the maximum depth
        max_depth = max(max_depth, current_depth)
        # Traverse all outgoing edges
        for outgoing_edge in node.outgoing_edges:
            # If the outgoing edge leads to a branching node, increase the current depth
            if len(outgoing_edge.node.outgoing_edges) > 1:
                traverse(outgoing_edge.node, current_depth + 1)
            else:
                traverse(outgoing_edge.node, current_depth)

    # Start the traversal from the entry node of the CFG
    traverse(cfg.entry_node, 0)

    return max_depth


# This Function is used to change the Soliditity compiler version to match the contract.
def use_solc(version):
    global current_version
    # Optamisation if version is same don't change.
    if current_version != version:
        subprocess.run(["solc-select", "use", version])
        current_version = version

results = process_directory(directory_path)

# Create the table
table = PrettyTable()
table.field_names = ["File Name", "Contract Name", "Function Name", "Number of Parameters"]

# Populate the table
for file_name, contract_results in results.items():
    for contract_name, function_results in contract_results.items():
        for function_name, parameter_count in function_results.items():
            table.add_row([file_name, contract_name, function_name, parameter_count])

# Print the table
print(table)
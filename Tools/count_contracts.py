import subprocess
from slither.slither import Slither
from slither.core.cfg.node import NodeType
from slither.core.expressions import CallExpression
from slither.slithir.operations.library_call import LibraryCall
import os
from prettytable import PrettyTable
import re
from benchmark import function_benchmark,print_benchmark_results
from termcolor import colored

# Specify the directory path
directory_path = "../Contracts"
# directory_path = 'C:/Github/DAppSCAN/DAppSCAN-source/contracts/Ackee_Blockchain-GoodGhosting'

# directory_path = "C:\\Users\\shiva\\Downloads\\_Code\\openzeppelin-contracts\\contracts-exposed\\access"

current_version = None
@function_benchmark
def calculate_inheritance_depth(contract):
    # Get the list of inherited contracts
    inherited_contracts = contract.inheritance

    # If the contract doesn't inherit from any other contracts, its depth of inheritance is 0
    if not inherited_contracts:
        return 0

    # If the contract does inherit from other contracts, its depth of inheritance is 1 plus the maximum depth of inheritance of the contracts it inherits from
    # And since multiple inhertance is allowed we'll looping through the list of contracts.
    return 1 + max(calculate_inheritance_depth(inherited_contract) for inherited_contract in inherited_contracts)

@function_benchmark
def process_directory(directory_path):
    results = {}

    # Loop over all directories, subdirectories, and files
    for root, dirs, filenames in os.walk(directory_path):
        for file_name in filenames:
            if file_name.endswith(".sol"):
                file_path = os.path.join(root, file_name)
                contract_results = process_contracts(file_path)
                results[file_name] = contract_results

    return results
@function_benchmark
def process_contracts(file_path):
    contract_results = {}

    # Define the regular expression pattern for the version
    version_pattern = re.compile(r"\d+\.\d+\.\d+")

    with open(file_path, "r") as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith("pragma solidity"):
                # Use the solc version specified in the contract file
                version_match = version_pattern.search(line)
                if version_match:
                    version = version_match.group()
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
            # Calculate the nesting depth
            nesting_depth = calculate_nesting_depth(function)
            # Calculate the number of function calls
            function_calls = calculate_function_call(function)
            function_results[function.name] = (len(parameters), nesting_depth, function_calls)
        # Calculate the inheritance depth
        inheritance_depth = calculate_inheritance_depth(contract)
        contract_results[contract.name] = (function_results, inheritance_depth)

    return contract_results
@function_benchmark
def calculate_function_call(function):
    # Get the nodes of the function's CFG
    nodes = function.nodes

    # Initialize the number of function calls to 0
    function_calls = 0

    # Traverse the CFG
    for node in nodes:
        # If the node contains a function call, increment the number of function calls
        if isinstance(node.expression, (CallExpression, LibraryCall)):
            function_calls += 1

    return function_calls
@function_benchmark
def calculate_nesting_depth(function):
    # Get the nodes of the function's CFG
    nodes = function.nodes
    # print(function.name)

    max_depth = 0
    current_depth = 0

    # Create a set to keep track of visited nodes, had to because loops gave stack overflow
    visited_nodes = set()

    # Define a recursive function to traverse the CFG
    def traverse(node):
        nonlocal max_depth, current_depth

        # If the node has already been visited, return immediately
        if node in visited_nodes:
            return

        # Mark the node as visited
        visited_nodes.add(node)

        # Check the type of the node
        if node.type in {NodeType.IF, NodeType.STARTLOOP}:
            # If the node is a control structure that starts a new block, increment the current depth
            current_depth += 1
        elif node.type in {NodeType.ENDIF, NodeType.ENDLOOP}:
            # If the node is a control structure that ends a block, decrement the current depth
            current_depth -= 1

        # Update the maximum depth
        max_depth = max(max_depth, current_depth)

        # Traverse all outgoing edges
        if node is not None:
            # print(node.type)
            # print(node.expression)
            # print("New Depth",current_depth,"Max Depth",max_depth,"Current Depth",current_depth)
            # Check if the 'sons' attribute exists
            if hasattr(node, 'sons'):
                for son in node.sons:
                    traverse(son)

    # Start the traversal from the entry node of the CFG
    if function.entry_point is not None:
        traverse(function.entry_point)

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
table.field_names = ["File Name", "Number of Contracts", "Contract Name", "Inheritance Depth", "Number of Functions", "Function Name", "Number of Parameters", "Nesting Depth", "Function Calls"]

# Populate the table
for file_name, contract_results in results.items():
    for contract_name, data in contract_results.items():
        function_results, inheritance_depth = data
        for function_name, function_data in function_results.items():
            parameter_count, nesting_depth, function_calls = function_data
            table.add_row([file_name, len(contract_results), contract_name, inheritance_depth, len(function_results), function_name, parameter_count, nesting_depth, function_calls])

print(colored(table, 'light_cyan'))

print_benchmark_results()
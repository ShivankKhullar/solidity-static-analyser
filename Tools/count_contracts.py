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

directory_path = "../Contracts"
# directory_path = 'C:/Github/DAppSCAN/DAppSCAN-source/contracts/Ackee_Blockchain-GoodGhosting'

# directory_path = "C:\\Users\\shiva\\Downloads\\_Code\\openzeppelin-contracts\\contracts-exposed\\access"

class NodeProcessor:

    @staticmethod
    def process_for_nesting_depth(node):
        if node is None:
            return 0
        elif node.type in {NodeType.IF, NodeType.STARTLOOP}:
            return 1
        elif node.type in {NodeType.ENDIF, NodeType.ENDLOOP}:
            return -1
        else:
            return 0

    @staticmethod
    def process_for_function_call(node):
        if isinstance(node.expression, (CallExpression, LibraryCall)):
            return 1
        else:
            return 0


class CFGTraverser:

    def __init__(self, processor):
        self.processor = processor
        self.visited_nodes = set()

    def tree_traversal(self, node):
        if node in self.visited_nodes:
            return 0

        self.visited_nodes.add(node)

        count = self.processor(node)
        if node is not None and hasattr(node, 'sons'):
            for son in node.sons:
                count += self.tree_traversal(son)

        return count

    def node_list_traversal(self, nodes):
        count = 0
        for node in nodes:
            count += self.processor(node)
        return count


class ContractAnalyzer:
    def __init__(self):
        self.current_version = None
        self.max_depth = 0
        self.current_depth = 0
        self.function_calls = 0

    @function_benchmark
    def calculate_inheritance_depth(self, contract):
        inherited_contracts = contract.inheritance
        if not inherited_contracts:
            return 0
        return 1 + max(self.calculate_inheritance_depth(inherited_contract) for inherited_contract in inherited_contracts)

    @function_benchmark
    def calculate_function_call(self, function):
        traverser = CFGTraverser(NodeProcessor.process_for_function_call)
        self.function_calls = traverser.node_list_traversal(function.nodes)

    @function_benchmark
    def calculate_nesting_depth(self, function):
        traverser = CFGTraverser(NodeProcessor.process_for_nesting_depth)
        depth_changes = traverser.tree_traversal(function.entry_point)
        self.current_depth += depth_changes
        self.max_depth = max(self.max_depth, self.current_depth)

    def use_solc(self, version):
        if self.current_version != version:
            subprocess.run(["solc-select", "use", version])
            self.current_version = version

    @function_benchmark
    def process_contracts(self, file_path):
        contract_results = {}
        version_pattern = re.compile(r"\d+\.\d+\.\d+")
        with open(file_path, "r") as file:
            lines = file.readlines()
            for line in lines:
                if line.startswith("pragma solidity"):
                    version_match = version_pattern.search(line)
                    if version_match:
                        version = version_match.group()
                        self.use_solc(version)
                    break
        slither = Slither(file_path)
        contracts = slither.contracts
        for contract in contracts:
            functions = contract.functions
            function_results = {}
            for function in functions:
                parameters = function.parameters
                self.calculate_nesting_depth(function)
                self.calculate_function_call(function)
                function_results[function.name] = (len(parameters), self.max_depth, self.function_calls)
            inheritance_depth = self.calculate_inheritance_depth(contract)
            contract_results[contract.name] = (function_results, inheritance_depth)
        return contract_results


class DirectoryProcessor:

    @function_benchmark
    def process_directory(self, directory_path):
        results = {}
        analyzer = ContractAnalyzer()
        for root, dirs, filenames in os.walk(directory_path):
            for file_name in filenames:
                if file_name.endswith(".sol"):
                    file_path = os.path.join(root, file_name)
                    contract_results = analyzer.process_contracts(file_path)
                    results[file_name] = contract_results
        return results


class ResultPrinter:

    def print_results(self, results):
        table = PrettyTable()
        table.field_names = ["File Name", "Number of Contracts", "Contract Name", "Inheritance Depth", "Number of Functions", "Function Name", "Number of Parameters", "Nesting Depth", "Function Calls"]
        for file_name, contract_results in results.items():
            for contract_name, data in contract_results.items():
                function_results, inheritance_depth = data
                for function_name, function_data in function_results.items():
                    parameter_count, nesting_depth, function_calls = function_data
                    table.add_row([file_name, len(contract_results), contract_name, inheritance_depth, len(function_results), function_name, parameter_count, nesting_depth, function_calls])
        print(colored(table, 'light_cyan'))


directory_processor = DirectoryProcessor()
results = directory_processor.process_directory(directory_path)

result_printer = ResultPrinter()
result_printer.print_results(results)

print_benchmark_results()

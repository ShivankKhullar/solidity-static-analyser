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
import datetime
import csv

directory_path = "../Contracts"
# directory_path = 'C:/Github/DAppSCAN/DAppSCAN-source/contracts/Ackee_Blockchain-GoodGhosting'

# directory_path = "C:\\Users\\shiva\\Downloads\\_Code\\openzeppelin-contracts\\contracts-exposed\\access"

class NodeProcessor:

    @staticmethod
    def process_node_for_nesting_depth(node, state):
        if node is None:
            state['current_depth'] += 0
        elif node.type in {NodeType.IF, NodeType.STARTLOOP}:
            state['current_depth'] += 1
        elif node.type in {NodeType.ENDIF, NodeType.ENDLOOP}:
            state['current_depth'] -= 1

        state['max_depth'] = max(state['max_depth'], state['current_depth'])
        return state

    @staticmethod
    def process_node_for_function_calls(node, state):
        if isinstance(node.expression, (CallExpression, LibraryCall)):
            state['function_calls'] += 1
        return state

class CFGTraverser:

    def __init__(self, processor):
        self.processor = processor
        self.visited_nodes = set()

    def tree_traversal(self, node, state):
        if node in self.visited_nodes:
            return state

        self.visited_nodes.add(node)
        state = self.processor(node, state)

        if node is not None and hasattr(node, 'sons'):
            for son in node.sons:
                state = self.tree_traversal(son, state)

        return state

    def node_list_traversal(self, nodes, state):
        for node in nodes:
            state = self.processor(node, state)
        return state

class ContractAnalyzer:
    def __init__(self):
        self.current_version = None
        self.slither_object = None
        self.state = {
            'max_depth': 0,
            'current_depth': 0,
            'function_calls': 0
        }

        self.function_metrics = {
            "No. of Parameters": self.calculate_parameters_count,
            "Nesting Depth": self.calculate_nesting_depth,
            "Function Calls": self.calculate_function_call,
            "Cyclomatic Complexity": self.calculate_cyclomatic_complexity
            # ...add more function metrics here...
        }

        self.contract_metrics = {
            "Inheritance Depth": self.calculate_inheritance_depth,
            "CBO": self.calculate_cbo
            # ...add more contract metrics here...
        }

    @function_benchmark
    def calculate_cbo(self, contract):
        # Limitation of running the contracts by saving them in a dictonary is that they need to have the same parameters.
        # That is why I made the slither object acessible for the class.
        all_contracts = self.slither_object.contracts
        called_contracts = set()
        for function in contract.functions:
            for call in function.high_level_calls:
                called_contract = call[0]
                if called_contract != contract and called_contract in all_contracts:
                    called_contracts.add(called_contract)
        return len(called_contracts)

    @function_benchmark
    def calculate_parameters_count(self, function):
        return len(function.parameters)
    
    @function_benchmark
    def calculate_nesting_depth(self, function):
        self.state['current_depth'] = 0
        self.state['max_depth'] = 0
        traverser = CFGTraverser(NodeProcessor.process_node_for_nesting_depth)
        self.state = traverser.tree_traversal(function.entry_point, self.state)
        return self.state['max_depth']

    @function_benchmark
    def calculate_function_call(self, function):
        self.state['function_calls'] = 0
        traverser = CFGTraverser(NodeProcessor.process_node_for_function_calls)
        self.state = traverser.node_list_traversal(function.nodes, self.state)
        return self.state['function_calls']

    @function_benchmark
    def calculate_inheritance_depth(self, contract):
        inherited_contracts = contract.inheritance
        if not inherited_contracts:
            return 0
        return 1 + max(self.calculate_inheritance_depth(inherited_contract) for inherited_contract in inherited_contracts)

    @function_benchmark
    def calculate_cyclomatic_complexity(self, function):
        cfg = function.nodes
        E = sum(len(node.sons) for node in cfg) # No of Edges
        N = len(cfg) # No of Nodes
        return E - N + 2

    def use_solc(self, version):
        if self.current_version != version:
            subprocess.run(["solc-select", "use", version])
            self.current_version = version

    def extract_solidity_version(self, file_path):
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

    @function_benchmark
    def process_contracts(self, file_path):
        self.extract_solidity_version(file_path)
        slither = Slither(file_path)
        self.slither_object = slither
        contract_results = {}
        contracts = slither.contracts
        for contract in contracts:
            function_results = {}
            for function in contract.functions:
                function_results[function.name] = {metric_name: metric(function) for metric_name, metric in self.function_metrics.items()}
            contract_results[contract.name] = {**{metric_name: metric(contract) for metric_name, metric in self.contract_metrics.items()}, "Functions": function_results}
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
                    try:
                        contract_results = analyzer.process_contracts(file_path)
                        results[file_name] = contract_results
                    except Exception as e:
                        print(colored(f"Error while processing file {file_path}", "red"))  
        return results

class Results:

    def __init__(self, contract_metrics, function_metrics):
        self.contract_metrics = contract_metrics
        self.function_metrics = function_metrics

    def generate_table(self, results):
        table = PrettyTable()
        table.field_names = ["File Name", "No. of Contracts", "Contract Name"] + list(self.contract_metrics.keys()) + ["No. of Functions", "Function Name"] + list(self.function_metrics.keys())
        for file_name, contract_results in results.items():
            for contract_name, contract_data in contract_results.items():
                function_results = contract_data.pop("Functions")
                contract_metrics_data = contract_data
                for function_name, function_data in function_results.items():
                    table.add_row([file_name, len(contract_results), contract_name] + list(contract_metrics_data.values()) + [len(function_results), function_name] + list(function_data.values()))
        return table


    def print_table(self, table):
        print(colored(table, 'light_cyan'))

    def save_table_to_csv(self, table, directory_path):
        timestamp = datetime.datetime.now().strftime('%d-%m-%Y_%H-%M-%S')
        filename = f'../csv_results/results_{timestamp}.csv'
        header = f'These metrics have been extracted from all contracts with the parent directory as {directory_path} on {timestamp}\n'
        
        with open(filename, 'w', newline='') as f:  # add newline='' here
            f.write(header)
            writer = csv.writer(f)
            writer.writerow(table.field_names)  # write the header row
            for row in table._rows:  # iterate through the data rows
                writer.writerow(row)  # write each row    

analyzer = ContractAnalyzer()
results = Results(analyzer.contract_metrics, analyzer.function_metrics)

directory_processor = DirectoryProcessor()
results_dictionary = directory_processor.process_directory(directory_path)

table = results.generate_table(results_dictionary)

results.print_table(table)

# results.save_table_to_csv(table, directory_path)

print_benchmark_results()

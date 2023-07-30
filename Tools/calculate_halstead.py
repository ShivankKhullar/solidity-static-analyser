import math
from prettytable import PrettyTable
from halstead_extractor import HalsteadExtractor

class HalsteadMetrics:
    def __init__(self, file):
        self.file_path = file
        self.operator_metrics = HalsteadExtractor(file, "operators")
        self.operand_metrics = HalsteadExtractor(file, "operands")

    def calculate_metrics(self):
        contract_function_metrics = {}

        # Use zip to iterate through both operator_metrics and operand_metrics dicionaries together
        for (contract_operator, functions_operator), (contract_operand, functions_operand) in zip(self.operator_metrics.count().items(), self.operand_metrics.count().items()):
            for (function_operator, counts_operator), (function_operand, counts_operand) in zip(functions_operator.items(), functions_operand.items()):

                # Halstead's parameters -> n1, n2, N1, N2
                self.total_operator_count = counts_operator['total_count']
                self.unique_operator_count = counts_operator['unique_count']
                self.total_operand_count = counts_operand['total_count']
                self.unique_operand_count = counts_operand['unique_count']

                # Calculate metrics based on the counts for the current function
                self.calculate_program_length()
                self.calculate_volume()
                self.calculate_difficulty()
                self.calculate_effort()
                self.calculate_time()

                if contract_operator not in contract_function_metrics:
                    contract_function_metrics[contract_operator] = {}
                # Dictionary of the calculated Halstead Metrics per Contract    
                contract_function_metrics[contract_operator][function_operator] = {
                    'unique_operator_count': self.unique_operator_count,
                    'unique_operand_count': self.unique_operand_count,
                    'operator_count': self.total_operator_count,
                    'operand_count': self.total_operand_count,
                    'program_length': self.program_length,
                    'volume': self.volume,
                    'difficulty': self.difficulty,
                    'effort': self.effort,
                    'time': self.time
                }

        return contract_function_metrics

    def calculate_program_length(self):
        # N = N1 + N2
        self.program_length = self.total_operator_count + self.total_operand_count

    def calculate_volume(self):
        # V = N × log2(n1 + n2)
        self.volume = round((self.program_length * math.log2(self.unique_operator_count + self.unique_operand_count)),3)

    def calculate_difficulty(self):
        # D = (n1 * N2) / (n2 * 2)
        self.difficulty = round(((self.unique_operator_count * self.unique_operand_count) / (self.total_operand_count * 2)),3)

    def calculate_effort(self):
        # E = D × V
        self.effort = round((self.difficulty * self.volume),3)

    def calculate_time(self):
        # T = E ÷ 18
        self.time = round((self.effort / 18),3)


# File path to the Solidity contract
file = "../Contracts/racecondition.sol"

halstead = HalsteadMetrics(file)
contract_function_metrics = halstead.calculate_metrics()

# print(contract_function_metrics)

# Display on table -> more readible
table = PrettyTable()
table.field_names = ["Contract", "Function", "Unique Operator Count (n1)", "Unique Operand Count (n2)", "Total Operator Count (N1)", "Total Operand Count (N2)", "Program Length (N)", "Volume (V)", "Difficulty (D)", "Effort (E)", "Time (T)"]
for contract, functions in contract_function_metrics.items():
    for function, metrics in functions.items():
        table.add_row([contract, function, metrics['unique_operator_count'], metrics['unique_operand_count'], metrics['operator_count'], metrics['operand_count'], metrics['program_length'], metrics['volume'], metrics['difficulty'], metrics['effort'], metrics['time']])

print(table)

print('\n', contract_function_metrics, '\n')
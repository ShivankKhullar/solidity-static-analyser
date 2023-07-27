from antlr4 import FileStream, CommonTokenStream
from SolidityLexer import SolidityLexer
from collections import Counter
from token_types import operator_types, operand_types

class HalsteadExtractor:
    def __init__(self, file: str, what_to_calculate: str):
        """
        The contructor initializes all the things needed for antlr.
        Args:
            file: The file to extract metrics from.
            what_to_calculate: Either 'operators' or 'operands'.
        """
        self.file = file
        self.what_to_calculate = what_to_calculate
        self.input_stream = FileStream(file)
        self.lexer = SolidityLexer(self.input_stream)
        self.stream = CommonTokenStream(self.lexer)
        self.stream.fill()

        if self.what_to_calculate == "operators":
            self.types_to_count = operator_types
        elif self.what_to_calculate == "operands":
            self.types_to_count = operand_types
        else:
            raise ValueError("what_to_calculate must be either 'operators' or 'operands'")
        
        self.contract_counts = {}
        self.contract_name = None
        self.function_name = None

    def count(self) -> dict:
        """
        Count the total and unique operators/operands for each function in each contract.
        Returns:
            A dictionary where the keys are contract names, the values are dictionaries where the keys are function names
            and the values are dictionaries with keys 'total_count' and 'unique_count' representing the total number
            of operators/operands and the number of unique operators/operands, respectively.
            Eg - {'SampleContract': {'incrementCount': {'N1': 6, 'n1': 6}, 'decrementCount': {'N1': 52, 'n1': 12}, 'resetCount': {'N1': 6, 'n1': 6}, 'complexFunction': {'N1': 69, 'n1': 17}}}
        """
        for i, token in enumerate(self.stream.tokens):
            if token.type == SolidityLexer.Contract:
                self._start_new_contract(i)
            elif token.type == SolidityLexer.Function:
                self._start_new_function(i)
            elif token.type in self.types_to_count and self.function_name is not None:
                self.contract_counts[self.contract_name][self.function_name][token.type] += 1
        self._calculate_total_and_unique_counts()
        return self.contract_counts

    def _start_new_contract(self, i: int):
        """
        Args:
            i: The index of the 'contract' token.
        """
        contract_name_token = self.stream.tokens[i + 1]
        self.contract_name = contract_name_token.text
        self.contract_counts[self.contract_name] = {}

    def _start_new_function(self, i: int):
        """
        Args:
            i: The index of the 'function' token.
        """
        function_name_token = self.stream.tokens[i + 1]
        self.function_name = function_name_token.text
        self.contract_counts[self.contract_name][self.function_name] = Counter()

    def _calculate_total_and_unique_counts(self):
        for contract in self.contract_counts:
            for function in self.contract_counts[contract]:
                operator_counter = self.contract_counts[contract][function]
                total_count = sum(operator_counter.values())
                unique_count = len(operator_counter)
                self.contract_counts[contract][function] = {'total_count': total_count, 'unique_count': unique_count}

file = "..\Contracts\TestingContracts\Conditions.sol"
extractor = HalsteadExtractor(file, "operators")
results = extractor.count()
print(results)

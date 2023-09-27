"""
Developed By: Shivank Khullar
Description: Extracts Halstead metrics from Solidity contracts using ANTLR4. 
             Computes total and unique operators/operands for each function in a contract.
"""

from antlr4 import FileStream, CommonTokenStream
from antlr_generated_files.SolidityLexer import SolidityLexer
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
            # print(token, token.type,token.text)
            if token.type == SolidityLexer.Contract:
                self._start_new_contract(i)
            elif token.type == SolidityLexer.Function:
                self._start_new_function(i)
            elif token.type in self.types_to_count and self.function_name is not None:
                # print(self.contract_name,self.function_name)
                # Don't count the token if the previous token was a Function or Contract token
                # This is for skiping declarations when counting operands.
                if i > 0 and self.stream.tokens[i-1].type not in [SolidityLexer.Function, SolidityLexer.Contract]:
                    # print("Counted",token.type)
                    self.contract_counts[self.contract_name][self.function_name][token.text] += 1
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
        self.function_name = None # When we step into a new contract we erase the last function.

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

file = "..\Contracts\TestingContracts\Coupling.sol"
extractor_operators = HalsteadExtractor(file, "operators")
results_operators = extractor_operators.count()
print(results_operators)

extractor_operands = HalsteadExtractor(file, "operands")
results_operands = extractor_operands.count()
print(results_operands)

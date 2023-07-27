from antlr4 import FileStream, CommonTokenStream
from SolidityLexer import SolidityLexer
from collections import Counter

def count_operators(file):
    input_stream = FileStream(file)
    lexer = SolidityLexer(input_stream)
    stream = CommonTokenStream(lexer)
    stream.fill()

    operator_types = {
        SolidityLexer.While, SolidityLexer.LParen, SolidityLexer.RParen,
        SolidityLexer.LBrack, SolidityLexer.RBrack, SolidityLexer.LBrace,
        SolidityLexer.RBrace, SolidityLexer.Colon, SolidityLexer.Semicolon,
        SolidityLexer.Period, SolidityLexer.Conditional, SolidityLexer.DoubleArrow,
        SolidityLexer.RightArrow, SolidityLexer.Assign, SolidityLexer.AssignBitOr,
        SolidityLexer.AssignBitXor, SolidityLexer.AssignBitAnd, SolidityLexer.AssignShl,
        SolidityLexer.AssignSar, SolidityLexer.AssignShr, SolidityLexer.AssignAdd,
        SolidityLexer.AssignSub, SolidityLexer.AssignMul, SolidityLexer.AssignDiv,
        SolidityLexer.AssignMod, SolidityLexer.Comma, SolidityLexer.Or,
        SolidityLexer.And, SolidityLexer.BitOr, SolidityLexer.BitXor,
        SolidityLexer.BitAnd, SolidityLexer.Shl, SolidityLexer.Sar,
        SolidityLexer.Shr, SolidityLexer.Add, SolidityLexer.Sub,
        SolidityLexer.Mul, SolidityLexer.Div, SolidityLexer.Mod,
        SolidityLexer.Exp, SolidityLexer.Equal, SolidityLexer.NotEqual,
        SolidityLexer.LessThan, SolidityLexer.GreaterThan, SolidityLexer.LessThanOrEqual,
        SolidityLexer.GreaterThanOrEqual, SolidityLexer.Not, SolidityLexer.BitNot,
        SolidityLexer.Inc, SolidityLexer.Dec,
        SolidityLexer.Bytes, SolidityLexer.Else, SolidityLexer.FixedBytes,
        SolidityLexer.For, SolidityLexer.UnsignedIntegerType, SolidityLexer.Return,
        SolidityLexer.If
    }

    # print("Stream.tokens length", len(stream.tokens))
    
    contract_counts = {}  # Dictionary to store counts for each contract
    contract_name = None  # The name of the current contract
    function_name = None  # The name of the current function
    for i, token in enumerate(stream.tokens):
        if token.type == SolidityLexer.Contract:  # Replace with the token type for the start of a contract
            contract_name_token = stream.tokens[i + 1]  # The next token should be the contract name
            contract_name = contract_name_token.text
            contract_counts[contract_name] = {}  # Start a new dictionary for this contract
        elif token.type == SolidityLexer.Function:  # Replace with the token type for the start of a function
            function_name_token = stream.tokens[i + 1]  # The next token should be the function name
            function_name = function_name_token.text
            contract_counts[contract_name][function_name] = Counter()  # Start a new Counter for this function
        elif token.type in operator_types and function_name is not None:  # Only count operators if we're inside a function
            contract_counts[contract_name][function_name][token.type] += 1

    # Now, for each function, calculate N1 and n1
    for contract in contract_counts:
        for function in contract_counts[contract]:
            operator_counter = contract_counts[contract][function]
            N1 = sum(operator_counter.values())
            n1 = len(operator_counter)
            contract_counts[contract][function] = {'N1': N1, 'n1': n1}

    return contract_counts

file = "..\Contracts\TestingContracts\Conditions.sol"
# file = "..\Contracts\MyContract.sol"
results = count_operators(file)
print(results)

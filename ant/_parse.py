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
    
    operator_counts = Counter()  # Initialize a Counter object
    for token in stream.tokens:
        # print(token)
        if token.type in operator_types:
            # print("Match", token)
            # print("Type",token.type)
            operator_counts[token.type] += 1  # Increment the count for this token type

    print("operator_counts.values() ",operator_counts.values())
    print("operator_counts.values() ",operator_counts.keys())
    N1 = sum(operator_counts.values())  # Total number of operator occurrences
    n1 = len(operator_counts.keys())  # Number of unique operators

    return N1, n1

# Use the function
file = "..\Contracts\MyContract.sol"
N1, n1 = count_operators(file)
print(f"N1 = {N1}, n1 = {n1}")

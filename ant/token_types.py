from SolidityLexer import SolidityLexer

operator_types = [
    SolidityLexer.While, SolidityLexer.LParen, SolidityLexer.RParen,
    SolidityLexer.LBrack, SolidityLexer.RBrace, SolidityLexer.LBrace,
    # SolidityLexer.RBrack, We won't count ], because it not a seprate operation like a closing ) or }
    SolidityLexer.Colon, SolidityLexer.Semicolon,
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
]

operand_types = [    
    # Identifiers are used for variables and funtions
    # Just need to make sure function and contract definifions aren't counted.
    # So if a Indentifier is after a function or contract token it shouldn't be counted.
    SolidityLexer.Identifier, SolidityLexer.DecimalNumber, SolidityLexer.HexNumber,
    SolidityLexer.OctalNumber, SolidityLexer.False_, SolidityLexer.True_,
    SolidityLexer.Hex, SolidityLexer.DecimalNumberFollowedByIdentifier,
    SolidityLexer.HexString, SolidityLexer.HexNumber, SolidityLexer.String,
    SolidityLexer.NonEmptyStringLiteral, SolidityLexer.EmptyStringLiteral,
    SolidityLexer.UnicodeStringLiteral,
    # add any other token types you want to count as operands...
]
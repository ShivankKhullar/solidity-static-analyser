from SolidityLexer import SolidityLexer

operator_types = [
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
]

operand_types = [
    # Add your operand types here...
]
# Generated from SolidityParser.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .SolidityParser import SolidityParser
else:
    from SolidityParser import SolidityParser

# This class defines a complete listener for a parse tree produced by SolidityParser.
class SolidityParserListener(ParseTreeListener):

    # Enter a parse tree produced by SolidityParser#sourceUnit.
    def enterSourceUnit(self, ctx:SolidityParser.SourceUnitContext):
        pass

    # Exit a parse tree produced by SolidityParser#sourceUnit.
    def exitSourceUnit(self, ctx:SolidityParser.SourceUnitContext):
        pass


    # Enter a parse tree produced by SolidityParser#pragmaDirective.
    def enterPragmaDirective(self, ctx:SolidityParser.PragmaDirectiveContext):
        pass

    # Exit a parse tree produced by SolidityParser#pragmaDirective.
    def exitPragmaDirective(self, ctx:SolidityParser.PragmaDirectiveContext):
        pass


    # Enter a parse tree produced by SolidityParser#importDirective.
    def enterImportDirective(self, ctx:SolidityParser.ImportDirectiveContext):
        pass

    # Exit a parse tree produced by SolidityParser#importDirective.
    def exitImportDirective(self, ctx:SolidityParser.ImportDirectiveContext):
        pass


    # Enter a parse tree produced by SolidityParser#importAliases.
    def enterImportAliases(self, ctx:SolidityParser.ImportAliasesContext):
        pass

    # Exit a parse tree produced by SolidityParser#importAliases.
    def exitImportAliases(self, ctx:SolidityParser.ImportAliasesContext):
        pass


    # Enter a parse tree produced by SolidityParser#path.
    def enterPath(self, ctx:SolidityParser.PathContext):
        pass

    # Exit a parse tree produced by SolidityParser#path.
    def exitPath(self, ctx:SolidityParser.PathContext):
        pass


    # Enter a parse tree produced by SolidityParser#symbolAliases.
    def enterSymbolAliases(self, ctx:SolidityParser.SymbolAliasesContext):
        pass

    # Exit a parse tree produced by SolidityParser#symbolAliases.
    def exitSymbolAliases(self, ctx:SolidityParser.SymbolAliasesContext):
        pass


    # Enter a parse tree produced by SolidityParser#contractDefinition.
    def enterContractDefinition(self, ctx:SolidityParser.ContractDefinitionContext):
        pass

    # Exit a parse tree produced by SolidityParser#contractDefinition.
    def exitContractDefinition(self, ctx:SolidityParser.ContractDefinitionContext):
        pass


    # Enter a parse tree produced by SolidityParser#interfaceDefinition.
    def enterInterfaceDefinition(self, ctx:SolidityParser.InterfaceDefinitionContext):
        pass

    # Exit a parse tree produced by SolidityParser#interfaceDefinition.
    def exitInterfaceDefinition(self, ctx:SolidityParser.InterfaceDefinitionContext):
        pass


    # Enter a parse tree produced by SolidityParser#libraryDefinition.
    def enterLibraryDefinition(self, ctx:SolidityParser.LibraryDefinitionContext):
        pass

    # Exit a parse tree produced by SolidityParser#libraryDefinition.
    def exitLibraryDefinition(self, ctx:SolidityParser.LibraryDefinitionContext):
        pass


    # Enter a parse tree produced by SolidityParser#inheritanceSpecifierList.
    def enterInheritanceSpecifierList(self, ctx:SolidityParser.InheritanceSpecifierListContext):
        pass

    # Exit a parse tree produced by SolidityParser#inheritanceSpecifierList.
    def exitInheritanceSpecifierList(self, ctx:SolidityParser.InheritanceSpecifierListContext):
        pass


    # Enter a parse tree produced by SolidityParser#inheritanceSpecifier.
    def enterInheritanceSpecifier(self, ctx:SolidityParser.InheritanceSpecifierContext):
        pass

    # Exit a parse tree produced by SolidityParser#inheritanceSpecifier.
    def exitInheritanceSpecifier(self, ctx:SolidityParser.InheritanceSpecifierContext):
        pass


    # Enter a parse tree produced by SolidityParser#contractBodyElement.
    def enterContractBodyElement(self, ctx:SolidityParser.ContractBodyElementContext):
        pass

    # Exit a parse tree produced by SolidityParser#contractBodyElement.
    def exitContractBodyElement(self, ctx:SolidityParser.ContractBodyElementContext):
        pass


    # Enter a parse tree produced by SolidityParser#namedArgument.
    def enterNamedArgument(self, ctx:SolidityParser.NamedArgumentContext):
        pass

    # Exit a parse tree produced by SolidityParser#namedArgument.
    def exitNamedArgument(self, ctx:SolidityParser.NamedArgumentContext):
        pass


    # Enter a parse tree produced by SolidityParser#callArgumentList.
    def enterCallArgumentList(self, ctx:SolidityParser.CallArgumentListContext):
        pass

    # Exit a parse tree produced by SolidityParser#callArgumentList.
    def exitCallArgumentList(self, ctx:SolidityParser.CallArgumentListContext):
        pass


    # Enter a parse tree produced by SolidityParser#identifierPath.
    def enterIdentifierPath(self, ctx:SolidityParser.IdentifierPathContext):
        pass

    # Exit a parse tree produced by SolidityParser#identifierPath.
    def exitIdentifierPath(self, ctx:SolidityParser.IdentifierPathContext):
        pass


    # Enter a parse tree produced by SolidityParser#modifierInvocation.
    def enterModifierInvocation(self, ctx:SolidityParser.ModifierInvocationContext):
        pass

    # Exit a parse tree produced by SolidityParser#modifierInvocation.
    def exitModifierInvocation(self, ctx:SolidityParser.ModifierInvocationContext):
        pass


    # Enter a parse tree produced by SolidityParser#visibility.
    def enterVisibility(self, ctx:SolidityParser.VisibilityContext):
        pass

    # Exit a parse tree produced by SolidityParser#visibility.
    def exitVisibility(self, ctx:SolidityParser.VisibilityContext):
        pass


    # Enter a parse tree produced by SolidityParser#parameterList.
    def enterParameterList(self, ctx:SolidityParser.ParameterListContext):
        pass

    # Exit a parse tree produced by SolidityParser#parameterList.
    def exitParameterList(self, ctx:SolidityParser.ParameterListContext):
        pass


    # Enter a parse tree produced by SolidityParser#parameterDeclaration.
    def enterParameterDeclaration(self, ctx:SolidityParser.ParameterDeclarationContext):
        pass

    # Exit a parse tree produced by SolidityParser#parameterDeclaration.
    def exitParameterDeclaration(self, ctx:SolidityParser.ParameterDeclarationContext):
        pass


    # Enter a parse tree produced by SolidityParser#constructorDefinition.
    def enterConstructorDefinition(self, ctx:SolidityParser.ConstructorDefinitionContext):
        pass

    # Exit a parse tree produced by SolidityParser#constructorDefinition.
    def exitConstructorDefinition(self, ctx:SolidityParser.ConstructorDefinitionContext):
        pass


    # Enter a parse tree produced by SolidityParser#stateMutability.
    def enterStateMutability(self, ctx:SolidityParser.StateMutabilityContext):
        pass

    # Exit a parse tree produced by SolidityParser#stateMutability.
    def exitStateMutability(self, ctx:SolidityParser.StateMutabilityContext):
        pass


    # Enter a parse tree produced by SolidityParser#overrideSpecifier.
    def enterOverrideSpecifier(self, ctx:SolidityParser.OverrideSpecifierContext):
        pass

    # Exit a parse tree produced by SolidityParser#overrideSpecifier.
    def exitOverrideSpecifier(self, ctx:SolidityParser.OverrideSpecifierContext):
        pass


    # Enter a parse tree produced by SolidityParser#functionDefinition.
    def enterFunctionDefinition(self, ctx:SolidityParser.FunctionDefinitionContext):
        pass

    # Exit a parse tree produced by SolidityParser#functionDefinition.
    def exitFunctionDefinition(self, ctx:SolidityParser.FunctionDefinitionContext):
        pass


    # Enter a parse tree produced by SolidityParser#modifierDefinition.
    def enterModifierDefinition(self, ctx:SolidityParser.ModifierDefinitionContext):
        pass

    # Exit a parse tree produced by SolidityParser#modifierDefinition.
    def exitModifierDefinition(self, ctx:SolidityParser.ModifierDefinitionContext):
        pass


    # Enter a parse tree produced by SolidityParser#fallbackFunctionDefinition.
    def enterFallbackFunctionDefinition(self, ctx:SolidityParser.FallbackFunctionDefinitionContext):
        pass

    # Exit a parse tree produced by SolidityParser#fallbackFunctionDefinition.
    def exitFallbackFunctionDefinition(self, ctx:SolidityParser.FallbackFunctionDefinitionContext):
        pass


    # Enter a parse tree produced by SolidityParser#receiveFunctionDefinition.
    def enterReceiveFunctionDefinition(self, ctx:SolidityParser.ReceiveFunctionDefinitionContext):
        pass

    # Exit a parse tree produced by SolidityParser#receiveFunctionDefinition.
    def exitReceiveFunctionDefinition(self, ctx:SolidityParser.ReceiveFunctionDefinitionContext):
        pass


    # Enter a parse tree produced by SolidityParser#structDefinition.
    def enterStructDefinition(self, ctx:SolidityParser.StructDefinitionContext):
        pass

    # Exit a parse tree produced by SolidityParser#structDefinition.
    def exitStructDefinition(self, ctx:SolidityParser.StructDefinitionContext):
        pass


    # Enter a parse tree produced by SolidityParser#structMember.
    def enterStructMember(self, ctx:SolidityParser.StructMemberContext):
        pass

    # Exit a parse tree produced by SolidityParser#structMember.
    def exitStructMember(self, ctx:SolidityParser.StructMemberContext):
        pass


    # Enter a parse tree produced by SolidityParser#enumDefinition.
    def enterEnumDefinition(self, ctx:SolidityParser.EnumDefinitionContext):
        pass

    # Exit a parse tree produced by SolidityParser#enumDefinition.
    def exitEnumDefinition(self, ctx:SolidityParser.EnumDefinitionContext):
        pass


    # Enter a parse tree produced by SolidityParser#userDefinedValueTypeDefinition.
    def enterUserDefinedValueTypeDefinition(self, ctx:SolidityParser.UserDefinedValueTypeDefinitionContext):
        pass

    # Exit a parse tree produced by SolidityParser#userDefinedValueTypeDefinition.
    def exitUserDefinedValueTypeDefinition(self, ctx:SolidityParser.UserDefinedValueTypeDefinitionContext):
        pass


    # Enter a parse tree produced by SolidityParser#stateVariableDeclaration.
    def enterStateVariableDeclaration(self, ctx:SolidityParser.StateVariableDeclarationContext):
        pass

    # Exit a parse tree produced by SolidityParser#stateVariableDeclaration.
    def exitStateVariableDeclaration(self, ctx:SolidityParser.StateVariableDeclarationContext):
        pass


    # Enter a parse tree produced by SolidityParser#constantVariableDeclaration.
    def enterConstantVariableDeclaration(self, ctx:SolidityParser.ConstantVariableDeclarationContext):
        pass

    # Exit a parse tree produced by SolidityParser#constantVariableDeclaration.
    def exitConstantVariableDeclaration(self, ctx:SolidityParser.ConstantVariableDeclarationContext):
        pass


    # Enter a parse tree produced by SolidityParser#eventParameter.
    def enterEventParameter(self, ctx:SolidityParser.EventParameterContext):
        pass

    # Exit a parse tree produced by SolidityParser#eventParameter.
    def exitEventParameter(self, ctx:SolidityParser.EventParameterContext):
        pass


    # Enter a parse tree produced by SolidityParser#eventDefinition.
    def enterEventDefinition(self, ctx:SolidityParser.EventDefinitionContext):
        pass

    # Exit a parse tree produced by SolidityParser#eventDefinition.
    def exitEventDefinition(self, ctx:SolidityParser.EventDefinitionContext):
        pass


    # Enter a parse tree produced by SolidityParser#errorParameter.
    def enterErrorParameter(self, ctx:SolidityParser.ErrorParameterContext):
        pass

    # Exit a parse tree produced by SolidityParser#errorParameter.
    def exitErrorParameter(self, ctx:SolidityParser.ErrorParameterContext):
        pass


    # Enter a parse tree produced by SolidityParser#errorDefinition.
    def enterErrorDefinition(self, ctx:SolidityParser.ErrorDefinitionContext):
        pass

    # Exit a parse tree produced by SolidityParser#errorDefinition.
    def exitErrorDefinition(self, ctx:SolidityParser.ErrorDefinitionContext):
        pass


    # Enter a parse tree produced by SolidityParser#userDefinableOperator.
    def enterUserDefinableOperator(self, ctx:SolidityParser.UserDefinableOperatorContext):
        pass

    # Exit a parse tree produced by SolidityParser#userDefinableOperator.
    def exitUserDefinableOperator(self, ctx:SolidityParser.UserDefinableOperatorContext):
        pass


    # Enter a parse tree produced by SolidityParser#usingDirective.
    def enterUsingDirective(self, ctx:SolidityParser.UsingDirectiveContext):
        pass

    # Exit a parse tree produced by SolidityParser#usingDirective.
    def exitUsingDirective(self, ctx:SolidityParser.UsingDirectiveContext):
        pass


    # Enter a parse tree produced by SolidityParser#typeName.
    def enterTypeName(self, ctx:SolidityParser.TypeNameContext):
        pass

    # Exit a parse tree produced by SolidityParser#typeName.
    def exitTypeName(self, ctx:SolidityParser.TypeNameContext):
        pass


    # Enter a parse tree produced by SolidityParser#elementaryTypeName.
    def enterElementaryTypeName(self, ctx:SolidityParser.ElementaryTypeNameContext):
        pass

    # Exit a parse tree produced by SolidityParser#elementaryTypeName.
    def exitElementaryTypeName(self, ctx:SolidityParser.ElementaryTypeNameContext):
        pass


    # Enter a parse tree produced by SolidityParser#functionTypeName.
    def enterFunctionTypeName(self, ctx:SolidityParser.FunctionTypeNameContext):
        pass

    # Exit a parse tree produced by SolidityParser#functionTypeName.
    def exitFunctionTypeName(self, ctx:SolidityParser.FunctionTypeNameContext):
        pass


    # Enter a parse tree produced by SolidityParser#variableDeclaration.
    def enterVariableDeclaration(self, ctx:SolidityParser.VariableDeclarationContext):
        pass

    # Exit a parse tree produced by SolidityParser#variableDeclaration.
    def exitVariableDeclaration(self, ctx:SolidityParser.VariableDeclarationContext):
        pass


    # Enter a parse tree produced by SolidityParser#dataLocation.
    def enterDataLocation(self, ctx:SolidityParser.DataLocationContext):
        pass

    # Exit a parse tree produced by SolidityParser#dataLocation.
    def exitDataLocation(self, ctx:SolidityParser.DataLocationContext):
        pass


    # Enter a parse tree produced by SolidityParser#UnaryPrefixOperation.
    def enterUnaryPrefixOperation(self, ctx:SolidityParser.UnaryPrefixOperationContext):
        pass

    # Exit a parse tree produced by SolidityParser#UnaryPrefixOperation.
    def exitUnaryPrefixOperation(self, ctx:SolidityParser.UnaryPrefixOperationContext):
        pass


    # Enter a parse tree produced by SolidityParser#PrimaryExpression.
    def enterPrimaryExpression(self, ctx:SolidityParser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by SolidityParser#PrimaryExpression.
    def exitPrimaryExpression(self, ctx:SolidityParser.PrimaryExpressionContext):
        pass


    # Enter a parse tree produced by SolidityParser#OrderComparison.
    def enterOrderComparison(self, ctx:SolidityParser.OrderComparisonContext):
        pass

    # Exit a parse tree produced by SolidityParser#OrderComparison.
    def exitOrderComparison(self, ctx:SolidityParser.OrderComparisonContext):
        pass


    # Enter a parse tree produced by SolidityParser#Conditional.
    def enterConditional(self, ctx:SolidityParser.ConditionalContext):
        pass

    # Exit a parse tree produced by SolidityParser#Conditional.
    def exitConditional(self, ctx:SolidityParser.ConditionalContext):
        pass


    # Enter a parse tree produced by SolidityParser#PayableConversion.
    def enterPayableConversion(self, ctx:SolidityParser.PayableConversionContext):
        pass

    # Exit a parse tree produced by SolidityParser#PayableConversion.
    def exitPayableConversion(self, ctx:SolidityParser.PayableConversionContext):
        pass


    # Enter a parse tree produced by SolidityParser#Assignment.
    def enterAssignment(self, ctx:SolidityParser.AssignmentContext):
        pass

    # Exit a parse tree produced by SolidityParser#Assignment.
    def exitAssignment(self, ctx:SolidityParser.AssignmentContext):
        pass


    # Enter a parse tree produced by SolidityParser#UnarySuffixOperation.
    def enterUnarySuffixOperation(self, ctx:SolidityParser.UnarySuffixOperationContext):
        pass

    # Exit a parse tree produced by SolidityParser#UnarySuffixOperation.
    def exitUnarySuffixOperation(self, ctx:SolidityParser.UnarySuffixOperationContext):
        pass


    # Enter a parse tree produced by SolidityParser#ShiftOperation.
    def enterShiftOperation(self, ctx:SolidityParser.ShiftOperationContext):
        pass

    # Exit a parse tree produced by SolidityParser#ShiftOperation.
    def exitShiftOperation(self, ctx:SolidityParser.ShiftOperationContext):
        pass


    # Enter a parse tree produced by SolidityParser#BitAndOperation.
    def enterBitAndOperation(self, ctx:SolidityParser.BitAndOperationContext):
        pass

    # Exit a parse tree produced by SolidityParser#BitAndOperation.
    def exitBitAndOperation(self, ctx:SolidityParser.BitAndOperationContext):
        pass


    # Enter a parse tree produced by SolidityParser#FunctionCall.
    def enterFunctionCall(self, ctx:SolidityParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by SolidityParser#FunctionCall.
    def exitFunctionCall(self, ctx:SolidityParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by SolidityParser#IndexRangeAccess.
    def enterIndexRangeAccess(self, ctx:SolidityParser.IndexRangeAccessContext):
        pass

    # Exit a parse tree produced by SolidityParser#IndexRangeAccess.
    def exitIndexRangeAccess(self, ctx:SolidityParser.IndexRangeAccessContext):
        pass


    # Enter a parse tree produced by SolidityParser#IndexAccess.
    def enterIndexAccess(self, ctx:SolidityParser.IndexAccessContext):
        pass

    # Exit a parse tree produced by SolidityParser#IndexAccess.
    def exitIndexAccess(self, ctx:SolidityParser.IndexAccessContext):
        pass


    # Enter a parse tree produced by SolidityParser#AddSubOperation.
    def enterAddSubOperation(self, ctx:SolidityParser.AddSubOperationContext):
        pass

    # Exit a parse tree produced by SolidityParser#AddSubOperation.
    def exitAddSubOperation(self, ctx:SolidityParser.AddSubOperationContext):
        pass


    # Enter a parse tree produced by SolidityParser#BitOrOperation.
    def enterBitOrOperation(self, ctx:SolidityParser.BitOrOperationContext):
        pass

    # Exit a parse tree produced by SolidityParser#BitOrOperation.
    def exitBitOrOperation(self, ctx:SolidityParser.BitOrOperationContext):
        pass


    # Enter a parse tree produced by SolidityParser#ExpOperation.
    def enterExpOperation(self, ctx:SolidityParser.ExpOperationContext):
        pass

    # Exit a parse tree produced by SolidityParser#ExpOperation.
    def exitExpOperation(self, ctx:SolidityParser.ExpOperationContext):
        pass


    # Enter a parse tree produced by SolidityParser#AndOperation.
    def enterAndOperation(self, ctx:SolidityParser.AndOperationContext):
        pass

    # Exit a parse tree produced by SolidityParser#AndOperation.
    def exitAndOperation(self, ctx:SolidityParser.AndOperationContext):
        pass


    # Enter a parse tree produced by SolidityParser#InlineArray.
    def enterInlineArray(self, ctx:SolidityParser.InlineArrayContext):
        pass

    # Exit a parse tree produced by SolidityParser#InlineArray.
    def exitInlineArray(self, ctx:SolidityParser.InlineArrayContext):
        pass


    # Enter a parse tree produced by SolidityParser#OrOperation.
    def enterOrOperation(self, ctx:SolidityParser.OrOperationContext):
        pass

    # Exit a parse tree produced by SolidityParser#OrOperation.
    def exitOrOperation(self, ctx:SolidityParser.OrOperationContext):
        pass


    # Enter a parse tree produced by SolidityParser#MemberAccess.
    def enterMemberAccess(self, ctx:SolidityParser.MemberAccessContext):
        pass

    # Exit a parse tree produced by SolidityParser#MemberAccess.
    def exitMemberAccess(self, ctx:SolidityParser.MemberAccessContext):
        pass


    # Enter a parse tree produced by SolidityParser#MulDivModOperation.
    def enterMulDivModOperation(self, ctx:SolidityParser.MulDivModOperationContext):
        pass

    # Exit a parse tree produced by SolidityParser#MulDivModOperation.
    def exitMulDivModOperation(self, ctx:SolidityParser.MulDivModOperationContext):
        pass


    # Enter a parse tree produced by SolidityParser#FunctionCallOptions.
    def enterFunctionCallOptions(self, ctx:SolidityParser.FunctionCallOptionsContext):
        pass

    # Exit a parse tree produced by SolidityParser#FunctionCallOptions.
    def exitFunctionCallOptions(self, ctx:SolidityParser.FunctionCallOptionsContext):
        pass


    # Enter a parse tree produced by SolidityParser#NewExpr.
    def enterNewExpr(self, ctx:SolidityParser.NewExprContext):
        pass

    # Exit a parse tree produced by SolidityParser#NewExpr.
    def exitNewExpr(self, ctx:SolidityParser.NewExprContext):
        pass


    # Enter a parse tree produced by SolidityParser#BitXorOperation.
    def enterBitXorOperation(self, ctx:SolidityParser.BitXorOperationContext):
        pass

    # Exit a parse tree produced by SolidityParser#BitXorOperation.
    def exitBitXorOperation(self, ctx:SolidityParser.BitXorOperationContext):
        pass


    # Enter a parse tree produced by SolidityParser#Tuple.
    def enterTuple(self, ctx:SolidityParser.TupleContext):
        pass

    # Exit a parse tree produced by SolidityParser#Tuple.
    def exitTuple(self, ctx:SolidityParser.TupleContext):
        pass


    # Enter a parse tree produced by SolidityParser#EqualityComparison.
    def enterEqualityComparison(self, ctx:SolidityParser.EqualityComparisonContext):
        pass

    # Exit a parse tree produced by SolidityParser#EqualityComparison.
    def exitEqualityComparison(self, ctx:SolidityParser.EqualityComparisonContext):
        pass


    # Enter a parse tree produced by SolidityParser#MetaType.
    def enterMetaType(self, ctx:SolidityParser.MetaTypeContext):
        pass

    # Exit a parse tree produced by SolidityParser#MetaType.
    def exitMetaType(self, ctx:SolidityParser.MetaTypeContext):
        pass


    # Enter a parse tree produced by SolidityParser#assignOp.
    def enterAssignOp(self, ctx:SolidityParser.AssignOpContext):
        pass

    # Exit a parse tree produced by SolidityParser#assignOp.
    def exitAssignOp(self, ctx:SolidityParser.AssignOpContext):
        pass


    # Enter a parse tree produced by SolidityParser#tupleExpression.
    def enterTupleExpression(self, ctx:SolidityParser.TupleExpressionContext):
        pass

    # Exit a parse tree produced by SolidityParser#tupleExpression.
    def exitTupleExpression(self, ctx:SolidityParser.TupleExpressionContext):
        pass


    # Enter a parse tree produced by SolidityParser#inlineArrayExpression.
    def enterInlineArrayExpression(self, ctx:SolidityParser.InlineArrayExpressionContext):
        pass

    # Exit a parse tree produced by SolidityParser#inlineArrayExpression.
    def exitInlineArrayExpression(self, ctx:SolidityParser.InlineArrayExpressionContext):
        pass


    # Enter a parse tree produced by SolidityParser#identifier.
    def enterIdentifier(self, ctx:SolidityParser.IdentifierContext):
        pass

    # Exit a parse tree produced by SolidityParser#identifier.
    def exitIdentifier(self, ctx:SolidityParser.IdentifierContext):
        pass


    # Enter a parse tree produced by SolidityParser#literal.
    def enterLiteral(self, ctx:SolidityParser.LiteralContext):
        pass

    # Exit a parse tree produced by SolidityParser#literal.
    def exitLiteral(self, ctx:SolidityParser.LiteralContext):
        pass


    # Enter a parse tree produced by SolidityParser#literalWithSubDenomination.
    def enterLiteralWithSubDenomination(self, ctx:SolidityParser.LiteralWithSubDenominationContext):
        pass

    # Exit a parse tree produced by SolidityParser#literalWithSubDenomination.
    def exitLiteralWithSubDenomination(self, ctx:SolidityParser.LiteralWithSubDenominationContext):
        pass


    # Enter a parse tree produced by SolidityParser#booleanLiteral.
    def enterBooleanLiteral(self, ctx:SolidityParser.BooleanLiteralContext):
        pass

    # Exit a parse tree produced by SolidityParser#booleanLiteral.
    def exitBooleanLiteral(self, ctx:SolidityParser.BooleanLiteralContext):
        pass


    # Enter a parse tree produced by SolidityParser#stringLiteral.
    def enterStringLiteral(self, ctx:SolidityParser.StringLiteralContext):
        pass

    # Exit a parse tree produced by SolidityParser#stringLiteral.
    def exitStringLiteral(self, ctx:SolidityParser.StringLiteralContext):
        pass


    # Enter a parse tree produced by SolidityParser#hexStringLiteral.
    def enterHexStringLiteral(self, ctx:SolidityParser.HexStringLiteralContext):
        pass

    # Exit a parse tree produced by SolidityParser#hexStringLiteral.
    def exitHexStringLiteral(self, ctx:SolidityParser.HexStringLiteralContext):
        pass


    # Enter a parse tree produced by SolidityParser#unicodeStringLiteral.
    def enterUnicodeStringLiteral(self, ctx:SolidityParser.UnicodeStringLiteralContext):
        pass

    # Exit a parse tree produced by SolidityParser#unicodeStringLiteral.
    def exitUnicodeStringLiteral(self, ctx:SolidityParser.UnicodeStringLiteralContext):
        pass


    # Enter a parse tree produced by SolidityParser#numberLiteral.
    def enterNumberLiteral(self, ctx:SolidityParser.NumberLiteralContext):
        pass

    # Exit a parse tree produced by SolidityParser#numberLiteral.
    def exitNumberLiteral(self, ctx:SolidityParser.NumberLiteralContext):
        pass


    # Enter a parse tree produced by SolidityParser#block.
    def enterBlock(self, ctx:SolidityParser.BlockContext):
        pass

    # Exit a parse tree produced by SolidityParser#block.
    def exitBlock(self, ctx:SolidityParser.BlockContext):
        pass


    # Enter a parse tree produced by SolidityParser#uncheckedBlock.
    def enterUncheckedBlock(self, ctx:SolidityParser.UncheckedBlockContext):
        pass

    # Exit a parse tree produced by SolidityParser#uncheckedBlock.
    def exitUncheckedBlock(self, ctx:SolidityParser.UncheckedBlockContext):
        pass


    # Enter a parse tree produced by SolidityParser#statement.
    def enterStatement(self, ctx:SolidityParser.StatementContext):
        pass

    # Exit a parse tree produced by SolidityParser#statement.
    def exitStatement(self, ctx:SolidityParser.StatementContext):
        pass


    # Enter a parse tree produced by SolidityParser#simpleStatement.
    def enterSimpleStatement(self, ctx:SolidityParser.SimpleStatementContext):
        pass

    # Exit a parse tree produced by SolidityParser#simpleStatement.
    def exitSimpleStatement(self, ctx:SolidityParser.SimpleStatementContext):
        pass


    # Enter a parse tree produced by SolidityParser#ifStatement.
    def enterIfStatement(self, ctx:SolidityParser.IfStatementContext):
        pass

    # Exit a parse tree produced by SolidityParser#ifStatement.
    def exitIfStatement(self, ctx:SolidityParser.IfStatementContext):
        pass


    # Enter a parse tree produced by SolidityParser#forStatement.
    def enterForStatement(self, ctx:SolidityParser.ForStatementContext):
        pass

    # Exit a parse tree produced by SolidityParser#forStatement.
    def exitForStatement(self, ctx:SolidityParser.ForStatementContext):
        pass


    # Enter a parse tree produced by SolidityParser#whileStatement.
    def enterWhileStatement(self, ctx:SolidityParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by SolidityParser#whileStatement.
    def exitWhileStatement(self, ctx:SolidityParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by SolidityParser#doWhileStatement.
    def enterDoWhileStatement(self, ctx:SolidityParser.DoWhileStatementContext):
        pass

    # Exit a parse tree produced by SolidityParser#doWhileStatement.
    def exitDoWhileStatement(self, ctx:SolidityParser.DoWhileStatementContext):
        pass


    # Enter a parse tree produced by SolidityParser#continueStatement.
    def enterContinueStatement(self, ctx:SolidityParser.ContinueStatementContext):
        pass

    # Exit a parse tree produced by SolidityParser#continueStatement.
    def exitContinueStatement(self, ctx:SolidityParser.ContinueStatementContext):
        pass


    # Enter a parse tree produced by SolidityParser#breakStatement.
    def enterBreakStatement(self, ctx:SolidityParser.BreakStatementContext):
        pass

    # Exit a parse tree produced by SolidityParser#breakStatement.
    def exitBreakStatement(self, ctx:SolidityParser.BreakStatementContext):
        pass


    # Enter a parse tree produced by SolidityParser#tryStatement.
    def enterTryStatement(self, ctx:SolidityParser.TryStatementContext):
        pass

    # Exit a parse tree produced by SolidityParser#tryStatement.
    def exitTryStatement(self, ctx:SolidityParser.TryStatementContext):
        pass


    # Enter a parse tree produced by SolidityParser#catchClause.
    def enterCatchClause(self, ctx:SolidityParser.CatchClauseContext):
        pass

    # Exit a parse tree produced by SolidityParser#catchClause.
    def exitCatchClause(self, ctx:SolidityParser.CatchClauseContext):
        pass


    # Enter a parse tree produced by SolidityParser#returnStatement.
    def enterReturnStatement(self, ctx:SolidityParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by SolidityParser#returnStatement.
    def exitReturnStatement(self, ctx:SolidityParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by SolidityParser#emitStatement.
    def enterEmitStatement(self, ctx:SolidityParser.EmitStatementContext):
        pass

    # Exit a parse tree produced by SolidityParser#emitStatement.
    def exitEmitStatement(self, ctx:SolidityParser.EmitStatementContext):
        pass


    # Enter a parse tree produced by SolidityParser#revertStatement.
    def enterRevertStatement(self, ctx:SolidityParser.RevertStatementContext):
        pass

    # Exit a parse tree produced by SolidityParser#revertStatement.
    def exitRevertStatement(self, ctx:SolidityParser.RevertStatementContext):
        pass


    # Enter a parse tree produced by SolidityParser#assemblyStatement.
    def enterAssemblyStatement(self, ctx:SolidityParser.AssemblyStatementContext):
        pass

    # Exit a parse tree produced by SolidityParser#assemblyStatement.
    def exitAssemblyStatement(self, ctx:SolidityParser.AssemblyStatementContext):
        pass


    # Enter a parse tree produced by SolidityParser#assemblyFlags.
    def enterAssemblyFlags(self, ctx:SolidityParser.AssemblyFlagsContext):
        pass

    # Exit a parse tree produced by SolidityParser#assemblyFlags.
    def exitAssemblyFlags(self, ctx:SolidityParser.AssemblyFlagsContext):
        pass


    # Enter a parse tree produced by SolidityParser#variableDeclarationList.
    def enterVariableDeclarationList(self, ctx:SolidityParser.VariableDeclarationListContext):
        pass

    # Exit a parse tree produced by SolidityParser#variableDeclarationList.
    def exitVariableDeclarationList(self, ctx:SolidityParser.VariableDeclarationListContext):
        pass


    # Enter a parse tree produced by SolidityParser#variableDeclarationTuple.
    def enterVariableDeclarationTuple(self, ctx:SolidityParser.VariableDeclarationTupleContext):
        pass

    # Exit a parse tree produced by SolidityParser#variableDeclarationTuple.
    def exitVariableDeclarationTuple(self, ctx:SolidityParser.VariableDeclarationTupleContext):
        pass


    # Enter a parse tree produced by SolidityParser#variableDeclarationStatement.
    def enterVariableDeclarationStatement(self, ctx:SolidityParser.VariableDeclarationStatementContext):
        pass

    # Exit a parse tree produced by SolidityParser#variableDeclarationStatement.
    def exitVariableDeclarationStatement(self, ctx:SolidityParser.VariableDeclarationStatementContext):
        pass


    # Enter a parse tree produced by SolidityParser#expressionStatement.
    def enterExpressionStatement(self, ctx:SolidityParser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by SolidityParser#expressionStatement.
    def exitExpressionStatement(self, ctx:SolidityParser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by SolidityParser#mappingType.
    def enterMappingType(self, ctx:SolidityParser.MappingTypeContext):
        pass

    # Exit a parse tree produced by SolidityParser#mappingType.
    def exitMappingType(self, ctx:SolidityParser.MappingTypeContext):
        pass


    # Enter a parse tree produced by SolidityParser#mappingKeyType.
    def enterMappingKeyType(self, ctx:SolidityParser.MappingKeyTypeContext):
        pass

    # Exit a parse tree produced by SolidityParser#mappingKeyType.
    def exitMappingKeyType(self, ctx:SolidityParser.MappingKeyTypeContext):
        pass


    # Enter a parse tree produced by SolidityParser#yulStatement.
    def enterYulStatement(self, ctx:SolidityParser.YulStatementContext):
        pass

    # Exit a parse tree produced by SolidityParser#yulStatement.
    def exitYulStatement(self, ctx:SolidityParser.YulStatementContext):
        pass


    # Enter a parse tree produced by SolidityParser#yulBlock.
    def enterYulBlock(self, ctx:SolidityParser.YulBlockContext):
        pass

    # Exit a parse tree produced by SolidityParser#yulBlock.
    def exitYulBlock(self, ctx:SolidityParser.YulBlockContext):
        pass


    # Enter a parse tree produced by SolidityParser#yulVariableDeclaration.
    def enterYulVariableDeclaration(self, ctx:SolidityParser.YulVariableDeclarationContext):
        pass

    # Exit a parse tree produced by SolidityParser#yulVariableDeclaration.
    def exitYulVariableDeclaration(self, ctx:SolidityParser.YulVariableDeclarationContext):
        pass


    # Enter a parse tree produced by SolidityParser#yulAssignment.
    def enterYulAssignment(self, ctx:SolidityParser.YulAssignmentContext):
        pass

    # Exit a parse tree produced by SolidityParser#yulAssignment.
    def exitYulAssignment(self, ctx:SolidityParser.YulAssignmentContext):
        pass


    # Enter a parse tree produced by SolidityParser#yulIfStatement.
    def enterYulIfStatement(self, ctx:SolidityParser.YulIfStatementContext):
        pass

    # Exit a parse tree produced by SolidityParser#yulIfStatement.
    def exitYulIfStatement(self, ctx:SolidityParser.YulIfStatementContext):
        pass


    # Enter a parse tree produced by SolidityParser#yulForStatement.
    def enterYulForStatement(self, ctx:SolidityParser.YulForStatementContext):
        pass

    # Exit a parse tree produced by SolidityParser#yulForStatement.
    def exitYulForStatement(self, ctx:SolidityParser.YulForStatementContext):
        pass


    # Enter a parse tree produced by SolidityParser#yulSwitchCase.
    def enterYulSwitchCase(self, ctx:SolidityParser.YulSwitchCaseContext):
        pass

    # Exit a parse tree produced by SolidityParser#yulSwitchCase.
    def exitYulSwitchCase(self, ctx:SolidityParser.YulSwitchCaseContext):
        pass


    # Enter a parse tree produced by SolidityParser#yulSwitchStatement.
    def enterYulSwitchStatement(self, ctx:SolidityParser.YulSwitchStatementContext):
        pass

    # Exit a parse tree produced by SolidityParser#yulSwitchStatement.
    def exitYulSwitchStatement(self, ctx:SolidityParser.YulSwitchStatementContext):
        pass


    # Enter a parse tree produced by SolidityParser#yulFunctionDefinition.
    def enterYulFunctionDefinition(self, ctx:SolidityParser.YulFunctionDefinitionContext):
        pass

    # Exit a parse tree produced by SolidityParser#yulFunctionDefinition.
    def exitYulFunctionDefinition(self, ctx:SolidityParser.YulFunctionDefinitionContext):
        pass


    # Enter a parse tree produced by SolidityParser#yulPath.
    def enterYulPath(self, ctx:SolidityParser.YulPathContext):
        pass

    # Exit a parse tree produced by SolidityParser#yulPath.
    def exitYulPath(self, ctx:SolidityParser.YulPathContext):
        pass


    # Enter a parse tree produced by SolidityParser#yulFunctionCall.
    def enterYulFunctionCall(self, ctx:SolidityParser.YulFunctionCallContext):
        pass

    # Exit a parse tree produced by SolidityParser#yulFunctionCall.
    def exitYulFunctionCall(self, ctx:SolidityParser.YulFunctionCallContext):
        pass


    # Enter a parse tree produced by SolidityParser#yulBoolean.
    def enterYulBoolean(self, ctx:SolidityParser.YulBooleanContext):
        pass

    # Exit a parse tree produced by SolidityParser#yulBoolean.
    def exitYulBoolean(self, ctx:SolidityParser.YulBooleanContext):
        pass


    # Enter a parse tree produced by SolidityParser#yulLiteral.
    def enterYulLiteral(self, ctx:SolidityParser.YulLiteralContext):
        pass

    # Exit a parse tree produced by SolidityParser#yulLiteral.
    def exitYulLiteral(self, ctx:SolidityParser.YulLiteralContext):
        pass


    # Enter a parse tree produced by SolidityParser#yulExpression.
    def enterYulExpression(self, ctx:SolidityParser.YulExpressionContext):
        pass

    # Exit a parse tree produced by SolidityParser#yulExpression.
    def exitYulExpression(self, ctx:SolidityParser.YulExpressionContext):
        pass



del SolidityParser
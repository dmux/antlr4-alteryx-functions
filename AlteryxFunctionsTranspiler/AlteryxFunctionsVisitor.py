# Generated from AlteryxFunctions.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .AlteryxFunctionsParser import AlteryxFunctionsParser
else:
    from AlteryxFunctionsParser import AlteryxFunctionsParser

# This class defines a complete generic visitor for a parse tree produced by AlteryxFunctionsParser.

class AlteryxFunctionsVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by AlteryxFunctionsParser#prog.
    def visitProg(self, ctx:AlteryxFunctionsParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlteryxFunctionsParser#expr.
    def visitExpr(self, ctx:AlteryxFunctionsParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlteryxFunctionsParser#value.
    def visitValue(self, ctx:AlteryxFunctionsParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlteryxFunctionsParser#ifExpr.
    def visitIfExpr(self, ctx:AlteryxFunctionsParser.IfExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlteryxFunctionsParser#iifExpr.
    def visitIifExpr(self, ctx:AlteryxFunctionsParser.IifExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlteryxFunctionsParser#switchExpr.
    def visitSwitchExpr(self, ctx:AlteryxFunctionsParser.SwitchExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlteryxFunctionsParser#casePair.
    def visitCasePair(self, ctx:AlteryxFunctionsParser.CasePairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlteryxFunctionsParser#conversionExpr.
    def visitConversionExpr(self, ctx:AlteryxFunctionsParser.ConversionExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlteryxFunctionsParser#conversionFunction.
    def visitConversionFunction(self, ctx:AlteryxFunctionsParser.ConversionFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlteryxFunctionsParser#condition.
    def visitCondition(self, ctx:AlteryxFunctionsParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlteryxFunctionsParser#expression.
    def visitExpression(self, ctx:AlteryxFunctionsParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlteryxFunctionsParser#functionCall.
    def visitFunctionCall(self, ctx:AlteryxFunctionsParser.FunctionCallContext):
        return self.visitChildren(ctx)



del AlteryxFunctionsParser
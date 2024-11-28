# Generated from AlteryxFunctions.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,33,108,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,1,0,1,0,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,40,8,1,1,1,1,1,1,1,
        5,1,45,8,1,10,1,12,1,48,9,1,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,5,5,
        74,8,5,10,5,12,5,77,9,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,7,1,7,
        1,7,1,7,1,7,1,8,1,8,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,
        10,3,10,104,8,10,1,11,1,11,1,11,0,1,2,12,0,2,4,6,8,10,12,14,16,18,
        20,22,0,3,1,0,23,28,3,0,16,16,19,19,31,33,1,0,10,14,107,0,24,1,0,
        0,0,2,39,1,0,0,0,4,49,1,0,0,0,6,51,1,0,0,0,8,59,1,0,0,0,10,68,1,
        0,0,0,12,82,1,0,0,0,14,86,1,0,0,0,16,91,1,0,0,0,18,93,1,0,0,0,20,
        103,1,0,0,0,22,105,1,0,0,0,24,25,3,2,1,0,25,26,5,0,0,1,26,1,1,0,
        0,0,27,28,6,1,-1,0,28,40,3,6,3,0,29,40,3,8,4,0,30,40,3,10,5,0,31,
        40,3,14,7,0,32,33,5,22,0,0,33,40,3,2,1,3,34,35,5,1,0,0,35,36,3,2,
        1,0,36,37,5,2,0,0,37,40,1,0,0,0,38,40,3,4,2,0,39,27,1,0,0,0,39,29,
        1,0,0,0,39,30,1,0,0,0,39,31,1,0,0,0,39,32,1,0,0,0,39,34,1,0,0,0,
        39,38,1,0,0,0,40,46,1,0,0,0,41,42,10,4,0,0,42,43,7,0,0,0,43,45,3,
        2,1,5,44,41,1,0,0,0,45,48,1,0,0,0,46,44,1,0,0,0,46,47,1,0,0,0,47,
        3,1,0,0,0,48,46,1,0,0,0,49,50,7,1,0,0,50,5,1,0,0,0,51,52,5,3,0,0,
        52,53,3,18,9,0,53,54,5,4,0,0,54,55,3,2,1,0,55,56,5,5,0,0,56,57,3,
        2,1,0,57,58,5,6,0,0,58,7,1,0,0,0,59,60,5,7,0,0,60,61,5,1,0,0,61,
        62,3,18,9,0,62,63,5,8,0,0,63,64,3,2,1,0,64,65,5,8,0,0,65,66,3,2,
        1,0,66,67,5,2,0,0,67,9,1,0,0,0,68,69,5,9,0,0,69,70,5,1,0,0,70,75,
        3,20,10,0,71,72,5,8,0,0,72,74,3,12,6,0,73,71,1,0,0,0,74,77,1,0,0,
        0,75,73,1,0,0,0,75,76,1,0,0,0,76,78,1,0,0,0,77,75,1,0,0,0,78,79,
        5,8,0,0,79,80,3,2,1,0,80,81,5,2,0,0,81,11,1,0,0,0,82,83,3,20,10,
        0,83,84,5,8,0,0,84,85,3,2,1,0,85,13,1,0,0,0,86,87,3,16,8,0,87,88,
        5,1,0,0,88,89,3,20,10,0,89,90,5,2,0,0,90,15,1,0,0,0,91,92,7,2,0,
        0,92,17,1,0,0,0,93,94,3,20,10,0,94,19,1,0,0,0,95,104,5,15,0,0,96,
        104,5,16,0,0,97,104,5,17,0,0,98,99,5,1,0,0,99,100,3,2,1,0,100,101,
        5,2,0,0,101,104,1,0,0,0,102,104,3,22,11,0,103,95,1,0,0,0,103,96,
        1,0,0,0,103,97,1,0,0,0,103,98,1,0,0,0,103,102,1,0,0,0,104,21,1,0,
        0,0,105,106,3,14,7,0,106,23,1,0,0,0,4,39,46,75,103
    ]

class AlteryxFunctionsParser ( Parser ):

    grammarFileName = "AlteryxFunctions.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'IF'", "'THEN'", "'ELSE'", 
                     "'ENDIF'", "'IIF'", "','", "'SWITCH'", "'TOBOOLEAN'", 
                     "'TODATE'", "'TONUMBER'", "'ToNumber'", "'TOSTRING'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'AND'", "'OR'", "'NOT'", "'=='", "'!='", 
                     "'<'", "'>'", "'<='", "'>='", "'IN'", "'NOT IN'", "'NULL'", 
                     "'TRUE'", "'FALSE'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "TEXT", "NUMBER", 
                      "BOOLEAN", "WS", "STRING", "AND", "OR", "NOT", "EQ", 
                      "NEQ", "LT", "GT", "LEQ", "GEQ", "IN", "NOTIN", "NULL", 
                      "TRUE", "FALSE" ]

    RULE_prog = 0
    RULE_expr = 1
    RULE_value = 2
    RULE_ifExpr = 3
    RULE_iifExpr = 4
    RULE_switchExpr = 5
    RULE_casePair = 6
    RULE_conversionExpr = 7
    RULE_conversionFunction = 8
    RULE_condition = 9
    RULE_expression = 10
    RULE_functionCall = 11

    ruleNames =  [ "prog", "expr", "value", "ifExpr", "iifExpr", "switchExpr", 
                   "casePair", "conversionExpr", "conversionFunction", "condition", 
                   "expression", "functionCall" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    TEXT=15
    NUMBER=16
    BOOLEAN=17
    WS=18
    STRING=19
    AND=20
    OR=21
    NOT=22
    EQ=23
    NEQ=24
    LT=25
    GT=26
    LEQ=27
    GEQ=28
    IN=29
    NOTIN=30
    NULL=31
    TRUE=32
    FALSE=33

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(AlteryxFunctionsParser.ExprContext,0)


        def EOF(self):
            return self.getToken(AlteryxFunctionsParser.EOF, 0)

        def getRuleIndex(self):
            return AlteryxFunctionsParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = AlteryxFunctionsParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.expr(0)
            self.state = 25
            self.match(AlteryxFunctionsParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ifExpr(self):
            return self.getTypedRuleContext(AlteryxFunctionsParser.IfExprContext,0)


        def iifExpr(self):
            return self.getTypedRuleContext(AlteryxFunctionsParser.IifExprContext,0)


        def switchExpr(self):
            return self.getTypedRuleContext(AlteryxFunctionsParser.SwitchExprContext,0)


        def conversionExpr(self):
            return self.getTypedRuleContext(AlteryxFunctionsParser.ConversionExprContext,0)


        def NOT(self):
            return self.getToken(AlteryxFunctionsParser.NOT, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AlteryxFunctionsParser.ExprContext)
            else:
                return self.getTypedRuleContext(AlteryxFunctionsParser.ExprContext,i)


        def value(self):
            return self.getTypedRuleContext(AlteryxFunctionsParser.ValueContext,0)


        def EQ(self):
            return self.getToken(AlteryxFunctionsParser.EQ, 0)

        def NEQ(self):
            return self.getToken(AlteryxFunctionsParser.NEQ, 0)

        def LT(self):
            return self.getToken(AlteryxFunctionsParser.LT, 0)

        def GT(self):
            return self.getToken(AlteryxFunctionsParser.GT, 0)

        def LEQ(self):
            return self.getToken(AlteryxFunctionsParser.LEQ, 0)

        def GEQ(self):
            return self.getToken(AlteryxFunctionsParser.GEQ, 0)

        def getRuleIndex(self):
            return AlteryxFunctionsParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = AlteryxFunctionsParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.state = 28
                self.ifExpr()
                pass
            elif token in [7]:
                self.state = 29
                self.iifExpr()
                pass
            elif token in [9]:
                self.state = 30
                self.switchExpr()
                pass
            elif token in [10, 11, 12, 13, 14]:
                self.state = 31
                self.conversionExpr()
                pass
            elif token in [22]:
                self.state = 32
                self.match(AlteryxFunctionsParser.NOT)
                self.state = 33
                self.expr(3)
                pass
            elif token in [1]:
                self.state = 34
                self.match(AlteryxFunctionsParser.T__0)
                self.state = 35
                self.expr(0)
                self.state = 36
                self.match(AlteryxFunctionsParser.T__1)
                pass
            elif token in [16, 19, 31, 32, 33]:
                self.state = 38
                self.value()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 46
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = AlteryxFunctionsParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 41
                    if not self.precpred(self._ctx, 4):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                    self.state = 42
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 528482304) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 43
                    self.expr(5) 
                self.state = 48
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(AlteryxFunctionsParser.STRING, 0)

        def NUMBER(self):
            return self.getToken(AlteryxFunctionsParser.NUMBER, 0)

        def NULL(self):
            return self.getToken(AlteryxFunctionsParser.NULL, 0)

        def TRUE(self):
            return self.getToken(AlteryxFunctionsParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(AlteryxFunctionsParser.FALSE, 0)

        def getRuleIndex(self):
            return AlteryxFunctionsParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = AlteryxFunctionsParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 15032975360) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition(self):
            return self.getTypedRuleContext(AlteryxFunctionsParser.ConditionContext,0)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AlteryxFunctionsParser.ExprContext)
            else:
                return self.getTypedRuleContext(AlteryxFunctionsParser.ExprContext,i)


        def getRuleIndex(self):
            return AlteryxFunctionsParser.RULE_ifExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfExpr" ):
                listener.enterIfExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfExpr" ):
                listener.exitIfExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfExpr" ):
                return visitor.visitIfExpr(self)
            else:
                return visitor.visitChildren(self)




    def ifExpr(self):

        localctx = AlteryxFunctionsParser.IfExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_ifExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(AlteryxFunctionsParser.T__2)
            self.state = 52
            self.condition()
            self.state = 53
            self.match(AlteryxFunctionsParser.T__3)
            self.state = 54
            self.expr(0)
            self.state = 55
            self.match(AlteryxFunctionsParser.T__4)
            self.state = 56
            self.expr(0)
            self.state = 57
            self.match(AlteryxFunctionsParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IifExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition(self):
            return self.getTypedRuleContext(AlteryxFunctionsParser.ConditionContext,0)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AlteryxFunctionsParser.ExprContext)
            else:
                return self.getTypedRuleContext(AlteryxFunctionsParser.ExprContext,i)


        def getRuleIndex(self):
            return AlteryxFunctionsParser.RULE_iifExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIifExpr" ):
                listener.enterIifExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIifExpr" ):
                listener.exitIifExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIifExpr" ):
                return visitor.visitIifExpr(self)
            else:
                return visitor.visitChildren(self)




    def iifExpr(self):

        localctx = AlteryxFunctionsParser.IifExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_iifExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(AlteryxFunctionsParser.T__6)
            self.state = 60
            self.match(AlteryxFunctionsParser.T__0)
            self.state = 61
            self.condition()
            self.state = 62
            self.match(AlteryxFunctionsParser.T__7)
            self.state = 63
            self.expr(0)
            self.state = 64
            self.match(AlteryxFunctionsParser.T__7)
            self.state = 65
            self.expr(0)
            self.state = 66
            self.match(AlteryxFunctionsParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SwitchExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(AlteryxFunctionsParser.ExpressionContext,0)


        def expr(self):
            return self.getTypedRuleContext(AlteryxFunctionsParser.ExprContext,0)


        def casePair(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AlteryxFunctionsParser.CasePairContext)
            else:
                return self.getTypedRuleContext(AlteryxFunctionsParser.CasePairContext,i)


        def getRuleIndex(self):
            return AlteryxFunctionsParser.RULE_switchExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitchExpr" ):
                listener.enterSwitchExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitchExpr" ):
                listener.exitSwitchExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSwitchExpr" ):
                return visitor.visitSwitchExpr(self)
            else:
                return visitor.visitChildren(self)




    def switchExpr(self):

        localctx = AlteryxFunctionsParser.SwitchExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_switchExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(AlteryxFunctionsParser.T__8)
            self.state = 69
            self.match(AlteryxFunctionsParser.T__0)
            self.state = 70
            self.expression()
            self.state = 75
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 71
                    self.match(AlteryxFunctionsParser.T__7)
                    self.state = 72
                    self.casePair() 
                self.state = 77
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

            self.state = 78
            self.match(AlteryxFunctionsParser.T__7)
            self.state = 79
            self.expr(0)
            self.state = 80
            self.match(AlteryxFunctionsParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CasePairContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(AlteryxFunctionsParser.ExpressionContext,0)


        def expr(self):
            return self.getTypedRuleContext(AlteryxFunctionsParser.ExprContext,0)


        def getRuleIndex(self):
            return AlteryxFunctionsParser.RULE_casePair

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCasePair" ):
                listener.enterCasePair(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCasePair" ):
                listener.exitCasePair(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCasePair" ):
                return visitor.visitCasePair(self)
            else:
                return visitor.visitChildren(self)




    def casePair(self):

        localctx = AlteryxFunctionsParser.CasePairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_casePair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.expression()
            self.state = 83
            self.match(AlteryxFunctionsParser.T__7)
            self.state = 84
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConversionExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conversionFunction(self):
            return self.getTypedRuleContext(AlteryxFunctionsParser.ConversionFunctionContext,0)


        def expression(self):
            return self.getTypedRuleContext(AlteryxFunctionsParser.ExpressionContext,0)


        def getRuleIndex(self):
            return AlteryxFunctionsParser.RULE_conversionExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConversionExpr" ):
                listener.enterConversionExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConversionExpr" ):
                listener.exitConversionExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConversionExpr" ):
                return visitor.visitConversionExpr(self)
            else:
                return visitor.visitChildren(self)




    def conversionExpr(self):

        localctx = AlteryxFunctionsParser.ConversionExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_conversionExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.conversionFunction()
            self.state = 87
            self.match(AlteryxFunctionsParser.T__0)
            self.state = 88
            self.expression()
            self.state = 89
            self.match(AlteryxFunctionsParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConversionFunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AlteryxFunctionsParser.RULE_conversionFunction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConversionFunction" ):
                listener.enterConversionFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConversionFunction" ):
                listener.exitConversionFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConversionFunction" ):
                return visitor.visitConversionFunction(self)
            else:
                return visitor.visitChildren(self)




    def conversionFunction(self):

        localctx = AlteryxFunctionsParser.ConversionFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_conversionFunction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 31744) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(AlteryxFunctionsParser.ExpressionContext,0)


        def getRuleIndex(self):
            return AlteryxFunctionsParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = AlteryxFunctionsParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self):
            return self.getToken(AlteryxFunctionsParser.TEXT, 0)

        def NUMBER(self):
            return self.getToken(AlteryxFunctionsParser.NUMBER, 0)

        def BOOLEAN(self):
            return self.getToken(AlteryxFunctionsParser.BOOLEAN, 0)

        def expr(self):
            return self.getTypedRuleContext(AlteryxFunctionsParser.ExprContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(AlteryxFunctionsParser.FunctionCallContext,0)


        def getRuleIndex(self):
            return AlteryxFunctionsParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = AlteryxFunctionsParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_expression)
        try:
            self.state = 103
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 95
                self.match(AlteryxFunctionsParser.TEXT)
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 96
                self.match(AlteryxFunctionsParser.NUMBER)
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 3)
                self.state = 97
                self.match(AlteryxFunctionsParser.BOOLEAN)
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 4)
                self.state = 98
                self.match(AlteryxFunctionsParser.T__0)
                self.state = 99
                self.expr(0)
                self.state = 100
                self.match(AlteryxFunctionsParser.T__1)
                pass
            elif token in [10, 11, 12, 13, 14]:
                self.enterOuterAlt(localctx, 5)
                self.state = 102
                self.functionCall()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conversionExpr(self):
            return self.getTypedRuleContext(AlteryxFunctionsParser.ConversionExprContext,0)


        def getRuleIndex(self):
            return AlteryxFunctionsParser.RULE_functionCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCall" ):
                return visitor.visitFunctionCall(self)
            else:
                return visitor.visitChildren(self)




    def functionCall(self):

        localctx = AlteryxFunctionsParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_functionCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.conversionExpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         





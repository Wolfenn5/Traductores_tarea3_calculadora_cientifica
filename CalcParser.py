# Generated from Calc.g4 by ANTLR 4.13.2
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
        4,1,12,51,2,0,7,0,2,1,7,1,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,29,
        8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        5,1,46,8,1,10,1,12,1,49,9,1,1,1,0,1,2,2,0,2,0,0,57,0,4,1,0,0,0,2,
        28,1,0,0,0,4,5,3,2,1,0,5,6,5,0,0,1,6,1,1,0,0,0,7,8,6,1,-1,0,8,9,
        5,2,0,0,9,10,5,3,0,0,10,11,3,2,1,0,11,12,5,4,0,0,12,29,1,0,0,0,13,
        14,5,5,0,0,14,15,5,3,0,0,15,16,3,2,1,0,16,17,5,4,0,0,17,29,1,0,0,
        0,18,19,5,6,0,0,19,20,5,3,0,0,20,21,3,2,1,0,21,22,5,4,0,0,22,29,
        1,0,0,0,23,24,5,3,0,0,24,25,3,2,1,0,25,26,5,4,0,0,26,29,1,0,0,0,
        27,29,5,11,0,0,28,7,1,0,0,0,28,13,1,0,0,0,28,18,1,0,0,0,28,23,1,
        0,0,0,28,27,1,0,0,0,29,47,1,0,0,0,30,31,10,10,0,0,31,32,5,1,0,0,
        32,46,3,2,1,11,33,34,10,6,0,0,34,35,5,7,0,0,35,46,3,2,1,7,36,37,
        10,5,0,0,37,38,5,8,0,0,38,46,3,2,1,6,39,40,10,4,0,0,40,41,5,9,0,
        0,41,46,3,2,1,5,42,43,10,3,0,0,43,44,5,10,0,0,44,46,3,2,1,4,45,30,
        1,0,0,0,45,33,1,0,0,0,45,36,1,0,0,0,45,39,1,0,0,0,45,42,1,0,0,0,
        46,49,1,0,0,0,47,45,1,0,0,0,47,48,1,0,0,0,48,3,1,0,0,0,49,47,1,0,
        0,0,3,28,45,47
    ]

class CalcParser ( Parser ):

    grammarFileName = "Calc.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'^'", "'sin'", "'('", "')'", "'cos'", 
                     "'log'", "'*'", "'/'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "NUM", "WS" ]

    RULE_prog = 0
    RULE_expr = 1

    ruleNames =  [ "prog", "expr" ]

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
    NUM=11
    WS=12

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
            return self.getTypedRuleContext(CalcParser.ExprContext,0)


        def EOF(self):
            return self.getToken(CalcParser.EOF, 0)

        def getRuleIndex(self):
            return CalcParser.RULE_prog

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

        localctx = CalcParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.expr(0)
            self.state = 5
            self.match(CalcParser.EOF)
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


        def getRuleIndex(self):
            return CalcParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class MulExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalcParser.ExprContext)
            else:
                return self.getTypedRuleContext(CalcParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulExpr" ):
                listener.enterMulExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulExpr" ):
                listener.exitMulExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulExpr" ):
                return visitor.visitMulExpr(self)
            else:
                return visitor.visitChildren(self)


    class PowerExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalcParser.ExprContext)
            else:
                return self.getTypedRuleContext(CalcParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPowerExpr" ):
                listener.enterPowerExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPowerExpr" ):
                listener.exitPowerExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPowerExpr" ):
                return visitor.visitPowerExpr(self)
            else:
                return visitor.visitChildren(self)


    class DivExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalcParser.ExprContext)
            else:
                return self.getTypedRuleContext(CalcParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDivExpr" ):
                listener.enterDivExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDivExpr" ):
                listener.exitDivExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDivExpr" ):
                return visitor.visitDivExpr(self)
            else:
                return visitor.visitChildren(self)


    class NumberExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(CalcParser.NUM, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumberExpr" ):
                listener.enterNumberExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumberExpr" ):
                listener.exitNumberExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumberExpr" ):
                return visitor.visitNumberExpr(self)
            else:
                return visitor.visitChildren(self)


    class SubExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalcParser.ExprContext)
            else:
                return self.getTypedRuleContext(CalcParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubExpr" ):
                listener.enterSubExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubExpr" ):
                listener.exitSubExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubExpr" ):
                return visitor.visitSubExpr(self)
            else:
                return visitor.visitChildren(self)


    class LogExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(CalcParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogExpr" ):
                listener.enterLogExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogExpr" ):
                listener.exitLogExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogExpr" ):
                return visitor.visitLogExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParentExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(CalcParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParentExpr" ):
                listener.enterParentExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParentExpr" ):
                listener.exitParentExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParentExpr" ):
                return visitor.visitParentExpr(self)
            else:
                return visitor.visitChildren(self)


    class AddExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalcParser.ExprContext)
            else:
                return self.getTypedRuleContext(CalcParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddExpr" ):
                listener.enterAddExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddExpr" ):
                listener.exitAddExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddExpr" ):
                return visitor.visitAddExpr(self)
            else:
                return visitor.visitChildren(self)


    class SinExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(CalcParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSinExpr" ):
                listener.enterSinExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSinExpr" ):
                listener.exitSinExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSinExpr" ):
                return visitor.visitSinExpr(self)
            else:
                return visitor.visitChildren(self)


    class CosExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(CalcParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCosExpr" ):
                listener.enterCosExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCosExpr" ):
                listener.exitCosExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCosExpr" ):
                return visitor.visitCosExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CalcParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                localctx = CalcParser.SinExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 8
                self.match(CalcParser.T__1)
                self.state = 9
                self.match(CalcParser.T__2)
                self.state = 10
                self.expr(0)
                self.state = 11
                self.match(CalcParser.T__3)
                pass
            elif token in [5]:
                localctx = CalcParser.CosExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 13
                self.match(CalcParser.T__4)
                self.state = 14
                self.match(CalcParser.T__2)
                self.state = 15
                self.expr(0)
                self.state = 16
                self.match(CalcParser.T__3)
                pass
            elif token in [6]:
                localctx = CalcParser.LogExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 18
                self.match(CalcParser.T__5)
                self.state = 19
                self.match(CalcParser.T__2)
                self.state = 20
                self.expr(0)
                self.state = 21
                self.match(CalcParser.T__3)
                pass
            elif token in [3]:
                localctx = CalcParser.ParentExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 23
                self.match(CalcParser.T__2)
                self.state = 24
                self.expr(0)
                self.state = 25
                self.match(CalcParser.T__3)
                pass
            elif token in [11]:
                localctx = CalcParser.NumberExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 27
                self.match(CalcParser.NUM)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 47
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 45
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = CalcParser.PowerExprContext(self, CalcParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 30
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 31
                        self.match(CalcParser.T__0)
                        self.state = 32
                        self.expr(11)
                        pass

                    elif la_ == 2:
                        localctx = CalcParser.MulExprContext(self, CalcParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 33
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 34
                        self.match(CalcParser.T__6)
                        self.state = 35
                        self.expr(7)
                        pass

                    elif la_ == 3:
                        localctx = CalcParser.DivExprContext(self, CalcParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 36
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 37
                        self.match(CalcParser.T__7)
                        self.state = 38
                        self.expr(6)
                        pass

                    elif la_ == 4:
                        localctx = CalcParser.AddExprContext(self, CalcParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 39
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 40
                        self.match(CalcParser.T__8)
                        self.state = 41
                        self.expr(5)
                        pass

                    elif la_ == 5:
                        localctx = CalcParser.SubExprContext(self, CalcParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 42
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 43
                        self.match(CalcParser.T__9)
                        self.state = 44
                        self.expr(4)
                        pass

             
                self.state = 49
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
                return self.precpred(self._ctx, 10)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         





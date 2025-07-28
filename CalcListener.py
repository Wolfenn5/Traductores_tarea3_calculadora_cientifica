# Generated from Calc.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CalcParser import CalcParser
else:
    from CalcParser import CalcParser

# This class defines a complete listener for a parse tree produced by CalcParser.
class CalcListener(ParseTreeListener):

    # Enter a parse tree produced by CalcParser#prog.
    def enterProg(self, ctx:CalcParser.ProgContext):
        pass

    # Exit a parse tree produced by CalcParser#prog.
    def exitProg(self, ctx:CalcParser.ProgContext):
        pass


    # Enter a parse tree produced by CalcParser#MulExpr.
    def enterMulExpr(self, ctx:CalcParser.MulExprContext):
        pass

    # Exit a parse tree produced by CalcParser#MulExpr.
    def exitMulExpr(self, ctx:CalcParser.MulExprContext):
        pass


    # Enter a parse tree produced by CalcParser#PowerExpr.
    def enterPowerExpr(self, ctx:CalcParser.PowerExprContext):
        pass

    # Exit a parse tree produced by CalcParser#PowerExpr.
    def exitPowerExpr(self, ctx:CalcParser.PowerExprContext):
        pass


    # Enter a parse tree produced by CalcParser#DivExpr.
    def enterDivExpr(self, ctx:CalcParser.DivExprContext):
        pass

    # Exit a parse tree produced by CalcParser#DivExpr.
    def exitDivExpr(self, ctx:CalcParser.DivExprContext):
        pass


    # Enter a parse tree produced by CalcParser#NumberExpr.
    def enterNumberExpr(self, ctx:CalcParser.NumberExprContext):
        pass

    # Exit a parse tree produced by CalcParser#NumberExpr.
    def exitNumberExpr(self, ctx:CalcParser.NumberExprContext):
        pass


    # Enter a parse tree produced by CalcParser#SubExpr.
    def enterSubExpr(self, ctx:CalcParser.SubExprContext):
        pass

    # Exit a parse tree produced by CalcParser#SubExpr.
    def exitSubExpr(self, ctx:CalcParser.SubExprContext):
        pass


    # Enter a parse tree produced by CalcParser#LogExpr.
    def enterLogExpr(self, ctx:CalcParser.LogExprContext):
        pass

    # Exit a parse tree produced by CalcParser#LogExpr.
    def exitLogExpr(self, ctx:CalcParser.LogExprContext):
        pass


    # Enter a parse tree produced by CalcParser#ParentExpr.
    def enterParentExpr(self, ctx:CalcParser.ParentExprContext):
        pass

    # Exit a parse tree produced by CalcParser#ParentExpr.
    def exitParentExpr(self, ctx:CalcParser.ParentExprContext):
        pass


    # Enter a parse tree produced by CalcParser#AddExpr.
    def enterAddExpr(self, ctx:CalcParser.AddExprContext):
        pass

    # Exit a parse tree produced by CalcParser#AddExpr.
    def exitAddExpr(self, ctx:CalcParser.AddExprContext):
        pass


    # Enter a parse tree produced by CalcParser#SinExpr.
    def enterSinExpr(self, ctx:CalcParser.SinExprContext):
        pass

    # Exit a parse tree produced by CalcParser#SinExpr.
    def exitSinExpr(self, ctx:CalcParser.SinExprContext):
        pass


    # Enter a parse tree produced by CalcParser#CosExpr.
    def enterCosExpr(self, ctx:CalcParser.CosExprContext):
        pass

    # Exit a parse tree produced by CalcParser#CosExpr.
    def exitCosExpr(self, ctx:CalcParser.CosExprContext):
        pass



del CalcParser
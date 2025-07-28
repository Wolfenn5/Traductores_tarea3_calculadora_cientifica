# Generated from Calc.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CalcParser import CalcParser
else:
    from CalcParser import CalcParser

# This class defines a complete generic visitor for a parse tree produced by CalcParser.

class CalcVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CalcParser#prog.
    def visitProg(self, ctx:CalcParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcParser#MulExpr.
    def visitMulExpr(self, ctx:CalcParser.MulExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcParser#PowerExpr.
    def visitPowerExpr(self, ctx:CalcParser.PowerExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcParser#DivExpr.
    def visitDivExpr(self, ctx:CalcParser.DivExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcParser#NumberExpr.
    def visitNumberExpr(self, ctx:CalcParser.NumberExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcParser#SubExpr.
    def visitSubExpr(self, ctx:CalcParser.SubExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcParser#LogExpr.
    def visitLogExpr(self, ctx:CalcParser.LogExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcParser#ParentExpr.
    def visitParentExpr(self, ctx:CalcParser.ParentExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcParser#AddExpr.
    def visitAddExpr(self, ctx:CalcParser.AddExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcParser#SinExpr.
    def visitSinExpr(self, ctx:CalcParser.SinExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcParser#CosExpr.
    def visitCosExpr(self, ctx:CalcParser.CosExprContext):
        return self.visitChildren(ctx)



del CalcParser
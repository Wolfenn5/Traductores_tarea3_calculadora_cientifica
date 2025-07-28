# -------------------- Estructura basica e importacion del parser generado por antlr --------------------
from antlr4 import *
from CalcParser import CalcParser
from CalcVisitor import CalcVisitor
import math # para las funciones matematicas

class MyCalcVisitor(CalcVisitor):
    """
    Visitor personalizado que se obtuvo de CalcVisitor generado por antlr  para evaluar expresiones de la calculadora científica
    Tiene todos los metodos para cada tipo de expresion en la gramatica


    ctx.visit fue generado en la clase base del parser de antlr
       Donde:
       ctx: contiene la informacion sobre la variable encontrada en el arbol del analisis sintactico
       tipos de clases por antlr como      CalcParser.SinExprContext: son generadas automaticamente por antlr que son en si el nodo de una variable
       "continua procesando los hijos de este nodo"
    """




    # -------------------- Implementacion de las funciones matematicas --------------------
    #Visita el nodo raiz del programa (contiene una expresión)
    def visitProg(self, ctx: CalcParser.ProgContext):
        return self.visit(ctx.expr()) # acceder al nodo de expresion hijo (arbol) de forma recursiva con self.visit


    #Maneja expresiones de potencia: expr ^ expr
    def visitPowerExpr(self, ctx: CalcParser.PowerExprContext):
        base = self.visit(ctx.expr(0))  # Evalúa la expresión izquierda
        exponente = self.visit(ctx.expr(1))  # Evalúa la expresión derecha
        return base ** exponente



    #Maneja la función seno: sin(expr)
    def visitSinExpr(self, ctx: CalcParser.SinExprContext):
        valor = self.visit(ctx.expr())  # Evalúa la expresión dentro del seno
        return math.sin(valor)




    #Maneja la función coseno: cos(expr)
    def visitCosExpr(self, ctx: CalcParser.CosExprContext):
        valor = self.visit(ctx.expr())  # Evalúa la expresión dentro del coseno
        return math.cos(valor)




    #Maneja el logaritmo natural: log(expr)
    def visitLogExpr(self, ctx: CalcParser.LogExprContext):
        valor = self.visit(ctx.expr())  # Evalúa la expresión dentro del log
        return math.log(valor)



    #Maneja multiplicaciones: expr * expr
    def visitMulExpr(self, ctx: CalcParser.MulExprContext):
        izquierda = self.visit(ctx.expr(0))  # Evalúa la expresión izquierda
        derecha = self.visit(ctx.expr(1))  # Evalúa la expresión derecha
        return izquierda * derecha



    #Maneja divisiones: expr / expr
    def visitDivExpr(self, ctx: CalcParser.DivExprContext):
        numerador = self.visit(ctx.expr(0))  # Evalúa el numerador
        denominador = self.visit(ctx.expr(1))  # Evalúa el denominador
        return numerador / denominador


    #Maneja sumas: expr + expr
    def visitAddExpr(self, ctx: CalcParser.AddExprContext):
        izquierda = self.visit(ctx.expr(0))  # Evalúa la expresión izquierda
        derecha = self.visit(ctx.expr(1))  # Evalúa la expresión derecha
        return izquierda + derecha # suma


    #Maneja restas: expr - expr
    def visitSubExpr(self, ctx: CalcParser.SubExprContext):
        izquierda = self.visit(ctx.expr(0))  # Evalúa la expresión izquierda
        derecha = self.visit(ctx.expr(1))  # Evalúa la expresión derecha
        return izquierda - derecha



    #Maneja paréntesis (expr), evalua lo que hay dentro de la expresion
    def visitParentExpr(self, ctx: CalcParser.ParentExprContext):
        return self.visit(ctx.expr())



    #Maneja números literales
    def visitNumberExpr(self, ctx: CalcParser.NumberExprContext):
        return float (ctx.NUM().getText())  # Convierte el texto a número flotante, obteniendo el token NUM y con gettext devuelve el texto del token
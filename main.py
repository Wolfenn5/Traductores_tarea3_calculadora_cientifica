# antlr -Dlanguage=Python3 -visitor Calc.g4




from antlr4 import *
from CalcLexer import CalcLexer
from CalcParser import CalcParser
from MyCalcVisitor import MyCalcVisitor

def evaluar_expresion(expresion: str):

    # Crear el flujo de entrada a partir del string
    input_stream = InputStream(expresion) # convierte el string a objeto que antlr lo entienda

    # Crear el lexer y el stream de tokens
    lexer = CalcLexer(input_stream) # divide los tokens  3    +    5
    stream = CommonTokenStream(lexer) # organiza los tokens para que el parser los procese

    # Crear el parser y generar el arbol
    parser = CalcParser(stream)
    arbol = parser.prog()

    # Crear el visitor y visitar el arbol
    visitor = MyCalcVisitor()
    resultado = visitor.visit(arbol)

    return resultado



# main
print("Calculadora Científica (para terminar escribir 'salir' )")

while True: # infinito hasta cerrar
    try:
        entrada = input("Expresion: ").strip() # entrada del usuario
        if entrada.lower() == 'salir': # convertir a minuscula para distincion de mayus y minus
            break

        if not entrada: # si se dan puros enter
            continue

        resultado = evaluar_expresion(entrada)
        print(f"Resultado: {resultado}")

    except Exception as e:
        print(f"Error: {e}")


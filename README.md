# Calculadora Científica con ANTLR4 y Python

Implementación de una calculadora científica que evalúa expresiones matemáticas utilizando ANTLR4 y un Visitor para nodos de un arbol en Python.



## Ejecucion del programa
Se puede iniciar la calculadora mediante el uso de una terminal utilizando el siguiente comando:

    python main.py

## Requerimientos Adicionales
Utilizando el IDE IntelliJ (aunque no absolutamente necesario). Primero se descarga antlr mediante una terminal utilizando el comando 

    brew install antlr

Una vez descargado, tambien es necesario un archivo con extension **.jar** que se puede descargar o en el siguiente enlace:
[Descargar ANTLR](https://www.antlr.org/download.html). El cual contiene las bibliotecas necesarias para generar los archivos del lexer y el parser e indicarlo en intelliJ en ***File -> Project Structure -> Modules -> Dependencies -> JARs or directories***

En este caso se utilizo python en lugar de java y fue necesario instalar el target de python utilizando el siguiente comando en una terminal:

    pip install antlr4-python3-runtime

Para generar el parser y el lexer junto a sus archivos correspondientes de ANTLR se utilizo el siguiente comando

    antlr -Dlanguage=Python3 -visitor Calc.g4




## Características que soporta

- Operaciones básicas: `+`, `-`, `*`, `/`
- Operaciones avanzadas: potencias (`^`), funciones trigonométricas (`sin`, `cos`), logaritmo natural (`log`)
- Uso de paréntesis para agrupar expresiones
- Precedencia de operadores definidas en (`Calc.g4`)

## ¿Cómo funciona?

Se tiene el siguiente flujo de ejecución:

1. **Entrada del usuario**: Se ingresa una expresión (ejemplo: *3 + 5 * sin(0.5)*)
2. **Lexer**: Divide la entrada en tokens (números, operadores, funciones)
3. **Parser**: Construye un árbol sintáctico según la gramática definida en Calc.g4
4. **Visitor**: Recorre el árbol y evalúa cada nodo
5. **Resultado**: Devuelve el valor calculado




## Preguntas Didacticas


### 1. ¿Por qué es útil el patrón Visitor en este contexto?

El patrón Visitor es particularmente útil en esta implementación porque la estructura del arbol sintactico facilitando la lectura de los nodos y estructura del arbol haciendo mas facil la implementacion de cada operación matemática en un método o funcion unico haciendolo modular y si hay que corregir algo, sea mas sencillo que a su vez hace mas facil agregar nuevas operaciones.

### 2. ¿Cómo se maneja la precedencia de operadores?

Mediante la definición en la **gramática** (`Calc.g4`):
   - Las reglas están ordenadas de menor a mayor precedencia
   - ANTLR genera automáticamente el árbol de parsing respetando este orden:
   - ANTLR construye el árbol sintáctico según las reglas de precedencia
   - El Visitor recorre el árbol ya construido con la precedencia correcta

## Jerarquía de precedencia:
La precedencia de operadores se maneja mediante la definición en la gramática (`Calc.g4`). Las operaciones con mayor precedencia están declaradas más abajo en las reglas y ANTLR genera automáticamente el árbol respetando este orden:
```
->  sin
->  cos
->  log
->  ( )
->  ^ 
->  * 
->  / 
->  + 
->  -
```



### 3. ¿Qué cambios se harian para añadir soporte para variables?
Podrian ser los siguientes tanto a la gramatica como al visitador

#### Modificaciones a la gramática (Calc.g4):
```
expr: VARI '=' expr       # AssignExpr
 | VARI                   # VarExpr
 | expr '^' expr          # PowerExpr
 | ... 
```

#### Modificaciones visitor (MyvisitorV2):
```
 class MyCalcVisitor(CalcVisitor):
    def __init__(self):
        self.variables = {}  # Diccionario para almacenar variables
    
    def visitAssignExpr(self, ctx):
        var_name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.variables[var_name] = value
        return value
    
    def visitVarExpr(self, ctx):
        var_name = ctx.ID().getText()
        if var_name not in self.variables:
            raise Exception(f"Variable no definida: {var_name}")
        return self.variables[var_name]
```




### 4. ¿Qué sucede si se ingresa una expresión inválida como sin()?
ANTLR generara un error de sintaxis porque la regla 'sin' espera una expresión entre paréntesis.









## Ejemplos de uso

```plaintext
--> 3 + 5 * 2
Resultado: 13.0

--> sin(0) + cos(0)
Resultado: 1.0

--> 2 ^ 3
Resultado: 8.0

--> (3 + 5) * 2
Resultado: 16.0

--> log(1)
Resultado: 0.0
```

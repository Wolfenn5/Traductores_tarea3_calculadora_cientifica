    grammar Calc;

    prog: expr EOF;

    expr: expr '^' expr          # PowerExpr
        | 'sin' '(' expr ')'     # SinExpr
        | 'cos' '(' expr ')'     # CosExpr
        | 'log' '(' expr ')'     # LogExpr
        | expr '*' expr          # MulExpr
        | expr '/' expr          # DivExpr
        | expr '+' expr          # AddExpr
        | expr '-' expr          # SubExpr
        | '(' expr ')'           # ParentExpr
        | NUM                    # NumberExpr
        ;

    NUM: [0-9]+('.'[0-9]+)?;
    WS: [ \t]+ -> skip;
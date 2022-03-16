grammar marzo;

program : expression*statement*expression*statement* ;
expression: 
    expression '+' expression #suma
    | expression '=' expression #asignacion
    | expression '<' expression #menor
    | expression '>' expression #mayor
    | Letra                 #secundaria
    | Numero                #primaria
    ;

statement:
    'if (' expression ')' statement #ifnoelse
    | 'if (' expression ')' statement 'else' statement #if
    | 'int' Letra  #declaracion
    | 'print(' expression ')' #print
    ;

Numero : [0-9]+;

Letra: [a-zA-Z];

Todo: [a-zA-Z0-9]+;

WS : [ \t\n\r]+ -> skip ;
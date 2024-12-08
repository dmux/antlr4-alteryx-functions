grammar AlteryxFunctions;

// Entrada principal
prog: expr EOF;

// Definição das expressões
expr
    : ifExpr
    | iifExpr
    | switchExpr
    | conversionExpr
    | expr ('==' | '!=' | '<' | '>' | '<=' | '>=') expr
    | 'NOT' expr
    | '(' expr ')'
    | value
    ;

value: STRING
     | NUMBER
     | 'NULL'
     | 'TRUE'
     | 'FALSE';

// Definição do IF...THEN...ELSE...ENDIF
ifExpr: 'IF' condition 'THEN' expr 'ELSE' expr 'ENDIF';

// Definição do IIF
iifExpr: 'IIF' '(' condition ',' expr ',' expr ')';

// Definição do SWITCH
switchExpr: 'SWITCH' '(' expression (',' casePair)* ',' expr ')';

// Par de casos no SWITCH
casePair: expression ',' expr;

// Definição das funções de conversão
conversionExpr: conversionFunction '(' expression ')';

// Funções de conversão
conversionFunction
    : 'TOBOOLEAN'
    | 'TODATE'
    | 'TONUMBER'
    | 'ToNumber'
    | 'TOSTRING'
    | 'ToString'
    ;

// Condições e expressões
condition: expression;
expression: TEXT | NUMBER | BOOLEAN | '(' expr ')' | functionCall;

// Chamada de função genérica
functionCall: conversionExpr;

// Tokens básicos
TEXT: '"' .*? '"';
NUMBER: [0-9]+ ('.' [0-9]+)?;
BOOLEAN: [Tt][Rr][Uu][Ee] | [Ff][Aa][Ll][Ss][Ee]; // Suporte a variações de True/False

// Espaços em branco e comentários ignorados
WS: [ \t\r\n]+ -> skip;


STRING: '"' (ESC | ~["\\])* '"';
fragment ESC: '\\' ["\\/bfnrt] | UNICODE;
fragment UNICODE: 'u' HEX HEX HEX HEX;
fragment HEX: [0-9a-fA-F];

AND : 'AND';
OR  : 'OR';
NOT : 'NOT';
EQ  : '==';
NEQ : '!=';
LT  : '<';
GT  : '>';
LEQ : '<=';
GEQ : '>=';
IN  : 'IN';
NOTIN : 'NOT IN';
NULL : 'NULL';
TRUE : 'TRUE';
FALSE : 'FALSE';

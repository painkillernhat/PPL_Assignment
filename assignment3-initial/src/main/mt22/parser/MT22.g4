grammar MT22;

// Student ID: 2053478

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: program_decl EOF ;
program_decl: program_content program_decl | program_content ;
program_content: vardecl | funcdecl ;

// ----------------------------------------------------------------------------------------------------------------------------------------------------------
// --------------------------------------------------------------------- PHASE 2: RECOGNIZER ----------------------------------------------------------------
// ----------------------------------------------------------------------------------------------------------------------------------------------------------
// --------------------------------------------------------------------- DECLARATIONS -----------------------------------------------------------------------
var_decl_short: idlist COLON (atomic_typ | array_type | AUTO);
var_part: COLON (atomic_typ | AUTO | array_type) ASSIGN;
var_recur: IDENTIFIER var_part init_list | IDENTIFIER COMMA var_recur COMMA init_list;
vardecl: (var_decl_short | var_recur) SEMICOLON; // variable declaration

idlist: IDENTIFIER COMMA idlist | IDENTIFIER ;
init_list: arraylit | exp;

arraylit: LB exp_list RB ;
array_type: ARRAY dimension OF atomic_typ ;
dimension: LS int_list RS;
int_list: INTLIT COMMA int_list | INTLIT ;

paramdecl: INHERIT? OUT? IDENTIFIER COLON (atomic_typ | AUTO | array_type);
funcdecl: IDENTIFIER COLON FUNCTION (atomic_typ | VOID| array_type | AUTO) LP param_list RP (INHERIT IDENTIFIER)? block_stmt;
param_list: param_list_prime | ;
param_list_prime: paramdecl COMMA param_list_prime | paramdecl;

func_call: IDENTIFIER LP exp_list RP ;
			// | readint | printint | readfloat | printfloat | readbool | printbool | readstr | printstr | call_sup | prev_def;


//  operators
relational_op: EQUAL | NOT_EQUAL | LESS_THAN | LESS_EQUAL_THAN | GREATER_THAN | GREATER_EQUAL_THAN ;
logical_op: LOG_AND | LOG_OR ;
adding_op: ADDOP | SUBOP ;
multiplying_op: MULOP | DIVOP | MODOP ;
//intlist: INTLIT COMMA intlist | INTLIT ;
indexop: LS exp_list_prime RS ; // expression-list not nullable
// ----------------------------------------------------------------------------------------------------------------------------------------------------------
// --------------------------------------------------------------------- EXPRESSIONS ------------------------------------------------------------------------
exp_list: exp_list_prime | ;
exp_list_prime: exp COMMA exp_list_prime | exp ;
exp_prime: exp | ;
exp: exp1 SCOPE exp1 | exp1 ;
exp1: exp2 relational_op exp2 | exp2 ;
exp2: exp2 logical_op exp3 | exp3 ;
exp3: exp3 adding_op exp4 | exp4 ;
exp4: exp4 multiplying_op exp5 | exp5 ;
exp5: LOG_NOT exp5 | exp6 ;
exp6: SUBOP exp6 | exp7 ;
exp7: IDENTIFIER indexop | exp8;
exp8: LP exp RP | literal | IDENTIFIER | func_call | arraylit;
// ----------------------------------------------------------------------------------------------------------------------------------------------------------
// --------------------------------------------------------------------- STATEMENTS -------------------------------------------------------------------------
assign_stmt: lhs ASSIGN exp SEMICOLON ;
lhs: IDENTIFIER indexop? ;

if_stmt: IF LP exp RP stmt (ELSE stmt)? ;
for_stmt: FOR LP lhs ASSIGN exp COMMA exp COMMA exp RP stmt ;
while_stmt: WHILE LP exp RP stmt ;
dowhile_stmt: DO block_stmt WHILE LP exp RP SEMICOLON;
break_stmt: BREAK SEMICOLON ;
cont_stmt: CONTINUE SEMICOLON ;
return_stmt: RETURN exp_prime SEMICOLON ;
call_stmt: IDENTIFIER LP exp_list RP SEMICOLON ;
block_stmt: LB stmt_list RB ;
stmt_list: stmt_list_prime | ;
stmt_list_prime: stmt_content stmt_list_prime | stmt_content ;
stmt_content: stmt_list_content | vardecl ;
stmt_list_content: stmt COMMA stmt_list_content | stmt;

stmt: assign_stmt | if_stmt | for_stmt | while_stmt | dowhile_stmt | break_stmt | cont_stmt | call_stmt | block_stmt | return_stmt;
	// | readint | printint | readfloat | printfloat | readbool | printbool | readstr | printstr | call_sup | prev_def;
// ----------------------------------------------------------------------------------------------------------------------------------------------------------
// --------------------------------------------------------------------- SPECIAL FUNCTIONS ------------------------------------------------------------------
// readint: READINT LP RP ;
// printint: PRINTINT LP exp RP ;
// readfloat: READFLOAT LP RP ;
// printfloat: PRINTFLOAT LP exp RP ; // change writeFloat to printFloat
// readbool: READBOOL LP RP ;
// printbool: PRINTBOOL LP exp RP ;
// readstr: READSTR LP RP;
// printstr: PRINTSTR LP exp RP ;
// call_sup: SUPER LP exp_list RP;
// prev_def: PREVENTDEF LP RP ; // printInt(arg: int) ;


WS : [ \t\r\n\b\f]+ -> skip ; // skip spaces, tabs, newlines

// ----------------------------------------------------------------------------------------------------------------------------------------------------------
// --------------------------------------------------------------------- PHASE 1: LEXER ---------------------------------------------------------------------
// ----------------------------------------------------------------------------------------------------------------------------------------------------------
// --------------------------------------------------------------------- CHARACTER SET ----------------------------------------------------------------------
BLANK: ' ' ;
TAB: '\t' ;
BACKSPACE: '\b' ; // \\b
FF: '\f' ; // form feed
CR: '\r' ; // carriage return
NEWLINE: '\n' ;
// ----------------------------------------------------------------------------------------------------------------------------------------------------------
// --------------------------------------------------------------------- PROGRAM COMMENT --------------------------------------------------------------------
COMMENT: ('/*' .*? '*/' | '//' ~[\r\n]*) -> skip;

//UNTERMINATED_COMMENT: '/*' (~[*] | '*' ~[/])* (EOF) {
//	raise UnterminatedComment(self.text)
//};
// ----------------------------------------------------------------------------------------------------------------------------------------------------------
// --------------------------------------------------------------------- KEYWORDS ---------------------------------------------------------------------------
AUTO: 'auto' ;
BREAK: 'break' ;
BOOLEAN: 'boolean' ;
DO: 'do' ;
ELSE: 'else' ;
FALSE: 'false' ;
FLOAT: 'float' ;
FOR: 'for' ;
FUNCTION: 'function' ;
IF: 'if' ;
INTEGER: 'integer' ;
RETURN: 'return' ;
STRING: 'string' ;
TRUE: 'true' ;
VOID: 'void' ;
WHILE: 'while' ;
OUT: 'out' ;
CONTINUE: 'continue' ;
OF: 'of' ;
INHERIT: 'inherit' ;
ARRAY: 'array' ;
// ----------------------------------------------------------------------------------------------------------------------------------------------------------
// --------------------------------------------------------------------- OPERATORS --------------------------------------------------------------------------
ADDOP: '+' ;
SUBOP: '-' ;
MULOP: '*' ;
DIVOP: '/' ;
MODOP: '%' ;
LOG_NOT: '!' ; 
LOG_AND: '&&' ;
LOG_OR: '||' ;
EQUAL: '==' ;
NOT_EQUAL: '!=' ;
LESS_THAN: '<' ;
LESS_EQUAL_THAN: '<=' ;
GREATER_THAN: '>' ;
GREATER_EQUAL_THAN: '>=' ;
SCOPE: '::' ; // scope resolution
// ----------------------------------------------------------------------------------------------------------------------------------------------------------
// --------------------------------------------------------------------- SEPERATORS -------------------------------------------------------------------------
LP: '(' ; // left parentheses
RP: ')' ; // right parentheses
LS: '[' ; // left square
RS: ']' ; // right square
PERIOD: '.' ;
COMMA: ',' ;
SEMICOLON: ';' ;
COLON: ':' ;
LB: '{' ; // left braces
RB: '}' ; // right braces
ASSIGN: '=' ;
// ----------------------------------------------------------------------------------------------------------------------------------------------------------
// --------------------------------------------------------------------- LITERALS ---------------------------------------------------------------------------
fragment INT_PART: [0-9]+ ;
fragment DEC_PART: '.'[0-9]* ;
fragment EXP_PART: [eE] [+-]? INT_PART ;
fragment UNDERSCORE: '_' ;
fragment INTFLOAT: '0' | [1-9] (UNDERSCORE? INT_PART)* ;

INTLIT: INTFLOAT {self.text=self.text.replace("_", "")};
FLOATLIT: DEC_PART EXP_PART
		| INTFLOAT DEC_PART? EXP_PART {self.text=self.text.replace("_", "")}
		| INTFLOAT DEC_PART {self.text=self.text.replace("_", "")};

boolit: TRUE | FALSE ;

fragment ESCAPE_SEQUENCE: '\\' [bfrnt'\\"];
fragment STR_CHAR: (~["\\\n\r'] | ESCAPE_SEQUENCE | '\\"') ;
STRINGLIT: '"' STR_CHAR* '"'  {self.text = self.text[1:-1]} ;
// ----------------------------------------------------------------------------------------------------------------------------------------------------------
// --------------------------------------------------------------------- TYPE SYSTEM AND VALUES -------------------------------------------------------------
atomic_typ: INTEGER | FLOAT | STRING | BOOLEAN ;
literal: INTLIT | FLOATLIT | STRINGLIT | boolit ; 
// ----------------------------------------------------------------------------------------------------------------------------------------------------------
// --------------------------------------------------------------------- SPECIAL FUNCTIONS ------------------------------------------------------------------
// READINT: 'readInteger' ;
// PRINTINT: 'printInteger' ;
// READFLOAT: 'readFloat' ;
// PRINTFLOAT: 'printFloat' ;
// READBOOL: 'readBoolean' ;
// PRINTBOOL: 'printBoolean' ;
// READSTR: 'readString' ;
// PRINTSTR: 'printString' ;
// SUPER: 'super';
// PREVENTDEF: 'preventDefault' ;
// ----------------------------------------------------------------------------------------------------------------------------------------------------------
// --------------------------------------------------------------------- IDENTIFIERS ------------------------------------------------------------------------
IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]* ;
// ----------------------------------------------------------------------------------------------------------------------------------------------------------
// --------------------------------------------------------------------- ERRORS -----------------------------------------------------------------------------
UNCLOSE_STRING: '"' STR_CHAR* ('\n'| EOF | '\r') {
	if self.text[-1] in ['\n', '\r']:
		raise UncloseString(self.text[1:-1])
	else:
		raise UncloseString(self.text[1:])
};

fragment LEGAL_ESCAPE: '\\' ~[bfrnt'\\"] ;
ILLEGAL_ESCAPE: '"' STR_CHAR* LEGAL_ESCAPE {
	raise IllegalEscape(self.text[1:])
};

ERROR_CHAR: .{
	raise ErrorToken(self.text)
};
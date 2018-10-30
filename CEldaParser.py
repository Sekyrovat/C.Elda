import sys
from sly import Parser
from CEldaLexer import CEldaLexer

class CEldaParser(Parser):
	#start = 'tabs'
	#debugfile = 'parser.out'
	tokens = CEldaLexer.tokens

	precedence = (
		('right', NEWLINE),
		('right', ASSIGNMENT),
		('right', TERNARIOPT1, TERNARIOPT2),
		('left', OR),
		('left', AND),
		('left', BIT_OR),
		('left', BIT_XOR),
		('left', BIT_AND),
		('left', EQ_NEQ),
		('left', COMPARADOR),
		('left', BITWISE_SHIFT),
		('left', PLUS, MINUS),
		('left', TIMES, DIV, MOD),
		('right', "+", "-", "!", "~", INCREMENT, DECREMENT), # Unary plus and minus operatord
		('left', POSTINCDEC) # Version postfija de incremento y decremento
	)

	def __init__(self):
		pass

	@_('comentarioInicial bloqueDeclaracionConstantes bloqueDeclaracionGlobales bloqueDeclaracionFunciones MAIN cuerpoFuncion')
	def programa(self, p):
		print("Success!")
		return 0

	@_('comentarioInicialSimple',
	   'comentarioInicialBloque')
	def comentarioInicial(self, p):
		pass

	@_('COMENTARIO_SIMPLE CONTENIDO_COMENTARIO NEWLINE COMENTARIO_SIMPLE comentarioInicialSimple2')
	def comentarioInicialSimple(self, p):
		pass

	@_('CONTENIDO_COMENTARIO NEWLINE COMENTARIO_SIMPLE comentarioInicialSimple2',
	   'NEWLINE COMENTARIO_SIMPLE comentarioInicialSimple2',
	   'MATRICULA newlines')
	def comentarioInicialSimple2(self, p):
		pass

	@_('INICIO_COMENTARIO_BLOQUE contenidoComentarioBloque newlines')
	def comentarioInicialBloque(self, p):
		pass

	@_('CONTENIDO_COMENTARIO contenidoComentarioBloque2')
	def contenidoComentarioBloque(self, p):
		pass
	
	@_('CONTENIDO_COMENTARIO contenidoComentarioBloque2',
	   'MATRICULA contenidoComentarioBloque3')
	def contenidoComentarioBloque2(self, p):
		pass

	@_('CONTENIDO_COMENTARIO contenidoComentarioBloque3',
	   'MATRICULA contenidoComentarioBloque3',
	   'FIN_COMENTARIO_BLOQUE')
	def contenidoComentarioBloque3(self, p):
		pass

	@_('CONST SPACE declaracionConstante ";" newlines bloqueDeclaracionConstantes',
	   'empty')
	def bloqueDeclaracionConstantes(self, p):
		pass

	@_('BOOL SPACE BOCONID ASSIGNMENT A_BOOLEAN',
	   'FLOAT SPACE FLCONID ASSIGNMENT DECIMAL',
	   'INT SPACE INCONID ASSIGNMENT ENTERO',
	   'CHAR SPACE CHCONID ASSIGNMENT A_CHAR',
	   'STRING SPACE STCONID ASSIGNMENT A_STRING')
	def declaracionConstante(self, p):
		pass

	@_('declaracionVariable ";" newlines bloqueDeclaracionGlobales',
	   'empty')
	def bloqueDeclaracionGlobales(self, p):
		pass

	@_('FUNC SPACE tipo SPACE IDFUNCION "(" declaracionArgumentos bloqueDeclaracionFunciones2 bloqueDeclaracionFunciones',
	   'empty')
	def bloqueDeclaracionFunciones(self, p):
		pass

	@_('cuerpoFuncion newlines',
	   '";" newlines')
	def bloqueDeclaracionFunciones2(self, p):
		pass

	@_('VOID',
	   'BOOL',
	   'FLOAT',
	   'INT',
	   'CHAR',
	   'STRING')
	def tipo(self, p):
		pass

	@_('declaracionVariable declaracionArgumentos2',
	   '")"')
	def declaracionArgumentos(self, p):
		pass

	@_('"," SPACE declaracionVariable declaracionArgumentos2',
	   '")"')
	def declaracionArgumentos2(self, p):
		pass

	@_('NEWLINE "{" NEWLINE bloqueDeclaracionVariables statements "}" NEWLINE')
	def cuerpoFuncion(self, p):
		pass

	@_('declaracionVariable ";" newlines bloqueDeclaracionVariables',
	   'empty')
	def bloqueDeclaracionVariables(self, p):
		pass

	@_('declaracionBool',
	   'declaracionFloat',
	   'declaracionInt',
	   'declaracionChar',
	   'declaracionString',
	   'declaracionFila',
	   'declaracionPila')
	def declaracionVariable(self, p):
		pass

	@_('BOOL SPACE declaracionBool2')
	def declaracionBool(self, p):
		pass

	@_('boolSimple',
	   'boolArray',
	   'boolMatriz')
	def declaracionBool2(self, p):
		pass

	@_('BOID')
	def boolSimple(self, p):
		pass

	@_('BOARRID "[" asignacion "]"')
	def boolArray(self, p):
		pass

	@_('BOMATID "[" asignacion "]" "[" asignacion "]"')
	def boolMatriz(self, p):
		pass

	@_('FLOAT SPACE declaracionFloat2')
	def declaracionFloat(self, p):
		pass

	@_('floatSimple',
	   'floatArray',
	   'floatMatriz')
	def declaracionFloat2(self, p):
		pass

	@_('FLID')
	def floatSimple(self, p):
		pass

	@_('FLARRID "[" asignacion "]"')
	def floatArray(self, p):
		pass

	@_('FLMATID "[" asignacion "]" "[" asignacion "]"')
	def floatMatriz(self, p):
		pass

	@_('INT SPACE declaracionInt2')
	def declaracionInt(self, p):
		pass

	@_('intSimple',
	   'intArray',
	   'intMatriz')
	def declaracionInt2(self, p):
		pass

	@_('INID')
	def intSimple(self, p):
		pass

	@_('INARRID "[" asignacion "]"')
	def intArray(self, p):
		pass

	@_('INMATID "[" asignacion "]" "[" asignacion "]"')
	def intMatriz(self, p):
		pass

	@_('CHAR SPACE declaracionChar2')
	def declaracionChar(self, p):
		pass

	@_('charSimple',
	   'charArray',
	   'charMatriz')
	def declaracionChar2(self, p):
		pass

	@_('CHID')
	def charSimple(self, p):
		pass

	@_('CHARRID "[" asignacion "]"')
	def charArray(self, p):
		pass

	@_('CHMATID "[" asignacion "]" "[" asignacion "]"')
	def charMatriz(self, p):
		pass

	@_('STRING SPACE declaracionString2')
	def declaracionString(self, p):
		pass

	@_('stringSimple',
	   'stringArray',
	   'stringMatriz')
	def declaracionString2(self, p):
		pass

	@_('STID')
	def stringSimple(self, p):
		pass

	@_('STARRID "[" asignacion "]"')
	def stringArray(self, p):
		pass

	@_('STMATID "[" asignacion "]" "[" asignacion "]"')
	def stringMatriz(self, p):
		pass

	@_('FILA SPACE declaracionFila2')
	def declaracionFila(self, p):
		pass

	@_('BOOL SPACE FIBOID',
	   'FLOAT SPACE FIFLID',
	   'INT SPACE FIINID',
	   'CHAR SPACE FICHID',
	   'STRING SPACE FISTID')
	def declaracionFila2(self, p):
		pass

	@_('PILA SPACE declaracionPila2')
	def declaracionPila(self, p):
		pass

	@_('BOOL SPACE PIBOID',
	   'FLOAT SPACE PIFLID',
	   'INT SPACE PIINID',
	   'CHAR SPACE PICHID',
	   'STRING SPACE PISTID')
	def declaracionPila2(self, p):
		pass

	@_('tabs statement newlines')
	def statements(self, p):
		pass

	@_('condicionalIf',
	   'condicionalSwitch',
	   'cicloFor',
	   'cicloWhile',
	   'cicloDo ";"',
	   'asignacion ";"',
	   'estatutoReturn ";"',
	   'estatutoContinue ";"',
	   'estatutoBreak ";"')
	def statement(self, p):
		pass

	@_('IF parentesis corchetes condicionalIf2')
	def condicionalIf(self, p):
		pass

	@_('ELSEIF parentesis corchetes condicionalIf2',
	   'ELSE corchetes',
	   'empty')
	def condicionalIf2(self, p):
		pass

	@_('SWITCH parentesis NEWLINE tabs "{" NEWLINE tabs cases "}" newlines')
	def condicionalSwitch(self, p):
		pass

	@_('CASE SPACE literalOConstante ":" NEWLINE statements tabs cases2')
	def cases(self, p):
		pass

	@_('CASE SPACE literalOConstante ":" NEWLINE statements tabs cases2',
	   'CASE SPACE DEFAULT ":" NEWLINE statements tabs')
	def cases2(self, p):
		pass

	@_('literal',
	   'constante')
	def literalOConstante(self, p):
		pass
		
	@_('A_BOOLEAN',
	   'DECIMAL',
	   'ENTERO',
	   'A_CHAR',
	   'A_STRING')
	def literal(self, p):
		pass

	@_('BOCONID',
	   'FLCONID',
	   'INCONID',
	   'CHCONID',
	   'STCONID')
	def constante(self, p):
		pass

	@_('FOR "(" asignacion ";" asignacion ";" asignacion ")" corchetes')
	def cicloFor(self, p):
		pass

	@_('WHILE parentesis corchetes')
	def cicloWhile(self, p):
		pass

	@_('DO corchetes WHILE parentesis')
	def cicloDo(self, p):
		pass

	@_('NEWLINE "{" NEWLINE statements "}" newlines')
	def corchetes(self, p):
		pass

	@_('id ASSIGNMENT asignacion',
	   'ternario')
	def asignacion(self, p):
		pass

	@_('logicOr ternario2')
	def ternario(self, p):
		pass

	@_('TERNARIOPT1 ternario TERNARIOPT2 ternario',
	   'empty')
	def ternario2(self, p):
		pass

	@_('logicAnd logicOr2')
	def logicOr(self, p):
		pass

	@_('OR logicAnd logicOr2',
	   'empty')
	def logicOr2(self, p):
		pass

	@_('bitwiseOr logicAnd2')
	def logicAnd(self, p):
		pass

	@_('AND bitwiseOr logicAnd2',
	   'empty')
	def logicAnd2(self, p):
		pass

	@_('bitwiseXor bitwiseOr2')
	def bitwiseOr(self, p):
		pass

	@_('BIT_OR bitwiseXor bitwiseOr2',
	   'empty')
	def bitwiseOr2(self, p):
		pass

	@_('bitwiseAnd bitwiseXor2')
	def bitwiseXor(self, p):
		pass

	@_('BIT_XOR bitwiseAnd bitwiseXor2',
	   'empty')
	def bitwiseXor2(self, p):
		pass

	@_('eqComparisson bitwiseAnd2')
	def bitwiseAnd(self, p):
		pass

	@_('BIT_AND eqComparisson bitwiseAnd2',
	   'empty')
	def bitwiseAnd2(self, p):
		pass

	@_('comparisson eqComparisson2')
	def eqComparisson(self, p):
		pass

	@_('EQ_NEQ comparisson eqComparisson2',
	   'empty')
	def eqComparisson2(self, p):
		pass

	@_('shift comparisson2')
	def comparisson(self, p):
		pass

	@_('COMPARADOR shift comparisson2',
	   'empty')
	def comparisson2(self, p):
		pass

	@_('exp shift2')
	def shift(self, p):
		pass

	@_('BITWISE_SHIFT exp shift2',
	   'empty')
	def shift2(self, p):
		pass

	@_('termino exp2')
	def exp(self, p):
		pass

	@_('PLUS termino exp2',
	   'MINUS termino exp2',
	   'empty')
	def exp2(self, p):
		pass

	@_('factor termino2')
	def termino(self, p):
		pass

	@_('TIMES factor termino2',
	   'DIV factor termino2',
	   'MOD factor termino2',
	   'empty')
	def termino2(self, p):
		pass

	@_('unidad',
	   '"!" unidad',
	   '"~" unidad',
	   '"+" unidad',
	   '"-" unidad',
	   'INCREMENT unidad',
	   'DECREMENT unidad')
	def factor(self, p):
		pass

	@_('id',
	   'id INCREMENT %prec POSTINCDEC',
	   'id DECREMENT %prec POSTINCDEC',
	   'llamadaFuncion',
	   'parentesis',
	   'literalOConstante')
	def unidad(self, p):
		pass

	@_('"(" asignacion ")"')
	def parentesis(self, p):
		pass

	@_('idSencillo',
	   'idArr',
	   'idMat')
	def id(self, p):
		pass

	@_('BOID',
	   'FLID',
	   'INID',
	   'CHID',
	   'STID')
	def idSencillo(self, p):
		pass

	@_('BOARRID "[" asignacion "]"',
	   'FLARRID "[" asignacion "]"',
	   'INARRID "[" asignacion "]"',
	   'CHARRID "[" asignacion "]"',
	   'STARRID "[" asignacion "]"')
	def idArr(self, p):
		pass

	@_('BOMATID "[" asignacion "]" "[" asignacion "]"',
	   'FLMATID "[" asignacion "]" "[" asignacion "]"',
	   'INMATID "[" asignacion "]" "[" asignacion "]"',
	   'CHMATID "[" asignacion "]" "[" asignacion "]"',
	   'STMATID "[" asignacion "]" "[" asignacion "]"')
	def idMat(self, p):
		pass

	@_('IDFUNCION "(" argumentos',
	   'READ "(" ")"',
	   'WRITE "(" argumentos')
	def llamadaFuncion(self, p):
		pass

	@_('asignacion argumentos2',
	   '")"')
	def argumentos(self, p):
		pass

	@_('"," SPACE asignacion argumentos2',
	   '")"')
	def argumentos2(self, p):
		pass

	@_('RETURN SPACE asignacion')
	def estatutoReturn(self, p):
		pass

	@_('CONTINUE')
	def estatutoContinue(self, p):
		pass

	@_('BREAK')
	def estatutoBreak(self, p):
		pass

	@_('NEWLINE newlines',
	   'NEWLINE')
	def newlines(self, p):
		pass

	@_('TAB tabs2')
	def tabs(self, p):
		pass

	@_('TAB tabs2',
	   'empty')
	def tabs2(self, p):
		pass

	@_('')
	def empty(self, p):
		pass

if __name__ == '__main__':
	lexer = CEldaLexer()
	parser = CEldaParser()

	with open(sys.argv[1], "r") as inputFile:
		data = inputFile.read()
	inputFile.close()
	if data:
		result = parser.parse(lexer.tokenize(data))
		print(result)

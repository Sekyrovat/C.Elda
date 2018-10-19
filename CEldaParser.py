import sys
from sly import Parser
from CEldaLexer import CEldaLexer

class CEldaParser(Parser):
	debugfile = 'parser.out'
	tokens = CEldaLexer.tokens
	tokens = {TAB, SPACE, NEWLINE, ASSIGNMENT, OR, AND, EQ_NEQ, COMPARADOR, BITWISE_SHIFT, INCREMENT, DECREMENT, 
			  BOID, BOCONID, BOARRID, BOMATID, FLID, FLCONID, FLARRID, FLMATID, INID, INCONID, INARRID, INMATID,
			  CHID, CHCONID, CHARRID, CHMATID, STID, STCONID, STARRID, STMATID, FIID, PIID, IDFUNCION, A_BOOLEAN,
			  DECIMAL, ENTERO, A_CHAR, A_STRING, CONST, INT, FLOAT, BOOL, CHAR, STRING, FILA, PILA, MAIN, IF, ELSEIF,
			  ELSE, SWITCH, CASE, DO, WHILE, FOR, RETURN, READ, WRITE, COMENTARIO_SIMPLE, INICIO_COMENTARIO_BLOQUE,
			  CONTENIDO_COMENTARIO, MATRICULA, FIN_COMENTARIO_BLOQUE}

	# precedence = (
	# 	('left', "+", "-"),
	# 	('left', "*", "/", "%"),
	# 	('right', UMINUS) # Unary minus operator
	# )

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

	@_('BOOL SPACE BOCONID SPACE ASSIGNMENT SPACE A_BOOLEAN',
	   'FLOAT SPACE FLCONID SPACE ASSIGNMENT SPACE DECIMAL',
	   'INT SPACE INCONID SPACE ASSIGNMENT SPACE ENTERO',
	   'CHAR SPACE CHCONID SPACE ASSIGNMENT SPACE A_CHAR',
	   'STRING SPACE STCONID SPACE ASSIGNMENT SPACE A_STRING')
	def declaracionConstante(self, p):
		pass

	@_('declaracionVariable ";" newlines bloqueDeclaracionGlobales',
	   'empty')
	def bloqueDeclaracionGlobales(self, p):
		pass

	@_('tipo SPACE IDFUNCION "(" declaracionArgumentos cuerpoFuncion')
	def bloqueDeclaracionFunciones(self, p):
		pass

	@_('declaracionVariable declaracionArgumentos2',
	   '")"')
	def declaracionArgumentos(self, p):
		pass

	@_('"," SPACE declaracionVariable declaracionArgumentos2',
	   '")"')
	def declaracionArgumentos2(self, p):
		pass

	@_('NEWLINE "{" NEWLINE bloqueDeclaracionVariables statements NEWLINE "}" NEWLINE')
	def cuerpoFuncion(self, p):
		pass

	@_('TAB declaracionVariable ";" newlines bloqueDeclaracionVariables',
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

	# @_('BOOL ')
	# def declaracionBool(self, p):
	# 	pass

	@_('id SPACE ASSIGNMENT SPACE asignacion',
	   'ternario')
	def asignacion(self, p):
		pass

	@_('logicOr ternario2')
	def ternario(self, p):
		pass

	@_('SPACE "?" SPACE ternario SPACE ":" SPACE ternario',
	   'empty')
	def ternario2(self):
		pass

	@_('logicAnd logicOr2')
	def logicOr(self, p):
		pass

	@_('SPACE OR SPACE logicAnd logicOr2',
	   'empty')
	def logicOr2(self, p):
		pass

	@_('bitwiseOr logicAnd2')
	def logicAnd(self, p):
		pass

	@_('SPACE AND SPACE bitwiseOr logicAnd2',
	   'empty')
	def logicAnd2(self, p):
		pass

	@_('bitwiseXor bitwiseOr2')
	def bitwiseOr(self, p):
		pass

	@_('SPACE "|" SPACE bitwiseXor bitwiseOr2',
	   'empty')
	def bitwiseOr2(self, p):
		pass

	@_('bitwiseAnd bitwiseXor2')
	def bitwiseXor(self, p):
		pass

	@_('SPACE "^" SPACE bitwiseAnd bitwiseXor2',
	   'empty')
	def bitwiseXor2(self, p):
		pass

	@_('eqComparisson bitwiseAnd2')
	def bitwiseAnd(self, p):
		pass

	@_('SPACE "&" SPACE eqComparisson bitwiseAnd2',
	   'empty')
	def bitwiseAnd2(self, p):
		pass

	@_('comparisson eqComparisson2')
	def eqComparisson(self, p):
		pass

	@_('SPACE EQ_NEQ SPACE comparisson eqComparisson2',
	   'empty')
	def eqComparisson2(self, p):
		pass

	@_('shift comparisson2')
	def comparisson(self, p):
		pass

	@_('SPACE COMPARADOR SPACE shift comparisson2',
	   'empty')
	def comparisson2(self, p):
		pass

	@_('exp shift2')
	def shift(self, p):
		pass

	@_('SPACE BITWISE_SHIFT SPACE exp shift2',
	   'empty')
	def shift2(self, p):
		pass

	@_('logicAnd logicOr2')
	def logicOr(self, p):
		pass

	@_('SPACE OR SPACE logicAnd logicOr2',
	   'empty')
	def logicOr2(self, p):
		pass

	@_('logicAnd logicOr2')
	def logicOr(self, p):
		pass

	@_('SPACE OR SPACE logicAnd logicOr2',
	   'empty')
	def logicOr2(self, p):
		pass

	@_('logicAnd logicOr2')
	def logicOr(self, p):
		pass

	@_('SPACE OR SPACE logicAnd logicOr2',
	   'empty')
	def logicOr2(self, p):
		pass

	@_('logicAnd logicOr2')
	def logicOr(self, p):
		pass

	@_('SPACE OR SPACE logicAnd logicOr2',
	   'empty')
	def logicOr2(self, p):
		pass

	@_('"(" asignacion ")"')
	def parentesis(self, p):
		pass

	@_('TAB tabs',
	   'empty')
	def tabs(self, p):
		pass

	@_('NEWLINE newlines',
	   'empty')
	def newlines(self, p):
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

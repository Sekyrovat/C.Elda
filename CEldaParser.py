#!/usr/bin/python
#
# CEldaParser.py
# Sergio López Madriz A01064725
# Héctor Hernández Morales A00816446

import sys
from sly import Parser
from CEldaLexer import CEldaLexer
from tablas import TablaConstantes, TablaVariables
from cuadruplos import Cuadruplos
import cuboSemantico

class CEldaParser(Parser):
	#start = 'tabs'
	debugfile = 'parser.out'
	tokens = CEldaLexer.tokens

	precedence = (
		('right', NEWLINE),
		#('right', ASSIGNMENT),
		#('right', TERNARIOPT1, TERNARIOPT2),
		# ('left', OR),
		# ('left', AND),
		# ('left', BIT_OR),
		# ('left', BIT_XOR),
		# ('left', BIT_AND),
		# ('left', EQ_NEQ),
		# ('left', COMPARADOR),
		# ('left', BITWISE_SHIFT),
		# ('left', PLUS, MINUS),
		# ('left', TIMES, DIV, MOD),
		('right', "+", "-", "!", "~", INCREMENT, DECREMENT), # Unary plus and minus operatord
		('left', POSTINCDEC) # Version postfija de incremento y decremento
	)

	def __init__(self):
		self.tablaConstantes = TablaConstantes()
		self.tablaVariables = TablaVariables()
		self.cuadruplos = Cuadruplos()
		self.pilaOperandos = []
		self.pilaOperadores = []
		self.contadorCuadruplos = 0
		self.contadorTemporales = 0
		self.dirVariables = 5000

	@_('comentarioInicial bloqueDeclaracionConstantes bloqueDeclaracionGlobales bloqueDeclaracionFunciones MAIN cuerpoFuncion')
	def programa(self, p):
		print("Success!")
		print(self.tablaConstantes)
		print(self.tablaVariables)
		print(self.cuadruplos)
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
		self.tablaConstantes.agregarATabla(p[2], p[0], p[4])

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
		self.tablaVariables.agregarATabla(p.BOID, 'bool', self.dirVariables)
		self.dirVariables += 1

	@_('BOARRID "[" tamano "]"')
	def boolArray(self, p):
		self.tablaVariables.agregarATabla(p.BOARRID, 'bool', self.dirVariables, p.tamano)
		self.dirVariables += p.tamano

	@_('BOMATID "[" tamano "]" "[" tamano "]"')
	def boolMatriz(self, p):
		self.tablaVariables.agregarATabla(p.BOMATID, 'bool', self.dirVariables, p.tamano0, p.tamano1)
		self.dirVariables += p.tamano0 * p.tamano1

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
		self.tablaVariables.agregarATabla(p.FLID, 'float', self.dirVariables)
		self.dirVariables += 1

	@_('FLARRID "[" tamano "]"')
	def floatArray(self, p):
		self.tablaVariables.agregarATabla(p.FLARRID, 'float', self.dirVariables, p.tamano)
		self.dirVariables += p.tamano

	@_('FLMATID "[" tamano "]" "[" tamano "]"')
	def floatMatriz(self, p):
		self.tablaVariables.agregarATabla(p.FLMATID, 'float', self.dirVariables, p.tamano0, p.tamano1)
		self.dirVariables += p.tamano0 * p.tamano1

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
		self.tablaVariables.agregarATabla(p.INID, 'int', self.dirVariables)
		self.dirVariables += 1

	@_('INARRID "[" tamano "]"')
	def intArray(self, p):
		self.tablaVariables.agregarATabla(p.INARRID, 'int', self.dirVariables, p.tamano)
		self.dirVariables += p.tamano

	@_('INMATID "[" tamano "]" "[" tamano "]"')
	def intMatriz(self, p):
		self.tablaVariables.agregarATabla(p.INMATID, 'int', self.dirVariables, p.tamano0, p.tamano1)
		self.dirVariables += p.tamano0 * p.tamano1

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
		self.tablaVariables.agregarATabla(p.CHID, 'char', self.dirVariables)
		self.dirVariables += 1

	@_('CHARRID "[" tamano "]"')
	def charArray(self, p):
		self.tablaVariables.agregarATabla(p.CHARRID, 'char', self.dirVariables, p.tamano)
		self.dirVariables += p.tamano

	@_('CHMATID "[" tamano "]" "[" tamano "]"')
	def charMatriz(self, p):
		self.tablaVariables.agregarATabla(p.CHMATID, 'char', self.dirVariables, p.tamano0, p.tamano1)
		self.dirVariables += p.tamano0 * p.tamano1

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
		self.tablaVariables.agregarATabla(p.STID, 'string', self.dirVariables)
		self.dirVariables += 1

	@_('STARRID "[" tamano "]"')
	def stringArray(self, p):
		self.tablaVariables.agregarATabla(p.STARRID, 'string', self.dirVariables, p.tamano)
		self.dirVariables += p.tamano

	@_('STMATID "[" tamano "]" "[" tamano "]"')
	def stringMatriz(self, p):
		self.tablaVariables.agregarATabla(p.STMATID, 'string', self.dirVariables, p.tamano0, p.tamano1)
		self.dirVariables += p.tamano0 * p.tamano1

	@_('ENTERO',
	   'INCONID')
	def tamano(self, p):
		try:
			return self.tablaConstantes.getValor(p.INCONID)[2]
		except KeyError:
			return p[0]

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

	@_('statements tabs statement newlines',
	   'tabs statement newlines')
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
		return (p[0], 'v')
		
	@_('A_BOOLEAN',
	   'DECIMAL',
	   'ENTERO',
	   'A_CHAR',
	   'A_STRING')
	def literal(self, p):
		return p[0]

	@_('BOCONID',
	   'FLCONID',
	   'INCONID',
	   'CHCONID',
	   'STCONID')
	def constante(self, p):
		return self.tablaConstantes.getValor(p[0])[2]

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
		try:
			self.cuadruplos.generaCuadruplo(p.ASSIGNMENT, p.asignacion, None, p.id)
			self.contadorCuadruplos += 1
		except KeyError:
			return p.ternario

	@_('logicOr TERNARIOPT1 ternario TERNARIOPT2 ternario',
	   'logicOr')
	def ternario(self, p):
		return p[0]

	@_('logicOr OR logicAnd',
	   'logicAnd')
	def logicOr(self, p):
		return p[0]

	@_('logicAnd AND bitwiseOr',
	   'bitwiseOr')
	def logicAnd(self, p):
		return p[0]

	@_('bitwiseOr BIT_OR bitwiseXor',
	   'bitwiseXor')
	def bitwiseOr(self, p):
		return p[0]

	@_('bitwiseXor BIT_XOR bitwiseAnd',
	   'bitwiseAnd')
	def bitwiseXor(self, p):
		return p[0]

	@_('bitwiseAnd BIT_AND eqComparisson',
	   'eqComparisson')
	def bitwiseAnd(self, p):
		return p[0]

	@_('eqComparisson EQ_NEQ comparisson',
	   'comparisson')
	def eqComparisson(self, p):
		return p[0]

	@_('comparisson COMPARADOR shift',
	   'shift')
	def comparisson(self, p):
		return p[0]

	@_('shift BITWISE_SHIFT exp',
	   'exp')
	def shift(self, p):
		return p[0]

	@_('exp PLUS termino',
	   'exp MINUS termino',
	   'termino')
	def exp(self, p):
		if len(p) == 3:
			operandoDerecho = p.exp
			operandoIzquierdo = p.termino
			#tipo = cuboSemantico.verificaSemantica2Operandos('+', operandoIzquierdo[1], operandoDerecho[1])
			#if tipo != 'error':
			resultado = (self.contadorTemporales, 't')
			self.cuadruplos.generaCuadruplo(p[1], operandoIzquierdo, operandoDerecho, resultado)
			self.contadorTemporales += 1
			self.contadorCuadruplos += 1
			return resultado
		return p.termino

	@_('termino SPACE TIMES SPACE factor',
	   'termino SPACE DIV SPACE factor',
	   'termino SPACE MOD SPACE factor',
	   'factor')
	def termino(self, p):
		if len(p) == 5:
			operandoDerecho = p.factor
			operandoIzquierdo = p.termino
			#tipo = cuboSemantico.verificaSemantica2Operandos('+', operandoIzquierdo[1], operandoDerecho[1])
			#if tipo != 'error':
			resultado = (self.contadorTemporales, 't')
			self.cuadruplos.generaCuadruplo(p[2], operandoIzquierdo, operandoDerecho, resultado)
			self.contadorTemporales += 1
			self.contadorCuadruplos += 1
			return resultado
		return p.factor

	@_('unidad',
	   'operacionUnaria')
	def factor(self, p):
		return p[0]

	@_('"!" unidad',
	   '"~" unidad',
	   '"+" unidad',
	   '"-" unidad',
	   'INCREMENT unidad',
	   'DECREMENT unidad')
	def operacionUnaria(self, p):
		return p[1]

	@_('id',
	   'id INCREMENT %prec POSTINCDEC',
	   'id DECREMENT %prec POSTINCDEC',
	   'llamadaFuncion',
	   'parentesis',
	   'literalOConstante')
	def unidad(self, p):
		self.pilaOperandos.append(p[0])
		return p[0]

	@_('"(" asignacion ")"')
	def parentesis(self, p):
		return p.asignacion

	@_('idSencillo',
	   'idArr',
	   'idMat')
	def id(self, p):
		return (p[0], 'd')

	@_('BOID',
	   'FLID',
	   'INID',
	   'CHID',
	   'STID')
	def idSencillo(self, p):
		return self.tablaVariables.conseguirDireccion(p[0])

	@_('BOARRID "[" asignacion "]"',
	   'FLARRID "[" asignacion "]"',
	   'INARRID "[" asignacion "]"',
	   'CHARRID "[" asignacion "]"',
	   'STARRID "[" asignacion "]"')
	def idArr(self, p):
		return self.tablaVariables.conseguirDireccion(p[0], p.asignacion[0])

	@_('BOMATID "[" asignacion "]" "[" asignacion "]"',
	   'FLMATID "[" asignacion "]" "[" asignacion "]"',
	   'INMATID "[" asignacion "]" "[" asignacion "]"',
	   'CHMATID "[" asignacion "]" "[" asignacion "]"',
	   'STMATID "[" asignacion "]" "[" asignacion "]"')
	def idMat(self, p):
		return self.tablaVariables.conseguirDireccion(p[0], p.asignacion0[0], p.asignacion1[0])

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

	@_('tabs TAB',
	   'TAB')
	def tabs(self, p):
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

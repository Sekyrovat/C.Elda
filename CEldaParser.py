#!/usr/bin/python3.7
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
		('right', MNEWLINES),
		('right', NEWLINE),
		# ('right', ASSIGNMENT),
		# ('right', TERNARIOPT1, TERNARIOPT2),
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
		self.pilaSaltosPendientes = []
		self.pilaAuxTernario = []
		self.contadorCuadruplos = 0
		self.contadorTemporales = 0
		self.dirVariables = 5000

	@_('comentarioInicial bloqueDeclaracionConstantes bloqueDeclaracionGlobales bloqueDeclaracionFunciones MAIN cuerpoFuncion',
	   'comentarioInicial bloqueDeclaracionConstantes bloqueDeclaracionGlobales                            MAIN cuerpoFuncion',
	   'comentarioInicial bloqueDeclaracionConstantes                           bloqueDeclaracionFunciones MAIN cuerpoFuncion',
	   'comentarioInicial bloqueDeclaracionConstantes                                                      MAIN cuerpoFuncion',
	   'comentarioInicial                             bloqueDeclaracionGlobales bloqueDeclaracionFunciones MAIN cuerpoFuncion',
	   'comentarioInicial                             bloqueDeclaracionGlobales                            MAIN cuerpoFuncion',
	   'comentarioInicial                                                       bloqueDeclaracionFunciones MAIN cuerpoFuncion',
	   'comentarioInicial                                                                                  MAIN cuerpoFuncion')
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

	@_('COMENTARIO_SIMPLE CONTENIDO_COMENTARIO NEWLINE comentarioInicialSimple',
	   'COMENTARIO_SIMPLE NEWLINE comentarioInicialSimple',
	   'COMENTARIO_SIMPLE MATRICULA newlines')
	def comentarioInicialSimple(self, p):
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

	@_('bloqueDeclaracionConstantes CONST SPACE declaracionConstante ";" newlines',
	   'CONST SPACE declaracionConstante ";" newlines')
	def bloqueDeclaracionConstantes(self, p):
		pass

	@_('BOOL SPACE BOCONID ASSIGNMENT A_BOOLEAN',
	   'FLOAT SPACE FLCONID ASSIGNMENT DECIMAL',
	   'INT SPACE INCONID ASSIGNMENT ENTERO',
	   'CHAR SPACE CHCONID ASSIGNMENT A_CHAR',
	   'STRING SPACE STCONID ASSIGNMENT A_STRING')
	def declaracionConstante(self, p):
		self.tablaConstantes.agregarATabla(p[2], p[0], p[4])

	@_('bloqueDeclaracionGlobales declaracionVariable ";" newlines',
	   'declaracionVariable ";" newlines')
	def bloqueDeclaracionGlobales(self, p):
		pass

	@_('bloqueDeclaracionFunciones declaracionFuncion',
	   'declaracionFuncion')
	def bloqueDeclaracionFunciones(self, p):
		pass

	@_('FUNC SPACE tipo SPACE IDFUNCION "(" declaracionArgumentos cuerpoFuncion newlines',
	   'FUNC SPACE tipo SPACE IDFUNCION "(" declaracionArgumentos ";" newlines')
	def declaracionFuncion(self, p):
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

	@_('NEWLINE "{" newlines bloqueDeclaracionVariables statements "}" NEWLINE',
	   'NEWLINE "{" newlines statements "}" NEWLINE')
	def cuerpoFuncion(self, p):
		pass

	@_('bloqueDeclaracionVariables tabs declaracionVariable ";" newlines',
	   'tabs declaracionVariable ";" newlines')
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

	@_('ENTERO')
	def tamano(self, p):
		return p.ENTERO

	@_('INCONID')
	def tamano(self, p):
		return self.tablaConstantes.getValor(p.INCONID)

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

	@_('condicionIf corchetes SPACE elseif SPACE condicionalIf')
	def condicionalIf(self, p):
		pass

	@_('condicionIf corchetes SPACE elseFinal corchetes',
	   'condicionIf corchetes')
	def condicionalIf(self, p):
		saltoPendiente = self.pilaSaltosPendientes.pop()
		self.cuadruplos.rellena(saltoPendiente, self.contadorCuadruplos)

	@_('IF SPACE parentesis')
	def condicionIf(self, p):
		self.pilaSaltosPendientes.append(self.contadorCuadruplos)
		self.cuadruplos.generaCuadruplo('GoToF', p.parentesis, None, -1)
		self.contadorCuadruplos += 1

	@_('ELSE')
	def elseif(self, p):
		saltoPendiente = self.pilaSaltosPendientes.pop()
		self.cuadruplos.rellena(saltoPendiente, self.contadorCuadruplos)

	@_('ELSE')
	def elseFinal(self, p):
		saltoPendiente = self.pilaSaltosPendientes.pop()
		self.pilaSaltosPendientes.append(self.contadorCuadruplos)
		self.cuadruplos.generaCuadruplo('GoTo', None, None, -1)
		self.contadorCuadruplos += 1
		self.cuadruplos.rellena(saltoPendiente, self.contadorCuadruplos)

	@_('SWITCH SPACE parentesis NEWLINE tabs "{" NEWLINE cases tabs "}"')
	def condicionalSwitch(self, p):
		pass

	@_('tabs CASE SPACE literalOConstante ":" NEWLINE statements cases',
	   'tabs DEFAULT ":" NEWLINE statements')
	def cases(self, p):
		pass

	@_('literal',
	   'constante')
	def literalOConstante(self, p):
		return ('v',) + p[0]
		
	@_('A_BOOLEAN')
	def literal(self, p):
		return (p.A_BOOLEAN, 'bool')

	@_('DECIMAL')
	def literal(self, p):
		return (p.DECIMAL, 'float')

	@_('ENTERO')
	def literal(self, p):
		return (p.ENTERO, 'int')

	@_('A_CHAR')
	def literal(self, p):
		return (p.A_CHAR, 'char')

	@_('A_STRING')
	def literal(self, p):
		return (p.A_STRING, 'string')

	@_('BOCONID')
	def constante(self, p):
		return (self.tablaConstantes.getValor(p.BOCONID), 'bool')

	@_('FLCONID')
	def constante(self, p):
		return (self.tablaConstantes.getValor(p.FLCONID), 'float')

	@_('INCONID')
	def constante(self, p):
		return (self.tablaConstantes.getValor(p.INCONID), 'int')

	@_('CHCONID')
	def constante(self, p):
		return (self.tablaConstantes.getValor(p.CHCONID), 'char')

	@_('STCONID')
	def constante(self, p):
		return (self.tablaConstantes.getValor(p.STCONID), 'string')

	@_('FOR "(" asignacion ";" asignacion ";" asignacion ")" corchetes')
	def cicloFor(self, p):
		pass

	@_('WHILE parentesis corchetes')
	def cicloWhile(self, p):
		pass

	@_('DO corchetes SPACE WHILE parentesis')
	def cicloDo(self, p):
		pass

	@_('NEWLINE tabs "{" newlines statements tabs "}"')
	def corchetes(self, p):
		pass

	@_('id ASSIGNMENT asignacion')
	def asignacion(self, p):
		self.cuadruplos.generaCuadruplo(p.ASSIGNMENT, p.asignacion, None, p.id)
		self.contadorCuadruplos += 1
		return p.id

	@_('ternario')
	def asignacion(self, p):
		return p.ternario

	@_('condicionYOpTernario1 ternarioYOpTernario2 ternario')
	def ternario(self, p):
		tipo = cuboSemantico.verificaSemanticaTernario(p.ternarioYOpTernario2[2], p.ternario[2])
		if tipo == 'error':
			print('Error: type mismatch in line:', p.lineno, 'with ternary operator')
		direccionFinTernario1 = self.pilaAuxTernario.pop()
		resultado = self.pilaAuxTernario.pop()[0:2] + (tipo,)
		self.cuadruplos.rellena(direccionFinTernario1, resultado)
		saltoPendiente = self.pilaSaltosPendientes.pop()
		self.cuadruplos.generaCuadruplo('=', p.ternario, None, resultado)
		self.contadorCuadruplos += 1
		self.cuadruplos.rellena(saltoPendiente, self.contadorCuadruplos)
		return resultado

	@_('logicOr')
	def ternario(self, p):
		return p.logicOr

	@_('logicOr TERNARIOPT1')
	def condicionYOpTernario1(self, p):
		if p.logicOr[2] == 'string':
			print('Error: type mismatch in line:', p.lineno, 'ternary operators can\'t choose based on a string')
		self.pilaAuxTernario.append(('t', self.contadorTemporales, 'pendiente'))
		self.pilaSaltosPendientes.append(self.contadorCuadruplos)
		self.cuadruplos.generaCuadruplo('GoToF', p.logicOr, None, -1)
		self.contadorTemporales += 1
		self.contadorCuadruplos += 1
		return p.logicOr

	@_('ternario TERNARIOPT2')
	def ternarioYOpTernario2(self, p):
		resultado = self.pilaAuxTernario[-1]
		saltoPendiente = self.pilaSaltosPendientes.pop()
		self.pilaAuxTernario.append(self.contadorCuadruplos)
		self.cuadruplos.generaCuadruplo('=', p.ternario, None, resultado)
		self.contadorCuadruplos += 1
		self.pilaSaltosPendientes.append(self.contadorCuadruplos)
		self.cuadruplos.generaCuadruplo('GoTo', None, None, -1)
		self.contadorCuadruplos += 1
		self.cuadruplos.rellena(saltoPendiente, self.contadorCuadruplos)
		return p.ternario

	@_('logicOr OR logicAnd')
	def logicOr(self, p):
		operandoIzq = p.logicOr
		operandoDer = p.logicAnd
		tipo = cuboSemantico.verificaSemantica2Operandos(p.OR, operandoIzq[2], operandoDer[2])
		if tipo == 'error':
			print('Error: type mismatch in line:', p.lineno, 'with operator ', p.OR)
		resultado = ('t', self.contadorTemporales, tipo)
		self.cuadruplos.generaCuadruplo(p.OR, operandoIzq, operandoDer, resultado)
		self.contadorTemporales += 1
		self.contadorCuadruplos += 1
		return resultado

	@_('logicAnd')
	def logicOr(self, p):
		return p.logicAnd

	@_('logicAnd AND bitwiseOr')
	def logicAnd(self, p):
		operandoIzq = p.logicAnd
		operandoDer = p.bitwiseOr
		tipo = cuboSemantico.verificaSemantica2Operandos(p.AND, operandoIzq[2], operandoDer[2])
		if tipo == 'error':
			print('Error: type mismatch in line:', p.lineno, 'with operator ', p.AND)
		resultado = ('t', self.contadorTemporales, tipo)
		self.cuadruplos.generaCuadruplo(p.AND, operandoIzq, operandoDer, resultado)
		self.contadorTemporales += 1
		self.contadorCuadruplos += 1
		return resultado

	@_('bitwiseOr')
	def logicAnd(self, p):
		return p.bitwiseOr

	@_('bitwiseOr BIT_OR bitwiseXor')
	def bitwiseOr(self, p):
		operandoIzq = p.bitwiseOr
		operandoDer = p.bitwiseXor
		tipo = cuboSemantico.verificaSemantica2Operandos(p.BIT_OR, operandoIzq[2], operandoDer[2])
		if tipo == 'error':
			print('Error: type mismatch in line:', p.lineno, 'with operator ', p.BIT_OR)
		resultado = ('t', self.contadorTemporales, tipo)
		self.cuadruplos.generaCuadruplo(p.BIT_OR, operandoIzq, operandoDer, resultado)
		self.contadorTemporales += 1
		self.contadorCuadruplos += 1
		return resultado

	@_('bitwiseXor')
	def bitwiseOr(self, p):
		return p.bitwiseXor

	@_('bitwiseXor BIT_XOR bitwiseAnd')
	def bitwiseXor(self, p):
		operandoIzq = p.bitwiseXor
		operandoDer = p.bitwiseAnd
		tipo = cuboSemantico.verificaSemantica2Operandos(p.BIT_XOR, operandoIzq[2], operandoDer[2])
		if tipo == 'error':
			print('Error: type mismatch in line:', p.lineno, 'with operator ', p.BIT_XOR)
		resultado = ('t', self.contadorTemporales, tipo)
		self.cuadruplos.generaCuadruplo(p.BIT_XOR, operandoIzq, operandoDer, resultado)
		self.contadorTemporales += 1
		self.contadorCuadruplos += 1
		return resultado

	@_('bitwiseAnd')
	def bitwiseXor(self, p):
		return p.bitwiseAnd

	@_('bitwiseAnd BIT_AND eqComparisson')
	def bitwiseAnd(self, p):
		operandoIzq = p.bitwiseAnd
		operandoDer = p.eqComparisson
		tipo = cuboSemantico.verificaSemantica2Operandos(p.BIT_AND, operandoIzq[2], operandoDer[2])
		if tipo == 'error':
			print('Error: type mismatch in line:', p.lineno, 'with operator ', p.BIT_AND)
		resultado = ('t', self.contadorTemporales, tipo)
		self.cuadruplos.generaCuadruplo(p.BIT_AND, operandoIzq, operandoDer, resultado)
		self.contadorTemporales += 1
		self.contadorCuadruplos += 1
		return resultado

	@_('eqComparisson')
	def bitwiseAnd(self, p):
		return p.eqComparisson

	@_('eqComparisson EQ_NEQ comparisson')
	def eqComparisson(self, p):
		operandoIzq = p.eqComparisson
		operandoDer = p.comparisson
		tipo = cuboSemantico.verificaSemantica2Operandos(p.EQ_NEQ, operandoIzq[2], operandoDer[2])
		if tipo == 'error':
			print('Error: type mismatch in line:', p.lineno, 'with operator ', p.EQ_NEQ)
		resultado = ('t', self.contadorTemporales, tipo)
		self.cuadruplos.generaCuadruplo(p.EQ_NEQ, operandoIzq, operandoDer, resultado)
		self.contadorTemporales += 1
		self.contadorCuadruplos += 1
		return resultado

	@_('comparisson')
	def eqComparisson(self, p):
		return p.comparisson

	@_('comparisson COMPARADOR shift')
	def comparisson(self, p):
		operandoIzq = p.comparisson
		operandoDer = p.shift
		tipo = cuboSemantico.verificaSemantica2Operandos(p.COMPARADOR, operandoIzq[2], operandoDer[2])
		if tipo == 'error':
			print('Error: type mismatch in line:', p.lineno, 'with operator ', p.COMPARADOR)
		resultado = ('t', self.contadorTemporales, tipo)
		self.cuadruplos.generaCuadruplo(p.COMPARADOR, operandoIzq, operandoDer, resultado)
		self.contadorTemporales += 1
		self.contadorCuadruplos += 1
		return resultado

	@_('shift')
	def comparisson(self, p):
		return p.shift

	@_('shift BITWISE_SHIFT exp')
	def shift(self, p):
		operandoIzq = p.shift
		operandoDer = p.exp
		tipo = cuboSemantico.verificaSemantica2Operandos(p.BITWISE_SHIFT, operandoIzq[2], operandoDer[2])
		if tipo == 'error':
			print('Error: type mismatch in line:', p.lineno, 'with operator ', p.BITWISE_SHIFT)
		resultado = ('t', self.contadorTemporales, tipo)
		self.cuadruplos.generaCuadruplo(p.BITWISE_SHIFT, operandoIzq, operandoDer, resultado)
		self.contadorTemporales += 1
		self.contadorCuadruplos += 1
		return resultado

	@_('exp')
	def shift(self, p):
		return p.exp

	@_('exp PLUS termino',
	   'exp MINUS termino')
	def exp(self, p):
		operandoIzq = p.exp
		operandoDer = p.termino
		tipo = cuboSemantico.verificaSemantica2Operandos(p[1], operandoIzq[2], operandoDer[2])
		if tipo != 'error':
			resultado = ('t', self.contadorTemporales, tipo)
			self.cuadruplos.generaCuadruplo(p[1], operandoIzq, operandoDer, resultado)
			self.contadorTemporales += 1
			self.contadorCuadruplos += 1
			return resultado

	@_('termino')
	def exp(self, p):
		return p.termino

	@_('termino TIMES factor',
	   'termino DIV factor',
	   'termino MOD factor')
	def termino(self, p):
		operandoIzq = p.termino
		operandoDer = p.factor
		tipo = cuboSemantico.verificaSemantica2Operandos(p[1], operandoIzq[2], operandoDer[2])
		if tipo != 'error':
			resultado = ('t', self.contadorTemporales, tipo)
			self.cuadruplos.generaCuadruplo(p[1], operandoIzq, operandoDer, resultado)
			self.contadorTemporales += 1
			self.contadorCuadruplos += 1
			return resultado

	@_('factor')
	def termino(self, p):
		return p.factor

	@_('unidad',
	   '"+" unidad')
	def factor(self, p):
		if len(p) == 2:
			#mandar mensaje + unario innecesario
			pass
		return p.unidad

	@_('INCREMENT unidad',
	   'DECREMENT unidad')
	def factor(self, p):
		self.cuadruplos.generaCuadruplo(p[0][0], p.unidad, ('v', 1, 'int'), p.unidad)
		self.contadorCuadruplos += 1
		return p[1]

	@_('"!" unidad',
	   '"~" unidad',
	   '"-" unidad')
	def factor(self, p):
		tipo = cuboSemantico.verificaSemantica1Operando(p[0], p.unidad[2])
		if tipo != 'error':
			resultado = ('t', self.contadorTemporales, tipo)
			self.cuadruplos.generaCuadruplo(p[0], p.unidad, None, resultado)
			self.contadorTemporales += 1
			self.contadorCuadruplos += 1
			return resultado

	@_('id',
	   'llamadaFuncion',
	   'parentesis',
	   'literalOConstante')
	def unidad(self, p):
		return p[0]

	@_('id INCREMENT %prec POSTINCDEC',
	   'id DECREMENT %prec POSTINCDEC')
	def unidad(self, p):
		# logica para incremento post
		return p[0]

	@_('"(" asignacion ")"')
	def parentesis(self, p):
		return p.asignacion

	@_('idSencillo',
	   'idArr',
	   'idMat')
	def id(self, p):
		return ('d',) + p[0]

	@_('BOID')
	def idSencillo(self, p):
		return (self.tablaVariables.conseguirDireccion(p.BOID), 'bool')

	@_('FLID')
	def idSencillo(self, p):
		return (self.tablaVariables.conseguirDireccion(p.FLID), 'float')

	@_('INID')
	def idSencillo(self, p):
		return (self.tablaVariables.conseguirDireccion(p.INID), 'int')

	@_('CHID')
	def idSencillo(self, p):
		return (self.tablaVariables.conseguirDireccion(p.CHID), 'char')

	@_('STID')
	def idSencillo(self, p):
		return (self.tablaVariables.conseguirDireccion(p.STID), 'string')

	@_('BOARRID "[" asignacion "]"')
	def idArr(self, p):
		return (self.tablaVariables.conseguirDireccion(p.BOARRID, p.asignacion[1]), 'bool')

	@_('FLARRID "[" asignacion "]"')
	def idArr(self, p):
		return (self.tablaVariables.conseguirDireccion(p.FLARRID, p.asignacion[1]), 'float')

	@_('INARRID "[" asignacion "]"')
	def idArr(self, p):
		return (self.tablaVariables.conseguirDireccion(p.INARRID, p.asignacion[1]), 'int')

	@_('CHARRID "[" asignacion "]"')
	def idArr(self, p):
		return (self.tablaVariables.conseguirDireccion(p.CHARRID, p.asignacion[1]), 'char')

	@_('STARRID "[" asignacion "]"')
	def idArr(self, p):
		return (self.tablaVariables.conseguirDireccion(p.STARRID, p.asignacion[1]), 'string')

	@_('BOMATID "[" asignacion "]" "[" asignacion "]"')
	def idMat(self, p):
		return (self.tablaVariables.conseguirDireccion(p.BOMATID, p.asignacion0[1], p.asignacion1[1]), 'bool')

	@_('FLMATID "[" asignacion "]" "[" asignacion "]"')
	def idMat(self, p):
		return (self.tablaVariables.conseguirDireccion(p.FLMATID, p.asignacion0[1], p.asignacion1[1]), 'float')

	@_('INMATID "[" asignacion "]" "[" asignacion "]"')
	def idMat(self, p):
		return (self.tablaVariables.conseguirDireccion(p.INMATID, p.asignacion0[1], p.asignacion1[1]), 'int')

	@_('CHMATID "[" asignacion "]" "[" asignacion "]"')
	def idMat(self, p):
		return (self.tablaVariables.conseguirDireccion(p.CHMATID, p.asignacion0[1], p.asignacion1[1]), 'char')

	@_('STMATID "[" asignacion "]" "[" asignacion "]"')
	def idMat(self, p):
		return (self.tablaVariables.conseguirDireccion(p.STMATID, p.asignacion0[1], p.asignacion1[1]), 'string')

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

	@_('NEWLINE newlines %prec MNEWLINES',
	   'NEWLINE %prec MNEWLINES')
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

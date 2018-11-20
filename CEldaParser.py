#!/usr/bin/python3.7
#
# CEldaParser.py
# Sergio López Madriz A01064725
# Héctor Hernández Morales A00816446

import sys
from sly import Parser
from CEldaLexer import CEldaLexer
from tablas import TablaConstantes, TablaVariables, TablaModulos
from cuadruplos import Cuadruplos
import cuboSemantico

class CEldaParser(Parser):
	#start = 'tabs'
	#debugfile = 'parser.out'
	tokens = CEldaLexer.tokens

	# Declaramos la asociacion de algunos operadores.
	precedence = (
		('right', MNEWLINES),
		('left', NEWLINE),
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

	# Funcion para inicializar algunos de los valores que se usaran a lo largo del programa.
	def __init__(self):
		self.tablaConstantes = TablaConstantes()
		self.tablaVariablesGlobales = TablaVariables()
		self.tablaVariablesActual = None
		self.tablaModulos = TablaModulos()
		self.cuadruplos = Cuadruplos()
		self.pilaSaltosPendientes = []
		self.pilaAuxTernario = []
		self.pilaAuxSwitch = []
		self.pilaAuxContinue = []
		self.pilaAuxContinueFor = []
		self.pilaAuxContinueWhile = []
		self.pilaAuxContinueDo = []
		self.pilaAuxBreak = []
		self.pilaAuxPost = []
		self.contadorCuadruplos = 0
		self.contadorTemporales = 0
		self.nivelDeEspera = 0
		self.dirVariables = 0
		self.finVariablesGlobales = 0
		self.numeroParametro = 0
		self.contadorLlamadas = 0

	'''
		El uso de niveles de espera es para el uso de fors y ciclos, ya que esto permite su
		manejo de forma adecuada y sencilla.
	'''
	# Aumentamos el nivel de espera presente.
	def agregaCapaEspera(self):
		self.cuadruplos.agregaCapaEspera()
		self.nivelDeEspera += 1

	# Liberamos el nivel de espera.
	def liberaEspera(self):
		self.contadorCuadruplos += self.cuadruplos.liberaEspera()
		self.nivelDeEspera -= 1

	# Funcion usada para generar el cuadruplo, en base a las indicacions que se le den.
	def generaCuadruplo(self, operacion, operando1, operando2, resultado):
		if self.nivelDeEspera:
			self.cuadruplos.generaEnEspera(operacion, operando1, operando2, resultado)
		else:
			self.cuadruplos.generaCuadruplo(operacion, operando1, operando2, resultado)
			self.contadorCuadruplos += 1

	# Funcion usada para eliminar el ultimo cuadruplo generado, utilizada especificamente para el caso default del switch
	def popCuadruplo(self):
		if self.nivelDeEspera:
			self.cuadruplos.enEspera[-1].pop()
		else:
			self.cuadruplos.cuadruplos.pop()
			self.contadorCuadruplos -= 1

	# Esta funcion es para generar las temporales que se requiera de la operacion.
	def generaTemporal(self, tipo):
		resultado = ('t', self.contadorTemporales, tipo)
		self.contadorTemporales += 1
		return resultado

	def agregaVariable(self, nombre, tipo, *dimensiones):
		if self.tablaVariablesActual is None:
			self.tablaVariablesGlobales.agregarATabla(nombre, tipo, self.dirVariables, dimensiones)
		elif self.tablaVariablesActual != -1:
			self.tablaVariablesActual.agregarATabla(nombre, tipo, self.dirVariables, dimensiones)

	def consigueVariable(self, nombre):
		if self.tablaVariablesActual.variableExiste(nombre):
			return self.tablaVariablesActual.tablaVariables[nombre]
		elif self.tablaVariablesGlobales.variableExiste(nombre):
			return self.tablaVariablesGlobales.tablaVariables[nombre]
		else:
			print ('variable no definida', nombre)
			sys.exit(1)

	def consigueDirVariable(self, nombre): # dims parche temporal
		if self.tablaVariablesActual.variableExiste(nombre):
			return self.tablaVariablesActual.conseguirDireccion(nombre)
		elif self.tablaVariablesGlobales.variableExiste(nombre):
			return self.tablaVariablesGlobales.conseguirDireccion(nombre)
		else:
			print ('variable no definida', nombre)
			sys.exit(1)

	def generaAccesoArreglo(self, tipo):
		resultado = ('(t)', self.contadorTemporales, tipo)
		self.contadorTemporales += 1
		return resultado

	##################################################################
	##################################################################
	################ Comienzan las reglas de sintaxis ################
	##################################################################
	##################################################################
	
	# Funcion con la regla para la estructura general del programa.
	@_('comentarioInicial bloqueDeclaracionConstantes declaracionesGlobales bloqueDeclaracionFunciones inicializaMain cuerpoFuncion',
	   'comentarioInicial bloqueDeclaracionConstantes declaracionesGlobales                            inicializaMain cuerpoFuncion',
	   'comentarioInicial bloqueDeclaracionConstantes                       bloqueDeclaracionFunciones inicializaMain cuerpoFuncion',
	   'comentarioInicial bloqueDeclaracionConstantes                                                  inicializaMain cuerpoFuncion',
	   'comentarioInicial                             declaracionesGlobales bloqueDeclaracionFunciones inicializaMain cuerpoFuncion',
	   'comentarioInicial                             declaracionesGlobales                            inicializaMain cuerpoFuncion',
	   'comentarioInicial                                                   bloqueDeclaracionFunciones inicializaMain cuerpoFuncion',
	   'comentarioInicial                                                                              inicializaMain cuerpoFuncion')
	def programa(self, p):
		self.tablaModulos.agregarTamanosMemoria('main', self.dirVariables - self.finVariablesGlobales, self.contadorTemporales)
		self.generaCuadruplo('EXIT', None, None, None)
		print()
		print('Tabla de Constantes')
		print(self.tablaConstantes)
		print()
		print('Tabla de Variables Globales')
		print(self.tablaVariablesGlobales)
		print()
		print('Tabla de Modulos')
		print(self.tablaModulos)
		print()
		print(self.finVariablesGlobales)
		print(self.tablaModulos.creaReduccion())
		print()
		print('Cuadruplos')
		print(self.cuadruplos)
		print()
		salida = {}
		salida['frontera'] = self.finVariablesGlobales
		salida['funciones'] = self.tablaModulos.creaReduccion()
		salida['cuadruplos'] = self.cuadruplos.cuadruplos
		return salida

	'''
		Funcion con la regla para el procesamiento del comentario inicial, estaregla se usa para 
		distinguir entre comentarios sencillos y comentarios de tipo bloque
	'''
	@_('comentarioInicialSimple',
	   'comentarioInicialBloque')
	def comentarioInicial(self, p):
		self.generaCuadruplo('GoTo', None, None, -1)

	# Funcion con la regla encargada del manejo de comentario simple. Debe recibir la matricula.
	@_('COMENTARIO_SIMPLE CONTENIDO_COMENTARIO NEWLINE comentarioInicialSimple',
	   'COMENTARIO_SIMPLE NEWLINE comentarioInicialSimple',
	   'COMENTARIO_SIMPLE MATRICULA newlines')
	def comentarioInicialSimple(self, p):
		pass

	# Funcion con la regla para el manejo del comentario de bloque.
	@_('INICIO_COMENTARIO_BLOQUE contenidoComentarioBloque newlines')
	def comentarioInicialBloque(self, p):
		pass

	# Regla especial para el manejo y consumo del contenido del comentario de tipo bloque.
	@_('CONTENIDO_COMENTARIO contenidoComentarioBloque2')
	def contenidoComentarioBloque(self, p):
		pass
	
	# Para poder finalizar con el comentario debe de recibir una matricula y el cierre del comentario.
	@_('CONTENIDO_COMENTARIO contenidoComentarioBloque2',
	   'MATRICULA contenidoComentarioBloque3')
	def contenidoComentarioBloque2(self, p):
		pass

	# Para poder finalizar con el comentario debe de recibir una matricula y el cierre del comentario.
	@_('CONTENIDO_COMENTARIO contenidoComentarioBloque3',
	   'MATRICULA contenidoComentarioBloque3',
	   'FIN_COMENTARIO_BLOQUE')
	def contenidoComentarioBloque3(self, p):
		pass

	''''
		Esta regla esta creada con la intencion de encargarse de todas las declaraciones de constantes.
		Se realizo recursion por la izquierda aprovechando que SLY es de tipo LALR(1)
	'''
	@_('bloqueDeclaracionConstantes CONST SPACE declaracionConstante ";" newlines',
	   'CONST SPACE declaracionConstante ";" newlines')
	def bloqueDeclaracionConstantes(self, p):
		pass

	'''
		FRegla secundaria a la regla de "def bloqueDeclaracionConstantes(self, p):" donde declaramos
		el tipo de la constant, su nombre y la igualamos a un valor.
	'''
	@_('BOOL SPACE BOCONID ASSIGNMENT A_BOOLEAN',
	   'FLOAT SPACE FLCONID ASSIGNMENT DECIMAL',
	   'INT SPACE INCONID ASSIGNMENT ENTERO',
	   'CHAR SPACE CHCONID ASSIGNMENT A_CHAR',
	   'STRING SPACE STCONID ASSIGNMENT A_STRING')
	def declaracionConstante(self, p):
		self.tablaConstantes.agregarATabla(p[2], p[0], p[4])


	@_('bloqueDeclaracionGlobales')
	def declaracionesGlobales(self, p):
		self.finVariablesGlobales = self.dirVariables

	'''
		Regla encargada de la declaracion de las variables globales, estas se deben declarar fuera
		de cualquier modulo y tienen un scope global.
	'''
	@_('bloqueDeclaracionGlobales declaracionVariable ";" newlines',
	   'declaracionVariable ";" newlines')
	def bloqueDeclaracionGlobales(self, p):
		pass

	'''
		Tras haber definido las variables globales, debemos procesar las funciones, esto debido a 
		la estructura base que hemos diseniado para el lenguaje. Esta regla nos permite declarar
		varias funciones, pero antes de avanzar con la siguiente funcion llama a 
		"def declaracionFuncion(self, p):"
	'''
	@_('bloqueDeclaracionFunciones declaracionFuncion',
	   'declaracionFuncion')
	def bloqueDeclaracionFunciones(self, p):
		pass

	'''
		Esta regla esta encargada de obtener la funcion, ya sea la version completa o el
		prototipo de la funcion que se llama. En caso de que no sea un prototipo se llama 
		a la funcion de "def cuerpoFuncion(self, p):". Se hace notar que 'tipo' tambien
		llama a una funcion "def tipo(self,p):" que nos da el tipo de retorno.
	'''
	@_('validaFuncion cuerpoFuncion newlines')
	def declaracionFuncion(self, p):
		self.tablaModulos.agregarTamanosMemoria(p.validaFuncion, self.dirVariables - self.finVariablesGlobales, self.contadorTemporales)
		self.generaCuadruplo("ENDPROC", None, None, None)
		self.contadorTemporales = 0
		self.dirVariables = self.finVariablesGlobales
		self.tablaVariablesActual = None

	@_('setupPrototipo "(" declaracionArgumentos ";" newlines')
	def declaracionFuncion(self, p):
		self.tablaModulos.agregarPrototipo(p.setupPrototipo[0], p.setupPrototipo[1], p.declaracionArgumentos)
		self.dirVariables = self.finVariablesGlobales

	@_('setupFuncion "(" declaracionArgumentos')
	def validaFuncion(self, p):
		if self.tablaModulos.funcionExiste(p.setupFuncion[0]):
			if self.tablaModulos.checarFirma(p.setupFuncion[0], p.setupFuncion[1], p.declaracionArgumentos):
				self.tablaModulos.agregarATabla(p.setupFuncion[0], p.setupFuncion[1], self.contadorCuadruplos, p.declaracionArgumentos, self.tablaVariablesActual)
			else:
				print('Funcion no coincide con el prototipo declarado o intento de redeclaración', p.setupFuncion[0], p.lineno)
				sys.exit(1)
		else:
			self.tablaModulos.agregarATabla(p.setupFuncion[0], p.setupFuncion[1], self.contadorCuadruplos, p.declaracionArgumentos, self.tablaVariablesActual)
		return p.setupFuncion[0]

	@_('FUNC SPACE tipo SPACE IDFUNCION')
	def setupFuncion(self, p):
		self.tablaVariablesActual = TablaVariables()
		self.contadorLlamadas = 0
		return (p.IDFUNCION, p.tipo)

	@_('PROTO SPACE tipo SPACE IDFUNCION')
	def setupPrototipo(self, p):
		self.tablaVariablesActual = -1
		if self.tablaModulos.funcionExiste(p.IDFUNCION):
			print('Funcion ya declarada', p.IDFUNCION, 'prototipo duplicado en linea', p.lineno)
			sys.exit('Funcion declarada multiples veces.')
		return (p.IDFUNCION, p.tipo)

	# Nos permite obtener el tipo de la variable o funcion.
	@_('VOID',
	   'BOOL',
	   'FLOAT',
	   'INT',
	   'CHAR',
	   'STRING')
	def tipo(self, p):
		return p[0]

	@_('declaracionVariable "," SPACE declaracionArgumentos')
	def declaracionArgumentos(self, p):
		return [p.declaracionVariable].extend(p.declaracionArgumentos)

	@_('declaracionVariable ")"')
	def declaracionArgumentos(self, p):
		return [p.declaracionVariable]

	@_('")"')
	def declaracionArgumentos(self, p):
		return []

	@_('MAIN')
	def inicializaMain(self, p):
		self.cuadruplos.rellena(0, self.contadorCuadruplos)
		self.tablaVariablesActual = TablaVariables()
		self.tablaModulos.tablaModulos['main'] = ('main', 'void', self.contadorCuadruplos, [], self.tablaVariablesActual)

	'''
		Esta es una de las funciones mas importantes que tenemos, ya que se encarga del
		cuerpo de las funciones que tengamos, esto incluye al main. Su esetructura 
		puede tener un bloqueDeclaracionVariables pero necesita statements. Que son todas
		las expresiones y operaciones validas.
	'''
	@_('NEWLINE "{" newlines bloqueDeclaracionVariables statements "}" NEWLINE',
	   'NEWLINE "{" newlines statements "}" NEWLINE')
	def cuerpoFuncion(self, p):
		pass

	# Esta regla nos permite manejar la declaracion de variables en un punto dado.
	@_('bloqueDeclaracionVariables tabs declaracionVariable ";" newlines',
	   'tabs declaracionVariable ";" newlines')
	def bloqueDeclaracionVariables(self, p):
		pass

	'''
		Debido a la naturaleza del lenguaje, cada declaracion tiene su propia regla o 
		diagrama, pero todas siguen el mismo algoritmo de declaracion, donde obtenemos
		el tipo, la dimension y por ultimo esperamos un nombre en base a estos mismos
		detalles de la variable.
	'''
	@_('declaracionBool',
	   'declaracionFloat',
	   'declaracionInt',
	   'declaracionChar',
	   'declaracionString')
	def declaracionVariable(self, p):
		return p[0]

	# El uso de espacios es obligatorio.
	@_('BOOL SPACE declaracionBool2')
	def declaracionBool(self, p):
		return (p.BOOL,) + p.declaracionBool2 

	# Debemos ver cual de los tres tipos de declaracion se hara.
	@_('boolSimple',
	   'boolArray',
	   'boolMatriz')
	def declaracionBool2(self, p):
		return p[0]

	'''
		Si es una variable simple utilizamos esta regla. Donde agregamos a la tabla la nueva
		variable que se genero.
	'''
	@_('BOID')
	def boolSimple(self, p):
		self.agregaVariable(p.BOID, 'bool')
		self.dirVariables += 1
		return (p.BOID,)
	
	'''
		Si es una variable de una dimension utilizamos esta regla. Donde agregamos a la 
		tabla la nueva variable que se genero, pero incluimos el tamanio del arreglo.
	'''
	@_('BOARRID "[" tamano "]"')
	def boolArray(self, p):
		self.agregaVariable(p.BOARRID, 'bool', p.tamano)
		self.dirVariables += p.tamano
		return (p.BOARRID, p.tamano)

	'''
		Si es una variable de dos dimensiones utilizamos esta regla. Donde agregamos a la 
		tabla la nueva variable que se genero, pero inclcuimos el tamanio de las dos dimensiones.
	'''
	@_('BOMATID "[" tamano "]" "[" tamano "]"')
	def boolMatriz(self, p):
		self.agregaVariable(p.BOMATID, 'bool', p.tamano0, p.tamano1)
		self.dirVariables += p.tamano0 * p.tamano1
		return (p.BOMATID, p.tamano0, p.tamano1)

	@_('FLOAT SPACE declaracionFloat2')
	def declaracionFloat(self, p):
		return (p.FLOAT,) + p.declaracionFloat2

	@_('floatSimple',
	   'floatArray',
	   'floatMatriz')
	def declaracionFloat2(self, p):
		return p[0]

	@_('FLID')
	def floatSimple(self, p):
		self.agregaVariable(p.FLID, 'float')
		self.dirVariables += 1
		return (p.FLID,)

	@_('FLARRID "[" tamano "]"')
	def floatArray(self, p):
		self.agregaVariable(p.FLARRID, 'float', p.tamano)
		self.dirVariables += p.tamano
		return (p.FLARRID, p.tamano)

	@_('FLMATID "[" tamano "]" "[" tamano "]"')
	def floatMatriz(self, p):
		self.agregaVariable(p.FLMATID, 'float', p.tamano0, p.tamano1)
		self.dirVariables += p.tamano0 * p.tamano1
		return (p.FLMATID, p.tamano0, p.tamano1)

	@_('INT SPACE declaracionInt2')
	def declaracionInt(self, p):
		return (p.INT,) + p.declaracionInt2

	@_('intSimple',
	   'intArray',
	   'intMatriz')
	def declaracionInt2(self, p):
		return p[0]

	@_('INID')
	def intSimple(self, p):
		self.agregaVariable(p.INID, 'int')
		self.dirVariables += 1
		return (p.INID,)

	@_('INARRID "[" tamano "]"')
	def intArray(self, p):
		self.agregaVariable(p.INARRID, 'int', p.tamano)
		self.dirVariables += p.tamano
		return (p.INARRID, p.tamano)

	@_('INMATID "[" tamano "]" "[" tamano "]"')
	def intMatriz(self, p):
		self.agregaVariable(p.INMATID, 'int', p.tamano0, p.tamano1)
		self.dirVariables += p.tamano0 * p.tamano1
		return (p.INMATID, p.tamano0, p.tamano1)

	@_('CHAR SPACE declaracionChar2')
	def declaracionChar(self, p):
		return (p.CHAR,) + p.declaracionChar2

	@_('charSimple',
	   'charArray',
	   'charMatriz')
	def declaracionChar2(self, p):
		return p[0]

	@_('CHID')
	def charSimple(self, p):
		self.agregaVariable(p.CHID, 'char')
		self.dirVariables += 1
		return (p.CHID,)

	@_('CHARRID "[" tamano "]"')
	def charArray(self, p):
		self.agregaVariable(p.CHARRID, 'char', p.tamano)
		self.dirVariables += p.tamano
		return (p.CHARRID, p.tamano)

	@_('CHMATID "[" tamano "]" "[" tamano "]"')
	def charMatriz(self, p):
		self.agregaVariable(p.CHMATID, 'char', p.tamano0, p.tamano1)
		self.dirVariables += p.tamano0 * p.tamano1
		return (p.CHMATID, p.tamano0, p.tamano1)

	@_('STRING SPACE declaracionString2')
	def declaracionString(self, p):
		return (p.STRING,) + p.declaracionString2

	@_('stringSimple',
	   'stringArray',
	   'stringMatriz')
	def declaracionString2(self, p):
		return p[0]

	@_('STID')
	def stringSimple(self, p):
		self.agregaVariable(p.STID, 'string')
		self.dirVariables += 1
		return (p.STID,)

	@_('STARRID "[" tamano "]"')
	def stringArray(self, p):
		self.agregaVariable(p.STARRID, 'string', p.tamano)
		self.dirVariables += p.tamano
		return (p.STARRID, p.tamano)

	@_('STMATID "[" tamano "]" "[" tamano "]"')
	def stringMatriz(self, p):
		self.agregaVariable(p.STMATID, 'string', p.tamano0, p.tamano1)
		self.dirVariables += p.tamano0 * p.tamano1
		return (p.STMATID, p.tamano0, p.tamano1)

	'''
		Regla para tokenizar los enteros. Se hace notar que el tamanio de las dimensiones
		debe ser un entero o una constante de tipo entero.
	'''
	@_('ENTERO')
	def tamano(self, p):
		return p.ENTERO

	# Esta regla es usada para obtener el valor de una constante entera.
	@_('INCONID')
	def tamano(self, p):
		return self.tablaConstantes.getValor(p.INCONID)

	'''
		La regla siguiente es la base de la creacion de programas, ya que nos permite
		desplazarnos a las expresiones que se usan en el desarrollo de codigo de dia a dia.
		Maneja la recursion por la izquierda hasta que ya no se leen mas.
	'''	
	@_('statements tabs statement newlines',
	   'tabs statement newlines')
	def statements(self, p):
		pass

	# Aqui se dan las expresiones generales que tenemos.
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
		self.contadorCuadruplos += len(self.pilaAuxPost)
		if self.pilaAuxPost:
			self.cuadruplos.agregaCuadruplos(self.pilaAuxPost)
			self.pilaAuxPost.clear()


	'''
		Punto inicial del cual parte el if, lee la condicion, los corchetes,
		llama a 'elseif' spacio y recursivamente a si misma.
	'''
	'''
		Segundo caso que se puede presentar es en caso de que solo se presente
		un if o un if con un else. Y no se lleve mas.
	'''
	@_('condicionIf corchetes SPACE elseif SPACE condicionalIf',
	   'condicionIf corchetes SPACE elseFinal corchetes',
	   'condicionIf corchetes')
	def condicionalIf(self, p):
		saltoPendiente = self.pilaSaltosPendientes.pop()
		self.cuadruplos.rellena(saltoPendiente, self.contadorCuadruplos)

	'''
		Regla para tratar el inicio del IF, ya que toma el if, el espacio y llama al
		parentesis
	'''
	@_('IF SPACE parentesis')
	def condicionIf(self, p):
		self.pilaSaltosPendientes.append(self.contadorCuadruplos)
		self.generaCuadruplo('GoToF', p.parentesis, None, -1)
	
	'''
		El caso de la regla del else rellena el salto que dejo pendiente el GoToF del
		inicio del if.
	'''
	@_('ELSE')
	def elseif(self, p):
		saltoPendiente = self.pilaSaltosPendientes.pop()
		self.pilaSaltosPendientes.append(self.contadorCuadruplos)
		self.generaCuadruplo('GoTo', None, None, -1)
		self.cuadruplos.rellena(saltoPendiente, self.contadorCuadruplos)

	'''
		El caso de la regla del else final rellena el salto que dejo pendiente el 
		GoToF del inicio del if. Ademas de generar el GoTo al final del else.
	'''
	@_('ELSE')
	def elseFinal(self, p):
		saltoPendiente = self.pilaSaltosPendientes.pop()
		self.pilaSaltosPendientes.append(self.contadorCuadruplos)
		self.generaCuadruplo('GoTo', None, None, -1)
		self.cuadruplos.rellena(saltoPendiente, self.contadorCuadruplos)

	@_('SWITCH SPACE condicionSwitch NEWLINE tabs "{" NEWLINE tabs cases "}"')
	def condicionalSwitch(self, p):
		self.pilaAuxSwitch.pop()
		while self.pilaAuxBreak[-1] != '/':
			self.cuadruplos.rellena(self.pilaAuxBreak.pop(), self.contadorCuadruplos)
		self.pilaAuxBreak.pop()


	@_('parentesis')
	def condicionSwitch(self, p):
		self.pilaAuxSwitch.append(p.parentesis)
		self.pilaAuxBreak.append('/')
		return p.parentesis

	@_('CASE SPACE condicionPrimerCase ":" NEWLINE statements jumpNextCaseCheck cases2',
	   'CASE SPACE condicionPrimerCase ":" NEWLINE jumpNextCaseCheck cases2')
	def cases(self, p):
		pass

	@_('literalOConstante')
	def condicionPrimerCase(self, p):
		resultado = self.generaTemporal('bool')
		self.generaCuadruplo('==', self.pilaAuxSwitch[-1], p.literalOConstante, resultado)
		self.pilaSaltosPendientes.append(self.contadorCuadruplos)
		self.generaCuadruplo('GoToF', resultado, None, -1)
		return p.literalOConstante

	@_('CASE SPACE condicionCase ":" NEWLINE statements jumpNextCaseCheck cases2',
	   'CASE SPACE condicionCase ":" NEWLINE jumpNextCaseCheck cases2')
	def cases2(self, p):
		pass

	@_('setupDefaultCase ":" NEWLINE statements tabs')
	def cases2(self, p):
		pass

	@_('literalOConstante')
	def condicionCase(self, p):
		resultado = self.generaTemporal('bool')
		saltoPendiente = self.pilaSaltosPendientes.pop()
		self.cuadruplos.rellena(saltoPendiente, self.contadorCuadruplos)
		self.generaCuadruplo('==', self.pilaAuxSwitch[-1], p.literalOConstante, resultado)
		self.pilaSaltosPendientes.append(self.contadorCuadruplos)
		self.generaCuadruplo('GoToF', resultado, None, -1)
		return p.literalOConstante

	@_('tabs')
	def jumpNextCaseCheck(self, p):
		self.generaCuadruplo('GoTo', None, None, self.contadorCuadruplos + 3)

	@_('DEFAULT')
	def setupDefaultCase(self, p):
		self.popCuadruplo()
		saltoPendiente = self.pilaSaltosPendientes.pop()
		self.cuadruplos.rellena(saltoPendiente, self.contadorCuadruplos)

	# Esta regla es para el manejo de literales o constantes.
	@_('literal',
	   'constante')
	def literalOConstante(self, p):
		return ('v',) + p[0]
		
	# Regla para identificar booleanos.
	@_('A_BOOLEAN')
	def literal(self, p):
		return (p.A_BOOLEAN, 'bool')

	# Regla para identificar numeros decimales
	@_('DECIMAL')
	def literal(self, p):
		return (p.DECIMAL, 'float')

	# Regla para identificar numeros enteros
	@_('ENTERO')
	def literal(self, p):
		return (p.ENTERO, 'int')
	# Regla para identificar chars
	@_('A_CHAR')
	def literal(self, p):
		return (p.A_CHAR, 'char')

	# Regla para identificar strings
	@_('A_STRING')
	def literal(self, p):
		return (p.A_STRING, 'string')

	# Regla para identificar booleanos constantes.
	@_('BOCONID')
	def constante(self, p):
		return (self.tablaConstantes.getValor(p.BOCONID), 'bool')

	# Regla para identificar numeros decimales constantes.
	@_('FLCONID')
	def constante(self, p):
		return (self.tablaConstantes.getValor(p.FLCONID), 'float')

	# Regla para identificar numeros enteros constantes.
	@_('INCONID')
	def constante(self, p):
		return (self.tablaConstantes.getValor(p.INCONID), 'int')

	# Regla para identificar chars constantes.
	@_('CHCONID')
	def constante(self, p):
		return (self.tablaConstantes.getValor(p.CHCONID), 'char')

	# Regla para identificar strings constantes.
	@_('STCONID')
	def constante(self, p):
		return (self.tablaConstantes.getValor(p.STCONID), 'string')

	'''
		Regla encargada de manejar el FOR, aumenta el nivel de espera, mientras que 
		quita un cuadruplo de la pila de espera, genera un GoTo y rellena el fin de
		cuadruplo de la salida del for con el valor.

	'''
	@_('FOR SPACE "(" inicializacionFor ";" SPACE condicionFor ";" SPACE actualizacionFor ")" corchetes')
	def cicloFor(self, p):
		while self.pilaAuxContinueFor[-1] != '/':
			self.cuadruplos.rellena(self.pilaAuxContinueFor.pop(), self.contadorCuadruplos)
		self.pilaAuxContinueFor.pop()
		self.nivelDeEspera += 1
		self.liberaEspera()
		salidaDelFor = self.pilaSaltosPendientes.pop()
		self.generaCuadruplo('GoTo', None, None, self.pilaSaltosPendientes.pop())
		self.cuadruplos.rellena(salidaDelFor, self.contadorCuadruplos)
		while self.pilaAuxBreak[-1] != '/':
			self.cuadruplos.rellena(self.pilaAuxBreak.pop(), self.contadorCuadruplos)
		self.pilaAuxBreak.pop()
		self.pilaAuxContinue.pop()


	'''
		La inicializacion en el for consta de una asignacion, ademas de meter en la pila 
		de daltos pendientes el contador de cuadruplos.
	'''
	@_('asignacion')
	def inicializacionFor(self, p):
		self.pilaSaltosPendientes.append(self.contadorCuadruplos)
		self.pilaAuxBreak.append('/')
		self.pilaAuxContinue.append('For')
		self.pilaAuxContinueFor.append('/')
		return p.asignacion

	'''
		La condicion en el for consta de una asignacion. Se valida que no se use un string
		para realizar la coomparacion y se mete a la pila de daltos pendientes el actual.
		Se genera un GoToF que aun no esta completo que depende de la condicion.
		Y metemos el cuadruplo a la lista de espera.
	'''
	@_('asignacion')
	def condicionFor(self, p):
		if p.asignacion[2] == 'string':
			print('Error: type mismatch in line:', p.lineno, 'For loops can\'t choose based on a string')
		self.pilaSaltosPendientes.append(self.contadorCuadruplos)
		self.generaCuadruplo('GoToF', p.asignacion, None, -1)
		self.agregaCapaEspera()
		return p.asignacion

	# En la actualizacion manejamos la asignacion y le debemos restar al nivel de espera.
	@_('asignacion')
	def actualizacionFor(self, p):
		self.nivelDeEspera -= 1
		return p.asignacion

	@_('palabraWhile SPACE condicionWhile corchetes')
	def cicloWhile(self, p):
		salidaDelWhile = self.pilaSaltosPendientes.pop()
		self.generaCuadruplo('GoTo', None, None, self.pilaSaltosPendientes.pop())
		self.cuadruplos.rellena(salidaDelWhile, self.contadorCuadruplos)
		while self.pilaAuxBreak[-1] != '/':
			self.cuadruplos.rellena(self.pilaAuxBreak.pop(), self.contadorCuadruplos)
		self.pilaAuxBreak.pop()
		self.pilaAuxContinue.pop()
		self.pilaAuxContinueWhile.pop()

	@_('WHILE')
	def palabraWhile(self, p):
		self.pilaSaltosPendientes.append(self.contadorCuadruplos)
		self.pilaAuxBreak.append('/')
		self.pilaAuxContinue.append('While')
		self.pilaAuxContinueWhile.append(self.contadorCuadruplos)
		return p.WHILE

	@_('parentesis')
	def condicionWhile(self, p):
		if p.parentesis[2] == 'string':
			print('Error: type mismatch in line:', p.lineno, 'While loops can\'t choose based on a string')
		self.pilaSaltosPendientes.append(self.contadorCuadruplos)
		self.generaCuadruplo('GoToF', p.parentesis, None, -1)
		return p.parentesis

	@_('palabraDO corchetes SPACE antesCondicion SPACE parentesis')
	def cicloDo(self, p):
		if p.parentesis[2] == 'string':
			print('Error: type mismatch in line:', p.lineno, 'Do loops can\'t choose based on a string')
		self.generaCuadruplo('GoToV', p.parentesis, None, self.pilaSaltosPendientes.pop())
		while self.pilaAuxBreak[-1] != '/':
			self.cuadruplos.rellena(self.pilaAuxBreak.pop(), self.contadorCuadruplos)
		self.pilaAuxBreak.pop()
		self.pilaAuxContinue.pop()
		return p.parentesis

	@_('DO')
	def palabraDO(self, p):
		self.pilaSaltosPendientes.append(self.contadorCuadruplos)
		self.pilaAuxBreak.append('/')
		self.pilaAuxContinue.append('Do')
		self.pilaAuxContinueDo.append('/')
		return p.DO

	@_('NEWLINE tabs "{" newlines statements tabs "}"')
	def corchetes(self, p):
		pass

	@_('WHILE')
	def antesCondicion(self, p):
		while self.pilaAuxContinueDo[-1] != '/':
			self.cuadruplos.rellena(self.pilaAuxContinueDo.pop(), self.contadorCuadruplos)
		self.pilaAuxContinueDo.pop()

	@_('id ASSIGNMENT asignacion')
	def asignacion(self, p):
		self.generaCuadruplo(p.ASSIGNMENT, p.asignacion, None, p.id)
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
		self.generaCuadruplo('=', p.ternario, None, resultado)
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
		self.generaCuadruplo('GoToF', p.logicOr, None, -1)
		return p.logicOr

	@_('ternario TERNARIOPT2')
	def ternarioYOpTernario2(self, p):
		resultado = self.pilaAuxTernario[-1]
		saltoPendiente = self.pilaSaltosPendientes.pop()
		self.pilaAuxTernario.append(self.contadorCuadruplos)
		self.generaCuadruplo('=', p.ternario, None, resultado)
		self.pilaSaltosPendientes.append(self.contadorCuadruplos)
		self.generaCuadruplo('GoTo', None, None, -1)
		self.cuadruplos.rellena(saltoPendiente, self.contadorCuadruplos)
		return p.ternario

	@_('logicOr OR logicAnd')
	def logicOr(self, p):
		operandoIzq = p.logicOr
		operandoDer = p.logicAnd
		tipo = cuboSemantico.verificaSemantica2Operandos(p.OR, operandoIzq[2], operandoDer[2])
		if tipo == 'error':
			print('Error: type mismatch in line:', p.lineno, 'with operator ', p.OR)
		resultado = self.generaTemporal(tipo)
		self.generaCuadruplo(p.OR, operandoIzq, operandoDer, resultado)
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
		resultado = self.generaTemporal(tipo)
		self.generaCuadruplo(p.AND, operandoIzq, operandoDer, resultado)
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
		resultado = self.generaTemporal(tipo)
		self.generaCuadruplo(p.BIT_OR, operandoIzq, operandoDer, resultado)
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
		resultado = self.generaTemporal(tipo)
		self.generaCuadruplo(p.BIT_XOR, operandoIzq, operandoDer, resultado)
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
		resultado = self.generaTemporal(tipo)
		self.generaCuadruplo(p.BIT_AND, operandoIzq, operandoDer, resultado)
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
		resultado = self.generaTemporal(tipo)
		self.generaCuadruplo(p.EQ_NEQ, operandoIzq, operandoDer, resultado)
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
		resultado = self.generaTemporal(tipo)
		self.generaCuadruplo(p.COMPARADOR, operandoIzq, operandoDer, resultado)
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
		resultado = self.generaTemporal(tipo)
		self.generaCuadruplo(p.BITWISE_SHIFT, operandoIzq, operandoDer, resultado)
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
			resultado = self.generaTemporal(tipo)
			self.generaCuadruplo(p[1], operandoIzq, operandoDer, resultado)
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
			resultado = self.generaTemporal(tipo)
			self.generaCuadruplo(p[1], operandoIzq, operandoDer, resultado)
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
		self.generaCuadruplo(p[0][0], p.unidad, ('v', 1, 'int'), p.unidad)
		return p[1]

	@_('"!" unidad',
	   '"~" unidad',
	   '"-" unidad')
	def factor(self, p):
		tipo = cuboSemantico.verificaSemantica1Operando(p[0], p.unidad[2])
		if tipo != 'error':
			resultado = self.generaTemporal(tipo)
			self.contadorTemporales += 1
			self.generaCuadruplo(p[0], p.unidad, None, resultado)
			return resultado

	@_('id',
	   'llamadaFuncion',
	   'parentesis',
	   'literalOConstante')
	def unidad(self, p):
		return p[0]

	@_('id INCREMENT %prec POSTINCDEC')
	def unidad(self, p):
		print('El uso de incremento postfijo es altamnete desanimado. Linia:',p.lineno)
		self.pilaAuxPost.append(('+', p.id, ('v', 1, 'int'), p.id))
		return p[0]

	@_('id DECREMENT %prec POSTINCDEC')
	def unidad(self, p):
		print('El uso de decremento postfijo es altamnete desanimado. Linia:',p.lineno)
		self.pilaAuxPost.append(('-', p.id, ('v', 1, 'int'), p.id))
		return p[0]

	@_('"(" asignacion ")"')
	def parentesis(self, p):
		return p.asignacion

	@_('idSencillo')
	def id(self, p):
		return ('d',) + p.idSencillo

	@_('idArr',
	   'idMat')
	def id(self, p):
		return p[0]

	@_('BOID')
	def idSencillo(self, p):
		return (self.consigueDirVariable(p.BOID), 'bool')

	@_('FLID')
	def idSencillo(self, p):
		return (self.consigueDirVariable(p.FLID), 'float')

	@_('INID')
	def idSencillo(self, p):
		return (self.consigueDirVariable(p.INID), 'int')

	@_('CHID')
	def idSencillo(self, p):
		return (self.consigueDirVariable(p.CHID), 'char')

	@_('STID')
	def idSencillo(self, p):
		return (self.consigueDirVariable(p.STID), 'string')

	@_('BOARRID "[" asignacion "]"')
	def idArr(self, p):
		if p.asignacion[2] == 'string':
			print('Los accesos a un arreglo no pueden ser string. Linia:', p.lineno)
			sys.exit()
		arreglo = self.consigueVariable(p.BOARRID)
		self.generaCuadruplo('Ver', p.asignacion, 0, arreglo[3].tamano)
		resultado = self.generaAccesoArreglo('bool')
		self.generaCuadruplo('+', p.asignacion, ('v', self.consigueDirVariable(p.BOARRID), 'int'), resultado)
		return resultado

	@_('FLARRID "[" asignacion "]"')
	def idArr(self, p):
		if p.asignacion[2] == 'string':
			print('Los accesos a un arreglo no pueden ser string. Linia:', p.lineno)
			sys.exit()
		arreglo = self.consigueVariable(p.FLARRID)
		self.generaCuadruplo('Ver', p.asignacion, 0, arreglo[3].tamano)
		resultado = self.generaAccesoArreglo('float')
		self.generaCuadruplo('+', p.asignacion, ('v', self.consigueDirVariable(p.FLARRID), 'int'), resultado)
		return resultado

	@_('INARRID "[" asignacion "]"')
	def idArr(self, p):
		if p.asignacion[2] == 'string':
			print('Los accesos a un arreglo no pueden ser string. Linia:', p.lineno)
			sys.exit()
		arreglo = self.consigueVariable(p.INARRID)
		self.generaCuadruplo('Ver', p.asignacion, 0, arreglo[3].tamano)
		resultado = self.generaAccesoArreglo('int')
		self.generaCuadruplo('+', p.asignacion, ('v', self.consigueDirVariable(p.INARRID), 'int'), resultado)
		return resultado

	@_('CHARRID "[" asignacion "]"')
	def idArr(self, p):
		if p.asignacion[2] == 'string':
			print('Los accesos a un arreglo no pueden ser string. Linia:', p.lineno)
			sys.exit()
		arreglo = self.consigueVariable(p.CHARRID)
		self.generaCuadruplo('Ver', p.asignacion, 0, arreglo[3].tamano)
		resultado = self.generaAccesoArreglo('char')
		self.generaCuadruplo('+', p.asignacion, ('v', self.consigueDirVariable(p.CHARRID), 'int'), resultado)
		return resultado

	@_('STARRID "[" asignacion "]"')
	def idArr(self, p):
		if p.asignacion[2] == 'string':
			print('Los accesos a un arreglo no pueden ser string. Linia:', p.lineno)
			sys.exit()
		arreglo = self.consigueVariable(p.STARRID)
		self.generaCuadruplo('Ver', p.asignacion, 0, arreglo[3].tamano)
		resultado = self.generaAccesoArreglo('string')
		self.generaCuadruplo('+', p.asignacion, ('v', self.consigueDirVariable(p.STARRID), 'int'), resultado)
		return resultado

	@_('BOMATID "[" asignacion "]" "[" asignacion "]"')
	def idMat(self, p):
		if p.asignacion0[2] == 'string' or p.asignacion1[2] == 'string':
			print('Los accesos a una matriz no pueden ser string. Linia:', p.lineno)
			sys.exit()
		matriz = self.consigueVariable(p.BOMATID)
		self.generaCuadruplo('Ver', p.asignacion0, 0, matriz[3].tamano)
		temporal1 = self.generaTemporal('int')
		self.generaCuadruplo('*', p.asignacion0, ('v', matriz[3].m, 'int'), temporal1)
		self.generaCuadruplo('Ver', p.asignacion1, 0, matriz[3].next.tamano)
		temporal2 = self.generaTemporal('int')
		self.generaCuadruplo('+', temporal1, p.asignacion1, temporal2)
		resultado = self.generaAccesoArreglo('bool')
		self.generaCuadruplo('+', temporal2, ('v', self.consigueDirVariable(p.BOMATID), 'int'), resultado)
		return resultado

	@_('FLMATID "[" asignacion "]" "[" asignacion "]"')
	def idMat(self, p):
		if p.asignacion0[2] == 'string' or p.asignacion1[2] == 'string':
			print('Los accesos a una matriz no pueden ser string. Linia:', p.lineno)
			sys.exit()
		matriz = self.consigueVariable(p.FLMATID)
		self.generaCuadruplo('Ver', p.asignacion0, 0, matriz[3].tamano)
		temporal1 = self.generaTemporal('int')
		self.generaCuadruplo('*', p.asignacion0, ('v', matriz[3].m, 'int'), temporal1)
		self.generaCuadruplo('Ver', p.asignacion1, 0, matriz[3].next.tamano)
		temporal2 = self.generaTemporal('int')
		self.generaCuadruplo('+', temporal1, p.asignacion1, temporal2)
		resultado = self.generaAccesoArreglo('float')
		self.generaCuadruplo('+', temporal2, ('v', self.consigueDirVariable(p.FLMATID), 'int'), resultado)
		return resultado

	@_('INMATID "[" asignacion "]" "[" asignacion "]"')
	def idMat(self, p):
		if p.asignacion0[2] == 'string' or p.asignacion1[2] == 'string':
			print('Los accesos a una matriz no pueden ser string. Linia:', p.lineno)
			sys.exit()
		matriz = self.consigueVariable(p.INMATID)
		self.generaCuadruplo('Ver', p.asignacion0, 0, matriz[3].tamano)
		temporal1 = self.generaTemporal('int')
		self.generaCuadruplo('*', p.asignacion0, ('v', matriz[3].m, 'int'), temporal1)
		self.generaCuadruplo('Ver', p.asignacion1, 0, matriz[3].next.tamano)
		temporal2 = self.generaTemporal('int')
		self.generaCuadruplo('+', temporal1, p.asignacion1, temporal2)
		resultado = self.generaAccesoArreglo('int')
		self.generaCuadruplo('+', temporal2, ('v', self.consigueDirVariable(p.INMATID), 'int'), resultado)
		return resultado

	@_('CHMATID "[" asignacion "]" "[" asignacion "]"')
	def idMat(self, p):
		if p.asignacion0[2] == 'string' or p.asignacion1[2] == 'string':
			print('Los accesos a una matriz no pueden ser string. Linia:', p.lineno)
			sys.exit()
		matriz = self.consigueVariable(p.CHMATID)
		self.generaCuadruplo('Ver', p.asignacion0, 0, matriz[3].tamano)
		temporal1 = self.generaTemporal('int')
		self.generaCuadruplo('*', p.asignacion0, ('v', matriz[3].m, 'int'), temporal)
		self.generaCuadruplo('Ver', p.asignacion1, 0, matriz[3].next.tamano)
		temporal2 = self.generaTemporal('int')
		self.generaCuadruplo('+', temporal1, p.asignacion1, temporal2)
		resultado = self.generaAccesoArreglo('char')
		self.generaCuadruplo('+', temporal2, ('v', self.consigueDirVariable(p.CHMATID), 'int'), resultado)
		return resultado

	@_('STMATID "[" asignacion "]" "[" asignacion "]"')
	def idMat(self, p):
		if p.asignacion0[2] == 'string' or p.asignacion1[2] == 'string':
			print('Los accesos a una matriz no pueden ser string. Linia:', p.lineno)
			sys.exit()
		matriz = self.consigueVariable(p.STMATID)
		self.generaCuadruplo('Ver', p.asignacion0, 0, matriz[3].tamano)
		temporal1 = self.generaTemporal('int')
		self.generaCuadruplo('*', p.asignacion0, ('v', matriz[3].m, 'int'), temporal1)
		self.generaCuadruplo('Ver', p.asignacion1, 0, matriz[3].next.tamano)
		temporal2 = self.generaTemporal('int')
		self.generaCuadruplo('+', temporal1, p.asignacion1, temporal2)
		resultado = self.generaAccesoArreglo('string')
		self.generaCuadruplo('+', temporal2, ('v', self.consigueDirVariable(p.STMATID), 'int'), resultado)
		return resultado

	@_('inicilizaLlamada "(" argumentos')
	def llamadaFuncion(self, p):
		direccionFuncion = self.tablaModulos.conseguirDireccion(p.inicilizaLlamada[0])
		self.generaCuadruplo('GOSUB', direccionFuncion, None, p.inicilizaLlamada[1])
		return p.inicilizaLlamada[1]

	@_('READ "(" tipo ")"')
	def llamadaFuncion(self, p):
		if p.tipo == 'void':
			print('tipo void invalido para read. Linia', p.lineno)
			sys.exit(1)
		resultado = self.generaTemporal(p.tipo)
		self.generaCuadruplo('READ', None, None, resultado)
		return resultado

	@_('WRITE "(" asignacion ")"')
	def llamadaFuncion(self, p):
		self.generaCuadruplo('WRITE', p.asignacion, None, None)

	@_('IDFUNCION')
	def inicilizaLlamada(self, p):
		if self.tablaModulos.funcionExiste(p.IDFUNCION):
			self.numeroParametro = 0
			modulo = self.tablaModulos.tablaModulos[p.IDFUNCION]
			nombre = 'llamada' + str(self.contadorLlamadas)
			self.agregaVariable(nombre, modulo[1])
			self.dirVariables += 1
			self.contadorLlamadas += 1
			self.generaCuadruplo('ERA', p.IDFUNCION, None, None)
			self.numeroParametro = self.finVariablesGlobales
			datosVariableLlamada = self.tablaVariablesActual.tablaVariables[nombre]
			formaUsable = ('d', datosVariableLlamada[2], datosVariableLlamada[1])
		else:
			print('Funcion no declarada', p.IDFUNCION, 'usada en', p.lineno)
			sys.exit(1)
		return (p.IDFUNCION, formaUsable)

	@_('argumento "," SPACE argumentos',
	   'argumento ")"',
	   '")"')
	def argumentos(self, p):
		pass

	@_('asignacion')
	def argumento(self, p):
		self.generaCuadruplo('PARAM', p.asignacion, None, self.numeroParametro)

	@_('RETURN SPACE asignacion')
	def estatutoReturn(self, p):
		self.generaCuadruplo('RETURN', p.asignacion, None, None)

	@_('CONTINUE')
	def estatutoContinue(self, p):
		tipoLoop = self.pilaAuxContinue[-1]
		if tipoLoop == 'For':
			self.pilaAuxContinueFor.append(self.contadorCuadruplos)
			self.generaCuadruplo('GoTo', None, None, -1)
		elif tipoLoop == 'While':
			direccion = self.pilaAuxContinueWhile[-1]
			self.generaCuadruplo('GoTo', None, None, direccion)
		elif tipoLoop == 'Do':
			self.pilaAuxContinueDo.append(self.contadorCuadruplos)
			self.generaCuadruplo('GoTo', None, None, -1)

	@_('BREAK')
	def estatutoBreak(self, p):
		self.pilaAuxBreak.append(self.contadorCuadruplos)
		self.generaCuadruplo('GoTo', None, None, -1)

	@_('NEWLINE newlines %prec MNEWLINES',
	   'NEWLINE %prec MNEWLINES')
	def newlines(self, p):
		pass

	@_('tabs TAB',
	   'TAB')
	def tabs(self, p):
		pass

	###################################################################
	###################################################################
	################# Terminan las reglas de sintaxis #################
	###################################################################
	###################################################################


if __name__ == '__main__':
	import json
	from CEldaEncoder import CEldaEncoder
	lexer = CEldaLexer()
	parser = CEldaParser()

	with open(sys.argv[1], "r") as inputFile:
		data = inputFile.read()
		inputFile.close()
	if data:
		result = parser.parse(lexer.tokenize(data))
		encoder = CEldaEncoder()
		with open('out.CEldaObj', 'w') as outfile:
			outfile.write(encoder.encode(result))
			outfile.close()

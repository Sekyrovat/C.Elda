#!/usr/bin/python

# CEldaLexer.py
# Sergio López Madriz A01064725
# Héctor Hernández Morales A00816446

import sys
from sly import Lexer

'''
	Clase del lexer que se usara para verificar la existencia del comentario inicial.
	Debido a que el comentario inicial puede ser en un bloque (/* */) o de linea (//)
	esta clase activara otra clase dependiendo del tipo de comentario que detecte.

	Es importante hacer notar que el primer comentario con matricula es importante ya
	que de otra forma no continuara con la compilacion, ya que ignorara todo hasta 
	encontrar una matricula valida.
'''
class ComentarioInicialLexer(Lexer):

	tokens = {COMENTARIO_SIMPLE, INICIO_COMENTARIO_BLOQUE}

	# Dependiendo de la regla que se cumpla se llamara a la clase adecuada

	COMENTARIO_SIMPLE = r'//'
	INICIO_COMENTARIO_BLOQUE = r'/\*'

	def COMENTARIO_SIMPLE(self, t):
		self.begin(ComentarioInicialSimpleLexer)
		return t

	def INICIO_COMENTARIO_BLOQUE(self, t):
		self.begin(ComentarioInicialBloqueLexer)
		return t

	# Funcion utilizada para marcar que no se logro procesar un caracter.
	def error(self, t):
		print('Line %d: Bad character %r' % (self.lineno, t.value[0]))
		self.index += 1

# Clase encargada de procesar el primer comentario si es simple (//)
class ComentarioInicialSimpleLexer(Lexer):

	tokens = {COMENTARIO_SIMPLE, CONTENIDO_COMENTARIO, MATRICULA, NEWLINE}

	COMENTARIO_SIMPLE = r'//'

	'''
		La matricula debe iniciar con A o L ya sea en mayuscula o minuscula.
		Seguida de 8 numeros en el rango de 0 va 9.
	'''
	NEWLINE = r'\n'

	# Se usan expresiones regex. En el regex usado la expresion \d es equivalente a [0-9]
	MATRICULA = r'\s.*\b[AaLl]\d{8}\b.*'
	
	# Regla para ignorar todo el texto del comentario que no sea la matricula.
	CONTENIDO_COMENTARIO = r'\s.*'

	'''
		Si encontramos un NEWLINE debemos aumentar el numero de lineas en 1. Esto es 
		importante ya que es lo que nos permitira indicarle al programador donde fue 
		su error.
	'''
	def NEWLINE(self, t):
		self.lineno += 1
		return t

	'''
		Si encontramos la matricula llamamos a la clase del lexer que procesara el cuerpo del
		codigo.
	'''
	def MATRICULA(self, t):
		self.begin(CEldaLexer)
		return t

	# Funcion utilizada para marcar que no se logro procesar un caracter.
	def error(self, t):
		print('Line %d: Bad character %r' % (self.lineno, t.value[0]))
		self.index += 1
# Clase encargada de procesar el primer comentario si es de bloque (/* */)
class ComentarioInicialBloqueLexer(Lexer):

	tokens = {INICIO_COMENTARIO_BLOQUE, FIN_COMENTARIO_BLOQUE, CONTENIDO_COMENTARIO, MATRICULA}

	# Rewgla para indicar que existe un fin de linea.
	ignore_newline = r'\n'

	# Reglas para marcar el inicio y fin del comentario en bloque.
	INICIO_COMENTARIO_BLOQUE = r'/\*'
	FIN_COMENTARIO_BLOQUE = r'\*/'
	
	'''
		La matricula debe iniciar con A o L ya sea en mayuscula o minuscula.
		Seguida de 8 numeros en el rango de 0 va 9.
	'''
	# Se usan expresiones regex. En el regex usado la expresion \d es equivalente a [0-9]
	MATRICULA = r'(.*)\b[AaLl]\d{8}\b(?:(?!\*/).)*'
	
	# Regla para ignorar todo el texto del comentario que no sea la matricula.
	CONTENIDO_COMENTARIO = r'(?:(?!\*/).)+'

	'''
		Si encontramos un NEWLINE debemos aumentar el numero de lineas en 1. Esto es 
		importante ya que es lo que nos permitira indicarle al programador donde fue 
		su error.
	'''
	def ignore_newline(self, t):
		self.lineno += 1

	# Cuando se termina el comentario llamamos ala funcion principal.
	def FIN_COMENTARIO_BLOQUE(self, t):
		self.begin(CEldaLexer)
		return t

	# Funcion utilizada para marcar que no se logro procesar un caracter.
	def error(self, t):
		print('Line %d: Bad character %r' % (self.lineno, t.value[0]))
		self.index += 1

# Clase encargada de ignorar todos los comentarios de bloque.
class ComentarioBloqueLexer(Lexer):

	tokens = {}
	
	# Todo lo que va dentro de un comentario de bloque debe ser ignorado.
	ignore_newline = r'\n'

	# Sin embargo se debe de poner atencion al fin del comentario.
	ignore_fin_comentario_bloque = r'\*/'
	
	ignore_contenido_comentario = r'(?:(?!\*/).)+'

	# Cuando se detecten saltos de linea debemos sumarle uno al numero de linea.
	def ignore_newline(self, t):
		self.lineno += 1

	# Cuando se termina el comentario de bloque quitamos el estado.
	def ignore_fin_comentario_bloque(self, t):
		self.pop_state()

	# Funcion utilizada para marcar que no se logro procesar un caracter.
	def error(self, t):
		print('Line %d: Bad character %r' % (self.lineno, t.value[0]))
		self.index += 1

'''
	Cuando se termina de procesar el comentario Inicial se procede a utilizar este lexer en el resto
	del programa.
	Este Lexer se encargara de la tokenizacion primaria.
'''
class CEldaLexer(Lexer):

	def __init__(self):
		# Inicializamos variables de control.
		self.nesting_level = 0
		self.lineno = 1
		# Este Lexer inicia al del comentario inicial para realizar la busqueda del comentario con matricula.
		self.begin(ComentarioInicialLexer)

	# Aqui se dan todas las tokens que seran utilizadas.
	tokens = {INCREMENT, DECREMENT, TAB, SPACE, NEWLINE, BITWISE_SHIFT, COMPARADOR, EQ_NEQ, AND, OR, ASSIGNMENT, MATRICULA, BOID, BOARRID, BOMATID, FLID, FLARRID, FLMATID, INID, INARRID, INMATID, CHID, CHARRID, CHMATID, STID, STARRID, STMATID, FIID, PIID, TEXT, NUMERO, IDFUNCION, COMMENT}
	# Aqui declaramos las literales que se usaran.
	literals = {',', ';', '{', '}', '(', ')', '+', '-', '*', '/', '!', '~', '?', ':', '[', ']', '%', '^', '&', '|'}
	# ignore = ' \t'

	'''
		La siguiente seccion de codigo consiste en la declaracion de todas las expresiones regulares
		de los tokens que usara el compilador.
	'''
	
	'''
		Las siguientes expresiones regulares estan hechas con el proposito de forzar a que exista como
		minimo un espacio en blanco entre el inicio del cuerpo de un comentario y la inicializacion del
		mismo.
		Estas reglas se usan con la intencion de poder ignorar comentarios.
	'''
	ignore_comentario_simple = r'//.*'
	ignore_comentario_bloque = r'/\*'

	# Es importante procesar los TABS ya que seran parte de los soft errors que se graficaran.
	TAB = r'\t'
	SPACE = r' '

	'''
		Los NEWLINES tambien se consideraran para los softerrors ya que mas 80 caracteres por linea 
		se consideran mala practica, ademas de que se requieren por estandar junto con el uso de 
		whiles, fors, if, etcetera. Seran parte de lo graficado.
	'''
	NEWLINE = r'\n'

	'''
		Tokens para incremento y decremento de variables. Ejem i++, --j
		Se graficara el uso optimo de este tipo de incremento y decremento.
		Considerando al mas optimos como ++i o --j.
	'''
	INCREMENT = r'\+\+'
	DECREMENT = r'--'
	
	# Expresione regular para la verificacion de igualdad o diferncia.
	EQ_NEQ = r'(=|!)='

	'''
		Expresion regular que maneja los multiples tipos de asignacion.
		Se maneja la asignacion con suma(+=), resta(-=), multiplicacion(*=), 
		division(/=), modulo(%=), bitwise left shift(<<=), bitwise right shift(>>=),
		bitwise AND(&=), bitwise OR(|=), bitwise not(^=) y la asignacion sencilla (=) 
	'''
	ASSIGNMENT = r'(\+|-|\*|/|%|&|\^|\||<<|>>)?='

	# Expresion regular para realizar un shift de bits.
	BITWISE_SHIFT = r'<<|>>'

	# Expresiones regulares para las comparaciones.
	COMPARADOR = r'(<|>)=?'
	AND = r'&&'
	OR = r'\|\|'

	# Seccion con las expresiones regulares que se usaran para procesar los IDs.
	# Se debe hacer notar que \w expande [a-zA-Z0-9_]
	BOMATID = r'bMat[A-Z]\w*'
	BOARRID = r'bArr[A-Z]\w*'
	BOID = r'b[A-Z]\w*'
	
	FLMATID = r'fMat[A-Z]\w*'
	FLARRID = r'fArr[A-Z]\w*'
	FLID = r'f[A-Z]\w*'
	
	INMATID = r'iMat[A-Z]\w*'
	INARRID = r'iArr[A-Z]\w*'
	INID = r'i[A-Z]\w*'
	
	CHMATID = r'cMat[A-Z]\w*'
	CHARRID = r'cArr[A-Z]\w*'
	CHID = r'c[A-Z]\w*'
	
	STMATID = r'sMat[A-Z]\w*'
	STARRID = r'sArr[A-Z]\w*'
	STID = r's[A-Z]\w*'
	

	#####################################################################
	############# Falta modificar las expresiones para que  #############
	############# cumplan con los diagramas, ya que carecen #############
	############# de un ID y el tipo de dato que almacenan  #############
	#####################################################################
	# ID de pilas y de Filas
	FIID = r'stk[A-Z]\w*'
	PIID = r'q[A-Z]\w*'
	#####################################################################
	#####################################################################
	#####################################################################
	#####################################################################

	#TEXT
	#NUMERO

	'''
		Expresion regular para procesar el ID de la funcion.
		En la declaracion de la funcion primero va incluido el tipo de retorno
		de dicha funcion.
	'''
	IDFUNCION = r'[a-zA-Z]\w*'
	
	# ID = r'[a-zA-Z]\w*'
	# CTE_F = r'\d*\.\d+'
	# CTE_I = r'\d+'
	# A_STRING = r'\"(\\\"|[^\"])*\"'
	# A_CHAR = r'\'.|(\\n)\''
	# ID["program"] = PROGRAM
	# ID["var"] = VAR
	# ID["if"] = IF
	# ID["else"] = ELSE
	# ID["print"] = PRINT
	# ID["int"] = INT
	# ID["float"] = FLOAT 
	# COMPARADOR = r'<>?|>'

	# Extra action for newlines

	'''
		En caso de que se detecte un comentario de bloque guardamos el estado.
		Ademas de llamar la clase del lexer encargada de procesar los comentarios
		de bloque.
	'''
	def ignore_comentario_bloque(self, t):
		self.push_state(ComentarioBloqueLexer)

	'''
		Si encontramos un NEWLINE debemos aumentar el numero de lineas en 1. Esto es 
		importante ya que es lo que nos permitira indicarle al programador donde fue 
		su error.
	'''
	def NEWLINE(self, t):
		self.lineno += 1
		return t

	# Funcion utilizada para marcar que no se logro procesar un caracter.
	def error(self, t):
		print('Line %d: Bad character %r' % (self.lineno, t.value[0]))
		self.index += 1

if __name__ == '__main__':
	lexer = ComentarioInicialLexer()
	if len(sys.argv) > 1:
		with open(sys.argv[1], "r") as inputFile:
			data = inputFile.read()
		inputFile.close()
		for token in lexer.tokenize(data):
			print(token)
	else:
		while True:
			try:
				text = input('C.Elda > ')
			except EOFError:
				break
			if text == "exit":
				break
			if text:
				for token in lexer.tokenize(text):
					print(token)

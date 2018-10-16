#!/usr/bin/python

# C.Elda.py
# Sergio López Madriz A01064725
# Héctor Hernández Morales A00816446

import sys
from argparse import ArgumentParser
from CEldaLexer import CEldaLexer

# '''
#  Clase de Lexer utilizado para el comentario inicial que debe dar el alumno.
#  Contiene los tokes de comentario inicial y matricula, ya que de acuerdo a las especificaciones 
#  dadas esto es un requerimieto.
# '''
# class ComentarioInicialLexer(Lexer):
# 	tokens = {COMMENTARIO_INICIAL, MATRICULA}
# 	COMMENTARIO_INICIAL = r'//'
# 	'''
# 		La matricula debe iniciar con A o L ya sea en mayuscula o minuscula.
# 		Seguida de 8 numeros en el rango de 0 va 9.
# 	'''
# 	# Se usan expresiones regex. En el regex usado la expresion \d es equivalente a [0-9]
# 	MATRICULA = r'[AaLl]\d{8}' # \d expande a [0-9]

# '''
# 	Cuando se termina de procesar el comentario Inicial se procede a utilizar este lexer en el resto
# 	del programa.
# '''
# class CEldaLexer(Lexer):
# 	# Aqui se dan todas las tokens que seran utilizadas.
# 	tokens = {INCREMENT, DECREMENT, TAB, SPACE, NEWLINE, BITWISE_SHIFT, COMPARADOR, EQ_NEQ, AND, OR, ASSIGNMENT, MATRICULA, BOID, BOARRID, BOMATID, FLID, FLARRID, FLMATID, INID, INARRID, INMATID, CHID, CHARRID, CHMATID, STID, STARRID, STMATID, FIID, PIID, TEXT, NUMERO, IDFUNCION, COMMENT}
# 	# Aqui declaramos las literales que se usaran.
# 	literals = {',', ';', '{', '}', '(', ')', '+', '-', '*', '/', '!', '~', '?', ':', '[', ']', '%', '^', '&', '|'}
# 	# ignore = ' \t'

# 	# Tokens
# 	'''
# 		Aqui declaramos todos los tokens que usara el compilador.
# 	'''
# 	# Es importante procesar los TABS ya que seran parte de los soft errors que se graficaran.
# 	TAB = r'\t'
# 	SPACE = r' '
# 	'''
# 		Los NEWLINES tambien se consideraran para los softerrors ya que mas 80 caracteres por linea 
# 		se consideran mala practica, ademas de que se requieren por estandar junto con el uso de 
# 		whiles, fors, if, etcetera. Seran parte de lo graficado.
# 	'''
# 	NEWLINE = r'\n'

# 	'''
# 		Tokens para incremento y decremento de variables. Ejem i++, --j
# 		Se graficara el uso optimo de este tipo de incremento y decremento.
# 		Considerando al mas optimos como ++i o --j.
# 	'''
# 	INCREMENT = r'\+\+'
# 	DECREMENT = r'--'
	
# 	# Expresione regular para la verificacion de igualdad o diferncia.
# 	EQ_NEQ = r'(=|!)='

# 	'''
# 		Expresion regular que maneja los multiples tipos de asignacion.
# 		Se maneja la asignacion con suma(+=), resta(-=), multiplicacion(*=), 
# 		division(/=), modulo(%=), bitwise left shift(<<=), bitwise right shift(>>=),
# 		bitwise AND(&=), bitwise OR(|=), bitwise not(^=) y la asignacion sencilla (=) 
# 	'''
# 	ASSIGNMENT = r'(\+|-|\*|/|%|&|\^|\||<<|>>)?='

# 	# Expresion regular para realizar un shift de bits.
# 	BITWISE_SHIFT = r'<<|>>'

# 	# Expresiones regulares para las comparaciones.
# 	COMPARADOR = r'(<|>)=?'
# 	AND = r'&&'
# 	OR = r'\|\|'

# 	# Seccion con las expresiones regulares que se usaran para procesar los IDs.
# 	# Se debe hacer notar que \w expande [a-zA-Z0-9_]
# 	BOMATID = r'bMat[A-Z]\w*'
# 	BOARRID = r'bArr[A-Z]\w*'
# 	BOID = r'b[A-Z]\w*'
	
# 	FLMATID = r'fMat[A-Z]\w*'
# 	FLARRID = r'fArr[A-Z]\w*'
# 	FLID = r'f[A-Z]\w*'
	
# 	INMATID = r'iMat[A-Z]\w*'
# 	INARRID = r'iArr[A-Z]\w*'
# 	INID = r'i[A-Z]\w*'
	
# 	CHMATID = r'cMat[A-Z]\w*'
# 	CHARRID = r'cArr[A-Z]\w*'
# 	CHID = r'c[A-Z]\w*'
	
# 	STMATID = r'sMat[A-Z]\w*'
# 	STARRID = r'sArr[A-Z]\w*'
# 	STID = r's[A-Z]\w*'
	

# 	#####################################################################
# 	############# Falta modificar las expresiones para que  #############
# 	############# cumplan con los diagramas, ya que carecen #############
# 	############# de un ID y el tipo de dato que almacenan  #############
# 	#####################################################################
# 	# ID de pilas y de Filas
# 	FIID = r'stk[A-Z]\w*'
# 	PIID = r'q[A-Z]\w*'
# 	#####################################################################
# 	#####################################################################
# 	#####################################################################
# 	#####################################################################

# 	#TEXT
# 	#NUMERO

# 	'''
# 		Expresion regular para procesar el ID de la funcion.
# 		En la declaracion de la funcion primero va incluido el tipo de retorno
# 		de dicha funcion.
# 	'''
# 	IDFUNCION = r'[a-zA-Z]\w*'
	
# 	# ID = r'[a-zA-Z]\w*'
# 	# CTE_F = r'\d*\.\d+'
# 	# CTE_I = r'\d+'
# 	# A_STRING = r'\"(\\\"|[^\"])*\"'
# 	# A_CHAR = r'\'.|(\\n)\''
# 	# ID["program"] = PROGRAM
# 	# ID["var"] = VAR
# 	# ID["if"] = IF
# 	# ID["else"] = ELSE
# 	# ID["print"] = PRINT
# 	# ID["int"] = INT
# 	# ID["float"] = FLOAT 
# 	# COMPARADOR = r'<>?|>'

# 	# Ignored pattern
# 	'''
# 		Seccion de expresiones regulares que se usaran para ignorar comentarios.
# 		Se buscara que antes de cada funcion se agrege un comentario. Esto sera parte
# 		del output grafico. Ya que seran errores de tipo soft.
# 	'''
# 	ignore_comments = r'//.*'
# 	ignore_multiline_commets = r'/\*(.*|\n)\*/'

# 	# Extra action for newlines
# 	# def ignore_newline(self, t):
# 	# 	self.lineno += t.value.count('\n')

# 	# Funcion utilizada para marcar que no se logro procesar un caracter.
# 	def error(self, t):
# 		print('Line %d: Bad character %r' % (self.lineno, t.value[0]))
# 		self.index += 1

# class CEldaParser(Parser):
# 	debugfile = 'parser.out'
# 	tokens = LittleDuck2018Lexer.tokens

# 	precedence = (
# 		('left', "+", "-"),
# 		('left', TIMES_DIVIDE),
# 		('right', UMINUS),            # Unary minus operator
# 	)

# 	def __init__(self):
# 		pass

# 	@_('PROGRAM ID ";" programa2 bloque')
# 	def programa(self, p):
# 		print("Success!")
# 		return 0

# 	@_('vars',
# 	   'empty')
# 	def programa2(self, p):
# 		pass

# 	@_('VAR vars2')
# 	def vars(self, p):
# 		pass

# 	@_('ids ":" tipo ";" vars2',
# 	   'empty')
# 	def vars2(self, p):
# 		pass

# 	@_('ID ids2')
# 	def ids(self, p):
# 		pass

# 	@_('"," ID ids2',
# 	   'empty')
# 	def ids2(self, p):
# 		pass

# 	@_('INT',
# 	   'FLOAT')
# 	def tipo(self, p):
# 		pass

# 	@_('"{" estatutos "}"')
# 	def bloque(self, p):
# 		pass

# 	@_('estatuto estatutos',
# 	   'empty')
# 	def estatutos(self, p):
# 		pass

# 	@_('asignacion',
# 	   'condicion',
# 	   'escritura')
# 	def estatuto(self, p):
# 		pass

# 	@_('ID "=" expresion ";"')
# 	def asignacion(self, p):
# 		pass

# 	@_('exp expresion2')
# 	def expresion(self, p):
# 		pass

# 	@_('COMPARATOR exp',
# 	   'empty')
# 	def expresion2(self, p):
# 		pass

# 	@_('termino exp2')
# 	def exp(self, p):
# 		pass

# 	@_('"+" termino exp2',
# 	   '"-" termino exp2',
# 	   'empty')
# 	def exp2(self, p):
# 		pass

# 	@_('factor termino2')
# 	def termino(self, p):
# 		pass

# 	@_('TIMES_DIVIDE factor termino2',
# 	   'empty')
# 	def termino2(self, p):
# 		pass

# 	@_('"(" expresion ")"',
# 	   '"+" var_cte %prec UMINUS',
# 	   '"-" var_cte %prec UMINUS',
# 	   'var_cte')
# 	def factor(self, p):
# 		pass

# 	@_('ID',
# 	   'CTE_I',
# 	   'CTE_F')
# 	def var_cte(self, p):
# 		pass

# 	@_('IF "(" expresion ")" bloque condicion2 ";"')
# 	def condicion(self, p):
# 		pass

# 	@_('ELSE bloque',
# 	   'empty')
# 	def condicion2(self, p):
# 		pass

# 	@_('PRINT "(" escritura2 ")" ";"')
# 	def escritura(self, p):
# 		pass

# 	@_('expresion escritura3',
# 	   'CTE_STRING escritura3')
# 	def escritura2(self, p):
# 		pass

# 	@_('"," escritura2',
# 	   'empty')
# 	def escritura3(self, p):
# 		pass

# 	@_('')
# 	def empty(self, p):
# 		pass

'''
	Temporalmente solo esta con el procesamiento de los argumentos que se le pasaran en la CLI.
'''
def main():
	argParser = ArgumentParser(description="Compile a C.Elda program")
	argParser.add_argument('-V', '--version', action="store_true", help='display version information and exit')
	argParser.add_argument('-i', '--input', help='Name/Path of the input file')
	argParser.add_argument('-I', '--input-directory', '--files-from', help='Base path for input files')
	argParser.add_argument('-o', '--output', help='Name/Path of the output file (default: C.Elda', default='./C.Elda')
	argParser.add_argument('-O', '--output-directory', help='Base path for the output file (default: ./', default='./')
	argParser.add_argument('-d', '--directory', '--cd', help='set working directory', default='./')
	argParser.add_argument('-t', '--tokenize', action="store_true", help='only tokenize the input')
	argParser.parse_args()


if __name__ == '__main__':
	# main()
	lexer = CEldaLexer()
	# parser = CEldaParser()
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

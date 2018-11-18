#!/usr/bin/python3.7

# CEldaLexer.py
# Sergio López Madriz A01064725
# Héctor Hernández Morales A00816446

import sys
from sly import Lexer

eliminaEspacios = {
	' * ':		'*', 
	' / ':		'/', 
	' % ':		'%', 
	' + ':		'+', 
	' - ':		'-', 
	' << ':		'<<', 
	' >> ':		'>>', 
	' < ':		'<', 
	' <= ':		'<=', 
	' > ':		'>', 
	' >= ':		'>=', 
	' == ':		'==', 
	' != ':		'!=', 
	' & ':		'&', 
	' ^ ':		'^', 
	' | ':		'|', 
	' && ':		'&&', 
	' || ':		'||', 
	' ? ':		'?', 
	' : ':		':', 
	' += ':		'+=',
	' -= ':		'-=',
	' *= ':		'*=',
	' /= ':		'/=',
	' %= ':		'%=',
	' &= ':		'&=',
	' ^= ':		'^=',
	' |= ':		'|=',
	' <<= ':	'<<=',
	' >>= ':	'>>=',
	' = ':		'='
}

'''
 Clase de Lexer utilizado para el comentario inicial que debe dar el alumno.
 Contiene los tokens de comentario inicial y matricula, ya que de acuerdo a las especificaciones --- Hice muchas cosas, tienes que rehacer este comentario, perdon XD
 dadas esto es un requerimieto.
'''
class ComentarioInicialLexer(Lexer):

	tokens = {COMENTARIO_SIMPLE, INICIO_COMENTARIO_BLOQUE}

	COMENTARIO_SIMPLE = r'//'
	INICIO_COMENTARIO_BLOQUE = r'/\*'

	def COMENTARIO_SIMPLE(self, t):
		self.begin(ComentarioInicialSimpleLexer)
		return t

	def INICIO_COMENTARIO_BLOQUE(self, t):
		self.begin(ComentarioInicialBloqueLexer)
		return t

	def error(self, t):
		self.begin(CEldaLexer)

class ComentarioInicialSimpleLexer(Lexer):

	tokens = {COMENTARIO_SIMPLE, CONTENIDO_COMENTARIO, MATRICULA, NEWLINE}

	COMENTARIO_SIMPLE = r'//'
	'''
		La matricula debe iniciar con A o L ya sea en mayuscula o minuscula.
		Seguida de 8 numeros en el rango de 0 va 9.
	'''
	NEWLINE = r'\n'
	# Se usan expresiones regex. En el regex usado la expresion \d es equivalente a [0-9]
	MATRICULA = r'\s.*\b[AaLl]\d{8}\b.*' # \d expande a [0-9]
	CONTENIDO_COMENTARIO = r'\s.*'

	def NEWLINE(self, t):
		self.lineno += 1
		return t

	def MATRICULA(self, t):
		self.begin(CEldaLexer)
		return t

	def error(self, t):
		self.begin(CEldaLexer)

class ComentarioInicialBloqueLexer(Lexer):

	tokens = {FIN_COMENTARIO_BLOQUE, CONTENIDO_COMENTARIO, MATRICULA}

	ignore_newline = r'\n'

	FIN_COMENTARIO_BLOQUE = r'\*/'
	'''
		La matricula debe iniciar con A o L ya sea en mayuscula o minuscula.
		Seguida de 8 numeros en el rango de 0 va 9.
	'''
	# Se usan expresiones regex. En el regex usado la expresion \d es equivalente a [0-9]
	MATRICULA = r'(.*)\b[AaLl]\d{8}\b(?:(?!\*/).)*' # \d expande a [0-9]
	CONTENIDO_COMENTARIO = r'(?:(?!\*/).)+'

	def ignore_newline(self, t):
		self.lineno += 1

	def FIN_COMENTARIO_BLOQUE(self, t):
		self.begin(CEldaLexer)
		return t

	def error(self, t):
		self.begin(CEldaLexer)

class ComentarioBloqueLexer(Lexer):

	tokens = {}
	
	ignore_newline = r'\n'
	ignore_fin_comentario_bloque = r'\*/'
	'''
		La matricula debe iniciar con A o L ya sea en mayuscula o minuscula.
		Seguida de 8 numeros en el rango de 0 va 9.
	'''
	# Se usan expresiones regex. En el regex usado la expresion \d es equivalente a [0-9]
	ignore_contenido_comentario = r'(?:(?!\*/).)+'

	def ignore_newline(self, t):
		self.lineno += 1

	def ignore_fin_comentario_bloque(self, t):
		self.pop_state()

	def error(self, t):
		print('Line %d: Bad character %r' % (self.lineno, t.value[0]))
		self.index += 1

'''
	Cuando se termina de procesar el comentario Inicial se procede a utilizar este lexer en el resto
	del programa.
'''
class CEldaLexer(Lexer):

	def __init__(self):
		self.nesting_level = 0
		self.lineno = 1
		self.tabCount = 0
		self.begin(ComentarioInicialLexer) # Cambiamos inmediatamente al lexer para procesar el comentario inicial.

	# Aqui se dan todas las tokens que seran utilizadas.
	tokens = {TAB, SPACE, NEWLINE, ASSIGNMENT, TERNARIOPT1, TERNARIOPT2, OR, AND, BIT_OR, BIT_XOR, BIT_AND, EQ_NEQ,
			  COMPARADOR, BITWISE_SHIFT, PLUS, MINUS, TIMES, DIV, MOD, INCREMENT, DECREMENT, 
			  BOID, BOCONID, BOARRID, BOMATID, FLID, FLCONID, FLARRID, FLMATID, INID, INCONID, INARRID, INMATID,
			  CHID, CHCONID, CHARRID, CHMATID, STID, STCONID, STARRID, STMATID, FIBOID, FIFLID, FIINID, FICHID, FISTID,
			  PIBOID, PIFLID, PIINID, PICHID, PISTID, IDFUNCION, A_BOOLEAN, DECIMAL, ENTERO, A_CHAR, A_STRING, CONST,
			  FUNC, PROTO, VOID, BOOL, FLOAT, INT, CHAR, STRING, FILA, PILA, MAIN, IF, ELSE, SWITCH, CASE, DEFAULT, DO,
			  WHILE, FOR, BREAK, CONTINUE, RETURN, READ, WRITE, COMENTARIO_SIMPLE, INICIO_COMENTARIO_BLOQUE,
			  CONTENIDO_COMENTARIO, MATRICULA, FIN_COMENTARIO_BLOQUE}
	# Aqui declaramos las literales que se usaran.
	literals = {',', ':', ';', '{', '}', '(', ')', '+', '-', '!', '~', '[', ']'}
	# ignore = ' \t'

	# Ignored pattern
	'''
		Seccion de expresiones regulares que se usaran para ignorar comentarios.
		Se buscara que antes de cada funcion se agrege un comentario. Esto sera parte
		del output grafico. Ya que seran errores de tipo soft.
	'''
	ignore_comentario_simple = r'(\t*| ?)//.*'
	ignore_comentario_bloque = r'(\t*| ?)/\*'

	# Tokens
	'''
		Aqui declaramos todos los tokens que usara el compilador. ---Las expresiones regulares de los tokens
	'''

	'''
		Tokens para incremento y decremento de variables. Ejem i++, --j
		Se graficara el uso optimo de este tipo de incremento y decremento.
		Considerando al mas optimos como ++i o --j.
	'''
	INCREMENT = r'\+\+'
	DECREMENT = r'--'

	TIMES	= r' \* '
	DIV		= r' / '
	MOD		= r' % '

	PLUS	= r' \+ '
	MINUS	= r' - '

	# Expresion regular para realizar un shift de bits.
	BITWISE_SHIFT = r' (<<|>>) '

	# Expresiones regulares para las comparaciones.
	COMPARADOR	= r' ((<|>)=?) '
	EQ_NEQ 		= r' (=|!)= '
	BIT_AND		= r' & '
	BIT_XOR		= r' \^ '
	BIT_OR		= r' \| '
	AND			= r' && '
	OR			= r' \|\| '

	TERNARIOPT1	= r' \? '
	TERNARIOPT2	= r' : '
	
	'''
		Expresion regular que maneja los multiples tipos de asignacion.
		Se maneja la asignacion con suma(+=), resta(-=), multiplicacion(*=), 
		division(/=), modulo(%=), bitwise left shift(<<=), bitwise right shift(>>=),
		bitwise AND(&=), bitwise OR(|=), bitwise not(^=) y la asignacion sencilla (=) 
	'''
	ASSIGNMENT = r' (\+|-|\*|/|%|&|\^|\||<<|>>)?= '

	# Seccion con las expresiones regulares que se usaran para procesar los IDs.
	# Se debe hacer notar que \w expande [a-zA-Z0-9_]
	BOMATID		= r'bMat[A-Z]\w*\b'
	BOARRID		= r'bArr[A-Z]\w*\b'
	BOCONID		= r'b[A-Z][A-Z_]*\b'
	BOID		= r'b[A-Z]\w*\b'
	A_BOOLEAN	= r'TRUE|FALSE'
	FIBOID		= r'fiBool[A-Z]\w*\b'
	PIBOID		= r'piBool[A-Z]\w*\b'
	
	FLMATID	= r'fMat[A-Z]\w*\b'
	FLARRID	= r'fArr[A-Z]\w*\b'
	FLCONID	= r'f[A-Z][A-Z_]*\b'
	FLID	= r'f[A-Z]\w*\b'
	DECIMAL	= r'\d+\.\d+'
	FIFLID	= r'fiFloat[A-Z]\w*\b'
	PIFLID	= r'piFloat[A-Z]\w*\b'
	
	INMATID	= r'iMat[A-Z]\w*\b'
	INARRID	= r'iArr[A-Z]\w*\b'
	INCONID	= r'i[A-Z][A-Z_]*\b'
	INID	= r'i[A-Z]\w*\b'
	ENTERO	= r'\d+'
	FIINID	= r'fiInt[A-Z]\w*\b'
	PIINID	= r'piInt[A-Z]\w*\b'
	
	CHMATID	= r'cMat[A-Z]\w*\b'
	CHARRID	= r'cArr[A-Z]\w*\b'
	CHCONID	= r'c[A-Z][A-Z_]*\b'
	CHID	= r'c[A-Z]\w*\b'
	A_CHAR	= r'\'.\''
	FICHID	= r'fiChar[A-Z]\w*\b'
	PICHID	= r'piChar[A-Z]\w*\b'
	
	STMATID		= r'sMat[A-Z]\w*\b'
	STARRID		= r'sArr[A-Z]\w*\b'
	STCONID		= r's[A-Z][A-Z_]*\b'
	STID		= r's[A-Z]\w*\b'
	A_STRING	= r'"[^"\\]*(?:\\.[^"\\]*)*"'
	FISTID		= r'fiString[A-Z]\w*\b'
	PISTID		= r'piString[A-Z]\w*\b'

	'''
		Expresion regular para procesar el ID de la funcion.
		En la declaracion de la funcion primero va incluido el tipo de retorno
		de dicha funcion.
	'''
	IDFUNCION = r'[a-zA-Z]\w*'

	IDFUNCION["const"]		= CONST
	IDFUNCION["func"]		= FUNC
	IDFUNCION["proto"]		= PROTO
	IDFUNCION["void"]		= VOID
	IDFUNCION["bool"]		= BOOL
	IDFUNCION["float"]		= FLOAT
	IDFUNCION["int"]		= INT
	IDFUNCION["char"]		= CHAR
	IDFUNCION["string"]		= STRING
	IDFUNCION["fila"]		= FILA
	IDFUNCION["pila"]		= PILA
	IDFUNCION["main"]		= MAIN
	IDFUNCION["if"]			= IF
	IDFUNCION["else"]		= ELSE
	IDFUNCION["switch"]		= SWITCH
	IDFUNCION["case"]		= CASE
	IDFUNCION["default"]	= DEFAULT
	IDFUNCION["for"]		= FOR
	IDFUNCION["do"]			= DO
	IDFUNCION["while"]		= WHILE
	IDFUNCION["break"]		= BREAK
	IDFUNCION["continue"]	= CONTINUE
	IDFUNCION["return"]		= RETURN
	IDFUNCION["read"]		= READ
	IDFUNCION["write"]		= WRITE
	'''
		Los NEWLINES tambien se consideraran para los softerrors ya que mas 80 caracteres por linea 
		se consideran mala practica, ademas de que se requieren por estandar junto con el uso de 
		whiles, fors, if, etcetera. Seran parte de lo graficado.
	'''
	NEWLINE = r'\n'
	# Es importante procesar los TABS ya que seran parte de los soft errors que se graficaran.
	TAB		= r'\t'
	SPACE	= r' '

	# Extra action for newlines
	def ignore_comentario_bloque(self, t):
		self.push_state(ComentarioBloqueLexer)

	def TAB(self, t):
		self.tabCount += 1
		return t

	def NEWLINE(self, t):
		self.lineno += 1
		self.tabCount = 0
		return t

	def DECIMAL(self, t):
		t.value = float(t.value)
		return t

	def ENTERO(self, t):
		t.value = int(t.value)
		return t

	def A_BOOLEAN(self, t):
		if t.value == 'TRUE':
			t.value = 1
		else:
			t.value = 0
		return t

	def TIMES(self, t):
		t.value = eliminaEspacios[t.value]
		return t

	def DIV(self, t):
		t.value = eliminaEspacios[t.value]
		return t

	def MOD(self, t):
		t.value = eliminaEspacios[t.value]
		return t

	def PLUS(self, t):
		t.value = eliminaEspacios[t.value]
		return t

	def MINUS(self, t):
		t.value = eliminaEspacios[t.value]
		return t

	def BITWISE_SHIFT(self, t):
		t.value = eliminaEspacios[t.value]
		return t

	def COMPARADOR(self, t):
		t.value = eliminaEspacios[t.value]
		return t

	def EQ_NEQ(self, t):
		t.value = eliminaEspacios[t.value]
		return t

	def BIT_AND(self, t):
		t.value = eliminaEspacios[t.value]
		return t

	def BIT_XOR(self, t):
		t.value = eliminaEspacios[t.value]
		return t

	def BIT_OR(self, t):
		t.value = eliminaEspacios[t.value]
		return t

	def AND(self, t):
		t.value = eliminaEspacios[t.value]
		return t

	def OR(self, t):
		t.value = eliminaEspacios[t.value]
		return t

	def TERNARIOPT1(self, t):
		t.value = eliminaEspacios[t.value]
		return t

	def TERNARIOPT2(self, t):
		t.value = eliminaEspacios[t.value]
		return t

	def ASSIGNMENT(self, t):
		t.value = eliminaEspacios[t.value]
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



# Link a la pagina de plotly que suaremos para la grafica resultante:
# https://plot.ly/python/pie-charts/
# Link a la tablade precedencia
# https://en.cppreference.com/w/c/language/operator_precedence

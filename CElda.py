#!/usr/bin/python3.7
#
# CElda.py
# Sergio López Madriz A01064725
# Héctor Hernández Morales A00816446

import json
import os
import sys
from argparse import ArgumentParser, FileType
from CEldaLexer import CEldaLexer
from CEldaParser import CEldaParser
from CEldaEncoder import CEldaEncoder, hinted_tuple_hook
from CEldaMaquinaVirtual import CEldaMaquinaVirtual

'''
	Temporalmente solo esta con el procesamiento de los argumentos que se le pasaran en la CLI.
'''
def main():
	argParser = ArgumentParser(description="Compile/Execute a C.Elda program")
	modo = argParser.add_mutually_exclusive_group()
	modo.add_argument('-t', '--tokenize', action="store_true", help='only tokenize the input')
	modo.add_argument('-p', '--parse', action="store_true", help='tokenize and parse the input')
	modo.add_argument('-c', '--compile', action="store_true", help='tokenize, parse and compile, doesn\'t require the -o option')
	modo.add_argument('-x', '--execute', action="store_true", help='run a precompiled file ignores -o option')
	argParser.add_argument('-o', '--outputofile', action="store_true", help='write to output to file.')
	argParser.add_argument('CEldaSrc', help='File to process', type=FileType('r', encoding='UTF-8'))
	args = argParser.parse_args()
	tokenize = args.tokenize
	parse = args.parse
	comp = args.compile
	execute = args.execute
	output = args.outputofile
	inFile = args.CEldaSrc

	name = os.path.splitext(inFile.name)[0]

	if not execute:
		lexer = CEldaLexer()
		data = inFile.read()
		inFile.close()
		if data:
			result = lexer.tokenize(data)
			if tokenize:
				if output:
					filename = name + '.tokens'
					with open(filename, 'w', encoding='UTF-8') as outfile:
						for token in result:
							outfile.write(str(token))
							outfile.write('\n')
						outfile.close()
				else:
					for token in result:
						print(token)
				sys.exit(0)
			parser = CEldaParser()
			result = parser.parse(result) 
			if parse:
				if output:
					filename = name + '.parse'
					with open(filename, 'w', encoding='UTF-8') as outfile:
						outfile.write('Tabla de Constantes\n')
						outfile.write(str(parser.tablaConstantes))
						outfile.write('\n')
						outfile.write('Tabla de Variables Globales\n')
						outfile.write(str(parser.tablaVariablesGlobales))
						outfile.write('\n')
						outfile.write('Tabla de Modulos\n')
						outfile.write(str(parser.tablaModulos))
						outfile.write('\n')
						outfile.write(str(parser.finVariablesGlobales))
						outfile.write('\n')
						outfile.write(str(parser.tablaModulos.creaReduccion()))
						outfile.write('\n')
						outfile.write('Cuadruplos\n')
						outfile.write(str(parser.cuadruplos))
						outfile.write('\n')
						outfile.close()
				else:
					print()
					print('Tabla de Constantes')
					print(parser.tablaConstantes)
					print()
					print('Tabla de Variables Globales')
					print(parser.tablaVariablesGlobales)
					print()
					print('Tabla de Modulos')
					print(parser.tablaModulos)
					print()
					print(parser.finVariablesGlobales)
					print(parser.tablaModulos.creaReduccion())
					print()
					print('Cuadruplos')
					print(parser.cuadruplos)
				sys.exit(0)
			if comp:
				filename = name + '.CEldaObj'
				encoder = CEldaEncoder()
				with open(filename, 'w', encoding='UTF-8') as outfile:
					outfile.write(encoder.encode(result))
					outfile.close()
				sys.exit(0)
			maquina = CEldaMaquinaVirtual(result)
			maquina.run()
	else:
		content = inFile.read()
		data = json.loads(content, object_hook=hinted_tuple_hook)
		inFile.close()
		maquina = CEldaMaquinaVirtual(data)
		maquina.run()



if __name__ == '__main__':
	main()
	
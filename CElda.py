#!/usr/bin/python
#
# CElda.py
# Sergio López Madriz A01064725
# Héctor Hernández Morales A00816446

import sys
from argparse import ArgumentParser
from CEldaLexer import CEldaLexer

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

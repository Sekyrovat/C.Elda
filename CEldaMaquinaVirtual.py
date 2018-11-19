#!/usr/bin/python3.7
#
# CEldaMaquinaVirtual.py
# Sergio López Madriz A01064725
# Héctor Hernández Morales A00816446

import sys
import json
from CEldaEncoder import hinted_tuple_hook

with open('out.json', 'r') as json_file:
	content = json_file.read()
	data = json.loads(content, object_hook=hinted_tuple_hook)
	json_file.close()
print(data)

class CEldaMaquinaVirtual(object):
	"""docstring for CEldaMaquinaVirtual"""
	def __init__(self):
		self.frontera = data['frontera']
		self.infoFunciones = data['funciones']
		self.cuadruplos = data['cuadruplos']
		self.currentCuad = 0;
		self.memoriaGlobales = creaLista(frontera)
		self.memoriaFuncion = creaLista(infoFunciones['main'][0])
		self.memoriaTemporales = creaLista(infoFunciones['main'][1])
		self.pilaDePopsaAhacerTemps = []
		self.pilaDePausaTemps = []
		self.pilaDePopsaAhacer = []
		self.pilaDePausa= []
		self.pilaRetorno = []

		print(self.frontera)
		print()
		print(self.infoFunciones)
		print()
		print(self.cuadruplos)

	def getValue(self, tripleta):
		if tripleta[0] == 'v':
			return tripleta[1]
		elif tripleta[0] == 'd'
			if tripleta[1] < self.frontera:
				valor = self.memoriaGlobales[tripleta[1]]
			else:
				direccion = tripleta[1] - self.frontera
				valor = self.memoriaFuncion[direccion]
			if valor is None:
				print("Variable no inicializada.")
				sys.exit(1)
			return valor
		else
			return self.memoriaTemporales[tripleta[1]]
	

	def setValue(self, tripleta, valor):
		if tripleta[0] == 'd':
			if tripleta[1] < self.frontera:
				self.memoriaGlobales[tripleta[1]] = valor
			else:
				direccion = tripleta[1] - self.frontera
				self.memoriaFuncion[direccion] = valor
		else:
			self.memoriaTemporales[tripleta[1]] = valor

	def GoTo(self, cuadruplo):
		self.currentCuad = cuadruplos.resultado - 1

	def GoToV(self, cuadruplo):
		if getValue(cuadruplo[1]) > 0:
			self.currentCuad = cuadruplos[3]-1
	
	def GoToF(self, cuadruplo):
		if getValue(cuadruplo[1]) == 0:
			self.currentCuad = cuadruplos[3]-1

	def asign(self,cuadruplo):
        self.setValue(cuadruplo[3], cuadruplo[1][1])

##########################
##########################
##########################
	def ENDPROC(self):
		pops = self.pilaDePopsaAhacer.pop()
		pilaTemp = []
		while pops >= 0:
			pilaTemp.append(self.pilaDePausa.pop())
			pops -= 1
		self.memoriaFuncion = pilaTemp
		pops = self.pilaDePopsaAhacerTemps.pop()
		pilaTemp = []
		while pops >= 0:
			pilaTemp.append(self.pilaDePausaTemps.pop())
			pops -= 1
		self.memoriaTemporales = pilaTemp

	def opArit(self,cuad,memoria):
        arg1 = self.getValue(cuadruplo[1])
        arg2 =  self.getValue(cuadruplo[2])
		op = cuadruplo[0]
		if op == '+':
            arg3 = arg1 + arg2
        elif op == '-':
            arg3 = arg1 - arg2
        elif op == '*':
            arg3 = arg1 * arg2
        elif op == '<<':
        	arg3 = arg1 << arg2
        elif op == '>>':
        	arg3 = arg1 >> arg2
        elif op == '^'
        	arg3 = arg1 ^ arg2
		elif op == '&'
			arg3 = arg1 & arg2
		elif op == '|'
			arg3 = arg1 | arg2
		self.setValue(cuadruplo[3], arg3)

    def opWithDiv(self, cuadruplo):
        arg1 = self.getValue(cuadruplo[1])
        arg2 =  self.getValue(cuadruplo[2])
		op = cuadruplo[0]
        if(arg2 == 0):
            print('ERROR division con 0')
            quit()
        if op == '/':
            arg3 = arg1 / arg2
        elif op == '%':
            arg3 = arg1 % arg2
        self.setValue(cuadruplo[3], arg3)

    def opLogic(self,cuadruplo):
        arg1 = self.getValue(cuadruplo[1])
        arg2 =  self.getValue(cuadruplo[2])
		op = cuadruplo[0]
		if op == '&&'
			arg3 = arg1 && arg2
		elif op == '||'
			arg3 = arg1 || arg2 
        elif op == '<':
        	arg3 = arg1 < arg2
        elif op == '<='
        	arg3 = arg1 <= arg2
		elif op == '>'
			arg3 = arg1 > arg2
		elif op == '>='
			arg3 = arg1 >= arg2
		elif op == '!='
			arg3 = arg1 != arg2
		elif op == '=='
			arg3 = arg1 == arg2 
		self.setValue(cuadruplo[3], arg3)

##########################
##########################
	def ERA(self, cuadruplo):
		self.pilaDePausa.append(memoriaFuncion)
		self.pilaDePausaTemps.append(memoriaTemporales)
		self.pilaDePopsaAhacer.append(len(memoriaFuncion))
		self.pilaDePopsaAhacerTemps.append(len(memoriaTemporales))
		self.memoriaFuncion = []
		self.memoriaTemporales = []
		self.memoriaFuncion = creaLista(cuadruplo[1][0])
		self.memoriaTemporales = creaLista(cuadruplo[1][1])

##########################
	def GOSUB(self, cuadruplo):
		self.currentCuad = cuadruplos[3]-1

##########################
##########################
##########################
	def PARAM(self, cuadruplo):
		pass
##########################
##########################
##########################
	def RETURN(self):
		pass

	# def WriteVar(self, cuadruplo):
	# 	print(getValue(cuadruplo[1]))

	# def ReadVar(self, cuadruplo):
	# 	temp = input()
	# 	print(setValue(cuadruplo[3], cuadruplo[1]))
		
	def run(self,begin,end):
        while self.cuadruplos[self.currentCuad[0]] != EXIT:
            cuadruplo = self.cuadruplos[self.currentCuad]
            operacion = cuadruplo[0]
            if operacion == 'GoTo':
                self.GoTo(cuadruplo)
            elif operacion == 'GoToF':
                self.GoToF(cuadruplo)
            elif operacion == 'GoToV':
                self.GoToV(cuadruplo)
            elif operacion == 'ERA':
                self.era(cuadruplo)
            elif operacion == 'GOSUB':
                self.GOSUB(cuadruplo)
            elif operacion == 'ENDPROC':
            	self.enproc(cuadruplo)
            elif operacion == 'PARAM':
                self.PARAM(cuadruplo)
            elif operacion == 'RETURN':
                self.RETURN(cuadruplo)
            # elif operacion == 'verify':
            #     self.verify()
            elif operacion == '+' or operacion == '-' or operacion == '*' or operacion == '<<' or operacion == '>>' or operacion == '^' or operacion == '&' or operacion == '|':
                self.opArit(cuadruplo)
            elif operacion == '/' or operacion == '%':
                self.opWithDiv(cuadruplo)
            elif  operacion == '&&' or operacion == '||' or operacion == '<' or operacion == '<=' or operacion == '>' or operacion == '>=' or operacion == '!=' or operacion == '==':
                self.opLogic(cuadruplo)
            elif operacion == '=':
                self.asign(cuadruplo)
            elif operacion == 'Write':
                self.WriteVar(cuadruplo)
            elif operacion == 'Read':
                self.ReadVar(cuadruplo)

            else:
                print('ERROR, cuadruplo no acceptado: ')
                print(cuadruplo)

            self.cuadActual = self.cuadActual + 1
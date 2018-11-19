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
		self.memoriaGlobales = self.creaLista(self.frontera)
		self.memoriaFuncion = self.creaLista(self.infoFunciones['main'][0])
		print(len(self.memoriaFuncion))
		self.memoriaTemporales = self.creaLista(self.infoFunciones['main'][1])
		self.memACrear = []
		self.memoriaLlamada = []
		self.pilaDePausaTemps = []
		self.pilaDePausa= []
		self.pilaRetorno = []

	def getValue(self, tripleta):
		print(tripleta)
		print(self.currentCuad)
		if tripleta[0] == 'v':
			return tripleta[1]
		elif tripleta[0] == 'd':
			if tripleta[1] < self.frontera:
				valor = self.memoriaGlobales[tripleta[1]]
			else:
				direccion = tripleta[1] - self.frontera
				valor = self.memoriaFuncion[direccion]
			if valor is None:
				print("Variable no inicializada.")
				sys.exit(1)
			return valor
		else:
			return self.memoriaTemporales[tripleta[1]]
	

	def setValue(self, tripleta, valor):
		print(tripleta, valor)
		if tripleta[0] == 'd':
			if tripleta[1] < self.frontera:
				self.memoriaGlobales[tripleta[1]] = valor
			else:
				direccion = tripleta[1] - self.frontera
				print(direccion)
				self.memoriaFuncion[direccion] = valor
		else:
			self.memoriaTemporales[tripleta[1]] = valor

	def setParam(self, valor, direccion):
		direccion -= self.frontera
		print(direccion)
		self.memoriaLlamada[direccion] = valor

	def GoTo(self, cuadruplo):
		self.currentCuad = cuadruplo[3] - 1

	def GoToV(self, cuadruplo):
		if self.getValue(cuadruplo[1]) > 0:
			self.currentCuad = cuadruplo[3] - 1
	
	def GoToF(self, cuadruplo):
		if self.getValue(cuadruplo[1]) == 0:
			self.currentCuad = cuadruplo[3] - 1

	def asign(self, cuadruplo):
		self.setValue(cuadruplo[3], cuadruplo[1][1])

##########################

	def opArit(self, cuadruplo):
		print(cuadruplo)
		print(self.currentCuad)
		arg1 = self.getValue(cuadruplo[1])
		if cuadruplo[2] is None:
			arg2 = arg1
			arg1 = 0
		else:
			arg2 = self.getValue(cuadruplo[2])
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
		elif op == '^':
			arg3 = arg1 ^ arg2
		elif op == '&':
			arg3 = arg1 & arg2
		elif op == '|':
			arg3 = arg1 | arg2
		self.setValue(cuadruplo[3], arg3)


	def opAritIgual(self, cuadruplo):
		arg1 = self.getValue(cuadruplo[3])
		arg2 = self.getValue(cuadruplo[1])
		op = cuadruplo[0]
		if op == '=+':
			arg3 = arg1 + arg2
		elif op == '=-':
			arg3 = arg1 - arg2
		elif op == '=*':
			arg3 = arg1 * arg2
		elif op == '=<<':
			arg3 = arg1 << arg2
		elif op == '=>>':
			arg3 = arg1 >> arg2
		elif op == '=^':
			arg3 = arg1 ^ arg2
		elif op == '=&':
			arg3 = arg1 & arg2
		elif op == '=|':
			arg3 = arg1 | arg2
		self.setValue(cuadruplo[3], arg3)


	def opWithDiv(self, cuadruplo):
		arg1 = self.getValue(cuadruplo[1])
		arg2 =  self.getValue(cuadruplo[2])
		op = cuadruplo[0]
		if(arg2 == 0):
			print('ERROR division con 0')
			sys.exit()
		if op == '/':
			arg3 = arg1 / arg2
		elif op == '%':
			arg3 = arg1 % arg2
		self.setValue(cuadruplo[3], arg3)

	def opWithDivIgual(self, cuadruplo):
		arg1 = self.getValue(cuadruplo[3])
		arg2 =  self.getValue(cuadruplo[1])
		op = cuadruplo[0]
		if(arg2 == 0):
			print('ERROR division con 0')
			sys.exit()
		if op == '=/':
			arg1 = arg1 / arg2
		elif op == '=%':
			arg1 = arg1 % arg2
		self.setValue(cuadruplo[3], arg3)

	def opLogic(self,cuadruplo):
		arg1 = self.getValue(cuadruplo[1])
		arg2 =  self.getValue(cuadruplo[2])
		op = cuadruplo[0]
		if op == '&&':
			arg3 = arg1 and arg2
		elif op == '||':
			arg3 = arg1 or arg2 
		elif op == '<':
			arg3 = arg1 < arg2
		elif op == '<=':
			arg3 = arg1 <= arg2
		elif op == '>':
			arg3 = arg1 > arg2
		elif op == '>=':
			arg3 = arg1 >= arg2
		elif op == '!=':
			arg3 = arg1 != arg2
		elif op == '==':
			arg3 = arg1 == arg2 
		self.setValue(cuadruplo[3], arg3)

##########################
	def ERA(self, cuadruplo):
		self.pilaDePausa.append(self.memoriaFuncion)
		self.pilaDePausaTemps.append(self.memoriaTemporales)
		self.memACrear = self.infoFunciones[cuadruplo[1]]
		self.memoriaLlamada = self.creaLista(self.memACrear[0])

##########################
	def GOSUB(self, cuadruplo):
		self.currentCuad = cuadruplo[3]-1
		self.memoriaFuncion = self.memoriaLlamada
		self.memoriaTemporales = self.creaLista(self.memACrear[1])

##########################
	def PARAM(self, cuadruplo):
		print(cuadruplo)
		print(self.currentCuad)
		self.setParam(cuadruplo[1], cuadruplo[3])

	def ENDPROC(self):
		pilaTemp = []
		pilaTemp.append(self.pilaDePausa.pop())
		self.memoriaFuncion = pilaTemp
		pilaTemp = []
		pilaTemp.append(self.pilaDePausaTemps.pop())
		self.memoriaTemporales = pilaTemp
		
##########################
	def RETURN(self, cuadruplo):
		pilaTemp = []
		pilaTemp.append(self.pilaDePausa.pop())
		self.memoriaFuncion = pilaTemp
		pilaTemp = []
		pilaTemp.append(self.pilaDePausaTemps.pop())
		self.memoriaTemporales = pilaTemp
		self.pilaRetorno.append(getValue(cuadruplo[2]))

	def WriteVar(self, cuadruplo):
		print(getValue(cuadruplo[1]))

	def ReadVar(self, cuadruplo):
		temp = input()
		print(setValue(cuadruplo[3], cuadruplo[1]))

	def creaLista(self, tam):
		lista = [None] * tam
		return lista
		
	def run(self):
		while self.cuadruplos[self.currentCuad][0] != 'EXIT':
			cuadruplo = self.cuadruplos[self.currentCuad]
			operacion = cuadruplo[0]
			if operacion == 'GoTo':
				self.GoTo(cuadruplo)
			elif operacion == 'GoToF':
				self.GoToF(cuadruplo)
			elif operacion == 'GoToV':
				self.GoToV(cuadruplo)
			elif operacion == 'ERA':
				self.ERA(cuadruplo)
			elif operacion == 'GOSUB':
				self.GOSUB(cuadruplo)
			elif operacion == 'ENDPROC':
				self.ENDPROC(cuadruplo)
			elif operacion == 'PARAM':
				self.PARAM(cuadruplo)
			elif operacion == 'RETURN':
				self.RETURN(cuadruplo)
			# elif operacion == 'verify':
			#     self.verify()
			elif operacion == '+' or operacion == '-' or operacion == '*' or operacion == '<<' or operacion == '>>' or operacion == '^' or operacion == '&' or operacion == '|':
				self.opArit(cuadruplo)
			elif operacion == '+=' or operacion == '-=' or operacion == '*=' or operacion == '<<=' or operacion == '>>=' or operacion == '^=' or operacion == '&=' or operacion == '|=':
				self.opAritIgual(cuadruplo)
			elif operacion == '/' or operacion == '%':
				self.opWithDiv(cuadruplo)
			elif operacion == '/=' or operacion == '%=':
				self.opWithDivIgual(cuadruplo)
			elif  operacion == '&&' or operacion == '||' or operacion == '<' or operacion == '<=' or operacion == '>' or operacion == '>=' or operacion == '!=' or operacion == '==':
				self.opLogic(cuadruplo)
			elif operacion == '=':
				self.asign(cuadruplo)
			elif operacion == 'WRITE':
				self.WriteVar(cuadruplo)
			elif operacion == 'READ':
				self.ReadVar(cuadruplo)
			else:
				print('ERROR, cuadruplo no acceptado: ')
				print(cuadruplo)
			self.currentCuad = self.currentCuad + 1
				# print(self.currentCuad)
			print(cuadruplo)

if __name__ == '__main__':
	maquina = CEldaMaquinaVirtual()
	maquina.run()
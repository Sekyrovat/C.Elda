#!/usr/bin/python3.7
#
# tablas.py
# Sergio López Madriz A01064725
# Héctor Hernández Morales A00816446

import json
from nodoDimension import NodoDimension

# Clase que contiene la informacion de las constantes que se usen en el codigo.
class TablaConstantes(object):
	"""docstring for TablaConstantes"""
	def __init__(self):
		# Se define como un diccionario vacio.
		self.tablaConstantes = {}

	# La funcion para agregar recibe el nombre, ti[p y valor de la constante que se defina
	def agregarATabla(self, nombre, tipo, valor):
		self.tablaConstantes[nombre] = (nombre, tipo, valor)

	# Funcion para obtener el valor, aprovechamos el funcionamiento de diciconario.
	def getValor(self, nombre):
		return self.tablaConstantes[nombre][2]
	
	def __str__(self):
		entradas = []
		for variable, datos in self.tablaConstantes.items():
			entradas.append(variable + " => (" + ', '.join(map(str, datos)) + ")")
		return '\n'.join(entradas)

class TablaVariables:
	"""docstring for TablaVariables"""
	def __init__(self):
		# Se define como un diccionario vacio
		self.tablaVariables = {}
	
	def agregarATabla(self, nombre, tipo, direccion, tamDimensiones):
		# Debemos ver si el tamanio es igual a 0 para agregar la primer variable
		if len(tamDimensiones) == 0:
			self.tablaVariables[nombre] = (nombre, tipo, direccion, None)
		# De lo contrario generamos un nodo y buscamos si existe en la tabla
		# Si existe indicamos que existe y lo tratamos en la ubicacion existente
		# De lo contrario tomamos la posicion final de la tabla para agregarlo.
		else:
			nodo = None
			for tamano in tamDimensiones[::-1]:
				if nodo == None:
					nodo = NodoDimension(tamano)
				else:
					nodo = NodoDimension(tamano, nodo)
			self.tablaVariables[nombre] = (nombre, tipo, direccion, nodo)

	def variableExiste(self, nombre):
		return nombre in self.tablaVariables

	# Funcion para consegui la direccion de la variable que se nos indica.
	def conseguirDireccion(self, nombre, *accesos):
		if len(accesos) == 0:
			return self.tablaVariables[nombre][2]
		else:
			InfoDimension = self.tablaVariables[nombre][3]
			desplazamiento = 0
			for entrada in accesos:
				# Debemos verficar que la entrada no sea mayor al tamanio.
				if entrada >= InfoDimension.tamano:
					pass # error index ouf of bounds
				# Debemos obtener el desplazamiento adecuado para obtener la direccion adecuada.
				desplazamiento += int(entrada) * InfoDimension.m
				InfoDimension = InfoDimension.next
			return self.tablaVariables[nombre][2] + desplazamiento

	def __str__(self):
		entradas = []
		for variable, datos in self.tablaVariables.items():
			entradas.append(variable + " => (" + ', '.join(map(str, datos)) + ")")
		return '\n'.join(entradas)

class TablaModulos:
	"""docstring for TablaModulos"""
	def __init__(self):
		# Se define como un diccionario vacio
		self.tablaModulos = {}

	def agregarPrototipo(self, nombre, tipo, argumentos):
		self.tablaModulos[nombre] = (nombre, tipo, argumentos)

	def checarFirma(self, nombre, tipo, argumentos):
		return self.tablaModulos[nombre] == (nombre, tipo, argumentos)
		
	def agregarATabla(self, nombre, tipo, direccion, argumentos, tablaVariables):
		self.tablaModulos[nombre] = (nombre, tipo, direccion, argumentos, tablaVariables)

	def agregarTamanosMemoria(self, nombre, memoriaVariables, numeroTemporales):
		self.tablaModulos[nombre] += (memoriaVariables, numeroTemporales)

	def funcionExiste(self, nombre):
		return nombre in self.tablaModulos

	# Funcion para consegui la direccion de la variable que se nos indica.
	def conseguirDireccion(self, nombre):
		return self.tablaModulos[nombre][2]

	def creaReduccion(self):
		reduccion = {}
		for key, data in self.tablaModulos.items():
			reduccion[key] = data[5:7]
		return reduccion

	def __str__(self):
		entradas = []
		for variable, datos in self.tablaModulos.items():
			entradas.append(variable + " => (" + ', '.join(map(str, datos)) + ")")
		return '\n'.join(entradas)

#!/usr/bin/python3.7
#
# tablas.py
# Sergio López Madriz A01064725
# Héctor Hernández Morales A00816446

import json
from nodoDimension import NodoDimension

class TablaConstantes(object):
	"""docstring for TablaConstantes"""
	def __init__(self):
		self.tablaConstantes = {}

	def agregarATabla(self, nombre, tipo, valor):
		self.tablaConstantes[nombre] = (nombre, tipo, valor)

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
		self.tablaVariables = {}
	
	def agregarATabla(self, nombre, tipo, direccion, *tamDimensiones):
		if len(tamDimensiones) == 0:
			self.tablaVariables[nombre] = (nombre, tipo, direccion, None)
		else:
			nodo = None
			for tamano in tamDimensiones[::-1]:
				if nodo == None:
					nodo = NodoDimension(tamano)
				else:
					nodo = NodoDimension(tamano, nodo)
			self.tablaVariables[nombre] = (nombre, tipo, direccion, nodo)

	def conseguirDireccion(self, nombre, *accesos):
		if len(accesos) == 0:
			return self.tablaVariables[nombre][2]
		else:
			InfoDimension = self.tablaVariables[nombre][3]
			desplazamiento = 0
			for entrada in accesos:
				if entrada >= InfoDimension.tamano:
					pass # error index ouf of bounds
				desplazamiento += int(entrada) * InfoDimension.m
				InfoDimension = InfoDimension.next
			return self.tablaVariables[nombre][2] + desplazamiento

	def __str__(self):
		entradas = []
		for variable, datos in self.tablaVariables.items():
			entradas.append(variable + " => (" + ', '.join(map(str, datos)) + ")")
		return '\n'.join(entradas)

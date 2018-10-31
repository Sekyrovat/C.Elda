from NodoDimension import NodoDimension

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

	def __str__(self):
		toString = ""
		for variable, datos in self.tablaVariables.items():
			toString += variable + " => (" + ', '.join(map(str, datos)) + ")\n"
		return toString

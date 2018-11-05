#!/usr/bin/python
#
# cuadruplos.py
# Sergio López Madriz A01064725
# Héctor Hernández Morales A00816446

class Cuadruplos(object):
	"""docstring for Cuadruplos"""
	def __init__(self):
		self.cuadruplos = []
	
	def generaCuadruplo(self, operacion, operando1, operando2, resultado):
		self.cuadruplos.append((operacion, operando1, operando2, resultado))

	def rellenaGoTo(self, numeroCuadruplo, direccionDeSalto):
		self.cuadruplos[numeroCuadruplo] = self.cuadruplos[numeroCuadruplo][0:3] + (direccionDeSalto,)

	def __str__(self):
		return '\n'.join(map(str, self.cuadruplos))



if __name__ == '__main__':
	cuadruplos = Cuadruplos()
	cuadruplos.generaCuadruplo('*', '87', '2', 't2')
	cuadruplos.generaCuadruplo('GoTo', 't2', None, None)
	print(cuadruplos)
	cuadruplos.rellenaGoTo(1, 200)
	print(cuadruplos)
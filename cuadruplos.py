#!/usr/bin/python3.7
#
# cuadruplos.py
# Sergio López Madriz A01064725
# Héctor Hernández Morales A00816446

def toStringHelper(string):
	return  string[1:-1]

class Cuadruplos(object):
	"""docstring for Cuadruplos"""
	def __init__(self):
		self.cuadruplos = []
		self.enEspera = []
	
	def generaCuadruplo(self, operacion, operando1, operando2, resultado):
		self.cuadruplos.append((operacion, operando1, operando2, resultado))

	def rellena(self, numeroCuadruplo, valor):
		self.cuadruplos[numeroCuadruplo] = self.cuadruplos[numeroCuadruplo][0:3] + (valor,)

	def agregaCapaEspera(self):
		self.enEspera.append([])

	def generaEnEspera(self, operacion, operando1, operando2, resultado):
		self.enEspera[-1].append((operacion, operando1, operando2, resultado))

	def liberaEspera(self):
		espera = self.enEspera.pop()
		self.cuadruplos.extend(espera)
		return len(espera)

	def __str__(self):
		return '\n'.join(map(toStringHelper, map(str, enumerate(self.cuadruplos))))



if __name__ == '__main__':
	cuadruplos = Cuadruplos()
	cuadruplos.generaCuadruplo('*', '87', '2', 't2')
	cuadruplos.generaCuadruplo('GoTo', 't2', None, None)
	print(cuadruplos)
	cuadruplos.rellena(1, 200)
	print(cuadruplos)
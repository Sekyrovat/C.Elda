#!/usr/bin/python3.7
#
# cuboSemantico.py
# Sergio López Madriz A01064725
# Héctor Hernández Morales A00816446


'''
	Cubo para manejo de ternarios, donde la primer llave es el operando izquierdo
	la segunda llave es el operando derecho y el valor sera el tipo de retorno que
	tenemos.
'''
cuboTernario = {
	'int' : {
		'int' 	: 'int',
		'char' 	: 'int',
		'bool' 	: 'int',
		'float' : 'float',
		'string': 'error'
	},
	'char' : {
		'int' 	: 'int',
		'char' 	: 'char',
		'bool' 	: 'char',
		'float' : 'float',
		'string': 'error'
	},
	'bool' : {
		'int' 	: 'int',
		'char' 	: 'char',
		'bool' 	: 'bool',
		'float' : 'float',
		'string': 'error'
	},
	'float' : {
		'int' : 'float',
		'char' : 'float',
		'bool' : 'float',
		'float' : 'float',
		'string' : 'error'
	},
	'string' : {
		'int' : 'error',
		'char' : 'error',
		'bool' : 'error',
		'float' : 'error',
		'string' : 'string'
	}
}

'''
	Cubo para manejo de operaciones de 1 solo operando, donde la primer llave es la operacion
	la segunda llave es el operando y el valor sera el tipo de retorno que tenemos.
'''
cubo1Operando = {
	'++' : {
		'int' 	: 'int',
		'char' 	: 'int',
		'bool' 	: 'int',
		'float' : 'float',
		'string': 'error'
	},
	'--' : {
		'int' 	: 'int',
		'char' 	: 'int',
		'bool' 	: 'int',
		'float' : 'float',
		'string': 'error'
	},
	'!' : {
		'int' 	: 'int',
		'char' 	: 'int',
		'bool' 	: 'int',
		'float' : 'float',
		'string': 'error'
	},
	'-' : {
		'int' 	: 'int',
		'char' 	: 'error',
		'bool' 	: 'int',
		'float' : 'float',
		'string': 'error'
	},
	'~' : {
		'int' 	: 'int',
		'char' 	: 'int',
		'bool' 	: 'int',
		'float' : 'float',
		'string': 'error'
	}
}

'''
	Cubo para manejo de operaciones, donde la primer llave es la oepracion que se 
	desea realizar, la segunda llave es el operando izquierdo asi como la tercera
	 y el valor sera el tipo de retorno que se dara.
'''
cubo2Operandos = {
	'+' : {
		'int' : {
			'int' 	: 'int',
			'char' 	: 'int',
			'bool' 	: 'int',
			'float' : 'float',
			'string': 'error'
		},
		'char' : {
			'int' 	: 'int',
			'char' 	: 'int',
			'bool' 	: 'int',
			'float' : 'float',
			'string': 'error'
		},
		'bool' : {
			'int' 	: 'int',
			'char' 	: 'int',
			'bool' 	: 'int',
			'float' : 'float',
			'string': 'error'
		},
		'float' : {
			'int' : 'float',
			'char' : 'float',
			'bool' : 'float',
			'float' : 'float',
			'string' : 'error'
		},
		'string' : {
			'int' : 'string',
			'char' : 'string',
			'bool' : 'string',
			'float' : 'string',
			'string' : 'string'
		}
	},

	'-' : {
		'int' : {
			'int' : 'int',
			'char' : 'int',
			'bool' : 'int',
			'float' : 'float',
			'string' : 'error'
		},
		'char' : {
			'int' : 'int',
			'char' : 'int',
			'bool' : 'int',
			'float' : 'float',
			'string' : 'error'
		},
		'bool' : {
			'int' : 'int',
			'char' : 'int',
			'bool' : 'int',
			'float' : 'float',
			'string' : 'error'
		},
		'float' : {
			'int' : 'float',
			'char' : 'float',
			'bool' : 'float',
			'float' : 'float',
			'string' : 'error'
		},
		'string' : {
			'int' : 'error',
			'char' : 'error',
			'bool' : 'error',
			'float' : 'error',
			'string' : 'error'
		}
	},

	'*' : {
		'int' : {
			'int' : 'int',
			'char' : 'int',
			'bool' : 'int',
			'float' : 'float',
			'string' : 'error'
		},
		'char' : {
			'int' : 'int',
			'char' : 'int',
			'bool' : 'int',
			'float' : 'float',
			'string' : 'error'
		},
		'bool' : {
			'int' : 'int',
			'char' : 'int',
			'bool' : 'int',
			'float' : 'float',
			'string' : 'error'
		},
		'float' : {
			'int' : 'float',
			'char' : 'float',
			'bool' : 'float',
			'float' : 'float',
			'string' : 'error'
		},
		'string' : {
			'int' : 'error',
			'char' : 'error',
			'bool' : 'error',
			'float' : 'error',
			'string' : 'error'
		}
	},

	'/' : {
		'int' : {
			'int' : 'int',
			'char' : 'int',
			'bool' : 'int',
			'float' : 'float',
			'string' : 'error'
		},
		'char' : {
			'int' : 'int',
			'char' : 'int',
			'bool' : 'int',
			'float' : 'float',
			'string' : 'error'
		},
		'bool' : {
			'int' : 'int',
			'char' : 'int',
			'bool' : 'int',
			'float' : 'float',
			'string' : 'error'
		},
		'float' : {
			'int' : 'float',
			'char' : 'float',
			'bool' : 'float',
			'float' : 'float',
			'string' : 'error'
		},
		'string' : {
			'int' : 'error',
			'char' : 'error',
			'bool' : 'error',
			'float' : 'error',
			'string' : 'error'
		}
	},

	'%' : {
		'int' : {
			'int' : 'int',
			'char' : 'int',
			'bool' : 'int',
			'float' : 'error',
			'string' : 'error'
		},
		'char' : {
			'int' : 'int',
			'char' : 'int',
			'bool' : 'int',
			'float' : 'error',
			'string' : 'error'
		},
		'bool' : {
			'int' : 'int',
			'char' : 'int',
			'bool' : 'int',
			'float' : 'error',
			'string' : 'error'
		},
		'float' : {
			'int' : 'int',
			'char' : 'int',
			'bool' : 'int',
			'float' : 'error',
			'string' : 'error'
		},
		'string' : {
			'int' : 'error',
			'char' : 'error',
			'bool' : 'error',
			'float' : 'error',
			'string' : 'error'
		}
	},

	'!=' : {
		'int' : {
			'int' : 'bool',
			'char' : 'bool',
			'bool' : 'bool',
			'float' : 'bool',
			'string' : 'error'
		},
		'char' : {
			'int' : 'bool',
			'char' : 'bool',
			'bool' : 'bool',
			'float' : 'bool',
			'string' : 'error'
		},
		'bool' : {
			'int' : 'bool',
			'char' : 'bool',
			'bool' : 'bool',
			'float' : 'bool',
			'string' : 'error'
		},
		'float' : {
			'int' : 'bool',
			'char' : 'bool',
			'bool' : 'bool',
			'float' : 'bool',
			'string' : 'error'
		},
		'string' : {
			'int' : 'error',
			'char' : 'error',
			'bool' : 'error',
			'float' : 'error',
			'string' : 'error'
		}
	},

	'==' : {
		'int' : {
			'int' : 'bool',
			'char' : 'bool',
			'bool' : 'bool',
			'float' : 'bool',
			'string' : 'error'
		},
		'char' : {
			'int' : 'bool',
			'char' : 'bool',
			'bool' : 'bool',
			'float' : 'bool',
			'string' : 'error'
		},
		'bool' : {
			'int' : 'bool',
			'char' : 'bool',
			'bool' : 'bool',
			'float' : 'bool',
			'string' : 'error'
		},
		'float' : {
			'int' : 'bool',
			'char' : 'bool',
			'bool' : 'bool',
			'float' : 'bool',
			'string' : 'error'
		},
		'string' : {
			'int' : 'error',
			'char' : 'error',
			'bool' : 'error',
			'float' : 'error',
			'string' : 'error'
		}
	},

	'=' : {
		'int' : {
			'int' : 'int',
			'char' : 'int',
			'bool' : 'int',
			'float' : 'int',
			'string' : 'error'
		},
		'char' : {
			'int' : 'int',
			'char' : 'int',
			'bool' : 'int',
			'float' : 'int',
			'string' : 'error'
		},
		'bool' : {
			'int' : 'int',
			'char' : 'int',
			'bool' : 'int',
			'float' : 'int',
			'string' : 'error'
		},
		'float' : {
			'int' : 'float',
			'char' : 'float',
			'bool' : 'float',
			'float' : 'float',
			'string' : 'error'
		},
		'string' : {
			'int' : 'string',
			'float' : 'string',
			'string' : 'string'
		}
	},

	'&&' : {
		'int' : {
			'int' : 'bool',
			'char' : 'bool',
			'bool' : 'bool',
			'float' : 'bool',
			'string' : 'error'
		},
		'char' : {
			'int' : 'bool',
			'char' : 'bool',
			'bool' : 'bool',
			'float' : 'bool',
			'string' : 'error'
		},
		'bool' : {
			'int' : 'bool',
			'char' : 'bool',
			'bool' : 'bool',
			'float' : 'bool',
			'string' : 'error'
		},
		'float' : {
			'int' : 'bool',
			'char' : 'bool',
			'bool' : 'bool',
			'float' : 'bool',
			'string' : 'error'
		},
		'string' : {
			'int' : 'error',
			'char' : 'error',
			'bool' : 'error',
			'float' : 'error',
			'string' : 'error'
		}
	},

	'||' : {
		'int' : {
			'int' : 'bool',
			'char' : 'bool',
			'bool' : 'bool',
			'float' : 'bool',
			'string' : 'error'
		},
		'char' : {
			'int' : 'bool',
			'char' : 'bool',
			'bool' : 'bool',
			'float' : 'bool',
			'string' : 'error'
		},
		'bool' : {
			'int' : 'bool',
			'char' : 'bool',
			'bool' : 'bool',
			'float' : 'bool',
			'string' : 'error'
		},
		'float' : {
			'int' : 'bool',
			'char' : 'bool',
			'bool' : 'bool',
			'float' : 'bool',
			'string' : 'error'
		},
		'string' : {
			'int' : 'error',
			'char' : 'error',
			'bool' : 'error',
			'float' : 'error',
			'string' : 'error'
		}
	},
	
	'<' : {
		'int' : {
			'int' : 'bool',
			'char' : 'bool',
			'bool' : 'bool',
			'float' : 'bool',
			'string' : 'error'
		},
		'char' : {
			'int' : 'bool',
			'char' : 'bool',
			'bool' : 'bool',
			'float' : 'bool',
			'string' : 'error'
		},
		'bool' : {
			'int' : 'bool',
			'char' : 'bool',
			'bool' : 'bool',
			'float' : 'bool',
			'string' : 'error'
		},
		'float' : {
			'int' : 'bool',
			'char' : 'bool',
			'bool' : 'bool',
			'float' : 'bool',
			'string' : 'error'
		},
		'string' : {
			'int' : 'error',
			'char' : 'error',
			'bool' : 'error',
			'float' : 'error',
			'string' : 'error'
		}
	},
	
	'>' : {
		'int' : {
			'int' : 'bool',
			'char' : 'bool',
			'bool' : 'bool',
			'float' : 'bool',
			'string' : 'error'
		},
		'char' : {
			'int' : 'bool',
			'char' : 'bool',
			'bool' : 'bool',
			'float' : 'bool',
			'string' : 'error'
		},
		'bool' : {
			'int' : 'bool',
			'char' : 'bool',
			'bool' : 'bool',
			'float' : 'bool',
			'string' : 'error'
		},
		'float' : {
			'int' : 'bool',
			'char' : 'bool',
			'bool' : 'bool',
			'float' : 'bool',
			'string' : 'error'
		},
		'string' : {
			'int' : 'error',
			'char' : 'error',
			'bool' : 'error',
			'float' : 'error',
			'string' : 'error'
		}
	},
	
	'<=' : {
		'int' : {
			'int' : 'bool',
			'char' : 'bool',
			'bool' : 'bool',
			'float' : 'bool',
			'string' : 'error'
		},
		'char' : {
			'int' : 'bool',
			'char' : 'bool',
			'bool' : 'bool',
			'float' : 'bool',
			'string' : 'error'
		},
		'bool' : {
			'int' : 'bool',
			'char' : 'bool',
			'bool' : 'bool',
			'float' : 'bool',
			'string' : 'error'
		},
		'float' : {
			'int' : 'bool',
			'char' : 'bool',
			'bool' : 'bool',
			'float' : 'bool',
			'string' : 'error'
		},
		'string' : {
			'int' : 'error',
			'char' : 'error',
			'bool' : 'error',
			'float' : 'error',
			'string' : 'error'
		}
	},
	
	'>=' : {
		'int' : {
			'int' : 'bool',
			'char' : 'bool',
			'bool' : 'bool',
			'float' : 'bool',
			'string' : 'error'
		},
		'char' : {
			'int' : 'bool',
			'char' : 'bool',
			'bool' : 'bool',
			'float' : 'bool',
			'string' : 'error'
		},
		'bool' : {
			'int' : 'bool',
			'char' : 'bool',
			'bool' : 'bool',
			'float' : 'bool',
			'string' : 'error'
		},
		'float' : {
			'int' : 'bool',
			'char' : 'bool',
			'bool' : 'bool',
			'float' : 'bool',
			'string' : 'error'
		},
		'string' : {
			'int' : 'error',
			'char' : 'error',
			'bool' : 'error',
			'float' : 'error',
			'string' : 'error'
		}
	},
	
	'&' : {
		'int' : {
			'int' : 'int',
			'char' : 'int',
			'bool' : 'int',
			'float' : 'error',
			'string' : 'error'
		},
		'char' : {
			'int' : 'int',
			'char' : 'int',
			'bool' : 'int',
			'float' : 'error',
			'string' : 'error'
		},
		'bool' : {
			'int' : 'int',
			'char' : 'int',
			'bool' : 'int',
			'float' : 'error',
			'string' : 'error'
		},
		'float' : {
			'int' : 'error',
			'char' : 'error',
			'bool' : 'error',
			'float' : 'error',
			'string' : 'error'
		},
		'string' : {
			'int' : 'error',
			'char' : 'error',
			'bool' : 'error',
			'float' : 'error',
			'string' : 'error'
		}
	},
	
	'|' : {
		'int' : {
			'int' : 'int',
			'char' : 'int',
			'bool' : 'int',
			'float' : 'error',
			'string' : 'error'
		},
		'char' : {
			'int' : 'int',
			'char' : 'int',
			'bool' : 'int',
			'float' : 'error',
			'string' : 'error'
		},
		'bool' : {
			'int' : 'int',
			'char' : 'int',
			'bool' : 'int',
			'float' : 'error',
			'string' : 'error'
		},
		'float' : {
			'int' : 'error',
			'char' : 'error',
			'bool' : 'error',
			'float' : 'error',
			'string' : 'error'
		},
		'string' : {
			'int' : 'error',
			'char' : 'error',
			'bool' : 'error',
			'float' : 'error',
			'string' : 'error'
		}
	},
	
	'^' : {
		'int' : {
			'int' : 'int',
			'char' : 'int',
			'bool' : 'int',
			'float' : 'error',
			'string' : 'error'
		},
		'char' : {
			'int' : 'int',
			'char' : 'int',
			'bool' : 'int',
			'float' : 'error',
			'string' : 'error'
		},
		'bool' : {
			'int' : 'int',
			'char' : 'int',
			'bool' : 'int',
			'float' : 'error',
			'string' : 'error'
		},
		'float' : {
			'int' : 'error',
			'char' : 'error',
			'bool' : 'error',
			'float' : 'error',
			'string' : 'error'
		},
		'string' : {
			'int' : 'error',
			'char' : 'error',
			'bool' : 'error',
			'float' : 'error',
			'string' : 'error'
		}
	},
	
	'<<' : {
		'int' : {
			'int' : 'int',
			'char' : 'int',
			'bool' : 'int',
			'float' : 'error',
			'string' : 'error'
		},
		'char' : {
			'int' : 'int',
			'char' : 'int',
			'bool' : 'int',
			'float' : 'error',
			'string' : 'error'
		},
		'bool' : {
			'int' : 'int',
			'char' : 'int',
			'bool' : 'int',
			'float' : 'error',
			'string' : 'error'
		},
		'float' : {
			'int' : 'error',
			'char' : 'error',
			'bool' : 'error',
			'float' : 'error',
			'string' : 'error'
		},
		'string' : {
			'int' : 'error',
			'char' : 'error',
			'bool' : 'error',
			'float' : 'error',
			'string' : 'error'
		}
	},
	
	'>>' : {
		'int' : {
			'int' : 'int',
			'char' : 'int',
			'bool' : 'int',
			'float' : 'error',
			'string' : 'error'
		},
		'char' : {
			'int' : 'int',
			'char' : 'int',
			'bool' : 'int',
			'float' : 'error',
			'string' : 'error'
		},
		'bool' : {
			'int' : 'int',
			'char' : 'int',
			'bool' : 'int',
			'float' : 'error',
			'string' : 'error'
		},
		'float' : {
			'int' : 'error',
			'char' : 'error',
			'bool' : 'error',
			'float' : 'error',
			'string' : 'error'
		},
		'string' : {
			'int' : 'error',
			'char' : 'error',
			'bool' : 'error',
			'float' : 'error',
			'string' : 'error'
		}
	}
}

# Las sigueintes son funciones de acceso

def verificaSemantica2Operandos(operacion, izq, der):
	return cubo2Operandos[operacion][izq][der]

def verificaSemantica1Operando(operacion, operando):
	return cubo1Operando[operacion][operando]

def verificaSemanticaTernario(izq, der):
	return cuboTernario[izq][der]

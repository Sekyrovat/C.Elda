#!/usr/bin/python3.7
#
# cuboSemantico.py
# Sergio López Madriz A01064725
# Héctor Hernández Morales A00816446

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

def verificaSemantica2Operandos(operacion, izq, der):
	return cubo2Operandos[operacion][izq][der]

def verificaSemantica1Operando(operacion, operando):
	return cubo1Operando[operacion][operando]

def verificaSemanticaTernario(izq, der):
	return cuboTernario[izq][der]

class CuboSemantico:
	"""docstring for CuboSemantico"""
	def __init__(self):
		self.cubo1Operando = {
			'++' : {
				'int' 	: 'integer',
				'char' 	: 'integer',
				'bool' 	: 'integer',
				'float' : 'float',
				'string': 'error'
			},
			'--' : {
				'int' 	: 'integer',
				'char' 	: 'integer',
				'bool' 	: 'integer',
				'float' : 'float',
				'string': 'error'
			},
			'!' : {
				'int' 	: 'integer',
				'char' 	: 'integer',
				'bool' 	: 'integer',
				'float' : 'float',
				'string': 'error'
			},
			'-' : {
				'int' 	: 'integer',
				'char' 	: 'error',
				'bool' 	: 'integer',
				'float' : 'float',
				'string': 'error'
			},
			'~' : {
				'int' 	: 'integer',
				'char' 	: 'integer',
				'bool' 	: 'integer',
				'float' : 'float',
				'string': 'error'
			}
		}

		self.cubo2Operandos = {
			'+' : {
				'int' : {
					'int' 	: 'integer',
					'char' 	: 'integer',
					'bool' 	: 'integer',
					'float' : 'float',
					'string': 'error'
				},
				'char' : {
					'int' 	: 'integer',
					'char' 	: 'integer',
					'bool' 	: 'integer',
					'float' : 'float',
					'string': 'error'
				},
				'bool' : {
					'int' 	: 'integer',
					'char' 	: 'integer',
					'bool' 	: 'integer',
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
					'int' : 'integer',
					'char' : 'integer',
					'bool' : 'integer',
					'float' : 'float',
					'string' : 'error'
				},
				'char' : {
					'int' : 'integer',
					'char' : 'integer',
					'bool' : 'integer',
					'float' : 'float',
					'string' : 'error'
				},
				'bool' : {
					'int' : 'integer',
					'char' : 'integer',
					'bool' : 'integer',
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
					'int' : 'integer',
					'char' : 'integer',
					'bool' : 'integer',
					'float' : 'float',
					'string' : 'error'
				},
				'char' : {
					'int' : 'integer',
					'char' : 'integer',
					'bool' : 'integer',
					'float' : 'float',
					'string' : 'error'
				},
				'bool' : {
					'int' : 'integer',
					'char' : 'integer',
					'bool' : 'integer',
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
					'int' : 'integer',
					'char' : 'integer',
					'bool' : 'integer',
					'float' : 'float',
					'string' : 'error'
				},
				'char' : {
					'int' : 'integer',
					'char' : 'integer',
					'bool' : 'integer',
					'float' : 'float',
					'string' : 'error'
				},
				'bool' : {
					'int' : 'integer',
					'char' : 'integer',
					'bool' : 'integer',
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
					'int' : 'integer',
					'char' : 'integer',
					'bool' : 'integer',
					'float' : 'error',
					'string' : 'error'
				},
				'char' : {
					'int' : 'integer',
					'char' : 'integer',
					'bool' : 'integer',
					'float' : 'error',
					'string' : 'error'
				},
				'bool' : {
					'int' : 'integer',
					'char' : 'integer',
					'bool' : 'integer',
					'float' : 'error',
					'string' : 'error'
				},
				'float' : {
					'int' : 'integer',
					'char' : 'integer',
					'bool' : 'integer',
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
					'int' : 'integer',
					'char' : 'integer',
					'bool' : 'integer',
					'float' : 'integer',
					'string' : 'error'
				},
				'char' : {
					'int' : 'integer',
					'char' : 'integer',
					'bool' : 'integer',
					'float' : 'integer',
					'string' : 'error'
				},
				'bool' : {
					'int' : 'integer',
					'char' : 'integer',
					'bool' : 'integer',
					'float' : 'integer',
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
					'int' : 'integer',
					'char' : 'integer',
					'bool' : 'integer',
					'float' : 'error',
					'string' : 'error'
				},
				'char' : {
					'int' : 'integer',
					'char' : 'integer',
					'bool' : 'integer',
					'float' : 'error',
					'string' : 'error'
				},
				'bool' : {
					'int' : 'integer',
					'char' : 'integer',
					'bool' : 'integer',
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
					'int' : 'integer',
					'char' : 'integer',
					'bool' : 'integer',
					'float' : 'error',
					'string' : 'error'
				},
				'char' : {
					'int' : 'integer',
					'char' : 'integer',
					'bool' : 'integer',
					'float' : 'error',
					'string' : 'error'
				},
				'bool' : {
					'int' : 'integer',
					'char' : 'integer',
					'bool' : 'integer',
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
					'int' : 'integer',
					'char' : 'integer',
					'bool' : 'integer',
					'float' : 'error',
					'string' : 'error'
				},
				'char' : {
					'int' : 'integer',
					'char' : 'integer',
					'bool' : 'integer',
					'float' : 'error',
					'string' : 'error'
				},
				'bool' : {
					'int' : 'integer',
					'char' : 'integer',
					'bool' : 'integer',
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
					'int' : 'integer',
					'char' : 'integer',
					'bool' : 'integer',
					'float' : 'error',
					'string' : 'error'
				},
				'char' : {
					'int' : 'integer',
					'char' : 'integer',
					'bool' : 'integer',
					'float' : 'error',
					'string' : 'error'
				},
				'bool' : {
					'int' : 'integer',
					'char' : 'integer',
					'bool' : 'integer',
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
					'int' : 'integer',
					'char' : 'integer',
					'bool' : 'integer',
					'float' : 'error',
					'string' : 'error'
				},
				'char' : {
					'int' : 'integer',
					'char' : 'integer',
					'bool' : 'integer',
					'float' : 'error',
					'string' : 'error'
				},
				'bool' : {
					'int' : 'integer',
					'char' : 'integer',
					'bool' : 'integer',
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

	def verificaSemantica2Operandos(self, operacion, izq, der):
		return self.cubo2Operandos[operacion][izq][der]

	def verificaSemantica1Operando(self,operacion,operando):
		return self.cubo1Operando[operacion][operando]

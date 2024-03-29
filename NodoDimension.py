#!/usr/bin/python3.7
#
# nodoDimension.py
# Sergio López Madriz A01064725
# Héctor Hernández Morales A00816446

class NodoDimension:
	def __init__(self, tamano, *nextNode):
		self.tamano = int(tamano)
		if len(nextNode) == 0:
			self.m = 1
			self.next = None
		elif len(nextNode) == 1 and isinstance(nextNode[0], NodoDimension):
			self.m = nextNode[0].tamano * nextNode[0].m
			self.next = nextNode[0]

	def __str__(self):
		return "tamano: " + str(self.tamano) + " m: " + str(self.m) + " next: (" + str(self.next) + ")"

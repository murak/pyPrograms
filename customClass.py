class A:
	def __init__(self, a, b):
		self.a = a
		self.b = b

	def __str__(self):
		return "(" + str(self.a) + "," + str(self.b) + ")"

	def __repr__(self):
		return "(" + str(self.a) + "," + str(self.b) + ")"


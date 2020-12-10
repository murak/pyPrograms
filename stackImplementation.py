class Stack:
	def __init__(self):
		self.list = []

	def isEmpty(self):
		return len(self.list) == 0

	def push(self, item):
		self.list.append(item)

	def pop(self):
		if len(self.list) == 0:
			print("stack is empty")
		else:
			return self.list.pop()

	def peek(self):
		if len(self.list) == 0:
			print("no item in stack")
		else:
			return self.list[-1]

	def size(self):
		return len(self.list)

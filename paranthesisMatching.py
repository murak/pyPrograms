# paranthesis matching

from stackImplementation import Stack

class ParanthesisMatching:

	def __init__(self):
		pass

	def isMatching(self, exp):
		if exp == None or len(exp) == 0:
			return True
		s = Stack()

		for ch in exp:
			if ch == '{' or ch == '[' or ch == '(':
				s.push(ch)
			else:
				if s.isEmpty():
					return False

				top = s.peek()
				if (ch == ']' and top == '[') or (ch == '}' and top == '{') or (ch == ')' and top == '('):
					s.pop()
				else:
					return False

		if s.isEmpty():
			return True

		return False

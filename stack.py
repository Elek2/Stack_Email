
class Stack:
	def __init__(self, st: list):
		self.st = st

	def __str__(self):
		return f"{self.st}"

	def __iter__(self):
		for elem in self.st:
			yield elem

	def is_empty(self):
		return len(self.st) == 0

	def push(self, arg):
		self.st.insert(0, arg)

	def pop(self):
		if len(self.st) != 0:
			return self.st.pop(0)
		else:
			return None

	def peek(self):
		if len(self.st) != 0:
			return self.st[0]
		else:
			return None

	def size(self):
		return len(self.st)


def brackets_check(_input):
	brackets = {
		")": "(",
		"]": "[",
		"}": "{",
	}
	stack = Stack([])

	for bracket in _input:
		if bracket in brackets.values():
			stack.push(bracket)
		elif brackets[bracket] == stack.peek():
			stack.pop()
		else:
			stack.push(bracket)
			break
	if stack.is_empty():
		return "Сбалансировано"
	else:
		return "Несбалансировано"


if __name__ == '__main__':

	inp = list(input("Введите стек: "))
	result = brackets_check(inp)
	print(result)



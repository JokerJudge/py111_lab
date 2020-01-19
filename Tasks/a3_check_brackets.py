def check_brackets(brackets_row: str) -> bool:
	"""
	Check whether input string is a valid bracket sequence
	Valid examples: "", "()", "()()(()())", invalid: "(", ")", ")("
	:param brackets_row: input string to be checked
	:return: True if valid, False otherwise
	"""
	counter_open = 0
	counter_close = 0
	# число скобок должно быть одинаковым
	# не может появиться закрывающая скобка перед открывающей
	for i in brackets_row:
		if i == "(":
			counter_open += 1
		elif i == ")":
			counter_close += 1
			if counter_close > counter_open:
				return False
	if counter_open == counter_close:
		return True
	else:
		return False

if __name__ == "__main__":
	pass
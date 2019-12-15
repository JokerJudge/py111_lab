"""
My little Stack
"""
from typing import Any

stack = []

def push(elem: Any) -> None:
	"""
	Operation that add element to stack

	:param elem: element to be pushed
	:return: Nothing
	"""
	print(elem)
	global stack
	stack.append(elem)
	return None


def pop() -> Any:
	"""
	Pop element from the top of the stack. If not elements - should return None.

	:return: popped element
	"""
	global stack
	if stack:
		a = stack[-1]
		stack.pop()
		return a
	else:
		return None


def peek(ind: int = 0) -> Any:
	"""
	Allow you to see at the element in the stack without popping it.

	:param ind: index of element (count from the top, 0 - top, 1 - first from top, etc.)
	:return: peeked element or None if no element in this place
	"""
	print(ind)
	global stack
	try:
		a = stack[len(stack) - 1 - ind]
		return a
	except:
		return None


def clear() -> None:
	"""
	Clear my stack

	:return: None
	"""
	global stack
	stack = []
	return None

if __name__ == "__main__":
	push(1)
	push(25)
	push(88)
	push(435)
	push(123)
	pop()
	peek(0)
	peek(2)
	peek(100)
	print(stack)
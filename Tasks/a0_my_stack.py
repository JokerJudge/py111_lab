"""
My little Stack
"""
from typing import Any

stack = [] # переменная стек
# последний элемент в списке будет первым

def push(elem: Any) -> None:
	"""
	Operation that add element to stack

	:param elem: element to be pushed
	:return: Nothing
	"""
	print("Добавили элемент {} в стек".format(elem))
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
		stack.pop()
	else:
		return None

	return None


def peek(ind: int = 0) -> Any:
    """
    Allow you to see at the element in the stack without popping it.

    :param ind: index of element (count from the top, 0 - top, 1 - first from top, etc.)
    :return: peeked element or None if no element in this place
    """
    #print(ind)

    global stack
    #print(stack)
    if stack:
        try:
            x = stack[len(stack) - 1 - ind]
            return x
        except:
            return None
    else:
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
    push(24)
    push(47)
    print(stack)
    pop()
    peek(0)
    peek(1)
    print(stack)
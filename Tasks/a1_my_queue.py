"""
My little Queue
"""
from typing import Any

queue = []

def enqueue(elem: Any) -> None:
	"""
	Operation that add element to the end of the queue

	:param elem: element to be added
	:return: Nothing
	"""
	print(elem)
	global queue
	queue.append(elem)
	return None


def dequeue() -> Any:
	"""
	Return element from the beginning of the queue. Should return None if no elements.

	:return: dequeued element
	"""
	global queue
	if queue:
		temp = queue[0]
		queue.remove(queue[0])
		return temp
	else:
		return None


def peek(ind: int = 0) -> Any:
	"""
	Allow you to see at the element in the queue without dequeuing it

	:param ind: index of element (count from the beginning)
	:return: peeked element
	"""
	print(ind)
	global queue
	if queue:
		try:
			return queue[ind]
		except IndexError:
			return None
	else:
		return None


def clear() -> None:
	"""
	Clear my queue

	:return: None
	"""
	global queue
	queue = []
	return None

if __name__ == "__main__":
	pass
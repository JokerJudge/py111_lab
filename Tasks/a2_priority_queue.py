"""
Priority Queue

Queue priorities are from 0 to 5
"""
from typing import Any

queue = []

def enqueue(elem: Any, priority: int = 0) -> None:
	"""
	Operation that add element to the end of the queue

	:param elem: element to be added
	:return: Nothing
	"""
	global queue
	queue.append((priority, elem))
	return None


def dequeue() -> Any:
	"""
	Return element from the beginning of the queue. Should return None if not elements.

	:return: dequeued element
	"""
	global queue
	min = 5
	if queue:
		for i in queue: # находим сначала минимальный приоритет
			if i[0] < min:
				min = i[0]
		for i in queue: # выбираем первый в списке элемент с минимальной очередью
			if i[0] == min:
				temp = i[1]
				queue.remove(i)
				return temp
	else:
		return None


def peek(ind: int = 0, priority: int = 0) -> Any:
	"""
	Allow you to see at the element in the queue without dequeuing it

	:param ind: index of element (count from the beginning)
	:return: peeked element
	"""
	global queue
	if queue:
		try:
			return queue[ind][1]
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

"""
Priority Queue

Queue priorities are from 0 to 5
"""
from typing import Any

queue = []
MIN_QUEUE_PRIORITY = 5

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
	global queue, MIN_QUEUE_PRIORITY
	min_ = MIN_QUEUE_PRIORITY
	min_res = None
	if queue:
		#for i in queue: # находим сначала минимальный приоритет
		#	if i[0] < min_:
		#		min_ = i[0]
		#for i in queue: # выбираем первый в списке элемент с минимальной очередью
		#	if i[0] == min_:
		#		temp = i[1]
		#		queue.remove(i)
		#		return temp
		for i in queue: # переделал. Теперь работает за один проход по циклу
			if i[0] < min_:
				min_ = i[0]
				min_res = i[1]
		temp = min_res
		queue.remove((min_, min_res))
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

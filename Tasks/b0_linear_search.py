"""
This module implements some functions based on linear search algo
"""
from typing import Sequence
import numpy as np
import time


def min_search(arr: Sequence) -> int:
	"""
	Function that find minimal element in array

	:param arr: Array containing numbers
	:return: index of first occurrence of minimal element in array
	"""
	print(arr)
	return -1

def t(fn):
	def wrapper(*args, **kwargs):
		start = time.time()
		result = fn(*args, **kwargs)
		finish = time.time()
		print(finish - start)
		return result
	return wrapper

@t
def finding_elem(find_elem, array):
	index = None
	for i, elem in enumerate(array):
		if elem == find_elem:
			index = i
			return index
	#if find_elem in array:
	#	return array.index(find_elem)

	return index



if __name__ == "__main__":
	n = 10000000
	array = np.arange(n)
	find_elem = np.random.choice(array)
	np.random.shuffle(array)
	print(finding_elem(find_elem, array))

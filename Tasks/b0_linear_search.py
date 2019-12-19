"""
This module implements some functions based on linear search algo
"""
from typing import Any, Sequence, Optional
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

@t
def binary_search(elem: Any, arr: Sequence) -> Optional[int]:
	"""
	Performs binary search of given element inside of array

	:param elem: element to be found
	:param arr: array where element is to be found
	:return: Index of element if it's presented in the arr, None otherwise
	"""
	arr = sorted(arr)
	left = 0
	right = len(arr) - 1
	if elem in arr:
		while True:
			if right - left == 1:
				if elem == arr[right]:
					return right
				elif elem == arr[left]:
					return left
				else:
					return None
			middle = (left + right) // 2
			if elem == arr[middle]:
				return middle
			else:
				if elem < arr[middle]:
					right = middle - 1
				elif elem > arr[middle]:
					left = middle + 1

	else:
		return None



if __name__ == "__main__":
	n = 1000000
	array = np.arange(n)
	find_elem = 200000
	np.random.shuffle(array)
	print(finding_elem(find_elem, array))
	print(binary_search(find_elem, array))

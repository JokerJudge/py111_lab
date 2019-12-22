"""
This module implements some functions based on linear search algo
"""
from typing import Sequence
import numpy as np

def min_search(arr: Sequence) -> int:
	"""
	Function that find minimal element in array

	:param arr: Array containing numbers
	:return: index of first occurrence of minimal element in array
	"""
	print(arr)
	temp_min = max(arr)
	min_index = None
	if arr:
		for i, elem in enumerate(arr):
			if elem < temp_min:
				temp_min = elem
				min_index = i
		return min_index
	else:
		return None

# все, что ниже - код, который писали на практическом занятии

def finding_elem(find_elem, array):
	index = None
	for i, elem in enumerate(array):
		if elem == find_elem:
			index = i
			return index

	return index

if __name__ == "__main__":
	n = 100
	array = np.arange(n)
	find_elem = 20
	np.random.shuffle(array)
	print(finding_elem(find_elem, array))
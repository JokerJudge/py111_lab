from typing import Any, Sequence, Optional
import numpy as np

def binary_search(elem: Any, arr: Sequence) -> Optional[int]:
	"""
	Performs binary search of given element inside of array

	:param elem: element to be found
	:param arr: array where element is to be found
	:return: Index of element if it's presented in the arr, None otherwise
	"""
	print(elem, arr)
    left = 0
    right = len(arr) - 1
    while True:



	return None


if __name__ == "__main__":
	n = 1000
	array = np.arange(n)
	some_elem = np.random.choice(array)
	np.random.shuffle(array)
	print(finding_elem(find_elem, array))
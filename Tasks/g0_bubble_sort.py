from typing import Collection, TypeVar

_Tt = TypeVar("_Tt")


def sort(container: Collection[_Tt]) -> Collection[_Tt]:
	"""
	Sort input container with bubble sort

	:param container: container of elements to be sorted
	:return: container sorted in ascending order
	"""
	'''

	index = 0
	while index < len(container):
		for i in range(len(container) - 1):
			if container[i] > container[i+1]:
				container[i], container[i+1] = container[i+1], container[i]
		index += 1

	return container
	'''
	'''
	# решение препода:
	def bubble_sort(array):
		for i in range(len(array)-1):
			for j in range(len(array) - i - 1):
				if sorted_array[j] > sorted_array[j + 1]:
					sorted_array[j], sorted_array[j + 1] = sorted_array[j + 1], sorted_array[j]
			return sorted_array
	'''





	'''
	# решение препода № 2:
	for i in range(len(container) - 1):
		for j in range(len(container) - 1 - i): # после каждого прохода уменьшаем на единичку, т.к. последний элемент в любом случае самый большой после первого проброса
			if container[j] > container[j + 1]:
				container[j], container[j+1] = container[j+1], container[j]
	return container
	'''

	# решение препода № 3:
	replace = 0
	for i in range(len(container) - 1):
		for j in range(len(container) - 1 - i): # после каждого прохода уменьшаем на единичку, т.к. последний элемент в любом случае самый большой после первого проброса
			if container[j] > container[j + 1]:
				container[j], container[j+1] = container[j+1], container[j]
				replace += 1
		print("Count replace: ", replace)
		replace = 0
	return container


if __name__ == "__main__":
	import random
	N = 5
	#shuffle_list = list(range(N))
	#shuffle_list = [1,0,4,2,3]
	#random.shuffle(shuffle_list)
	#print(shuffle_list)
	#print(sort(shuffle_list))
	#shuffle_list_2 = [0,1,2,3,4]
	shuffle_list_3 = [5,4,3,2,1,0]
	print(sort(shuffle_list_3))
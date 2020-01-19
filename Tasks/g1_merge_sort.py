from typing import Collection, TypeVar

_Tt = TypeVar("_Tt")


def sort(container: Collection[_Tt]) -> Collection[_Tt]:
	"""
	Sort input container with merge sort

	:param container: container of elements to be sorted
	:return: container sorted in ascending order
	"""
	'''
	#мое пока неудавшееся решение
	part_list = container[0:len(container)//2]
	part_list_2 = container[len(container)//2:]
	print(part_list)
	print(part_list_2)
	#while len(part_list) > 1:
	'''
	if len(container) <= 1:
		return container
	else:
		middle = len(container) // 2 # получим индекс середины
		print("=====")
		print("Common split")
		print("left container: ", container[:middle])
		print("right container: ", container[middle:])
		print("Split left container")
		left_container = sort(container[:middle]) # список должен быть отсортирован. Вызываем эту же функцию
		print("Split right container")
		right_container = sort(container[middle:]) # когда разделили до 1 элемента - начинаем сливать

	print("Merge", left_container, right_container)
	return merge(left_container, right_container)


def merge(left_container, right_container):
	sorted_ = []
	left_container_index = 0
	right_container_index = 0
	left_container_lenght = len(left_container)
	right_container_lenght = len(right_container)

	for _ in range(left_container_lenght + right_container_lenght):
		if (left_container_index < left_container_lenght) and (right_container_index < right_container_lenght):
			if left_container[left_container_index] <= right_container[right_container_index]:
				sorted_.append(left_container[left_container_index])
				left_container_index += 1
			else:
				sorted_.append(right_container[right_container_index])
				right_container_index += 1

		elif left_container_index == left_container_lenght:
			sorted_.append(right_container[right_container_index]) # или extend всей оставшейся части - нужно попробовать
			right_container_index += 1

		elif right_container_index == right_container_lenght:
			sorted_.append(left_container[left_container_index])
			left_container_index += 1

	print("Merged", sorted_)
	return sorted_

if __name__ == "__main__":
	list = [6, 5, 12, 10, 9, 1]
	print(list)
	print(sort(list))
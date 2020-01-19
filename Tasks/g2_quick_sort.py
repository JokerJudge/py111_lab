from typing import Collection, TypeVar

_Tt = TypeVar("_Tt")


def sort(container: Collection[_Tt]) -> Collection[_Tt]:
	"""
	Sort input container with quick sort

	:param container: container of elements to be sorted
	:return: container sorted in ascending order
	"""
	return container

def partition(array, low, high):
    # Выбираем средний элемент в качестве опорного
    # Также возможен выбор первого, последнего
    # или произвольного элементов в качестве опорного
    median = array[(low + high) // 2]
    left_list_index = low - 1
    right_list_index = high + 1
    while True:
        left_list_index += 1
        while array[left_list_index] < median:
            left_list_index += 1

        right_list_index -= 1
        while array[right_list_index] > median:
            right_list_index -= 1

        if left_list_index >= right_list_index:
            return right_list_index

        # Если элемент с индексом i (слева от опорного) больше, чем
        # элемент с индексом j (справа от опорного), меняем их местами
        array[left_list_index], array[right_list_index] = array[right_list_index], array[left_list_index]


def quick_sort(nums):
    # Создадим вспомогательную функцию, которая вызывается рекурсивно
    def _quick_sort(items, low, high):
        if low < high:
            # This is the index after the pivot, where our lists are split
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)


def qsort(L):
    if L:
        return qsort(list(filter(lambda x: x < L[0], L[1:]))) + L[0:1] + qsort(list(filter(lambda x: x >= L[0], L[1:])))
    return []
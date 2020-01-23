'''
Оценить асимптотическую сложность приведенного ниже алгоритма:
a = len(arr) - 1
out = list()
while a > 0:
    out.append(arr[a])
    a = a // 1.7
out.merge_sort()
'''

'''
Ответ:
Проходит по массиву за O(nlogn) < x < О(n)
Сортировка происходит за O(nlogn)

Общая сложность - O(nlogn) < x < О(n)

'''
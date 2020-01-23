'''
Сорт
Дано: массив из 10**6 целых чисел, каждое из которых лежит на отрезке [13, 25].
Задача: отсортировать массив наиболее эффективным способом
'''

# самый эффективный - counting sort (Роман говорил на лекции)
# работает не через сравнение, а через подсчет
import random

def counting_sort(array):
    d = {i: 0 for i in range(13, 26)}
    s = [i for i in range(13, 25)]
    print(d)
    for i in array:
        d[i] += 1
    print(d)
    result = []
    for i in s:
        result.extend([i] * d[i])

    return result



if __name__ == "__main__":
    N = 10**6
    list = [random.randint(13, 25) for _ in range(N)]
    print(list[:50])
    print(counting_sort(list))

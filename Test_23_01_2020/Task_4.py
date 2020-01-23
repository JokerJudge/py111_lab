'''
Навигатор на сетке.
Дана плоская квадратная двумерная сетка (массив), на которой определена стоимость захода в каждую ячейку
(все стоимости положительные). Необходимо найти путь минимальной стоимости из заданной ячейки
в заданную ячейку и вывести этот путь.
'''
# не сделал

import numpy as np

def calculate_paths(shape, scr: (int, int), dst: (int, int)):
    '''
    Ходить может только вниз и вправо

    :param shape: квадрат со стороной N
    :param scr: начальная точка
    :param dst: конечная точка
    :return:
    '''
    # F = np.zeros(shape, dtype=np.int32)
    F = np.zeros(shape)
    N = shape[0]  # строки
    M = shape[0]  # столбцы

    #point = (point[0] - 1, point[1] - 1)

    F[0, 0] = 1

    for i in range(shape[0]):  # проход по строкам
        for j in range(shape[1]):  # проход по столбцам
            if F[i, j] != 0:
                # на одну клетку вниз и две вправо
                if (i + 1 < N) and (j + 2 < M):
                    F[i + 1, j + 2] += F[i, j] * 2
                # на одну клетку вниз и две влево
                if (i + 1 < N) and (j - 2 >= 0):
                    F[i + 1, j - 2] += F[i, j] * 2
                # на две клетки вниз и одну вправо
                if (i + 2 < N) and (j + 1 < M):
                    F[i + 2, j + 1] += F[i, j] * 2
                # на две клетки вниз и одну влево
                if (i + 2 < N) and (j - 1 >= 0):
                    F[i + 2, j - 1] += F[i, j] * 2

    print(F)

    return F[point[0], point[1]]


if __name__ == "__main__":
    N = 4
    M = 4
    scr = (0, 0)
    point = (4, 3)

    print(calculate_paths((N, M), scr, point))
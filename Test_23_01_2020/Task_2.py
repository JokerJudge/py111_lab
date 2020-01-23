'''
Считалочка
Дано N человек, считалка из K слогов. Считалка начинает считать с первого человека.
Когда считалка досчитывает до k-го слога, человек, на котором она остановилась, вылетает.
Игра происходит до тех пор, пока не останется последний человек.
Для данных N и К дать номер последнего оставшегося человека.
'''

def twister(N, K):
    """
    :param N: количество человек
    :param K: количество слогов
    :return:
    """
    people = [i for i in range(1, N + 1)]
    #print(people)
    twist = [1 for _ in range(K)]
    #print(twist)
    index_people = 0
    index_tw = 0

    while len(people) > 1: # пока список содержит больше одного человека
        while index_tw < len(twist) - 1:
            index_people += 1
            index_tw += 1
            if index_people == len(people):
                index_people = 0
        a = people[index_people]
        #print(a)
        people.remove(people[index_people])
        #print(people)
        index_tw = 0
        index_people = 0

    return people[0]




if __name__ == "__main__":
    N = 3 # количество человек
    K = 5 # количество слогов
    print("Номер последнего оставшегося человека: ", twister(N, K))
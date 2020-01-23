'''
Аренда ракет
Вы – компания, дающая в аренду ракеты. Каждый день к вам приходит список заявок на использование ракет в виде:
(час_начала, час_конца), (час_начала, час_конца), ...
Если аренда ракеты заканчивается в час X, то в этот же час ее уже можно взять в аренду снова
(т.е. час_начала может начинаться с Х).
Дано: список заявок на использование ракет
Задача: вывести ответ, хватит ли вам одной ракеты, чтобы удовлетворить все заявки на этот день
'''

import networkx as nx
import matplotlib.pyplot as plt


def rocket(orders):
    for order in orders:
        for i in range(order[0], order[1]):
            graph.add_edge(i, i + 1)

    #plot(graph)

    temp_lst = graph.degree
    print(graph.degree)
    for i in temp_lst:
        if i[1] > 2:
            return "Одной ракеты не хватит"
    return "Одной ракеты хватит"




def plot(graph):
    pos = nx.spring_layout(graph) # словарь, в котором ключи это вершины и их координаты в спец. формате
    labels = {n: n for n in graph.nodes()} # против каждой вершины мы можем назвать их как-то, мы здесь ими же и назвали
    nx.draw_networkx_nodes(graph, pos) # отрисовывает вершины
    nx.draw_networkx_edges(graph, pos) # отрисовывает связи
    nx.draw_networkx_labels(graph, pos, labels, font_size=16) # отрисовывает лэйблы

    plt.show() # визуализирует
    print(graph.degree)


if __name__ == "__main__":
    graph = nx.MultiDiGraph() # nx.MultiGraph() так как может сразу несколько связей идти из одного нода в другой
    graph.add_nodes_from(range(0, 24))  # часы

    orders = [
        (5, 12),
        (11, 15),
        (21, 23)
    ]
    print(rocket(orders))


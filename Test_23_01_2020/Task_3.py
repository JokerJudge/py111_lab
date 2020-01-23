'''
Назовем связным такой граф, в котором есть путь от любой вершины к любой другой вершине.
Дан граф, состоящий из 2+ связных подграфов, которые не связаны между собой.
Задача: посчитать число компонент связности графа, т.е. количество таких подграфов.

В графе на картинке – три подграфа, т.е. число компонент связности = 3.
'''
import networkx as nx

def connection_component(graph, start_node):
    all_visits = [] # список посещенных вершин всего графа
    visited = []  # список посещенных вершин одной связи
    queue = []  # список очереди
    connection_rate = 0
    #print(graph.nodes)
    queue.append(start_node)

    while all_visits != graph.nodes:
        queue.append(start_node)
        for node in queue:
            d = graph.adj[node]
            visited.append(node)
            for k in d:
                if k in visited or k in queue:
                    pass
                else:
                    queue.append(k)

        all_visits.extend(visited)
        temp_lst = list(set(graph.nodes) - set(all_visits))
        #print(temp_lst)
        connection_rate += 1
        if len(temp_lst) == 0:
            return connection_rate
        start_node = temp_lst[0]
        #print(temp_lst[0])


if __name__ == "__main__":
    g = nx.Graph()
    g.add_nodes_from("ABCDEFG")  # это 7 узлов в нашем графе
    g.add_edges_from(  # добавление простых связей
        [
            ("A", "B"),
            ("B", "C"),
            ("B", "D"),
            ("C", "D"),
            ("G", "F")
        ]
    )

    print("Компонент связанности графа: ", connection_component(g, "A"))

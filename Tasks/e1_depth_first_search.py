from typing import Hashable, List
import networkx as nx



def dfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
	"""
	Do an depth-first search and returns list of nodes in the visited order

	:param g: input graph
	:param start_node: starting node of search
	:return: list of nodes in the visited order
	"""
	visited = []  # список посещенных вершин
	queue = []  # список очереди (по медели стека)
	queue.append(start_node)
	for node in queue:
		index = queue.index(node) # ставим указатель на текущий индекс в стеке
		d = g.adj[node]
		visited.append(node)
		for k in d:
			if k in visited or k in queue:
				pass
			else:
				queue.insert(index + 1, k) # вставляем необходимые вершины сразу за текущим индексом
				index += 1

	return visited

'''
Работа на паре (dfs_find)

def dfs_find(graph, src, dst, visited): # граф, где ищем (откуда смотрим), что ищем (целевой узел), вершины, которые были посещены
	if src == dst: # dst - destination, базовый случай выхода из рекурсии
		return True
	visited[src] = True
	for node in graph.adj[src]: # на первом заходе заходим в узлы B и C
		if not visited[node]: # если мы еще тут не были - то запускаем рекурсию
			if dfs_find(graph, node, dst, visited): # вот этот момент нужно дебажить. Я не понимаю, почему недостаточно базового случая выхода из рекурсии
				return True


	return False


if __name__ == "__main__":
	graph = nx.Graph()
	graph.add_nodes_from("ABCDEFG") # это 7 узлов в нашем графе
	graph.add_edges_from( # добавление простых связей
		[
			("A", "B"),
			("A", "C"),
			("B", "D"),
			("B", "E"),
			("C", "F"),
			("E", "G")
		]
	)

	graph.add_node("Z")

	src = "A"
	dst = "F" # если тут меняем на Z, то не найдет, так как нет связи между Z и любой другой вершиной
	visited = {node: False for node in graph.nodes()} # будет фиксировать, где мы были
	print(visited)
	print(graph.nodes())
	for node in graph.adj: # матрица смежности - можно посмотреть примеры в гугле
		print(node, graph.adj[node])

	print(dfs_find(graph, src, dst, visited))
#####################################
'''

if __name__ == "__main__":
	graph = nx.Graph()
	graph.add_nodes_from("ABCDEFG") # это 7 узлов в нашем графе
	graph.add_edges_from( # добавление простых связей
		[
			("A", "B"),
			("A", "C"),
			("B", "D"),
			("B", "E"),
			("C", "F"),
			("E", "G")
		]
	)


	visited = {node: False for node in graph.nodes()}
	lst_of_nodes = []

	print(dfs(graph, "A"))


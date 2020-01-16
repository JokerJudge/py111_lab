from typing import Hashable, List
import networkx as nx
from collections import deque


def bfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
	"""
	Do an breadth-first search and returns list of nodes in the visited order

	:param g: input graph
	:param start_node: starting node for search
	:return: list of nodes in the visited order
	"""
	print(g, start_node)
	return list(g.nodes)

def bfs_find(graph, src, dst):
	visited = {node: False for node in graph.nodes()}
	parents = {src: src}
	deque_nodes = deque()
	deque_nodes.appendleft(src) # чтобы добавлять элементы слева (чтобы это был стек)

	while True:
		try: # остановимся, когда из очереди все снимется. Тогда мы будем уверены, что мы все элементы прошли
			src = deque_nodes.pop()
			visited[src] = True
			for node in graph.adj[src]: # проходимся по всем потомкам узла src
				if not visited[node]:
					deque_nodes.appendleft(node) # добавляем подожженные nodes
					parents[node] = parents[src] + node # это будет путь до dst
				if node == dst:
					return parents[node]
		except IndexError:
			return None # прошли по всему графу и не нашли искомый элемент - возвращаем None


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
			("E", "G"),
			("D", "F") # - если добавим это при поиске от B до F - то найдет еще короче путь
		]
	)

	graph.add_node("Z")

	src = "B"
	dst = "F"

	print(bfs_find(graph, src, dst))

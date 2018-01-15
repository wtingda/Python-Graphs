# unweighted graph implementation
# (c) 2017 @author Tingda Wang

from collections import defaultdict # for default values, set in this case
from pprint import pprint

class Graph:

    def __init__(self, edges, directed = False):
        self._graph = defaultdict(set)
        self._directed = directed
        self.add_edges(edges)

    def add_edges(self, edges):
        for n1, n2 in edges:
            self.add_edge(n1, n2)
    
    def add_edge(self, node1, node2):
        self._graph[node1].add(node2)
        if not self._directed:
            self._graph[node2].add(node1)

    def remove(self, node): # delete all edges 
        for edges in self._graph.iteritems():
            try:
                edges.remove(node)
            except KeyError:
                pass
            try:
                del self._graph[node]
            except KeyError:
                pass

    def has_edge(self, node1, node2): # path fron node1 to node2
        return node1 in self._graph and node2 in self._graph[node1]

    def find_path(self, node1, node2, path = []):
        path = path + [node1]
        if node1 == node2:
            return path
        if node1 not in self._graph:
            return None
        for node in self._graph[node1]:
            if node not in path:
                new_path = self.find_path(node, node2, path)
                if new_path:
                    return new_path
        return None

    def __str__(self):
        return '{}: ({})'.format(self.__class__.__name__, dict(self._graph))

if __name__ == "__main__":
    edges = [('A', 'B'), ('B', 'C'), ('B', 'D'),
             ('C', 'D'), ('E', 'F'), ('F', 'C')]
    graph = Graph(edges, directed = True)
    print(graph)
    pprint(graph._graph)
    graph = Graph(edges)
    pprint(graph._graph)
    print(graph.find_path('F', 'A'))

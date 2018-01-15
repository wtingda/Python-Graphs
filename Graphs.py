# graph implementation with direction, weights, and shortest path
# (c) 2017 @author Tingda Wang

from collections import defaultdict # for default values, set in this case
from pprint import pprint

class Graph:

    def __init__(self, edges, directed = False, weighted = False):
        self._graph = defaultdict(set)
        self._directed = directed
        self._weighted = weighted
        self.add_edges(edges)
        self._weights = defaultdict(int)
                
    def add_edges(self, edges, weights = None):
        for n1, n2 in edges:
            self.add_edge(n1, n2)
        if self._weighted:
            self.set_weights(weights)

    def add_edge(self, node1, node2, weight = None):
        self._graph[node1].add(node2)
        self.add_weight(node1, node2, weight)
        if not self._directed:
            self._graph[node2].add(node1)
            self.add_weight(node2, node1, weight)
    
    def set_weights(self, weights):
        if self._weighted:
            self._weights = weights
    
    def add_weight(self, node1, node2, weight):
        if self._weighted:
            self._weights[(node1, node2)] = weight
    
    def remove(self, node): # delete all edges 
        for edges in self._graph.items():
            try:
                edges.remove(node)
            except KeyError:
                pass
            try:
                del self._graph[node]
            except KeyError:
                pass

            if self.weighted:
                for edge in self._weights.items():
                    if edge[0] == node or edge[1] == node:
                        self._weights.remove(edge)
        
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

    def shortest_path(self, start):
        _visited = {start: 0}
        _path = {}

        _nodes = [key for key in self._graph.keys()]

        while _nodes:
            _min = None
            for node in _nodes:
                if node in _visited:
                    if _min is None:
                        _min = node
                    elif _visited[node] < _visited[_min]:
                        _min = node

            if _min is None:
                break
        
            _nodes.remove(_min)
            _current_weight = _visited[_min]

            for edge in self._graph[_min]:
                if self._weighted:
                    weight = _current_weight + self._graph.weights[(_min, edge)]
                else: 
                    weight = _current_weight + 1
                
                if edge not in _visited or weight < _visited[edge]:
                    _visited[edge] = weight
                    _path[edge] = _min

        return _visited, _path

    def __str__(self):
        return '{}: ({})'.format(self.__class__.__name__, dict(self._graph))


if __name__ == "__main__":
    edges = [('A', 'B'), ('B', 'C'), ('B', 'D'),
             ('C', 'D'), ('E', 'F'), ('D', 'E')]
    graph = Graph(edges, directed = True)
    print(graph)
    pprint(graph._graph)
    graph = Graph(edges)
    pprint(graph._graph)
    print(graph.find_path('F', 'A'))
    print('We visit these: {} \nThe paths are:{}'.format(graph.shortest_path('A')[0], graph.shortest_path('A')[1]))

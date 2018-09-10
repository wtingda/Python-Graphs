# (c) 2017 Tingda Wang
# Graph implementation with direction, weights, and shortest path

from functools import reduce

import heapq, math

INF = math.inf

class Graph():

    def __init__(self, vertices = [], edges = [], directed = False, weighted = False):
        ''' 
        @args vertices is list of vertices
        edges is tuple of (v1, v2) if unweighted or (v1, v2, w) if weighted
        '''
        
        self.weighted = weighted
        self.directed = directed
        self.edges = {}

        # adjacency list
        for vertex in vertices:
            self.edges[vertex] = []

        # store weights
        if self.weighted:
            self.weights = {}

        # adds edges
        self.add_edges(edges)

    def add_node(self, vertex):
        ''' adds a vertex if not in graph'''
        if vertex not in self.edges.keys():
            self.edges[vertex] = []

    def remove_node(self, v1):
        ''' deletes a vertex from the graph and erases all incoming/outgoing edges '''
        del self.edges[v1]
        for vertex in self.edges:
            if v1 in self.edges[vertex]:
                self.edges[vertex].remove(v1)

    def add_edges(self, edges):
        ''' adds all edges from list of edges '''
        if self.weighted:
            for v1, v2, weight in edges:
                self.add_edge(v1, v2, weight)
        else:
            for v1, v2 in edges:
                self.add_edge(v1, v2)

    def add_edge(self, v1, v2, weight = 1):
        ''' adds an edge '''
        self.edges[v1].append(v2)

        if self.weighted:
            self.weights[(v1, v2)] = weight
            
        if not self.directed:
            self.edges[v2].append(v1)

            if self.weighted:
                self.weights[(v2, v1)] = weight

    def set_weight(self, v1, v2, weight):
        ''' sets weight of edge (v1, v2)'''
        if self.weighted and self.contains_edge(v1, v2):
            self.weights[(v1, v2)] = weight
            if not self.directed:
                self.weights[(v2, v1)] = weight

    def remove_edge(self, v1, v2):
        ''' removes the edge between v1 and v2'''
        if self.contains_edge(v1, v2):
            self.edges[v1].remove(v2)

            if self.weighted:
                del self.weights[(v1, v2)]

            # have to do it again if not directed :(
            if not self.directed:
                self.edges[v2].remove(v1)

                if self.weighted:
                    del self.weights[(v2, v1)]
        else:
            raise EdgeNotFoundError("no edge between %s and %s" %(str(v1), str(v2)))
            
    def contains_edge(self, v1, v2):
        ''' determines if an edge exists'''
        return v2 in self.edges[v1] and (not self.directed or v1 in self.edges[v2])

    @property
    def vertices(self):
        ''' list of vertices '''
        return list(self.edges.keys())
    
    @property
    def num_vertices(self):
        ''' returns number of vertices'''
        return len(self.edges.keys())

    @property
    def num_edges(self):
        ''' returns number of edges'''

        # cheating alittle and using functional programming
        edges = reduce(lambda x, y: x + len(y), self.edges.values(), 0) 

        # undirected double counts edges
        return edges if self.weighted else edges // 2

    # ------------------- djikstra's algorithm ----------------------

    def _get_weight(self, v1, v2):
        ''' returns the weight of edge, helper for djikstra's '''
        assert self.contains_edge(v1, v2)
        
        if self.weighted:
            return self.weights[(v1, v2)]
        else:
            return 1

        
    def shortest_path(self, start, end):
        ''' 
        implementation of Djikstra's shortest path algorithm 
        returns (distance, path) tuple where path is a list of vertices on path
        if no path exists between start and end, returns (INF, [])
        '''

        if start not in self.edges:
            raise KeyError("Invalid start node %s" %start)
        
        # min heap for getting closest edge
        heap = [[INF, vertex] for vertex in self.vertices if not vertex == start]

        # start has min distance
        heap.append([0, start])

        # make min heap
        heapq.heapify(heap)
        
        parent = {x: None for x in self.vertices}

        # distance
        dist = INF
        
        # while there is still a node in heap
        while heap:
        
            popped = heapq.heappop(heap) # lowest distance

            # got to destination!
            if popped[1] == end:
                dist = popped[0]
                break # we can stop now
            
            for adjacent in self.edges[popped[1]]:
                for tup in heap: 
                    if tup[1] == adjacent:
                        
                        # get new distance from start
                        weight = popped[0] + self._get_weight(popped[1], adjacent)

                        if weight < tup[0]: 
                            # update distance
                            tup[0] = weight
                            # update parent dict
                            parent[adjacent] = popped[1]

        path = []

        if dist < INF: # there actually is such a path
            s = end
            
            while (not s == start) and (s is not None):
                path.append(s)
                s = parent[s]

            path.append(s)
            
        return dist, list(reversed(path))

    # ------------------------------------------------
    
    def __len__(self):
        ''' just number of vertices'''
        return self.num_vertices()

    def __repr__(self):
        ''' prints list of vertices and edges '''
        weight = 'Weighted' if self.weighted else 'Unweighted'
        directed = 'Directed' if self.directed else 'Undirected'
        graph = '---%s %s Graph---\n' %(weight, directed)
        s1 = 'Vertices: %s\nEdges: ' % str(list(self.edges.keys()))
        edges = [str((k, v)) for k, vs in self.edges.items() for v in vs]
        s2 = ', '.join(edges)
        return graph + s1 + s2

if __name__ == '__main__':
    vertices = ['a', 'b', 'c', 'd', 'e', 'f']
    edges = [('a', 'c'), ('b', 'e'), ('a', 'f'), ('e', 'd')]
    directed = False
    weighted = False
    g = Graph(vertices, edges, directed, weighted)
    print(g.num_vertices)
    print(g.num_edges)
    print(g)
    g.remove_edge('a', 'f')
    print(g)
    g.remove_node('a')
    print(g)
    g.add_node('a')
    g.add_edge('a', 'f')
    g.add_edge('a', 'c')
    print(g)
    print(g.vertices)
    print(g.shortest_path('c', 'f'))
    print(g.shortest_path('a', 'b'))

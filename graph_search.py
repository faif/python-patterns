#!/usr/bin/env python
# -*- coding: utf-8 -*-


class GraphSearch:

    """Graph search emulation in python, from source
    http://www.python.org/doc/essays/graphs/"""

    def __init__(self, graph):
        self.graph = graph

    def find_path(self, start, end, path=None):
        self.start = start
        self.end = end
        self.path = path if path else []

        self.path += [self.start]
        if self.start == self.end:
            return self.path
        if self.start not in self.graph:
            return None
        for node in self.graph[self.start]:
            if node not in self.path:
                newpath = self.find_path(node, self.end, self.path)
                if newpath:
                    return newpath
        return None

    def find_all_path(self, start, end, path=None):
        self.start = start
        self.end = end
        _path = path if path else []
        _path += [self.start]
        if self.start == self.end:
            return [_path]
        if self.start not in self.graph:
            return []
        paths = []
        for node in self.graph[self.start]:
            if node not in _path:
                newpaths = self.find_all_path(node, self.end, _path[:])
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

    def find_shortest_path(self, start, end, path=None):
        self.start = start
        self.end = end
        _path = path if path else []

        _path += [self.start]
        if self.start == self.end:
            return _path
        if self.start not in self.graph:
            return None
        shortest = None
        for node in self.graph[self.start]:
            if node not in _path:
                newpath = self.find_shortest_path(node, self.end, _path[:])
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest

# example of graph usage
graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C']
         }

# initialization of new graph search object
graph1 = GraphSearch(graph)


print(graph1.find_path('A', 'D'))
print(graph1.find_all_path('A', 'D'))
print(graph1.find_shortest_path('A', 'D'))

### OUTPUT ###
# ['A', 'B', 'C', 'D']
# [['A', 'B', 'C', 'D'], ['A', 'B', 'D'], ['A', 'C', 'D']]
# ['A', 'B', 'D']

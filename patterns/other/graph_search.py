class GraphSearch:

    """Graph search emulation in python, from source
    http://www.python.org/doc/essays/graphs/

    dfs stands for Depth First Search
    bfs stands for Breadth First Search"""

    def __init__(self, graph):
        self.graph = graph

    def find_path_dfs(self, start, end, path=None):
        path = path or []

        path.append(start)
        if start == end:
            return path
        for node in self.graph.get(start, []):
            if node not in path:
                newpath = self.find_path(node, end, path[:])
                if newpath:
                    return newpath

    def find_all_paths_dfs(self, start, end, path=None):
        path = path or []
        path.append(start)
        if start == end:
            return [path]
        paths = []
        for node in self.graph.get(start, []):
            if node not in path:
                newpaths = self.find_all_path(node, end, path[:])
                paths.extend(newpaths)
        return paths

    def find_shortest_path_dfs(self, start, end, path=None):
        path = path or []
        path.append(start)

        if start == end:
            return path
        shortest = None
        for node in self.graph.get(start, []):
            if node not in path:
                newpath = self.find_shortest_path(node, end, path[:])
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest

    def find_shortest_path_bfs(self, start, end):
        queue = [start]
        dist_to = {start: 0}
        edge_to = {}

        while len(queue):
            value = queue.pop(0)
            for node in self.graph[value]:
                if node not in dist_to.keys():
                    edge_to[node] = value
                    dist_to[node] = dist_to[value] + 1
                    queue.append(node)
            if end in edge_to.values():
                break

        path = []
        node = end
        while dist_to[node] != 0:
            path.insert(0, node)
            node = edge_to[node]
        path.insert(0, start)
        return path


def main():
    """
    # example of graph usage
    >>> graph = {'A': ['B', 'C'], 'B': ['C', 'D'], 'C': ['D'], 'D': ['C'], 'E': ['F'], 'F': ['C']}

    # initialization of new graph search object
    >>> graph1 = GraphSearch(graph)

    >>> print(graph1.find_path_dfs('A', 'D'))
    ['A', 'B', 'C', 'D']
    >>> print(graph1.find_all_paths_dfs('A', 'D'))
    [['A', 'B', 'C', 'D'], ['A', 'B', 'D'], ['A', 'C', 'D']]
    >>> print(graph1.find_shortest_path_dfs('A', 'D'))
    ['A', 'B', 'D']
    >>> print(graph1.find_shortest_path_bfs('A', 'D'))
    ['A', 'B', 'C']
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()

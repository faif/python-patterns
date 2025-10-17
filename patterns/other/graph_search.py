from typing import Any, Dict, List, Optional, Union


class GraphSearch:
    """Graph search emulation in python, from source
    http://www.python.org/doc/essays/graphs/

    dfs stands for Depth First Search
    bfs stands for Breadth First Search"""

    def __init__(self, graph: Dict[str, List[str]]) -> None:
        self.graph = graph

    def find_path_dfs(
        self, start: str, end: str, path: Optional[List[str]] = None
    ) -> Optional[List[str]]:
        path = path or []

        path.append(start)
        if start == end:
            return path
        for node in self.graph.get(start, []):
            if node not in path:
                newpath = self.find_path_dfs(node, end, path[:])
                if newpath:
                    return newpath

    def find_all_paths_dfs(
        self, start: str, end: str, path: Optional[List[str]] = None
    ) -> List[Union[List[str], Any]]:
        path = path or []
        path.append(start)
        if start == end:
            return [path]
        paths = []
        for node in self.graph.get(start, []):
            if node not in path:
                newpaths = self.find_all_paths_dfs(node, end, path[:])
                paths.extend(newpaths)
        return paths

    def find_shortest_path_dfs(
        self, start: str, end: str, path: Optional[List[str]] = None
    ) -> Optional[List[str]]:
        path = path or []
        path.append(start)

        if start == end:
            return path
        shortest = None
        for node in self.graph.get(start, []):
            if node not in path:
                newpath = self.find_shortest_path_dfs(node, end, path[:])
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest

    def find_shortest_path_bfs(self, start: str, end: str) -> Optional[List[str]]:
        """
        Finds the shortest path between two nodes in a graph using breadth-first search.

        :param start: The node to start from.
        :type start: str or int
        :param end: The node to find the shortest path to.
            :type end: str or int

            :returns queue_path_to_end, dist_to[end]: A list of nodes
        representing the shortest path from `start` to `end`, and a dictionary
        mapping each node in the graph (except for `start`) with its distance from it
        (in terms of hops). If no such path exists, returns an empty list and an empty
        dictionary instead.
        """
        queue = [start]
        dist_to = {start: 0}
        edge_to = {}

        if start == end:
            return queue

        while len(queue):
            value = queue.pop(0)
            for node in self.graph[value]:
                if node not in dist_to.keys():
                    edge_to[node] = value
                    dist_to[node] = dist_to[value] + 1
                    queue.append(node)
                    if end in edge_to.keys():
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
    >>> graph = {
    ...     'A': ['B', 'C'],
    ...     'B': ['C', 'D'],
    ...     'C': ['D', 'G'],
    ...     'D': ['C'],
    ...     'E': ['F'],
    ...     'F': ['C'],
    ...     'G': ['E'],
    ...     'H': ['C']
    ... }

    # initialization of new graph search object
    >>> graph_search = GraphSearch(graph)

    >>> print(graph_search.find_path_dfs('A', 'D'))
    ['A', 'B', 'C', 'D']

    # start the search somewhere in the middle
    >>> print(graph_search.find_path_dfs('G', 'F'))
    ['G', 'E', 'F']

    # unreachable node
    >>> print(graph_search.find_path_dfs('C', 'H'))
    None

    # non existing node
    >>> print(graph_search.find_path_dfs('C', 'X'))
    None

    >>> print(graph_search.find_all_paths_dfs('A', 'D'))
    [['A', 'B', 'C', 'D'], ['A', 'B', 'D'], ['A', 'C', 'D']]
    >>> print(graph_search.find_shortest_path_dfs('A', 'D'))
    ['A', 'B', 'D']
    >>> print(graph_search.find_shortest_path_dfs('A', 'F'))
    ['A', 'C', 'G', 'E', 'F']

    >>> print(graph_search.find_shortest_path_bfs('A', 'D'))
    ['A', 'B', 'D']
    >>> print(graph_search.find_shortest_path_bfs('A', 'F'))
    ['A', 'C', 'G', 'E', 'F']

    # start the search somewhere in the middle
    >>> print(graph_search.find_shortest_path_bfs('G', 'F'))
    ['G', 'E', 'F']

    # unreachable node
    >>> print(graph_search.find_shortest_path_bfs('A', 'H'))
    None

    # non existing node
    >>> print(graph_search.find_shortest_path_bfs('A', 'X'))
    None
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()

from patterns.other.graph_search import GraphSearch


def test_find_shortest_path_bfs_handles_leaf_nodes_without_outgoing_edges():
    # Leaf nodes ('C', 'D') have no entry in the graph dict, same as a
    # real-world adjacency list that only lists nodes with outgoing edges.
    graph = {
        "A": ["B"],
        "B": ["C", "D"],
    }
    search = GraphSearch(graph)

    assert search.find_shortest_path_bfs("A", "D") == ["A", "B", "D"]
    # Searching for a node that is unreachable must still traverse through
    # the leaf nodes without raising KeyError.
    assert search.find_shortest_path_bfs("A", "Z") is None

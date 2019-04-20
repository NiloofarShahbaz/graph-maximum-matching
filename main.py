from graph import Graph
from findMaximumMatching import FindMaximumMatching
import random
from copy import deepcopy
from igraph import Graph

g = Graph.Famous("noperfectmatching")
matching = g.maximum_matching()


def find_maximum_matching(vertices, edges):
    matching = {(1, 6)}
    saturated_vertices = [1, 6]
    print('matching', matching)
    for i in range(0, 7):
        print('------------ i ---------------')


def find_augmenting_path(matching, saturated_vertices, graph_edges):
    if len(matching) is 0:
        path = {random.choice(graph_edges)}
        return path
    path = deepcopy(matching)

    for edge in matching:
        for vertex in edge:
            pass


def find_connected_edges_to_vertex(vertex, graph_edges):
    result = {}
    for edge in graph_edges:
        if edge[0] is vertex or edge[1] is vertex:
            result.get(edge)
    return result



vertices = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
edges = {(1, 6), (1, 7), (2, 7), (2, 9), (3, 8), (3, 6), (4, 7), (4, 10), (5, 8), (5, 10)}

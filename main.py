from graph import Graph
from findMaximumMatching import FindMaximumMatching

vertices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
edges = [(1, 6), (1, 7), (2, 7), (2, 9), (3, 8), (3, 6), (4, 7), (4, 10), (5, 8), (5, 10)]
G = Graph(vertices=vertices, edges=edges)
algorithm = FindMaximumMatching(graph=G)
algorithm.run()

class Graph:
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges

    def bfs(self, node):
        related_edges = []
        for edge in self.edges:
            if edge[0] == node or edge[1] == node:
                related_edges.append(edge)
        return related_edges

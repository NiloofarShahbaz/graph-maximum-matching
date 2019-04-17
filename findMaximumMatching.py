import random
from copy import deepcopy

class FindMaximumMatching:
    def __init__(self, graph):
        self.graph = graph
        self.saturated_vertices = []
        self.seperated_graphs = []
        self.matching = [(1, 6)]

    def run(self):
        # augmenting_path = self.find_augmenting_path()
        print('matching', self.matching)
        for i in range(0, 7):
            print('------------ i ---------------')
            augmenting_path = self.find_augmenting_path()
            print('path', augmenting_path)
            self.matching = self.get_symmetric_difference(augmenting_path)
            print('matching', self.matching)

    def find_augmenting_path(self):
        m = len(self.matching)
        # if we have no matching choose a random edge to start width
        if m is 0:
            path = [random.choice(self.graph.edges)]
            return path
        path = deepcopy(self.matching)

        for edge in self.matching:
            v1, v2 = edge
            edges_related_to_v1 = self.graph.bfs(v1)
            print(v1, edges_related_to_v1)
            edges_related_to_v2 = self.graph.bfs(v2)
            print(v2, edges_related_to_v2)
            for e in edges_related_to_v1:
                if e in self.matching:
                    edges_related_to_v1.remove(e)
            for e in edges_related_to_v2:
                if e in self.matching:
                    edges_related_to_v2.remove(e)

            for edge1 in edges_related_to_v1:
                for edge2 in edges_related_to_v2:
                    if edge1 == edge2:
                        path.append(edge1)
                        break
            else:
                path.append(random.choice(edges_related_to_v1))
                path.append(random.choice(edges_related_to_v2))

        return path




    def find_related_edges_to_vertex(self, vertex, ):
        pass




    def get_symmetric_difference(self, path):
        # remove the identical edges from path
        for p in range(0, len(path)):
            print(p)
            for m in self.matching:
                print('sdhdks', p, m)
                if path[p] is m:
                    path.pop(p)
                    p = p - 1

        print('why', path)
        return path




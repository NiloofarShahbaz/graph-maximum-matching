import random
from copy import deepcopy

class FindMaximumMatching:
    def __init__(self, edges, vertices):
        self.edges=edges
        self.vertices=set(vertices)
        self.matching={(1, 6),(6,1)}
        self.saturated_vertices = {1, 6}

    def find_maximum_matching(self):
        print('matching', self.matching)
        for i in range(0, 7):
            print('------------ i ---------------')
            unsaturated = self.vertices.difference(self.saturated_vertices)
            if not len(unsaturated):
                return "yaaaaay"
            augmenting_path = self.find_augmenting_path()
            print(augmenting_path)

    def find_augmenting_path(self):
        if len(self.matching) is 0:
            path = {random.choice(self.edges)}
            return path

        unsaturated = self.vertices.difference(self.saturated_vertices)
        for v in unsaturated:
            vertices_copy = deepcopy(self.vertices)
            print("unsaturated ",v)
            depth = len(self.matching)  + 1
            agument_path=self.dfs(depth, vertices_copy, v, False)
            print("path",agument_path)
            if agument_path:
                break
        else:
            print("badbakht")

        # for match in self.matching:
        #     for v in match:
        #         connected_edges=self.find_connected_edges_to_vertex(v)
        #         connected_edges=connected_edges.difference(match)
        #         for edge in connected_edges:
        #             for v in edge:
        #                 if v not in self.saturated_vertices:
        #                     depth=len(self.matching)*2+1
        #                     agument_path=self.dfs(depth, vertices_copy, v, False)




    def dfs(self, depth, vertices, v, is_matching):
        print("depth ", depth , "ver", vertices , "v", v , is_matching)
        if depth==0:
            return [v]
        connected_edges=set(self.find_connected_edges_to_vertex(v, vertices))
        if is_matching:
            connected_edges=connected_edges.intersection(self.matching)
            vertices.remove(v)
            if len(connected_edges):
                v1, v2 = connected_edges
                if v1==v:
                    path=self.dfs(depth-1, vertices, v2, not is_matching)
                else:
                    path=self.dfs(depth-1, vertices, v1, not is_matching)
                if path is None:
                    return
                return path.append(v)
            else:
                return


        else:
            connected_edges=connected_edges.difference(self.matching)
            path=None
            vertices.remove(v)
            for edge in connected_edges:
                v1,v2=edge
                if v1==v:
                    path=self.dfs(depth-1,vertices,v2,not is_matching)
                else:
                    path=self.dfs(depth-1, vertices, v1, not is_matching)
                if path is not None:
                    return path.append(v)
            if path is None:
                return
            return


    def find_connected_edges_to_vertex(self, vertex , vertices):
        result = set()
        for edge in self.edges:
            if edge[0] is vertex:
                if edge[0] in vertices:
                    result.add(edge)
                    result.add((edge[1],edge[0]))
            elif edge[1] is vertex:
                if edge[1] in vertices:
                    result.add(edge)
        print("connected", result)
        return result



vertices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
edges = [(1, 6), (1, 7), (2, 7), (2, 9), (3, 8), (3, 6), (4, 7), (4, 10), (5, 8), (5, 10)]

f=FindMaximumMatching(edges,vertices)
f.find_maximum_matching()
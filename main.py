import random
from copy import deepcopy


class FindMaximumMatching:
    def __init__(self, edges, vertices):
        self.edges = edges
        self.vertices = set(vertices)
        self.matching = []
        self.saturated_vertices = set()
        self.separate = False

    def find_maximum_matching(self):
        print('matching', self.matching)
        fake_matching = []
        reveiw_augmenting_path = False
        i = 0
        while True:
            print('--------------', i, '--------------')
            i = i + 1
            unsaturated = self.vertices.difference(self.saturated_vertices)
            if len(unsaturated) <= 1:
                print('yaaay')
                return
            if reveiw_augmenting_path:
                print('reveiwwwww')
                print('fucking unsaturated', unsaturated)
                start = unsaturated.pop()
                for finish in unsaturated:
                    path = self.bfs_find_path_between(start, finish)
                    print('pathhhh', path)
                    if path:
                        if (len(path) - 1) % 2 is not 0:
                            unsaturated.remove(finish)
                            augmenting_vertices = self.dfs(depth=len(path) - 1, vertices=deepcopy(self.vertices),
                                                           v=start, is_matching=False, fake_matching=None,
                                                           finish=finish)
                            print('augmenting_vertices', augmenting_vertices)
                            self.saturated_vertices = self.saturated_vertices.union(augmenting_vertices)
                            print('saturated', self.saturated_vertices)
                            augmenting_path = []
                            for j in range(0, len(augmenting_vertices) - 1):
                                augmenting_path.append({augmenting_vertices[j], augmenting_vertices[j + 1]})
                            print(augmenting_path)
                            for edge in augmenting_path:
                                if edge in self.matching:
                                    self.matching.remove(edge)
                                else:
                                    self.matching.append(edge)
                            print('matching', self.matching)
                            break
                else:
                    self.vertices.remove(start)

            else:
                if not self.separate:
                    augmenting_vertices = self.find_augmenting_path()
                    if augmenting_vertices:
                        print('augmenting_vertices', augmenting_vertices)
                        self.saturated_vertices = self.saturated_vertices.union(augmenting_vertices)
                        print('saturated', self.saturated_vertices)
                        augmenting_path = []
                        for j in range(0, len(augmenting_vertices) - 1):
                            augmenting_path.append({augmenting_vertices[j], augmenting_vertices[j + 1]})
                        print(augmenting_path)
                        self.matching = [edge for edge in augmenting_path if edge not in self.matching]
                        print('matching', self.matching)
                    else:
                        self.separate = True
                        fake_matching = []
                        print('SEPERATEEEEED')
                else:
                    print('fake matching', fake_matching)
                    augmenting_vertices = self.find_augmenting_path(fake_matching)
                    print(augmenting_vertices)
                    if augmenting_vertices == 'FINISH':
                        return
                    if augmenting_vertices is not None:
                        print('augmenting_vertices', augmenting_vertices)
                        self.saturated_vertices = self.saturated_vertices.union(augmenting_vertices)
                        print('saturated', self.saturated_vertices)
                        augmenting_path = []
                        for j in range(0, len(augmenting_vertices) - 1):
                            augmenting_path.append({augmenting_vertices[j], augmenting_vertices[j + 1]})
                        print(augmenting_path)
                        for edge in augmenting_path:
                            if edge in self.matching:
                                self.matching.remove(edge)
                            else:
                                self.matching.append(edge)

                        print('matching', self.matching)
                        fake_matching = [edge for edge in augmenting_path if edge not in fake_matching]
                        print('fake matching ', fake_matching)
                    else:
                        if len(fake_matching) is 0:
                            # we cannot find a path with these vertices.
                            reveiw_augmenting_path = True
                        else:
                            fake_matching = []

    def find_augmenting_path(self, fake_matching=None, check_path=False):
        if len(self.matching) is 0:
            v1, v2 = random.choice(self.edges)
            path = [v1, v2]
            return path

        unsaturated = self.vertices.difference(self.saturated_vertices)
        print('unsaturated list', unsaturated)
        if fake_matching is None:
            for v in unsaturated:
                vertices_copy = deepcopy(self.vertices)
                print("unsaturated ", v)
                depth = len(self.matching) * 2 + 1
                path = self.dfs(depth, vertices_copy, v, False)
                if path:
                    return path
        else:
            temp_vertices = unsaturated
            for edge in fake_matching:
                v1, v2 = edge
                temp_vertices.add(v1)
                temp_vertices.add(v2)

            for v in unsaturated:
                vertices_copy = deepcopy(temp_vertices)
                print("unsaturated ", v)
                depth = len(fake_matching) * 2 + 1
                path = self.dfs(depth, vertices_copy, v, False, fake_matching)
                if path:
                    return path

    def bfs_find_path_between(self, start, finish):
        print(start, finish)
        queue = [[start]]
        visited = []
        while len(queue):
            path = queue.pop(0)
            node = path[-1]

            connected_edges = self.find_connected_edges_to_vertex(node, self.vertices)
            for edge in connected_edges:
                v1, v2 = edge
                new_path = deepcopy(path)
                if v1 is node:
                    if v2 not in visited:
                        new_path.append(v2)
                        queue.append(new_path)
                        if v2 is finish:
                            return new_path
                else:
                    if v1 not in visited:
                        new_path.append(v1)
                        queue.append(new_path)
                        if v1 is finish:
                            return new_path
            visited.append(node)

    def dfs(self, depth, vertices, v, is_matching, fake_matching=None, finish=None):
        print("depth ", depth, "vertices", vertices, "v", v, is_matching)
        if finish is not None:
            print('aaaaa')
            if depth is 0 and v is finish:
                return [v]
        else:
            if depth is 0:
                return [v]

        if not len(vertices):
            return
        connected_edges = self.find_connected_edges_to_vertex(v, vertices)
        if is_matching:
            if fake_matching:
                connected_edges = [edge for edge in connected_edges if edge in fake_matching]

            else:
                connected_edges = [edge for edge in connected_edges if edge in self.matching]
            print(connected_edges)
            vertices.remove(v)
            if len(connected_edges) is 1:
                v1, v2 = connected_edges[0]
                if v1 == v:
                    path = self.dfs(depth - 1, deepcopy(vertices), v2, not is_matching, fake_matching, finish)
                else:
                    path = self.dfs(depth - 1, deepcopy(vertices), v1, not is_matching, fake_matching, finish)
                # print('pp', path)
                if path:
                    path.append(v)
                    return path
        else:
            if fake_matching:
                connected_edges = [edge for edge in connected_edges if edge not in fake_matching]
            else:
                connected_edges = [edge for edge in connected_edges if edge not in self.matching]
            print(connected_edges)
            vertices.remove(v)
            for edge in connected_edges:
                v1, v2 = edge
                if v1 == v:
                    path = self.dfs(depth - 1, deepcopy(vertices), v2, not is_matching, fake_matching, finish)
                else:
                    path = self.dfs(depth - 1, deepcopy(vertices), v1, not is_matching, fake_matching, finish)
                # print('p', path)
                if path:
                    path.append(v)
                    return path

    def find_connected_edges_to_vertex(self, vertex, vertices):
        result = []
        for edge in self.edges:
            v1, v2 = edge
            if v1 is vertex:
                if v2 in vertices:
                    result.append(edge)
            elif v2 is vertex:
                if v1 in vertices:
                    result.append(edge)

        return result


vertices = [1, 2, 3, 4, 5, 6, 7, 8]
# edges = [{1, 6}, {1, 7}, {1, 9}, {1, 10}, {2, 6}, {2, 7}, {2, 9}, {2, 10}, {3, 8}, {3, 10}, {4, 6}, {4, 10}, {5, 10}]
# edges = [{1, 6}, {1, 7}, {2, 7}, {2, 9}, {3, 8}, {3, 6}, {4, 7}, {4, 10}, {5, 10}, {5, 8}]
edges = [{1, 3}, {1, 6}, {1, 8}, {2, 4}, {2, 6}, {2, 7}, {2, 8}]

f = FindMaximumMatching(edges, vertices)
f.find_maximum_matching()
print(f.matching)

from itertools import permutations

class Graph:
    # Grafo implementado por uma lista de adjacencia
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges
        self.adjacency_list = {vertice: [] for vertice in range(len(vertices))}

        for i, (u, v) in enumerate(self.edges):
          u_index = self.vertices.index(u)
          v_index = self.vertices.index(v)
          self.adjacency_list[u_index].append(v)
          self.adjacency_list[v_index].append(u)

    def get_neighbors(self, vertice):
        vert_index = self.vertices.index(vertice)
        return self.adjacency_list[vert_index]

def is_isomorphic(g1, g2):
    if len(g1.vertices) != len(g2.vertices) or len(g1.edges) != len(g2.edges):
        return False

    def isomorphism_match(mapping, u, v):
        for u_neighbor in g1.get_neighbors(u):
            u_mapped = mapping.get(u_neighbor)
            if u_mapped:
                if v not in g2.get_neighbors(u_mapped):
                    return False
            else:
                v_neighbors = g2.get_neighbors(v)
                if not any(isomorphism_match(mapping, u_neighbor, v_neighbor) for v_neighbor in v_neighbors):
                    return False
        return True

    vertices1 = list(g1.vertices)
    vertices2 = list(g2.vertices)

    for perm in permutations(vertices2):
        mapping = {vertices1[i]: perm[i] for i in range(len(vertices1))}
        if isomorphism_match(mapping, vertices1[0], perm[0]):
            return True

    return False

# Exemplos:

# Caso 1 - é isomorfico
vertices1 = [1, 2, 3]
edges1 = [[1, 2]]

vertices2 = [5, 4, 3]
edges2 = [[5, 3]]

graph1 = Graph(vertices1, edges1)
graph2 = Graph(vertices2, edges2)
result = is_isomorphic(graph1, graph2)
print(f"É isomorfico: {result}") 

# Caso 2 - não é isomorfico (número diferente de arestas)
vertices1 = [1, 2, 3, 4, 5]
edges1 = [[1, 2], [1, 3], [1, 5]]

vertices2 = [5, 4, 3, 2, 1]
edges2 = [[5, 3], [5, 1]]

graph1 = Graph(vertices1, edges1)
graph2 = Graph(vertices2, edges2)
result = is_isomorphic(graph1, graph2)
print(f"É isomorfico: {result}")

# Caso 3 - não é isomorfico (número diferente de vértices)
vertices1 = [1, 2, 3]
edges1 = [[1, 2], [1, 3]]

vertices2 = [5, 4, 3, 2, 1]
edges2 = [[5, 1], [5, 4]]

graph1 = Graph(vertices1, edges1)
graph2 = Graph(vertices2, edges2)
result = is_isomorphic(graph1, graph2)
print(f"É isomorfico: {result}")

# Caso 4 - não é isomorfico (arestas diferentes)
vertices1 = [1, 2, 3, 4, 5]
edges1 = [[1, 2], [1, 3]]

vertices2 = [5, 4, 3, 2, 1]
edges2 = [[5, 1], [5, 4], [5, 3]]

graph1 = Graph(vertices1, edges1)
graph2 = Graph(vertices2, edges2)
result = is_isomorphic(graph1, graph2)
print(f"É isomorfico: {result}")

# Caso 5 - é isomórfico 
vertices1 = ['A', 'B','C', 'D']
edges1 = [['A', 'B'], ['A', 'C'], ['B', 'D'], ['C', 'D']]

vertices2 = ['X', 'Y', 'Z', 'W']
edges2 = [['X', 'Y'], ['X', 'Z'], ['Y', 'W'], ['Z', 'W']]

graph1 = Graph(vertices1, edges1)
graph2 = Graph(vertices2, edges2)
result = is_isomorphic(graph1, graph2)
print(f"É isomorfico: {result}")
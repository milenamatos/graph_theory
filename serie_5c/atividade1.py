import networkx as nx
import matplotlib.pyplot as plt

class AdjacencyList:
    def __init__(self, vertices, edges):
      self.vertices = vertices
      self.edges = edges
      self.adjacency_list = {vertice: [] for vertice in range(len(vertices))}

      for i, (u, v) in enumerate(self.edges):
        u_index = self.vertices.index(u)
        v_index = self.vertices.index(v)
        self.adjacency_list[u_index].append(v)
        self.adjacency_list[v_index].append(u)

    def display_adjacency_list(self):
      self.render_graph()
      print("Lista de adjacência:")
      for v, neighbors in self.adjacency_list.items():
          print(f"Vertice {self.vertices[v]}: {neighbors}")

    def render_graph(self):
      graph = nx.Graph()
      graph.add_nodes_from(self.vertices)
      graph.add_edges_from(self.edges)

      pos = nx.circular_layout(graph)
      nx.draw(graph, with_labels=True, pos=pos)
      plt.show()  

def graph_union(g1, g2):
    # União de vértices
    vertices_union = set(g1.vertices) | set(g2.vertices)

    # União de arestas
    edges_union = g1.edges.copy()
    for edge in g2.edges:
        if edge not in edges_union and (edge[1], edge[0]) not in edges_union:
            edges_union.append(edge)
    
    return AdjacencyList(list(vertices_union), edges_union)

def graph_intersection(g1, g2):
    # Interseção de vértices
    vertices_intersect = set(g1.vertices) & set(g2.vertices)

    # Interseção de arestas
    edges_intersect = [edge for edge in g1.edges if edge in g2.edges or (edge[1], edge[0]) in g2.edges]
    
    return AdjacencyList(list(vertices_intersect), edges_intersect)

def graph_symmetric_difference(g1, g2):
    # União dos grafos
    union = graph_union(g1, g2)

    # Interseção dos grafos
    intersection = graph_intersection(g1, g2)
    
    # Vértices na diferença simétrica
    vertices_symmetric_difference = union.vertices
    
    # Arestas na diferença simétrica
    edges_symmetric_difference = [edge for edge in union.edges if edge not in intersection.edges]
    
    return AdjacencyList(vertices_symmetric_difference, edges_symmetric_difference)

# Exemplo de uso
g1 = AdjacencyList([1, 2, 3], [(1, 2), (2, 3)])
print("G1:")
g1.display_adjacency_list()

g2 = AdjacencyList([2, 3, 4], [(2, 3), (3, 4)])
print("G2:")
g2.display_adjacency_list()

uniao = graph_union(g1, g2)
print(f'União - Vértices: {uniao.vertices} / Arestas: {uniao.edges}')
uniao.display_adjacency_list()

intersecao = graph_intersection(g1, g2)
print(f'Interseção - Vértices: {intersecao.vertices} / Arestas: {intersecao.edges}')
intersecao.display_adjacency_list()

diferenca_simetrica = graph_symmetric_difference(g1, g2)
print(f'Diferença Simétrica - Vértices: {diferenca_simetrica.vertices} / Arestas: {diferenca_simetrica.edges}')
diferenca_simetrica.display_adjacency_list()
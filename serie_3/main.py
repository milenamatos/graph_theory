from AdjMatrix import AdjacencyMatrix
from IncMatrix import IncidenceMatrix
from AdjList import AdjacencyList

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []
        
    def add_edge(self, u, v):
        if 0 <= u < self.vertices and 0 <= v < self.vertices:
            self.edges.append([u, v])

if __name__ == "__main__":
    num_vertices = 5 
    # Neste exemplo o código considera 0 um vértice, então serão: 0, 1, 2, 3, 4
    graph = Graph(num_vertices)

    # Adicionando arestas
    graph.add_edge(0, 2)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)

    adj_matrix = AdjacencyMatrix(num_vertices, graph.edges)
    adj_matrix.display_adjacency_matrix()
    adj_matrix.generate_graph_from_adjacency_matrix()

    inc_matrix = IncidenceMatrix(num_vertices, graph.edges)
    inc_matrix.display_incidence_matrix()
    inc_matrix.generate_graph_from_incidence_matrix()

    adj_list = AdjacencyList(num_vertices, graph.edges)
    adj_list.display_adjacency_list()
    adj_list.generate_graph_from_adjacency_list()

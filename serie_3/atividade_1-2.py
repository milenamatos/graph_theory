from src.AdjMatrix import AdjacencyMatrix
from src.IncMatrix import IncidenceMatrix
from src.AdjList import AdjacencyList

class Graph:
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges

    def num_vertices(self):
       return len(self.vertices)

    def add_edge(self, u, v):
        if 0 <= u < self.num_vertices() and 0 <= v < self.num_vertices():
            self.edges.append([u, v])

if __name__ == "__main__":
    #Vertices
    vertices = [1, 2, 3, 4, 5]
    # Arestas
    edges = [[1, 2], [1, 4], [1, 5], [2, 4], [2, 3]]

    graph = Graph(vertices, edges)

    adj_matrix = AdjacencyMatrix(vertices, edges)
    adj_matrix.display_adjacency_matrix()
    adj_matrix.generate_graph_from_adjacency_matrix()
    adj_matrix.get_neighbors(2)
    adj_matrix.has_edge(1, 4)
    adj_matrix.has_edge(3, 5)
    adj_matrix.get_degree(1)
    adj_matrix.get_all_degrees()
    path = adj_matrix.find_simple_path(3, 5)
    print("Caminho simples de 3 a 5:", path)

    # inc_matrix = IncidenceMatrix(vertices, edges)
    # inc_matrix.display_incidence_matrix()
    # inc_matrix.generate_graph_from_incidence_matrix()
    # inc_matrix.get_neighbors(2)
    # inc_matrix.has_edge(1, 4)
    # inc_matrix.has_edge(3, 5)
    # inc_matrix.get_degree(1)
    # inc_matrix.get_all_degrees()
    # path = inc_matrix.find_simple_path(3, 5)
    # print("Caminho simples de 3 a 5:", path)

    # adj_list = AdjacencyList(vertices, edges)
    # adj_list.display_adjacency_list()
    # adj_list.generate_graph_from_adjacency_list()
    # adj_list.get_neighbors(2)
    # adj_list.has_edge(1, 4)
    # adj_list.has_edge(3, 5)
    # adj_list.get_degree(1)
    # adj_list.get_all_degrees()
    # path = adj_list.find_simple_path(3, 5)
    # print("Caminho simples de 3 a 5:", path)


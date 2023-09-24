class IncidenceMatrix:
    def __init__(self, vertices, edges):
      self.vertices = vertices
      self.edges = edges
      self.incidence_matrix = [[0] * len(self.edges) for _ in range(self.vertices)]  # Gera matriz de incidência zerada

      for edge_index, (u, v) in enumerate(self.edges):
          self.incidence_matrix[u][edge_index] = 1
          self.incidence_matrix[v][edge_index] = 1

    def display_incidence_matrix(self):
      print("Matriz de incidência:")
      for row in self.incidence_matrix:
        print(" ".join(map(str, row)))

    def generate_graph_from_incidence_matrix(self):
      vertices = len(self.incidence_matrix[0])
      edges = len(self.incidence_matrix[1])
      print("Vertices: ", " ".join(map(str, range(vertices))))
      print("Arestas:")
      
      for i in range(edges):
        current_edge = []
        for j in range(vertices):
            if self.incidence_matrix[j][i] == 1:
                current_edge.append(j)
        print(" ".join(map(str, current_edge)))
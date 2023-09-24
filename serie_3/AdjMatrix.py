class AdjacencyMatrix:
    def __init__(self, vertices, edges):
      self.vertices = vertices
      self.edges = edges
      self.adj_matrix = [[0] * vertices for _ in range(vertices)] # Gera matriz de adjacência zerada

      for i, (u, v) in enumerate(self.edges): 
        self.adj_matrix[u][v] = 1
        self.adj_matrix[v][u] = 1

    def display_adjacency_matrix(self):
      print("Matriz de adjacência:")
      for row in self.adj_matrix:
          print(" ".join(map(str, row)))

    def generate_graph_from_adjacency_matrix(self):
      vertices = len(self.adj_matrix[0])
      print("Vertices: ", " ".join(map(str, range(vertices))))
      print("Arestas:")
      
      for i in range(vertices):
        for j in range(i+1, vertices): # o i+1 é utilizado para percorrer apenas na diagonal superior da matriz
            if self.adj_matrix[i][j] == 1:
                print(i, j)
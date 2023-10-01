class AdjacencyMatrix:
    def __init__(self, vertices, edges):
      self.vertices = vertices
      self.edges = edges
      self.adj_matrix = [[0] * len(vertices) for _ in range(len(vertices))] # Gera matriz de adjacência zerada

      for i, (u, v) in enumerate(self.edges):
        u_index = self.vertices.index(u)
        v_index = self.vertices.index(v)
        self.adj_matrix[u_index][v_index] = 1
        self.adj_matrix[v_index][u_index] = 1

    def num_vertices(self):
       return len(self.adj_matrix[0])

    def num_edges(self):
       return len(self.edges)

    def display_adjacency_matrix(self):
      print("Matriz de adjacência:")
      for row in self.adj_matrix:
          print(" ".join(map(str, row)))

    def generate_graph_from_adjacency_matrix(self):
      vertices = len(self.adj_matrix[0])
      print("Vertices: ", " ".join(map(str, self.vertices)))
      print("Arestas:")

      for i in range(vertices):
        for j in range(i+1, vertices): # o i+1 é utilizado para percorrer apenas na diagonal superior da matriz
            if self.adj_matrix[i][j] == 1:
                print(self.vertices[i], self.vertices[j])

    def get_neighbors(self, vertice):
      vert_index = self.vertices.index(vertice)
      neighbors = []

      for i in range(self.num_vertices()):
        if self.adj_matrix[vert_index][i] == 1:
          neighbors.append(self.vertices[i])

      return neighbors

    def has_edge(self, u, v):
      u_index = self.vertices.index(u)
      v_index = self.vertices.index(v)
      has_edge = self.adj_matrix[u_index][v_index] == 1

      if (has_edge):
        print(f"{u} e {v} possuem uma aresta")
      else:
        print(f"{u} e {v} não possuem uma aresta")

    def get_degree(self, vertice):
      v_index = self.vertices.index(vertice)
      degree = sum(self.adj_matrix[v_index])

      print(f"Grau de {vertice}: {degree}")

    def get_all_degrees(self):
      print("Todos os graus:")
      for v in self.vertices:
        self.get_degree(v)

    def find_simple_path(self, start, end, path=None):
        if path is None:
          path = []

        start_index = self.vertices.index(start)
        path.append(start)

        if start == end:
          return path  # Encontramos o caminho

        for neighbor_index, has_edge in enumerate(self.adj_matrix[start_index]):
          if has_edge == 1 and self.vertices[neighbor_index] not in path:
            new_path = self.find_simple_path(self.vertices[neighbor_index], end, path)
            if new_path:
              return new_path

        path.pop()

        return None  # Não há caminho simples entre os vértices

    def find_cycle(self, vertice):
      visited = [False] * len(self.vertices) # Inicializa array com False em todas posições
      path = []
      
      def dfs(start_vertex, target_vertex, parent):
        vertex_index = self.vertices.index(start_vertex)
        visited[vertex_index] = True
        path.append(start_vertex)
    
        for neighbor in self.get_neighbors(start_vertex):
          neighbor_index = self.vertices.index(neighbor)
          if not visited[neighbor_index]:
            if dfs(neighbor, target_vertex, start_vertex):
              return True
          elif neighbor != parent and neighbor == target_vertex:
              path.append(neighbor)
              return True
        
        if path[-1] == start_vertex:
          # Remove o último vértice do caminho, já que não faz parte do ciclo
          path.pop()

        return False

      if dfs(vertice, vertice, -1):
        print(f"Existe um ciclo contendo o vértice {vertice}.")
        print(f"Ciclo:"," ".join(map(str, path)))
      else:
        print(f"Não existe um ciclo contendo o vértice {vertice}.")

    def is_subgraph(self, subgraph_vertices, subgraph_edges):
      # Verifica se todos os vértices do subconjunto estão presentes no grafo principal
      for vertice in subgraph_vertices:
        if vertice not in self.vertices:
          return False

      # Verifica se todas as arestas do subconjunto estão presentes no grafo principal
      for u, v in subgraph_edges:
        u_index = self.vertices.index(u)
        v_index = self.vertices.index(v)
        if self.adj_matrix[u_index][v_index] != 1:
          return False

      return True
      
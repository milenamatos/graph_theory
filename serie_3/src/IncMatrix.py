class IncidenceMatrix:
    def __init__(self, vertices, edges):
      self.vertices = vertices
      self.edges = edges
      self.incidence_matrix = [[0] * len(self.edges) for _ in range(len(vertices))]  # Gera matriz de incidência zerada

      for edge_index, (u, v) in enumerate(self.edges):
        u_index = self.vertices.index(u)
        v_index = self.vertices.index(v)
        self.incidence_matrix[u_index][edge_index] = 1
        self.incidence_matrix[v_index][edge_index] = 1

    def num_vertices(self):
       return len(self.incidence_matrix[0])

    def num_edges(self):
      return len(self.edges)

    def display_incidence_matrix(self):
      print("Matriz de incidência:")
      for row in self.incidence_matrix:
        print(" ".join(map(str, row)))

    def generate_graph_from_incidence_matrix(self):
      edges = len(self.incidence_matrix[1])
      print("Vertices: ", " ".join(map(str, self.vertices)))
      print("Arestas:")

      for i in range(edges):
        current_edge = []
        for j in range(self.num_vertices()):
            if self.incidence_matrix[j][i] == 1:
                current_edge.append(self.vertices[j])
        print(" ".join(map(str, current_edge)))

    def get_neighbors(self, vertice):
      vert_index = self.vertices.index(vertice)
      neighbors = []

      for edge in range(self.num_edges()):
        if self.incidence_matrix[vert_index][edge] == 1:
          for v in range(self.num_vertices()):
            if v != vert_index and self.incidence_matrix[v][edge] == 1:
              neighbors.append(self.vertices[v])

      return neighbors


    def has_edge(self, u, v):
      u_index = self.vertices.index(u)
      v_index = self.vertices.index(v)
      has_edge = False

      for edge in range(self.num_edges()):
        if self.incidence_matrix[u_index][edge] == 1 and self.incidence_matrix[v_index][edge] == 1:
          has_edge = True

      if (has_edge):
        print(f"{u} e {v} possuem uma aresta")
      else:
        print(f"{u} e {v} não possuem uma aresta")

    def get_degree(self, vertice):
      v_index = self.vertices.index(vertice)
      degree = 0

      for edge in range(self.num_edges()):
        if self.incidence_matrix[v_index][edge] == 1:
          degree += 1

      print(f"Grau de {vertice}: {degree}")

    def get_all_degrees(self):
      print("Todos os graus:")
      for v in self.vertices:
        self.get_degree(v)

    def find_simple_path(self, start, end, visited=None, path=None):
      if visited is None:
        visited = set()
      if path is None:
        path = []

      start_index = self.vertices.index(start)

      visited.add(start)
      path.append(start)

      if start == end:
        return path  # Encontramos o caminho

      for edge in range(self.num_edges()):
        if self.incidence_matrix[start_index][edge] == 1:
          for v in range(self.num_vertices()):
            if v != start_index and self.incidence_matrix[v][edge] == 1:
              neighbor = self.vertices[v]
              if neighbor not in visited:
                new_path = self.find_simple_path(neighbor, end, visited, path)
                if new_path:
                  return new_path

      path.pop()
      visited.remove(start)

      return None  # Não há caminho simples entre os vértices

    def find_cycle(self, vertice):
      visited = [False] * self.num_vertices() # Inicializa array com False em todas posições
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
        is_edge_present = False

        for edge in range(self.num_edges()):
          if self.incidence_matrix[u_index][edge] == 1 and self.incidence_matrix[v_index][edge] == 1:
            is_edge_present = True
            break

        if not is_edge_present:
          return False

      return True

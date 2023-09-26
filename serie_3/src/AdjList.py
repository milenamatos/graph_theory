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

    def num_vertices(self):
       return len(self.adjacency_list)

    def num_edges(self):
       return len(self.edges)

    def display_adjacency_list(self):
      print("Lista de adjacência:")
      for v, neighbors in self.adjacency_list.items():
          print(f"Vertice {self.vertices[v]}: {neighbors}")

    def generate_graph_from_adjacency_list(self):
      edges = []
      print("Vertices: ", " ".join(map(str, self.vertices)))
      print("Arestas:")

      for u in self.adjacency_list:
        for v in self.adjacency_list[u]:
            edges.append([self.vertices[u], v]) # Neste caso as arestas podem se repetir por conta da ordem

      for i in range(len(edges)):
        print(" ".join(map(str, edges[i])))

    def get_neighbors(self, vertice):
      vert_index = self.vertices.index(vertice)
      print(f"Vizinhos de {vertice}:"," ".join(map(str, self.adjacency_list[vert_index])))

    def has_edge(self, u, v):
      u_index = self.vertices.index(u)
      has_edge = v in self.adjacency_list[u_index]

      if (has_edge):
        print(f"{u} e {v} possuem uma aresta")
      else:
        print(f"{u} e {v} não possuem uma aresta")

    def get_degree(self, vertice):
      v_index = self.vertices.index(vertice)
      degree = len(self.adjacency_list[v_index])

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

      for neighbor in self.adjacency_list[start_index]:
        if neighbor not in visited:
          new_path = self.find_simple_path(neighbor, end, visited, path)
          if new_path:
            return new_path

      path.pop()
      visited.remove(start)

      return None  # Não há caminho entre os vértices
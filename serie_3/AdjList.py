class AdjacencyList:
    def __init__(self, vertices, edges):
      self.vertices = vertices
      self.edges = edges
      self.adjacency_list = {vertice: [] for vertice in range(self.vertices)}

      for i, (u, v) in enumerate(self.edges):
          self.adjacency_list[u].append(v)
          self.adjacency_list[v].append(u)

    def display_adjacency_list(self):
      print("Lista de adjacência:")
      for vertice, neighbors in self.adjacency_list.items():
          print(f"Vertice {vertice}: {neighbors}")

    def generate_graph_from_adjacency_list(self):
      vertices = len(self.adjacency_list)
      edges = []
      print("Vertices: ", " ".join(map(str, range(vertices))))
      print("Arestas:")

      for u in self.adjacency_list:
        for v in self.adjacency_list[u]:
            edges.append([u, v]) # Neste caso as arestas podem se repetir por conta da ordem
      
      for i in range(len(edges)):
        print(" ".join(map(str, edges[i])))
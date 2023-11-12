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
      print("Lista de adjacência:")
      for v, neighbors in self.adjacency_list.items():
          print(f"Vertice {self.vertices[v]}: {neighbors}")

    def get_neighbors(self, vertice):
      vert_index = self.vertices.index(vertice)
      return self.adjacency_list[vert_index]

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

    def find_cycle(self, vertice):
      visited = [False] * len(self.vertices)
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
        print(f"Ciclo:")
        for i in range(len(path) - 1):
          edge = f'{path[i]}-{path[i + 1]}'
          print(f'Vértice: {path[i]} - Aresta: {edge}')
        print(f'Vértice: {path[-1]}')
      else:
        print(f"Não existe um ciclo contendo o vértice {vertice}.")


    def is_connected(self):
        def dfs(start):
          stack = [start]
          visited = set()

          while stack:
              current_vertex = stack.pop()

              if current_vertex not in visited:
                  visited.add(current_vertex)

                  for neighbor in self.get_neighbors(current_vertex):
                      stack.append(neighbor)

          return visited

        # Escolha um vértice qualquer como ponto de partida
        start_vertex = self.vertices[0]

        # Execute DFS a partir do vértice escolhido
        reachable_vertices = dfs(start_vertex)

        # Verifique se todos os vértices foram alcançados
        return len(reachable_vertices) == len(self.vertices)
      

if __name__ == "__main__":
    ########## Utilizando lista de adjacência ##########
    vertices = [1, 2, 3, 4, 5]
    edges = [[1, 2], [1, 4], [1, 5], [2, 4], [2, 3]]   

    adj_list = AdjacencyList(vertices, edges)
    adj_list.display_adjacency_list()

    path = adj_list.find_simple_path(3, 5)
    print("Caminho simples de 3 a 5:")
    for i in range(len(path) - 1):
        edge = f'{path[i]}-{path[i + 1]}'
        print(f'Vértice: {path[i]} - Aresta: {edge}')
    print(f'Vértice: {path[-1]}')
    
    adj_list.find_cycle(3)
    adj_list.find_cycle(4)

    print("Grafo Conectado:", adj_list.is_connected())

    ########## Exemplo de grafo desconexo ###########
    vertices = [1, 2, 3, 4]
    edges = [[1, 2], [3, 4]]
    adj_list = AdjacencyList(vertices, edges)
    adj_list.display_adjacency_list()
    
    print("Grafo Conectado:", adj_list.is_connected())
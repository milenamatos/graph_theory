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


def read_vertices():
	vertices = []
	
	with open('arquivos/estacoes.txt', 'r') as file:
		for line in file:
			vertices.append(line.strip())
	
	return vertices

def read_edges():
	edges = []
	
	with open('arquivos/conexoes.txt', 'r') as file:
		for line in file:
			vertices = line.strip().split(',')
			if len(vertices) == 2:
				edges.append((vertices[0].strip(), vertices[1].strip()))
	
	return edges


if __name__ == "__main__":
    #Vertices
    vertices = read_vertices()
    # Arestas
    edges = read_edges()

    adj_list = AdjacencyList(vertices, edges)
    adj_list.display_adjacency_list()
    adj_list.get_all_degrees()



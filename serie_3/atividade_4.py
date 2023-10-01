from src.AdjList import AdjacencyList
import networkx as nx
import matplotlib.pyplot as plt

def read_vertices():
	vertices = []
	
	with open('serie_3/arquivos/destinos_latam.txt', 'r') as file:
		for line in file:
			vertices.append(line.strip())
	
	return vertices

def read_edges():
	edges = []
	
	with open('serie_3/arquivos/rotas.txt', 'r') as file:
		for line in file:
			vertices = line.strip().split(',')
			if len(vertices) == 2:
				edges.append((vertices[0].strip(), vertices[1].strip()))
	
	return edges

def render_graph(vertices, edges):
	g = nx.Graph()
	g.add_nodes_from(vertices)
	g.add_edges_from(edges)

	nx.draw(g, with_labels=True)
	plt.show()  

if __name__ == "__main__":
	#Vertices
	vertices = read_vertices()
	# Arestas
	edges = read_edges()

	render_graph(vertices, edges)

	adj_list = AdjacencyList(vertices, edges)
	adj_list.display_adjacency_list()

	adj_list.get_all_degrees()
		
	# exemplo que não é subgrafo
	subgraph_vertices = ['São Paulo', 'Florianópolis', 'Porto Alegre']
	subgraph_edges = [['São Paulo', 'Florianópolis'], ['Florianópolis', 'Porto Alegre']]

	if(adj_list.is_subgraph(subgraph_vertices, subgraph_edges)):
		print(f"Vértices {subgraph_vertices}; arestas {subgraph_edges} é subgrafo")
	else:
		print(f"Vértices {subgraph_vertices}; arestas {subgraph_edges} NÃO é subgrafo")

	# exemplo de subgrafo
	subgraph_vertices = ['Fortaleza', 'Goiânia', 'Rio de Janeiro', 'Brasilia']
	subgraph_edges = [['Fortaleza', 'Rio de Janeiro'], ['Rio de Janeiro', 'Brasilia'], ['Brasilia', 'Goiânia']]

	if(adj_list.is_subgraph(subgraph_vertices, subgraph_edges)):
		print(f"Vértices {subgraph_vertices}; arestas {subgraph_edges} é subgrafo")
	else:
		print(f"Vértices {subgraph_vertices}; arestas {subgraph_edges} NÃO é subgrafo")

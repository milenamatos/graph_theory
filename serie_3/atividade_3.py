from src.AdjList import AdjacencyList

def read_vertices():
	vertices = []
	
	with open('serie_3/arquivos/estacoes.txt', 'r') as file:
		for line in file:
			vertices.append(line.strip())
	
	return vertices

def read_edges():
	edges = []
	
	with open('serie_3/arquivos/conexoes.txt', 'r') as file:
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
		
	# exemplo que não é subgrafo
	subgraph_vertices = ['Pinheiros', 'Faria Lima', 'Oscar Freire']
	subgraph_edges = [['Pinheiros', 'Faria Lima'], ['Faria Lima', 'Oscar Freire']]

	if(adj_list.is_subgraph(subgraph_vertices, subgraph_edges)):
		print(f"Vértices {subgraph_vertices}; arestas {subgraph_edges} é subgrafo")
	else:
		print(f"Vértices {subgraph_vertices}; arestas {subgraph_edges} NÃO é subgrafo")

	# exemplo de subgrafo
	subgraph_vertices = ['Luz', 'República', 'Higienópolis', 'Tiradentes']
	subgraph_edges = [['Luz', 'República'], ['República', 'Higienópolis'], ['Tiradentes', 'Luz']]

	if(adj_list.is_subgraph(subgraph_vertices, subgraph_edges)):
		print(f"Vértices {subgraph_vertices}; arestas {subgraph_edges} é subgrafo")
	else:
		print(f"Vértices {subgraph_vertices}; arestas {subgraph_edges} NÃO é subgrafo")

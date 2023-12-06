import networkx as nx
import matplotlib.pyplot as plt

class Grafo:
    def __init__(self, vertices, arestas):
        self.vertices = vertices
        self.arestas = arestas
        self.adjacencias = {v: [] for v in vertices}

        for aresta in arestas:
            v1, v2 = aresta
            self.adjacencias[v1].append(v2)
            self.adjacencias[v2].append(v1)

    def dfs(self, vertice, visitados, pai):
        visitados.add(vertice)

        for vizinho in self.adjacencias[vertice]:
            if vizinho not in visitados:
                if self.dfs(vizinho, visitados, vertice):
                    return True
            elif vizinho != pai:
                return True

        return False

    def eh_conexo(self):
        visitados = set()
        self.dfs(list(self.vertices)[0], visitados, None)
        return len(visitados) == len(self.vertices)

    def tem_ciclo(self):
        visitados = set()

        for vertice in self.vertices:
            if vertice not in visitados:
                if self.dfs(vertice, visitados, None):
                    return True

        return False

    def eh_minimamente_conectado(self):
        return self.eh_conexo() and not self.tem_ciclo() and len(self.arestas) == len(self.vertices) - 1


# G1
V1 = [1, 2, 3, 4, 5]
E1 = [(1, 2), (1, 3), (2, 4), (2, 5)]

# Criar o grafo
grafo1 = Grafo(V1, E1)

# Verificar propriedades
conexo = grafo1.eh_conexo()
sem_ciclo = not grafo1.tem_ciclo()
minimamente_conectado = grafo1.eh_minimamente_conectado()

# Imprimir resultados
print(f"G1 é conexo: {conexo}")
print(f"G1 não possui ciclos: {sem_ciclo}")
print(f"G1 é minimamente conectado: {minimamente_conectado}")

# Verificar se é uma árvore
if conexo and sem_ciclo and minimamente_conectado:
    print("G1 é uma árvore.")

    # Plotar o grafo
    G = nx.Graph()
    G.add_nodes_from(V1)
    G.add_edges_from(E1)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_color='black', font_size=10, edge_color='gray')
    plt.show()
else:
    print("G1 não é uma árvore.")

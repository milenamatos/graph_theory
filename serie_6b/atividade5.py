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

    def eh_arvore(self):
        return self.eh_minimamente_conectado()


    # Plotar o grafo
    def plotar_grafo(self):
        G = nx.Graph()
        G.add_nodes_from(self.vertices)
        G.add_edges_from(self.arestas)
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_color='black', font_size=10, edge_color='gray')
        plt.show()


# G1
V1 = [1, 2, 3, 4, 5]
E1 = [(1, 2), (1, 3), (2, 4), (2, 5)]

# Criar o grafo
grafo1 = Grafo(V1, E1)

# Verificar propriedades
resultado = grafo1.eh_arvore()

# Imprimir resultados
if resultado:
    print("G1 é uma árvore.")
    grafo1.plotar_grafo()

else:
    print("G1 não é uma árvore.")


# G2
V2 = [1, 2, 3, 4, 5, 6, 7]
E2 = [(1, 4), (1, 6), (2, 7), (2, 5), (2, 3), (4, 5)]

# Criar o grafo
grafo2 = Grafo(V2, E2)

# Verificar propriedades
resultado = grafo2.eh_arvore()

# Imprimir resultados
if resultado:
    print("G2 é uma árvore.")
    grafo2.plotar_grafo()

else:
    print("G2 não é uma árvore.")

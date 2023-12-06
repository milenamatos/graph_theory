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

    def distancia_entre_vertices(self, vi, vj):
        # Verificar se os vértices são válidos
        if vi not in self.vertices or vj not in self.vertices:
            raise ValueError("Vértices inválidos")

        # Implementar busca em largura (BFS) para calcular a distância
        visitados = set()
        fila = [(vi, 0)]  # A tupla (vértice, distância) será usada na fila
        visitados.add(vi)

        while fila:
            vertice_atual, distancia_atual = fila.pop(0)

            if vertice_atual == vj:
                return distancia_atual

            for vizinho in self.adjacencias[vertice_atual]:
                if vizinho not in visitados:
                    fila.append((vizinho, distancia_atual + 1))
                    visitados.add(vizinho)

        # Se os vértices não estão conectados, retorna -1 ou algum valor indicando distância infinita
        return -1

    def excentricidade_vertice(self, vi):
        # Verificar se o vértice é válido
        if vi not in self.vertices:
            raise ValueError("Vértice inválido")

        # Calcular a distância entre o vértice vi e todos os outros vértices
        distancias = [self.distancia_entre_vertices(vi, vj) for vj in self.vertices]

        # A excentricidade é a maior distância calculada
        return max(distancias)

    def todas_as_excentricidades(self):
        for v in self.vertices:
            excentricidade = self.excentricidade_vertice(v)
            print(f"Excentricidade de {v}: {excentricidade}")

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

# Verificar todas as excentricidades
grafo1.todas_as_excentricidades()

# Plotar grafo
grafo1.plotar_grafo()

# G2
V2 = [1, 2, 3, 4, 5, 6, 7]
E2 = [(1, 4), (1, 6), (2, 7), (2, 5), (2, 3), (4, 5)]

# Criar o grafo
grafo2 = Grafo(V2, E2)

# Verificar todas as excentricidades
grafo2.todas_as_excentricidades()

# Plotar grafo
grafo2.plotar_grafo()

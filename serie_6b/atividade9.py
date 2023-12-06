import matplotlib.pyplot as plt
import networkx as nx

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

    def encontrar_centro_arvore(self):
        # Inicializar variáveis para armazenar os centros
        centros = []
        menor_excentricidade = float('inf')

        # Iterar sobre todos os vértices para calcular as excentricidades
        for vi in self.vertices:
            excentricidade_vi = self.excentricidade_vertice(vi)

            # Se a excentricidade for menor ou igual, adicionar ao conjunto de centros
            if excentricidade_vi < menor_excentricidade:
                centros = [vi]
                menor_excentricidade = excentricidade_vi
            elif excentricidade_vi == menor_excentricidade:
                centros.append(vi)

        return centros

    def encontrar_raio(self):
        centros = self.encontrar_centro_arvore()
        raio = self.excentricidade_vertice(centros[0])
        return raio

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
grafo1 = Grafo(V1, E1)

raio = grafo1.encontrar_raio()
plotar_grafo(grafo1)
print(f"Raio da árvore: {raio}")

# G2
V2 = [1, 2, 3, 4, 5, 6, 7]
E2 = [(1, 4), (1, 6), (2, 7), (2, 5), (2, 3), (4, 5)]
grafo2 = Grafo(V2, E2)

raio = grafo2.encontrar_raio()
plotar_grafo(grafo2)
print(f"Raio da árvore: {raio}")

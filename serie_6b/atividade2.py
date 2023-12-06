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

# Plotar o grafo
def plotar_grafo(grafo):
    G = {v: [] for v in grafo.vertices}
    for aresta in grafo.arestas:
        v1, v2 = aresta
        G[v1].append(v2)
        G[v2].append(v1)

    pos = {v: (v % 2, v // 2) for v in grafo.vertices}  # Layout básico para este exemplo
    for v in grafo.vertices:
        plt.scatter(*pos[v], color='skyblue', s=500)
        plt.text(pos[v][0], pos[v][1], str(v), fontsize=12, ha='center', va='center')

    for aresta in grafo.arestas:
        v1, v2 = aresta
        plt.plot([pos[v1][0], pos[v2][0]], [pos[v1][1], pos[v2][1]], color='gray', linestyle='-', linewidth=2)

    plt.title("Grafo")
    plt.axis('off')
    plt.show()

# Plotar o grafo com destaque na excentricidade
def plotar_grafo_com_excentricidade(grafo, vi):
    G = {v: [] for v in grafo.vertices}
    for aresta in grafo.arestas:
        v1, v2 = aresta
        G[v1].append(v2)
        G[v2].append(v1)

    pos = {v: (v % 2, v // 2) for v in grafo.vertices}
    excentricidade_vi = grafo.excentricidade_vertice(vi)

    for v in grafo.vertices:
        cor = 'skyblue' if v != vi else 'red'  # Destaque na excentricidade
        plt.scatter(*pos[v], color=cor, s=500)
        plt.text(pos[v][0], pos[v][1], str(v), fontsize=12, ha='center', va='center')

    for aresta in grafo.arestas:
        v1, v2 = aresta
        plt.plot([pos[v1][0], pos[v2][0]], [pos[v1][1], pos[v2][1]], color='gray', linestyle='-', linewidth=2)

    plt.title(f"Grafo com destaque na excentricidade de {vi}")
    plt.axis('off')
    plt.show()

############ Exercício A
V1 = [1, 2, 3, 4, 5]
E1 = [(1, 2), (1, 3), (2, 4), (2, 5)]

grafo1 = Grafo(V1, E1)

# Calcular a distância entre dois vértices (por exemplo, entre 1 e 4)
vi = 1
vj = 4
distancia = grafo1.distancia_entre_vertices(vi, vj)
print(f"A distância entre os vértices {vi} e {vj} é {distancia}.")

# Chamar a função de plotagem
plotar_grafo(grafo1)

############## Exercício B
V2 = [1, 2, 3, 4, 5, 6]
E2 = [(1, 2), (1, 3), (2, 4), (2, 5), (5, 6)]

grafo2 = Grafo(V2, E2)

# Calcular e imprimir a excentricidade de um vértice (por exemplo, vértice 1)
vi = 1
excentricidade = grafo2.excentricidade_vertice(vi)
print(f"A excentricidade do vértice {vi} é {excentricidade}.")

# Chamar a função de plotagem com destaque na excentricidade
plotar_grafo_com_excentricidade(grafo2, vi)

############## Exercício C

# Encontrar e imprimir o centro da árvore
centros = grafo2.encontrar_centro_arvore()
plotar_grafo(grafo2)
print(f"Centro da árvore: {centros}")

# G2
V2 = [1, 2, 3, 4, 5, 6, 7]
E2 = [(1, 4), (1, 6), (2, 7), (2, 5), (2, 3), (4, 5)]
grafo2 = Grafo(V2, E2)

centros = grafo2.encontrar_centro_arvore()
plotar_grafo(grafo2)
print(f"Centro da árvore: {centros}")

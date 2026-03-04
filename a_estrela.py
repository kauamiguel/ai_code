import heapq

grafo = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 5)],
    'D': [],
    'E': [('G', 2)],
    'F': [('G', 1)],
    'G': []
}

heuristica = {
    'A': 4,
    'B': 2,
    'C': 4,
    'D': 6,
    'E': 1,
    'F': 1,
    'G': 0
}

def a_star(grafo, heuristica, inicio, objetivo):
    fila = []
    heapq.heappush(fila, (0,inicio))

    g_custo = {inicio: 0}

    pais = {inicio: None}

    while fila:
        f_atual, no_atual = heapq.heappop(fila)

        if no_atual == objetivo:
            caminho = []
            while no_atual:
                caminho.append(no_atual)
                no_atual = pais[no_atual]
            return caminho[::-1]
        for vizinho, custo in grafo[no_atual]:
            novo_g = g_custo[no_atual] + custo

            if vizinho not in g_custo or novo_g < g_custo[vizinho]:
                g_custo[vizinho] = novo_g
                f = novo_g + heuristica[vizinho]
                heapq.heappush(fila, (f, vizinho))
                pais[vizinho] = no_atual
    return None

caminho = a_star(grafo, heuristica, 'A', 'G')
print("Menor caminho:", caminho)

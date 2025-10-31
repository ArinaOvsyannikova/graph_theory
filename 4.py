import time

def floyd_warshall(graph):
    n = len(graph)  # Получаем количество вершин в графе
    dist = [[float('inf') for _ in range(n)] for _ in range(n)]  # Инициализируем матрицу расстояний

    for i in range(n):
        dist[i][i] = 0  # Устанавливаем расстояние от вершины до самой себя равным 0

    vertices = list(graph.keys())  # Получаем список вершин графа

    for i, u in enumerate(vertices):
        for j, v in enumerate(vertices):
            if v in graph[u]:  # Проверяем наличие ребра между вершинами
                dist[i][j] = graph[u][v]  # Заполняем матрицу расстояний весами ребер

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])  # Обновляем кратчайшее расстояние

    return dist  # Возвращаем матрицу кратчайших расстояний

# Пример графа для алгоритма Флойда-Уоршелла с учетом весов ребер
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1},
    'E': {'F': 2, 'G': 8},
    'F': {'E': 2, 'G': 3},
    'G': {'E': 8, 'F': 3}
}

# Вызов функции для нахождения кратчайших путей между всеми парами вершин
shortest_paths = floyd_warshall(graph)
print(shortest_paths)

# Оценка скорости работы алгоритма
start_time = time.time()  # Засекаем начало выполнения алгоритма

end_time = time.time()  # Засекаем конец выполнения алгоритма
execution_time = end_time - start_time  # Вычисляем время выполнения
print("Время выполнения алгоритма: {:.6f} секунд".format(execution_time))

import heapq


def dijkstra(graph, start):
    # Инициализация расстояний до всех вершин как бесконечность, кроме стартовой
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    # Очередь с приоритетами для хранения вершин и их расстояний
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Проверка, не является ли текущее расстояние больше, чем уже известное
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Если найденное расстояние до соседней вершины меньше, обновляем его
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# Пример графа в виде словаря с весами ребер
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1},
    'E':{ 'F': 2, 'G': 8},
    'F':{'E':2, 'G': 3},
    'G':{'E': 8, 'F':3}
}

# Вызов функции для поиска кратчайших путей от вершины 'A'
shortest_paths_from_A = dijkstra(graph, 'A')
print(shortest_paths_from_A)

import time


def shortest_path(graph, start, end):
    if end not in graph:
        return "Конечная вершина не найдена в графе. Кратчайший путь не существует."

    distances = dijkstra(graph, start)

    if distances[end] == float('infinity'):
        return "Кратчайший путь не существует."

    path = []
    current_vertex = end
    while current_vertex != start:
        path.insert(0, current_vertex)
        for neighbor, weight in graph[current_vertex].items():
            if distances[current_vertex] == distances[neighbor] + weight:
                current_vertex = neighbor
                break
    path.insert(0, start)

    return path

    return path



# Пример использования для нахождения кратчайшего пути между вершинами 'A' и 'D'
shortest_path_AD = shortest_path(graph, 'A', 'G')
print(shortest_path_AD)

# Оценка скорости работы алгоритма
start_time = time.time()
# Здесь можно добавить вызов алгоритма для больших графов или многократные вызовы для оценки времени
end_time = time.time()
execution_time = end_time - start_time
print("Время выполнения алгоритма: {:.6f} секунд".format(execution_time))

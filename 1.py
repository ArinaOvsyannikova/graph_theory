
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import random
from datetime import datetime
import time


# Создание матрицы смежности
adj_matrix = np.zeros((20, 20))
random.seed(datetime.now().timestamp())
# Задаем связи для первой компоненты
for i in range(10):
    for j in range(i,10):
        if i != j:
            adj_matrix[i][j] = random.randint(0, 1)

# Задаем связи для второй компоненты (вершины с 7 по 14)
for i in range(10, 20):
    for j in range(i, 20):
        if i != j:
            adj_matrix[i][j] = random.randint(0, 1)

print(adj_matrix)

# Преобразование матрицы смежности в список ребер
edges = []
for i in range(len(adj_matrix)):
    for j in range(len(adj_matrix[i])):
        if adj_matrix[i][j]:
            edges.append((i+1,j+1))

# Вывод списка ребер
print("Список ребер:")
for edge in edges:
    print(edge)

# Создание графа из списка ребер
G = nx.Graph(edges)

# Отображение графа
nx.draw(G, with_labels=True)
plt.title('Граф из списка ребер')
plt.show()

# Создание матрицы смежности из списка ребер
num_vertices = max(max(edge) for edge in edges) +1
adj_matrix_new = np.zeros((num_vertices,num_vertices))

for edge in edges:
    adj_matrix_new[edge[0]-1][edge[1]-1] = adj_matrix_new[edge[1]-1][edge[0]-1] = 1

# Вывод матрицы смежности
print("\nМатрица смежности:")
for row in adj_matrix_new:
     print(row)

# Создание графа из матрицы смежности
G_new = nx.Graph(adj_matrix_new)

nx.draw(G_new, with_labels=True)
plt.title('Граф из матрицы смежности')
plt.show()


#2
start_time = time.time()

def logical_matrix(matrix):
    reachability_matrix = np.array(matrix, copy=True)
    n = len(reachability_matrix)
    for u in range (n-1):
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    reachability_matrix = np.logical_or(reachability_matrix, np.dot(reachability_matrix, reachability_matrix))

    return reachability_matrix.astype(int)
reachability_matrix = logical_matrix(adj_matrix_new)
print(reachability_matrix)

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Прошло времени: {elapsed_time} секунд")

print()
# 3 задание
start_time = time.time()
def warshall_algorithm(matrix):
    reachability_matrix = np.array(matrix)
    n = len(reachability_matrix)

    for i in range(n):
        for j in range(n):
            for k in range(n):

                    reachability_matrix[i][j] = reachability_matrix[i][j] or (reachability_matrix[i][k] and reachability_matrix[k][j])

    return reachability_matrix

reachability_matrix = warshall_algorithm(adj_matrix_new)
print(reachability_matrix.astype(int))
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Прошло времени: {elapsed_time} секунд")

n = len(reachability_matrix.astype(int))
def find_connected_components(reachability_matrix):
    components = []

    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            component = []
            stack = [i]
            while stack:
                vertex = stack.pop()
                if not visited[vertex]:
                    visited[vertex] = True
                    component.append(vertex)
                    for j in range(n):
                        if reachability_matrix[vertex][j] and not visited[j]:
                            stack.append(j)
            components.append(component)
    return components

components = find_connected_components(reachability_matrix.astype(int))
print("Компоненты связности:")
for component in components:
    print(component)










import networkx as nx

# Чтение графа из файла
with open('data_mo5_1.txt', 'r') as f:
    edges = [tuple(map(int, line.split())) for line in f.readlines()]

# Создание графа
G = nx.Graph()
G.add_weighted_edges_from(edges)

# Построение минимального остовного дерева
mst = nx.minimum_spanning_tree(G)

# Вывод результата
print("Ребра минимального остовного дерева:")
for edge in mst.edges(data=True):
    print(edge)

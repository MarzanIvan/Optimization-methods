import networkx as nx

# Пример чтения графа для кратчайшего пути
def shortest_path(graph_file, start, end):
    G = nx.read_weighted_edgelist(graph_file)
    path = nx.dijkstra_path(G, source=start, target=end)
    return path

# Пример чтения графа для максимального потока
def max_flow(graph_file, source, sink):
    G = nx.read_edgelist(graph_file, data=(('capacity', int),))
    flow_value, flow_dict = nx.maximum_flow(G, _s=source, _t=sink)
    return flow_value, flow_dict

# Пример чтения графа для потока наименьшей стоимости
def min_cost_flow(graph_file, source, sink):
    G = nx.read_weighted_edgelist(graph_file, create_using=nx.DiGraph)
    flowCost, flowDict = nx.network_simplex(G)
    return flowCost, flowDict

# Примеры вызовов функций
def main():
    shortest_path_result = shortest_path('data_mo5_2_1.txt', '1', '4')
    print(f"Кратчайший путь от 1 до 4: {shortest_path_result}")

    max_flow_result, flow_dict = max_flow('data_mo5_2_2.txt', '0', '1')
    print(f"Максимальный поток от 0 до 1: {max_flow_result}")
    print(f"Словарь потоков: {flow_dict}")

    min_cost_flow_result, flow_cost_dict = min_cost_flow('data_mo5_2_3.txt', '0', '1')
    print(f"Стоимость потока от 0 до 1: {min_cost_flow_result}")
    print(f"Словарь потоков при наименьшей стоимости: {flow_cost_dict}")

if __name__ == "__main__":
    main()

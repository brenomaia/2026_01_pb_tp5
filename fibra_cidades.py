from min_heap_tuple import BinaryHeap

class Connection:
    def __init__(self, origin, dest, cost, latency):
        self.origin = origin
        self.dest = dest
        self.cost = cost
        self.latency = latency


cities_num = 30
# origin, destination, cost, latency
connections = [
    (0, 1, 45, 3), (0, 2, 60, 8), (0, 3, 75, 12), (1, 2, 20, 2), (1, 4, 55, 6),
    (2, 3, 35, 4), (2, 5, 40, 5), (3, 6, 80, 10), (4, 5, 15, 1), (4, 7, 90, 14),
    (5, 6, 30, 3), (5, 8, 50, 7), (6, 9, 65, 9), (7, 8, 25, 2), (7, 10, 70, 11),
    (8, 9, 45, 5), (8, 11, 60, 8), (9, 12, 85, 13), (10, 11, 15, 1), (10, 13, 50, 6),
    (11, 12, 40, 4), (11, 14, 55, 7), (12, 15, 75, 10), (13, 14, 30, 3), (13, 16, 65, 9),
    (14, 15, 35, 4), (14, 17, 45, 6), (15, 18, 90, 15), (16, 17, 20, 2), (16, 19, 55, 8),
    (17, 18, 40, 5), (17, 20, 60, 9), (18, 21, 80, 12), (19, 20, 25, 3), (19, 22, 70, 11),
    (20, 21, 35, 4), (20, 23, 50, 7), (21, 24, 75, 10), (22, 23, 15, 1), (22, 25, 60, 8),
    (23, 24, 45, 6), (23, 26, 55, 7), (24, 27, 90, 14), (25, 26, 30, 3), (25, 28, 65, 9),
    (26, 27, 40, 5), (26, 29, 70, 11), (27, 29, 50, 6), (28, 29, 25, 2), (0, 4, 110, 18),
    (1, 5, 85, 11), (2, 6, 95, 14), (3, 9, 120, 22), (4, 8, 70, 9), (5, 9, 60, 8),
    (6, 12, 110, 16), (7, 11, 65, 9), (8, 12, 80, 11), (9, 15, 130, 24), (10, 14, 55, 7),
    (11, 15, 70, 9), (12, 18, 115, 19), (13, 17, 60, 8), (14, 18, 75, 10), (15, 21, 140, 25),
    (16, 20, 65, 9), (17, 21, 85, 12), (18, 24, 125, 20), (19, 23, 60, 8), (20, 24, 80, 11),
    (21, 27, 135, 23), (22, 26, 55, 7), (23, 27, 75, 10), (24, 29, 110, 17), (0, 7, 200, 35),
    (3, 12, 180, 28), (10, 19, 150, 22), (13, 22, 140, 21), (16, 25, 160, 26), (1, 8, 95, 13),
    (2, 9, 105, 15), (7, 13, 85, 12), (11, 17, 90, 13), (19, 25, 80, 12), (20, 26, 85, 13)
]

def mst(cities: int, graph: list[Connection]):
    heap = BinaryHeap()
    visited = set()
    current_city = 0
    
    heap.insert((0, None, current_city))
    
    final_graph = {}
    total_cost = 0

    while heap.data and len(visited) < cities:
        cost, origin, dest = heap.extract_min()
        current_city = dest
        total_cost += cost

        visited.add(current_city)
        final_graph[origin] = final_graph.get(origin, [(current_city, cost)])

        for conn in graph:
            if conn.origin == current_city and conn.dest not in visited:
                heap.insert((conn.cost, conn.origin, conn.dest))

    final_graph.pop(None)
    print(f'Custo total de implementação da fibra: {total_cost}')
    print(f'\n\nDesenho final da fibra: {final_graph}')
    return final_graph
        

def dijkstra(cities: int, initial_city: int, graph: list[Connection]):
    heap = BinaryHeap()
    visited = set()

    heap.insert((0, initial_city))
    result_graph = {}

    while heap.data and len(visited) < cities:
        latency, city = heap.extract_min()

        if latency > result_graph.get(city, float("inf")):
            continue

        visited.add(city)
        result_graph[city] = latency

        for conn in graph:
            if conn.origin == city and conn.dest not in visited:
                heap.insert((latency + conn.latency, conn.dest))

    print(f'Grafo de latência: {result_graph}')
    return result_graph


def main(connections: list[tuple]):
    connections_transformed = []
    for conn in connections:
        structured_conn = Connection(conn[0], conn[1], conn[2], conn[3])
        connections_transformed.append(structured_conn)

    print('Calculando custo de implementação da filtra')
    mst(30, connections_transformed)

    print('\n\n\nMontando grafo de latência: ')
    dijkstra(30, 0, connections_transformed)



main(connections)
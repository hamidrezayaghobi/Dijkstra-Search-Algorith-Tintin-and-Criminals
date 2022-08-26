from sys import stdin, stdout
from heapq import heappush, heappop


class Graph:
    vert_dict = {}

    def __init__(self, source_node, target_node, weight):
        Graph.vert_dict[source_node].append((target_node, weight))
        Graph.vert_dict[target_node].append((source_node, weight))

    @staticmethod
    def clear_memory():
        Graph.vert_dict = {}


def dijkstra(start_city, end_city):
    best_path = {}
    heap = []
    graph = Graph.vert_dict
    pre_city_dict = {}
    heappush(heap, (0, start_city, None))

    while heap:
        path_distance, last_reached_node, pre_city = heappop(heap)
        if last_reached_node in best_path:
            continue
        best_path[last_reached_node] = path_distance
        pre_city_dict[last_reached_node] = pre_city
        if last_reached_node == end_city:
            path = []
            while last_reached_node:
                path.append(last_reached_node)
                last_reached_node = pre_city_dict[last_reached_node]

            path.reverse()
            return best_path[end_city], path
        else:
            for neighbour, weight in graph[last_reached_node]:
                heappush(heap, (path_distance + weight, neighbour, last_reached_node))
    return None


def villain_dijkstra(end_city, villain_location, car_location):
    best_path = {}
    heap = []
    graph = Graph.vert_dict
    for villain in villain_location:
        heappush(heap, (0, villain, 2 if villain in car_location else 1))

    while heap:
        path_distance, last_reached_node, velocity = heappop(heap)
        if last_reached_node in best_path:
            continue
        best_path[last_reached_node] = path_distance
        if last_reached_node in car_location:
            velocity = 2
        if last_reached_node == end_city:
            break
        else:
            for neighbour, weight in graph[last_reached_node]:
                heappush(heap, (path_distance + weight / velocity, neighbour, velocity))
    if not best_path[end_city]:
        return 10E6
    return best_path[end_city]


def run_experiment():
    city_count, road_count = [int(i) for i in stdin.readline().split()]
    Graph.vert_dict = {i: [] for i in range(1, city_count + 1)}
    for road in range(road_count):
        u, v, d = [int(i) for i in stdin.readline().split()]
        Graph(u, v, d)

    villain_count = stdin.readline()
    villain_location = [int(i) for i in stdin.readline().split()]

    car_count = stdin.readline()
    car_location = [int(x) for x in stdin.readline().split()]

    s, g = [int(x) for x in stdin.readline().split()]

    if g in villain_location:
        return "Poor Tintin\n"

    total_tintin_time, tintin_path = dijkstra(s, g)
    villain_time_to_tintin = villain_dijkstra(g, villain_location, car_location)
    if villain_time_to_tintin < total_tintin_time:
        return "Poor Tintin\n"
    else:
        return str(total_tintin_time) + "\n" + str(len(tintin_path)) + "\n" + " ".join(map(str, tintin_path)) + "\n"


string_output = ""
experiment_count = int(stdin.readline())
for exp in range(experiment_count):
    string_output = string_output + run_experiment()
    Graph.clear_memory()

stdout.write(string_output)

def dijkstra(graph, start):
    num_vertices = len(graph)
    visited = [False] * num_vertices
    distances = [float('inf')] * num_vertices
    distances[start] = 0

    for _ in range(num_vertices):
        min_dist = float('inf')
        min_index = -1

        for v in range(num_vertices):
            if not visited[v] and distances[v] < min_dist:
                min_dist = distances[v]
                min_index = v

        visited[min_index] = True

        for v in range(num_vertices):
            if not visited[v] and graph[min_index][v] != 0:
                new_dist = distances[min_index] + graph[min_index][v]
                if new_dist < distances[v]:
                    distances[v] = new_dist

    return distances


# Example usage:
graph = [
    [0, 4, 0, 0, 0, 0, 0, 8, 0],
    [4, 0, 8, 0, 0, 0, 0, 11, 0],
    [0, 8, 0, 7, 0, 4, 0, 0, 2],
    [0, 0, 7, 0, 9, 14, 0, 0, 0],
    [0, 0, 0, 9, 0, 10, 0, 0, 0],
    [0, 0, 4, 14, 10, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 1, 6],
    [8, 11, 0, 0, 0, 0, 1, 0, 7],
    [0, 0, 2, 0, 0, 0, 6, 7, 0]
]

start_vertex = 0
distances = dijkstra(graph, start_vertex)

print("Shortest distances from vertex", start_vertex, "to all other vertices:")
for i, distance in enumerate(distances):
    print("Vertex", i, ":", distance)

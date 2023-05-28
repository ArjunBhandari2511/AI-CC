def dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()

        if vertex not in visited:
            visited.add(vertex)
            print(vertex, end=" ")  # Process the vertex

            # Add unvisited neighbors to the stack
            stack.extend(graph[vertex] - visited)

# Test the function
graph = {
        'A': {'B', 'C'},
        'B': {'A', 'D', 'E'},
        'C': {'A', 'F'},
        'D': {'B'},
        'E': {'B'},
        'F': {'C'}
    }

start_vertex = 'A'
print("DFS traversal starting from vertex", start_vertex)
dfs(graph, start_vertex)

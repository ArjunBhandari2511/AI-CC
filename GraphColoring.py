def is_safe(graph, colors, vertex, color):
    for neighbor in graph[vertex]:
        if colors[neighbor] == color:
            return False
    return True

def graph_coloring(graph, num_colors):
    num_vertices = len(graph)
    colors = [-1] * num_vertices
    colors[0] = 0
    stack = [(0, 1)]  # (vertex, next_color)

    while stack:
        vertex, next_color = stack.pop()

        while next_color < num_colors:
            if is_safe(graph, colors, vertex, next_color):
                colors[vertex] = next_color
                break
            next_color += 1

        if next_color == num_colors:
            colors[vertex] = -1  # Reset color if no valid color found
            if vertex == 0:  # All possibilities explored
                return None
            stack.append((vertex, 0))  # Backtrack to previous vertex
        else:
            if vertex == num_vertices - 1:  # Solution found
                return colors
            stack.append((vertex + 1, 1))  # Move to next vertex

    return None  # No solution found


# Example usage
graph = {
    0: [1, 2, 3],
    1: [0, 2],
    2: [0, 1, 3],
    3: [0, 2]
}
num_colors = 3

colors = graph_coloring(graph, num_colors)
if colors is not None:
    print("Solution found:")
    for vertex, color in enumerate(colors):
        print(f"Vertex {vertex}: Color {color}")
else:
    print("No solution exists.")

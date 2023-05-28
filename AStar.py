def heuristic(node, goal):
    # Calculate the Manhattan distance heuristic between the current node and the goal node
    x1, y1 = node
    x2, y2 = goal
    return abs(x1 - x2) + abs(y1 - y2)


def a_star_search(graph, start, goal):
    # Initialize the open and closed sets
    open_set = [start]
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}

    while open_set:
        # Find the node with the lowest f_score value
        current = min(open_set, key=lambda node: f_score[node])

        if current == goal:
            # Reconstruct the path
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            path.reverse()
            return path

        open_set.remove(current)
        for neighbor in graph[current]:
            # Calculate the tentative g_score
            tentative_g_score = g_score[current] + 1

            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                # Update the path
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal)
                if neighbor not in open_set:
                    open_set.append(neighbor)

    return None


# Test the A* algorithm
graph = {
    (0, 0): [(1, 0), (0, 1)],
    (1, 0): [(0, 0), (2, 0)],
    (0, 1): [(0, 0), (0, 2)],
    (2, 0): [(1, 0), (3, 0)],
    (0, 2): [(0, 1), (0, 3)],
    (3, 0): [(2, 0)]
}

start_node = (0, 0)
goal_node = (3, 0)
path = a_star_search(graph, start_node, goal_node)
if path:
    print(f"Shortest path from {start_node} to {goal_node}:")
    for node in path:
        print(node)
else:
    print(f"No path found from {start_node} to {goal_node}.")

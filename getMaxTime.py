def getMaxTime(g_nodes, g_from, g_to):
    # Step 1: Build the adjacency list representation of the tree
    graph = {i: [] for i in range(1, g_nodes + 1)}

    for u, v in zip(g_from, g_to):
        graph[u].append(v)
        graph[v].append(u)

    # Step 2: BFS function using a simple list as a queue
    def bfs(start):
        visited = set()
        queue = [(start, 0)]  # (node, distance)
        farthest_node, max_distance = start, 0
        front = 0  # Pointer to simulate queue behavior

        while front < len(queue):
            node, dist = queue[front]
            front += 1  # Move pointer instead of using pop(0) for efficiency

            if node not in visited:
                visited.add(node)
                farthest_node, max_distance = node, dist  # Update farthest node

                for neighbor in graph[node]:
                    if neighbor not in visited:
                        queue.append((neighbor, dist + 1))

        return farthest_node, max_distance

    # Step 3: Run BFS twice to find the tree's diameter
    farthest_node, _ = bfs(1)  # Find farthest node from an arbitrary node (1)
    _, max_time = bfs(farthest_node)  # Find the longest path from that node

    return max_time

# Updated Example Input
g_nodes = 5
g_from = [1, 5, 1, 5]
g_to = [5, 3, 2, 4]
print(getMaxTime(g_nodes, g_from, g_to))  # Output: 3

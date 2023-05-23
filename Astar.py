def astar():
    # Input graph as adjacency list
    graph = {}
    num_edges = int(input("Enter the number of edges: "))
    for i in range(num_edges):
        u, v, cost = input("Enter edge as 'start,end cost': ").split()
        cost = int(cost)
        if u not in graph:
            graph[u] = {}
        graph[u][v] = cost
        if v not in graph:
            graph[v] = {}
        graph[v][u] = cost  # assuming undirected graph

    # Input start and goal nodes
    start = input("Enter the start node: ")
    goal = input("Enter the goal node: ")

    # Define heuristic function
    def h(n1, n2):
        # Heuristic function for single character nodes
        return abs(ord(n1) - ord(n2))

    # Run A* algorithm
    frontier = [(0, start)]
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while frontier:
        _, current = min(frontier, key=lambda x: x[0])
        frontier = [node for node in frontier if node[1] != current]

        if current == goal:
            path = []
            while current != start:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
           
            return path

        for next_node in graph[current]:
            new_cost = cost_so_far[current] + graph[current][next_node]
            if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                cost_so_far[next_node] = new_cost
                priority = new_cost + h(next_node, goal)
                frontier.append((priority, next_node))
                came_from[next_node] = current

    return None

path = astar()
if path:
    print("Minimum cost path:", ' -> '.join(path))
else:
    print("No path found")

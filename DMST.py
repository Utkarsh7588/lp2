from heapq import heappop, heappush

def dijkstra_mst(graph, n, start):
    pq = [(0, start)]
    dist = [float('inf')] * n
    dist[start] = 0
    parent = [-1] * n
    mst = []

    while pq:
        d, u = heappop(pq)

        if d != dist[u]:
            continue

        if parent[u] != -1:
            mst.append((parent[u], u, graph[parent[u]][u]))

        for v in range(n):
            if graph[u][v] != 0 and dist[v] > graph[u][v]:
                dist[v] = graph[u][v]
                parent[v] = u
                heappush(pq, (dist[v], v))

    return mst

n = int(input("Enter the number of vertices: "))
m = int(input("Enter the number of edges: "))
graph = [[0] * n for _ in range(n)]

for i in range(m):
    u, v, w = map(int, input("Enter edge {}: ".format(i+1)).split())
    graph[u-1][v-1] = w
    graph[v-1][u-1] = w

start = int(input("Enter the start vertex: ")) - 1
mst = dijkstra_mst(graph, n, start)

print("Edges in the minimum spanning tree:")
visited_edges = set()  # Keep track of visited edges
total_cost = 0  # Initialize total cost

for edge in mst:
    u, v, weight = edge

    # Check if the edge has already been visited
    if (u, v) in visited_edges or (v, u) in visited_edges:
        continue

    visited_edges.add((u, v))
    visited_edges.add((v, u))
    total_cost += weight

    print(f"{u+1} - {v+1}: {weight}")

print("Total Cost of the Minimum Spanning Tree:", total_cost)

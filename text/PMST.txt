import sys

def prim_mst(graph, n):
    mst = []
    visited = [False] * n
    key = [sys.maxsize] * n
    parent = [-1] * n

    key[0] = 0  # Start with the first vertex

    for _ in range(n):
        min_key = sys.maxsize
        u = -1

        # Find the vertex with the minimum key value among the unvisited vertices
        for v in range(n):
            if not visited[v] and key[v] < min_key:
                min_key = key[v]
                u = v

        visited[u] = True

        # Add the edge to the MST
        if parent[u] != -1:
            mst.append((parent[u], u, graph[u][parent[u]]))

        # Update key values of adjacent vertices
        for v in range(n):
            if (
                graph[u][v] != 0
                and not visited[v]
                and graph[u][v] < key[v]
            ):
                key[v] = graph[u][v]
                parent[v] = u

    return mst

n = int(input("Enter the number of vertices: "))
m = int(input("Enter the number of edges: "))
graph = [[0] * n for _ in range(n)]

for i in range(m):
    u, v, w = map(int, input(f"Enter edge {i+1} (u v w): ").split())
    graph[u-1][v-1] = w
    graph[v-1][u-1] = w

mst = prim_mst(graph, n)
print("Edges in the MST:")
for u, v, cost in mst:
    print(f"{u+1} - {v+1}: {cost}")

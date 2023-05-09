from queue import PriorityQueue

def prim_mst(graph, n):
    mst = []
    visited = [False] * n
    pq = PriorityQueue()
    pq.put((0, 0))

    while not pq.empty():
        cost, u = pq.get()

        if visited[u]:
            continue
        visited[u] = True

        if u != 0:
            mst.append((parent, u, cost))

        for v, w in graph[u]:
            if not visited[v]:
                pq.put((w, v))
                parent = u

    return mst

n = int(input("Enter the number of vertices: "))
m = int(input("Enter the number of edges: "))
graph = [[] for _ in range(n)]

for i in range(m):
    u, v, w = map(int, input("Enter edge {}: ".format(i+1)).split())
    graph[u-1].append((v-1, w))
    graph[v-1].append((u-1, w))

mst = prim_mst(graph, n)
print("Edges in the MST:")
for u, v, cost in mst:
    print("{} - {}: {}".format(u+1, v+1, cost))

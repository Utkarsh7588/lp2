def prim_mst(graph, n):
    mst = []
    visited = [False] * n
    pq = []

    def enqueue(item):
        pq.append(item)

    def dequeue():
        min_cost = float('inf')
        min_index = -1
        for i in range(len(pq)):
            if pq[i][0] < min_cost:
                min_cost = pq[i][0]
                min_index = i
        return pq.pop(min_index)

    enqueue((0, 0))

    while pq:
        cost, u = dequeue()

        if visited[u]:
            continue
        visited[u] = True

        if u != 0:
            mst.append((parent, u, cost))

        for v, w in graph[u]:
            if not visited[v]:
                enqueue((w, v))
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

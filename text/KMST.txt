def kruskal_mst(edges, n):
    edges.sort(key=lambda e: e[2])  # Sort edges based on weight
    parent = list(range(n))  # Initialize parent array
    rank = [0] * n  # Initialize rank array
    mst = []  # List to store edges in the MST

    def find(u):
        if parent[u] != u:
            parent[u] = find(parent[u])
        return parent[u]

    def union(u, v):
        u_root, v_root = find(u), find(v)
        if u_root == v_root:
            return
        if rank[u_root] > rank[v_root]:
            parent[v_root] = u_root
        else:
            parent[u_root] = v_root
            if rank[u_root] == rank[v_root]:
                rank[v_root] += 1

    for u, v, w in edges:
        if find(u) != find(v):
            union(u, v)
            mst.append((u, v, w))
        if len(mst) == n - 1:
            break

    return mst

# Take input from user
n = int(input("Enter the number of vertices: "))
m = int(input("Enter the number of edges: "))
edges = []
for i in range(m):
    u, v, w = map(int, input("Enter edge {}: ".format(i+1)).split())
    edges.append((u - 1, v - 1, w))

# Find the minimum spanning tree using Kruskal's algorithm
mst = kruskal_mst(edges, n)

# Print the edges in the minimum spanning tree and their total weight
print("Edges in the minimum spanning tree:")
total_weight = 0
for u, v, w in mst:
    print("{} - {}: {}".format(u + 1, v + 1, w))
    total_weight += w
print("Total weight of the minimum spanning tree:", total_weight)

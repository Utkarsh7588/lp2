# Definition of edge class
class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w

# Definition of disjoint set class
class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        u_root, v_root = self.find(u), self.find(v)
        if u_root == v_root:
            return
        if self.rank[u_root] > self.rank[v_root]:
            self.parent[v_root] = u_root
        else:
            self.parent[u_root] = v_root
            if self.rank[u_root] == self.rank[v_root]:
                self.rank[v_root] += 1

# Definition of Kruskal's algorithm function
def kruskal_mst(edges, n):
    edges.sort(key=lambda e: e.w)
    dsu = DisjointSet(n)
    mst = []
    for e in edges:
        if dsu.find(e.u) != dsu.find(e.v):
            dsu.union(e.u, e.v)
            mst.append(e)
        if len(mst) == n-1:
            break
    return mst

# Take input from user
n = int(input("Enter the number of vertices: "))
m = int(input("Enter the number of edges: "))
edges = []
for i in range(m):
    u, v, w = map(int, input("Enter edge {}: ".format(i+1)).split())
    edges.append(Edge(u-1, v-1, w))

# Find the minimum spanning tree using Kruskal's algorithm
mst = kruskal_mst(edges, n)

# Print the edges in the minimum spanning tree and their total weight
print("Edges in the minimum spanning tree:")
total_weight = 0
for e in mst:
    print("{} - {} : {}".format(e.u+1, e.v+1, e.w))
    total_weight += e.w
print("Total weight of the minimum spanning tree:", total_weight)

class Graph:
    def __init__(self):
        self.graph={}

    def add_edge(self,u,v):
        if u not in self.graph:
            self.graph[u]=[]
        if v not in self.graph:
            self.graph[v]=[]
        self.graph[v].append(u)
        self.graph[u].append(v)
    
    def dfs_util(self, v, visited):
        visited.add(v)
        print(v, end=' ')
        
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.dfs_util(neighbour, visited)
    
    def bfs(self, start):
        queue=[]
        visited=set()
        visited.add(start)
        queue.append(start)
        
        while queue:
            s=queue.pop(0)
            print(s, end=' ')
            for neighbour in self.graph[s]:
                if neighbour not in visited:
                    queue.append(neighbour)
                    visited.add(neighbour)

    def traverse(self, start_vertex):
        visited = set()
        print("Starting traversal from vertex:", start_vertex)
        self.dfs_util(start_vertex, visited)
        print()
        self.bfs(start_vertex)
        print()

g = Graph()
vertices = int(input("Enter the number of vertices: "))
edges = int(input("Enter the number of edges: "))

for i in range(edges):
    u, v = map(int, input(f"Enter edge {i+1} (u v): ").split())
    g.add_edge(u, v)

start_vertex = int(input("Enter the starting vertex: "))
print("Traversal:")
g.traverse(start_vertex)

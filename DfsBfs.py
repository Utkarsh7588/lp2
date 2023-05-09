from collections import defaultdict

# Define a class for the graph
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    # Function to add an edge to the graph
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    # Recursive function for DFS
    def dfs_util(self, v, visited):
        visited.add(v)
        print(v, end=' ')

        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.dfs_util(neighbour, visited)

    # DFS function
    def dfs(self, start):
        visited = set()
        self.dfs_util(start, visited)

    # BFS function
    def bfs(self, start):
        visited = set()
        queue = []
        visited.add(start)
        queue.append(start)

        while queue:
            s = queue.pop(0)
            print(s, end=' ')

            for neighbour in self.graph[s]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)

    # Function to perform DFS and BFS on a disconnected graph
    def traverse(self):
        visited = set()
        for vertex in self.graph.keys():
            if vertex not in visited:
                print("Starting traversal from vertex:", vertex)
                self.dfs_util(vertex, visited)
                print()
                self.bfs(vertex)
                print()
        
# Main program
g = Graph()
vertices = int(input("Enter the number of vertices: "))
edges = int(input("Enter the number of edges: "))

for i in range(edges):
    u, v = map(int, input(f"Enter edge {i+1} (u v): ").split())
    g.add_edge(u, v)

print("Traversal:")
g.traverse()

def is_safe(v, color, graph, colors, n):
    for i in range(n):
        if graph[v][i] and colors[i] == color:
            return False
    return True

def graph_coloring_backtracking(graph, m, colors, v, n):
    if v == n:
        return True

    for color in range(1, m+1):
        if is_safe(v, color, graph, colors, n):
            colors[v] = color
            if graph_coloring_backtracking(graph, m, colors, v+1, n):
                return True
            colors[v] = 0

    return False

n = int(input("Enter the number of vertices: "))
m = int(input("Enter the number of colors: "))
graph = [[0] * n for _ in range(n)]

e = int(input("Enter the number of edges: "))
print("Enter the edges:")
for _ in range(e):
    u, v = map(int, input().split())
    graph[u-1][v-1] = 1
    graph[v-1][u-1] = 1

colors = [0] * n

if graph_coloring_backtracking(graph, m, colors, 0, n):
    print("Graph coloring possible with", m, "colors:")
    for i in range(n):
        print("Vertex", i+1, "colored with color", colors[i])
else:
    print("Graph coloring not possible with", m, "colors.")

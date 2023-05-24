Graph_nodes = {}

n = int(input("Enter the number of nodes: "))
for _ in range(n):
    node = input("Enter the node: ")
    edges = []
    m = int(input("Enter the number of edges for {}: ".format(node)))
    for _ in range(m):
        neighbor, weight = input("Enter neighbor and weight (neighbor weight): ").split()
        edges.append((neighbor, int(weight)))
    Graph_nodes[node] = edges

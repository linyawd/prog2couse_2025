def init(vertices, edges):
    global V, edge_list
    V = vertices
    edge_list = []

def addEdge(source, destination, weight):
    edge_list.append((source, destination, weight))

def findDistance(start, end):
    dist = [float('inf')] * V
    dist[start] = 0

    for _ in range(V - 1):
        for u, v, w in edge_list:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    for u, v, w in edge_list:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            return -1  # негативний цикл

    return dist[end] if dist[end] != float('inf') else -1

from PriorityQueue import PriorityQueue

def init(vertices, edges):
    global graph, n
    n = vertices
    graph = [[] for _ in range(vertices)]

def addEdge(source, destination, weight):
    graph[source].append((destination, weight))

def getWay(start, end):
    dist = [float('inf')] * n
    prev = [-1] * n
    dist[start] = 0
    pq = PriorityQueue()
    pq.insert(start, 0)

    while not pq.empty():
        u = pq.extractMinimum()
        for v, w in graph[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                prev[v] = u
                if v in pq:
                    pq.updatePriority(v, dist[v])
                else:
                    pq.insert(v, dist[v])

    if dist[end] == float('inf'):
        return []

    path = []
    cur = end
    while cur != -1:
        path.append(cur)
        cur = prev[cur]
    path.reverse()
    return path

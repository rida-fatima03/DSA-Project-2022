from math import inf
def dijkstras(graph, root):
    n = len(graph)
    dist = [inf for _ in range(n)]
    dist[root] = 0
    visited = [False for _ in range(n)]
    for _ in range(n):
        u = -1
        for i in range(n):
            if not visited[i] and (u == -1 or dist[i] < dist[u]):
                u = i
        if dist[u] == inf:
            break
        visited[u] = True
        for v, l in graph[u]:
            if dist[u] + l < dist[v]:
                dist[v] = dist[u] + l
    return dist

def BinarySearch(x, y, l):
    start, end = 0, len(l) - 1
    while end >= start:
        mid = (start+end) // 2
        c= y[l[mid]]
        if c == y[x]:
            return mid
        elif c > y[x]:
            end = mid - 1  
        else:
            start = mid + 1
    return end+1

def Dijkstra(graph,start,stop):
    path = {}
    adjacentnode = {}
    queue = [start]
    for n in graph:
        path[n] = float("inf")
        adjacentnode[n] = []    
    path[start] = 0
    while queue:
        s = queue.pop(0)
        for i,j in graph[s]:
            alter = j + path[s]
            if path[i] > alter:
                path[i] = alter
                adjacentnode[i] = [s]
                queue.insert(BinarySearch(i, path, queue),i)
            elif alter == path[i]:
                if s not in adjacentnode[i]:
                    adjacentnode[i].append(s)
    if path[stop]==float('inf'):
        return False
    else:
        return (path,adjacentnode)
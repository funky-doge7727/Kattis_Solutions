from heapq import heappush, heappop

def dijkstra(s, dest):
    pq = [(0,s)]
    dist[s] = 0
    while pq:
        d, u = heappop(pq)
        if d > dist[u]: continue
        for w, v in AL[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heappush(pq, (dist[v], v))
    print(dist[dest]) if dist[dest] != float("inf") else print("Impossible")

while True:
    n, m, q, s = list(map(int,input().split()))
    if m + n + q + s == 0: break
    AL = [[] for _ in range(n)] 
    dist = [float("inf")] * (n) 

    for _ in range(m):
        x = list(map(int,input().split()))
        AL[x[0]].append((x[2], x[1]))

    for _ in range(q):
        dijkstra(s, int(input()))
    
    print()

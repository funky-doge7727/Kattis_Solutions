from collections import deque
from heapq import heappush, heappop

x, y, z = map(int,input().split())

AM = [list(map(int,input().split())) for _ in range(x)]

# AL = [[] for _ in range(x)]

# # AM conversion to AL
# for i in range(len(AM)):
#     for j in range(len(AM[0])):
#         if i == j: continue
#         AL[i].append((j, AM[i][j]))

# def dijkstra(s, dest): # For AL
#     dist = [float("inf")] * len(AM)
#     dist[s] = 0
#     pq = [(0,s)]
#     while pq:
#         d, u = heappop(pq)
#         if d > dist[u]: continue
#         for v, w in AL[u]:
#             if dist[v] <= dist[u] + w: continue
#             dist[v] = dist[u] + w
#             heappush(pq, (dist[v], v))
#     return dist[dest]

def dijkstra(s, dest): # For AM
    dist = [float("inf")] * len(AM)
    dist[s] = 0
    pq = [(0,s)]
    while pq:
        d, u = heappop(pq)
        if d > dist[u]: continue
        for i in range(len(AM[u])):
            v, w = i, AM[u][i]
            if w == 0 or dist[v] <= dist[u] + w: continue
            dist[v] = dist[u] + w
            heappush(pq, (dist[v], v))
    return dist[dest]

print(dijkstra(y, z))

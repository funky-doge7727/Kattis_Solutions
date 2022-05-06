import sys
from collections import defaultdict
sys.setrecursionlimit(10000000)

# problem: https://open.kattis.com/problems/builddeps

x = int(input())
AH = defaultdict(set)
topo_list = []
visited = set()

for _ in range(x):
    x = input().split()
    x[0] = x[0][:-1]
    for i in x[1:]:
        AH[i].add(x[0])

def dfs(u):
    visited.add(u)
    for v in AH[u]:
        if v not in visited: dfs(v)
    topo_list.append(u)

dfs(input())
print(*reversed(topo_list), sep="\n")

from collections import defaultdict

x, y = list(map(int,input().split()))

EL = [list(map(int,input().split())) for _ in range(y)]


# initialisation
AL = defaultdict(list)
visited = set()
KIV = set()
sum_of_soldiers = 0

for i in range(len(EL)):
    AL[EL[i][0]].append(EL[i][1])
    AL[EL[i][1]].append(EL[i][0])

for i in range(1,x+1):
    AL[i] = [int(input()),AL[i].copy()]

def dfs(src):
    global sum_of_soldiers
    if src != 1 and AL[src][0] >= sum_of_soldiers:
        return
    sum_of_soldiers += AL[src][0]
    stack = [src]
    visited.add(src)
    while stack:
        curr_node = stack.pop()
        for neighbour in AL[curr_node][1]:
            if neighbour not in visited:
                if sum_of_soldiers > AL[neighbour][0]:
                    if neighbour in KIV: KIV.remove(neighbour)
                    stack.append(neighbour)
                    visited.add(neighbour)
                    sum_of_soldiers += AL[neighbour][0]
                else:
                    KIV.add(neighbour)
            

dfs(1)
prev_KIV = len(KIV)

while KIV:
    for i in KIV:
        dfs(i)
    if prev_KIV == len(KIV): break
    prev_KIV == len(KIV)

print(sum_of_soldiers)

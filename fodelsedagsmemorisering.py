from collections import defaultdict
dictt = defaultdict(tuple)

for _ in range(int(input())):
    n, l, d = input().split()
    if d not in dictt or dictt.get(d)[1] < int(l): 
        dictt[d] = (n, int(l))

print(len(dictt))
[print(i) for i, _ in sorted(dictt.values())]

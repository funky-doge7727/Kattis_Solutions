input()
x = input()

stack = []
dictt = {'}': '{', ']': '[', ')': '('}
oksofar = True

for i, j in enumerate(x):
    if j == ' ': continue
    if j in dictt:
        if stack and dictt.get(j) == stack.pop(): 
            continue
        oksofar = False
        print(f"{j} {i}")
        break
    else:
        stack.append(j)

if oksofar: print('ok so far')

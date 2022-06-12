from string import ascii_lowercase
from statistics import median

def f1():
    print(7)

def f2():
    print("Bigger") if z[0] > z[1] else print("Equal") if z[0] == z[1] else print("Smaller")

def f3():
    print(median(z[:3]))

def f4():
    print(sum(z))

def f5():
    print(sum(filter(lambda x: not x % 2, z)))

def f6():
    print(''.join(list(map(lambda x: ascii_lowercase[x%26], z))))

def f7():
    lstt = [False] * len(z)
    p = 0
    while True:
        if lstt[p]:
            print("Cyclic")
            return 
        lstt[p] = True
        p = z[p]
        if p == len(z) - 1:
            print("Done")
            return
        if p > len(z) - 1:
            print("Out")
            return
        
x = [f1, f2, f3, f4, f5, f6, f7]

y = int(input().split()[1])
z = list(map(int,input().split()))

x[y-1]()

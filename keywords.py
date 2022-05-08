#problem: https://open.kattis.com/problems/keywords

print(len({input().lower().replace('-',' ') for _ in range(int(input()))}))

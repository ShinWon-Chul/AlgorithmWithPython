import sys
from sys import stdin

sys.setrecursionlimit(10**7)
n = int(input())
a = list(map(int, stdin.readline().rstrip().split()))
ops = list(map(int, input().split()))
idx = 1
result = a[0]
results = []
def dfs(idx, op, result):
    if idx == len(a):
        results.append(result)
        return    
    for i in range(4):
        if i == 0 and op[i] != 0:
            op[i] -= 1
            dfs(idx+1, op, result+a[idx])
            op[i] += 1
        if i == 1 and op[i] != 0:
            op[i] -= 1
            dfs(idx+1, op, result-a[idx])
            op[i] += 1
        if i == 2 and op[i] != 0:
            op[i] -= 1
            dfs(idx+1, op, result*a[idx])
            op[i] += 1
        if i == 3 and op[i] != 0:
            op[i] -= 1
            dfs(idx+1, op, int(result/a[idx]))
            op[i] += 1
            
dfs(idx, ops, result)
print(max(results))
print(min(results))
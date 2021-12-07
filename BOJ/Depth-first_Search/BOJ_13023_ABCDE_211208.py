from sys import stdin
import sys
sys.setrecursionlimit(10**6)

N, M = list(map(int, stdin.readline().split()))
graph = [[]for _ in range(N) ]

for _ in range(M):
    x, y = list(map(int, stdin.readline().split()))
    graph[x].append(y)
    graph[y].append(x)
    
visited = [False] * N

def dfs(x, count):
    global result
    if count == 4:
        result=count
    for n in graph[x]:
        if not visited[n] :
            visited[n] = True
            dfs(n, count+1)
            visited[n] = False

result = 0
for i in range(N):
    count = 0
    visited[i] = True
    dfs(i, count)
    visited[i] = False
    if result:
        print(1)
        break
        
if not result:
    print(0)
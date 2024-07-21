import sys
sys.setrecursionlimit(10**9)

n = int(input())  # 노드 수 입력
graph = [[] for _ in range(n+1)]  # 인접 리스트 초기화
result = [[] for _ in range(n+1)]

# 간선 입력
for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n+1)

def dfs(parent):
    visited[parent] = True
    for child in graph[parent]:
        if not visited[child]:
            result[child].append(parent)
            dfs(child)

dfs(1)

for i in range(2, len(result)):
    print(result[i][0])
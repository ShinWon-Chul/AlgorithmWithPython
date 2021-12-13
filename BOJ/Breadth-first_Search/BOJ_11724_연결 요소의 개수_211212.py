from collections import deque

n, m = list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e = list(map(int, input().split()))
    graph[s].append(e)
    graph[e].append(s)
    
visited = [False]*(n+1)

def bfs(start):
    q = deque([start])
    while q:
        n = q.popleft()
        for node in graph[n]:
            if not visited[node]:
                visited[node] = True
                q.append(node)

count = 0
for i in range(1, n+1):
    if not visited[i]:
        visited[i] = True
        bfs(i)
        count += 1
if m == 0:
    print(0)
else:
    print(count)
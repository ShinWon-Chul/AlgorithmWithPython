from collections import deque
n,m,k,x = list(map(int, input().split()))
graph = [[] for _ in range(n+1) ]
for _ in range(m):
    s, e = list(map(int, input().split()))
    graph[s].append(e)
visited = [0]* (n+1)

def bfs(start):
    q = deque([start])
    while q:
        n = q.popleft()
        for node in graph[n]:
            if visited[node] == 0:
                visited[node] = visited[n]+1
                q.append(node)
                
bfs(x)
result = []
for i, v in enumerate(visited):
    if v == k:
        result.append(i)
        
if len(result) == 0:
    print(-1)
else:
    for i in result:
        print(i)
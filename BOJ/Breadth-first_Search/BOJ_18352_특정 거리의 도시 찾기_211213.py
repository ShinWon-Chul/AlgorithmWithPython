from collections import deque
n,m,k,x = list(map(int, input().split()))
graph = [[] for _ in range(n+1) ]
for _ in range(m):
    s, e = list(map(int, input().split()))
    graph[s].append(e)

visited = [False]*(n+1)
distance = [0]* (n+1)

result = []
def bfs(start):
    q = deque([start])
    visited[start] = True
    while q:
        n = q.popleft()
        for node in graph[n]:
            if not visited[node]:
                visited[node] = True
                distance[node] = distance[n]+1
                q.append(node)
                if distance[node] == k:
                    result.append(node)
bfs(x)
result.sort()        
if len(result) == 0:
    print(-1)
else:
    for i in result:
        print(i)
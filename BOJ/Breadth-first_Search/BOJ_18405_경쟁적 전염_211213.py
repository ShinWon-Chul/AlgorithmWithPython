from collections import deque

n,k = map(int, input().split())
graph = []
data = []

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            data.append((graph[i][j], 0, i, j))
data.sort()
data
q = deque(data)

target_s, x, y = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

count = 0
while q:
    virus, s, cx, cy = q.popleft()
    if s == target_s:
        break
    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]
        if 0 <= nx < n and 0 <= ny < n :
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append([virus, s+1, nx, ny])
    
print(graph[x-1][y-1])
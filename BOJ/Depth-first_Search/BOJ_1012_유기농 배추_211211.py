from collections import deque
t = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i,j):
    q = deque([[i,j]])
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0<= nx <n and 0<= ny <m:
                if visited[nx][ny] == False and graph[nx][ny] != 0:
                    visited[nx][ny] = True
                    q.append([nx, ny])
for _ in range(t):                   
    count = 0
    m, n, k = list(map(int, input().split()))
    g = []
    for _ in range(k):
        g.append(list(map(int, input().split())))

    graph = [[0]*m for _ in range(n)]
    visited = [[False]*m for _ in range(n)]
    for x, y in g:
        graph[y][x] = 1

    for i in range(n):
        for j in range(m):
            if visited[i][j] == False and graph[i][j] != 0:
                visited[i][j] = True
                bfs(i, j)
                count += 1
    print(count)
from collections import deque
m,n = map(int, input().split())
inf = int(10e9)
graph = []
for _ in range(n):
    graph.append(input())
visited = [[inf]*m for _ in range(n)]
visited[0][0] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque([[x, y]])
    while q:
        cx,cy = q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == '1' and visited[nx][ny]>visited[cx][cy]+1:
                    visited[nx][ny] = min(visited[nx][ny], (visited[cx][cy]+1))
                    q.append([nx, ny])
                elif graph[nx][ny] == '0' and visited[nx][ny]>visited[cx][cy]:
                    visited[nx][ny] = min(visited[nx][ny], visited[cx][cy])
                    q.append([nx, ny])
bfs(0, 0)
print(visited[n-1][m-1])
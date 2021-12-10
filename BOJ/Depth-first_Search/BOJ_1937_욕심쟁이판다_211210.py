from sys import stdin
n = int(input())
forest = []
for _ in range(n):
    forest.append(list(map(int, stdin.readline().split())))

visited = [[0] * n for _ in range(n)] 
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def dfs(x, y):
    if visited[x][y]:
        return visited[x][y]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx < n and 0<= ny < n:
            if forest[nx][ny] > forest[x][y]:
                visited[x][y] = max(visited[x][y], dfs(nx, ny))
    visited[x][y] += 1
    return visited[x][y]
    
result = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            result = max(result, dfs(i, j))
print(result)
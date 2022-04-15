from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(maps, n, m):
    q = deque([[0, 0, 1]])
    while q:
        x, y, cost = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] != 0:
                    new_cost = cost + 1
                    if maps[nx][ny] > new_cost:
                        maps[nx][ny] = new_cost
                        q.append([nx, ny, new_cost])
def solution(maps):
    inf = int(1e9)
    n = len(maps)
    m = len(maps[0])
    for x in range(n):
        for y in range(m):
            if maps[x][y] == 1:
                maps[x][y] = inf
    maps[0][0] = 0
    bfs(maps, n, m)
    answer = maps[-1][-1]
    if answer != inf:
        return answer
    else:
        return -1

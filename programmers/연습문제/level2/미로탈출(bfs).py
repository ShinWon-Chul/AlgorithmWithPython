from collections import deque
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(maps, q, n, m):
    visited = [[ 1e9 for _ in range(n)] for _ in range(m)]
    # print(q[0])
    visited[q[0][1]][q[0][0]] = 0
    while q:
        x, y, cost = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if maps[ny][nx] != 'X':
                    if visited[ny][nx] > cost + 1:
                        visited[ny][nx] = cost + 1
                        q.append([nx, ny, cost+1])
    return visited
                        
        
def solution(maps):
    answer = 0

    n = len(maps[0])
    m = len(maps)
    for y, row in enumerate(maps):
        for x, col in enumerate(row):
            if col == 'S':
                sx, sy = x, y
            elif col == 'E':
                ex, ey = x, y
            elif col == 'L':
                lx, ly = x, y
    q = deque([[sx, sy, 0]])
    visited = bfs(maps, q, n, m)
    answer += visited[ly][lx]
    q = deque([[lx, ly, 0]])
    visited = bfs(maps, q, n, m)
    answer += visited[ey][ex]
    
    if answer >= 1e9:
        return -1
    else:
        return answer
from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(maps, visited, q, n, m):
    score = 0
    loc = [[q[0][0], q[0][1]]]
    visited[q[0][1]][q[0][0]] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if maps[ny][nx] != 'X' and visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    q.append([nx, ny])
                    loc.append([nx, ny])
    for x, y in loc:
        score += int(maps[y][x])
    return score
    
def solution(maps):
    answer = []
    n = len(maps[0])
    m = len(maps)
    visited = [ [0 for _ in range(n)] for _ in range(m)]
    
    for y, row in enumerate(maps):
        for x, col in enumerate(row):
            if col != 'X' and visited[y][x] == 0:
                q = deque([[x, y]])
                answer.append(dfs(maps, visited, q, n, m))
                
    answer.sort()
    if len(answer) == 0:
        return [-1]
    else:
        return answer
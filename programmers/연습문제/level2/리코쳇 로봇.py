from collections import deque

#좌우상하
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(q, n, m, visited, board):
    while q:
        x, y, cost = q.popleft()
        for i in range(4):
            nx = x
            ny = y
            while 0 <= nx + dx[i] < m and 0 <= ny + dy[i] < n:
                nx = nx + dx[i]
                ny = ny + dy[i]
                if board[ny][nx] == 'D':
                    nx -= dx[i]
                    ny -= dy[i]
                    break
            if visited[ny][nx] > cost + 1:
                visited[ny][nx] = cost + 1
                q.append([nx, ny, cost + 1])

def solution(board):
    answer = 0
    inf = int(1e9)
    n = len(board)
    m = len(board[0])
    visited = [ [inf for _ in range(m)] for _ in range(n)]
    for y, row in enumerate(board):
        for x, col in enumerate(row):
            if col == 'R' :
                start = [x, y, 0]
            elif col == 'G':
                end = [x, y]
    q = deque([start])
    bfs(q, n, m, visited, board)
    answer = visited[end[1]][end[0]]
    if answer == inf:
        answer = -1
    return answer
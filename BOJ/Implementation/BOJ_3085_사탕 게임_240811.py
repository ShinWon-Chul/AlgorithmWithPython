import copy
from collections import deque
N = int(input())
graph = [ list(input()) for _ in range(N)]

rl_dx = [1, -1]
rl_dy = [0, 0]
ud_dx = [0, 0]
ud_dy = [1, -1]

def bfs(graph, x, y, color, dx, dy):

    queue = deque()
    queue.append((x, y))
    visited = [[False] * N for _ in range(N)]
    visited[y][x] = True
    
    count = 1
    while queue:
        x, y = queue.popleft()
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[ny][nx]:
                if graph[ny][nx] == color:
                    count += 1
                    queue.append((nx, ny))

                    visited[ny][nx] = True
    return count

res = 0
for y in range(N):
    for x in range(N):
        # 좌우 변경
        if x+1 < N:
            n_graph = copy.deepcopy(graph)
            n_graph[y][x+1], n_graph[y][x] = graph[y][x], graph[y][x+1]
            count = bfs(n_graph, x, y, n_graph[y][x], rl_dx, rl_dy)
            res = max(res, count)
            count = bfs(n_graph, x, y, n_graph[y][x], ud_dx, ud_dy)
            res = max(res, count)
            count = bfs(n_graph, x+1, y, n_graph[y][x+1], rl_dx, rl_dy)
            res = max(res, count)
            count = bfs(n_graph, x+1, y, n_graph[y][x+1], ud_dx, ud_dy)
            res = max(res, count)
        # 위아래 변경
        if y+1 < N:
            n_graph = copy.deepcopy(graph)
            n_graph[y+1][x], n_graph[y][x] = graph[y][x], graph[y+1][x]
            count = bfs(n_graph, x, y, n_graph[y][x], rl_dx, rl_dy)
            res = max(res, count)
            count = bfs(n_graph, x, y, n_graph[y][x], ud_dx, ud_dy)
            res = max(res, count)
            count = bfs(n_graph, x, y+1, n_graph[y+1][x], rl_dx, rl_dy)
            res = max(res, count)
            count = bfs(n_graph, x, y+1, n_graph[y+1][x], ud_dx, ud_dy)
            res = max(res, count)
print(res) 

#N^2*8*N = 8*N^3 = N^3
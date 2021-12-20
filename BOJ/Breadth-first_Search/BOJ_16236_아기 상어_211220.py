from collections import deque

#상어의 현재 위치와 이동 거리 초기화
def init_s():
    for x, row in enumerate(graph):
        for y, col in enumerate(row):
            if graph[x][y] == 9:
                q = deque([[0, x, y]])
    return [q[0][1], q[0][2]], q

def bfs(q):
    eat = []
    while q:
        cost, x, y = q.popleft()
        visited[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and graph[nx][ny] <= size:
                    visited[nx][ny] = True
                    q.append([cost+1, nx, ny])
                    if 0< graph[nx][ny] < size:
                        eat.append([cost+1, nx, ny])
    eat.sort(key = lambda x : (x[0], x[1], x[2]))
    return eat

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

cloc, q = init_s()
size = 2
total_cost = 0
count = 0
while True:
    visited = [[False]*n for _ in range(n)]
    eat = bfs(q)
    if len(eat) > 0:
        count += 1
        total_cost += eat[0][0]
        graph[cloc[0]][cloc[1]] = 0
        graph[eat[0][1]][eat[0][2]] = 9
        cloc, q = init_s()
        if count == size:
            count = 0
            size += 1
    else:
        break
print(total_cost)
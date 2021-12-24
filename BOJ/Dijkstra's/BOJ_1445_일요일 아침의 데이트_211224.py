from heapq import heappush, heappop
from sys import stdin
n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(stdin.readline().rstrip()))
inf = int(10e9)
cost = [[inf] * m for _ in range(n)]
i_cost = [[inf] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

#시작 지점 초기화
for x in range(n):
    for y in range(m):
        if graph[x][y] == 'S':
            sx, sy  = x, y
        elif graph[x][y] == 'F':
            fx, fy  = x, y
        elif graph[x][y] == 'g':
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != 'g' and graph[nx][ny] != 'S' and graph[nx][ny] != 'F':
                    graph[nx][ny] = 'i'

cost[sx][sy] = 0
i_cost[sx][sy] = 0
def dijkstra():
    h = []
    heappush(h, (0,0, sx,sy))
    while h:
        dist,i_dist, x, y = heappop(h)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 'g':
                    next_cost = dist + 1
                    if next_cost < cost[nx][ny]:
                        cost[nx][ny] = next_cost
                        i_cost[nx][ny] = i_dist
                        heappush(h, (next_cost,i_dist, nx, ny))
                elif graph[nx][ny] == 'i':
                    next_i_cost = i_dist + 1
                    if next_i_cost < i_cost[nx][ny]:
                        cost[nx][ny] = dist
                        i_cost[nx][ny] = next_i_cost
                        heappush(h, (dist,next_i_cost, nx, ny))
                else:
                    if dist < cost[nx][ny] and i_dist < i_cost[nx][ny]:
                        cost[nx][ny] = dist
                        i_cost[nx][ny] = i_dist
                        heappush(h, (dist,i_dist,nx, ny))
dijkstra()
print(cost[fx][fy], i_cost[fx][fy])

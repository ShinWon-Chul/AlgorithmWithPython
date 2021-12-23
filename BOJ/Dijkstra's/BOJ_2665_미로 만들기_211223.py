from heapq import heappop, heappush
from sys import stdin
n = int(input())

graph = []
for _ in range(n):
    graph.append(list(stdin.readline().rstrip()))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

inf = int(10e9)
cost = [[inf] * n for _ in range(n)]

def dijkstra():
    h = []
    heappush(h, (0,0,0))
    while h:
        current_cost, x, y = heappop(h)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == '1':
                    if current_cost < cost[nx][ny]:
                        cost[nx][ny] = current_cost
                        heappush(h, (current_cost,nx, ny))
                else:
                    next_cost = current_cost + 1
                    if next_cost < cost[nx][ny]:
                        cost[nx][ny] = next_cost
                        heappush(h, (next_cost,nx, ny))
dijkstra()
print(cost[n-1][n-1])
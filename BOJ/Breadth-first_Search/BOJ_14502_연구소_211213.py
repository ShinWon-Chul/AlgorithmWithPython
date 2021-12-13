import itertools
import copy
from collections import deque
n, m = list(map(int, input().split()))
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

#상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
virus = deque()
e = []
for x, row in enumerate(grid):
    for y, col in enumerate(row):
        if col == 2:
            virus.append([x, y])
        elif col == 0:
            e.append([x, y])
walls = list(itertools.combinations(e, 3))
def bfs(q, newGrid):
    count = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if newGrid[nx][ny] == 0:
                    newGrid[nx][ny] = 2
                    q.append([nx, ny])
    for x, row in enumerate(newGrid):
        for y, col in enumerate(row): 
            if newGrid[x][y] == 0:
                count +=1
    return count

result = 0
for wi, wall in enumerate(walls):
    newGrid = copy.deepcopy(grid)
    for x, y in wall:
        newGrid[x][y] = 1
    result = max(result, bfs(virus.copy(), newGrid))
print(result)
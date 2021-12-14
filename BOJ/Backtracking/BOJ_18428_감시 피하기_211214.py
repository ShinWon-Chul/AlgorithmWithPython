from itertools import combinations 
import copy

n = int(input())
graph = []
for _ in range(n):
    row = list(input().split())
    graph.append(row)

e = []
teachers = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for xi, row in enumerate(graph):
    for yi, col in enumerate(row):
        if col == 'X':
            e.append((xi, yi))
        elif col == 'T':
            teachers.append((xi, yi))
walls = list(combinations(e, 3))

def dfs():
    for teacher in teachers:
        for i in range(4):
            x, y = teacher
            while 0<= x <n and 0<= y <n:
                x = x + dx[i]
                y = y + dy[i]
                if 0<= x < n and 0<= y <n:
                    if newGraph[x][y] == 'O':
                        break
                    elif newGraph[x][y] == 'S':
                        return 1
                
    return 0

result = []
for wall in walls:
    newGraph = copy.deepcopy(graph)
    for x,y in wall:
        newGraph[x][y] = 'O'
    result.append(dfs())
if 0 in result:
    print("YES")
else:
    print("NO")
from collections import deque
n, l, r = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
# graph = [[10, 100, 20, 90],
#          [80, 100, 60, 70],
#          [70, 20, 30, 40],
#          [50, 20, 100, 10]]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, visited):
    _count = 1
    pop = [graph[x][y]]
    cities = [[x, y]]
    q = deque([[x, y]])
    visited[x][y] = True
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < n and 0 <= ny < n :
                if visited[nx][ny] == False and l <= abs(graph[cx][cy]-graph[nx][ny]) <= r:
                    visited[nx][ny] = True
                    pop.append(graph[nx][ny])
                    cities.append([nx,ny])
                    _count += 1
                    q.append([nx, ny])
    if _count != 1:
        newPop = int(sum(pop)/_count)
        for ix, iy in cities:
            graph[ix][iy] = newPop
        return True
    return False

# 프로세스 함수 구현중

def process():
    count = 0
    while True:
        visited = [[False]*n for _ in range(n)]
        find = False
        for x, row in enumerate(graph):
            for y, col in enumerate(graph):
                if visited[x][y] == False:
                    if bfs(x, y, visited):
                        find = True
        if not find:
            break
        else : 
            count += 1
    return count
print(process())
                        
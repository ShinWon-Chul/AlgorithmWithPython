import copy
#물고기 이동 (물고기는 16까지 있다고 가정)
def move_fish(graph, direction):
    for i in range(1, 17):
        moved = False
        for x, row in enumerate(graph):
            for y, col in enumerate(row):
                #작은 번호 부터 이동 시작
                if graph[x][y] == i:
                    #현재 이동 방향
                    d = direction[x][y]
                    #이동 할 수 있는지 확인
                    for j in range(d, d + 8):
                        nx = x + dx[j]
                        ny = y + dy[j]
                        if j == 8:
                            direction[x][y] = j
                        else:
                            direction[x][y] = j%8
                        #이동 할 수 있다면 이동
                        if 0<= nx < 4 and 0<= ny < 4:
                            if graph[nx][ny] != 's':
                                    graph[x][y], graph[nx][ny] = graph[nx][ny], graph[x][y]
                                    direction[x][y], direction[nx][ny] = direction[nx][ny], direction[x][y]
                                    moved = True
                                    break
                if moved:
                    break
            if moved:
                break

def dfs(x, y, graph, direction, result):
    global total_result
    move_fish(graph, direction)
    d = direction[x][y] #상어가 있는 위치의 방향
    nx = x + dx[d] 
    ny = y + dy[d]
    exsist = False
    while 0<= nx < 4 and 0<= ny < 4:
        if graph[nx][ny] != 0:
            exsist = True
            graph[x][y] = 0
            direction[x][y] = 0
            prev = graph[nx][ny]
            graph[nx][ny] = 's'
            dfs(nx, ny, copy.deepcopy(graph), copy.deepcopy(direction), result + prev)
            graph[x][y] = 's'
            direction[x][y] = d
            graph[nx][ny] = prev
        nx = nx + dx[d] 
        ny = ny + dy[d]
    total_result = max(total_result, result)
    if not exsist:
        return

inputs = []
for _ in range(4):
    inputs.append(list(map(int, input().split())))
#초기 상태
graph = []
direction = []
for x, row in enumerate(inputs):
    d = []
    g = []
    for y, col in enumerate(row):
        if y % 2 == 0:
            g.append(inputs[x][y])
        elif y != 0 and y %2 != 0:
            d.append(inputs[x][y])
    graph.append(g)
    direction.append(d)
dx = [-1, -1, 0, 1, 1, 1, 0, -1] *2
dy = [0, -1, -1, -1, 0, 1, 1, 1] *2
dx = [0] + dx
dy = [0] + dy
#상어가 들어간 직후 상태
result = graph[0][0]
graph[0][0] = 's'
total_result = 0
dfs(0, 0, copy.deepcopy(graph), copy.deepcopy(direction), result)
print(total_result)
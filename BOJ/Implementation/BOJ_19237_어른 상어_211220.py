n, m, k = map(int, input().split()) #격자 크기, 상어, 냄새지속시간
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))
direction =  list(map(int, input().split()))#상 하 좌 우
priority = [[] for _ in range(m)]

for i in range(m):
    for j in range(4):
        priority[i].append(list(map(int, input().split())))

#상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

smell = [[[0, 0] for _ in range(n)] for _ in range(n)] #[상어, 냄새]

#냄새 갱신 함수
def update_smell(smell):
    for x, row in enumerate(smell):
        for y, col in enumerate(row):
            if col[1] > 0:
                col[1] -= 1
            if col[1] == 0:
                col[0] = 0
            if grid[x][y] != 0:
                smell[x][y] = [grid[x][y], k]
    return smell

#상어 이동 함수
def move_s(grid):
    moved = []
    for x in range(n):
        for y in range(n):
            #상어가 있다면
            if grid[x][y] != 0 and grid[x][y] not in moved:
                #이동 방향 결정
                d = priority[grid[x][y]-1][direction[grid[x][y]-1]-1]
                empty = False
                for i in range(4):
                    nx = x + dx[d[i]-1]
                    ny = y + dy[d[i]-1]
                    if 0 <= nx < n and 0 <= ny < n:
                        #냄새가 아직 없는 공간이 있다면
                        if smell[nx][ny][0] == 0:
                            #만약 다른 상어가 있다면
                            if grid[nx][ny] != 0:
                                #만약 다른 상어의 번호가 크다면 현재 상어가 다른 상어를 쫒아냄
                                if grid[nx][ny] > grid[x][y]:
                                    #direction 갱신
                                    direction[grid[x][y]-1] = d[i]
                                    moved.append(grid[x][y])
                                    grid[nx][ny] = 0
                                    grid[x][y], grid[nx][ny] = grid[nx][ny], grid[x][y]
                                    empty = True
                                    break
                                #만약 다른 상어의 번호가 작다면 현재 상어를 쫒아냄
                                else:
                                    grid[x][y] = 0
                                    empty = True
                                    break
                            #다른 상어가 없다면 그냥 단순 이동
                            else:
                                #direction 갱신
                                direction[grid[x][y]-1] = d[i]
                                moved.append(grid[x][y])
                                #위치 갱신
                                grid[x][y], grid[nx][ny] = grid[nx][ny], grid[x][y]
                                empty = True
                                break
                if empty :
                    continue
                #만약 빈공간이 없다면
                else:
                    for i in range(4):
                        nx = x + dx[d[i]-1]
                        ny = y + dy[d[i]-1]
                        if 0 <= nx < n and 0 <= ny < n:
                            #만약 내 냄새가 있는공간 이라면
                            if smell[nx][ny][0] == grid[x][y]:
                                #direction 갱신
                                direction[grid[x][y]-1] = d[i]
                                moved.append(grid[x][y])
                                grid[x][y], grid[nx][ny] = grid[nx][ny], grid[x][y]
                                break
    return grid

smell = update_smell(smell)
count = 0
while True:
    grid = move_s(grid)
    smell = update_smell(smell)
    count += 1
    one_left = True
    for x, row in enumerate(grid):
        for y, col in enumerate(row):
            if grid[x][y] > 1:
                one_left = False
    if one_left:
        print(count)
        break
    elif count == 1000:
        print(-1)
        break
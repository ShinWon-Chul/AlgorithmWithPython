import sys
sys.setrecursionlimit(10**7)
# turn을 저장할 배열
turn_arr = []
# 상하좌우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(maze, turn, r_loc, b_loc, r_arrive, b_arrive, width, high, rvisited, bvisited):
    global tunr_arr
    # 두 수레가 모두 도착한 경우
    if r_loc == r_arrive and b_loc == b_arrive:
        turn_arr.append(turn)
        return
    
    #현재 위치
    rx, ry = r_loc
    bx, by = b_loc
    for i in range(4):
        # 빨강 먼저 업데이트 
        nrx = rx + dx[i]
        nry = ry + dy[i]
        # 빨강은 파랑의 현재 위치, 벽, 이전에 지나온 길을 갈 수 없음
        if nrx != bx or nry != by and maze[nry][nrx] != 5 and rvisited[nry][nrx] != True: 
            nbx = bx + dx[i]
            nby = by + dy[i]
            # 파랑은 업데이트 된 빨강 위치, 벽, 이전에 지나온 길을 갈 수 없음
            if nbx != nrx or nry != nby and maze[nby][nbx] != 5 and bvisited[nry][nrx] != True:
                # 범위를 벗어나는지 판단
                if (0 <= nrx < width and 0 <= nry < high) and (0 <= nbx < width and 0 <= nby < high):
                    # 위 조건을 모두 만족했다면 만족했다면 
                    # r_loc, b_loc, r_arrive, b_arrive업데이트
                    nr_loc = [nrx, nry]
                    nb_loc = [nbx, nby]
                    rvisited[ry][rx] = True
                    bvisited[ry][rx] = True
                    dfs(maze, turn + 1, nr_loc, nb_loc, r_arrive, b_arrive, width, high, rvisited, bvisited)
        
        # backtracking
        rvisited[ry][rx] = False
        bvisited[ry][rx] = False

        ## 동일한 로직으로 파랑 업데이트
        # 파랑 먼저 업데이트 
        nbx = bx + dx[i]
        nby = by + dy[i]
        # 파랑은 빨강의 현재 위치, 벽, 이전에 지나온 길을 갈 수 없음
        if nbx != rx or nby != ry and maze[nby][nbx] != 5 and bvisited[nby][nbx] != True: 
            nrx = rx + dx[i]
            nry = ry + dy[i]
            # 빨강은 업데이트 된 파랑 위치, 벽, 이전에 지나온 길을 갈 수 없음
            if nrx != nbx or nry != nby and maze[nry][nrx] != 5 and rvisited[nry][nrx] != True:
                # 범위를 벗어나는지 판단
                if (0 <= nrx < width and 0 <= nry < high) and (0 <= nbx < width and 0 <= nby < high):
                    # 위 조건을 모두 만족했다면 만족했다면 
                    # r_loc, b_loc, r_arrive, b_arrive업데이트
                    nr_loc = [nrx, nry]
                    nb_loc = [nbx, nby]
                    rvisited[ry][rx] = True
                    bvisited[ry][rx] = True
                    dfs(maze, turn + 1, nr_loc, nb_loc, r_arrive, b_arrive, width, high, rvisited, bvisited)
        
        # 더이상 진행할 수 없는 경우
            # 배열에 0을 추가하고
            turn_arr.append(0)
            # dfs 생략
            continue
            
def solution(maze):
    answer = 0
    init_turn = 0
    high = len(maze)
    width = len(maze[0])
    rvisited = [[False for _ in range(width)] for _ in range(high)]
    bvisited = [[False for _ in range(width)] for _ in range(high)]
    for y in range(high):
        for x in range(width):
            if maze[y][x] == 1:
                # x, y좌표
                r_loc = [x, y]
            elif maze[y][x] == 2:
                b_loc = [x, y]
            elif maze[y][x] == 3:
                r_arrive = [x, y]
            elif maze[y][x] == 4:
                b_arrive = [x, y]
    dfs(maze, 0, r_loc, b_loc, r_arrive, b_arrive, width, high, rvisited, bvisited)
    return min(turn_arr)
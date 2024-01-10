# backtracking, dfs
import sys
import copy
sys.setrecursionlimit(10**7)
# turn을 저장할 배열
answer = int(1e9)
# 상하좌우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(maze, turn, r_loc, b_loc, r_arrive, b_arrive, width, height, rvisited, bvisited):
    global answer
    # 두 수레가 모두 도착한 경우
    if r_loc == r_arrive and b_loc == b_arrive:
        answer = min(answer, turn)
        return

    # 턴이 이미 도착한 최솟값을 넘어가면 더이상 탐색 할 필요가 없다.
    if turn >= answer:    
        return
    #현재 위치
    rx, ry = r_loc
    bx, by = b_loc


    for i in range(4):
        # 빨강이 도착해 있는 경우
        if rx == r_arrive[0] and ry == r_arrive[1]: 
            # 파랑만 업데이트
            nbx = bx + dx[i]
            nby = by + dy[i]
            # 범위를 벗어나는지 판단, 빨강 위치에 이동할 수 없음
            if (0 <= nbx < width and 0 <= nby < height) and (nbx != rx or ry != nby):
                # 벽, 이전에 지나온 길을 갈 수 없음
                if maze[nby][nbx] != 5 and bvisited[nby][nbx] != True:
                    # 위 조건을 모두 만족했다면 만족했다면 
                    # r_arrive, b_arrive업데이트
                    # nr_loc = [nrx, nry]
                    nb_loc = [nbx, nby]
                    # n_bvisited = copy.deepcopy(bvisited)
                    bvisited[nby][nbx] = True
                    dfs(maze, turn + 1, r_loc, nb_loc, r_arrive, b_arrive, width, height, rvisited, bvisited)
                    bvisited[nby][nbx] = False
        else:
            # 빨강 먼저 업데이트 
            nrx = rx + dx[i]
            nry = ry + dy[i]
            # 범위를 벗어나는지 판단, 파랑 위치에 이동할 수 없음
            if (0 <= nrx < width and 0 <= nry < height) and (nrx != bx or nry != by):
                # 벽, 이전에 지나온 길을 갈 수 없음
                if maze[nry][nrx] != 5 and rvisited[nry][nrx] != True:
                    for j in range(4):
                        nbx = bx + dx[j]
                        nby = by + dy[j]
                        # 범위를 벗어나는지 판단, 빨강 위치에 이동할 수 없음
                        if (0 <= nbx < width and 0 <= nby < height) and (nbx != nrx or nry != nby):
                            # 벽, 이전에 지나온 길을 갈 수 없음
                            if maze[nby][nbx] != 5 and bvisited[nby][nbx] != True:
                                # 위 조건을 모두 만족했다면 만족했다면 
                                # r_arrive, b_arrive업데이트
                                nr_loc = [nrx, nry]
                                nb_loc = [nbx, nby]
                                # n_rvisited = copy.deepcopy(rvisited)
                                # n_bvisited = copy.deepcopy(bvisited)
                                rvisited[nry][nrx] = True
                                bvisited[nby][nbx] = True
                                dfs(maze, turn + 1, nr_loc, nb_loc, r_arrive, b_arrive, width, height, rvisited, bvisited)
                                # backtracking
                                rvisited[nry][nrx] = False
                                bvisited[nby][nbx] = False
            


        ## 동일한 로직으로 파랑 업데이트
        # 파랑이 도착해 있는 경우
        if bx == b_arrive[0] and by == b_arrive[1]: 
            # 빨강만 업데이트
            nrx = rx + dx[i]
            nry = ry + dy[i]
            # 범위를 벗어나는지 판단, 빨강 위치에 이동할 수 없음
            if (0 <= nrx < width and 0 <= nry < height) and (nrx != bx or nry != by):
                # 벽, 이전에 지나온 길을 갈 수 없음
                if maze[nry][nrx] != 5 and rvisited[nry][nrx] != True:
                    # 위 조건을 모두 만족했다면 만족했다면 
                    # r_arrive, b_arrive업데이트
                    # nr_loc = [nrx, nry]
                    nr_loc = [nrx, nry]
                    # n_rvisited = copy.deepcopy(rvisited)
                    rvisited[nry][nrx] = True
                    dfs(maze, turn + 1, nr_loc, b_loc, r_arrive, b_arrive, width, height, rvisited, bvisited)
                    rvisited[nry][nrx] = False
        else:
            # 파랑 먼저 이동
            nbx = bx + dx[i]
            nby = by + dy[i]
            # 범위를 벗어나는지 판단, 빨강 위치에 이동할 수 없음
            if (0 <= nbx < width and 0 <= nby < height) and (nbx != rx or nby != ry):
                # 벽, 이전에 지나온 길을 갈 수 없음
                if maze[nby][nbx] != 5 and bvisited[nby][nbx] != True: 
                    for j in range(4):
                        nrx = rx + dx[j]
                        nry = ry + dy[j]
                        # 범위를 벗어나는지 판단, 파 위치에 이동할 수 없음
                        if (0 <= nrx < width and 0 <= nry < height) and (nrx != nbx or nry != nby):
                            # 벽, 이전에 지나온 길을 갈 수 없음
                            if  maze[nry][nrx] != 5 and rvisited[nry][nrx] != True:
                                # 위 조건을 모두 만족했다면 만족했다면 
                                # r_arrive, b_arrive업데이트
                                nr_loc = [nrx, nry]
                                nb_loc = [nbx, nby]
                                # n_rvisited = copy.deepcopy(rvisited)
                                # n_bvisited = copy.deepcopy(bvisited)
                                rvisited[nry][nrx] = True
                                bvisited[nby][nbx] = True
                                dfs(maze, turn + 1, nr_loc, nb_loc, r_arrive, b_arrive, width, height, rvisited, bvisited)
                                # backtracking
                                rvisited[nry][nrx] = False
                                bvisited[nby][nbx] = False
            
def solution(maze):
    init_turn = 0
    height = len(maze)
    width = len(maze[0])
    rvisited = [[False for _ in range(width)] for _ in range(height)]
    bvisited = [[False for _ in range(width)] for _ in range(height)]
    for y in range(height):
        for x in range(width):
            if maze[y][x] == 1:
                # x, y좌표
                r_loc = [x, y]
                rvisited[y][x] = True
            elif maze[y][x] == 2:
                b_loc = [x, y]
                bvisited[y][x] = True
            elif maze[y][x] == 3:
                r_arrive = [x, y]
            elif maze[y][x] == 4:
                b_arrive = [x, y]
                
    
    dfs(maze, 0, r_loc, b_loc, r_arrive, b_arrive, width, height, rvisited, bvisited)
    if answer == int(1e9):
        return 0
    else:
        return answer
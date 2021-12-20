from collections import deque

def solution(board):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    n = len(board)
    new_board = []
    new_board.append([1]*(len(board)+2))
    for i in board:
        new_board.append([1]+i+[1])
    new_board.append([1]*(len(board)+2))
    #print(new_board)
    q = deque([[(1,1),(1,2), 0]])
    visited = [[(1,1),(1,2)]]

    while q:
        pos1, pos2, cost = q.popleft()
        if pos1 == (n, n) or pos2 == (n, n):
            return cost
        for i in range(4):
            new_pos1 = (pos1[0]+dx[i],pos1[1]+dy[i])
            new_pos2 = (pos2[0]+dx[i],pos2[1]+dy[i])
            new_pos = [new_pos1, new_pos2, cost+1]
            #벽에 닿지 않는지 확인
            if 0<new_pos1[0]<=n and 0<new_pos1[1]<=n and 0<new_pos2[0]<=n and 0<new_pos2[1]<=n:
                #위치한 곳에 벽이 없는지 확인
                if new_board[new_pos1[0]][new_pos1[1]] != 1 and new_board[new_pos2[0]][new_pos2[1]] != 1:
                #몸체 둘중 하나라도 방문하지 않은 경우
                    if sorted(new_pos[:-1]) not in visited:
                        #방문 표시
                        visited.append(sorted(new_pos[:-1]))
                        #q에 추가
                        q.append(new_pos)
        #가로로 놓여 있는 경우의 회전
        if pos1[0] == pos2[0]:
            for i in (1, -1):
                if new_board[pos1[0]+i][pos1[1]] == 0 and new_board[pos2[0]+i][pos2[1]] == 0:
                    #왼쪽 으로 회전하는 경우
                    new_pos1 = (pos1[0], pos1[1])
                    new_pos2 = (pos1[0]+i, pos1[1])
                    new_pos = [new_pos1, new_pos2, cost+1]
                    if sorted(new_pos[:-1]) not in visited:
                        #방문 표시
                        visited.append(sorted(new_pos[:-1]))
                        #q에 추가
                        q.append(new_pos)
                    #오른쪽으로 회전하는경우
                    new_pos1 = (pos2[0], pos2[1])
                    new_pos2 = (pos2[0]+i, pos2[1])
                    new_pos = [new_pos1, new_pos2, cost+1]
                    if sorted(new_pos[:-1]) not in visited:
                        #방문 표시
                        visited.append(sorted(new_pos[:-1]))
                        #q에 추가
                        q.append(new_pos)
        #세로로 놓여 있는 경우의 회전
        elif pos1[1] == pos2[1]:
            for i in (1, -1):
                if new_board[pos1[0]][pos1[1]+i] == 0 and new_board[pos2[0]][pos2[1]+i] == 0:
                    #왼쪽 으로 회전하는 경우
                    new_pos1 = (pos1[0], pos1[1])
                    new_pos2 = (pos1[0], pos1[1]+i)
                    new_pos = [new_pos1, new_pos2, cost+1]
                    if sorted(new_pos[:-1]) not in visited:
                        #방문 표시
                        visited.append(sorted(new_pos[:-1]))
                        #q에 추가
                        q.append(new_pos)
                    #오른쪽으로 회전하는경우
                    new_pos1 = (pos2[0], pos2[1])
                    new_pos2 = (pos2[0], pos2[1]+i)
                    new_pos = [new_pos1, new_pos2, cost+1]
                    if sorted(new_pos[:-1]) not in visited:
                        #방문 표시
                        visited.append(sorted(new_pos[:-1]))
                        #q에 추가
                        q.append(new_pos)
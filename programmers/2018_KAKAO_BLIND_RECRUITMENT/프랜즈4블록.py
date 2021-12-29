def solution(m, n, board):
    new_board = []
    for row in board:
        new_board.append(list(row))
    dx = [0, 1, 1]
    dy = [1, 0, 1]  
    total_count = 0

    while True:
        block_count = 0
        remove = [[False] * n for _ in range(m)]
        for x in range(m):
            for y in range(n):
                if new_board[x][y] != '0':
                    block = new_board[x][y]
                    count = 1
                    for i in range(3):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if 0<= nx < m and 0 <= ny < n:
                            if new_board[nx][ny] != block:
                                break
                            else:
                                count += 1

                    # 2 x 2가 동일한 경우라면
                    if count == 4:
                        remove[x][y] = True
                        for i in range(3):
                            nx = x + dx[i]
                            ny = y + dy[i]
                            remove[nx][ny] = True

        #블록을 지워주며 지워진 블록 카운트
        for x in range(m):
            for y in range(n):
                if remove[x][y] :
                    new_board[x][y] = '0'
                    block_count += 1

        #남아있는 캐릭터를 아래쪽부터 확인하며 차례대로 밑으로 내려주기
        for x in range(m-2, -1, -1):
            for y in range(n):
                #빈공간이 아니라면
                if new_board[x][y] != '0':
                    #아래로 내려가면서 확인
                    block = new_board[x][y]
                    #바로 아래 공간이 있다면
                    if new_board[x+1][y] == '0':
                        for i in range(1, m):
                            #x+i 1, 2, 3
                            if x+i < m:
                                #아래가 빈 공간이 아닌경우
                                if new_board[x+i][y] != '0':
                                    #바로 위에 블록을 내려놓기
                                    new_board[x+i-1][y] = block
                                    #원래 있던 자리는 빈공간으로 만들기
                                    new_board[x][y] = '0'
                                    break
                                #바닥까지 내려간 경우
                                if x+i == m-1 and new_board[x+i][y] == '0':
                                    new_board[x+i][y] = block
                                    #원래 있던 자리는 빈공간으로 만들기
                                    new_board[x][y] = '0'
        #지워진 블록 누적 카운트
        if block_count > 0:
            total_count += block_count
        else:
            break
    return total_count
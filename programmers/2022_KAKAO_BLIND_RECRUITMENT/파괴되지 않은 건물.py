def solution(board, skill):
    n = len(board)
    m = len(board[0])
    skill_board = [[0] * (m+1) for _ in range(n+1)]

    # 2D prefix sum
    for type, r1, c1, r2, c2, degree in skill:
        if type == 1:
            skill_board[r1][c1] -= degree
            skill_board[r1][c2+1] += degree
            skill_board[r2+1][c2+1] -= degree
            skill_board[r2+1][c1] += degree
        else:
            skill_board[r1][c1] += degree
            skill_board[r1][c2+1] -= degree
            skill_board[r2+1][c2+1] += degree
            skill_board[r2+1][c1] -= degree
    for row in range(n+1):
        for col in range(1, m+1):
            skill_board[row][col] += skill_board[row][col-1]
    for col in range(m+1):
        for row in range(1, n+1):
            skill_board[row][col] += skill_board[row-1][col]

    # skill 적용
    for row in range(n):
        for col in range(m):
            board[row][col] += skill_board[row][col]

    # 0 보다 큰 원소 count
    cnt = 0
    for row in board:
        for col in row:
            if col >0:
                cnt += 1
    return cnt
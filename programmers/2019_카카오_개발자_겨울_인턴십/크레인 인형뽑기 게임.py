def solution(board, moves):
    result = 0
    stack = [0]
    n = len(board)
    for move in moves:
        for i in range(n):
            if board[i][move-1] != 0:
                if stack[-1] == board[i][move-1]:
                    stack.pop()
                    result += 2
                    board[i][move-1] = 0
                    break
                else:
                    stack.append(board[i][move-1])
                    board[i][move-1] = 0
                    break
    return result
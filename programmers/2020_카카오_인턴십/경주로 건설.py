from collections import deque

def solution(board):
    n = len(board)
    direction = [[-1, 0, 0], [1, 0, 1], [0, -1, 2], [0, 1, 3]]
    inf = int(1e9)

    dp = [[[inf]*n for _ in range(n)] for _ in range(4)]
    q = deque([[0, 0, 0, 1], [0, 0, 0, 3]])
    # dp테이블 접근 방법 : 방향, x, y
    dp[1][0][0] = 0
    dp[3][0][0] = 0

    while q:
        x, y, cost, d = q.popleft()
        for i in range(4):
            nx = x + direction[i][0]
            ny = y + direction[i][1]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] != 1:
                new_cost  = cost + 1
                if d != direction[i][2]:
                    new_cost += 5
                # 3차원 dp 테이블 이기 때문에 다른 방향에서 왔더라도 cost가 같은 경우를 고려하지 않아도됨
                # 다른 방향에서 왔을때 같인 경우를 고려하면 무한루프가 생길 수 있음
                if dp[direction[i][2]][nx][ny] > new_cost:
                    dp[direction[i][2]][nx][ny] = new_cost
                
                    # 최종지점 까지 건설하였다가 다시 뒤로 돌아가는것을 막기 위함
                    # TC 11에서 무한 루프가 발생하여 추가
                    if nx == n -1 and ny == n -1:
                        continue
                    q.append([nx, ny, new_cost, direction[i][2]])
                    
    result = inf
    for i in range(4):
        result = min(result, dp[i][-1][-1])                   
    return result * 100

#다시 풀어본 풀이
from collections import deque

def solution(board):
    n = len(board)
    inf = int(1e9)
    new_board = [ [[inf]*n for _ in range(n)] for _ in range(4)]
    
    # 상, 하, 좌, 우 = 0, 1, 2, 3
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque([[0, 0, 0, 1], [0, 0, 0, 3]])
    for i in range(4):
        new_board[i][0][0] = 0
    def bfs():
        while q:
            x, y, cost, direction = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0<= ny < n and board[nx][ny] != 1 :
                    if direction != i:
                        new_cost = cost + 6
                    else:
                        new_cost = cost + 1
                    if new_board[i][nx][ny] > new_cost:
                        q.append([nx, ny, new_cost, i])
                        new_board[i][nx][ny] = new_cost
    bfs()
    result = int(1e9)
    for i in range(4):
        result = min(result, new_board[i][-1][-1])
    return result*100
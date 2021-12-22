#1215
from collections import deque
from sys import stdin
n, m, x, y, k = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
directions = list(map(int, stdin.readline().rstrip().split()))
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

dice = [[[2,0]], 
      [[4,0],[1,0],[3,0]], 
        [[5,0]],
        [[6,0]]]

def rotate(dice, d):
    #동쪽으로 이동
    if d == 1:
        q = deque(dice[1])
        q.rotate(-1)
        shifted_list = list(q)
        dice[1] = shifted_list
        dice[1][-1], dice[3][0] = dice[3][0], dice[1][-1]
    #서쪽으로 이동
    elif d == 2:
        q = deque(dice[1])
        q.rotate(1)
        shifted_list = list(q)
        dice[1] = shifted_list
        dice[1][0], dice[3][0] = dice[3][0], dice[1][0]
    #북쪽으로 이동
    elif d == 3:
         dice[1][1], dice[2][0], dice[3][0], dice[0][0] = dice[0][0], dice[1][1], dice[2][0], dice[3][0]
    #남쪽으로 이동
    else:
        dice[3][0], dice[0][0], dice[1][1], dice[2][0] = dice[0][0], dice[1][1], dice[2][0], dice[3][0]
    return dice

for d in directions:
    #주사위 위치 이동
    nx = x + dx[d-1]
    ny = y + dy[d-1]
    #바깥으로 나가지 않는 명령일 경우
    if 0<=nx<n and 0<=ny<m:
        #주사위 회전
        dice = rotate(dice, d)
        #이동한 위치의 숫자가 0경우 주사위의 바닥면의 숫자를 칸에 복사
        if graph[nx][ny] == 0:
            graph[nx][ny] = dice[1][1][1]
        #이동한 위치의 숫자가 0이 아닌경우
        else:
            #칸에 쓰여있는 수를 주사위에 복사
            dice[1][1][1] = graph[nx][ny]
            #해당칸은 0이됨
            graph[nx][ny] = 0
        #주사위의 상단 값 출력
        up = 7-dice[1][1][0]
        for row in dice:
            for col in row:
                if col[0] == up:
                    print(col[1])
        #주사위의 위치 초기화
        x, y = nx, ny
    #바깥으로 나가는 명령일경우
    else:
        continue
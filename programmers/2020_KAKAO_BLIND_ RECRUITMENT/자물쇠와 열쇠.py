def rotate_key(key, m):
    new_key = [[0]*m for _ in range(m)]
    for x in range(m):
        for y in range(m):
            new_key[y][m-1-x] = key[x][y]
    return new_key

def check(lock, n):
    for i in range(n):
        for j in range(n):
            if lock[i+n][j+n] != 1:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)
    #자물쇠 초기화
    new_lock = [[0]*(n*3) for _ in range(n*3)]
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]

    #4번 회전
    for _ in range(4):
        key = rotate_key(key, m)  
        #열쇠를 넣어볼 시작지점
        for i in range(n*2):
            for j in range(n*2):
                #열쇠 넣기
                for x in range(m):
                    for y in range(m):
                        new_lock[i+x][j+y] = new_lock[i+x][j+y] + key[x][y]
                #만약에 열쇠가 맞다면 True return
                if check(new_lock, n):
                    return True
                #열쇠 빼기
                for x in range(m):
                    for y in range(m):
                        new_lock[i+x][j+y] = new_lock[i+x][j+y] - key[x][y]

    return False
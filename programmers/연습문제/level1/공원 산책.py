from collections import deque

def solution(park, routes):
    s_x, s_y = 0, 0
    for y, row in enumerate(park):
        for x, col in enumerate(row):
            if park[y][x] == 'S':
                s_x, s_y = x, y            
    H = len(park)
    W = len(park[0])
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    dict_ = {'H' : 0, 'S' : 1, 'W' : 2, 'E' : 3} 
    q = deque([ ])
    for r in routes:
        d, n = r.split()
        q.append([d, int(n)])
        
    while q:
        d, n = q.popleft()
        temp_x, temp_y = s_x, s_y
        for _ in range(n):
            nx = temp_x + dx[dict_[d]]
            ny = temp_y + dy[dict_[d]]
            if 0 <= nx < W and 0 <= ny < H and park[ny][nx] != 'X':
                temp_x = nx
                temp_y = ny
            else:
                break   
        else:
            s_x, s_y = temp_x, temp_y
    answer = [s_y, s_x]
    return answer
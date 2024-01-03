from collections import deque
# 상하좌우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

land_dict = {}
def bfs(land, x, y, visited, n, m, land_id):
    arr = [(x, y)]
    res = 1
    visited[y][x] = True
    q = deque([[x, y]])
    while q:
        x, y  = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if land[ny][nx] != 0 and visited[ny][nx] == False:
                    res += 1
                    visited[ny][nx] = True
                    q.append([nx,ny])
                    arr.append((nx, ny))
    for location in arr:
        land_dict[location] = [land_id, res]

def solution(land):
    answer = 0
    
    # 땅의 가로 길이
    m = len(land[0])
    # 땅의 세로 길이
    n = len(land)
    visited = [[False] * m for _ in range(n)]
    
    land_id = 0
    for x in range(m):
        for y in range(n):
            if land[y][x] == 1 and visited[y][x] == False:
                bfs(land, x, y, visited, n, m, land_id)
                land_id += 1    
    
    for x in range(m):
        id_dict = {}
        area_arr = []
        for y in range(n):
            if (x, y) in land_dict:
                land_id = land_dict[(x, y)][0]
                area = land_dict[(x, y)][1]
                if land_id not in id_dict:
                    id_dict[land_id] = 1
                    area_arr.append(area)
        answer =  max(answer, sum(area_arr))
    return answer
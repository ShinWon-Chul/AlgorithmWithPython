from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(sx, sy, place, visited):
    q = deque([[sx, sy, 0]])
    visited[sx][sy] = True
    while q:
        x, y, dist = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 5 and 0 <= ny < 5:
                if not visited[nx][ny] and place[nx][ny] == 'P' :
                    visited[nx][ny] = True
                    cost = dist + 1
                    if cost <= 2 :
                        return False
                    else :
                        q.append([nx, ny, cost])
                if not visited[nx][ny] and place[nx][ny] == 'O':
                    visited[nx][ny] = True
                    cost = dist + 1
                    q.append([nx, ny, cost])
                    
    return True

def solution(places):
    result = []
    for place in places:
        persons = []
        for sx in range(5):
            for sy in range(5):
                if place[sx][sy] == 'P':
                    persons.append([sx, sy])
        boolean = True
        for sx, sy in persons:
            visited = [ [False] * 5 for _ in range(5) ]
            if not bfs(sx, sy, place, visited):
                result.append(0)
                boolean = False
                break
        if boolean:
            result.append(1)
    return result
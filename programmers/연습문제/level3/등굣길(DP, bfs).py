from collections import deque

def solution(m, n, puddles):
    dx = [1, 0]
    dy = [0, 1]
    graph = [[0]*m for _ in range(n)]
    graph[0][0] = 1
    
    def bfs():
        q = deque([[0, 0]])
        while q:
            x, y = q.popleft()
            for i in range(2):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx<n and ny<m and [ny+1,nx+1] not in puddles:
                    if graph[nx][ny]==0:
                        if nx == 0:
                            graph[nx][ny] = graph[nx][ny-1]
                            q.append([nx,ny])
                        elif ny == 0:
                            graph[nx][ny] = graph[nx-1][ny]
                            q.append([nx,ny])
                        else:
                            graph[nx][ny] = graph[nx-1][ny] + graph[nx][ny-1]
                            q.append([nx,ny])
    
    bfs()
    return int(graph[-1][-1]%1000000007)
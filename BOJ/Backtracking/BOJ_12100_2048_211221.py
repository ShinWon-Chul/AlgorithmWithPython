import copy

def rotate_a_matrix_by_90_degree(a):
    row_length = len(a)
    column_length = len(a[0])
    
    res = [[0] * row_length for _ in range(column_length)]
    for r in range(row_length):
        for c in range(column_length):
            res[c][row_length-1-r] = a[r][c]
    
    return res

def move(graph, visited, d, count):
    global total_result
    if count < 5:
        #방향에 따라서 그래프 회전
        for _ in range(d):
            graph = rotate_a_matrix_by_90_degree(graph)
        for x in range(n):
            for y in range(n):
                nx = x + dx
                ny = y + dy
                while 0<= nx < n and 0<= ny < n:
                    #계속 진행 하다 숫자가 없는 벽을 만난 경우    
                    if nx == 0 and graph[nx][ny] == 0:
                        graph[nx][ny] = graph[x][y]
                        graph[x][y] = 0
                    #숫자를 만난 경우
                    if graph[nx][ny] != 0 :
                        #만난 숫자가 아직 합쳐진 숫자가 아닌 경우
                        if visited[nx][ny] == 0:
                            #현재 숫자와 동일한 경우
                            if graph[nx][ny] == graph[x][y]:
                                graph[nx][ny] += graph[x][y]
                                graph[x][y] = 0
                                visited[nx][ny] = 1
                                break
                            #만난 숫자가 다른 숫자인 경우
                            else:
                                #시작 지점 바로 위인경우
                                if nx-dx == x and ny-dy == y:
                                    break
                                else:#어느정도 거리가 있는경우
                                    graph[nx-dx][ny-dy] = graph[x][y]
                                    graph[x][y] = 0
                                    break
                        #만난 숫자가 합쳐진 숫자인 경우
                        else:
                            #시작 지점 바로 위인경우
                            if nx-dx == x and ny-dy == y:
                                break
                            else:#어느정도 거리가 있는경우
                                graph[nx-dx][ny-dy] = graph[x][y]
                                graph[x][y] = 0
                                break
                    #숫자가 아닌경우는 계속 진행
                    else:
                        nx = nx + dx
                        ny = ny + dy
        #모두 끝났을때 다시 원래 대로 회전
        #위로 올린 경우는 회전 하지 않아도 됨
        if d == 0:
            for nd in range(4):
                visited = [[0]*n for _ in range(n)]
                move(copy.deepcopy(graph), copy.deepcopy(visited), nd, count+1)
            
                #back_tracking
        else:
            for _ in range(4-d):
                graph = rotate_a_matrix_by_90_degree(graph)
            for nd in range(4):
                visited = [[0]*n for _ in range(n)]
                move(copy.deepcopy(graph), copy.deepcopy(visited), nd, count+1) 
    
    else:
#         print(graph)
        result = 0
        for x in range(n):
            for y in range(n):
                result = max(result, graph[x][y])
        total_result = max(total_result, result)

        
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
visited = [[0]*n for _ in range(n)]
dx = -1
dy = 0
visited = [[0]*n for _ in range(n)]
total_result = 0
count = 0
for i in range(4):
    move(copy.deepcopy(graph), copy.deepcopy(visited), i, count)
print(total_result)
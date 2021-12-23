import heapq
from sys import stdin
count = 0
while True:
    n = int(input())
    
    if n != 0:
        count += 1
        graph = []
        for _ in range(n):
            graph.append(list(map(int, stdin.readline().split())))


        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        inf = int(10e9)
        distance = [[inf] * n for _ in range(n)]
        distance[0][0] = graph[0][0]
        #최소힙의 초기 상태
        h = [(graph[0][0], (0, 0))]

        def dijkstra():
            while h:
                d, node = heapq.heappop(h)
                x, y = node
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    #범위 안에 있을때
                    if 0 <= nx < n and 0 <= ny < n:
                        #힙에서 꺼낸 노드의 최소 거리보다 distance 테이블의 거리가 더 작다면 넘어감
                        if distance[x][y] < d:
                            continue
                        else:
                            dist = graph[nx][ny] + d
                            if dist < distance[nx][ny]:
                                distance[nx][ny] = dist
                                heapq.heappush(h, (dist, (nx, ny)))
        dijkstra()
        print(f"Problem {count}: {distance[-1][-1]}")
    else:
        break
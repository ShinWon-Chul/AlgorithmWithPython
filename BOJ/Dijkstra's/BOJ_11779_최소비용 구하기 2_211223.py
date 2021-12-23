'''출발도시 에서 도착도시 까지의 최단 경로와 그 경로 사이에 있는 도시를 구하는 문제'''
import heapq
n = int(input()) #도시의 갯수
m = int(input()) #버스의 갯수

#그래프 생성
graph = [[] for _ in range(n+1)]
for _ in range(m):
    s, e, cost = map(int, input().split())
    graph[s].append([cost, e])
    
start, end = map(int, input().split()) #출발 도시, 도착 도시


#거리 초기화
inf = int(10e9)
distances = [inf] * (n+1)
distances[start] = 0

#path저장할 배열
path = [[] for _ in range(n + 1)]
path[start] = [start]
def dijkstra(start):
    h = []
    heapq.heappush(h, (0, start))
    while h:
        cost_, node = heapq.heappop(h)
        if distances[node] < cost_:
            continue
        else:
            for c, n in graph[node]:
                dist = c + cost_
                if distances[n] > dist:
                    distances[n] = dist
                    heapq.heappush(h, (dist, n))
                    path[n] = [] 
                    for p in path[node]: 
                        path[n].append(p) 
                    path[n].append(n)

dijkstra(start)
print(distances[end])
print(len(path[end]))
print(' '.join(map(str, path[end])))
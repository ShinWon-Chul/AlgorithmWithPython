from heapq import heappop, heappush
N = int(input())
M = int(input())
data = [ list(map(int, input().split())) for _ in range(M)]
start, end = list(map(int, input().split()))

graph = [[] for _ in range(N+1)]
for s, e, c, in data:
    graph[s].append((c, e))
inf = int(1e9)
distance = [inf] * (N+1)
distance[start] = 0
h = []
def Dijkstra():
    heappush(h, (0, start))
    while h:
        dist, c_n = heappop(h)
        # 최단 경로가 이미 정해져 있는 경우
        if dist > distance[c_n]:
            continue
        else:
            # 현재 최단 경로에서 다른 경로로 갈 수 있는 노드
            for n_node in graph[c_n]:
                # 현재 노드의 최단 경로에서 다른  로드로 갈 수 있는 거리
                n_dist = dist + n_node[0]
                # 그 거리가 최단 경로로 구해진 거리보다 짧다면
                if n_dist < distance[n_node[1]]:
                    distance[n_node[1]] = n_dist
                    heappush(h, (n_dist, n_node[1]))
Dijkstra()
print(distance[end])
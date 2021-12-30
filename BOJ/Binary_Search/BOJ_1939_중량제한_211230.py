from collections import deque

n, m = map(int, input().split()) #노드 엣지
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
start, end = map(int, input().split()) #출발지, 목적지

#중량 제한
min_weight = 1
max_weight = int(1e9)

#이분탐색으로 mid중량을 넘을 수 있는 다리의 경우에만 탐색 진행
def bfs(weight):
    q = deque([start])
    while q:
        city = q.popleft()
        for n_city, n_bw in graph[city]:
            if n_bw >= weight and n_city not in visited:
                visited.add(n_city)
                q.append(n_city)
    return True if end in visited else False


while min_weight <= max_weight:
    mid = int((min_weight + max_weight) / 2)
    visited = set()

    #중량이 통과된다면 중량을 증가시키기 위해 최소 중량을 증가
    if bfs(mid):
        min_weight = mid + 1
        result = mid
    #중량이 통과되지 않는다면 중량을 감소 시키기 위해 최대 중량을 감소
    else:
        max_weight = mid - 1

print(result)
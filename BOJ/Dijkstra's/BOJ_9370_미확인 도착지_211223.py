import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

from heapq import heappush, heappop

def dijkstra(start):
    q = []

    distances = [inf] * (n+1)

    heappush(q, (0, start))
    distances[start] = 0
    while q:
        dist, now = heappop(q)
        #다음 노드의 최소 거리를 계산할 노드의 시작점으로부터의 최단거리가, distance에 기록된 거리보다 길다면 넘어감
        if distances[now] < dist:
            continue
        # 만약 더 작다면 현재 노드로부터 다음 노드까지의 비용을 계산
        for i in graph[now]:
            cost = dist + i[0]
            #새로운 최단거리를 찾았다!
            if distances[i[1]] > cost:
                distances[i[1]] = cost
                heappush(q, (cost, i[1]))
                #새로 찾은 노드의 최단 거리 갱신
    return distances
    
tc = int(input())
for _ in range(tc):
    n, m ,t = map(int, input().split()) #노드, 엣지, 목적지 수
    s, g, h = map(int, input().split()) #출발지, g, h

    inf = int(1e9)

    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((c, b))
        graph[b].append((c, a))

    target = []
    for _ in range(t):
        target.append(int(input()))

    s_dijk = dijkstra(s)
    g_dijk = dijkstra(g)
    h_dijk = dijkstra(h)

    result = []
    for ta in target:
        if s_dijk[g] + g_dijk[h] + h_dijk[ta] == s_dijk[ta] or s_dijk[h] + h_dijk[g] + g_dijk[ta] == s_dijk[ta] :
            result.append(ta)
    result.sort()
    for w in result:
        print(w, end = ' ')
    print()
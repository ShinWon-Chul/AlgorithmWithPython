from heapq import heappush, heappop

def dijkstra(start, distance, graph):
    h = []
    heappush(h, (0, start))
    distance[start] = 0
    while h:
        cost, currend_node = heappop(h)
        #이미 처리된 노드는 건너뜀
        if cost > distance[currend_node]:
            continue
        for dist, node in graph[currend_node]:
            if distance[node] > dist + cost:
                dist += cost
                distance[node] = dist
                heappush(h, (dist, node))
    return distance

def solution(n, s, a, b, fares):
    inf  = int(1e9)
    # distance = [inf] * (n+1)
    graph = [[] for _ in range(n+1)]
    for sn, en, c in fares:
        graph[sn].append((c, en))
        graph[en].append((c, sn))

    answer = inf
    for i in range(1, n+1):
        s_distance = [inf] * (n+1)
        a_distance = [inf] * (n+1)
        b_distance = [inf] * (n+1)
        answer = min(answer,dijkstra(s, s_distance, graph)[i] + dijkstra(i, a_distance, graph)[a] + dijkstra(i, b_distance, graph)[b])

    return answer 
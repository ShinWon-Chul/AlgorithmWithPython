# 최단 경로를 구하는 문제로 먼저 다익스트라 알고리즘을 적용해보겠습니다.
# 노드가 N개 200, 간선 M이 10000개 이므로 최대 N*M의 시간 복잡도로 문제를 해결할 수 있습니다.

import heapq

# 입력을 받겠습니다.
N, M  = list(map(int, input().split()))
INF = int(1e9)

graph = {}
for _ in range(M):
	s, e, t = list(map(int, input().split()))
	if s not in graph:
		graph[s] = [[e, t]]
	else:
		graph[s].append([e, t])
	if e not in graph:
		graph[e] = [[s, t]]
	else:
		graph[e].append([s, t])

# 최단 경로를 구할 다익스트라 함수를 작성하겠습니다.
def Dijkstra(start):
	time_arr = [INF] * (N + 1)
	first_hop = [0] * (N + 1)
	first_hop[start] = '-'
	time_arr[start] = 0

	h = []
	heapq.heappush(h, [0, start])

	while h:
		time, node = heapq.heappop(h)

		# 이미 최단 경로가 있다면 건너 뜁니다.
		if time > time_arr[node]:
			continue
		for n_node, cost in graph[node]:
			n_cost = time + cost
			if time_arr[n_node] > n_cost:
				time_arr[n_node] = n_cost
				heapq.heappush(h, [n_cost, n_node])
				# 첫 번째로 거치는 노드를 기록
				if node == start:
					first_hop[n_node] = n_node
				else:
					first_hop[n_node] = first_hop[node]
					
	return time_arr, first_hop

for i in range(1, N+1):
	arr, first_hop = Dijkstra(i)
	first_hop = first_hop[1:]
	first_hop = ' '.join(list(map(str, first_hop)))
	print(first_hop)
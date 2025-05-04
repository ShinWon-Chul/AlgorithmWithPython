N, M  = list(map(int, input().split()))

graph = []

for _ in range(M):
	graph.append(list(map(int, input().split())))

INF = int(1e9)
distance = [INF] * (N + 1)
distance[1] = 0

def bellman_ford():
	is_cycel = False
	for i in range(N-1):
		for a, b, c in graph:
			if distance[a] != INF and distance[b] > distance[a] + c:
				distance[b] = distance[a] + c

	# 음의 사이클이 있는지 검사하겠습니다.
	for a, b, c in graph:
		if distance[a] != INF and distance[b] > distance[a] + c:
			is_cycel = True

	return is_cycel

is_cycel = bellman_ford()

# print(distance)
if is_cycel:
	print(-1)
else:
	for i in range(2, N+1):
		if distance[i] == INF:
			print(-1)
		else:
			print(distance[i])


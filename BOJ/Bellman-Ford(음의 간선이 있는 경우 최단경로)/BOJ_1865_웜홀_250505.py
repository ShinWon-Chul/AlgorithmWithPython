# 먼저 상수 조건을 확인하겠습니다.
# TC의 갯수는 최대 5입니다.
# 정점의 수 는 N =500, 도로의 수 M = 2500 입니다.
# 벨만 포드 알고리즘을 활용해서 N^2 = 2500 최대 5 * 2500의 시간 복잡도로 문제를 풀 수 있습니다.

# # 입력을 받겠습니다.
# TC = int(input())
# INF = int(1e9)

# for _ in range(TC):
# 	N, M, W = list(map(int, input().split()))
# 	# 그래프를 정의 하겠습니다.
# 	graph = []
# 	# 도로 입력 (양방향)
# 	for _ in range(M):
# 		S, E, T = map(int, input().split())
# 		graph.append((S, E, T))
# 		graph.append((E, S, T))

# 	# 웜홀 입력 (단방향, 음수 시간)
# 	for _ in range(W):
# 		S, E, T = map(int, input().split())
# 		graph.append((S, E, -T))

# 	# start, end, time = list(map(int, input().split()))

# 	# 그래프의 최단 경로를 저장한 distance 배열을 선언 하겠습니다.
# 	distance_arr = [INF] * (N + 1)
# 	distance_arr[1] = 0
# 	def bellman_ford():
# 		# N-1만큼 순회하면서 최단 거리를 갱신하겠습니다.
# 		for i in range(N-1):
# 			for s, e, t in graph:
# 				if distance_arr[s] != INF and distance_arr[e] > distance_arr[s] + t:
# 					distance_arr[e] = distance_arr[s] + t
# 		for u, v, w in graph:
# 			if distance_arr[u] != INF and distance_arr[v] > distance_arr[u] + w:
# 				return True
# 		return False

# 	# bellman_ford()
	
# 	if bellman_ford():
# 		print("YES")
# 	else:
# 		print("NO")

TC = int(input())
INF = int(1e9)

for _ in range(TC):
    N, M, W = map(int, input().split())
    graph = []

    # 도로 입력 (양방향)
    for _ in range(M):
        S, E, T = map(int, input().split())
        graph.append((S, E, T))
        graph.append((E, S, T))

    # 웜홀 입력 (단방향, 음수 시간)
    for _ in range(W):
        S, E, T = map(int, input().split())
        graph.append((S, E, -T))

    def bellman_ford():
	    distance = [0] * (N + 1)  # 모든 정점에서 출발 가능하게 0으로 초기화

	    for _ in range(N - 1):
	        for s, e, t in graph:
	            if distance[e] > distance[s] + t:
	                distance[e] = distance[s] + t

	    for s, e, t in graph:
	        if distance[e] > distance[s] + t:
	            return True  # 음수 사이클 존재
	    return False


    if bellman_ford():
        print("YES")
    else:
        print("NO")

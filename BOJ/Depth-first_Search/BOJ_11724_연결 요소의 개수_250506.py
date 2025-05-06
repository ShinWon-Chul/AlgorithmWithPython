import sys

# 재귀 깊이를 100000까지 허용
sys.setrecursionlimit(int(1e9))

input = sys.stdin.readline

N, M = list(map(int, input().split()))

visited = [False] * (N + 1)
graph = {}
for _ in range(M):
	s, e = list(map(int, input().split()))
	if s not in graph:
		graph[s] = [e]
	else:
		graph[s].append(e)
	if e not in graph:
		graph[e] = [s]
	else:
		graph[e].append(s)

def dfs(start):
	if visited[start]:
		return

	visited[start] = True
	if start in graph:
		for node in graph[start]:
			if not visited[node]:
				dfs(node)

count = 0
for i in range(1, N+1):

	if not visited[i]:
		# visited[i] = True
		dfs(i)
		count += 1

print(count)
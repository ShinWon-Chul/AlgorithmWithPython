from collections import deque

def solution(n, computers):
    count = 0
    graph = [[] for _ in range(n)]
    for i, computer in enumerate(computers):
        for j , connected in enumerate(computer):
            if connected == 1:
                if i != j:
                    graph[i].append(j)

    visited = [False] * n

    def bfs(start):
        q = deque([start])
        while q :
            com = q.popleft()
            for node in graph[com]:
                if not visited[node]:
                    visited[node] = True
                    q.append(node)

    for i in range(n):
        if not visited[i]:
            count += 1
            bfs(i)
    return count
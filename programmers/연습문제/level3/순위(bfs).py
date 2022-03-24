from collections import deque
def bfs(start, graph):
    visited = [False] * (n+1)
    q = deque([start])
    visited[start] = True
    result = []
    while q:
        current = q.popleft()
        for node in graph[current]:
            if not visited[node]:
                result.append(node)
                q.append(node)
                visited[node] = True
            
    return result

def solution(n, results):
    graph = [[] for _ in range(n+1)]
    inv_graph = [[] for _ in range(n+1)]

    for a, b in results:
        graph[b].append(a)
        inv_graph[a].append(b)
        
    count = 0
    for i in range(1, n+1):
        result1 = bfs(i, graph)
        result2 = bfs(i, inv_graph)
        if len(result1 + result2) == n-1:
            count += 1
    return count
from collections import deque

def bfs(start, remove, visited, graph):
    q = deque([start])
    visited[start] = True
    count = 1
    while q:
        cur_node = q.popleft()
        for next_node in graph[cur_node]:
            if not visited[next_node] and next_node != remove:
                visited[next_node] = True
                q.append(next_node)
                count += 1
    return count
    
def solution(n, wires):
    answer = int(1e9)
    graph = [[] for _ in range(n+1)]
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
        
    for a, b in wires:
        visited = [False] * (n+1)
        count1 = bfs(a, b, visited, graph)
        count2 = bfs(b, a, visited, graph)
        diff = abs(count1-count2)
        if diff < answer:
            answer = diff
    return answer
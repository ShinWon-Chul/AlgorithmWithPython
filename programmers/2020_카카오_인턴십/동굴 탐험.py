from collections import deque

# 위상 정렬 함수
def topology_sort(graph, indegree):
    q = deque([0]) # 큐 기능을 위한 deque 라이브러리 사용
    count = 0
    # 큐가 빌 때까지 반복
    while q:
        count += 1
        # 큐에서 원소 꺼내기
        now = q.popleft()
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)
    return count

def bfs(n, graph, indegree):
    new_graph = [[] for i in range(n + 1)]
    visited = [False] * n
    visited[0] = True
    q = deque([0])
    while q:
        cur_node = q.popleft()
        for node in graph[cur_node]:
            if not visited[node]:
                visited[node] = True
                new_graph[cur_node].append(node)
                indegree[node] += 1
                q.append(node)
    return new_graph, indegree

def solution(n, path, order):
    # 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
    graph = [[] for i in range(n + 1)]
    # 모든 노드에 대한 진입차수는 0으로 초기화
    indegree = [0] * (n + 1)
    # 양방향 그래프 생성
    for a, b in path:
        graph[a].append(b)
        graph[b].append(a)
    # bfs를 통해 단방향 그래프 생성
    new_graph, indegree = bfs(n, graph, indegree)
    for a, b in order:
        new_graph[a].append(b) # 정점 A에서 B로 이동 가능
        # 진입 차수를 1 증가
        indegree[b] += 1
    #모든 노드에 대한 위상 정렬이 가능하면 True 아니면 False 반환
    if n == topology_sort(new_graph, indegree):
        return True
    else:
        return False
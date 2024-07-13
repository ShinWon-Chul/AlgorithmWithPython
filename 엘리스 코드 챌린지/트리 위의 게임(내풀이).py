import sys
sys.setrecursionlimit(10**9)

n = int(input())  # 노드 수 입력
graph = [[] for _ in range(n+1)]  # 인접 리스트 초기화

# 간선 입력
for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 방향성을 부여할 새로운 그래프
directed_graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

def build_tree(node):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            directed_graph[node].append(neighbor)
            build_tree(neighbor)

build_tree(1)

def dfs(n, first, second, total, count):
    global max_total, res_first, res_second
    total += n
    
    if not directed_graph[n]:
        if max_total < total:
            max_total = total
            if count % 2 != 0:
                res_first = first + n
                res_second = second
            else:
                res_first = first
                res_second = second + n
        return
    
    for node in directed_graph[n]:
        # 선공
        if count % 2 != 0:
            dfs(node, first + n, second, total, count + 1)
        else:
            dfs(node, first, second + n, total, count + 1)

for i in range(1, n+1):
    max_total = 0
    res_first = 0
    res_second = 0
    dfs(i, 0, 0, 0, 1)
    if res_first >= res_second:
        print(1)
    else:
        print(0)
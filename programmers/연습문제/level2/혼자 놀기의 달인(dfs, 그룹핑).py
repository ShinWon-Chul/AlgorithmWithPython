# dfs를 활용해서 그룹을 찾아서 그룹의 최대값 2개를 곱한다
res = []
def dfs(graph, visited, start, cnt):
    global res
    if visited[start] == 1:
        
        res.append(cnt-1)
        return
    
    visited[start] = 1
    start = graph[start]
    dfs(graph, visited, start, cnt+1)
    
def solution(cards):
    answer = []
    visited = [ 0 for _ in range(len(cards)+1)]
    graph = {}
    for i, v in enumerate(cards):
        graph[i+1] = v
    for i in range(len(cards)):
        if visited[i+1] == 0:
            dfs(graph, visited, i+1, 1)
    res.sort(reverse = True)
    if len(res) > 1:
        return res[0] * res[1]
    else:
        return 0
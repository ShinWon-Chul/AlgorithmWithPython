import sys
sys.setrecursionlimit(10**6)

#최대 양의 수를 count할 변수 정의
max_cnt = 0

def solution(info, edges):
    # 입력받은 간선 정보를 통해 그래프 생성
    graph = [[]for _ in range(len(info)) ]
    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x)

    def dfs(cur, sheep, wolf, path):
        global max_cnt
        
        # 현재 노드에서 양과 늑대 수 count, 양은 0 늑대는 1이므로 xor로 count 구현
        sheep += info[cur]^1
        wolf += info[cur]
        
        # 양 보다 늑대가 많다면 탐색 종료
        if sheep <= wolf:
            return

        # 늑대보다 양이 더 많고, 최대 양의 수보다 count된 양의 수가 더 많다면 max_cnt 갱신
        if max_cnt < sheep:
            max_cnt = sheep
        
        # 방문 가능한 노드 갱신 및 dfs 수행
        for n in path:
            for next_node in graph[n]:
                if next_node not in path:
                    path.append(next_node)
                    dfs(next_node, sheep, wolf, path)
                    path.pop()

    dfs(0, 0, 0, [0])
    
    return max_cnt

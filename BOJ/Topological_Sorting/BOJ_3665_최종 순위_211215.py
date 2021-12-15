from collections import deque
for tc in range(int(input())):
    n = int(input())
    rank = list(map(int, input().split()))
    m = int(input())
    t = []
    for _ in range(m):
        t.append(list(map(int, input().split())))
    #graph 초기화
    graph = [[False] * (n + 1) for _ in range(n + 1)]
    for i, r in enumerate(rank):
        for j in range(i + 1, len(rank)):
            graph[rank[i]][rank[j]] = True

    #진입 차수 초기화
    indegree = [0] * (n + 1)
    for i in range(1, n+1):
        count = 0
        for row in graph:
            if row[i] == True:
                count += 1
        indegree[i] = count

    #변경 등수 적용
    for a, b in t:
        if graph[a][b] == True:
            graph[a][b] = False
            graph[b][a] = True
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1

    #위상 정렬 시작
    q = deque()
    result = []
    certain = True
    cycle = False
    for i in range(1, n+1):
        if indegree[i]== 0:
            q.append(i)
    count = 0
    if len(q) ==0 :
        print("IMPOSSIBLE")
        continue

    else:
        while q:
            if len(q) == 0 and count != n:
                cycle = True
                break
            if len(q) == 2:
                certain = False
                break

            node = q.popleft()
            result.append(node)
            for i, v in enumerate(graph[node]):
                 if v == True:
                    indegree[i] -= 1
            for i in range(1, n+1):
                if i not in result and indegree[i] == 0:
                    q.append(i)

    if not certain:
        print("?")
    elif cycle:
        print("IMPOSSIBLE")
    else:
        for i in result:
            print(i, end=" ")
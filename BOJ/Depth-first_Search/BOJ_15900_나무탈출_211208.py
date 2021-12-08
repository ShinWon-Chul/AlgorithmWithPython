from sys import stdin
N = int(stdin.readline())

graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    i, j = list(map(int, stdin.readline().split()))
    graph[i].append(j)
    graph[j].append(i)

visited = [False] * (N+1)
visited[1] = True

def dfs(n, count):
    global total
    if n != 1 and len(graph[n]) == 1:
        total += count
        return
    for node in graph[n]:
        if visited[node] == False:
            visited[node] = True
            dfs(node, count+1)
            visited[node] = False

total = 0
dfs(1, 0)
if total % 2 == 0:
    print('No')
else:
    print('Yes')
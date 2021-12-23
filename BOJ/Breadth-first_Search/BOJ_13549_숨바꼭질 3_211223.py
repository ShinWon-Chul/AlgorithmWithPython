from collections import deque
n, k = map(int, input().split())
inf = int(10e9)
maximum = 100001
visited = [inf] * maximum
visited [n] = 0
q = deque([n])
while q:
    loc = q.popleft()
    if loc * 2 < maximum and visited[loc * 2] == inf:
        visited[loc * 2] = visited[loc]
        q.appendleft(loc * 2)
    if loc + 1 < maximum and visited[loc + 1] == inf:
        visited[loc + 1] = visited[loc] +1
        q.append(loc + 1)
    if 0 <= loc - 1 and visited[loc - 1] == inf:
        visited[loc - 1] = visited[loc] + 1
        q.append(loc - 1)
print(visited[k])
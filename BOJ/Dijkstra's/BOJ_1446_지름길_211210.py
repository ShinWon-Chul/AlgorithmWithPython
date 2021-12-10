N, D = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(N)]
dis = [i for i in range(D+1)]
for i in range(D+1):
    if i > 0:
        dis[i] = min(dis[i], dis[i-1]+1)
    for s, e, d in li:
        if i == s and e <= D and dis[i]+d < dis[e]:
            dis[e] = dis[i]+d
print(dis[D])
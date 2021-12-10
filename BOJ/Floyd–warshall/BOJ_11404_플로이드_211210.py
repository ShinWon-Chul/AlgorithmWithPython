inf = int(1e9)
n = int(input())
m = int(input())

g = []
for _ in range(m):
    g.append(list(map(int, input().rstrip().split())))
    
metrix = [[inf]*(n+1) for _ in range(n+1)]

for s,e,d in g:
    metrix[s][e] = min(metrix[s][e], d)

for i in range(1, n+1) :
    for j in range(1, n+1):
        if i == j:
            metrix[i][j] = 0
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            metrix[i][j] = min(metrix[i][j], metrix[i][k] + metrix[k][j])   
            
for i in range(1, n+1):
    for j in range(1, n+1):
        print(metrix[i][j], end=" ")
    print()
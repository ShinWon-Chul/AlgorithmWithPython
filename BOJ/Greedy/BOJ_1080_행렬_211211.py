from sys import stdin
n, m = list(map(int, input().split()))
a = [list(map(int,input())) for _ in range(n)]
b = [list(map(int,input())) for _ in range(n)]

def reverse(i, j):
    for x in range(i, i+3):
        for y in range(j, j+3):
            if a[x][y] == 1:
                a[x][y] = 0
            else:
                a[x][y] = 1

count = 0
for x in range(n-2):
    for y in range(m-2):
        if a[x][y] != b[x][y]:
            reverse(x, y)
            count += 1
            
result = 0
for x in range(n):
    for y in range(m):
        if a[x][y] != b[x][y]:
            result = -1
            
if result == -1:
    print(-1)
else:
    print(count)
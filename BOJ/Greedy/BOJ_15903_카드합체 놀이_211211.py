from sys import stdin
n, m = list(map(int, input().split()))
c = list(map(int, stdin.readline().rstrip().split()))
for _ in range(m):
    c.sort()
    s = sum(c[:2])
    c[0] = s
    c[1] = s

print(sum(c))
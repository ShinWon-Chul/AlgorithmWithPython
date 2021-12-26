from sys import stdin
tc = int(input())
for t in range(tc):
    n = int(input())
    s = []
    for _ in range(2):
        s.append([0] + list(map(int, stdin.readline().rstrip().split())))

    for i in range(1, n+1):
        if i == 1:
            s[0][i] = s[1][i-1]+s[0][i] 
            s[1][i] = s[0][i-1]+s[1][i]

        else:
            s[0][i] = max(max(s[0][i-2], s[1][i-2]) + s[0][i], s[1][i-1]+s[0][i])
            s[1][i] = max(max(s[0][i-2], s[1][i-2]) + s[1][i], s[0][i-1]+s[1][i])

    print(max(s[0][-1], s[1][-1]))
from sys import stdin

N = int(input())
dp = []
for _ in range(N):
    dp.append(list(map(int, stdin.readline().rstrip().split())))

for i in range(1, N):
    for j in range(len(dp[i])):
        if j == 0:
            dp[i][j] = dp[i-1][j]+ dp[i][j]
            continue
        else:
            left = dp[i-1][j-1] + dp[i][j]

        if j == len(dp[i])-1:
            dp[i][j] = dp[i-1][j-1] + dp[i][j]
            continue
        else:
            right = dp[i-1][j] + dp[i][j]

        dp[i][j] = max(right, left)
            
print(max(dp[-1]))
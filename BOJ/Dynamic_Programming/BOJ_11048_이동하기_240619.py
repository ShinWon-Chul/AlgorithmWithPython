h,w = map(int, input().split())
maze = [ list(map(int, input().split())) for _ in range(h)]
dp = [[0 for _ in range(w)] for _ in range(h)]

# dp 배열 초기화
dp[0][0] = maze[0][0]
for i in range(1, h):
    dp[i][0] = dp[i-1][0] + maze[i][0]     
for j in range(1, w):
    dp[0][j] = dp[0][j-1] + maze[0][j]

for i in range(1, h):
    for j in range(1, w):
        dp[i][j] = max(dp[i-1][j-1]+ maze[i][j], dp[i][j-1]+ maze[i][j], dp[i-1][j]+ maze[i][j])
print(dp[h-1][w-1])
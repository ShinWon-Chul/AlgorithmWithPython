n = int(input())
dp = [1, 2, 4]
for i in range(3, int(1e6)):
	dp.append((dp[i-1] + dp[i-2] + dp[i-3])%1000000009)
for _ in range(n):
	num = int(input())
	print(dp[num-1])


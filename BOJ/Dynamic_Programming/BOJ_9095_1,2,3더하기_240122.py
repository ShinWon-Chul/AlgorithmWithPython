n = int(input())

for _ in range(n):
	# m=4
	m = int(input())
	
	dp = [0 for _ in range(11+1)]
	
	dp[0] = 1
	dp[1] = 1
	dp[2] = 2
	
	if m > 2:
		for i in range(3, m+1): # 3, 4
			for j in range(1, 4): #1, 2, 3
				dp[i] = dp[i] + dp[i-j]
		print(dp[m])
	else:
		print(dp[m])
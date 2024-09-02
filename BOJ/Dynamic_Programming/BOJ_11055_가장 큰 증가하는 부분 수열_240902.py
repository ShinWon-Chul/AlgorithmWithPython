n = int(input())
A = list(map(int, input().split()))

dp = [0] * n
dp[0] = A[0]

for i in range(1, n):
    max_sum = 0
    for j in range(i):
        if A[j] < A[i]:
            max_sum = max(max_sum, dp[j])
    
    dp[i] = max_sum + A[i]

print(max(dp))
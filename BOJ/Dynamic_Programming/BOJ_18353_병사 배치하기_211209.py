from sys import stdin
n = int(input())
sol = list(map(int, stdin.readline().rstrip().split()))
dp = [1] * n
sol.reverse()

for i in range(1, n):
    for j in range(0, i):
        if sol[j] < sol[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(n - max(dp))
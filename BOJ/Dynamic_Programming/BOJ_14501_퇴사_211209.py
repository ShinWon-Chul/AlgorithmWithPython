n = int(input())
t = []
p = []
for _ in range(n):
    ti, pi = list(map(int, input().split()))
    t.append(ti)
    p.append(pi)
    
dp = [0] * (n+1)

result = 0
for i in range(n-1, -1, -1):
    time = t[i]
    if i+time <= n:
        dp[i] = max(p[i] + dp[i+time], result)
        result = dp[i]
    else:
        dp[i] = result
print(result)

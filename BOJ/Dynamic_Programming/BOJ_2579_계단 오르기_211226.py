n = int(input())
stairs = []
for _ in range(n):
    stairs.append(int(input()))

dp = [0]
dp.append(stairs[0])
if len(stairs) >= 2:
    dp.append(stairs[0]+stairs[1])
stairs = [0] + stairs

for i in range(3, n+1):
    if i < n+1:
        dp.append(max(dp[i-2]+stairs[i], dp[i-3]+stairs[i-1]+stairs[i]))

print(dp[-1])
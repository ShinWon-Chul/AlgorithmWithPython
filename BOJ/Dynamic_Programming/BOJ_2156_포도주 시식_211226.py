n = int(input())
wine = []
for _ in range(n):
    wine.append(int(input()))
    
dp = [0]
dp.append(wine[0])
if len(wine) >= 2:
    dp.append(wine[0]+wine[1])
wine = [0] + wine

for i in range(3, n+1):
    dp.append(max(dp[i-1],dp[i-2]+wine[i], dp[i-3]+wine[i-1]+wine[i]))

print(dp[-1])
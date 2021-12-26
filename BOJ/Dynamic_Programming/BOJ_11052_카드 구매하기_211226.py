from sys import stdin
n = int(input())
c = list(map(int, stdin.readline().rstrip().split()))

c = [0] + c
dp = [0, c[1]]
for i in range(2, n+1):
    temp_arr = []
    for j in range(1, len(c)):
        if j <= i:
            temp_arr.append(dp[i-j]+c[j])
    dp.append(max(temp_arr))
print(dp[-1])
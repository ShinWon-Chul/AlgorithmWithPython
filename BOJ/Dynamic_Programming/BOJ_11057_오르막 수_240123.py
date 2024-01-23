"""
오르막 수는 수의 자리가 오름차순을 이루는 수를 말한다. 이때, 인접한 수가 같아도 오름차순으로 친다.

예를 들어, 2234와 3678, 11119는 오르막 수이지만, 2232, 3676, 91111은 오르막 수가 아니다.

수의 길이 N이 주어졌을 때, 오르막 수의 개수를 구하는 프로그램을 작성하시오. 수는 0으로 시작할 수 있다.
"""
n = int(input())
dp = [[1] for _ in range(10)]

for _ in range(n-1):
    dp[9].append(1)
for i in range(n-1):
    for j in range(10):
        num = 0
        for k in range(j, 10):
            num += dp[k][-1]
        dp[j].append(num)
res = 0

for i in range(10):
    res += dp[i][-1]
print(res%10007)
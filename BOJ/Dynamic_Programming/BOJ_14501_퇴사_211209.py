n = int(input())
t = []
p = []
for _ in range(n):
    ti, pi = list(map(int, input().split()))
    t.append(ti) # 시간
    p.append(pi) # 비용

# 각 일에서 시작했을 때 얻을 수 있는 최대 수익을 저장하는 리스트
dp = [0] * (n+1)

result = 0
for i in range(n-1, -1, -1):
    # 현재 일에 필요한 작업 시간을 가져옵니다.
    time = t[i]
    # 현재 일을 시작했을 때, 그 작업이 n일 내에 끝나는지 확인합니다.
    if i+time <= n:
        # (현재 일의 수익)와 (이후에 가능한 최대 수익)을 더한 값과 (이전 최대 수익) 중 더 큰 값으로 갱신합니다.
        dp[i] = max(p[i] + dp[i+time], result)
        result = dp[i]
    # 만약 작업이 기간 내에 끝나지 않는다면
    else:
        dp[i] = result
print(result)

# 2N의 시간 복잡도로 누적합을 사용해 풀이하겠습니다.
# 먼저 입력을 받습니다.

import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))
arr = list(map(int, input().split()))

# 누적합을 저장하기 위한 dp리스트를 선언하겠습니다.
dp = [0] * (N+1)


# 누적합을 계산하겠습니다.
for i in range(1, N+1):
	dp[i] = dp[i-1] + arr[i-1]

answer = 0
# 받을 수 있는 임금의 최대값을 계산하겠습니다.
for i in range(N-M+1):
	answer = max(answer, dp[i+M] - dp[i])
print(answer)

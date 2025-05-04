# 가장긴 증가하는 부분수열을 먼저 구해보겠습니다.
# 상수 조건을 확인하겠습니다.
# 수열의 크기가 N이고 가장긴 증가하는 부분수열을 구하는데 N2의 사간 복잡도를 가집니다.
# 감소도 검사해야 하기때문에 2N^2의 시간복잡도를 갖습니다.
# 첫번째 루프에서 2중으로 증가와 감소를 함께 검사해 up_dp 리스트를 업데이트하는 방식으로 접근하겠습니다.

N = int(input())
arr = list(map(int, input().split()))

# 자기 자신 혼자만으로도 수열이 될 수 있으므로 1로 초기화
# 해당 요소를 끝으로 하는 가장긴 수열의 숫자 수
up_dp = [1] * N
down_dp = [1] * N

# 가장 긴 수열을 찾고
for i in range(1, N):
	for j in range(i):
		if arr[i] > arr[j]:
			up_dp[i] = max(up_dp[i], up_dp[j]+1)
for i in range(N-2, -1, -1):
	for k in range(i+1, N):
		if arr[i] > arr[k]:
			down_dp[i] = max(down_dp[i], down_dp[k]+1)

# print(up_dp)
# print(down_dp)
answer = 0
for i in range(N):
	# 자기 자신을 포함하므로 결과에서 1을 빼겠습니다.
	answer = max(answer, up_dp[i] + down_dp[i]-1)

print(answer)

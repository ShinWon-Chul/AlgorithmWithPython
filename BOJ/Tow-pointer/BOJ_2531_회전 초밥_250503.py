# 연속되는 수열에서 중복되는 수가 가장 적은 수열을 구하는 문제로 볼 수 있습니다.
# 데이터의 처음과 끝이 이어져 있는것을 구현하기 위해 동일한 배열을 이어 붙여야합니다.
# 일단 투포인터 접근법이 떠오르는데 상수 조건을 먼저 확인하겠습니다.
# N이 30000인데 배열 두개를 이어 붙이면 60000입니다.
# log 시간 복잡도에서 해결해야 하고 투포인터 최악의 조건인 2N에서 풀릴 수 있을것같습니다.

# 먼저 입력을 받습니다.
# 초밥 수, 초밥 가지수, 연속 접시 수, 쿠폰 번호
N, d, k, c = list(map(int, input().split()))
arr = []
for _ in range(N):
	arr.append(int(input()))

arr += arr[:k-1] #최적화 포인트!!!

# 투포인터의 start와 end포인터를 정의하겠습니다.
start = 0
end = k
answer = 0

# 투포인터의 핵심 루프를 정의하겠습니다.
while end <= 2*N :
	a = arr[start:end]
	a += [c]
	a_set = set(a)
	num_a_set = len(a_set)
	answer = max(answer, num_a_set)
	start += 1
	end += 1

print(answer)

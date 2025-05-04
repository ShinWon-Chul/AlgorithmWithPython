# 나무를 베어 나무들의 합이 적어도 M미터가 되는 최대값 K를 찾는 문제입니다.
# 상수 조건을 확인하겠습니다.
# 나무의 갯수 N은 100만 입니다. 높이의 합은 1천만 입니다.
# N이 100만 이상이므로 N 시간대 또는 log시간대에 끝내야 합니다.
# 이분탐색으로 접근하겠습니다.

# 먼저 입력을 받겠습니다.

N, M = list(map(int, input().split()))
arr = list(map(int, input().split()))

# 이분탐색을 위한 start, end 변수를 초기화 하겠습니다.
start = 1
end = max(arr)

# 이분 탐색을 위한 루프를 정의하겠습니다.
while start <= end:
	mid = (start + end) // 2
	# mid 높이로 나무를 자르면서 총 길이를 계산 하겠습니다.
	length = 0
	for a in arr:
		if a > mid:
			length += a - mid
	# 총 길에 따른 전기톱의 길이를 조정하겠습니다.
	# 총 길이가 원하는 길이보다 짧다면 전기톱의 길이를 줄여야 합니다.
	if length < M:
		end = mid - 1
	# 원하는 길이보다 크거나 같다면 전기통의 길이를 늘려야 합니다.
	else:
		start = mid + 1
# 적어도 M길이를 얻을 수 있는 최대 길이는 루프가 끝나고 end값으로 얻을 수 있습니다.
print(end)

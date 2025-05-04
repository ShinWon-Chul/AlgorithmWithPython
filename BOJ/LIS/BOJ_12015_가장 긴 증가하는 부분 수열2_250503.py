# 먼저 가장긴 증가하는 부분 수열을 구하는 코드는 N^2의 시간 복잡도를 가집니다.
# N이 100만 이므로 N이나 logN 시간 복잡도에서 해를 구해야 합니다.
# 먼저 가장긴 증가하는 부분 수열 코드를 작성하고 이후에 최적화 해보겠습니다.

# # 입력을 받겠습니다.
# N = int(input())
# arr = list(map(int, input().split()))

# # 해당 인덱스의 요소를 마지막으로 하는 가장 긴 증가하는 부분 수열의 길이를 가지는 dp 배열을 선언합니다.
# # 자기 자신만으로 수열이 될 수 있으므로 각 값을 1로 초기화 합니다.
# dp = [1] * N

# # 가장 긴 증가하는 부분수열을 구하는 루프를 작성하겠습니다.
# for i in range(1, N):
# 	for j in range(i):
# 		if arr[i] > arr[j]:
# 			dp[i] = max(dp[i], dp[j]+1)

# print(max(dp))




# from bisect import bisect_right, bisect_left

# N = int(input())
# arr = list(map(int, input().split()))

# answer_arr = []
# for i in range(N):
	
# 	j = bisect_left(answer_arr, arr[i])
# 	if j == len(answer_arr):
# 		answer_arr.append(arr[i])

# print(len(answer_arr))



#bisect_left로 할 수 있는 NlogN 시간 복잡도 코드
from bisect import bisect_left

# 입력
N = int(input())
arr = list(map(int, input().split()))

# 이분 탐색을 이용한 LIS 저장용 배열
lis = []

for num in arr:
    pos = bisect_left(lis, num)
    if pos == len(lis):
        lis.append(num)
    else:
        lis[pos] = num

# LIS 길이 출력
print(len(lis))

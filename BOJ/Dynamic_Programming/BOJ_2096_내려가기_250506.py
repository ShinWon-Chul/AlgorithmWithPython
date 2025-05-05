# 메모리 제한이 있어 완전 탐색은 불가능 할 것같습니다.
# 다이나믹 프로그래밍으로 문제를 접근해보겠습니다.

# 입력을 받겠습니다.
# import sys
# input = sys.stdin.readline
# N = int(input())

# # 그리드를 정의 하겠습니다.
# arr = []
# for _ in range(N):
# 	arr.append(list(map(int, input().split())))
# 	# 그리드와 동일한 max_dp 배열을 생성하겠습니다.
# 	# max_dp.append([0,0,0])
# 	# min_dp.append([0,0,0])

# max_dp = arr[0]
# min_dp = arr[0]

# for i in range(1, N):
# 	for j in range(3):
# 		if j == 0:
# 			max0 = max(arr[i][j]+max_dp[j], arr[i][j]+max_dp[j+1])
# 		elif j == 1:
# 			max1 = max(arr[i][j]+max_dp[j], arr[i][j]+max_dp[j+1], arr[i][j]+max_dp[j-1])
# 		#j = 2
# 		else:
# 			max2 = max(arr[i][j]+max_dp[j], arr[i][j]+max_dp[j-1])
# 	max_dp = [max0, max1, max2]

# for i in range(1, N):
# 	for j in range(3):
# 		if j == 0:
# 			min0 = min(arr[i][j]+min_dp[j], arr[i][j]+min_dp[j+1])
# 		elif j == 1:
# 			min1 = min(arr[i][j]+min_dp[j], arr[i][j]+min_dp[j+1], arr[i][j]+min_dp[j-1])
# 		#j = 2
# 		else:
# 			min2 = min(arr[i][j]+min_dp[j], arr[i][j]+min_dp[j-1])
# 	min_dp = [min0, min1, min2]
# # print(max_dp)
# print(max(max_dp), min(min_dp))


import sys
input = sys.stdin.readline

N = int(input())

# 첫 줄은 직접 받아서 초기화
a = list(map(int, input().split()))
max_dp = a[:]
min_dp = a[:]

for _ in range(1, N):
    a = list(map(int, input().split()))
    # 다음 줄에서 계산될 새로운 DP 값
    max0 = max(max_dp[0], max_dp[1]) + a[0]
    max1 = max(max_dp[0], max_dp[1], max_dp[2]) + a[1]
    max2 = max(max_dp[1], max_dp[2]) + a[2]

    min0 = min(min_dp[0], min_dp[1]) + a[0]
    min1 = min(min_dp[0], min_dp[1], min_dp[2]) + a[1]
    min2 = min(min_dp[1], min_dp[2]) + a[2]

    max_dp = [max0, max1, max2]
    min_dp = [min0, min1, min2]

print(max(max_dp), min(min_dp))

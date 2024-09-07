n = int(input())  # 수열의 길이 입력
A = list(map(int, input().split()))  # 수열 입력

dp = [0] * n  # DP 테이블 초기화: 각 인덱스에서의 최대 합을 저장할 리스트
# dp[i]는 A[i]를 포함한 증가하는 부분 수열의 최대 합을 의미
dp[0] = A[0]  # 첫 번째 원소는 자신만으로 부분 수열을 이루므로 최대 합은 자기 자신

# 수열을 탐색하여 각 원소를 포함하는 최대 합을 계산
for i in range(1, n):
    max_sum = 0  # A[i]보다 작은 원소들 중에서의 최대 합을 저장할 변수
    for j in range(i):
        # A[i]보다 작은 A[j]에 대해 최대 합을 업데이트
        if A[j] < A[i]:
            max_sum = max(max_sum, dp[j])
    
    # A[i]를 포함하는 최대 합 갱신
    dp[i] = max_sum + A[i]

# DP 테이블 중 최대 값을 출력: 증가하는 부분 수열 중 최대 합
print(max(dp))

"""
A = [1, 100, 2, 50, 60, 3, 5, 6, 7, 8, 1000]
dp = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

i :  1
     A[j] < A[i] :  1 100
     max_sum = max(max_sum, dp[j]) :  0 1
dp = [1, 101, 0, 0, 0, 0, 0, 0, 0, 0, 0]

i :  2
     A[j] < A[i] :  1 2
     max_sum = max(max_sum, dp[j]) :  0 1

dp = [1, 101, 3, 0, 0, 0, 0, 0, 0, 0, 0]

i :  3
     A[j] < A[i] :  1 50
     max_sum = max(max_sum, dp[j]) :  0 1
     A[j] < A[i] :  2 50
     max_sum = max(max_sum, dp[j]) :  1 3
dp = [1, 101, 3, 53, 0, 0, 0, 0, 0, 0, 0]

i :  4
     A[j]< A[i] :  1 60
     max_sum = max(max_sum, dp[j]) :  0 1
     A[j]< A[i] :  2 60
     max_sum = max(max_sum, dp[j]) :  1 3
     A[j]< A[i] :  50 60
     max_sum = max(max_sum, dp[j]) :  3 53
[1, 101, 3, 53, 113, 0, 0, 0, 0, 0, 0]
"""

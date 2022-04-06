def solution(triangle):
    answer = 0
    dp = [[] for _ in range(len(triangle))]
    dp[0] = triangle[0]
    for i in range(1, len(triangle)):
        for j, k in enumerate(triangle[i]):
            if j == 0:
                dp[i].append(dp[i-1][0]+k)
            elif j == len(triangle[i])-1:
                dp[i].append(dp[i-1][-1]+k)
            else:
                dp[i].append(max(dp[i-1][j-1]+k, dp[i-1][j]+k))
    answer = max(dp[-1])
    return answer
N, S = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0

def dfs(idx, current_sum):
    global answer
    if idx == N:
        return
    current_sum += arr[idx]
    if current_sum == S:
        answer += 1
    # 현재 요소 포함 + 다음 탐색
    dfs(idx + 1, current_sum)
    # 현재 요소 미포함 + 다음 탐색
    dfs(idx + 1, current_sum - arr[idx])

dfs(0, 0)
print(answer)

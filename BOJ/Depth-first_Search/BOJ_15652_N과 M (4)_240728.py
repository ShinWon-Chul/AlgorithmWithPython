N, M = list(map(int, input().split()))

def dfs(sequence, start, N, M):
    # 수열의 길이가 M이면 해당값 출력후 return
    if len(sequence) == M:
        print(' '.join(map(str, sequence)))
        return

    # 중복 없이 오름차순 수열을 생성하기 위해 start <= i <= N  같은값으로 다음 수 생성
    for i in range(start, N + 1):
        dfs(sequence + [i], i, N, M)

dfs([], 1, N, M)

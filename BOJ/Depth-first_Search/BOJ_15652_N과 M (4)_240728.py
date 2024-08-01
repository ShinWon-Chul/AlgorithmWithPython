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


"""
재귀 호출의 깊이:
수열의 길이가 M이 될 때까지 재귀 호출이 진행
재귀 호출은 최대 M 번까지 중첩

각 단계에서 가능한 선택지:
각 재귀 호출에서 다음 숫자를 선택할 때, 현재 숫자부터 N까지의 숫자를 시도

O(N^M)
"""
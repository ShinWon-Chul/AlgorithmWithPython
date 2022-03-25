num = 1000000007
def solution(n):
    i = 1
    j = 2
    k = 0
    for _ in range(3, n+1):
        k = i + j
        i, j= j, k
    return int(k%num)
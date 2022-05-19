def solution(land):
    answer = 0
    n = len(land)
    for i in range(1, n):
        for j in range(4):
            arr = []
            for k in range(4):
                if j != k:
                    arr.append(land[i][j]+land[i-1][k])  
            land[i][j] = max(arr)
    return max(land[-1])
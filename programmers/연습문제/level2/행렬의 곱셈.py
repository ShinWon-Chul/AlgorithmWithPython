def solution(arr1, arr2):
    answer = []
    j = len(arr1[0])
    k = len(arr2[0])
    for row in arr1:
        arr = []
        for col_idx2 in range(k):
            col = []
            for row_idx2 in range(j):
                col.append(arr2[row_idx2][col_idx2])
            v = 0
            for idx in range(j):
                v += row[idx]*col[idx]
            arr.append(v)
        answer.append(arr)
    return answer
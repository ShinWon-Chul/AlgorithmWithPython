def solution(data, col, row_begin, row_end):
    answer = 0
    data.sort(key = lambda x : (x[col-1], -x[0]))

    arr = []
    for i in range(row_begin, row_end+1):
        v = 0
        for j in data[i-1]:
            v += j%i
        arr.append(v)
        
    answer = arr[0]
    for v in arr[1:]:
        answer ^= v

    return answer
def solution(common):
    answer = 0
    arr = []
    for i in range(2):
        arr.append(common[i] - common[i+1])
        
    if arr[0] == arr[1]:
        answer = common[-1] - arr[0]
    else:
        answer = common[-1] * (common[1]/common[0])
        
    return answer
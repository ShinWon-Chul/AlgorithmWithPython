def solution(arr):
    answer = 0
    while True:
        answer += 1
        for n in arr:
            if answer % n != 0:
                break
        else:
            break
    return answer
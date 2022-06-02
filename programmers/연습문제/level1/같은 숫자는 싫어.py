def solution(arr):
    answer = [10]
    for num in arr:
        if answer[-1] == num:
            continue
        else:
            answer.append(num)
    return answer[1:]
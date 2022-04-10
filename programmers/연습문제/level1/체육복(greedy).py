def solution(n, lost, reserve):
    answer = 0
    reserve.sort()
    remove = []
    for re in reserve:
        if re in lost:
            remove.append(re)
    for re in remove:
        reserve.remove(re)
        lost.remove(re)
    for re in reserve:
        if re - 1 in lost:
            lost.remove(re-1)
        elif re + 1 in lost:
            lost.remove(re+1)
    answer = n-len(lost)
    return answer
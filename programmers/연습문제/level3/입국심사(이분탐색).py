def solution(n, times):
    start = 1
    end = n * max(times)

    while start <= end:
        mid = int((start + end) / 2)
        person = 0
        for i in times:
            person += int(mid/i)

        if person < n:
            start = mid + 1
        else:
            end = mid - 1
            result = mid
    return result
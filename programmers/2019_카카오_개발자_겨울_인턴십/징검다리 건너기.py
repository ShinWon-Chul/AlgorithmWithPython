def solution(stones, k):
    start = 0
    end = max(stones)
    while start <= end:
        mid = int((start + end) / 2) 
        arr = list(map(lambda x : x-mid, stones))
        count = 0
        for i in arr:
            if count < k:
                if i <= 0:
                    count += 1
                else:
                    count = 0
            else:
                break

        if count < k:
            start = mid + 1
        else:
            end = mid - 1
            result = mid

    return result
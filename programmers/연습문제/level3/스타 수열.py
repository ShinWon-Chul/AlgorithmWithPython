from collections import Counter

def solution(a):
    if len(a) == 1:
        return 0
    cnt = Counter(a)
    n = len(a)
    result = 0
    for num, _ in cnt.most_common():
        valid = [1] * n
        count = 0
        for i, d in enumerate(a):
            if d == num:
                if i == 0:
                    if a[i+1] == num:
                        continue
                    else:
                        valid[i+1] = 0
                        count += 1
                else:
                    if valid[i-1] and a[i-1] != num :
                        valid[i-1] = 0
                        count += 1
                    else :
                        if i + 1 < n:
                            if a[i+1] != num:
                                valid[i+1] = 0
                                count += 1
        result = max(result, count)
        if count == cnt[num]:
            break
    return result*2
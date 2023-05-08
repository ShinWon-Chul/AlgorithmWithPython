def solution(n, m, section):
    answer = 0
    while section:
        s = section[0]
        e = s + m - 1
        while section:
            if section[0] <= e:
                section.pop(0)
            else:
                break
        answer += 1
    return answer
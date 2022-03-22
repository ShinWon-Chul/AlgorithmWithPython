def solution(routes):
    routes.sort()
    cam = -30000
    count = 0
    for start, end in routes:
        if start > cam:
            count += 1
            cam = end
        elif start < cam and end < cam:
            cam = end
        else:
            continue
    return count
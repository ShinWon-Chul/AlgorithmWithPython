def solution(n, stages):
    fails = []
    for stage in range(1, n+1):

        people = 0
        fail = 0
        for i in stages:
            if i > stage:
                people += 1
            elif stage == i:
                people += 1
                fail += 1
        if people == 0:
            ratio = 0
        else:
            ratio = fail/people
        fails.append((stage, ratio))

    fails.sort(key = lambda x : (-x[1], x[0]))
    result = list(map(lambda x : x[0], fails))
    return result
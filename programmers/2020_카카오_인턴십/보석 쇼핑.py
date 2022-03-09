from collections import defaultdict

def solution(gems):
    dictionary = defaultdict(lambda : 0)

    num_gems = len(gems)
    kind = len(set(gems))

    start = 0
    end = 0
    candidate = [] # 모든 종류의 보석을 소유한 지점들
    result = [0, 0] # 가장 짧은 구간중 가장 앞에 있는 구간
    while True:
        own_gems = len(dictionary)
        if start == num_gems:
            break

        # 모든 종류의 보석을 전부 소유했다면 start를 증가하면서 dictionary에서 제외
        if own_gems == kind:
            candidate.append([start+1, end])
            gem = gems[start]
            dictionary[gem] -= 1
            if dictionary[gem] == 0:
                del dictionary[gem]
            start += 1
            continue
        if end == num_gems:
            break

        # 모든 종류의 보석을 전부 소유하지 못했다면 end를 증가하여 dictionary에 추가
        if own_gems != kind:
            gem = gems[end]
            dictionary[gem] += 1
            end += 1
            continue
    interval = int(1e9)
    for s, e in candidate:
        if interval > e - s:
            interval = e - s
            result[0] = s
            result[1] = e
    return result

from collections import defaultdict

#더 빠르고 짧은 풀이 코드
def solution(gems):
    min_gems  = int(1e9)
    len_gems = len(gems) 
    n_gems = len(set(gems))
    end = 0
    temp = defaultdict(lambda : 0)
    for start, gem in enumerate(gems):
        while len(temp) < n_gems and end < len_gems: 
            temp[gems[end]] += 1
            end += 1
        if len(temp) == n_gems:
            if min_gems > end-start:
                min_gems = end-start
                result = [start+1, end]      
        temp[gem] -= 1
        if temp[gem] == 0:
            del(temp[gem])
    return result

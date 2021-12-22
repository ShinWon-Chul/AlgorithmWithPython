from collections import defaultdict
from bisect import bisect_left, bisect_right
import itertools


def solution(info, query):
    answer = []
    dictionary = defaultdict(list)

    for i in info:
        s_info = i.split()
        key = s_info[:-1]
        val = int(s_info[-1])
        # -가 포함된 쿼리
        for i in range(5):
            for x in itertools.combinations(key, i):
                dictionary[''.join(x)]+= [val]
    #딕셔너리 의 각 점수를 오름차순 정렬
    for k in dictionary:
        dictionary[k].sort()

    for q in query:
        q = list(filter(lambda x : x != 'and' and x != '-', q.split()))
        key = ''.join(q[:-1])
        value = int(q[-1])
        if key in dictionary:
            scores = dictionary[key]
            left_index = bisect_left(scores, value)
            
            #list를 슬라이싱 하는데 시간이 들어가는듯 함.. 
            #이미 있는 전체 리스트의 길이에서 left_index를 빼는 방식으로 count하는것도 시간을 줄이는데 중요함
            #answer.append(len(scores[left_index:])) 시간 초과!!!
            answer.append(len(scores)-left_index)
        else:
            answer.append(0)
    return answer
from itertools import combinations
from collections import defaultdict

def solution(clothes):
    clothe_dict = defaultdict(list)
    
    for clothe, kind in clothes:
        clothe_dict[kind].append(clothe)
    length_clothes = list(map(lambda x : len(x), list(clothe_dict.values())))
    
    answer = 1
    for i in length_clothes:
        answer *= (i+1)

    return answer -1
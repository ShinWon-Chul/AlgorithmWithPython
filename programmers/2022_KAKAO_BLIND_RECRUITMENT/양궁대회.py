from itertools import combinations_with_replacement
from collections import Counter
def calc_score_difference(arr1, arr2):
    """
    arr1 : 어피치 사격 결과
    arr2 : 라이언 사격 결과
    """
    a_s = 0 # 어피치 총 점수
    r_s = 0 # 라이언 총 점수
    s = 10
    for i in range(11):
        # 만약 라이언이 더 많은 화살을 맞췄다면
        if arr1[i] < arr2[i]:
            # 라이언에 점수 부여
            r_s += s-i
        # 만약 어피치가 라이언보다 같거나 많은 화살을 맞췄다면
        elif arr1[i] >= arr2[i] and arr1[i] != 0:
            a_s += s-i
    # 만약 라이언 점수가 어피치 점수보다 높다면 라이언 점수 배열 점수차이 리턴
    if r_s > a_s:
        return r_s-a_s
    # 만약 라이언 점수가 어피치 점수와 같거나 낮다면 None return
    else:
        return
    
def solution(n, info):
    max_score_diff = 0
    for comb in combinations_with_replacement(range(11), n):
        cnt = Counter(comb)
        scores = [0]*11
        for s in cnt:
            scores[10-s] = cnt[s]
        score_diff = calc_score_difference(info, scores)
        if score_diff and score_diff > max_score_diff:
            max_score_diff = score_diff
            result = scores
    if max_score_diff == 0:
        return [-1]
    else:
        return result

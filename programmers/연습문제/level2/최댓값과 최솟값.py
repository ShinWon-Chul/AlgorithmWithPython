def solution(s):
    s = s.split(' ')
    s = list(map(lambda x : int(x), s))
    answer = f'{min(s)} {max(s)}'
    return answer
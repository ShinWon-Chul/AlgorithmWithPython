import re
import itertools

def solution(user_id, banned_id):
    n = len(banned_id)
    candidate = []
    for permut in itertools.permutations(user_id, n):
        tmp = []
        for idx, u_id in enumerate(permut):
            match = re.match(banned_id[idx].replace('*', '\w'), u_id)
            if match and match.span()[1] == len(u_id):
                 tmp.append(u_id)
        if len(tmp) == n:
            tmp.sort()
            if tmp not in candidate:
                candidate.append(tmp)

    return len(candidate)
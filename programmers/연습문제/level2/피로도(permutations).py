from itertools import permutations

def solution(k, dungeons):
    answer = -1
    for permut in permutations(dungeons):
        new_k = k
        count = 0
        for dungeon in permut:
            if dungeon[0] <= new_k:
                count += 1
                new_k -= dungeon[1]
        answer = max(answer, count)
    return answer
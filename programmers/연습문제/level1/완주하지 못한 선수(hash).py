from collections import defaultdict

def solution(participant, completion):
    participant_dict = defaultdict(lambda : 0)
    completion_dict = defaultdict(lambda : 0)

    for p in participant:
        participant_dict[p] += 1
    for c in completion:
        completion_dict[c] += 1
    for p in participant:
        if participant_dict[p] - completion_dict[p] != 0:
            return p
    return answer[0]
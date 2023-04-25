from collections import defaultdict

def solution(name, yearning, photo):
    
    answer = []
    dict_ = defaultdict(lambda : 0)
    
    for i in range(len(name)):
        dict_[name[i]] = yearning[i]
        
    for p in photo:
        score = 0
        for n in p:
            score += dict_[n]
        answer.append(score)
        
    return answer
from collections import Counter

def solution(want, number, discount):
    answer = 0
    d = {k: v for k, v in zip(want, number)}

    for i in range(len(discount)):
        temp_arr = discount[i:i+10]
        c = Counter(temp_arr)
        
        for k, v in d.items():
            if c[k] >= d[k]:
                continue
            else:
                break
        else:
            answer += 1
    return answer
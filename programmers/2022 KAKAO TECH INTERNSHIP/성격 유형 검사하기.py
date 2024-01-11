def solution(survey, choices):
    answer = ''
    indicator = {0 : ['R', 'T'], 1 : ['C', 'F'], 2 : ['J', 'M'], 3 : ['A', 'N']}
    score = {1 : 3, 2 : 2, 3 : 1, 4 : 0, 5 : 1, 6 : 2, 7 : 3}
    res = { 'R' : 0, 'T' : 0, 'C' : 0, 'F' : 0, 'J' : 0, 'M' : 0, 'A' : 0, 'N' : 0}
    length = len(survey)
    for i in range(length):
        if choices[i] > 4:
            res[survey[i][1]] += score[choices[i]]
        else:
            res[survey[i][0]] += score[choices[i]]
            
    for _, v in indicator.items():
        if res[v[0]] > res[v[1]]:
            indi = v[0]
        elif res[v[0]] < res[v[1]]:
            indi = v[1]
        else:
            sorted(v)
            indi = v[0]
        answer += indi
    return answer
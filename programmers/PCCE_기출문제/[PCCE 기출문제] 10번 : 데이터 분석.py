def solution(data, ext, val_ext, sort_by):
    answer = []
    dictionary = {'code' : 0, 'date' : 1, 'maximum' : 2, 'remain' : 3}
    
    for d in data:
        code, date, maximum, remain = d
        
        if d[dictionary[ext]] < val_ext:
            answer.append(d)
    answer.sort(key = lambda x : x[dictionary[sort_by]])
    return answer
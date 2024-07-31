def solution(input_string):
    prev_loc = {}
    res = ''
    for i in range(len(input_string)):
        if input_string[i] not in prev_loc:
            prev_loc[input_string[i]] = i
        else:
            if prev_loc[input_string[i]] != i-1:
                if input_string[i] not in res:
                    res+= input_string[i]
            else:
                prev_loc[input_string[i]] = i
    res = list(res)
    res.sort()
    if res:
        return ''.join(res)
    else:
        return 'N'
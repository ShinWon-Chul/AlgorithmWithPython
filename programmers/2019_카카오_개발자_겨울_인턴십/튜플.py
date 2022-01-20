import re

def solution(s):
    n = s.count('{')
    s = re.split('[{},]', s)
    result = []
    arr = [[0] for _ in range(n-1)]
    tmp = []
    for i in s:
        if i.isdigit():
            tmp.append(int(i))
        else:
            if len(tmp) == 0:
                continue
            else:
                arr[len(tmp)-1]= tmp
                tmp = []
    for i in arr:
        for j in i:
            if j not in result:
                result.append(j)
    return result
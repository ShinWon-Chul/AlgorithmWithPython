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

# 다시 풀어본 코드
from collections import Counter
import re
def solution(s):
    temp = []
    arr = re.findall('\d+', s)
    cnt = Counter(arr)
    for n in cnt:
        temp.append([int(n), cnt[n]])
    temp.sort(key = lambda x : x[-1], reverse = True)
    result = list(map(lambda x : x[0], temp))
    return result 
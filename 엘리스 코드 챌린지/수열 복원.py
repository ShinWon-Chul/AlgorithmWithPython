import copy
from itertools import combinations
n = int(input())
# n = 4
sums = list(map(int, input().split(' ')))
# sums = [0, 1, 2, 3, 4, 5, 5, 6, 6, 7, 7, 8, 9, 10, 11, 12]

sums.sort()
# 0포함 앞에 두수는 확정
res = sums[1:3]

while len(res) < n:
    
    tmp_sums = []
    for i in range(1, len(res)+1):
        for c in combinations(res, i):
            tmp_sums.append(sum(c))

    # tmp_sums 조합의 부분합
    tmp_sums.sort()
    
    # 0 제외한 입력값
    copy_sums = copy.deepcopy(sums[1:]) 

    while tmp_sums:
        if tmp_sums[0] == copy_sums[0]:
            copy_sums = copy_sums[1:]
            tmp_sums = tmp_sums[1:]
        elif tmp_sums[0] != copy_sums[0]:
            break
    
    res.append(copy_sums[0])
    

print(' '.join(map(str, res)))
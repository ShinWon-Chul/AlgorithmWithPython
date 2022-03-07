from itertools import product

data = [1,2,3]

#2개를 뽑아 일렬로 나열하는 경우의 수(단, 중복 허용)
for i in product(sets, repeat = 2):
   print(i)

"""
n pi r
n^r
(1, 1)
(1, 2)
(1, 3)
(2, 1)
(2, 2)
(2, 3)
(3, 1)
(3, 2)
(3, 3)
"""
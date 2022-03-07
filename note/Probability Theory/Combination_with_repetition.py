from itertools import combinationswith_replacement

data = [1, 2, 3]

for i in combinations_with_replacement(data, 2):
   print(i)

"""
nHr = n+r-1Cr
(n+r-1)!/(n-1)!r!
(1, 1)
(1, 2)
(1, 3)
(2, 2)
(2, 3)
(3, 3)
"""
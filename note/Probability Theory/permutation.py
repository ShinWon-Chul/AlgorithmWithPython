import itertools

data = [1, 2, 3]
for x in itertools.permutations(data, 2):
    print(list(x))

"""
nPr
n!/(n-r)!
(1, 2)
(1, 3)
(2, 1)
(2, 3)
(3, 1)
(3, 2)
"""
import itertools

data = [1, 2, 3]
for x in itertools.combinations(data, 2):
    print(list(x))

"""
nCr
n!/(n-r)!r!
(1, 2)
(1, 3)
(2, 3)
"""
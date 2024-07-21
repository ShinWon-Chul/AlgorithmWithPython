N, L = map(int, input().split())

for l in range(L, 101):
    # N = l(2x +l-1)/2
    x = (2 * N / l - l + 1) / 2
    if x.is_integer() and x >= 0:
        result = list(range(int(x), int(x) + l))
        break
else:
    result = -1

if result == -1:
    print(result)
else:
    print(" ".join(map(str, result)))
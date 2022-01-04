n, h = map(int, input().split())

down = [0] * (h + 1)  # 석순
up = [0] * (h + 1)  # 종유석
for i in range(n):
    if i%2 == 0:
        down[int(input())] += 1
    else:
        up[int(input())] += 1

for i in range(h-1, 0, -1):
    down[i] += down[i+1]
    up[i] += up[i+1]

min_value = n
min_count = 0

for i in range(1, h+1):
    x = down[i] + up[h-i+1]
    if x < min_value:
        min_count = 1
        min_value = x
    elif x == min_value:
        min_count += 1
print(min_value, min_count)
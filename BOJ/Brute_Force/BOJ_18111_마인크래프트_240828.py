N, M, B = list(map(int, input().split()))
block = [ list(map(int, input().split())) for _ in range(N)]

hight = [h for h in range(256, -1, -1)]
min_time = 1e9
max_hight = 0

# 높이 256부터 0까지 순회, 가장 높은층을 출력해야 하므로
for h in hight:
    time = 0
    inv = B
    for row in block:
        for b in row:
            #기준 높이보다 크다면
            if b > h:
                # 제거하면서 인벤토리에 추가
                i_b = b-h
                inv += i_b
                # 제거하는 시간 추가
                time += i_b * 2
            #기준 높이보다 작다면
            elif b < h:
                # 채워야 하는 블록 수 증가
                c_b = h-b
                inv -= c_b
                # 채우는 시간 증가
                time += c_b
    # 채워야 하는 블록수가 가지고 있는 블록보다 많다면 불가능한 경우
    if inv < 0:
        continue
    else:
        # 시간이 더 적게 걸렸다면
        if min_time > time:
            min_time = time
            max_hight = h

print(min_time, max_hight)
H, W = list(map(int, input().split()))
hight = list(map(int, input().split()))

water = 0
# 물의 높이는 1부터 시작
for h in range(1, H+1):
    wa = 0
    # 가장 왼쪽은 물이 찰 수 없음
    for w in range(1, W):

        # 물이 처음 차기 시작함
        # 이전 위치의 블록이 현재 위치보다 크거나 같고, 현재 위치의 블록이 현재 높이보다 작다면 물이 차기 시작할 수 있음
        if hight[w-1] >= h and hight[w] < h:
            wa += 1

        # 물을 연속으로 채움
        # 물이 차기 시작했고, 현재 위치의 블록이 물의 높이보다 작다면 물이 더 추가될 수 있음
        elif wa > 0 and hight[w] < h:
            wa += 1

        # 현재까지 쌓인 물을 더하고 초기화
        # 현재 위치의 블록이 물의 높이보다 크거나 같다면 여태까지 쌓인 물을 더하고 물을 초기화
        elif hight[w] >= h:
            water += wa
            wa = 0
print(water)
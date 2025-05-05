import heapq

N, H, T = list(map(int, input().split()))

heap = []
count = 0
for _ in range(N):
    heapq.heappush(heap, -int(input()))

for i in range(T):
    hight = -heapq.heappop(heap)

    if hight < H:
        print('YES')
        print(count)
        break
    else:
        if hight == 1:
            count += 1
            heapq.heappush(heap, -1)
        else:
            count += 1
            heapq.heappush(heap, -int(hight/2))
    # print(heap)
else:
    hight = -heapq.heappop(heap)
    if hight < H:
        print('YES')
        print(count)
    else:
        print('NO')
        print(hight)

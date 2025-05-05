import heapq

# N = int(input())
# h = []
# for _ in range(N):
#     num = int(input())
#     if num == 0:
#         if h:
#             digit = heapq.heappop(h)
#             print(-digit)
#         else:
#             print(0)
#     else:
#         heapq.heappush(h, -num)

import sys
input = sys.stdin.readline  # 입력 속도 개선

N = int(input())
h = []
for _ in range(N):
    num = int(input())
    if num:
        heapq.heappush(h, -num)
    else:
        print(-heapq.heappop(h) if h else 0)

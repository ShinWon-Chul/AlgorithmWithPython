import heapq

n = int(input())
heap = []
for i in range(n):
    heapq.heappush(heap, int(input()))

result = 0
while len(heap) != 1:
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    sort = one+two
    result = result + sort
    heapq.heappush(heap, sort)
print(result)
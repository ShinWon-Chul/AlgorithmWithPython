import heapq

def solution(operations):
    new_operations = list(map(lambda x : x.split(' '), operations))
    min_heap = []
    max_heap = []
    for i, num in new_operations:
        if i == 'I':
            heapq.heappush(min_heap, int(num))
            heapq.heappush(max_heap, (-int(num), int(num)))
        elif i == 'D' and len(min_heap) > 0:
            if num == '-1': # 최소값 삭제
                x = heapq.heappop(min_heap)
                max_heap.remove((-x, x))
            else : # 최대값 삭제
                _, x = heapq.heappop(max_heap)
                min_heap.remove(x)
    if len(min_heap) > 0:
        _, max_value = heapq.heappop(max_heap)
        min_vlaue = heapq.heappop(min_heap)
        return [max_value, min_vlaue]
    else:
        return [0,0]

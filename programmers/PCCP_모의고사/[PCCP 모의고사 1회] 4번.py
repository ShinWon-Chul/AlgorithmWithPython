import heapq

def solution(program):
    answer = []
    wait_dict = {i: 0 for i in range(1, 11)}
    
    # 0 점수, 1 호출 시간, 2 실행 시간
    sorted_program = sorted(program, key=lambda x: x[1])
    
    time = sorted_program[0][1]
    min_heap = []
    index = 0
    n = len(sorted_program)
    
    while index < n or min_heap:
        while index < n and sorted_program[index][1] <= time:
            heapq.heappush(min_heap, (sorted_program[index][0], sorted_program[index][1], sorted_program[index][2]))
            index += 1
        
        if min_heap:
            priority, start_time, exec_time = heapq.heappop(min_heap)
            wait_dict[priority] += time - start_time
            time += exec_time
        else:
            if index < n:
                time = sorted_program[index][1]
    
    answer.append(time)
    for i in range(1, 11):
        answer.append(wait_dict[i])
    
    return answer

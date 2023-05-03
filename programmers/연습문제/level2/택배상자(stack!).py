def solution(order):
    answer = 0
    stack = []
    for i in range(len(order)):
        stack.append(i+1)
        # print(stack)
        while stack :
            if stack[-1] == order[answer]:
                stack.pop()
                answer += 1
            else:
                break

    return answer
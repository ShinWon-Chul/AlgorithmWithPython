def solution(n, left, right):
    answer = []
    count = 0
    x = int(left/n)
    y = left%n
    while count < right-left+1:
        answer.append(max(x, y) + 1)
        count += 1
        y += 1
        if y >= n:
            y = 0
            x += 1
    return answer
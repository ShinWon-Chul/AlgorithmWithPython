def solution(k, d):
    answer = 0
    # dist = math.sqrt(pow(abs(0-x),2) + pow(abs(0-y), 2))
    # x 좌표 값을 순회하며
    for x in range(0, d+1, k):
        # y 값이 0인 경우도 고려해야 하기 때문에 1을 더해줘야함
        answer += (pow(d, 2) - pow(x, 2)) ** (1/2) // k + 1
        
    return answer
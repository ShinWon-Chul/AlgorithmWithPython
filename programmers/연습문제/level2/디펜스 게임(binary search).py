def solution(n, k, enemy):
    answer = 0
    start = 1
    end = len(enemy)

    while start <= end:
        mid = int((start + end) / 2)
        
        temp_enemy = enemy[:mid]
        temp_enemy.sort(reverse = True)
        temp_enemy = temp_enemy[k:]
        nenemy = sum(temp_enemy)

        # 크기를 키우는 경우 -> n > 
        # 왜 answer가 위로 와야하는지?, 왜 작거나 같아야 하는지
        if nenemy <= n:
            start = mid + 1
            answer = mid
        else:
            end = mid - 1

    return answer
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

        if nenemy <= n:
            start = mid + 1
            answer = mid
        else:
            end = mid - 1

    return answer
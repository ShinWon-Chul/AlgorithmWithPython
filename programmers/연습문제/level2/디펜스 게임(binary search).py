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

        # 내가 상대할 수 있는 적수보다 적수가 작거나 같다면 라운드를 증가
        # answer가 위로 와야되는 이유는 찾아야 되는 지점이 큰지점이 아니라 작거나 같아야 하므로
        # 적수가 더 많다면 답이 될 수 없기 때문
        if nenemy <= n:
            start = mid + 1
            answer = mid # 
            
        else:
            end = mid - 1

    return answer
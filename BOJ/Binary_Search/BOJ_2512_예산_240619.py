n = int(input())
province = list(map(int, input().split())) 
budget = int(input())

start = 1
end = budget
result = 0

while start <= end:
    remain = budget
    mid = int((start+end)/2)
    
    # 상한선 만큼 예산 할당
    for p in province:
        # 상한액 이하인 경우
        if p <= mid:
            remain -= p

        # 상한액 초과인 경우
        else:
            remain -= mid

    # 남은 예산이 남는경우 시작값을 증가 (부등호 주의)
    if remain >= 0:
        start = mid + 1
    
    # 예산이 남지 않는다면 끝값을 감소
    else:
        result = end
        end = mid - 1

# 정해진 만큼 분배할 수 있는경우
if end == budget: #항상 상한액 이하로 분배가 가능하다면 예산이 항상 남을 것이므로 상한액이 예산과 같아짐
    print(max(province))
else:
    print(end)
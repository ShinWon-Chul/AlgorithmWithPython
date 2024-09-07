N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
#data 정렬
data.sort()
answer = 0

start, end = data[0][0], data[0][1]

for i in range(1, N):
    s, e = data[i]
    
    if end < s:  # 이전 구간과 겹치지 않으면
        answer += end - start  # 누적된 구간 길이를 계산
        start, end = s, e  # 새로운 구간으로 초기화
    else:
        end = max(end, e)  # 겹치는 구간을 합침

# 마지막 구간 계산
answer += end - start

print(answer)
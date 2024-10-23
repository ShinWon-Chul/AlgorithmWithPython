N = int(input())
p = list(map(int, input().split()))
line = [ [] for _ in range(N) ]

# 키가 1인 사람은 반드시 앞에 p[0]만큼 있음
line[p[0]].append(1)

# print(res)
for i in range(2, N+1):
    # 키가 2인 사람부터 검사
    num = p[i-1]
    for j in range(len(line)):
        # line[j]번째에 자리가 비어있다면 + 뒤로 간 횟수 충족
        if  not line[j] and num <= 0:
            break
        # j번쨰에 이미 사람이 있다면
        if line[j]:
            # 나보다 작다면 무시?
            if line[j][0] < i:
                continue
            # 앞에 나보다 큰사람이 있다면 뒤로 가야함
            elif line[j][0] > i:
                num -= 1
        # 앞에 아무도 없다면 자리를 남겨 두어야함
        else:
            num -= 1
    line[j].append(i)
    # print(line)

flattened_list = [item[0] for item in line]

print(' '.join(map(str, flattened_list)))
N = int(input())
p = list(map(int, input().split()))
line = [ [] for _ in range(N) ]
line[p[0]].append(1)

# print(res)
for i in range(2, N+1):
    num = p[i-1]
    for j in range(len(line)):
        if num <= 0 and not line[j]:
            break
        if line[j]:
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

# Flattening the list to remove inner lists
flattened_list = [item[0] for item in line]

print(' '.join(map(str, flattened_list)))
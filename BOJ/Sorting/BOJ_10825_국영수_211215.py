n = int(input())
p = []
for _ in range(n):
    p.append(input().split())
p.sort(key = lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in p:
    print(i[0])
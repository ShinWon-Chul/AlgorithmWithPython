t = int(input())
for _ in range(t):
    n = int(input())

    record = []
    for _ in range(n):
        record.append(list(map(int, input().split())))
    record.sort() #1 

    minrecord = record[0][1]	#2
    count = 1
    for i in range(1, n):
        if record[i][1] < minrecord:
            count += 1
            minrecord = record[i][1]

    print(count)
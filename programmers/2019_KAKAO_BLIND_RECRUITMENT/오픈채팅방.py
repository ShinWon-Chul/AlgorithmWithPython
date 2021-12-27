def solution(record):
    result = []
    info = {}
    for r in record:
        r = r.split()
        #들어온 경우
        if r[0] == "Enter":
            result.append([r[1], "님이 들어왔습니다."])
            info[r[1]] = r[2]
        #나간경우
        elif r[0] == "Leave":
            result.append([r[1], "님이 나갔습니다."])
        #변경된 경우
        else:
            info[r[1]] = r[2]
    result = list(map(lambda x : info[x[0]]+x[1], result))
    return result
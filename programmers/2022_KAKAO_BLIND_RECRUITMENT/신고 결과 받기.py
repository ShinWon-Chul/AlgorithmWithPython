from collections import defaultdict

def solution(id_list, report, k):
    # 제재당한 id를 저장할 리스트
    sanctions = []

    # 이용자가 신고한id를 담을 dictionary초기화
    Declaration = defaultdict(list)
    for id_ in id_list:
        Declaration[id_]

    # 신고id의 신고 횟수를 저장할 dictionary 초기화
    counting = defaultdict(lambda : 0)

    # 이용자와 신고id 분리
    report = list(map(lambda x : x.split(), report))

    # 신고 내용을 하나씩 확인하며 처리
    for x_id, y_id in report:
        # 만약 이용자가 처음 신고한 id라면 count
        if y_id not in Declaration[x_id]:
            Declaration[x_id].append(y_id)
            counting[y_id] += 1

    #신고를 k번 이상 당했다면 제재 아이디 list에 추가
    for key, value in counting.items():
        if value >= k:
            sanctions.append(key)

    #이용자가 신고한 id리스트 중 제재list에 있다면 count하여 결과 list에 저장
    result = []
    for key, value in Declaration.items():
        count = 0
        for id_ in value:
            if id_ in sanctions:
                count += 1
        result.append(count)
    return result
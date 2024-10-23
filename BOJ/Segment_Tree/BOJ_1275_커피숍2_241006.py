import sys
input = sys.stdin.readline

# 0. 입력받기
N, Q = map(int, input().split())
l = list(map(int, input().split()))  # 리스트 입력 받기
segment_tree = [0] * (N * 4)  # 넉넉하게 4배 크기의 세그먼트 트리

# 1. 트리 만들기
def init(start, end, index):
    if start == end:
        segment_tree[index] = l[start - 1]  # l은 0-based 이므로 start - 1
        return segment_tree[index]
    
    mid = (start + end) // 2
    segment_tree[index] = init(start, mid, index * 2) + init(mid + 1, end, index * 2 + 1)
    return segment_tree[index]

# 2. 트리에서 값 찾기 (구간 합 찾기)
def find(start, end, index, left, right):
    if start > right or end < left:  # 범위를 벗어날 경우
        return 0
    
    if start >= left and end <= right:  # 범위 안에 완전히 속할 경우
        return segment_tree[index]

    mid = (start + end) // 2
    return find(start, mid, index * 2, left, right) + find(mid + 1, end, index * 2 + 1, left, right)

# 3. 트리 값 바꿔주기 (업데이트)
def update(start, end, index, update_idx, diff):
    if start > update_idx or end < update_idx:  # 범위를 벗어나면 아무 일도 하지 않음
        return
    
    # 현재 노드의 값을 차이만큼 변경
    segment_tree[index] += diff

    if start == end:  # 리프 노드에 도달하면 종료
        return

    mid = (start + end) // 2
    update(start, mid, index * 2, update_idx, diff)
    update(mid + 1, end, index * 2 + 1, update_idx, diff)

# 초기화
init(1, N, 1)

# 쿼리 처리
for _ in range(Q):
    x, y, a, b = map(int, input().split())
    
    # x, y의 순서가 뒤바뀔 수 있으므로 정렬해서 처리
    left, right = min(x, y), max(x, y)
    
    # 구간 합 출력
    print(find(1, N, 1, left, right))
    
    # a번째 수를 b로 바꾸는 작업 (값을 b로 바꾸고 세그먼트 트리 업데이트)
    diff = b - l[a - 1]  # 값 차이 계산
    l[a - 1] = b  # 실제 배열 값을 변경
    update(1, N, 1, a, diff)  # 세그먼트 트리에서 값 갱신

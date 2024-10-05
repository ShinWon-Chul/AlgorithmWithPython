import sys
input = sys.stdin.read

# 세그먼트 트리를 빌드하는 함수
# arr: 원래 배열, tree: 세그먼트 트리, node: 현재 노드 번호, start: 시작 인덱스, end: 끝 인덱스
# build_tree(arr, tree, 1, 0, N - 1) arr = [1,2,3,4,5] tree = [0, 0, 0, 0, 0, ..., 0] N = 5
def build_tree(arr, tree, node, start, end):
    # 리프 노드: 배열의 한 요소만 가리킬 때 (start == end)
    if start == end:
        tree[node] = arr[start]  # 리프 노드에 배열의 값을 저장
    else:
        mid = (start + end) // 2  # 중간 인덱스를 계산하여 배열을 반으로 나눔
        # 왼쪽 자식 트리 구축 (node * 2: 왼쪽 자식, start부터 mid까지)
        build_tree(arr, tree, 2 * node, start, mid)
        # 오른쪽 자식 트리 구축 (node * 2 + 1: 오른쪽 자식, mid + 1부터 end까지)
        build_tree(arr, tree, 2 * node + 1, mid + 1, end)
        # 현재 노드는 왼쪽 자식과 오른쪽 자식의 합을 저장 (구간 합)
        tree[node] = tree[2 * node] + tree[2 * node + 1]

# 구간 합을 구하는 함수
# L ~ R 범위의 합을 구함
def query(tree, node, start, end, L, R):
    # 구간이 겹치지 않으면 (현재 노드가 구간 밖에 있으면) 0을 반환
    if L > end or R < start:
        return 0
    # 현재 구간이 완전히 [L, R] 범위에 포함되면 노드 값을 반환
    if L <= start and end <= R:
        return tree[node]
    
    # 구간이 일부만 겹칠 경우, 두 자식 노드에서 각각 구간 합을 구함
    mid = (start + end) // 2
    left_sum = query(tree, 2 * node, start, mid, L, R)  # 왼쪽 자식의 구간 합
    right_sum = query(tree, 2 * node + 1, mid + 1, end, L, R)  # 오른쪽 자식의 구간 합
    return left_sum + right_sum  # 두 구간의 합을 반환

# 배열의 값을 업데이트하는 함수
# idx 위치의 값을 value로 업데이트
def update(arr, tree, node, start, end, idx, value):
    # 리프 노드일 때 (start == end)
    if start == end:
        arr[idx] = value  # 배열 값을 업데이트
        tree[node] = value  # 세그먼트 트리의 해당 노드 값도 업데이트
    else:
        mid = (start + end) // 2
        # 왼쪽 자식의 범위에 있으면 왼쪽 자식을 업데이트
        if start <= idx <= mid:
            update(arr, tree, 2 * node, start, mid, idx, value)
        # 오른쪽 자식의 범위에 있으면 오른쪽 자식을 업데이트
        else:
            update(arr, tree, 2 * node + 1, mid + 1, end, idx, value)
        
        # 자식 노드 값이 변경되었으므로, 현재 노드 값도 자식들의 합으로 업데이트
        tree[node] = tree[2 * node] + tree[2 * node + 1]

# 메인 함수: 전체 입력을 처리하고 세그먼트 트리를 사용해 쿼리를 해결
def main():
    # 여러 줄의 입력을 받음
    data = input().splitlines()
    N, Q = map(int, data[0].split())  # 첫 번째 줄에서 N(배열의 크기), Q(쿼리 수)를 읽음
    arr = list(map(int, data[1].split()))  # 두 번째 줄에서 배열의 초기값을 읽음
    queries = [list(map(int, line.split())) for line in data[2:]]  # 각 쿼리를 리스트로 저장

    # 세그먼트 트리 크기는 일반적으로 4 * N으로 잡음 (2 * 2^logN 크기)
    tree = [0] * (4 * N)

    # 세그먼트 트리 초기화 (build_tree를 통해 트리 구축)
    build_tree(arr, tree, 1, 0, N - 1)

    # 각 쿼리를 처리
    result = []
    for q in queries:
        x, y, a, b = q
        # 첫 번째 작업: x~y 구간 합 구하기
        sum_value = query(tree, 1, 0, N - 1, x - 1, y - 1)
        result.append(str(sum_value))
        
        # 두 번째 작업: a번째 수를 b로 변경 (업데이트)
        update(arr, tree, 1, 0, N - 1, a - 1, b)

    # 결과 출력
    sys.stdout.write("\n".join(result) + "\n")

if __name__ == "__main__":
    main()

import sys
sys.setrecursionlimit(10**6)

def postorder(arr):
    # arr이 비어 있다면 return 합니다.
    if not arr:
        return

    root = arr[0]
    length = len(arr)

    for i in range(1, length):
        if arr[i] > root:
            left_tree = arr[1:i]
            right_tree = arr[i:]
            break

    # root보다 큰 값이 없다면 오른쪽 서브 트리는 존재하지 않습니다.
    else:
        left_tree = arr[1:]
        right_tree = []
    postorder(left_tree)
    postorder(right_tree)
    print(root)

def solution():
    preorder = []

    # 입력 받기 (EOF까지)
    for line in sys.stdin:
        line = line.strip()
        if line:
            preorder.append(int(line))

    postorder(preorder)

if __name__ == "__main__":
    solution()
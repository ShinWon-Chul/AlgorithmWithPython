import sys
sys.setrecursionlimit(10**6)

class Node():
    def __init__(self, x, y, item):
        self.x = x
        self.y = y
        self.item = item
        self.left = None
        self.right = None
        
def create_tree(root, x, y, item, tree):
    # y값이 부모보다 작다면
    if tree[root].y > y :
        # x값이 부모보다 작다면 left로 내려가야함
        if tree[root].x > x:
            # 현재 부모가 left에 자식이 없다면
            if tree[root].left == None:
                # 왼쪽 자식이 없다면 자식 추가
                tree[root].left = item
                tree[item] = Node(x, y, item)
                return
            # 현재 부모가 자식이 있다면
            else:
                # 현재 부모의 자식을 다시 부모로 하여 create_tree 다시 호출
                root = tree[root].left
                create_tree(root, x, y, item, tree)

        # x값이 부모보다 크다면 right로 내려가야함
        elif tree[root].x < x:
            # 오른쪽 자식이 없다면 자식 추가
            if tree[root].right == None:
                tree[root].right = item
                tree[item] = Node(x, y, item)
                return
            # 오른쪽 자식이 있다면 현재 자식을 부모로 하여 다시 create_tree 호출
            else:
                root = tree[root].right
                create_tree(root, x, y, item, tree)

# 프리 오더 구현
def preorder(root, tree, result):
    result[0].append(tree[root].item)
    if tree[root].left != None:
        preorder(tree[root].left, tree, result)
    if tree[root].right != None:
        preorder(tree[root].right, tree, result)

# 포스트 오더 구현
def postorder(root, tree, result):
    if tree[root].left != None:
        postorder(tree[root].left, tree, result)
    if tree[root].right != None:
        postorder(tree[root].right, tree, result)
    result[1].append(tree[root].item)
    
def solution(nodeinfo):
    for i, node in enumerate(nodeinfo):
        # 노드 번호 추가
        node.append(i+1)
    # y좌표를 내림차순, x 좌표를 오름차순으로 정렬
    nodeinfo.sort(key = lambda x:(-x[1], x[0]))
    
    
    root_node = nodeinfo[0] # nodeinfo의 첫번째 원소가 루트 노드임
    tree = {}
    tree[root_node[2]] = Node(root_node[0], root_node[1], root_node[2])
    root = root_node[2]

    for x, y, num in nodeinfo[1:]:
        create_tree(root, x, y, num, tree)

    result = [[]for _ in range(2)]
    preorder(root_node[2], tree, result)
    postorder(root_node[2], tree, result)
    
    return result
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
    if tree[root].y > y :
        if tree[root].x > x:
            if tree[root].left == None:
                tree[root].left = item
                tree[item] = Node(x, y, item)
                return
            else:
                root = tree[root].left
                create_tree(root, x, y, item, tree)

        elif tree[root].x < x:
            if tree[root].right == None:
                tree[root].right = item
                tree[item] = Node(x, y, item)
                return
            else:
                root = tree[root].right
                create_tree(root, x, y, item, tree)
    else:
        root = tree[root].left
        create_tree(root, x, y, item, tree)
        root = tree[root].right
        create_tree(root, x, y, item, tree)
        
def preorder(root, tree, result):
    result[0].append(tree[root].item)
    if tree[root].left != None:
        preorder(tree[root].left, tree, result)
    if tree[root].right != None:
        preorder(tree[root].right, tree, result)
        
def postorder(root, tree, result):
    if tree[root].left != None:
        postorder(tree[root].left, tree, result)
    if tree[root].right != None:
        postorder(tree[root].right, tree, result)
    result[1].append(tree[root].item)
    
def solution(nodeinfo):
    for i, node in enumerate(nodeinfo):
        node.append(i+1) 
    nodeinfo.sort(key = lambda x:(-x[1], x[0]))

    root_node = nodeinfo[0]
    tree = {}
    tree[root_node[2]] = Node(root_node[0], root_node[1], root_node[2])
    root = root_node[2]

    for x, y, num in nodeinfo[1:]:
        create_tree(root, x, y, num, tree)

    result = [[]for _ in range(2)]
    preorder(root_node[2], tree, result)
    postorder(root_node[2], tree, result)
    
    return result
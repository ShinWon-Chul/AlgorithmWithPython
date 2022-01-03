class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}

class Trie:
    # 초기화 해드를 빈 노드로 설정
    def __init__(self):
        self.head = Node(None)

    # insert함수 - 트리를 생성하기 위한 함수
    def insert(self, food):
        # head노드부터 시작
        current_node = self.head
        
        # 배열의 음식을 하나씩 확인
        for char in food:
            # 현재 노드의 자식중에 음식이 없다면
            if char not in current_node.children:
                # 자식 노드 추가 및 출력
                current_node.children[char] = Node(char)
                print(char)
            # 자식 중에 음식이 있다면 current_node를 자식 노드로 변경
            current_node = current_node.children[char]

n = int(input())
foods = []
for _ in range(n):
    x = input().split()[1:]
    foods.append(x)

#사전순으로 출력하기위한 정렬
foods.sort()
for food in foods:
    p = '--'
    layer = ''
    for idx, f in enumerate(food):
        food[idx] = layer+f
        layer += p
        
trie = Trie()
for food in foods:
    trie.insert(food)
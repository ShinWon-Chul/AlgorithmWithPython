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
    def insert(self, string):
        # head노드부터 시작
        current_node = self.head
        if current_node.data:
            return False
        # 문자열의 문자를 하나씩 확인
        for char in string:
            # 현재 노드의 자식중에 문자가 없다면
            if char not in current_node.children:
                # 자식 노드 추가
                current_node.children[char] = Node(char)
            # current_node를 자식 노드로 변경
            current_node = current_node.children[char]
            if current_node.data:
                return False

        
        # 문자열을 끝까지 탐색했다면 마지막 노드에 data추가
        current_node.data = string
        return True
    
t = int(input())
for _ in range(t):
    n = int(input())
    phone_numbers = []
    for _ in range(n):
        phone_numbers.append(input())    
    phone_numbers.sort()
    result = "YES"

    trie = Trie()
    for number in phone_numbers:
        if not trie.insert(number):
            result = "NO"
            break
    print(result)
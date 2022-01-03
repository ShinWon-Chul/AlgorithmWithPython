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
        
        # 문자열의 문자를 하나씩 확인
        for char in string:
            # 현재 노드의 자식중에 문자가 없다면
            if char not in current_node.children:
                # 자식 노드 추가
                current_node.children[char] = Node(char)
            # 자식 중에 문자가 있다면 current_node를 자식 노드로 변경
            current_node = current_node.children[char]
        
        # 문자열을 끝까지 탐색했다면 마지막 노드에 data추가
        current_node.data = string
    
    # Trie에서 string이 있는지 찾는 함수
    def search(self, string):
        # head노드부터 시작
        current_node = self.head
        
        #문자열의 문자를 하나씩 확인
        for char in string:
            # 만약 현재 노드의 자식노드중 문자에 해당하는 노드가 존재한다면
            if char in current_node.children:
                # current_node를 자식 노드로 변경
                current_node = current_node.children[char]
            # 현재 노드의 자식노드중 문자에 해당하는 노드가 없다면
            else:
                return False
        # 문자열 끝까지 탐색하여 마지막 노드에 데이터가 존재한다면
        if current_node.data:
            return True
        # 문자열 끝까지 탐색하여 마지막 노드에 데이터가 없다면
        else:
            return False
    
n, m = map(int, input().split())
s = []
string_set = []
for _ in range(n):
    s.append(input())
for _ in range(m):
    string_set.append(input())

trie = Trie()
for string in s:
    trie.insert(string)

count = 0
for string in string_set:
    if trie.search(string):
        count += 1
print(count)   
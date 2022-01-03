"""트라이 자료구조 구현"""
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

    # BFS 방식으로 깊이를 늘려가며 prefix로 시작하는 문자열을 저장한 배열 반환
    def starts_with(self, prefix):
        # head 노드부터 시작
        current_node = self.head
        #prefix로 시작하는 문자열을 저장할 리스트
        words = []

        # prefix의 처음부터 마지막까지 탐색
        for p in prefix:
            # 만약 현재 노드의 자식노드중 문자에 해당하는 노드가 존재한다면
            if p in current_node.children:
                # current_node를 자식 노드로 변경
                current_node = current_node.children[p]
            # 현재 노드의 자식노드중 문자에 해당하는 노드가 없다면 
            else:
                return None

        # prefix의 마지막 노드
        current_node = [current_node]
        # 다음 노드를 저장할 배열
        next_node = []
        while True:
            #현재 노드부터 탐색
            for node in current_node:
                #만약에 데이터가 있다면
                if node.data:
                    #word 배열에 추가
                    words.append(node.data)
                # 현재 노드의 자식 노드 전부를 next_node 배열에 추가
                # list extend 와 expend 정리
                next_node.extend(list(node.children.values()))
            
            # 만약 다음 노드가 존재한다면
            if len(next_node) != 0:
                # 다음 노드들을 현재 노드로 변경
                current_node = next_node
                #next_node는 다시 비워준다
                next_node = []
            # 다음 노드가 없다면 종료
            else:
                break

        return words

trie = Trie()
word_list = ["frodo", "front", "firefox", "fire"]
for word in word_list:
    trie.insert(word)
print(trie.starts_with("fr"))
print(trie.search("frodo"))
# 링크드 리스트 node 구현
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# 링크드 리스트에 데이터 추가
def add(data):
    node = head
    while node.next:
        node = node.next
    node.next = Node(data)   # 추가된 data를 연결된 다음 node에 추가


node1 = Node(1)     # data=1인 node 생성
node2 = Node(2)     # data=2인 node 생성
node1.next = node2      # node1 -> node2
head = node1
for index in range(3, 15):
    add(index)  # index를 데이터로 가지는 node 생성(add)
node = head
while node.next:
    print(node.data)
    node = node.next
print(node)


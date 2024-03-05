class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    # len()사용 시 연결 리스트의 길이 반환
    def __len__(self):
        return self.length

    def appendleft(self, data):
        # head가 존재하지 않을 때, 노드 생성 후 head 지정
        if self.head is None:
            self.head = Node(data)
        # head가 존재할 때, 새로운 노드 생성 후 연결 및 head로 지정
        else:
            node = Node(data)
            node.next = self.head
            self.head = node
        self.length += 1

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = Node(data)
        self.length += 1

    def __str__(self):
        if self.head is None:
            return 'Linked list is empty.'
        res = 'Head'
        node = self.head
        while node is not None:
            res += ' -> ' + str(node.data)
            node = node.next
        return res

    def __contains__(self, target):
        if self.head is None:
            return False
        node = self.head
        while node is not None:
            if node.data == target:
                return True
            node = node.next
        return False

    def popleft(self):
        if self.head is None:
            return None
        node = self.head
        self.head = self.head.next
        self.length -= 1
        return node.data

    def pop(self):
        if self.head is None:
            return None
        # self.head는 건드리는 것 아님
        node = self.head
        while node.next is not None:
            prev = node
            node = node.next
        if node == self.head:
            self.head = None
        else:
            # 다음 노드 끊기
            prev.next = None
        self.length -= 1
        return node.data

    def remove(self, target):
        node = self.head
        while node is not None and node.data != target:
            prev = node
            node = node.next
        if node is None:
            return False
        # head가 target일 경우
        if node == self.head:
            # head를 날려버림
            self.head = self.head.next
        # head가 target이 아닐 경우
        else:
            # prev - node - node.next 를
            # prev - node.next 변경
            prev.next = node.next
        self.length -= 1
        return True

    def insert(self, i, data):
        if i <= 0:
            self.appendleft(data)
        elif i >= self.length:
            self.append(data)
        else:
            node = self.head
            # 인덱스 범위 설정 유의하기
            for _ in range(i-1):
                node = node.next
            new_node = Node(data)
            new_node.next = node.next
            node.next = new_node
            self.length += 1

    def reverse(self):
        if self.length < 2:
            return
        prev = None
        ahead = self.head.next
        while ahead:
            self.head.next = prev
            prev = self.head
            self.head = ahead
            ahead = ahead.next
        self.head.next = prev


if __name__ == "__main__":
    my_list = LinkedList()
    for i in range(10):
        my_list.append(i)
    print(f'연결 리스트의 상태\n연결 리스트의 길이 = {len(my_list)}, {my_list}')
    print()
    my_list.reverse()
    print(f'연결 리스트를 뒤집은 후\n연결 리스트의 길이 = {len(my_list)}, {my_list}')
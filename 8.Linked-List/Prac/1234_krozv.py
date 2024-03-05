# 비밀번호
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def __len__(self):
        return self.length

    def __str__(self):
        if self.head is None:
            return 'Linked list is empty.'
        res = 'Head'
        node = self.head
        while node is not None:
            res += ' -> ' + str(node.data)
            node = node.next
        return res

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = Node(data)
        self.length += 1

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

import sys
sys.stdin = open('input.txt', 'r')
T = 1
for t in range(1, T+1):
    N, num_list = input().split()
    lst = LinkedList()
    head = None
    node = head
    # 연결리스트로 저장
    for num in num_list:
        if head is None:
            head = Node(num)
            node = head
        else:
            node.next = Node(num)
            node = node.next
    last = None
    while not last:

        node = head
        prev = None
        while node.next:
            k = head
            # print(node.data)
            if node.data == node.next.data:
                if prev and node.next.next:
                    print(1)
                    # node = node.next
                    node = node.next.next
                    # print(node.data)
                    prev.next = node
                # node.next.next가 없을 때
                elif prev and not node.next.next:
                    print(2)
                    prev.next = None
                    break
                # prev가 없을때(처음 시작하자마자 동일값인 경우)
                elif node.next.next:
                    print(3)
                    head = node.next.next
                    node = head
                    # 여기 수정해야함
            else:
                prev = node
                node = node.next
            res = 'Head'
            while k is not None:
                res += ' -> ' + str(k.data)
                k = k.next
            print(res)
            print(node.data)
            if not node.next:
                print('test')
    print(f'#{t}', end=' ')
    while head:
        print(head.data, end='')
        head = head.next
    print()
    # print(head)

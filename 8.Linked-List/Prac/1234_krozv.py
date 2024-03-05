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
    for num in num_list:
        if head is None:
            head = Node(num)
            node = head
        else:
            if node.data == num:
                node = prev
                prev =


            else:
                node.next = Node(num)
                prev = node
                node = node.next


            # print(head.data)
        # print(head, head.data)
        # node = node.next
    print(lst)

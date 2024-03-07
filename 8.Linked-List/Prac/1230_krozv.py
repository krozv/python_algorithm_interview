# 암호문
"""
0 ~ 999999 암호문 N개 모아 놓은 암호문 뭉치
3개의 명령어
I x, y, s: 앞에서부터 x번째 암호문 바로 다음에 y개의 암호문 삽입. s는 덧붙일 암호문
D x, y: 앞에서부터 x번째 암호문 바로 다음부터 y개의 암호문 삭제
A y, s:
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

import sys
sys.stdin = open('input.txt', 'r')
from collections import deque
T = 10
for t in range(1, T+1):
    N = int(input())    # 원본 암호문 뭉치 속 암호문의 개수 N
    arr = list(map(int, input().split()))    # 원본 암호문 뭉치
    M = int(input())    # 명령어의 개수 250<=M<=500
    command = deque(input().split())   # 명령어
    head = Node(arr[0])
    node = head
    for i in range(1, N):
        node.next = Node(arr[i])
        node = node.next

    for i in range(M):
        c = int(command.popleft())
        prev = None
        node = head
        if c == 'I':
            # x번째 암호문 바로 다음에 y개의 암호문 삽입
            x = int(command.popleft())
            for _ in range(x):
                prev, node = node, node.next
            y = int(command.popleft())
            for _ in range(y):
                if prev is None:

                new_node = Node(y)
                prev.next = new_node
                new_node.next = node
                prev = prev.next
                node = node.next




        elif c == 'D':
        elif c == 'A':

    while head:
        if head.next is None:
            print(head.data)
        else:
            print(head.data, end=' -> ')
        head = head.next
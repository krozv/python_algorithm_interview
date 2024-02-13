# Palindrome Linked List
"""
연결리스트를 활용하여 팰린드롬 판단하기
방향성
1. 연결리스트를 생성
2. range(0, N//2)까지의 연결 리스트를 가져옴
    2-1. N = 짝수
        node == next.node일 경우 둘다 삭제
        연결리스트가 존재하지 않으면 팰린드롬
    2-2. N = 홀수
        N//2번째 node는 그냥 삭제
        node == next.node일 경우 둘 다 삭제
        연결리스트가 존재하지 않으면 팰린드롬
"""
from typing import Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        node = head
        while node.next:
            node = node.next
        node.next = Node(data)


linked_list = ListNode()
linked_list.next
c = Solution()
test = [1, 2, 2, 1]
c.isPalindrome(test)
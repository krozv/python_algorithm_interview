"""
연결리스트를 뒤집어서 출력
list range 0 ~ 5000
"""
from typing import Optional
# 연결리스트 클래스 생성
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next
        return prev



l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)
l1.next.next.next.next = ListNode(5)

s = Solution()
l2 = ListNode()
result = s.reverseList(l1)
while result:
    print(result.val, end=' ')
    result = result.next
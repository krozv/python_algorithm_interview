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
        tail = None
        if head:
            t = head.val
            if not head.next:
                tail = head.val
            self.reverseList(head.next)
            l2 = ListNode(t)
            if l2 and tail and l2.val == tail:
                return l2
            l2 = l2.next
        return l2




# head = [1, 2, 3, 4, 5]
# # 리스트 head를 연결리스트로 변경
# lst = ListNode(head[0])
# head.pop(0)
# print(lst.val)
# while head:
#     lst.next = ListNode(head[0])
#     head.pop(0)
#     # print(lst.next.val)
#     lst = lst.next

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
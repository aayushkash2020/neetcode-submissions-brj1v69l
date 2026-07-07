# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next or not head.next.next:
            return
        tmp = head.next
        last = head
        prev = None
        while last.next:
            prev, last = last, last.next
        head.next = last
        last.next = tmp
        prev.next = None
        self.reorderList(tmp)
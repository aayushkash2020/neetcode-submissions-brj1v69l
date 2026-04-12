# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # def helper(self, list1, list2, front, back):
    #     if not list1 and not list2:
    #         return front
    #     if not list1:
    #         back.next = list2
    #         return self.helper(list1, list2.next, front, back.next)
    #     if not list2:
    #         back.next = list1
    #         return self.helper(list1.next, list2, front, back.next)
    #     if list1.val < list2.val:
    #         back.next = list1
    #         return self.helper(list1.next, list2, front, back.next)
    #     back.next = list2
    #     return self.helper(list1, list2.next, front, back.next)

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # front = ListNode()
        # back = ListNode()
        # front.next = back
        # return self.helper(list1, list2, front, back).next.next

        head = ListNode()
        tail = head
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        while list1:
            tail.next = list1
            tail = tail.next
            list1 = list1.next
        while list2:
            tail.next = list2
            tail = tail.next
            list2 = list2.next
        return head.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        total_els = 0
        temp_head = head
        while temp_head:
            total_els += 1
            temp_head = temp_head.next

        if total_els == 1:
            return ListNode(val=None).next
        
        n = total_els - n

        dummy = ListNode(0, head)
        l, r = None, dummy
        for _ in range(n + 1):
            l, r = r, r.next

        l.next = r.next
        return dummy.next   
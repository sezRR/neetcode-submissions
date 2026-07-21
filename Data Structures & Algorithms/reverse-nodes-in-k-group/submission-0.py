# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        connector = dummy
        h_copy = head
        l_prev, l = None, head
        while h_copy:
            r = 0
            while r != k and h_copy:
                r += 1
                h_copy = h_copy.next

            if r != k:
                break

            l_head = l
            while l is not h_copy:
                temp = l.next
                l.next = l_prev
                l_prev = l
                l = temp
            else:
                connector.next = l_prev
                connector = l_head
                l_head.next = h_copy
        return dummy.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # center
        s, f = head, head.next
        while f and f.next:
            s = s.next
            f = f.next.next

        # reverse
        rev_r = s.next
        rev_l = s.next = None
        while rev_r:
            temp = rev_r.next
            rev_r.next = rev_l
            rev_l, rev_r = rev_r, temp

        # merge
        l, r = head, rev_l
        while r:
            temp_l, temp_r = l.next, r.next
            l.next = r
            r.next = temp_l
            l, r = temp_l, temp_r 

        
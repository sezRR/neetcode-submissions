# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l, r = list1, list2
        merged = ListNode(None, None)
        result = merged
        while l and r:
            if l.val > r.val:
                merged.next = ListNode(r.val)
                r = r.next
            else:
                merged.next = ListNode(l.val)
                l = l.next
            merged = merged.next

        merged.next = l or r
        
        return result.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        res = dummy
        carry = 0
        while l1 and l2:
            sum = (l1.val) + (l2.val)
            res.next = ListNode((sum % 10) + carry)
            res = res.next
            carry = sum // 10

            l1 = l1.next
            l2 = l2.next

        while l1:
            sum_carry = (l1.val % 10) + carry
            res.next = ListNode(sum_carry % 10)
            carry = sum_carry // 10
            res = res.next
            l1 = l1.next

        while l2:
            sum_carry = (l2.val % 10) + carry
            res.next = ListNode(sum_carry % 10)
            carry = sum_carry // 10
            res = res.next
            l2 = l2.next

        if carry:
            res.next = ListNode(carry)
        
        return dummy.next
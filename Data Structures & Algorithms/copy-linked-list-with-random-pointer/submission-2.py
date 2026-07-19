"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        ref = {None: None}

        curr = head
        while curr:
            copy_curr = Node(curr.val)
            ref[curr] = copy_curr
            curr = curr.next

        curr = head
        while curr:
            copy_curr = ref[curr]
            copy_curr.next = ref[curr.next]
            copy_curr.random = ref[curr.random]
            curr = curr.next

        return ref[head]

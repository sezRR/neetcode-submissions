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
        stack = [] # format: (node_val, node_desired_random)
        node_ref_cache = dict()

        dummy = Node(0)
        res = dummy

        curr = head
        while curr:
            stack.append((curr, curr.random if curr.random else None))

            new_node = Node(curr.val)
            node_ref_cache[curr] = new_node

            res.next = new_node
            res = res.next

            curr = curr.next

        while stack:
            node, rand = stack.pop()
            node_ref_cache[node].random = node_ref_cache[rand] if rand else None

        return dummy.next
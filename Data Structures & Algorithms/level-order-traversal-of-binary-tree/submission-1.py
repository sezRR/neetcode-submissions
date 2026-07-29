# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = deque()
        queue.append((0, root))
        while queue:
            (i, node) = queue.popleft()
            if not node:
                continue

            if i >= len(res):
                res.append([])
            res[i].append(node.val)

            i += 1
            queue.append((i, node.left))
            queue.append((i, node.right))
        return res
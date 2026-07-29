# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        stack = [(0, root)] # (i, val)
        while stack:
            (i, node) = stack.pop(0)
            if not node:
                continue

            if i >= len(res):
                res.append([])
            res[i].append(node.val)

            i += 1
            stack.append((i, node.left))
            stack.append((i, node.right))
        return res
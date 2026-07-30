# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:        
        def dfs(node, max) -> int:
            if not node:
                return 0

            count = 0
            if node.val >= max:
                max = node.val
                count = 1
            return dfs(node.left, max) + dfs(node.right, max) + count

        return dfs(root, root.val)
        

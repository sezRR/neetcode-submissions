# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_val = 0

        def dfs(node):
            nonlocal max_val
            if not node:
                return 0

            l = dfs(node.left)
            r = dfs(node.right)
            max_val = max(max_val, l + r)
            return max(l, r) + 1
            
        dfs(root)
        return max_val
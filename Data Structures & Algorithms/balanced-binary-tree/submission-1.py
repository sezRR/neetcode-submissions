# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        max_diff = 0

        def dfs(node):
            nonlocal max_diff
            if not node:
                return 0

            l = dfs(node.left)
            r = dfs(node.right)
            max_diff = max(max_diff, abs(l - r))
            if max_diff > 1:
                return -1

            return max(l, r) + 1


        return True if dfs(root) != -1 else False
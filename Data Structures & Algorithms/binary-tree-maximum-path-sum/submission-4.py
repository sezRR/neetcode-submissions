# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float("-inf")
        def dfs(node):
            if not node:
                return 0

            nonlocal max_sum

            l = max(dfs(node.left), 0)
            r = max(dfs(node.right), 0)

            max_sum = max(max_sum, l + r + node.val)

            return max(l, r) + node.val

        dfs(root)
        return max_sum
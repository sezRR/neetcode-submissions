# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res_cache = []
        q = deque()
        q.append((0, root))
        while q:
            (i, node) = q.popleft()
            if not node:
                continue

            if i >= len(res_cache):
                res_cache.append([])
            res_cache[i].append(node.val)

            i += 1
            q.append((i, node.left))
            q.append((i, node.right))

        res = []
        for val in res_cache:
            res.append(val[-1])
        return res
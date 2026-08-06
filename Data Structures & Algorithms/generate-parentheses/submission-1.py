class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(opened, closed, path):
            if opened == closed == n:
                res.append("".join(path[:]))
                return

            if opened < n:
                path.append("(")
                backtrack(opened + 1, closed, path)
                path.pop()

            if closed < opened:
                path.append(")")
                backtrack(opened, closed + 1, path)
                path.pop()

        backtrack(0, 0, [])
        return res
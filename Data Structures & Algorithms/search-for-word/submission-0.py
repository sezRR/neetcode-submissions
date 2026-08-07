class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        def dfs(m, n, i):
            if i == len(word):
                return True

            if 0 > m or 0 > n or m >= len(board) or n >= len(board[0]) or (m, n) in visited or board[m][n] != word[i]:
                return False

            visited.add((m, n))
            result = (dfs(m + 1, n, i + 1) or
                        dfs(m - 1, n, i + 1) or
                        dfs(m, n + 1, i + 1) or
                        dfs(m, n - 1, i + 1))
            visited.remove((m, n))
            return result
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True

        return False
            
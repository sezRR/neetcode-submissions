class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_l = len(matrix)
        col_l = len(matrix[0])
        row_i = 0
        l, r = 0, col_l - 1
        while l <= r and row_i < row_l:
            if target > matrix[row_i][-1]:
                row_i += 1
            else:
                m = (l + r) // 2
                if matrix[row_i][m] == target:
                    return True
                elif matrix[row_i][m] > target:
                    r = m - 1
                else:
                    l = m + 1
        return False
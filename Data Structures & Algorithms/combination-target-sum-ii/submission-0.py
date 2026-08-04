class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []
        def backtrack(i, curr_sum, path):
            if curr_sum == target:
                res.append(path[:])
                return
            if i >= len(candidates) or curr_sum > target:
                return

            path.append(candidates[i])
            backtrack(i + 1, curr_sum + candidates[i], path)

            path.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            backtrack(i + 1, curr_sum, path)

        backtrack(0, 0, [])
        return res
            
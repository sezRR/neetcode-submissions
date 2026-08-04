class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []
        def backtrack(i, curr_sum, path):
            if curr_sum == 0:
                res.append(path[:])
                return
            if i >= len(candidates) or candidates[i] > curr_sum:
                return

            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue

                path.append(candidates[j])
                backtrack(j + 1, curr_sum - candidates[j], path)
                path.pop()

        backtrack(0, target, [])
        return res
            
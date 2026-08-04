class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(i, curr_sum, path):
            if curr_sum == target:
                res.append(path[:])
                return
            if i >= len(nums) or curr_sum > target:
                return

            path.append(nums[i])
            backtrack(i, curr_sum + nums[i], path)

            path.pop()

            backtrack(i + 1, curr_sum, path)

        backtrack(0, 0, [])
        return res
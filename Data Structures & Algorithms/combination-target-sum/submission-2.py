class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        def backtrack(i, curr_sum, path):
            if curr_sum == 0:
                res.append(path[:])
                return

            for j in range(i, len(nums)):
                if nums[j] > curr_sum:
                    break
                    
                path.append(nums[j])
                backtrack(j, curr_sum - nums[j], path)
                path.pop()

        backtrack(0, target, [])
        return res
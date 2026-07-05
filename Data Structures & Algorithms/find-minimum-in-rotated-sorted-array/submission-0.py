class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_val = float("inf")
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            min_val = min(min_val, nums[m])
            if nums[m] > nums[l]:
                min_val = min(min_val, nums[l])
                l = m + 1
            else:
                min_val = min(min_val, nums[r])
                r = m - 1
        return min_val
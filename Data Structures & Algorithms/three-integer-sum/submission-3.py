class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_sorted = sorted(nums)
        arr_len = len(nums_sorted)
        res = []
        for i in range(arr_len):
            if i > 0 and nums_sorted[i] == nums_sorted[i - 1]:
                continue

            l, r = i + 1, arr_len - 1
            while l < r:
                temp = nums_sorted[l] + nums_sorted[r] + nums_sorted[i]
                if temp == 0:
                    res.append([nums_sorted[i], nums_sorted[l], nums_sorted[r]])
                    l += 1
                    while nums_sorted[l] == nums_sorted[l - 1] and l < r:
                        l += 1
                elif temp > 0:
                    r -= 1
                else:
                    l += 1
        return res

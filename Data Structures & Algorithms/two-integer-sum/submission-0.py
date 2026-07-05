class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        needs = {}
        for i in range(len(nums)):
            need = target - nums[i]
            if need in needs:
                return [needs[need], i]
            needs[nums[i]] = i
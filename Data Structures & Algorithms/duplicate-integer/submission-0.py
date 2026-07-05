class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        c = set()
        for num in nums:
            if num in c:
                return True
            c.add(num)
        return False
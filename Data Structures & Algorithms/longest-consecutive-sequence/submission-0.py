class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        maxlen = 0
        for number in numbers:
            if number - 1 not in numbers:
                templen = 1
                while number + 1 in numbers:
                    templen += 1
                    number += 1
                maxlen = max(maxlen, templen)
        return maxlen
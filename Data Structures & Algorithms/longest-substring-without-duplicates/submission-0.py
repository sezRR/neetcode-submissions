class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c = set()
        max_sub = 0
        l = 0
        for r in range(len(s)):
            while s[r] in c:
                c.remove(s[l])
                l += 1
            c.add(s[r])
            max_sub = max(max_sub, r - l + 1)
        return max_sub
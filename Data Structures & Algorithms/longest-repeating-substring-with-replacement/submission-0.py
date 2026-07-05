class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        c = {}
        res = 0
        max_freq = 0
        for r in range(len(s)):
            c[s[r]] = c.get(s[r], 0) + 1
            max_freq = max(max_freq, c[s[r]])
            if (r - l + 1) - max_freq > k:
                c[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res